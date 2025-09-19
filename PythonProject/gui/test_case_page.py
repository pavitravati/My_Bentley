from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QTableWidget, QLabel, QSizePolicy,
    QCheckBox, QPushButton, QHBoxLayout, QTextEdit
)
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtCore import Qt, QTimer
from excel import load_data
from PythonProject.Test_Scripts.Android.all_tests import *
from PythonProject.core.log_emitter import log_emitter
from PythonProject.Test_Scripts.Android.RemoteLockTemp import Remote_Lock_Unlock001
from utils import make_item
from widgets import PaddingDelegate

testcase_map = load_data()

class TestCaseTablePage(QWidget):
    def __init__(self, service="DemoMode", parent=None):
        super().__init__(parent)
        self.service = service
        log_emitter.log_signal.connect(self.append_log)

        # Adds a vertical layout for the window and sets the padding around it
        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)

        # Adds a Horizontal layout and padding that will be used for the title and logo
        top_layout = QHBoxLayout()
        top_layout.setContentsMargins(0, 40, 0, 20)

        # Creates title and adds to the horizontal layout
        title = QLabel(service)
        title.setFont(QFont("Arial", 25, QFont.Bold))
        title.setStyleSheet("margin-left: 20px; margin-bottom: 20px;")
        top_layout.addWidget(title)

        # Adds a space between the title and logo
        top_layout.addStretch()

        # Creates logo item and adds to the horizontal layout
        logo = QLabel()
        logo.setPixmap(QPixmap('images/bentleylogo.png'))
        logo.setScaledContents(True)
        logo.setMaximumSize(135, 50)
        logo.setStyleSheet("margin-right: 20px;")
        top_layout.addWidget(logo)

        # Adds the horizontal layout to the main window layout
        layout.addLayout(top_layout)

        # Creates the button that will begin the automated test and adds to main layout
        main_button = QPushButton("Begin Automated Test")
        main_button.setStyleSheet("margin-bottom: 20px; margin-top: 20px; font-size: 16px; height: 30px; background-color: #394d45; color: white;")
        main_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        main_button.setCursor(Qt.PointingHandCursor)
        main_button.clicked.connect(self.main_button_clicked)
        layout.addWidget(main_button)

        # Create the table with 8 columns and the rows needed for all test cases
        self.table = QTableWidget()
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels(["Region", "Test Case Description", "Pre-Condition", "Action", "Expected Result", "Duration", "Result", "Error"])
        self.table.setRowCount(len(testcase_map[service]))
        self.table.verticalHeader().setDefaultSectionSize(100)
        self.table.setWordWrap(True)
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

        def create_wrapped_checkbox(text: str) -> QWidget:
            checkbox = QCheckBox()
            checkbox.setCursor(Qt.PointingHandCursor)
            checkbox.setText("")  # Keep it empty

            # Add this line to explicitly style the indicator
            checkbox.setStyleSheet("""
                QCheckBox::indicator {
                    width: 13px;
                    height: 13px;
                    border: 1px solid black;
                    background-color: white;
                }
                QCheckBox::indicator:checked {
                    background-color: #51645c; /* A simple blue background for the tick */
                    image: url("images/check.svg"); /* Or use a base64 encoded image */
                }
            """)

            label = QLabel(text)
            label.setWordWrap(True)
            label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
            label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

            layout = QHBoxLayout()
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(5)
            layout.addWidget(checkbox)
            layout.addWidget(label)

            container = QWidget()
            container.setLayout(layout)
            container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

            # 👇 Make background transparent
            container.setStyleSheet("background: transparent;")
            checkbox.show()

            # 👇 For easy state checking later
            container.checkbox = checkbox

            return container

        # Adds checkboxes and allows for them to control the test case
        def create_precondition_widget(case, row):
            # Creates the layout for the cell
            precondition_layout = QVBoxLayout()
            precondition_layout.setContentsMargins(0, 0, 0, 0)
            precondition_layout.setSpacing(5)
            precondition_widget = QWidget()
            precondition_widget.setObjectName("preconditionWidget")
            precondition_widget.setStyleSheet("#preconditionWidget { background: transparent; }")

            # Stores all the checkboxes for that cell
            checkboxes = []

            for precondition in case["Pre-Condition"]:
                wrapped_checkbox = create_wrapped_checkbox(precondition)
                precondition_layout.addWidget(wrapped_checkbox)
                checkboxes.append(wrapped_checkbox.checkbox)  # keep references to actual checkboxes

            # If the test case has a precondition adds a button
            if len(case["Pre-Condition"]) > 0:
                action_button = QPushButton("Run Testcase")
                action_button.setEnabled(False)
                action_button.setStyleSheet("margin-top: 2px; margin-right: 10px;")
                action_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
                action_button.setCursor(Qt.PointingHandCursor)

                # Connects the button pressed with the row
                action_button.clicked.connect(lambda _, r=row: self.precondition_button_clicked(r))

                # Checks if every checkbox in the cell is checked
                def update_button_state():
                    all_checked = all(cb.isChecked() for cb in checkboxes)
                    action_button.setEnabled(all_checked)

                # All checkboxes check to see if all are checked using the above function
                for cb in checkboxes:
                    cb.stateChanged.connect(update_button_state)

                # Adds the button to the cell
                precondition_layout.addWidget(action_button)

            precondition_widget.setLayout(precondition_layout)
            precondition_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            return precondition_widget

        # Loops through the table adding items to the correct cells
        for row, case in enumerate(testcase_map[service]):
            # In column 0,1,3,4 the data from the test case in Region column is added to that column in the table
            self.table.setItem(row, 0, make_item(case["Region"]))
            self.table.setItem(row, 1, make_item(case["Test Case Description"]))

            # Adds the checkbox and buttons to the precondition column
            precondition_widget = create_precondition_widget(case, row)
            self.table.setCellWidget(row, 2, precondition_widget)

            action_string = "\n".join(str(task) for task in case["Action"])
            self.table.setItem(row, 3, make_item(action_string))
            expected_string = "\n".join(str(task) for task in case["Expected Result"])
            self.table.setItem(row, 4, make_item(expected_string))
            # Last three columns are saved for data from the tests after completion
            self.table.setItem(row, 5, make_item(""))
            self.table.setItem(row, 6, make_item(""))
            self.table.setItem(row, 7, make_item(""))
            self.table.setWordWrap(True)

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
        QTimer.singleShot(0, self.final_adjust_layout)


    # Adjusts column widths roughly based on screen size
    def adjust_column_widths(self):
        col_widths = [60, 350, 395, 420, 420, 60, 60, 55]
        logical_dpi = self.logicalDpiX()
        for col, col_width in enumerate(col_widths):
            width = int(col_width * logical_dpi/96)
            self.table.setColumnWidth(col, width)

    def final_adjust_layout(self):
        self.adjust_column_widths()
        self.table.resizeRowsToContents()

        padding = 50

        for row in range(self.table.rowCount()):
            current_height = self.table.rowHeight(row)
            self.table.setRowHeight(row, current_height + padding)

    def main_button_clicked(self):
        # for row in range(self.table.rowCount()):
        for row in range(1, self.table.rowCount()+1):
            func_name = f"DemoMode_0{f"0{row}" if row < 10 else f"{row}"}"
            func = globals().get(func_name)
            if func:
                func()
            else:
                print(f"No function named {func_name}")

    # When app is working this runs the testcase for that row. Build on this to show results/process
    def precondition_button_clicked(self, row):
        # checking = 1
        # print(f"Execute button clicked for row {checking}")
        # if checking < 10:
        #     func_name = f"{self.service}_00{checking}"
        # else:
        #     func_name = f"{self.service}_0{checking}"
        # func = globals().get(func_name)
        # if func:
        #     func()
        Remote_Lock_Unlock001()