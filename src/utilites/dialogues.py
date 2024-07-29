import loguru
from PySide6.QtWidgets import QMessageBox, QFileDialog


title_err_select_sensor = "Error select"
text_err_select_sensor = """
< p style = 'color: white;' > Выбрана пустая ячейка!\n
Необходимо выбрать датчик.< / p >
"""


def open_file(parent):
    title = "Open file"
    directory = r'C:\User\Home\Downloads'
    filter_files = "*flash"
    # filter_files = "*csv; *bom"
    # file_path.getOpenFileNames(parent, title, directory, filter_files)[0]
    file_path = QFileDialog(parent).getOpenFileName(parent, title, directory, filter_files)
    if file_path:
        return file_path[0]


def ok_connect(parent):
    QMessageBox.information(
        parent,
        "Проверка подключения",
        "Подключение к БД проверено, \nнастройки правильные!",
        buttons=QMessageBox.StandardButton.Close
        # buttons=QMessageBox.StandardButton.Ok,
        # defaultButton=QMessageBox.StandardButton.Ok
    )


def err_connect(parent):
    QMessageBox.critical(
        parent,
        "Error connect on data base",
        "Ошибка подключения к базе данных\n "
        "Проверьте настройки подключения.\n",
        buttons=QMessageBox.Discard,
        defaultButton=QMessageBox.Discard,
    )


def err_selection(parent):
    QMessageBox.critical(
        parent,
        "Error selecting a port or net device",
        "< p style = 'color: white;' > Не выбран COM порт или сетевой контроллер\n" 
        "Необходимо выбрать порт и сетевой контроллер.\n< / p >",
        buttons=QMessageBox.Discard,
        defaultButton=QMessageBox.Discard,
    )


def err_selection_port_net_dev(parent):
    QMessageBox.critical(
        parent,
        "Error selecting port/net device",
        "< p style = 'color: white;' > Не выбрана запись для удаления\n"
        "Необходимо выбрать строку для удаления.\n< / p >",
        buttons=QMessageBox.Discard,
        defaultButton=QMessageBox.Discard,
    )

def err_set_fire(parent):
    QMessageBox.critical(
        parent,
        "Error set state sensor fire ",
        "< p style = 'color: white;' > У этого устройства нельзя установить режим ПОЖАР\n" 
        "Для данного типа устройства доступны состояния НОРМА и НЕИСПРАВНОСТЬ\n< / p >",
        buttons=QMessageBox.Discard,
        defaultButton=QMessageBox.Discard,
    )

# def err_message(parent, title, text_msg):
#     QMessageBox.critical(parent, title, text_msg, buttons=QMessageBox.Discard, defaultButton=QMessageBox.Discard)
