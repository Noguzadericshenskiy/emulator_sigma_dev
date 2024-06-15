from PySide6.QtWidgets import QMessageBox


title_err_select_sensor = "Error select"
text_err_select_sensor = """
< p style = 'color: white;' > Выбрана пустая ячейка!\n
Необходимо выбрать датчик.< / p >
"""


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

# def err_message(parent, title, text_msg):
#     QMessageBox.critical(parent, title, text_msg, buttons=QMessageBox.Discard, defaultButton=QMessageBox.Discard)
