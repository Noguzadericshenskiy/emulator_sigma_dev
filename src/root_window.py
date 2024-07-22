from PySide6.QtGui import QColor, Qt
from PySide6.QtCore import QRect, QSize
from PySide6.QtWidgets import (
    QMainWindow,
    QListWidgetItem,
    QTableWidgetItem,
    QAbstractItemView,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout
)
from loguru import logger

from src.ui.main_win import Ui_MainWindow
from src.ui.card_dev import CardDeviceASH, CardDeviceMB
from src.utilites.setup import (
    NumbersIPValidator,
    PortValidator,
    get_ports_info,
    check_join_table_output,
    save_conn_to_file,
    check_file,
    get_conn_from_file
)
from src.utilites.database import (
    get_net_devices_from_db,
    handler_devices,
    check_conn,
)
from src.utilites.server_mb import ServerMB
from src.utilites.server_ash import ServerAH
from src.utilites.dialogues import (
    err_selection,
    ok_connect,
    err_connect,
    err_selection_port_net_dev,
)

from src.ui.button_states import StatesBtn


class MainWindow(QMainWindow):
    def __init__(self):
        self.servers = []
        super().__init__()
        self.setWindowTitle("Эмулятор датчиков Modbus")
        self.ports = []
        self.net_devices = []
        self.ports_net_devs = []
        self.ui = Ui_MainWindow()
        self.btns = StatesBtn()
        self.ui.setupUi(self)
        check_file()
        self._set_parameters()
        self.ui.check_db_btn.clicked.connect(self._check_connect)
        self.ui.start_emulator_btn.clicked.connect(self._start_servers)
        self.ui.get_ports_btn.clicked.connect(self._output_ports)
        self.ui.get_net_dev_btn.clicked.connect(self._output_net_devices)
        self.ui.join_btn.clicked.connect(self._join_port_and_net_device)
        self.ui.save_db_btn.clicked.connect(self._save_params_conn)
        self.ui.delete_line_btn.clicked.connect(self._delete_line)

        self.ui.host_db_lineEdit.setValidator(NumbersIPValidator())
        self.ui.port_db_lineEdit.setValidator(PortValidator())
        self.ui.ash_devices_tableWidget.clicked.connect(self.change_state)

        self.ui.ash_out_net_dev_listWidget.clicked.connect(self._fill_table_ash)

    def _set_parameters(self):
        params_conn = get_conn_from_file()
        self.ui.host_db_lineEdit.setText(params_conn["host"])
        self.ui.port_db_lineEdit.setText(params_conn["port"])
        self.ui.user_db_lineEdit.setText(params_conn["user"])
        self.ui.pass_db_lineEdit.setText(params_conn["password"])
        self.ui.name_db_lineEdit.setText(params_conn["name"])
        self.ui.sn_emulator_lineEdit.setText("641")

    def set_btn_modbus(self):
        norma_btn = self.btns.btn_norma(self)
        fire_btn = self.btns.btn_fire(self)
        error = self.btns.btn_error_mb(self)
        self.hlay_top.addWidget(norma_btn)
        self.hlay_top.addWidget(fire_btn)
        self.hlay_bottom.addWidget(error)

    def set_btn_ir(self):
        norma_btn = self.btns.btn_norma(self)
        kz_btn = self.btns.btn_kz(self)
        fire_btn = self.btns.btn_fire(self)
        self.ui.ash_h_top_state_dev_layout.addWidget(norma_btn)
        self.ui.ash_h_top_state_dev_layout.addWidget(fire_btn)
        self.ui.ash_h_center_state_dev_layout.addWidget(kz_btn)
        norma_btn.clicked.connect(self._norma_state)
        kz_btn.clicked.connect(self._b_30_state)
        fire_btn.clicked.connect(self._b_31_state)

    def _set_btn_a2dpi(self):
        norma_btn = self.btns.btn_norma(self)
        fire_btn = self.btns.btn_fire(self)
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

    def set_btn_ar1(self):
        norma_btn = self.btns.btn_norma(self)
        fire_btn = self.btns.btn_fire(self)
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

    def set_btn_mkz(self):
        norma_btn = self.btns.btn_norma(self)
        kz_btn = self.btns.btn_kz(self)
        switch_btn = self.btns.btn_swich(self)
        self.ui.ash_h_top_state_dev_layout.addWidget(norma_btn)
        self.ui.ash_h_top_state_dev_layout.addWidget(switch_btn)
        self.ui.ash_h_center_state_dev_layout.addWidget(kz_btn)
        norma_btn.clicked.connect(self._norma_state)
        kz_btn.clicked.connect(self._b_30_state)
        switch_btn.clicked.connect(self._b_31_state)

    def set_btn_amk(self):
        norma_btn = self.btns.btn_norma(self)
        alarm_btn = self.btns.btn_alarm(self)
        self.ui.ash_h_top_state_dev_layout.addWidget(norma_btn)
        self.ui.ash_h_top_state_dev_layout.addWidget(alarm_btn)
        norma_btn.clicked.connect(self._norma_state)
        alarm_btn.clicked.connect(self._b_31_state)

    def set_btn_ati(self):
        norma_btn = self.btns.btn_norma(self)
        fire_btn = self.btns.btn_fire(self)
        diff_fire_btn = self.btns.btn_diff_fire(self)
        self.ui.ash_h_top_state_dev_layout.addWidget(norma_btn)
        self.ui.ash_h_top_state_dev_layout.addWidget(fire_btn)
        self.ui.ash_h_top_state_dev_layout.addWidget(diff_fire_btn)
        norma_btn.clicked.connect(self._norma_state)
        fire_btn.clicked.connect(self._b_31_state)
        diff_fire_btn.clicked.connect(self._b_30_state)

    def _set_btn_ism5(self):
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
        self.ui.ash_h_top_state_dev_layout.addWidget(norma)
        self.ui.ash_h_top_state_dev_layout.addWidget(alarm_in1)
        self.ui.ash_h_top_state_dev_layout.addWidget(alarm_in2)
        self.ui.ash_h_top_state_dev_layout.addWidget(switch)
        self.ui.ash_h_center_state_dev_layout.addWidget(kz_in1)
        self.ui.ash_h_center_state_dev_layout.addWidget(break_in1)
        self.ui.ash_h_center_state_dev_layout.addWidget(kz_out1)
        self.ui.ash_h_center_state_dev_layout.addWidget(break_out1)
        self.ui.ash_h_bottom_state_dev_layout.addWidget(kz_in2)
        self.ui.ash_h_bottom_state_dev_layout.addWidget(break_in2)
        self.ui.ash_h_bottom_state_dev_layout.addWidget(kz_out2)
        self.ui.ash_h_bottom_state_dev_layout.addWidget(break_out2)
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

    def change_state(self):
        params = self._get_current_sensor()
        logger.info(params)
        self._clear_layouts_ash()
        if params:
            match params["type"]:
                case "МКЗ":
                    self.set_btn_mkz()
                case "ИР-П":
                    self.set_btn_ir()
                case "А2ДПИ":
                    self._set_btn_a2dpi()
                case "АР1":
                    self.set_btn_ar1()
                case "АМК":
                    self.set_btn_amk()
                case "АТИ":
                    self.set_btn_ati()
                case "АОПИ":
                    ...

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

    def _start_servers(self):
        self.output_data_sensors = handler_devices(self._get_params_conn(), self.ports_net_devs)

        for net_dev in self.ports_net_devs:
            if net_dev[1][1] == "KAU03DConfig":
                self.ui.ash_out_net_dev_listWidget.addItem(QListWidgetItem(net_dev[1][2]))
            elif net_dev[1][1] == "SKAU03Config":
                self.ui.mb_out_net_dev_listWidget.addItem(QListWidgetItem(net_dev[1][2]))
        for server in self.output_data_sensors:
            controller = server["controllers"][0]
            logger.info(controller)
            if controller["net_dev"] == "KAU03DConfig":
                thread: ServerAH = ServerAH(server["controllers"], server["port"])
            # else:
            #     thread: ServerMB = ServerMB(controller, server["port"])

                thread.start()
                self.servers.append(thread)

        self.ui.tabWidget.setCurrentWidget(self.ui.ash_device_tab)

    def _fill_table_ash(self):
        MAX_ROW_INDEX = 4
        row = 0
        column = 0

        selected_ash_net_dev = self.ui.ash_out_net_dev_listWidget.currentItem().text()
        sensors = []
        self.ui.ash_devices_tableWidget.clear()
        self._clear_layouts_ash()
        for port_info in self.output_data_sensors:
            for controller in port_info["controllers"]:
                if controller["net_device"] == selected_ash_net_dev:
                    sensors = controller["sensors"]
                    self.ui.ash_port_info_lbl.setText(port_info["port"])
                    self.ui.ash_net_dev_info_lbl.setText(controller["net_device"])
        self.ui.ash_devices_tableWidget.setRowCount(6)
        self.ui.ash_devices_tableWidget.setColumnCount(16)

        for index, sensor in enumerate(sensors):
            self.ui.ash_devices_tableWidget.setColumnWidth(column, 150)
            self.ui.ash_devices_tableWidget.setRowHeight(row, 90)
            card = CardDeviceASH()
            card.set_text_lbl(sensor)
            self.ui.ash_devices_tableWidget.setCellWidget(row, column, card)

            if column % MAX_ROW_INDEX == 0 and column != 0:
                row += 1
                column = 0
            else:
                column += 1

    def _fill_table_mb(self):
        MAX_ROW_INDEX = 4
        row = 0
        column = 0

        selected_mb_net_dev = self.ui.mb_out_net_dev_listWidget.currentItem().text()
        sensors = []
        self.ui.mb_devices_tableWidget.clear()
        self.ui.mb_devices_tableWidget.setRowCount(row)
        self.ui.mb_devices_tableWidget.setColumnCount(column)
        # self._clear_layout_mb()

        for index, sensor in enumerate(sensors):
            self.ui.mb_devices_tableWidget.setColumnWidth(column, 150)
            self.ui.mb_devices_tableWidget.setRowHeight(row, 90)
            card = CardDeviceMB()
            card.set_text_lbl(sensor)
            self.ui.mb_devices_tableWidget.setCellWidget(row, column, card)

            if column % MAX_ROW_INDEX == 0 and column != 0:
                row += 1
                column = 0
            else:
                column += 1


        # output_data_sensors = handler_devices(self._get_params_conn(), self.ports_net_devs)
        # num_rows = len(output_data_sensors)
        # self.ui.output_table.setRowCount(num_rows)
        # self.ui.output_table.setColumnCount(130)
        # # self.ui.output_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.ui.output_table.setHorizontalHeaderLabels(["PORT", "Net-Dev"] + [str(i) for i in range(1, 130)])
        # for num_row in range(num_rows):
        #     sensors = []
        #     row = output_data_sensors[num_row]
        #     #{'port': 'COM6', 'net_device': 'КАУ03Д->5843', 'net_dev': 'KAU03DConfig',
        #     # 'sensors': [{'type': 51, 'state': 'N', 'slave': 1, 'threshold': '15', 'serialnumber': '10'},...
        #     self.ui.output_table.setItem(num_row, 0, QTableWidgetItem(row["port"]))
        #     self.ui.output_table.item(num_row, 0,).setForeground(QColor(255, 255, 255))
        #     self.ui.output_table.setItem(num_row, 1, QTableWidgetItem(row["net_device"]))
        #     for num_sensor in range(len(row["sensors"])):
        #         num_column = num_sensor + 2
        #         sensor = row["sensors"][num_sensor]
        #         self.ui.output_table.setItem(
        #             num_row, num_column,
        #             QTableWidgetItem(f'{sensor["type"]} {sensor["state"]} {sensor["slave"]}'))
        #         self.ui.output_table.item(num_row, num_column).setBackground(QColor(157, 242, 160))
        #
        #         sensor_tool_tip = create_toll_tip(sensor)
        #         self.ui.output_table.item(num_row, num_column).setToolTip(sensor_tool_tip)
        #         sensor["row"] = num_row
        #         sensor["column"] = num_column
        #         sensors.append(sensor)
        #     if row["net_dev"] == "KAU03DConfig":
        #         thread: ServerAH = ServerAH(sensors, row["port"])
        #     else:
        #         thread: ServerMB = ServerMB(sensors, row["port"])
        #     thread.start()
        #     self.servers.append(thread)
        # self.ui.tabWidget.setCurrentWidget(self.ui.main_tab)
        # self.ui.output_table.sortItems(0, order=Qt.SortOrder.AscendingOrder)
        # self.ui.output_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

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
        ...
        # params = self._get_current_sensor()
        # row = params["row"]
        # column = params["column"]
        # params["state"] = "N"
        # port = self.ui.output_table.item(row, 0).text()
        # self.ui.output_table.setItem(row, column, QTableWidgetItem(f'{params["type"]} N {params["slave"]}'))
        # self.ui.output_table.item(row, column).setBackground(QColor(157, 242, 160))
        # self._send_in_thread(port, params)

    def _norma_state(self):
        params = self._get_current_sensor()
        params["state"] = "Норма"
        params["state_cod"] = "N"
        logger.info(params)
        sensor = self.ui.ash_devices_tableWidget.cellWidget(params["row"], params["column"])
        sensor.set_text_lbl(params)
        self._save_state_sensor(params)
        # self._send_in_thread(sebsor)

    def _b_31_state(self):
        params = self._get_current_sensor()
        params["state"] = "Сработал"
        params["state_cod"] = 31
        logger.info(params)
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
        logger.info(params)
        sensor = self.ui.ash_devices_tableWidget.cellWidget(params["row"], params["column"])
        sensor.set_text_lbl(params)
        self._save_state_sensor(params)
        # self._send_in_thread(params)

    def _b_29_state(self):
        params = self._get_current_sensor()
        params["state"] = "Неисправность"
        params["state_cod"] = 29
        logger.info(params)
        sensor = self.ui.ash_devices_tableWidget.cellWidget(params["row"], params["column"])
        sensor.set_text_lbl(params)
        self._save_state_sensor(params)
        # self._send_in_thread(params)

    def _b_27_state(self):
        params = self._get_current_sensor()
        params["state"] = "Неисправность"
        params["state_cod"] = 27
        logger.info(params)
        sensor = self.ui.ash_devices_tableWidget.cellWidget(params["row"], params["column"])
        sensor.set_text_lbl(params)
        self._save_state_sensor(params)
        # self._send_in_thread(params)

    def _b_15_state(self):
        params = self._get_current_sensor()
        params["state"] = "Неисправность"
        params["state_cod"] = 15
        logger.info(params)
        sensor = self.ui.ash_devices_tableWidget.cellWidget(params["row"], params["column"])
        sensor.set_text_lbl(params)
        self._save_state_sensor(params)
        # self._send_in_thread(params)

    def _b_14_state(self):
        params = self._get_current_sensor()
        params["state"] = "Неисправность"
        params["state_cod"] = 14
        logger.info(params)
        sensor = self.ui.ash_devices_tableWidget.cellWidget(params["row"], params["column"])
        sensor.set_text_lbl(params)
        self._save_state_sensor(params)
        # self._send_in_thread(params)

    def _b_13_state(self):
        params = self._get_current_sensor()
        params["state"] = "Неисправность"
        params["state_cod"] = 13
        logger.info(params)
        sensor = self.ui.ash_devices_tableWidget.cellWidget(params["row"], params["column"])
        sensor.set_text_lbl(params)
        self._save_state_sensor(params)
        # self._send_in_thread(params)

    def _b_12_state(self):
        params = self._get_current_sensor()
        params["state"] = "Неисправность"
        params["state_cod"] = 12
        logger.info(params)
        sensor = self.ui.ash_devices_tableWidget.cellWidget(params["row"], params["column"])
        sensor.set_text_lbl(params)
        self._save_state_sensor(params)
        # self._send_in_thread(params)

    def _b_11_state(self):
        params = self._get_current_sensor()
        params["state"] = "Неисправность"
        params["state_cod"] = 11
        logger.info(params)
        sensor = self.ui.ash_devices_tableWidget.cellWidget(params["row"], params["column"])
        sensor.set_text_lbl(params)
        self._save_state_sensor(params)
        # self._send_in_thread(params)

    def _b_7_state(self):
        params = self._get_current_sensor()
        params["state"] = "Неисправность"
        params["state_cod"] = 7
        logger.info(params)
        sensor = self.ui.ash_devices_tableWidget.cellWidget(params["row"], params["column"])
        sensor.set_text_lbl(params)
        self._save_state_sensor(params)
        # self._send_in_thread(params)

    def _b_6_state(self):
        params = self._get_current_sensor()
        params["state"] = "Неисправность"
        params["state_cod"] = 6
        logger.info(params)
        sensor = self.ui.ash_devices_tableWidget.cellWidget(params["row"], params["column"])
        sensor.set_text_lbl(params)
        self._save_state_sensor(params)
        # self._send_in_thread(params)

    def _b_5_state(self):
        params = self._get_current_sensor()
        params["state"] = "Неисправность"
        params["state_cod"] = 5
        logger.info(params)
        sensor = self.ui.ash_devices_tableWidget.cellWidget(params["row"], params["column"])
        sensor.set_text_lbl(params)
        self._save_state_sensor(params)
        # self._send_in_thread(params)

    def _b_4_state(self):
        params = self._get_current_sensor()
        params["state"] = "Неисправность"
        params["state_cod"] = 4
        logger.info(params)
        sensor = self.ui.ash_devices_tableWidget.cellWidget(params["row"], params["column"])
        sensor.set_text_lbl(params)
        self._save_state_sensor(params)
        # self._send_in_thread(params)

    def _b_3_state(self):
        params = self._get_current_sensor()
        params["state"] = "Неисправность"
        params["state_cod"] = 3
        logger.info(params)
        sensor = self.ui.ash_devices_tableWidget.cellWidget(params["row"], params["column"])
        sensor.set_text_lbl(params)
        self._save_state_sensor(params)
        # self._send_in_thread(params)

    def _b_2_state(self):
        params = self._get_current_sensor()
        params["state"] = "Неисправность"
        params["state_cod"] = 2
        logger.info(params)
        sensor = self.ui.ash_devices_tableWidget.cellWidget(params["row"], params["column"])
        sensor.set_text_lbl(params)
        self._save_state_sensor(params)
        # self._send_in_thread(params)

    def _get_current_sensor(self) -> dict:
        """Получить значение выделенной ячейки
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
