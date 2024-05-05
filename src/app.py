import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QTableWidgetItem

from src.ui.main_win import Ui_MainWindow
from src.utilites.setup import (
    NumbersIPValidator,
    PortValidator,
    get_ports_info,
    get_net_devices,
    check_join_table_output,
    save_conn_to_file,
    check_file,
    get_conn_from_file
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Эмулятор датчиков Modbus")
        self.ports = []
        self.net_devices = []
        self.ports_net_devs = []
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        check_file()
        self._set_parameters()
        self.ui.get_ports_btn.clicked.connect(self._output_ports)
        self.ui.get_net_dev_btn.clicked.connect(self._output_net_devices)
        self.ui.join_btn.clicked.connect(self._join_port_and_net_device)
        self.ui.save_db_btn.clicked.connect(self._save_params_conn)
        self.ui.host_db_lineEdit.setValidator(NumbersIPValidator())
        self.ui.port_db_lineEdit.setValidator(PortValidator())

    def _set_parameters(self):
        params_conn = get_conn_from_file()
        self.ui.host_db_lineEdit.setText(params_conn["host"])
        self.ui.port_db_lineEdit.setText(params_conn["port"])
        self.ui.user_db_lineEdit.setText(params_conn["user"])
        self.ui.pass_db_lineEdit.setText(params_conn["password"])
        self.ui.name_db_lineEdit.setText(params_conn["name"])

    def _check_connect(self):
        ...

    def _save_params_conn(self):
        host = self.ui.host_db_lineEdit.text()
        port = self.ui.port_db_lineEdit.text()
        user = self.ui.user_db_lineEdit.text()
        password = self.ui.pass_db_lineEdit.text()
        name_db = self.ui.user_db_lineEdit.text()
        parameters = {"user": user, "password": password, "name": name_db, "host": host, "port": port}
        save_conn_to_file(parameters)

    def _output_ports(self):
        self.ui.ports_listWidget.clear()
        self.ports = get_ports_info()
        for i in self.ports:
            # self.ui.ports_listWidget.itemWidget(QListWidgetItem("i"))
            self.ui.ports_listWidget.addItem(QListWidgetItem(i[1]))

    def _output_net_devices(self):
        self.ui.net_dev_listWidget.clear()
        self.net_devices = get_net_devices()
        for net_dev in self.net_devices:
            self.ui.net_dev_listWidget.addItem(QListWidgetItem(net_dev))

    def _join_port_and_net_device(self):
        row_port = self.ui.ports_listWidget.currentRow()
        row_net_device = self.ui.net_dev_listWidget.currentRow()
        port = self.ports[row_port][0]
        net_device = self.net_devices[row_net_device]

        if check_join_table_output(port, net_device, self.ports_net_devs):
            cur_row = self.ui.port_and_net_dev_tableWidget.rowCount() + 1
            self.ui.port_and_net_dev_tableWidget.setRowCount(cur_row)
            self.ui.port_and_net_dev_tableWidget.setColumnCount(2)

            self.ui.port_and_net_dev_tableWidget.setHorizontalHeaderLabels(["port", "net device"])
            self.ui.port_and_net_dev_tableWidget.setItem(cur_row-1, 0, QTableWidgetItem(port))
            self.ui.port_and_net_dev_tableWidget.setItem(cur_row-1, 1, QTableWidgetItem(net_device))
            self.ports_net_devs.append((port, net_device))

    def _clear_table_ports_net_dev(self):
        self.ui.port_and_net_dev_tableWidget.clear()



if __name__ == "__main__":
    app = QApplication([])
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
