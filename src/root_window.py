from PySide6.QtGui import QColor
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QMainWindow,
    QListWidgetItem,
    QTableWidgetItem,
    QAbstractItemView,
    )
from loguru import logger

from ui.main_win import Ui_MainWindow
from ui.card_dev import CardDeviceASH, CardDeviceMB
from utilites.setup import (
    NumbersIPValidator,
    PortValidator,
    SNEmulatorValidator,
    get_ports_info,
    check_join_table_output,
    save_conn_to_file,
    check_file,
    get_conn_from_file,
    save_config_to_file,
    get_config_from_file
)
from utilites.database import (
    get_net_devices_from_db,
    handler_devices,
    check_conn,
)
from utilites.boot_firmware import (
    get_data_from_file,
    boot_firmware,
    )
from utilites.server_mb import ServerMB
from utilites.server_ash import ServerAH
from utilites.dialogues import (
    err_selection,
    ok_connect,
    err_connect,
    err_selection_port_net_dev,
    open_file,
    error_update,
    error_add_sensor
)
from ui.button_states import StatesBtn


logger.add("file_root_w.log", rotation="1 week")


class MainWindow(QMainWindow):
    def __init__(self):
        self.servers = []
        super().__init__()
        self.ports = []
        self.net_devices = []
        self.ports_net_devs = []
        self.ui = Ui_MainWindow()
        self.btns = StatesBtn()
        self.ui.setupUi(self)
        self.setWindowTitle('Эмулятор адресных устройств и устройств Modbus работающих с ПО "Индигирка"')
        check_file()
        self._set_parameters()
        self.ui.check_db_btn.clicked.connect(self._check_connect)
        self.ui.start_emulator_btn.clicked.connect(self._start_servers)
        self.ui.get_ports_btn.clicked.connect(self._output_ports)
        self.ui.get_net_dev_btn.clicked.connect(self._output_net_devices)
        self.ui.join_btn.clicked.connect(self._join_port_and_net_device)
        self.ui.save_db_btn.clicked.connect(self._save_params_conn)
        self.ui.save_config_btn.clicked.connect(self._save_config)
        self.ui.download_config_btn.clicked.connect(self._download_config)
        self.ui.delete_line_btn.clicked.connect(self._delete_line)
        self.ui.update_firmware_btn.clicked.connect(self._update_firmware)
        self.ui.file_selection_btn.clicked.connect(self._file_selection)
        self.ui.port_emul_btn.clicked.connect(self._view_port_ufw)

        self.ui.host_db_lineEdit.setValidator(NumbersIPValidator())
        self.ui.port_db_lineEdit.setValidator(PortValidator())
        self.ui.sn_emulator_lineEdit.setValidator(SNEmulatorValidator())
        self.ui.sn_skau_lineEdit.setValidator(SNEmulatorValidator())

        self.ui.ash_devices_tableWidget.clicked.connect(self.change_state)
        self.ui.mb_devices_tableWidget.clicked.connect(self.change_state_mb)

        self.ui.ash_out_net_dev_listWidget.clicked.connect(self._fill_table_ash)
        self.ui.mb_out_net_dev_listWidget.clicked.connect(self._fill_table_mb)
        self.ui.tabWidget.setCurrentWidget(self.ui.settings_tab)

    def _set_parameters(self):
        params_conn = get_conn_from_file()
        self.ui.host_db_lineEdit.setText(params_conn["host"])
        self.ui.port_db_lineEdit.setText(params_conn["port"])
        self.ui.user_db_lineEdit.setText(params_conn["user"])
        self.ui.pass_db_lineEdit.setText(params_conn["password"])
        self.ui.name_db_lineEdit.setText(params_conn["name"])
        self.ui.sn_emulator_lineEdit.setText("641")
        self.ui.loading_progressBar.setValue(0)
        for speed in ["9600", "19200", "115200"]:
            self.ui.speed_485_comboBox.addItem(speed)
        self.ui.speed_485_comboBox.setCurrentText("19200")

    def _set_btn_md(self):
        norma_btn = self.btns.btn_norma(self)
        activation_btn = self.btns.activation_fire(self)
        malfunction = self.btns.btn_error_mb(self)
        self.ui.mb_h_top_state_dev_layout.addWidget(norma_btn)
        self.ui.mb_h_top_state_dev_layout.addWidget(activation_btn)
        self.ui.mb_h_center_state_dev_layout.addWidget(malfunction)
        norma_btn.clicked.connect(self._norma_state_mb)
        activation_btn.clicked.connect(self._activation_state_mb)
        malfunction.clicked.connect(self._malfunction_state_mb)

    def _set_btn_mip_md(self):
        norma_btn = self.btns.btn_norma(self)
        activation_1_btn = self.btns.activation_fire(self, 101)
        activation_2_btn = self.btns.activation_fire(self, 102)
        activation_3_btn = self.btns.activation_fire(self, 103)
        malfunction_1_btn = self.btns.btn_error_mb(self, 121)
        malfunction_2_btn = self.btns.btn_error_mb(self, 122)
        malfunction_3_btn = self.btns.btn_error_mb(self, 123)

        self.ui.mb_h_top_state_dev_layout.addWidget(norma_btn)
        self.ui.mb_h_top_state_dev_layout.addWidget(activation_1_btn)
        self.ui.mb_h_top_state_dev_layout.addWidget(activation_2_btn)
        self.ui.mb_h_top_state_dev_layout.addWidget(activation_3_btn)
        self.ui.mb_h_center_state_dev_layout.addWidget(malfunction_1_btn)
        self.ui.mb_h_center_state_dev_layout.addWidget(malfunction_2_btn)
        self.ui.mb_h_center_state_dev_layout.addWidget(malfunction_3_btn)

        norma_btn.clicked.connect(self._norma_state_mb)
        activation_1_btn.clicked.connect(lambda: self._activation_state_mb(101))
        activation_2_btn.clicked.connect(lambda: self._activation_state_mb(102))
        activation_3_btn.clicked.connect(lambda: self._activation_state_mb(103))
        malfunction_1_btn.clicked.connect(lambda: self._malfunction_state_mb(121))
        malfunction_2_btn.clicked.connect(lambda: self._malfunction_state_mb(122))
        malfunction_3_btn.clicked.connect(lambda: self._malfunction_state_mb(123))

    def _set_btn_exip_535_mb(self):
        norma_btn = self.btns.btn_norma(self)
        activation_btn = self.btns.activation_fire(self)
        self.ui.mb_h_top_state_dev_layout.addWidget(norma_btn)
        self.ui.mb_h_top_state_dev_layout.addWidget(activation_btn)
        norma_btn.clicked.connect(self._norma_state_mb)
        activation_btn.clicked.connect(self._activation_state_mb)

    def _set_btn_ir(self):
        norma_btn = self.btns.btn_norma(self)
        kz_btn = self.btns.btn_kz(self)
        fire_btn = self.btns.activation_fire(self)
        self.ui.ash_h_top_state_dev_layout.addWidget(norma_btn)
        self.ui.ash_h_top_state_dev_layout.addWidget(fire_btn)
        self.ui.ash_h_center_state_dev_layout.addWidget(kz_btn)
        norma_btn.clicked.connect(self._norma_state)
        kz_btn.clicked.connect(self._b_30_state)
        fire_btn.clicked.connect(self._b_31_state)

    def _set_btn_a2dpi(self):
        norma_btn = self.btns.btn_norma(self)
        fire_btn = self.btns.activation_fire(self)
        sensitivity_btn = self.btns.btn_sensitivity(self)
        dirt_btn = self.btns.btn_dirt(self)
        self.ui.ash_h_top_state_dev_layout.addWidget(norma_btn)
        self.ui.ash_h_top_state_dev_layout.addWidget(fire_btn)
        self.ui.ash_h_center_state_dev_layout.addWidget(sensitivity_btn)
        self.ui.ash_h_center_state_dev_layout.addWidget(dirt_btn)
        norma_btn.clicked.connect(self._norma_state)
        fire_btn.clicked.connect(self._b_31_state)
        sensitivity_btn.clicked.connect(self._b_3_state)
        dirt_btn.clicked.connect(self._b_2_state)

    def _set_btn_ar1(self):
        norma_btn = self.btns.btn_norma(self)
        fire_btn = self.btns.activation_fire(self)
        noise_btn = self.btns.btn_noise(self)
        break_btn = self.btns.btn_break(self)
        kz_btn = self.btns.btn_kz(self)
        self.ui.ash_h_top_state_dev_layout.addWidget(norma_btn)
        self.ui.ash_h_top_state_dev_layout.addWidget(fire_btn)
        self.ui.ash_h_center_state_dev_layout.addWidget(noise_btn)
        self.ui.ash_h_center_state_dev_layout.addWidget(break_btn)
        self.ui.ash_h_center_state_dev_layout.addWidget(kz_btn)
        norma_btn.clicked.connect(self._norma_state)
        fire_btn.clicked.connect(self._b_31_state)
        noise_btn.clicked.connect(self._b_13_state)
        break_btn.clicked.connect(self._b_14_state)
        kz_btn.clicked.connect(self._b_15_state)

    def _set_btn_mkz(self):
        norma_btn = self.btns.btn_norma(self)
        kz_btn = self.btns.btn_kz(self)
        switch_btn = self.btns.btn_swich(self)
        self.ui.ash_h_top_state_dev_layout.addWidget(norma_btn)
        self.ui.ash_h_top_state_dev_layout.addWidget(switch_btn)
        self.ui.ash_h_center_state_dev_layout.addWidget(kz_btn)
        norma_btn.clicked.connect(self._norma_state)
        kz_btn.clicked.connect(self._b_30_state)
        switch_btn.clicked.connect(self._b_31_state)

    def _set_btn_amk(self):
        norma_btn = self.btns.btn_norma(self)
        alarm_btn = self.btns.btn_alarm(self)
        self.ui.ash_h_top_state_dev_layout.addWidget(norma_btn)
        self.ui.ash_h_top_state_dev_layout.addWidget(alarm_btn)
        norma_btn.clicked.connect(self._norma_state)
        alarm_btn.clicked.connect(self._b_31_state)

    def _set_btn_ati(self):
        norma_btn = self.btns.btn_norma(self)
        fire_btn = self.btns.activation_fire(self)
        diff_fire_btn = self.btns.btn_diff_fire(self)
        self.ui.ash_h_top_state_dev_layout.addWidget(norma_btn)
        self.ui.ash_h_top_state_dev_layout.addWidget(fire_btn)
        self.ui.ash_h_top_state_dev_layout.addWidget(diff_fire_btn)
        norma_btn.clicked.connect(self._norma_state)
        fire_btn.clicked.connect(self._b_31_state)
        diff_fire_btn.clicked.connect(self._b_30_state)

    def _set_btn_ism5(self):
        norma_btn = self.btns.btn_norma(self)
        switch_btn = self.btns.btn_swich(self)
        kz_in1_btn = self.btns.btn_kz_in1(self)
        kz_in2_btn = self.btns.btn_kz_in2(self)
        kz_out1_btn = self.btns.btn_kz_out1(self)
        kz_out2_btn = self.btns.btn_kz_out2(self)
        break_in1_btn = self.btns.btn_break_in1(self)
        break_in2_btn = self.btns.btn_break_in2(self)
        break_out1_btn = self.btns.btn_break_out1(self)
        break_out2_btn = self.btns.btn_break_out2(self)
        alarm_in1_btn = self.btns.btn_alarm_in1(self)
        alarm_in2_btn = self.btns.btn_alarm_in2(self)
        noise_s1_btn = self.btns.btn_noise_s1(self)
        noise_s2_btn = self.btns.btn_noise_s2(self)
        power_btn = self.btns.btn_pwr(self)
        mkz_btn = self.btns.btn_kz(self)
        self.ui.ash_h_top_state_dev_layout.addWidget(norma_btn)
        self.ui.ash_h_top_state_dev_layout.addWidget(alarm_in1_btn)
        self.ui.ash_h_top_state_dev_layout.addWidget(alarm_in2_btn)
        self.ui.ash_h_top_state_dev_layout.addWidget(mkz_btn)
        self.ui.ash_h_center_state_dev_layout.addWidget(kz_in1_btn)
        self.ui.ash_h_center_state_dev_layout.addWidget(break_in1_btn)
        self.ui.ash_h_center_state_dev_layout.addWidget(noise_s1_btn)
        self.ui.ash_h_center_state_dev_layout.addWidget(kz_out1_btn)
        self.ui.ash_h_center_state_dev_layout.addWidget(break_out1_btn)
        self.ui.ash_h_center_state_dev_layout.addWidget(switch_btn)
        self.ui.ash_h_bottom_state_dev_layout.addWidget(kz_in2_btn)
        self.ui.ash_h_bottom_state_dev_layout.addWidget(break_in2_btn)
        self.ui.ash_h_bottom_state_dev_layout.addWidget(noise_s2_btn)
        self.ui.ash_h_bottom_state_dev_layout.addWidget(kz_out2_btn)
        self.ui.ash_h_bottom_state_dev_layout.addWidget(break_out2_btn)
        self.ui.ash_h_bottom_state_dev_layout.addWidget(power_btn)
        norma_btn.clicked.connect(self._norma_state)
        switch_btn.clicked.connect(self._b_31_state)
        kz_in1_btn.clicked.connect(self._b_15_state)
        kz_in2_btn.clicked.connect(self._b_12_state)
        kz_out1_btn.clicked.connect(self._b_5_state)
        kz_out2_btn.clicked.connect(self._b_7_state)
        break_in1_btn.clicked.connect(self._b_14_state)
        break_in2_btn.clicked.connect(self._b_11_state)
        break_out1_btn.clicked.connect(self._b_4_state)
        break_out2_btn.clicked.connect(self._b_6_state)
        alarm_in1_btn.clicked.connect(self._b_29_state)
        alarm_in2_btn.clicked.connect(self._b_27_state)
        noise_s1_btn.clicked.connect(self._b_13_state)
        noise_s2_btn.clicked.connect(self._b_10_state)
        power_btn.clicked.connect(self._b_3_state)
        mkz_btn.clicked.connect(self._b_30_state)

    def _set_btn_ism4(self):
        norma = self.btns.btn_norma(self)
        switch = self.btns.btn_swich(self)
        kz_in1 = self.btns.btn_kz_in1(self)
        kz_in2 = self.btns.btn_kz_in2(self)
        kz_out1 = self.btns.btn_kz_out1(self)
        kz_out2 = self.btns.btn_kz_out2(self)
        break_in1 = self.btns.btn_break_in1(self)
        break_in2 = self.btns.btn_break_in2(self)
        break_out1 = self.btns.btn_break_out1(self)
        break_out2 = self.btns.btn_break_out2(self)
        alarm_in1 = self.btns.btn_alarm_in1(self)
        alarm_in2 = self.btns.btn_alarm_in2(self)
        alarm_in12 = self.btns.btn_alarm_in1_2(self)
        alarm_in22 = self.btns.btn_alarm_in2_2(self)
        noise_s1 = self.btns.btn_noise_s1(self)
        noise_s2 = self.btns.btn_noise_s2(self)
        power = self.btns.btn_pwr(self)
        mkz = self.btns.btn_kz(self)
        self.ui.ash_h_top_state_dev_layout.addWidget(norma)
        self.ui.ash_h_top_state_dev_layout.addWidget(alarm_in1)
        self.ui.ash_h_top_state_dev_layout.addWidget(alarm_in12)
        self.ui.ash_h_top_state_dev_layout.addWidget(alarm_in2)
        self.ui.ash_h_top_state_dev_layout.addWidget(alarm_in22)
        self.ui.ash_h_top_state_dev_layout.addWidget(mkz)
        self.ui.ash_h_center_state_dev_layout.addWidget(kz_in1)
        self.ui.ash_h_center_state_dev_layout.addWidget(break_in1)
        self.ui.ash_h_center_state_dev_layout.addWidget(noise_s1)
        self.ui.ash_h_center_state_dev_layout.addWidget(kz_out1)
        self.ui.ash_h_center_state_dev_layout.addWidget(break_out1)
        self.ui.ash_h_center_state_dev_layout.addWidget(switch)
        self.ui.ash_h_bottom_state_dev_layout.addWidget(kz_in2)
        self.ui.ash_h_bottom_state_dev_layout.addWidget(break_in2)
        self.ui.ash_h_bottom_state_dev_layout.addWidget(noise_s2)
        self.ui.ash_h_bottom_state_dev_layout.addWidget(kz_out2)
        self.ui.ash_h_bottom_state_dev_layout.addWidget(break_out2)
        self.ui.ash_h_bottom_state_dev_layout.addWidget(power)
        norma.clicked.connect(self._norma_state)
        switch.clicked.connect(self._b_31_state)
        kz_in1.clicked.connect(self._b_15_state)
        kz_in2.clicked.connect(self._b_12_state)
        kz_out1.clicked.connect(self._b_5_state)
        kz_out2.clicked.connect(self._b_7_state)
        break_in1.clicked.connect(self._b_14_state)
        break_in2.clicked.connect(self._b_11_state)
        break_out1.clicked.connect(self._b_4_state)
        break_out2.clicked.connect(self._b_6_state)
        alarm_in1.clicked.connect(self._b_29_state)
        alarm_in2.clicked.connect(self._b_27_state)
        alarm_in12.clicked.connect(self._b_28_state)
        alarm_in22.clicked.connect(self._b_26_state)
        noise_s1.clicked.connect(self._b_13_state)
        noise_s2.clicked.connect(self._b_10_state)
        power.clicked.connect(self._b_3_state)
        mkz.clicked.connect(self._b_30_state)

    def change_state(self):
        params = self._get_current_sensor()
        self._clear_layouts_ash()
        #params- {'type': 'А2ДПИ', 'slave': 2, 'serialnumber': 2, 'state': 'Норма', 'state_in': '00 00 00 00', 'row': 0, 'column': 1, 'port': 'COM17', 'net_device': 'КАУ03Д->100771'}
        if params:
            match params["type"]:
                case "МКЗ":
                    self._set_btn_mkz()
                case "ИР-П":
                    self._set_btn_ir()
                case "А2ДПИ":
                    self._set_btn_a2dpi()
                case "АР1":
                    self._set_btn_ar1()
                case "АМК":
                    self._set_btn_amk()
                case "АТИ":
                    self._set_btn_ati()
                case "ИСМ-5":
                    self._set_btn_ism5()
                case "ИСМ-220.4":
                    self._set_btn_ism4()
                case _:
                    logger.info(f"No device {params['type']}")

    def change_state_mb(self):
        params = self._get_current_sensor_mb()
        logger.info(f"params- {params}")
        self._clear_layouts_mb()
        if params:
            match params["type"]:
                case "ИП-535 (Эридан)":
                    self._set_btn_md()
                case "ИП Гелиос 3ИК (Эридан)":
                    self._set_btn_md()
                case "ИП-101 (Эридан)":
                    self._set_btn_md()
                case "ИП Кречет":
                    self._set_btn_md()
                case "ИП Феникс":
                    self._set_btn_md()
                case "ИПЭС ИК-УФ":
                    self._set_btn_md()
                case "МИП 3И":
                    self._set_btn_mip_md()
                case "ИПА V5":
                    self._set_btn_md()
                case "ExИП-535 (Эталон)":
                    self._set_btn_exip_535_mb()
                case "ИП329/330-3-1 (ВЕГА)":
                    self._set_btn_md()
                case _:
                    logger.info(f"No device {params['type']}")

    @Slot(tuple)
    def _change_state_in(self, params_sensor):
        num_row = self.ui.ash_devices_tableWidget.rowCount()
        num_column = self.ui.ash_devices_tableWidget.columnCount()

        for port_info in self.output_data_sensors:
            if port_info["port"] == params_sensor[0]:
                for controller in port_info["controllers"]:
                    if controller["sn_emul"] == params_sensor[1]:
                        for sens in controller["sensors"]:
                            if sens["slave"] == params_sensor[2]["slave"]:
                                sens["state_in"] = params_sensor[2]["state_in"]
                                break

        if self.ui.ash_port_info_lbl.text() == params_sensor[0] and self.ui.ash_net_dev_info_lbl.text() == params_sensor[3]:
            for row in range(num_row):
                for column in range(num_column):
                    sensor_card = self.ui.ash_devices_tableWidget.cellWidget(row, column)
                    if sensor_card:
                        info_sens = sensor_card.get_params()
                        if info_sens["slave"] == params_sensor[2]["slave"]:
                            # sensor_card.set_state_in(params_sensor[2]["state_in"])
                            sensor_card.set_state_in(params_sensor[2])
                            break

    def _clear_layouts_ash(self):
        num_top = self.ui.ash_h_top_state_dev_layout.count()
        num_center = self.ui.ash_h_center_state_dev_layout.count()
        num_bottom = self.ui.ash_h_bottom_state_dev_layout.count()
        if num_top > 0:
            for i in reversed(range(num_top)):
                ch = self.ui.ash_h_top_state_dev_layout.takeAt(i)
                ch.widget().deleteLater()
        if num_center > 0:
            for i in reversed(range(num_center)):
                ch = self.ui.ash_h_center_state_dev_layout.takeAt(i)
                ch.widget().deleteLater()
        if num_bottom > 0:
            for i in reversed(range(num_bottom)):
                ch = self.ui.ash_h_bottom_state_dev_layout.takeAt(i)
                ch.widget().deleteLater()

    def _clear_layouts_mb(self):
        num_top = self.ui.mb_h_top_state_dev_layout.count()
        num_center = self.ui.mb_h_center_state_dev_layout.count()
        num_bottom = self.ui.mb_h_bottom_state_dev_layout.count()
        if num_top > 0:
            for i in reversed(range(num_top)):
                ch = self.ui.mb_h_top_state_dev_layout.takeAt(i)
                ch.widget().deleteLater()
        if num_center > 0:
            for i in reversed(range(num_center)):
                ch = self.ui.mb_h_center_state_dev_layout.takeAt(i)
                ch.widget().deleteLater()
        if num_bottom > 0:
            for i in reversed(range(num_bottom)):
                ch = self.ui.mb_h_bottom_state_dev_layout.takeAt(i)
                ch.widget().deleteLater()

    def _get_params_conn(self):
        params_conn = dict()
        params_conn["host"] = self.ui.host_db_lineEdit.text()
        params_conn["port"] = self.ui.port_db_lineEdit.text()
        params_conn["user"] = self.ui.user_db_lineEdit.text()
        params_conn["password"] = self.ui.pass_db_lineEdit.text()
        params_conn["name"] = self.ui.name_db_lineEdit.text()
        return params_conn

    def _check_connect(self):
        if check_conn(self._get_params_conn()):
            ok_connect(self)
        else:
            err_connect(self)

    @logger.catch
    def _start_servers(self):
        # try:
            self.output_data_sensors = handler_devices(self._get_params_conn(), self.ports_net_devs)

            for net_dev in self.ports_net_devs:
                if net_dev[1][1] == "KAU03DConfig":
                    self.ui.ash_out_net_dev_listWidget.addItem(QListWidgetItem(net_dev[1][2]))
                elif net_dev[1][1] == "SKAU03Config":
                    self.ui.mb_out_net_dev_listWidget.addItem(QListWidgetItem(net_dev[1][2]))

            for server in self.output_data_sensors:
                controller = server["controllers"][0]
                if controller["net_dev"] == "KAU03DConfig":
                    thread: ServerAH = ServerAH(server["controllers"], server["port"])
                    thread.sig_state_in.connect(self._change_state_in)
                    thread.start()
                    self.servers.append(thread)
                elif controller["net_dev"] == "SKAU03Config":
                    thread: ServerMB = ServerMB(server["controllers"][0]["sensors"], server["port"])
                    thread.start()
                    self.servers.append(thread)
            self.ui.tabWidget.setCurrentWidget(self.ui.ash_device_tab)
        # except ValueError:
        #     error_add_sensor(self)

    def _fill_table_ash(self):
        max_column_index = 15
        row = 0
        column = 0
        max_row = 0

        selected_ash_net_dev = self.ui.ash_out_net_dev_listWidget.currentItem().text()
        sensors = []
        self.ui.ash_devices_tableWidget.clear()
        self._clear_layouts_ash()
        for port_info in self.output_data_sensors:
            for controller in port_info["controllers"]:
                if controller["net_device"] == selected_ash_net_dev:
                    sensors = controller["sensors"]
                    num_sens =len(sensors)
                    if num_sens % 16 == 0:
                        max_row = num_sens // max_column_index
                    else:
                        max_row = num_sens // max_column_index + 1

                    self.ui.ash_port_info_lbl.setText(port_info["port"])
                    self.ui.ash_net_dev_info_lbl.setText(controller["net_device"])
        self.ui.ash_devices_tableWidget.setRowCount(max_row)
        self.ui.ash_devices_tableWidget.setColumnCount(max_column_index + 1)

        for index, sensor in enumerate(sensors):
            self.ui.ash_devices_tableWidget.setColumnWidth(column, 150)
            self.ui.ash_devices_tableWidget.setRowHeight(row, 90)
            card = CardDeviceASH(sensor)
            card.set_text_lbl(sensor)
            self.ui.ash_devices_tableWidget.setCellWidget(row, column, card)

            if column % max_column_index == 0 and column != 0:
                row += 1
                column = 0
            else:
                column += 1

    def _fill_table_mb(self):
        max_column_index = 5
        row = 0
        column = 0

        selected_mb_net_dev = self.ui.mb_out_net_dev_listWidget.currentItem().text()
        sensors = []
        self.ui.mb_devices_tableWidget.clear()
        self._clear_layouts_mb()

        for port_info in self.output_data_sensors:
            logger.info(f"port_info {port_info}")
            port = port_info["port"]
            net_device = port_info["controllers"][0]["net_device"]
            if net_device == selected_mb_net_dev:
                sensors = port_info["controllers"][0]["sensors"]
                self.ui.mb_port_info_lbl.setText(port)
                self.ui.mb_net_dev_info_lbl.setText(net_device)

        self.ui.mb_devices_tableWidget.setRowCount(6)
        self.ui.mb_devices_tableWidget.setColumnCount(6)

        for index, sensor in enumerate(sensors):
            self.ui.mb_devices_tableWidget.setColumnWidth(column, 200)
            self.ui.mb_devices_tableWidget.setRowHeight(row, 70)
            card = CardDeviceMB()
            card.set_text_lbl(sensor)
            self.ui.mb_devices_tableWidget.setCellWidget(row, column, card)

            if column % max_column_index == 0 and column != 0:
                row += 1
                column = 0
            else:
                column += 1

    def _save_params_conn(self):
        parameters = self._get_params_conn()
        save_conn_to_file(parameters)

    def _output_ports(self):
        self.ui.ports_listWidget.clear()
        self.ports = get_ports_info()
        for i in self.ports:
            self.ui.ports_listWidget.addItem(QListWidgetItem(i[1]))

    def _output_net_devices(self):
        self.ui.net_dev_listWidget.clear()
        self.net_devices = get_net_devices_from_db(self._get_params_conn())
        if self.net_devices:
            for net_dev in self.net_devices:
                self.ui.net_dev_listWidget.addItem(QListWidgetItem(net_dev[2]))

    def _save_config(self):
        conf = self.ports_net_devs
        save_config_to_file(conf)

    def _download_config(self):
        self.ports_net_devs = get_config_from_file()
        self.output_data_sensors = handler_devices(self._get_params_conn(), self.ports_net_devs)
        self._output_config_to_widget()

    def _output_config_to_widget(self):
        self.ui.port_and_net_dev_tableWidget.setRowCount(len(self.ports_net_devs))
        cur_row = 0
        for row in self.ports_net_devs:
            cur_row += 1
            self.ui.port_and_net_dev_tableWidget.setColumnCount(3)
            self.ui.port_and_net_dev_tableWidget.setItem(cur_row - 1, 0, QTableWidgetItem(row[0]))
            self.ui.port_and_net_dev_tableWidget.setItem(cur_row - 1, 1, QTableWidgetItem(row[1][2]))
            if row[1][1] == "KAU03DConfig":
                self.ui.port_and_net_dev_tableWidget.setItem(cur_row - 1, 2, QTableWidgetItem(row[2]))

        self.ui.port_and_net_dev_tableWidget.setHorizontalHeaderLabels(["port", "net device", "emulator"])

    def _join_port_and_net_device(self):
        sn_emul = None
        try:
            row_port = self.ui.ports_listWidget.currentRow()
            row_net_device = self.ui.net_dev_listWidget.currentRow()

            if row_port < 0 or row_net_device < 0:
                raise IndexError
            port = self.ports[row_port][0]

            for dev_i in self.net_devices:
                if dev_i[2] == self.net_devices[row_net_device][2]:
                    if check_join_table_output(port, dev_i, self.ports_net_devs):
                        cur_row = self.ui.port_and_net_dev_tableWidget.rowCount() + 1
                        self.ui.port_and_net_dev_tableWidget.setRowCount(cur_row)
                        self.ui.port_and_net_dev_tableWidget.setColumnCount(3)
                        self.ui.port_and_net_dev_tableWidget.setHorizontalHeaderLabels(
                            ["port", "net device", "emulator"])
                        self.ui.port_and_net_dev_tableWidget.setItem(cur_row-1, 0, QTableWidgetItem(port))
                        self.ui.port_and_net_dev_tableWidget.setItem(cur_row-1, 1, QTableWidgetItem(dev_i[2]))
                        if dev_i[1] == "KAU03DConfig":
                            sn_emul = self.ui.sn_emulator_lineEdit.text()
                            self.ui.port_and_net_dev_tableWidget.setItem(cur_row - 1, 2, QTableWidgetItem(sn_emul))

                        self.ports_net_devs.append((port, dev_i, sn_emul))
                    self.ui.port_and_net_dev_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
                    break
        except IndexError:
            err_selection(self)

    def _save_state_sensor(self, sensor):
        for port_info in self.output_data_sensors:
            if port_info["port"] == sensor["port"]:
                for controller in port_info["controllers"]:
                    if controller["net_device"] == sensor["net_device"]:
                        for sens in controller["sensors"]:
                            if sens["slave"] == sensor["slave"]:
                                sens["state"] = sensor["state"]
                                sens["state_cod"] = sensor["state_cod"]

    def _norma_state_mb(self):
        params = self._get_current_sensor_mb()
        params["state"] = "Норма"
        params["state_cod"] = "N"
        sensor = self.ui.mb_devices_tableWidget.cellWidget(params["row"], params["column"])
        sensor.set_text_lbl(params)
        self._save_state_sensor(params)
        self._send_in_thread(params["port"], params)

    def _activation_state_mb(self, num=0):
        params = self._get_current_sensor_mb()
        if num == 101:
            params["state"] = "Сработал ШС1"
            params["state_cod"] = 101
        elif num == 102:
            params["state"] = "Сработал ШС2"
            params["state_cod"] = 102
        elif num == 103:
            params["state"] = "Сработал ШС3"
            params["state_cod"] = 103
        else:
            params["state"] = "Сработал"
            params["state_cod"] = 10
        sensor = self.ui.mb_devices_tableWidget.cellWidget(params["row"], params["column"])
        sensor.set_text_lbl(params)
        self._save_state_sensor(params)
        logger.info(f"params {params}")
        self._send_in_thread(params["port"], params)

    def _malfunction_state_mb(self, num=0):
        params = self._get_current_sensor_mb()
        if num == 121:
            params["state"] = "Неисправность ШС1"
            params["state_cod"] = 121
        elif num == 122:
            params["state"] = "Неисправность ШС2"
            params["state_cod"] = 122
        elif num == 123:
            params["state"] = "Неисправность ШС3"
            params["state_cod"] = 123
        else:
            params["state"] = "Неисправность"
            params["state_cod"] = 1
        sensor = self.ui.mb_devices_tableWidget.cellWidget(params["row"], params["column"])
        sensor.set_text_lbl(params)
        self._save_state_sensor(params)
        self._send_in_thread(params["port"], params)

    def _norma_state(self):
        params = self._get_current_sensor()
        params["state"] = "Норма"
        params["state_cod"] = "N"
        sensor = self.ui.ash_devices_tableWidget.cellWidget(params["row"], params["column"])
        sensor.set_text_lbl(params)
        self._save_state_sensor(params)
        # self._send_in_thread(sebsor)

    def _b_31_state(self):
        params = self._get_current_sensor()
        params["state"] = "Сработал"
        params["state_cod"] = 31
        sensor = self.ui.ash_devices_tableWidget.cellWidget(params["row"], params["column"])
        sensor.set_text_lbl(params)
        self._save_state_sensor(params)
        # self._send_in_thread(sebsor)

    def _b_30_state(self):
        params = self._get_current_sensor()
        if params["type"] == "АТИ":
            params["state"] = "Сработал"
        else:
            params["state"] = "Неисправность"
        params["state_cod"] = 30
        sensor = self.ui.ash_devices_tableWidget.cellWidget(params["row"], params["column"])
        sensor.set_text_lbl(params)
        self._save_state_sensor(params)
        # self._send_in_thread(params)

    def _b_29_state(self):
        params = self._get_current_sensor()
        params["state"] = "Неисправность"
        params["state_cod"] = 29
        sensor = self.ui.ash_devices_tableWidget.cellWidget(params["row"], params["column"])
        sensor.set_text_lbl(params)
        self._save_state_sensor(params)
        # self._send_in_thread(params)

    def _b_28_state(self):
        params = self._get_current_sensor()
        params["state"] = "Неисправность"
        params["state_cod"] = 28
        sensor = self.ui.ash_devices_tableWidget.cellWidget(params["row"], params["column"])
        sensor.set_text_lbl(params)
        self._save_state_sensor(params)
        # self._send_in_thread(params)

    def _b_27_state(self):
        params = self._get_current_sensor()
        params["state"] = "Неисправность"
        params["state_cod"] = 27
        sensor = self.ui.ash_devices_tableWidget.cellWidget(params["row"], params["column"])
        sensor.set_text_lbl(params)
        self._save_state_sensor(params)
        # self._send_in_thread(params)

    def _b_26_state(self):
        params = self._get_current_sensor()
        params["state"] = "Неисправность"
        params["state_cod"] = 26
        sensor = self.ui.ash_devices_tableWidget.cellWidget(params["row"], params["column"])
        sensor.set_text_lbl(params)
        self._save_state_sensor(params)
        # self._send_in_thread(params)

    def _b_15_state(self):
        params = self._get_current_sensor()
        params["state"] = "Неисправность"
        params["state_cod"] = 15
        sensor = self.ui.ash_devices_tableWidget.cellWidget(params["row"], params["column"])
        sensor.set_text_lbl(params)
        self._save_state_sensor(params)
        # self._send_in_thread(params)

    def _b_14_state(self):
        params = self._get_current_sensor()
        params["state"] = "Неисправность"
        params["state_cod"] = 14
        sensor = self.ui.ash_devices_tableWidget.cellWidget(params["row"], params["column"])
        sensor.set_text_lbl(params)
        self._save_state_sensor(params)
        # self._send_in_thread(params)

    def _b_13_state(self):
        params = self._get_current_sensor()
        params["state"] = "Неисправность"
        params["state_cod"] = 13
        sensor = self.ui.ash_devices_tableWidget.cellWidget(params["row"], params["column"])
        sensor.set_text_lbl(params)
        self._save_state_sensor(params)
        # self._send_in_thread(params)

    def _b_12_state(self):
        params = self._get_current_sensor()
        params["state"] = "Неисправность"
        params["state_cod"] = 12
        sensor = self.ui.ash_devices_tableWidget.cellWidget(params["row"], params["column"])
        sensor.set_text_lbl(params)
        self._save_state_sensor(params)
        # self._send_in_thread(params)

    def _b_11_state(self):
        params = self._get_current_sensor()
        params["state"] = "Неисправность"
        params["state_cod"] = 11
        sensor = self.ui.ash_devices_tableWidget.cellWidget(params["row"], params["column"])
        sensor.set_text_lbl(params)
        self._save_state_sensor(params)
        # self._send_in_thread(params)

    def _b_10_state(self):
        params = self._get_current_sensor()
        params["state"] = "Неисправность"
        params["state_cod"] = 10
        sensor = self.ui.ash_devices_tableWidget.cellWidget(params["row"], params["column"])
        sensor.set_text_lbl(params)
        self._save_state_sensor(params)
        # self._send_in_thread(params)

    def _b_7_state(self):
        params = self._get_current_sensor()
        params["state"] = "Неисправность"
        params["state_cod"] = 7
        sensor = self.ui.ash_devices_tableWidget.cellWidget(params["row"], params["column"])
        sensor.set_text_lbl(params)
        self._save_state_sensor(params)
        # self._send_in_thread(params)

    def _b_6_state(self):
        params = self._get_current_sensor()
        params["state"] = "Неисправность"
        params["state_cod"] = 6
        sensor = self.ui.ash_devices_tableWidget.cellWidget(params["row"], params["column"])
        sensor.set_text_lbl(params)
        self._save_state_sensor(params)
        # self._send_in_thread(params)

    def _b_5_state(self):
        params = self._get_current_sensor()
        params["state"] = "Неисправность"
        params["state_cod"] = 5
        sensor = self.ui.ash_devices_tableWidget.cellWidget(params["row"], params["column"])
        sensor.set_text_lbl(params)
        self._save_state_sensor(params)
        # self._send_in_thread(params)

    def _b_4_state(self):
        params = self._get_current_sensor()
        params["state"] = "Неисправность"
        params["state_cod"] = 4
        sensor = self.ui.ash_devices_tableWidget.cellWidget(params["row"], params["column"])
        sensor.set_text_lbl(params)
        self._save_state_sensor(params)
        # self._send_in_thread(params)

    def _b_3_state(self):
        params = self._get_current_sensor()
        params["state"] = "Неисправность"
        params["state_cod"] = 3
        sensor = self.ui.ash_devices_tableWidget.cellWidget(params["row"], params["column"])
        sensor.set_text_lbl(params)
        self._save_state_sensor(params)
        # self._send_in_thread(params)

    def _b_2_state(self):
        params = self._get_current_sensor()
        params["state"] = "Неисправность"
        params["state_cod"] = 2
        sensor = self.ui.ash_devices_tableWidget.cellWidget(params["row"], params["column"])
        sensor.set_text_lbl(params)
        self._save_state_sensor(params)
        # self._send_in_thread(params)

    def _get_current_sensor(self) -> dict:
        """Получить параметры сенсора из выделенной ячейки
            :param
            :return: {'type': 'А2ДПИ', 'slave': '1', 'serialnumber': '1', 'state': 'Норма',
            "row": 1, "column": 1, "port": "COM1", "net_dev": 'КАУ03Д->5843'}
        """
        row = self.ui.ash_devices_tableWidget.currentRow()
        column = self.ui.ash_devices_tableWidget.currentColumn()
        port = self.ui.ash_port_info_lbl.text()
        net_dev = self.ui.ash_net_dev_info_lbl.text()
        try:
            sens = self.ui.ash_devices_tableWidget.cellWidget(row, column)
            params = sens.get_params()
            params["row"] = row
            params["column"] = column
            params["port"] = port
            params["net_device"] = net_dev
            return params
        except AttributeError:
            ...

    def _get_current_sensor_mb(self) -> dict:
        """Получить параметры сенсора из выделенной ячейки ModBus
        """
        row = self.ui.mb_devices_tableWidget.currentRow()
        column = self.ui.mb_devices_tableWidget.currentColumn()
        port = self.ui.mb_port_info_lbl.text()
        net_dev = self.ui.mb_net_dev_info_lbl.text()
        try:
            sens = self.ui.mb_devices_tableWidget.cellWidget(row, column)
            params = sens.get_params()
            params["row"] = row
            params["column"] = column
            params["port"] = port
            params["net_device"] = net_dev
            return params
        except AttributeError:
            ...

    def _send_in_thread(self, name: str, params: dict) -> None:
        """
        :param name: str (COM1...) название потока (COM порт)
        :return:
        """
        for thread in self.servers:
            if thread.name == name:
                thread.changing_state(params)

    def _delete_line(self):
        row_num = self.ui.port_and_net_dev_tableWidget.currentRow()
        if row_num == -1:
            err_selection_port_net_dev(self)
        else:
            row_item = self.ports_net_devs[row_num]
            self.ui.port_and_net_dev_tableWidget.removeRow(row_num)
            for num_row_port in range(self.ui.ports_listWidget.count()):
                if f"({row_item[0]})" in self.ui.ports_listWidget.item(num_row_port).text().split():
                    self.ui.ports_listWidget.item(num_row_port).setBackground(QColor(0, 85, 127))
            for num_row_net_dev in range(self.ui.net_dev_listWidget.count()):
                if row_item[1] == self.ui.net_dev_listWidget.item(num_row_net_dev).text():
                    self.ui.net_dev_listWidget.item(num_row_net_dev).setBackground(QColor(0, 85, 127))
            self.ports_net_devs.pop(row_num)

    def _file_selection(self):
        self.file_path = open_file(self)
        if self.file_path:
            self.ui.path_info_lbl.setText(self.file_path)

    def _view_port_ufw(self):
        """
        [('COM6', 'ICPDAS Serial Converter (COM6)').....]
        :return:
        """
        self.ui.port_loading_listWidget.clear()
        self.ports = get_ports_info()
        for port in self.ports:
            self.ui.port_loading_listWidget.addItem(port[1])

    def _update_firmware(self):
        """
        Команда A2 обновление прошивки
        """

        port = None
        sn = None
        path = None

        try:
            path = self.file_path
            sn = self.ui.sn_skau_lineEdit.text()
            speed = self.ui.speed_485_comboBox.currentText()
            if not sn.isdigit():
                raise AttributeError("No selecton SN")
            for port_i in self.ports:
                if port_i[1] == self.ui.port_loading_listWidget.currentItem().text():
                    port = port_i[0]
            if not port:
                raise AttributeError("No selection port")

            data = get_data_from_file(path)
            boot_firmware(port, int(sn), data, speed, self)

        except AttributeError as err:
            error_update(self, err)
            logger.info(f"Error update>> {err}")
