from PySide6.QtGui import QColor, Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QListWidgetItem,
    QTableWidgetItem,
    QAbstractItemView)
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


class MainWindow(QMainWindow):
    def __init__(self):
        self.servers = []
        super().__init__()
        self.setWindowTitle("Эмулятор датчиков Modbus")
        self.ports = []
        self.net_devices = []
        self.ports_net_devs = []
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        check_file()
        self._set_parameters()
        self.ui.check_db_btn.clicked.connect(self._check_connect)
        self.ui.send_table_btn.clicked.connect(self._fill_table)
        self.ui.get_ports_btn.clicked.connect(self._output_ports)
        self.ui.get_net_dev_btn.clicked.connect(self._output_net_devices)
        self.ui.join_btn.clicked.connect(self._join_port_and_net_device)
        self.ui.save_db_btn.clicked.connect(self._save_params_conn)
        self.ui.delete_line_btn.clicked.connect(self._delet_line)
        self.ui.normal_btn.clicked.connect(self._norma_btn)
        self.ui.fire_btn.clicked.connect(self._fire_btn)
        self.ui.failure_btn.clicked.connect(self._failure_btn)
        self.ui.host_db_lineEdit.setValidator(NumbersIPValidator())
        self.ui.port_db_lineEdit.setValidator(PortValidator())

    def _set_parameters(self):
        params_conn = get_conn_from_file()
        self.ui.host_db_lineEdit.setText(params_conn["host"])
        self.ui.port_db_lineEdit.setText(params_conn["port"])
        self.ui.user_db_lineEdit.setText(params_conn["user"])
        self.ui.pass_db_lineEdit.setText(params_conn["password"])
        self.ui.name_db_lineEdit.setText(params_conn["name"])
        self.ui.break_r_btn.click()

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
        """"""
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
                # self.ui.output_table.item(num_row, num_column).setToolTip(
                #     f"< p style = 'color: blue;' >s/n {sensor['serialnumber']}< / p >")
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

    def _norma_btn(self):
        sensor_params = self._get_current_params()
        self._set_status_norma(sensor_params)

    def _fire_btn(self):
        sensor_params = self._get_current_params()
        self._set_status_fire(sensor_params)

    def _failure_btn(self):
        sensor_params = self._get_current_params()
        self._set_status_failure(sensor_params)

    def _set_status_norma(self, params: dict):
        row = params["row"]
        column = params["column"]
        port = self.ui.output_table.item(row, 0).text()
        self.ui.output_table.setItem(row, column, QTableWidgetItem(f'{params["type"]} N {params["slave"]}'))
        self.ui.output_table.item(row, column).setBackground(QColor(157, 242, 160))
        params["state"] = "N"
        params["err"] = None
        self._send_in_thread(port, params)

    def _set_status_fire(self, params: dict):
        row = params["row"]
        column = params["column"]
        port = self.ui.output_table.item(row, 0).text()
        self.ui.output_table.setItem(row, column, QTableWidgetItem(f'{params["type"]} F {params["slave"]}'))
        self.ui.output_table.item(row, column).setBackground(QColor(255, 0, 0))
        params["state"] = "F"
        params["err"] = None
        self._send_in_thread(port, params)

    def _set_status_failure(self, params: dict):
        row = params["row"]
        column = params["column"]
        port = self.ui.output_table.item(row, 0).text()
        self.ui.output_table.setItem(row, column, QTableWidgetItem(f'{params["type"]} E {params["slave"]}'))
        self.ui.output_table.item(row, column).setBackground(QColor(255, 140, 0))
        err = self.ui.kz_r_btn.clicked
        params["state"] = "E"
        if self.ui.kz_r_btn.isChecked():
            params["err"] = 1
        elif self.ui.break_r_btn.isChecked():
            params["err"] = 2
        elif self.ui.option_r_btn.isChecked():
            params["err"] = 3
        self._send_in_thread(port, params)
        logger.info(err)

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

    def _delet_line(self):
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
