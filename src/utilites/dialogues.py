from PySide6.QtWidgets import QMessageBox


def err_connect(parent):
    QMessageBox.critical(
        parent,
        "Error connect on data base",
        "Ошибка подключения к базе данных\n "
        "Проверьте настройки подключения.\n",
        buttons=QMessageBox.Discard,
        defaultButton=QMessageBox.Discard,
    )
