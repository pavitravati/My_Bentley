from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QTableWidget, QLabel, QSizePolicy,
    QCheckBox, QPushButton, QHBoxLayout, QApplication, QHeaderView
)
from PySide6.QtGui import QFont, QPixmap, QColor, QBrush
from PySide6.QtCore import Qt, QTimer, Slot, QThread
from excel import load_data
from core.log_emitter import log_emitter
from utils import make_item
from widgets import PaddingDelegate
from test_worker import TestRunnerWorker
from error_page import ErrorPage
from service_report import ServiceReport
from pathlib import Path
import os
import glob
from PySide6.QtCore import QTime

testcase_map = load_data()

class TestCaseTablePage(QWidget):
    def __init__(self, service="DemoMode", parent=None):
        super().__init__(parent)
        self.service = service
        self.log_history = {}
        self.current_row = None
        log_emitter.log_signal.connect(self.handle_log)
        self.test_start_times = {}

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
        img_path = Path(__file__).parent / "images" / "bentleylogo.png"
        pixmap = QPixmap(str(img_path))
        logo.setPixmap(pixmap)
        # logo.setPixmap(QPixmap('images/bentleylogo.png'))
        logo.setScaledContents(True)
        logo.setMaximumSize(162, 60)
        logo.setStyleSheet("margin-right: 20px;")
        top_layout.addWidget(logo)

        # Adds the horizontal layout to the main window layout
        layout.addLayout(top_layout)

        # Creates the button that will begin the automated test and adds to main layout
        main_button = QPushButton("Begin Automated Test")
        main_button.setStyleSheet("""
            QPushButton {
                margin-top: 20px;
                margin-bottom: 20px;
                font-size: 16px;
                height: 30px;
                background-color: #394d45;
                color: white;
            }
            QPushButton:disabled {
                background-color: #859990; 
                color: #cccccc;      
            }
            QPushButton:hover {
                background-color: #323c38;
            }
        """)
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
                    background-color: #51645c;
                    image: url("images/check.svg");
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

        self.results_btn = QPushButton("Show results")
        self.results_btn.setVisible(False)
        self.results_btn.setCursor(Qt.PointingHandCursor)
        self.results_btn.setStyleSheet("margin-top: 20px; font-size: 16px; height: 30px; background-color: #394d45; color: white;")
        self.results_btn.setStyleSheet("""
            QPushButton {
                margin-top: 20px;
                font-size: 16px;
                height: 30px;
                background-color: #394d45;
                color: white;
            }
            QPushButton:disabled {
                background-color: #859990; 
                color: #cccccc;      
            }
            QPushButton:hover {
                background-color: #323c38;
            }
        """)
        self.results_btn.clicked.connect(lambda checked: self.testing_click())
        layout.addWidget(self.results_btn)

    def generate_results(self):
        self.results_btn.setVisible(True)

    def testing_click(self):
        self.service_report = ServiceReport(service_title=f"{self.service}", logs=self.log_history)
        self.service_report.show()

    def adjust_column_widths(self):
        screen_size = QApplication.primaryScreen().size()
        available_width = screen_size.width()
        available_width -= 90

        if available_width < 1500:
            multi = 1.95
            proportions = [0.04, 0.20, 0.20, 0.20, 0.22, 0.05, 0.06, 0.05]
        else:
            multi = 3
            proportions = [0.03, 0.22, 0.22, 0.22, 0.22, 0.03, 0.03, 0.03]

        total = sum(proportions)
        proportions = [p / total for p in proportions]

        for col, prop in enumerate(proportions):
            self.table.setColumnWidth(col, int(available_width * prop))

        # prevent auto-stretching (each col keeps its proportional size)
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Fixed)

    def final_adjust_layout(self):
        self.adjust_column_widths()
        self.table.resizeRowsToContents()

        padding = 50

        for row in range(self.table.rowCount()):
            current_height = self.table.rowHeight(row)
            self.table.setRowHeight(row, current_height + padding)

    def main_button_clicked(self):

        self.sender().setVisible(False)

        self.thread = QThread()
        self.worker = TestRunnerWorker(self.service, self.table.rowCount())
        self.worker.moveToThread(self.thread)

        # Connect signals
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.need_precondition.connect(self.on_need_precondition)

        self.worker.current_row.connect(self.set_current_row)
        self.worker.row_finished.connect(self.on_row_finished)

        self.worker.progress.connect(self.update_progress)

        self.worker.finished.connect(self.generate_results)

        self.thread.start()

    def update_progress(self, row):
        print(f"Completed test row: {row}")

    def handle_log(self, message: str):
        try:
            self.log_history[self.current_row].append(message)
        except:
            self.log_history[self.current_row] = [message]
        print(message)

    @Slot(int)
    def set_current_row(self, row: int):
        self.current_row = row
        self.test_start_times[row] = QTime.currentTime()

    def on_row_finished(self, row: int):
        colors = []

        if row in self.test_start_times:
            start_time = self.test_start_times[row]
            end_time = QTime.currentTime()
            duration_ms = start_time.msecsTo(end_time)

            # convert to mm:ss
            mins, secs = divmod(duration_ms // 1000, 60)
            if secs < 1:
                secs = 1
            duration_str = f"{mins:02d}:{secs:02d}"

            # put it into column 5 ("Duration")
            duration_item = self.table.item(row - 1, 5)
            if duration_item:
                duration_item.setText(duration_str)
                duration_item.setFont(QFont("Arial", 10))

        for i in range(len(self.log_history[row])):
            colors.append('green') if self.log_history[row][i][0] == '✅' else colors.append('red') if self.log_history[row][i][0] == '❌' else colors.append('yellow') if self.log_history[row][i][0] == '⚠' else None

        result_cell = self.table.item(row-1, 6)
        if 'red' in colors or 'yellow' in colors:
            error_btn = QPushButton("Error")
            error_btn.setCursor(Qt.PointingHandCursor)
            error_btn.clicked.connect(lambda checked: self.open_test_case_detail(row))
            self.table.setCellWidget(row-1, 7, error_btn)

            result_cell.setText("Failed")
            result_cell.setForeground(QBrush(QColor("white")))
            result_cell.setBackground(QColor("red"))
        else:
            result_cell.setText("Passed")
            result_cell.setForeground(QBrush(QColor("white")))
            result_cell.setBackground(QColor("green"))


        action_item = self.table.item(row-1, 3)
        action_text = action_item.text()
        action_lines = action_text.split("\n")
        action_colors = colors[:len(action_lines)]
        action_item.setText("")

        action_html = []
        for i, line in enumerate(action_lines):
            if 'yellow' in colors:
                color = '#F6BE00'
            else:
                try:
                    color = action_colors[i]
                except IndexError:
                    color = action_colors[-1]
                # color = action_colors[i]
            escaped_line = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            action_html.append(f'<span style="color:{color}">{escaped_line}</span>')
        action_html_text = "<br>".join(action_html)

        action_label = QLabel()
        action_label.setTextFormat(Qt.RichText)
        action_label.setWordWrap(True)
        action_label.setStyleSheet("background: transparent;")
        action_label.setText(action_html_text)

        self.table.setCellWidget(row-1, 3, action_label)

        expected_item = self.table.item(row-1, 4)
        expected_text = expected_item.text()
        expected_lines = expected_text.split("\n")
        expected_colors = colors[len(expected_lines)-1:]
        expected_item.setText("")

        expected_html = []
        for i, line in enumerate(expected_lines):
            if 'yellow' in colors:
                color = '#F6BE00'
            else:
                try:
                    color = expected_colors[i]
                except IndexError:
                    try:
                        color = expected_colors[-1]
                    except IndexError:
                        color = action_colors[-1]
                # color = expected_colors[i]
            escaped_line = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            expected_html.append(f'<span style="color:{color}">{escaped_line}</span>')
        expected_html_text = "<br>".join(expected_html)

        expected_label = QLabel()
        expected_label.setTextFormat(Qt.RichText)
        expected_label.setWordWrap(True)
        expected_label.setStyleSheet("background: transparent;")
        expected_label.setText(expected_html_text)

        self.table.setCellWidget(row-1, 4, expected_label)

    # Need to update so that it checks by row and by service
    def open_test_case_detail(self, row):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        image_dir = os.path.join(base_dir, "fail_images")
        image_paths = []
        row_num = f"0{row}" if row < 10 else f"{row}"

        for file_path in glob.glob(os.path.join(image_dir, "*.png")):
            filename = os.path.basename(file_path)
            if row_num in filename:
                image_paths.append(file_path)

        self.error_window = ErrorPage(title=f"{self.service}-0{row_num}",
                                      logs=self.log_history[row], images=image_paths)
        self.error_window.show()

    def on_need_precondition(self, row):
        # Highlight row / notify user if you like
        print(f"⚠️ Waiting for preconditions at row {row}")
        # Optionally: flash the Run Testcase button
        precondition_widget = self.table.cellWidget(row - 1, 2)
        if precondition_widget:
            for child in precondition_widget.findChildren(QPushButton):
                if child.text() == "Run Testcase":
                    child.setEnabled(True)

    def precondition_button_clicked(self, row):
        print(f"✅ Preconditions met for row {row}, resuming test...")

        if hasattr(self, "worker") and self.worker:
            self.worker.resume()

        # optionally disable the button after pressing
        precondition_widget = self.table.cellWidget(row, 2)
        if precondition_widget:
            for child in precondition_widget.findChildren(QPushButton):
                if child.text() == "Run Testcase":
                    child.setEnabled(False)