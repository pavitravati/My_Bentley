from PySide6.QtWidgets import (
    QStyledItemDelegate
)

# Class that allows for padding to be added to items
class PaddingDelegate(QStyledItemDelegate):
    def __init__(self, left=10, top=20, right=0, bottom=20, parent=None):
        super().__init__(parent)
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom

    # Applies the padding to the item
    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        option.rect.adjust(self.left, self.top, -self.right, -self.bottom)