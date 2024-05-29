from PySide6.QtWidgets import QMessageBox

title_err_select_sensor = "Error select"
text_err_select_sensor = """
< p style = 'color: white;' > Выбрана пустая ячейка!\n
Необходимо выбрать датчик.< / p >
"""





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


def err_message(parent, title, text_msg):
    QMessageBox.critical(parent, title, text_msg, buttons=QMessageBox.Discard, defaultButton=QMessageBox.Discard)
