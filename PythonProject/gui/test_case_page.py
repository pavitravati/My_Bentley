from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QTableWidget, QLabel, QSizePolicy,
    QCheckBox, QPushButton, QHBoxLayout, QApplication, QHeaderView, QToolButton
)
from PySide6.QtGui import QFont, QPixmap, QColor, QBrush, QIcon
from PySide6.QtCore import Qt, QTimer, Slot, QThread, QSize
from excel import load_data
from core.log_emitter import log_emitter
from utils import make_item
from widgets import PaddingDelegate
from test_worker import TestRunnerWorker
from error_page import ErrorPage
from metric_page import MetricPage
import os
import glob
from excel import resource_path
from PySide6.QtCore import QTime
import globals

testcase_map = load_data()

class TestCaseTablePage(QWidget):
    def __init__(self, main_window, service, parent=None, auto_run=True):
        super().__init__(parent)
        self.current_row = None
        self.service = service
        globals.log_history[service] = {}
        log_emitter.log_signal.connect(self.handle_log)
        self.test_start_times = {}
        self.main_window = main_window
        self.auto_run = auto_run

        # Adds a vertical layout for the window and sets the padding around it
        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)

        # Adds a Horizontal layout and padding that will be used for the title and logo
        top_layout = QHBoxLayout()
        top_layout.setContentsMargins(0, 40, 0, 20)

        home_btn = QPushButton()
        # homeimg = Path(__file__).parent / "images" / "homebtn.png"
        # home_btn.setIcon(QIcon(str(homeimg)))
        img_path = resource_path("gui/images/homebtn.png")
        home_btn.setIcon(QIcon(img_path))
        home_btn.setCursor(Qt.PointingHandCursor)
        home_btn.setIconSize(QSize(40, 40))
        home_btn.setIconSize(QSize(50, 50))
        home_btn.clicked.connect(self.home_button_clicked)
        home_btn.setStyleSheet("""
            QPushButton {
                border: none;
                background: #394d45;
                border-radius: 20px;
                width: 70px;
                height: 70px;
                margin-left: 20px
            }
            QPushButton:hover {
                background-color: #323c38;
                border-radius: 20px;
            }
        """)
        top_layout.addWidget(home_btn)

        # Creates title and adds to the horizontal layout
        title = QLabel(service)
        title.setFont(QFont("Arial", 25, QFont.Bold))
        title.setStyleSheet("margin-left: 20px; margin-bottom: 20px; padding-top: 25px;")
        top_layout.addWidget(title)

        # Adds a space between the title and logo
        top_layout.addStretch()

        # Creates logo item and adds to the horizontal layout
        logo = QLabel()
        # img_path = Path(__file__).parent / "images" / "bentleylogo.png"
        # pixmap = QPixmap(str(img_path))
        img_path = resource_path("gui/images/bentleylogo.png")
        pixmap = QPixmap(img_path)
        logo.setPixmap(pixmap)
        logo.setScaledContents(True)
        logo.setMaximumSize(162, 60)
        logo.setStyleSheet("margin-right: 20px;")
        top_layout.addWidget(logo)

        # Adds the horizontal layout to the main window layout
        layout.addLayout(top_layout)

        # Create the table with 8 columns and the rows needed for all test cases
        self.table = QTableWidget()
        self.table.setColumnCount(7 if auto_run else 8)
        horizontal_labels = ["Test Case Description", "Pre-Condition", "Action", "Expected Result", "Duration", "Result", "Details"]
        if not auto_run:
            horizontal_labels.insert(0, 'Run')
        self.table.setHorizontalHeaderLabels(horizontal_labels)
        self.table.verticalHeader().setVisible(False)
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
            if not auto_run:
                self.table.setItem(row, 0, make_item(""))
                manual_run_btn = QPushButton("Run")
                manual_run_btn.setCursor(Qt.PointingHandCursor)
                manual_run_btn.clicked.connect(lambda checked, r=row: self.run_testcase_manual(r))
                self.table.setCellWidget(row, 0, manual_run_btn)
            # In column 0,1,3,4 the data from the test case in Region column is added to that column in the table
            self.table.setItem(row, 0 if auto_run else 1, make_item(case["Test Case Description"]))

            # Adds the checkbox and buttons to the precondition column
            precondition_widget = create_precondition_widget(case, row)
            self.table.setCellWidget(row, 1 if auto_run else 2, precondition_widget)

            action_string = "\n".join(str(task) for task in case["Action"])
            self.table.setItem(row, 2 if auto_run else 3, make_item(action_string))
            expected_string = "\n".join(str(task) for task in case["Expected Result"])
            self.table.setItem(row, 3 if auto_run else 4, make_item(expected_string))
            # Last three columns are saved for data from the tests after completion
            self.table.setItem(row, 4 if auto_run else 5, make_item(""))
            self.table.setItem(row, 5 if auto_run else 6, make_item(""))
            self.table.setItem(row, 6 if auto_run else 7, make_item(""))
            self.table.setWordWrap(True)

        # Centres the text in the following columns
        centre_columns = [0, 4, 5, 6] if auto_run else [1, 5, 6, 7]
        for row in range(self.table.rowCount()):
            for col in centre_columns:
                item = self.table.item(row, col)
                if item:
                    item.setTextAlignment(Qt.AlignCenter)

        # Adds padding to certain columns
        delegate = PaddingDelegate()
        for col in range(3):
            self.table.setItemDelegateForColumn(col+1 if auto_run else col+2, delegate)

        # Adds the table to the main layout
        layout.addWidget(self.table)
        # Waits for table to be added and then adjusts the column widths
        QTimer.singleShot(0, self.final_adjust_layout)

        if auto_run:
            self.thread = QThread()
            self.worker = TestRunnerWorker(service, self.table.rowCount())
            self.worker.moveToThread(self.thread)

            self.thread.started.connect(self.worker.run)
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(self.worker.deleteLater)
            self.worker.finished.connect(self.worker.deleteLater)
            self.thread.finished.connect(self.thread.deleteLater)
            self.worker.need_precondition.connect(self.on_need_precondition)

            self.worker.current_row.connect(self.set_current_row)
            self.worker.row_finished.connect(self.on_row_finished)
            self.worker.finished.connect(self.next_service)

            self.thread.start()

    def adjust_column_widths(self):
        screen_size = QApplication.primaryScreen().size()
        available_width = screen_size.width()
        available_width -= 75

        if available_width < 1500:
            if self.auto_run:
                proportions = [0.21, 0.21, 0.21, 0.21, 0.06, 0.06, 0.06]
            else:
                proportions = [0.06, 0.19, 0.19, 0.20, 0.20, 0.06, 0.06, 0.06]
        else:
            if self.auto_run:
                proportions = [0.22, 0.22, 0.22, 0.22, 0.04, 0.04, 0.04]
            else:
                proportions = [0.04, 0.21, 0.21, 0.21, 0.21, 0.04, 0.04, 0.04]

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

    def handle_log(self, message: str):
        try:
            globals.log_history[self.service][self.current_row].append(message)
        except Exception:
            # fallback: ensure structure exists and append
            if self.service not in globals.log_history:
                globals.log_history[self.service] = {}
            if self.current_row not in globals.log_history[self.service]:
                globals.log_history[self.service][self.current_row] = []
            globals.log_history[self.service][self.current_row].append(message)

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
            duration_item = self.table.item(row - 1, 4 if self.auto_run else 5)
            if duration_item:
                duration_item.setText(duration_str)
                duration_item.setFont(QFont("Arial", 10))

        metrics = []
        for i in range(len(globals.log_history[self.service][row])):
            symbol = globals.log_history[self.service][row][i][0]
            if symbol == '✅':
                colors.append('green')
            elif symbol == '❌':
                colors.append('red')
            elif symbol == '⚠':
                colors.append('yellow')
            else:
                metrics.append(globals.log_history[self.service][row][i])

        result_cell = self.table.item(row-1, 5 if self.auto_run else 6)
        if 'red' in colors:
            error_btn = QPushButton("Error")
            error_btn.setCursor(Qt.PointingHandCursor)
            error_btn.clicked.connect(lambda checked: self.open_test_case_detail(row))
            self.table.setCellWidget(row-1, 6 if self.auto_run else 7, error_btn)

            result_cell.setText("Failed")
            result_cell.setForeground(QBrush(QColor("white")))
            result_cell.setBackground(QColor("red"))

            self.table.item(row-1, 2 if self.auto_run else 3).setForeground(QBrush(QColor("red")))
            self.table.item(row-1, 3 if self.auto_run else 4).setForeground(QBrush(QColor("red")))
        elif 'yellow' in colors:
            error_btn = QPushButton("Error")
            error_btn.setCursor(Qt.PointingHandCursor)
            error_btn.clicked.connect(lambda checked: self.open_test_case_detail(row))
            self.table.setCellWidget(row-1, 6 if self.auto_run else 7, error_btn)

            result_cell.setText("Error")
            result_cell.setBackground(QColor("#F6BE00"))
            self.table.item(row-1, 2 if self.auto_run else 3).setForeground(QBrush(QColor("#F6BE00")))
            self.table.item(row-1, 3 if self.auto_run else 4).setForeground(QBrush(QColor("#F6BE00")))
        else:
            result_cell.setText("Passed")
            result_cell.setForeground(QBrush(QColor("white")))
            result_cell.setBackground(QColor("green"))
            self.table.item(row-1, 2 if self.auto_run else 3).setForeground(QBrush(QColor("green")))
            self.table.item(row-1, 3 if self.auto_run else 4).setForeground(QBrush(QColor("green")))
            if metrics:
                metric_btn = QPushButton("Metrics")
                metric_btn.setCursor(Qt.PointingHandCursor)
                metric_btn.clicked.connect(lambda checked: self.open_test_case_metrics(row, metrics))
                self.table.setCellWidget(row - 1, 6 if self.auto_run else 7, metric_btn)

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

        test_title = self.table.item(row, 0 if self.auto_run else 1).text()

        self.error_window = ErrorPage(title=test_title,
                                      logs=globals.log_history[self.service][row], images=image_paths)
        self.error_window.show()

    def open_test_case_metrics(self, row, metrics):
        test_title = self.table.item(row, 0 if self.auto_run else 1).text()

        self.metric_window = MetricPage(title=test_title, logs=metrics)
        self.metric_window.show()

    def on_need_precondition(self, row):
        print(f"⚠️ Waiting for preconditions at row {row}")

        precondition_widget = self.table.cellWidget(row - 1, 1 if self.auto_run else 2)
        if precondition_widget:
            for child in precondition_widget.findChildren(QPushButton):
                if child.text() == "Run Testcase":
                    child.setEnabled(True)

    def precondition_button_clicked(self, row):
        print(f"✅ Preconditions met for row {row}, resuming test...")

        if hasattr(self, "worker") and self.worker:
            self.worker.resume()

        # optionally disable the button after pressing
        precondition_widget = self.table.cellWidget(row, 1 if self.auto_run else 2)
        if precondition_widget:
            for child in precondition_widget.findChildren(QPushButton):
                if child.text() == "Run Testcase":
                    child.setEnabled(False)

    def home_button_clicked(self):
        globals.current_name = globals.current_email = globals.current_password = globals.current_pin = globals.vehicle_type = globals.phone_type = None
        globals.tests_run = globals.tests_passed = globals.tests_failed = 0
        globals.selected_services = [None]
        globals.service_index = 0
        globals.current_service = globals.selected_services[globals.service_index]
        globals.log_history = {}
        self.main_window.show_homepage()

    def next_service(self):
        globals.service_index += 1
        if globals.service_index >= len(globals.selected_services):
            self.home_button_clicked()
        else:
            self.main_window.setCentralWidget(None)
            self.main_window.setCentralWidget(TestCaseTablePage(self.main_window, globals.selected_services[globals.service_index]))

    def run_testcase_manual(self, row):
        self.thread = QThread()
        self.worker = TestRunnerWorker(self.service, 1)
        self.worker.moveToThread(self.thread)

        # When thread starts, emit start_manual with the zero-based row index
        self.thread.started.connect(lambda: self.worker.start_manual.emit(row))

        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.need_precondition.connect(self.on_need_precondition)

        self.worker.current_row.connect(self.set_current_row)
        self.worker.row_finished.connect(self.on_row_finished)
        # self.worker.finished.connect(self.next_service)

        self.thread.start()