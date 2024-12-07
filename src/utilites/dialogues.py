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


def error_update(parent, err):
    title = "Error update"
    text_err = None

    if err.args[0] == "No selecton SN":
        text_err = "Не задан серийный номер эмулятора"
    elif err.args[0] == "No selection port":
        text_err = "Не выбран COM порт"
    else:
        text_err = "Не выбран файл.\nНеобходимо выбрать файл"

    QMessageBox.critical(
        parent,
        title,
        text_err,
        buttons=QMessageBox.Discard,
        defaultButton=QMessageBox.Discard,
    )


def error_add_sensor(parent):
    QMessageBox.critical(
        parent,
        "Adding error device",
        f"< p style = 'color: red;' >В конфигурации не поддерживаемый \nизвещатель или устройство\n"
        "Необходимо проверить конфигурацию.\n< / p >",
        buttons=QMessageBox.Discard,
        defaultButton=QMessageBox.Discard,
    )

