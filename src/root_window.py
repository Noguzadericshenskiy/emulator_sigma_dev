from PySide6.QtGui import QColor, Qt
from PySide6.QtCore import QRect
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
from src.utilites.tool_tips import create_toll_tip

from src.ui.card_dev import CardDeviceMB


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
        self.ui.send_table_btn.clicked.connect(self._fill_table)
        self.ui.get_ports_btn.clicked.connect(self._output_ports)
        self.ui.get_net_dev_btn.clicked.connect(self._output_net_devices)
        self.ui.join_btn.clicked.connect(self._join_port_and_net_device)
        self.ui.save_db_btn.clicked.connect(self._save_params_conn)
        self.ui.delete_line_btn.clicked.connect(self._delete_line)
        self.ui.host_db_lineEdit.setValidator(NumbersIPValidator())
        self.ui.port_db_lineEdit.setValidator(PortValidator())
        self.ui.output_table.clicked.connect(self.change_state)
        self.vlay = QVBoxLayout(self.ui.states_groupBox)
        self.hlay_top = QHBoxLayout(self.ui.states_groupBox)
        self.hlay_bottom = QHBoxLayout(self.ui.states_groupBox)
        self.vlay.addLayout(self.hlay_top)
        self.vlay.addLayout(self.hlay_bottom)

        # self.ui.modbus_dev_tab.

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
        self.hlay_top.addWidget(norma_btn)
        self.hlay_bottom.addWidget(kz_btn)
        self.hlay_top.addWidget(fire_btn)
        norma_btn.clicked.connect(self._norma_state)
        kz_btn.clicked.connect(self._b_30_state)
        fire_btn.clicked.connect(self._b_31_state)

    def set_btn_a2dpi(self):
        norma_btn = self.btns.btn_norma(self)
        fire_btn = self.btns.btn_fire(self)
        sensitivity_btn = self.btns.btn_sensitivity(self)
        dirt_btn = self.btns.btn_dirt(self)
        self.hlay_top.addWidget(norma_btn)
        self.hlay_top.addWidget(fire_btn)
        self.hlay_bottom.addWidget(sensitivity_btn)
        self.hlay_bottom.addWidget(dirt_btn)
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
        self.hlay_top.addWidget(norma_btn)
        self.hlay_top.addWidget(fire_btn)
        self.hlay_bottom.addWidget(noise_btn)
        self.hlay_bottom.addWidget(break_btn)
        self.hlay_bottom.addWidget(kz_btn)
        norma_btn.clicked.connect(self._norma_state)
        fire_btn.clicked.connect(self._b_31_state)
        noise_btn.clicked.connect(self._b_13_state)
        break_btn.clicked.connect(self._b_14_state)
        kz_btn.clicked.connect(self._b_15_state)

    def set_btn_mkz(self):
        norma_btn = self.btns.btn_norma(self)
        kz_btn = self.btns.btn_kz(self)
        switch_btn = self.btns.btn_swich(self)
        self.hlay_top.addWidget(norma_btn)
        self.hlay_top.addWidget(switch_btn)
        self.hlay_bottom.addWidget(kz_btn)
        norma_btn.clicked.connect(self._norma_state)
        kz_btn.clicked.connect(self._b_30_state)
        switch_btn.clicked.connect(self._b_31_state)

    def set_btn_amk(self):
        norma_btn = self.btns.btn_norma(self)
        alarm_btn = self.btns.btn_alarm(self)
        self.hlay_top.addWidget(norma_btn)
        self.hlay_bottom.addWidget(alarm_btn)
        norma_btn.clicked.connect(self._norma_state)
        alarm_btn.clicked.connect(self._b_31_state)

    def set_btn_ati(self):
        norma_btn = self.btns.btn_norma(self)
        fire_btn = self.btns.btn_fire(self)
        diff_fire_btn = self.btns.btn_diff_fire(self)
        self.hlay_top.addWidget(norma_btn)
        self.hlay_top.addWidget(fire_btn)
        self.hlay_bottom.addWidget(diff_fire_btn)
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
        self.hlay_top.addWidget(norma)
        self.hlay_top.addWidget(alarm_in1)
        self.hlay_top.addWidget(alarm_in2)
        self.hlay_top.addWidget(switch)
        self.hlay_bottom.addWidget(kz_in1)
        self.hlay_bottom.addWidget(kz_in2)
        self.hlay_bottom.addWidget(break_in1)
        self.hlay_bottom.addWidget(break_in2)
        self.hlay_bottom.addWidget(kz_out1)
        self.hlay_bottom.addWidget(kz_out2)
        self.hlay_bottom.addWidget(break_out1)
        self.hlay_bottom.addWidget(break_out2)
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
        row = self.ui.output_table.currentRow()
        column = self.ui.output_table.currentColumn()
        type_sensor = self.ui.output_table.item(row, column).text().split()[0]
        self._clear_layouts()
        if 0 < int(type_sensor) < 20:
            self.set_btn_modbus()
        else:
            match int(type_sensor):
                case 65:  # МКЗ
                    self.set_btn_mkz()
                case 60:  # ИР
                    self.set_btn_ir()
                case 51: #A2ДПИ
                    self.set_btn_a2dpi()
                case 54: #АР1
                    self.set_btn_ar1()
                case 53: #АМК
                    self.set_btn_amk()
                case 57: #АТИ
                    self.set_btn_ati()
                case 61: #ИСМ5
                    self._set_btn_ism5()

    def _clear_layouts(self):
        num_widget_top = self.hlay_top.count()
        num_widget_bottom = self.hlay_bottom.count()
        if num_widget_top > 0:
            for i in reversed(range(num_widget_top)):
                ch = self.hlay_top.takeAt(i)
                ch.widget().deleteLater()
        if num_widget_bottom > 0:
            for i in reversed(range(num_widget_bottom)):
                ch = self.hlay_bottom.takeAt(i)
                ch.widget().deleteLater()

    def _set_parameters(self):
        params_conn = get_conn_from_file()
        self.ui.host_db_lineEdit.setText(params_conn["host"])
        self.ui.port_db_lineEdit.setText(params_conn["port"])
        self.ui.user_db_lineEdit.setText(params_conn["user"])
        self.ui.pass_db_lineEdit.setText(params_conn["password"])
        self.ui.name_db_lineEdit.setText(params_conn["name"])
        self.ui.sn_emulator_lineEdit.setText("641")

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

    def _fill_table(self):
        output_data_sensors = handler_devices(self._get_params_conn(), self.ports_net_devs)
        num_rows = len(output_data_sensors)
        self.ui.output_table.setRowCount(num_rows)
        self.ui.output_table.setColumnCount(130)
        # self.ui.output_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.output_table.setHorizontalHeaderLabels(["PORT", "Net-Dev"] + [str(i) for i in range(1, 130)])
        for num_row in range(num_rows):
            sensors = []
            row = output_data_sensors[num_row]
            #{'port': 'COM6', 'net_device': 'КАУ03Д->5843', 'net_dev': 'KAU03DConfig',
            # 'sensors': [{'type': 51, 'state': 'N', 'slave': 1, 'threshold': '15', 'serialnumber': '10'},...
            self.ui.output_table.setItem(num_row, 0, QTableWidgetItem(row["port"]))
            self.ui.output_table.item(num_row, 0,).setForeground(QColor(255, 255, 255))
            self.ui.output_table.setItem(num_row, 1, QTableWidgetItem(row["net_device"]))
            for num_sensor in range(len(row["sensors"])):
                num_column = num_sensor + 2
                sensor = row["sensors"][num_sensor]
                self.ui.output_table.setItem(
                    num_row, num_column,
                    QTableWidgetItem(f'{sensor["type"]} {sensor["state"]} {sensor["slave"]}'))
                self.ui.output_table.item(num_row, num_column).setBackground(QColor(157, 242, 160))

                sensor_tool_tip = create_toll_tip(sensor)
                self.ui.output_table.item(num_row, num_column).setToolTip(sensor_tool_tip)
                sensor["row"] = num_row
                sensor["column"] = num_column
                sensors.append(sensor)
            if row["net_dev"] == "KAU03DConfig":
                thread: ServerAH = ServerAH(sensors, row["port"])
            else:
                thread: ServerMB = ServerMB(sensors, row["port"])
            thread.start()
            self.servers.append(thread)
        self.ui.tabWidget.setCurrentWidget(self.ui.main_tab)
        self.ui.output_table.sortItems(0, order=Qt.SortOrder.AscendingOrder)
        self.ui.output_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

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
        try:
            row_port = self.ui.ports_listWidget.currentRow()
            row_net_device = self.ui.net_dev_listWidget.currentRow()
            if row_port < 0 or row_net_device < 0:
                raise IndexError
            port = self.ports[row_port][0]
            for dev_i in self.net_devices:
                if dev_i[2] == self.net_devices[row_net_device][2]:
                    net_device = dev_i[2]
                    if check_join_table_output(port, net_device, self.ports_net_devs):
                        cur_row = self.ui.port_and_net_dev_tableWidget.rowCount() + 1
                        self.ui.port_and_net_dev_tableWidget.setRowCount(cur_row)
                        self.ui.port_and_net_dev_tableWidget.setColumnCount(2)
                        self.ui.port_and_net_dev_tableWidget.setHorizontalHeaderLabels(["port", "net device"])
                        self.ui.port_and_net_dev_tableWidget.setItem(cur_row-1, 0, QTableWidgetItem(port))
                        self.ui.port_and_net_dev_tableWidget.setItem(cur_row-1, 1, QTableWidgetItem(net_device))
                        self.ports_net_devs.append((port, net_device, dev_i))
                        self.ui.ports_listWidget.currentItem().setBackground(QColor("red"))
                        self.ui.net_dev_listWidget.currentItem().setBackground(QColor("red"))
                    break
        except IndexError:
            err_selection(self)

    def _clear_table_ports_net_dev(self):
        self.ui.port_and_net_dev_tableWidget.clear()

    def _get_item_from_table(self):
        dev = []
        for row in range(self.ui.port_and_net_dev_tableWidget.rowCount()):
            dev.append((self.ui.port_and_net_dev_tableWidget.item(row, 0).text(),
                        self.ui.port_and_net_dev_tableWidget.item(row, 1).text()))
        return dev

    def _set_tool_tip(self, params):
        for server in self.servers:
            if server.name == self.ui.output_table.item(params["row"], 0).text():
                for sensor in server.sensors:
                    if sensor["slave"] == params["slave"]:
                        sensor["state"] = params["state"]
                        sensor_tool_tip = create_toll_tip(sensor)
                        return sensor_tool_tip
        logger.info(f"Ошибка создания ToolTip  {params}")

    def _norma_state_mb(self):
        params = self._get_current_params()
        row = params["row"]
        column = params["column"]
        params["state"] = "N"
        port = self.ui.output_table.item(row, 0).text()
        sensor_tool_tip = self._set_tool_tip(params)
        self.ui.output_table.setItem(row, column, QTableWidgetItem(f'{params["type"]} N {params["slave"]}'))
        self.ui.output_table.item(row, column).setBackground(QColor(157, 242, 160))
        self.ui.output_table.item(row, column).setToolTip(sensor_tool_tip)
        self._send_in_thread(port, params)

    def _norma_state(self):
        params = self._get_current_params()
        row = params["row"]
        column = params["column"]
        params["state"] = "N"
        params["err"] = None
        port = self.ui.output_table.item(row, 0).text()
        sensor_tool_tip = self._set_tool_tip(params)
        self.ui.output_table.setItem(row, column, QTableWidgetItem(f'{params["type"]} N {params["slave"]}'))
        self.ui.output_table.item(row, column).setBackground(QColor(157, 242, 160))
        self.ui.output_table.item(row, column).setToolTip(sensor_tool_tip)
        self._send_in_thread(port, params)

    def _b_31_state(self):
        params = self._get_current_params()
        row = params["row"]
        column = params["column"]
        params["state"] = "F"
        params["err"] = None
        port = self.ui.output_table.item(row, 0).text()
        sensor_tool_tip = self._set_tool_tip(params)
        self.ui.output_table.setItem(row, column, QTableWidgetItem(f'{params["type"]} F {params["slave"]}'))
        self.ui.output_table.item(row, column).setBackground(QColor(173, 0, 0))
        self.ui.output_table.item(row, column).setToolTip(sensor_tool_tip)
        self._send_in_thread(port, params)

    def _b_30_state(self):
        params = self._get_current_params()
        row = params["row"]
        column = params["column"]
        params["state"] = "E"
        params["err"] = 30
        port = self.ui.output_table.item(row, 0).text()
        sensor_tool_tip = self._set_tool_tip(params)
        self.ui.output_table.setItem(row, column, QTableWidgetItem(f'{params["type"]} E {params["slave"]}'))
        self.ui.output_table.item(row, column).setBackground(QColor(255, 140, 0))
        self.ui.output_table.item(row, column).setToolTip(sensor_tool_tip)
        self._send_in_thread(port, params)

    def _b_29_state(self):
        params = self._get_current_params()
        row = params["row"]
        column = params["column"]
        params["state"] = "E"
        params["err"] = 29
        port = self.ui.output_table.item(row, 0).text()
        sensor_tool_tip = self._set_tool_tip(params)
        self.ui.output_table.setItem(row, column, QTableWidgetItem(f'{params["type"]} E {params["slave"]}'))
        self.ui.output_table.item(row, column).setBackground(QColor(255, 140, 0))
        self.ui.output_table.item(row, column).setToolTip(sensor_tool_tip)
        self._send_in_thread(port, params)

    def _b_27_state(self):
        params = self._get_current_params()
        row = params["row"]
        column = params["column"]
        params["state"] = "E"
        params["err"] = 27
        port = self.ui.output_table.item(row, 0).text()
        sensor_tool_tip = self._set_tool_tip(params)
        self.ui.output_table.setItem(row, column, QTableWidgetItem(f'{params["type"]} E {params["slave"]}'))
        self.ui.output_table.item(row, column).setBackground(QColor(255, 140, 0))
        self.ui.output_table.item(row, column).setToolTip(sensor_tool_tip)
        self._send_in_thread(port, params)

    def _b_15_state(self):
        params = self._get_current_params()
        row = params["row"]
        column = params["column"]
        params["state"] = "E"
        params["err"] = 15
        port = self.ui.output_table.item(row, 0).text()
        sensor_tool_tip = self._set_tool_tip(params)
        self.ui.output_table.setItem(row, column, QTableWidgetItem(f'{params["type"]} E {params["slave"]}'))
        self.ui.output_table.item(row, column).setBackground(QColor(255, 140, 0))
        self.ui.output_table.item(row, column).setToolTip(sensor_tool_tip)
        self._send_in_thread(port, params)

    def _b_14_state(self):
        params = self._get_current_params()
        row = params["row"]
        column = params["column"]
        params["state"] = "E"
        params["err"] = 14
        port = self.ui.output_table.item(row, 0).text()
        sensor_tool_tip = self._set_tool_tip(params)
        self.ui.output_table.setItem(row, column, QTableWidgetItem(f'{params["type"]} E {params["slave"]}'))
        self.ui.output_table.item(row, column).setBackground(QColor(255, 140, 0))
        self.ui.output_table.item(row, column).setToolTip(sensor_tool_tip)
        self._send_in_thread(port, params)

    def _b_13_state(self):
        params = self._get_current_params()
        row = params["row"]
        column = params["column"]
        params["state"] = "E"
        params["err"] = 13
        port = self.ui.output_table.item(row, 0).text()
        sensor_tool_tip = self._set_tool_tip(params)
        self.ui.output_table.setItem(row, column, QTableWidgetItem(f'{params["type"]} E {params["slave"]}'))
        self.ui.output_table.item(row, column).setBackground(QColor(255, 140, 0))
        self.ui.output_table.item(row, column).setToolTip(sensor_tool_tip)
        self._send_in_thread(port, params)

    def _b_12_state(self):
        params = self._get_current_params()
        row = params["row"]
        column = params["column"]
        params["state"] = "E"
        params["err"] = 12
        port = self.ui.output_table.item(row, 0).text()
        sensor_tool_tip = self._set_tool_tip(params)
        self.ui.output_table.setItem(row, column, QTableWidgetItem(f'{params["type"]} E {params["slave"]}'))
        self.ui.output_table.item(row, column).setBackground(QColor(255, 140, 0))
        self.ui.output_table.item(row, column).setToolTip(sensor_tool_tip)
        self._send_in_thread(port, params)

    def _b_11_state(self):
        params = self._get_current_params()
        row = params["row"]
        column = params["column"]
        params["state"] = "E"
        params["err"] = 11
        port = self.ui.output_table.item(row, 0).text()
        sensor_tool_tip = self._set_tool_tip(params)
        self.ui.output_table.setItem(row, column, QTableWidgetItem(f'{params["type"]} E {params["slave"]}'))
        self.ui.output_table.item(row, column).setBackground(QColor(255, 140, 0))
        self.ui.output_table.item(row, column).setToolTip(sensor_tool_tip)
        self._send_in_thread(port, params)

    def _b_7_state(self):
        params = self._get_current_params()
        row = params["row"]
        column = params["column"]
        params["state"] = "E"
        params["err"] = 7
        port = self.ui.output_table.item(row, 0).text()
        sensor_tool_tip = self._set_tool_tip(params)
        self.ui.output_table.setItem(row, column, QTableWidgetItem(f'{params["type"]} E {params["slave"]}'))
        self.ui.output_table.item(row, column).setBackground(QColor(255, 140, 0))
        self.ui.output_table.item(row, column).setToolTip(sensor_tool_tip)
        self._send_in_thread(port, params)

    def _b_6_state(self):
        params = self._get_current_params()
        row = params["row"]
        column = params["column"]
        params["state"] = "E"
        params["err"] = 6
        port = self.ui.output_table.item(row, 0).text()
        sensor_tool_tip = self._set_tool_tip(params)
        self.ui.output_table.setItem(row, column, QTableWidgetItem(f'{params["type"]} E {params["slave"]}'))
        self.ui.output_table.item(row, column).setBackground(QColor(255, 140, 0))
        self.ui.output_table.item(row, column).setToolTip(sensor_tool_tip)
        self._send_in_thread(port, params)

    def _b_5_state(self):
        params = self._get_current_params()
        row = params["row"]
        column = params["column"]
        params["state"] = "E"
        params["err"] = 5
        port = self.ui.output_table.item(row, 0).text()
        sensor_tool_tip = self._set_tool_tip(params)
        self.ui.output_table.setItem(row, column, QTableWidgetItem(f'{params["type"]} E {params["slave"]}'))
        self.ui.output_table.item(row, column).setBackground(QColor(255, 140, 0))
        self.ui.output_table.item(row, column).setToolTip(sensor_tool_tip)
        self._send_in_thread(port, params)

    def _b_4_state(self):
        params = self._get_current_params()
        row = params["row"]
        column = params["column"]
        params["state"] = "E"
        params["err"] = 4
        port = self.ui.output_table.item(row, 0).text()
        sensor_tool_tip = self._set_tool_tip(params)
        self.ui.output_table.setItem(row, column, QTableWidgetItem(f'{params["type"]} E {params["slave"]}'))
        self.ui.output_table.item(row, column).setBackground(QColor(255, 140, 0))
        self.ui.output_table.item(row, column).setToolTip(sensor_tool_tip)
        self._send_in_thread(port, params)

    def _b_3_state(self):
        params = self._get_current_params()
        row = params["row"]
        column = params["column"]
        params["state"] = "E"
        params["err"] = 3
        port = self.ui.output_table.item(row, 0).text()
        sensor_tool_tip = self._set_tool_tip(params)
        self.ui.output_table.setItem(row, column, QTableWidgetItem(f'{params["type"]} E {params["slave"]}'))
        self.ui.output_table.item(row, column).setBackground(QColor(255, 140, 0))
        self.ui.output_table.item(row, column).setToolTip(sensor_tool_tip)
        self._send_in_thread(port, params)

    def _b_2_state(self):
        params = self._get_current_params()
        row = params["row"]
        column = params["column"]
        params["state"] = "E"
        params["err"] = 2
        port = self.ui.output_table.item(row, 0).text()
        sensor_tool_tip = self._set_tool_tip(params)
        self.ui.output_table.setItem(row, column, QTableWidgetItem(f'{params["type"]} E {params["slave"]}'))
        self.ui.output_table.item(row, column).setBackground(QColor(255, 140, 0))
        self.ui.output_table.item(row, column).setToolTip(sensor_tool_tip)
        self._send_in_thread(port, params)

    def _get_current_params(self) -> dict:
        """Получить значение выделенной ячейки
        Возвращает словарь {'type': 1, 'state': 'N', 'slave': 4, 'row': 0, 'column': 2}"""
        r: int = self.ui.output_table.currentRow()
        c: int = self.ui.output_table.currentColumn()
        if r < 0 or c < 0:
            raise ValueError
        if c != 1:
            item = self.ui.output_table.item(r, c).text().split(" ")
            return {'type': int(item[0]), 'state': item[1], 'slave': int(item[2]), 'row': r, 'column': c}

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
