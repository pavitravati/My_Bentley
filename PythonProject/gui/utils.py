from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtGui import QFont
from PySide6.QtCore import QSize

# Used to create the item put into the table with the correct font
def make_item(text):
    item = QTableWidgetItem(text)
    font = QFont("Arial", 9)
    item.setFont(font)

    return item