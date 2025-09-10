from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QTableWidget, QTableWidgetItem, QLabel, QStyledItemDelegate,
    QStatusBar, QToolBar, QSizePolicy, QCheckBox, QPushButton
)
from PySide6.QtGui import QFont, QAction, QBrush, QColor
from PySide6.QtCore import Qt, QTimer
from excel import testCases, services
from PIL import Image
import random
import sys
import os

directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(directory, 'Test_Scripts'))
from Android_TestCase import *

class PaddingDelegate(QStyledItemDelegate):
    def __init__(self, left=10, top=0, right=0, bottom=0, parent=None):
        super().__init__(parent)
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom

    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        option.displayAlignment = option.displayAlignment
        option.rect.adjust(self.left, self.top, -self.right, -self.bottom)

class TestCaseTablePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)

        title = QLabel("Remote Lock/Unlock")
        title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setStyleSheet("margin-left: 20px; margin-bottom: 20px;")
        layout.addWidget(title)

        main_button = QPushButton("Begin Automated Test")
        main_button.setStyleSheet("margin-bottom: 20px;")
        main_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        main_button.clicked.connect(self.simulate_test)
        layout.addWidget(main_button)



        # Create the table
        self.table = QTableWidget()
        self.table.setColumnCount(8)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setAlternatingRowColors(True)
        self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.table.setStyleSheet("""
            QTableWidget::item:hover {
                background-color: #ececed;
            }
            QTableWidget::item:selected {
                background-color: #ececed;
                color: black;
            }
        """)
        self.table.setHorizontalHeaderLabels(["Region", "Test Case Description", "Pre-Condition", "Action", "Expected Result", "Duration", "Result", "Error"])
        self.table.setRowCount(len(testCases))

        for row in range(self.table.rowCount()):
            self.table.setRowHeight(row, 100)

        font = QFont("Arial", 9)
        header_font = QFont("Arial", 8)
        header_font.setBold(True)
        self.table.horizontalHeader().setFont(header_font)
        self.table.verticalHeader().setFont(header_font)

        for row, case in enumerate(testCases):
            self.table.setItem(row, 0, make_item(case["Region"]))
            self.table.setItem(row, 1, make_item(case["Test Case Description"]))

            # precondition_string = "\n".join(str(task) for task in case["Pre-Condition"])
            # checkbox = QCheckBox("Preconditions Met")
            # checkbox.setCheckState(Qt.CheckState.Checked)
            # checkbox.stateChanged.connect(self.show_state)
            # self.table.setCellWidget(row, 2, checkbox)

            precondition_widget = QWidget()
            precondition_layout = QVBoxLayout()
            precondition_layout.setContentsMargins(0, 0, 0, 0)
            precondition_layout.setSpacing(5)

            checkboxes = []

            for precondition in case["Pre-Condition"]:
                checkbox = QCheckBox(precondition)
                checkbox.setChecked(False)
                checkbox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
                checkboxes.append(checkbox)
                precondition_layout.addWidget(checkbox)

            if len(case["Pre-Condition"]) > 0:
                action_button = QPushButton("Run Testcase")
                action_button.setEnabled(False)  # Initially disabled
                action_button.setStyleSheet("margin-top: 2px; margin-right: 10px;")
                action_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
                action_button.clicked.connect(lambda _, r=row: self.precondition_button_clicked(r))

                def update_button_state():
                    all_checked = all(cb.isChecked() for cb in checkboxes)
                    action_button.setEnabled(all_checked)

                for cb in checkboxes:
                    cb.stateChanged.connect(update_button_state)

                precondition_layout.addWidget(action_button)

            precondition_widget.setLayout(precondition_layout)
            precondition_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.table.setCellWidget(row, 2, precondition_widget)

            # self.table.setItem(row, 2, make_item(precondition_string))
            action_string = "\n".join(str(task) for task in case["Action"])
            self.table.setItem(row, 3, make_item(action_string))
            expected_string = "\n".join(str(task) for task in case["Expected Result"])
            self.table.setItem(row, 4, make_item(expected_string))
            self.table.setItem(row, 5, make_item(""))
            self.table.setItem(row, 6, make_item(""))
            self.table.setItem(row, 7, make_item(""))

        for row in range(self.table.rowCount()):
            for col in range(2):
                self.table.item(row, col).setTextAlignment(Qt.AlignCenter)
            for col in range(3):
                self.table.item(row, col+5).setTextAlignment(Qt.AlignCenter)


        delegate = PaddingDelegate()
        for col in range(3):
            self.table.setItemDelegateForColumn(col+2, delegate)


        layout.addWidget(self.table)
        QTimer.singleShot(0, self.adjust_column_widths)

    def adjust_column_widths(self):
        total_width = self.table.viewport().width()

        percentages = [0.07, 0.33, 0.18, 0.31, 0.46, 0.07, 0.07, 0.07]
        for col, percent in enumerate(percentages):
            width = int(total_width * percent)
            self.table.setColumnWidth(col, width)

    # When app is working this runs the testcase for that row. Build on this to show results/process
    # def precondition_button_clicked(self, row):
    #     print(f"Execute button clicked for row {row}")
    #     func_name = f"Remote_Lock_Unlock00{row}"
    #     func = globals().get(func_name)
    #     if func:
    #         func()

    def precondition_button_clicked(self, row):
        self.temp_row = 5
        self.current_row = 0
        self.table.item(row, 3).setForeground(QBrush(QColor("green")))
        QTimer.singleShot(1000, self.failed)


    def failed(self):
        text = "The action should perform and Door arming alarm should be played\nApp should be notified with an appropriate message\nThe status of the lock should be updated\nPush notification received in app"
        lines = text.split("\n")
        coloured_text = f"<span style='color: green;'>{lines[0]}</span><br>" \
                        f"<span style='color: green;'>{lines[1]}</span><br>" \
                        f"<span style='color: red;'>{lines[2]}</span><br>" \
                        f"<span style='color: green;'>{lines[3]}</span>"
        label = QLabel()
        label.setTextFormat(Qt.TextFormat.RichText)
        label.setText(coloured_text)
        self.table.setCellWidget(2, 4, label)
        self.current_column = 5
        QTimer.singleShot(1000, self.simulate_next_cell)

    def simulate_test(self):
        self.current_row = 0
        self.current_column = 3
        self.temp_row = 0
        self.simulate_next_cell()

    def simulate_next_cell(self):
        if self.current_row >= self.table.rowCount()-1 and self.temp_row != 5:
            return

        if self.temp_row == 5:
            self.current_row = 2

        header = self.table.horizontalHeaderItem(self.current_column).text()
        if header == "Action" or header == "Expected Result":
            item = self.table.item(self.current_row, self.current_column)
            item.setForeground(QBrush(QColor("green")))
        elif header == "Duration":
            random_duration = random.uniform(2, 5)
            self.table.item(self.current_row, self.current_column).setText(str(round(random_duration,2)))
        elif header == "Result":
            if self.temp_row:
                self.table.item(self.current_row, self.current_column).setText("Fail")
                self.table.item(self.current_row, self.current_column).setForeground(QBrush(QColor("white")))
                self.table.item(self.current_row, self.current_column).setBackground(QColor("red"))
            else:
                self.table.item(self.current_row, self.current_column).setText("Pass")
                self.table.item(self.current_row, self.current_column).setForeground(QBrush(QColor("white")))
                self.table.item(self.current_row, self.current_column).setBackground(QColor("green"))
        elif header == "Error":
            if self.temp_row == 5:
                error_button = QPushButton("Error")
                error_button.setStyleSheet("margin-top: 2px; margin-right: 10px;")
                error_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
                error_button.clicked.connect(self.error_img)
                self.table.setCellWidget(2,7, error_button)

        if self.current_column < 7:
            self.current_column += 1
            QTimer.singleShot(1000, self.simulate_next_cell)
        else:
            self.current_row += 1
            self.current_column = 3
            QTimer.singleShot(1000, self.simulate_next_cell)

    def error_img(self):
        image = Image.open("../resource/temp.png")
        image.show()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Test Case Viewer")
        self.setStyleSheet("background-color: white;")

        # Set the test case table as the central widget
        self.setCentralWidget(TestCaseTablePage())

        toolbar = QToolBar("Services")
        self.addToolBar(toolbar)

        for service in services:
            button_action = QAction(service, self)
            button_action.setStatusTip(f"{service} button")
            button_action.triggered.connect(self.toolbar_button_clicked)
            button_action.setCheckable(True)
            toolbar.addAction(button_action)

        self.setStatusBar(QStatusBar(self))

    def toolbar_button_clicked(self, s):
        print("click", s)

def make_item(text):
    item = QTableWidgetItem(text)
    font = QFont("Arial", 9)
    item.setFont(font)
    return item

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec())