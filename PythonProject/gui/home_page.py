from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QTableWidget, QLabel, QCheckBox, QPushButton, QHBoxLayout,
    QHeaderView, QTableWidgetItem, QFrame, QLineEdit, QSizePolicy, QApplication
)
from PySide6.QtGui import QFont, QPixmap, QCursor
from excel import services
from PySide6.QtCore import Qt, Signal
from excel import resource_path
from test_case_page import TestCaseTablePage
from service_report import ServiceReport
from openpyxl import load_workbook, Workbook
from excel import load_data
from datetime import datetime
import shutil
from openpyxl.utils import get_column_letter
import globals
import os

testcase_map = load_data()

class ClickableLabel(QLabel):
    clicked = Signal()
    def __init__(self, text):
        super().__init__(f"<a style='color:black; text-decoration:none; font-size:14px; margin:0px' href='#'>{text}</a>")
        self.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.setOpenExternalLinks(False)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.linkActivated.connect(lambda _: self.clicked.emit())

class HomePage(QWidget):
    def __init__(self, main_window, parent=None):
        super().__init__(parent)
        self.main_window = main_window
        QApplication.primaryScreen().size().width()
        if QApplication.primaryScreen().size().width() > 1500:
            self.screen = 'Monitor'
        else:
            self.screen = 'Laptop'

        # Adds a vertical layout for the window and sets the padding around it
        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)

        # Adds a Horizontal layout and padding that will be used for the title and logo
        top_layout = QHBoxLayout()
        top_layout.setContentsMargins(80, 40, 80, 0)

        # Creates title and adds to the horizontal layout
        title = QLabel("Automated Testing")
        title.setFont(QFont("Arial", 25, QFont.Bold))
        title.setStyleSheet("margin-left: 20px; margin-bottom: 20px;")
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

        main_container_widget = QWidget()
        if self.screen == 'Monitor':
            main_container_widget.setFixedHeight(650)
            main_container_widget.setFixedWidth(1500)
        else:
            main_container_widget.setFixedWidth(950)
            main_container_widget.setFixedHeight(410)
        main_container = QHBoxLayout(main_container_widget)
        main_container_widget.setObjectName("mainContainer")
        main_container_widget.setStyleSheet("""
            #mainContainer {
                border: 2px solid #394d45;
                border-radius: 8px;
                background-color: #f3f6f5;
            }
        """)

        left_side = QVBoxLayout()
        left_widget = QWidget()
        left_widget.setLayout(left_side)
        left_widget.setObjectName("leftSide")
        left_widget.setStyleSheet("""
            #leftSide {
                background-color: #f3f6f5;
            }
        """)
        left_side.setContentsMargins(40, 20, 20, 40)


        testcase_table = QTableWidget()
        testcase_table.setColumnCount(2)
        if self.screen == 'Monitor':
            testcase_table.setColumnWidth(0, 300)
            testcase_table.setColumnWidth(1, 75)
        else:
            testcase_table.setColumnWidth(0, 190)
            testcase_table.setColumnWidth(1, 75)
        testcase_table.setHorizontalHeaderLabels(["Service", "Run"])
        header = testcase_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Fixed)
        header.setFixedHeight(40)
        testcase_table.verticalHeader().setVisible(False)
        testcase_table.setRowCount(len(services)+1)
        testcase_table.setWordWrap(True)
        testcase_table.setEditTriggers(QTableWidget.NoEditTriggers)
        if self.screen == 'Monitor':
            testcase_table.setFixedWidth(395)
            testcase_table.setFixedHeight(560)
        else:
            testcase_table.setFixedWidth(280)
            testcase_table.setFixedHeight(354)
        testcase_table.setStyleSheet("""
                    QTableWidget {
                        background-color: white;
                        gridline-color: #dcdcdc;
                        font-size: 14px;
                        color: #25312c;
                        selection-background-color: #c7d3cc;
                        selection-color: black;
                        outline: 0;
                    }
                
                    QHeaderView::section {
                        background-color: #394d45;
                        color: white;
                        font-weight: bold;
                        border: none;
                        padding: 8px;
                        border-right: 1px solid #51645c;
                    }
                
                    QTableWidget::item {
                        border-bottom: 1px solid #dcdcdc;
                        padding: 6px;
                    }
                
                    QTableWidget::item:hover {
                        background-color: #e8edea;
                    }
                """)
        header_font = QFont("Arial", 15, QFont.Bold)
        testcase_table.horizontalHeader().setFont(header_font)

        for row in range(len(services)+1):
            checkbox = QCheckBox()
            checkbox.clicked.connect(lambda: self.update_run_btn(testcase_table))
            checkbox.setCursor(Qt.PointingHandCursor)
            checkbox.setStyleSheet("""
                            QCheckBox {
                                background: transparent;
                            }
                            QCheckBox::indicator {
                                width: 13px;
                                height: 13px;
                                border: 1px solid black;
                                background-color: white;
                            }
                            QCheckBox::indicator:checked {
                                background-color: #51645c;
                            }
                        """)
            cell_widget = QWidget()
            cell_widget.setStyleSheet("background: transparent;")
            check_layout = QHBoxLayout(cell_widget)
            check_layout.addWidget(checkbox)
            check_layout.setAlignment(Qt.AlignCenter)
            check_layout.setContentsMargins(8, 0, 0, 0)

            if row == 0:
                item = QTableWidgetItem("Run all services")
                item.setFont(QFont("Arial", 12, QFont.Bold))
                testcase_table.setItem(row, 0, item)
                testcase_table.setCellWidget(row, 1, cell_widget)
                checkbox.toggled.connect(lambda checked, t=testcase_table: self.all_tests_checkbox(checked, t))
            else:
                label = ClickableLabel(services[row-1])
                label.clicked.connect(lambda r=row: self.open_service_tests(services[r]))

                text_cell = QWidget()
                text_cell.setFixedHeight(20)
                text_layout = QHBoxLayout(text_cell)
                text_layout.addWidget(label)
                text_layout.setAlignment(Qt.AlignVCenter)
                text_layout.setContentsMargins(0, 0, 0, 0)
                text_cell.setStyleSheet("background: transparent;")

                text_cell.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                cell_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                testcase_table.setCellWidget(row, 0, text_cell)
                testcase_table.setCellWidget(row, 1, cell_widget)

        left_side.addWidget(testcase_table)
        main_container.addWidget(left_widget)

        middle_side = QVBoxLayout()
        if self.screen == 'Monitor':
            middle_side.setContentsMargins(30, 15, 75, 15)
        else:
            middle_side.setContentsMargins(35, 15, 15, 15)
        middle_container = QWidget()
        middle_container.setLayout(middle_side)
        middle_container.setStyleSheet("""
            background: transparent;
        """)
        credentials_frame = QFrame()
        if self.screen == 'Monitor':
            credentials_frame.setFixedSize(400, 560)
        else:
            credentials_frame.setFixedSize(265, 354)
        credentials_frame.setStyleSheet("""
                    QFrame {
                        border: 2px solid #394d45;
                        border-radius: 10px;
                        background-color: white;
                    }
                    QPushButton {
                        background-color: #394d45;
                        width: 220px;
                        height: 35px;
                        border: none;
                        border-radius: 10px;
                        padding: 6px 10px;
                        color: white;
                        font-size: 16px;
                        font-weight: bold;
                        margin-top: 2px;
                    }
                    QPushButton:hover {
                        background-color: #25312c;
                        cursor: pointer;
                    }
                    QLineEdit {
                        border: 2px solid #394d45;
                        border-radius: 8px;
                        padding: 6px 10px;
                        background-color: #f3f6f5;
                        color: #25312c;
                        font-size: 14px;
                        height: 35px;
                    }
                    QLineEdit:focus {
                        border: 2px solid #51645c;
                        background-color: #ffffff;
                    }
                    QLineEdit::placeholder {
                        color: #7a7a7a;
                    }
                """)

        form_layout = QVBoxLayout(credentials_frame)

        form_title = QLabel("Credentials")
        form_title.setAlignment(Qt.AlignCenter)
        form_title.setFont(QFont("Arial", 22, QFont.Bold))
        form_title.setStyleSheet("color: #394d45; border: 0px solid #394d45;")

        form_layout.addWidget(form_title)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Name")
        self.name_input.setStyleSheet("margin-bottom: 5px;")
        self.name_input.textChanged.connect(lambda: self.update_run_btn(testcase_table))

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")
        self.email_input.setStyleSheet("margin-bottom: 5px;")
        self.email_input.textChanged.connect(lambda: self.update_run_btn(testcase_table))

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setStyleSheet("margin-bottom: 5px;")
        self.password_input.textChanged.connect(lambda: self.update_run_btn(testcase_table))

        self.pin_input = QLineEdit()
        self.pin_input.setPlaceholderText("PIN")
        self.pin_input.setStyleSheet("margin-bottom: 5px;")
        self.pin_input.textChanged.connect(lambda: self.update_run_btn(testcase_table))

        form_layout.addWidget(self.name_input)
        form_layout.addWidget(self.email_input)
        form_layout.addWidget(self.password_input)
        form_layout.addWidget(self.pin_input)
        form_layout.setContentsMargins(30, 30, 30, 30)

        platform_layout = QHBoxLayout()
        platform_layout.setSpacing(10)
        platform_layout.setAlignment(Qt.AlignCenter)

        self.android_btn = QPushButton("Android")
        self.ios_btn = QPushButton("iOS")

        for btn in (self.android_btn, self.ios_btn):
            btn.setFixedSize(140, 45) if self.screen == 'Monitor' else btn.setFixedSize(85, 30)
            btn.clicked.connect(lambda: self.update_run_btn(testcase_table))
            btn.setCursor(Qt.PointingHandCursor)
            btn.setCheckable(True)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #dfe4e2;
                    border: 2px solid #394d45;
                    border-radius: 8px;
                    color: #394d45;
                    font-weight: bold;
                    font-size: 12px;
                }
                QPushButton:checked {
                    background-color: #394d45;
                    color: white;
                }
                QPushButton:hover {
                    background-color: #cfd4d2;
                }
            """)

        self.android_btn.clicked.connect(lambda: self._select_platform("android"))
        self.ios_btn.clicked.connect(lambda: self._select_platform("ios"))

        platform_layout.addWidget(self.android_btn)
        platform_layout.addWidget(self.ios_btn)

        vehicle_type_layout = QHBoxLayout()
        vehicle_type_layout.setSpacing(10)
        vehicle_type_layout.setAlignment(Qt.AlignCenter)

        self.ice_btn = QPushButton("ICE")
        self.phev_btn = QPushButton("PHEV")

        for btn in (self.ice_btn, self.phev_btn):
            btn.setFixedSize(140, 45) if self.screen == 'Monitor' else btn.setFixedSize(85, 30)
            btn.setCursor(Qt.PointingHandCursor)
            btn.clicked.connect(lambda: self.update_run_btn(testcase_table))
            btn.setCheckable(True)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #dfe4e2;
                    border: 2px solid #394d45;
                    border-radius: 8px;
                    color: #394d45;
                    font-weight: bold;
                    font-size: 12px;
                }
                QPushButton:checked {
                    background-color: #394d45;
                    color: white;
                }
                QPushButton:hover {
                    background-color: #cfd4d2;
                }
            """)

        self.ice_btn.clicked.connect(lambda: self._select_car("ice"))
        self.phev_btn.clicked.connect(lambda: self._select_car("phev"))

        vehicle_type_layout.addWidget(self.ice_btn)
        vehicle_type_layout.addWidget(self.phev_btn)

        form_layout.addLayout(vehicle_type_layout)
        form_layout.addLayout(platform_layout)

        middle_side.addWidget(credentials_frame)
        main_container.addWidget(middle_container)

        right_side = QVBoxLayout()
        right_side.setContentsMargins(30, 15 if self.screen == 'Monitor' else 12, 30, 15)
        right_container = QWidget()
        right_container.setLayout(right_side)
        right_container.setStyleSheet("""
            background: transparent;
        """)

        run_frame = QFrame()
        if self.screen == 'Monitor':
            run_frame.setFixedSize(400, 130)
        else:
            run_frame.setFixedSize(253, 82)
        run_frame.setStyleSheet("""
            QFrame {
                border: 2px solid #394d45;
                border-radius: 10px;
                background-color: white;
            }
            QPushButton {
                background-color: #dfe4e2;
                border: 2px solid #394d45;
                color: #394d45;
                font-size: 16px;
                font-weight: bold;
                width: 250px;
                height: 35px;
                border-radius: 10px;
                padding: 6px 10px;
            }
            QPushButton:enabled {
                background-color: #394d45;
                color: white;
            }
            QPushButton:hover {
                background-color: #25312c;

            }
        """)

        self.run_btn = QPushButton("Run")
        self.run_btn.setEnabled(False)
        self.run_btn.setCursor(Qt.PointingHandCursor)
        self.run_btn.clicked.connect(lambda: self.run_selected_services(testcase_table))

        btn_layout = QVBoxLayout()
        btn_layout.addWidget(self.run_btn)
        btn_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        btn_layout.setSpacing(30)
        btn_layout.setContentsMargins(10, 10, 10, 10)

        run_frame.setLayout(btn_layout)

        result_frame = QFrame()
        if self.screen == 'Monitor':
            result_frame.setFixedSize(400, 400)
        else:
            result_frame.setFixedSize(253, 270)
        result_frame.setStyleSheet("""
                    QFrame {
                        border: 2px solid #394d45;
                        border-radius: 10px;
                        background-color: white;
                    }
                    QPushButton {
                        background-color: #394d45;
                        font-size: 16px;
                        font-weight: bold;
                        width: 250px;
                        height: 35px;
                        border: none;
                        border-radius: 10px;
                        padding: 6px 10px;
                        color: white;
                    }
                    QPushButton:hover {
                        background-color: #25312c;
                        cursor: pointer;
                    }
                    QLabel {
                        font-size: 18px;
                        color: #394d45;
                        border: 0px solid #394d45;
                    }
                """)

        tests_run = QLabel("Tests run: 0")
        tests_passed = QLabel("Tests passed: 0")
        tests_failed = QLabel("Tests failed: 0")

        result_btn = QPushButton("Results")
        result_btn.setCursor(Qt.PointingHandCursor)
        result_btn.clicked.connect(self.result_btn_clicked)
        export_btn = QPushButton("Export")
        export_btn.setCursor(Qt.PointingHandCursor)
        export_btn.clicked.connect(self.export_result)
        if self.screen == 'Laptop':
            result_btn.setFixedHeight(30)
            export_btn.setFixedHeight(30)

        result_btn_layout = QVBoxLayout()
        result_btn_layout.addWidget(tests_run)
        result_btn_layout.addWidget(tests_passed)
        result_btn_layout.addWidget(tests_failed)
        result_btn_layout.addWidget(result_btn)
        result_btn_layout.addWidget(export_btn)
        result_btn_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        result_btn_layout.setSpacing(30 if self.screen == 'Monitor' else 15)
        result_btn_layout.setContentsMargins(10, 10, 10, 10)
        result_frame.setLayout(result_btn_layout)

        right_side.addWidget(run_frame)
        right_side.addWidget(result_frame)
        main_container.addWidget(right_container)

        layout.addWidget(main_container_widget, alignment=Qt.AlignCenter)

    def _select_platform(self, platform):
        if platform == "android":
            self.android_btn.setChecked(True)
            self.ios_btn.setChecked(False)
        else:
            self.android_btn.setChecked(False)
            self.ios_btn.setChecked(True)

    def _select_car(self, car_type):
        if car_type == "ice":
            self.ice_btn.setChecked(True)
            self.phev_btn.setChecked(False)
        else:
            self.ice_btn.setChecked(False)
            self.phev_btn.setChecked(True)

    def open_service_tests(self, service):
        self.main_window.show_test_cases(service)

    def all_tests_checkbox(self, checked, table):
        for row in range(1, table.rowCount()):
            cell_widget = table.cellWidget(row, 1)
            if cell_widget:
                cb = cell_widget.findChild(QCheckBox)
                if cb:
                    cb.setChecked(checked)
                    cb.setEnabled(not checked)

    def update_run_btn(self, table):
        name_filled = bool(self.name_input.text().strip())
        email_filled = bool(self.email_input.text().strip())
        password_filled = bool(self.password_input.text().strip())
        pin_filled = bool(self.pin_input.text().strip())
        vehicle_type = self.ice_btn.isChecked() or self.phev_btn.isChecked()
        phone_type = self.ios_btn.isChecked() or self.android_btn.isChecked()
        checkbox_check = False
        for row in range(table.rowCount()):
            cell_widget = table.cellWidget(row, 1)
            if cell_widget:
                cb = cell_widget.findChild(QCheckBox)
                if cb.isChecked():
                    checkbox_check = True

        can_submit = name_filled and email_filled and password_filled and pin_filled and vehicle_type and phone_type and checkbox_check

        self.run_btn.setEnabled(can_submit)

    def run_selected_services(self, table):
        globals.selected_services = []
        for row in range(table.rowCount()):
            cell_widget = table.cellWidget(row, 1)
            if cell_widget:
                cb = cell_widget.findChild(QCheckBox)
                if cb.isChecked():
                    globals.selected_services.append(services[row-1])
        globals.current_name = self.name_input.text()
        globals.current_email = self.email_input.text()
        globals.current_password = self.password_input.text()
        globals.current_pin = self.pin_input.text()
        globals.vehicle_type = "ice" if self.ice_btn.isChecked() else "phev"
        globals.phone_type = "Iphone" if self.ios_btn.isChecked() else "Android"

        self.main_window.setCentralWidget(TestCaseTablePage(self.main_window, globals.selected_services[globals.service_index]))

    def result_btn_clicked(self):
        self.service_report = ServiceReport()
        self.service_report.show()

    def export_result(self):
        workbook = Workbook()
        del workbook["Sheet"]
        for service in globals.log_history:
            new_sheet = workbook.create_sheet(title=service)
            for key, test_logs in globals.log_history[service].items():
                results = ''
                for res in test_logs:
                    results += res + '\n'
                new_sheet[f'A{key}'] = testcase_map[service][key-1]['Test Case Description']
                new_sheet[f'B{key}'] = results
        current_datetime = datetime.now().strftime("%Y-%m-%d %H+%M")
        script_dir = os.path.dirname(os.path.abspath(__file__))
        save_folder = os.path.join(script_dir, "test_results")
        subfolder = os.path.join(save_folder, current_datetime)
        imgfolder = os.path.join(subfolder, "images")
        os.makedirs(subfolder, exist_ok=True)
        os.makedirs(imgfolder, exist_ok=True)
        save_path = os.path.join(subfolder, f"test_results.xlsx")
        workbook.save(save_path)

        images = os.path.join(script_dir, "fail_images")
        dest_images = os.path.join(subfolder, "images")
        if os.path.exists(images):
            shutil.copytree(images, dest_images, dirs_exist_ok=True, ignore=shutil.ignore_patterns('.gitkeep'))