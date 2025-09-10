from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QTableWidget, QTableWidgetItem, QLabel, QStyledItemDelegate,
    QStatusBar, QToolBar, QSizePolicy, QCheckBox, QPushButton, QHBoxLayout
)
from PySide6.QtGui import QFont, QAction, QBrush, QColor, QPixmap, QCursor
from PySide6.QtCore import Qt, QTimer
from excel import testCases, services
from PIL import Image
import random
import sys
import os

# Imports all the android testcases
directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(directory, 'Test_Scripts'))
from Android_TestCase import *

# Class that allows for padding to be added to items
class PaddingDelegate(QStyledItemDelegate):
    def __init__(self, left=10, top=0, right=0, bottom=0, parent=None):
        super().__init__(parent)
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom

    # Applies the padding to the item
    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        option.rect.adjust(self.left, self.top, -self.right, -self.bottom)

class TestCaseTablePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Adds a vertical layout for the window and sets the padding around it
        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)

        # Adds a Horizontal layout and padding that will be used for the title and logo
        top_layout = QHBoxLayout()
        top_layout.setContentsMargins(0, 40, 0, 20)

        # Creates title and adds to the horizontal layout
        title = QLabel("Remote Lock/Unlock")
        title.setFont(QFont("Arial", 25, QFont.Bold))
        title.setStyleSheet("margin-left: 20px; margin-bottom: 20px;")
        top_layout.addWidget(title)

        # Adds a space between the title and logo
        top_layout.addStretch()

        # Creates logo item and adds to the horizontal layout
        logo = QLabel()
        logo.setPixmap(QPixmap('bentleylogo.png'))
        logo.setScaledContents(True)  # Make it scale to its QLabel size
        logo.setMaximumSize(135, 50)  # Adjust as needed to avoid large empty space
        logo.setStyleSheet("margin-right: 20px;")
        top_layout.addWidget(logo)

        # Adds the horizontal layout to the main window layout
        layout.addLayout(top_layout)

        # Creates the button that will begin the automated test and adds to main layout
        main_button = QPushButton("Begin Automated Test")
        main_button.setStyleSheet("margin-bottom: 20px; margin-top: 20px; font-size: 16px; height: 30px; background-color: #394d45; color: white;")
        main_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        main_button.setCursor(Qt.PointingHandCursor)
        main_button.clicked.connect(self.simulate_test)
        layout.addWidget(main_button)

        # Create the table with 8 columns and the rows needed for all test cases
        self.table = QTableWidget()
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels(["Region", "Test Case Description", "Pre-Condition", "Action", "Expected Result", "Duration", "Result", "Error"])
        self.table.setRowCount(len(testCases))
        self.table.verticalHeader().setDefaultSectionSize(100)
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

        # Sets the font of the table headers
        header_font = QFont("Arial", 8, QFont.Bold)
        self.table.horizontalHeader().setFont(header_font)
        self.table.verticalHeader().setFont(header_font)

        # Loops through the table adding items to the correct cells
        for row, case in enumerate(testCases):
            # In column 0,1,3,4 the data from the test case in Region column is added to that column in the table
            self.table.setItem(row, 0, make_item(case["Region"]))
            self.table.setItem(row, 1, make_item(case["Test Case Description"]))

            # Does not work so need to improve logic to have the checkboxes work in precondition column
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
                action_button.setCursor(Qt.PointingHandCursor)
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


            action_string = "\n".join(str(task) for task in case["Action"])
            self.table.setItem(row, 3, make_item(action_string))
            expected_string = "\n".join(str(task) for task in case["Expected Result"])
            self.table.setItem(row, 4, make_item(expected_string))
            # Last three columns are saved for data from the tests after completion
            self.table.setItem(row, 5, make_item(""))
            self.table.setItem(row, 6, make_item(""))
            self.table.setItem(row, 7, make_item(""))

        # Centres the text in the following columns
        centre_columns = [0, 1, 5, 6, 7]
        for row in range(self.table.rowCount()):
            for col in centre_columns:
                item = self.table.item(row, col)
                if item:
                    item.setTextAlignment(Qt.AlignCenter)

        # Adds padding to certain columns
        delegate = PaddingDelegate()
        for col in range(3):
            self.table.setItemDelegateForColumn(col+2, delegate)

        # Adds the table to the main layout
        layout.addWidget(self.table)
        # Waits for table to be added and then adjusts the column widths
        QTimer.singleShot(0, self.adjust_column_widths)

    # Adjusts column widths roughly based on screen size
    def adjust_column_widths(self):
        # Gets the width of the users screen
        total_width = self.table.viewport().width()

        # Percentages are how much of the screen the column takes up
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

    # Alot of the following is all temporary just for the demo
    def precondition_button_clicked(self, row):
        self.temp_row = 5
        self.current_row = 0
        # Sets the cell on current row column 3 to have green text (demo of success)
        self.table.item(row, 3).setForeground(QBrush(QColor("green")))
        # Waits and then demos the fail example
        QTimer.singleShot(1000, self.failed)

    # Simulates a failed test case
    def failed(self):
        # This allows for the text to be split and then individually coloured so that an individual thing can fail in theory
        text = "The action should perform and Door arming alarm should be played\nApp should be notified with an appropriate message\nThe status of the lock should be updated\nPush notification received in app"
        lines = text.split("\n")
        coloured_text = f"<span style='color: green;'>{lines[0]}</span><br>" \
                        f"<span style='color: green;'>{lines[1]}</span><br>" \
                        f"<span style='color: red;'>{lines[2]}</span><br>" \
                        f"<span style='color: green;'>{lines[3]}</span>"
        # The coloured text is then added to a label and then replaces the text in that cell initially
        label = QLabel()
        label.setTextFormat(Qt.TextFormat.RichText)
        label.setText(coloured_text)
        self.table.setCellWidget(2, 4, label)
        self.current_column = 5
        # Waits and then moves on to next cell
        QTimer.singleShot(1000, self.simulate_next_cell)

    # initialises row/column number and then moves on to the cells
    def simulate_test(self):
        self.current_row = 0
        self.current_column = 3
        self.temp_row = 0
        self.simulate_next_cell()

    # This is how in the demo each cell is modified individually
    def simulate_next_cell(self):
        # Returns if you have gone past the last row assuming temp_row is not 5 as that is used for demo purposes atm
        if self.current_row >= self.table.rowCount()-1 and self.temp_row != 5:
            return

        # Demo purposes to be on the last row
        if self.temp_row == 5:
            self.current_row = 2

        # Gets the column name of current cell to allow for specific rules to be applied
        header = self.table.horizontalHeaderItem(self.current_column).text()
        # If in Action or Expected columns, the text is turned green to simulate success
        if header == "Action" or header == "Expected Result":
            item = self.table.item(self.current_row, self.current_column)
            item.setForeground(QBrush(QColor("green")))
        # In duration column a random float is added just to simulate time
        elif header == "Duration":
            random_duration = random.uniform(2, 5)
            self.table.item(self.current_row, self.current_column).setText(str(round(random_duration,2)))
        # In result column if it is fail example, it is red and fail text, otherwise it is green and pass text
        elif header == "Result":
            if self.temp_row:
                self.table.item(self.current_row, self.current_column).setText("Fail")
                self.table.item(self.current_row, self.current_column).setForeground(QBrush(QColor("white")))
                self.table.item(self.current_row, self.current_column).setBackground(QColor("red"))
            else:
                self.table.item(self.current_row, self.current_column).setText("Pass")
                self.table.item(self.current_row, self.current_column).setForeground(QBrush(QColor("white")))
                self.table.item(self.current_row, self.current_column).setBackground(QColor("green"))
        # In error column a button is created if there is a failure that currently just opens an image, future it will open diagnostics page
        elif header == "Error":
            if self.temp_row == 5:
                error_button = QPushButton("Error")
                error_button.setStyleSheet("margin-top: 2px; margin-right: 10px;")
                error_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
                error_button.clicked.connect(self.error_img)
                self.table.setCellWidget(2,7, error_button)

        # If not at final column, move to next column
        if self.current_column < 7:
            self.current_column += 1
            QTimer.singleShot(1000, self.simulate_next_cell)
        # Else move to next row and 3rd column
        else:
            self.current_row += 1
            self.current_column = 3
            QTimer.singleShot(1000, self.simulate_next_cell)

    # The error img that is opened
    def error_img(self):
        image = Image.open("../resource/temp.png")
        image.show()

# Class of the Main window where the table is placed
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Test Case Viewer")
        self.setStyleSheet("background-color: white;")

        # Set the test case table as the central widget
        self.setCentralWidget(TestCaseTablePage())

        # Adds toolbar to the top which is how you would move through different services
        toolbar = QToolBar("Services")
        toolbar.setMovable(False)
        self.addToolBar(toolbar)
        toolbar.setStyleSheet("background-color: #394d45; color: white;")

        # Adds each service to the toolbar
        for service in services:
            button_action = QAction(service, self)
            button_action.setStatusTip(f"{service} button")
            button_action.triggered.connect(self.toolbar_button_clicked)
            button_action.setCheckable(True)
            toolbar.addAction(button_action)

    # Currently indicates if toolbar is interacted with
    def toolbar_button_clicked(self, s):
        print("click", s)

# Used to create the item put into the table with the correct font
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