import re
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QTableWidget, QLabel, QCheckBox, QPushButton, QHBoxLayout,
    QHeaderView, QTableWidgetItem, QFrame, QLineEdit, QSizePolicy, QApplication, QToolButton
)
from PySide6.QtGui import QFont, QPixmap, QCursor
from excel import services
from PySide6.QtCore import Qt, Signal
from excel import resource_path, no_vehicle_services
from gui.excel import only_vehicle_services, no_precondition_services
from gui.import_page import ImportResult
from test_case_page import TestCaseTablePage
from service_report import ServiceReport
from openpyxl import load_workbook, Workbook
from excel import load_data
from datetime import datetime
import shutil
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
            main_container_widget.setFixedHeight(500)
            main_container_widget.setFixedWidth(1100)
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
        left_side.setContentsMargins(40, 20, 20, 20)


        testcase_table = QTableWidget()
        testcase_table.setColumnCount(2)
        if self.screen == 'Monitor':
            testcase_table.setColumnWidth(0, 300)
            testcase_table.setColumnWidth(1, 75)
        else:
            testcase_table.setColumnWidth(0, 240)
            testcase_table.setColumnWidth(1, 75)
        testcase_table.setHorizontalHeaderLabels(["Service", "Run"])
        header = testcase_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Fixed)
        header.setFixedHeight(40)
        testcase_table.verticalHeader().setVisible(False)
        testcase_table.setRowCount(len(services)+4)
        testcase_table.setWordWrap(True)
        testcase_table.setEditTriggers(QTableWidget.NoEditTriggers)
        if self.screen == 'Monitor':
            testcase_table.setFixedWidth(395)
            testcase_table.setFixedHeight(560)
        else:
            testcase_table.setFixedWidth(330)
            testcase_table.setFixedHeight(430)
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

        for row in range(len(services)+4):
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
            elif row == 1:
                item = QTableWidgetItem("No Vehicle services")
                item.setFont(QFont("Arial", 12, QFont.Bold))
                testcase_table.setItem(row, 0, item)
                testcase_table.setCellWidget(row, 1, cell_widget)
                checkbox.toggled.connect(lambda checked, t=testcase_table: self.no_vehicle_tests_checkbox(checked, t))
            elif row == 2:
                item = QTableWidgetItem("Only Vehicle services")
                item.setFont(QFont("Arial", 12, QFont.Bold))
                testcase_table.setItem(row, 0, item)
                testcase_table.setCellWidget(row, 1, cell_widget)
                checkbox.toggled.connect(lambda checked, t=testcase_table: self.vehicle_tests_checkbox(checked, t))
            elif row == 3:
                item = QTableWidgetItem("No precondition services")
                item.setFont(QFont("Arial", 12, QFont.Bold))
                testcase_table.setItem(row, 0, item)
                testcase_table.setCellWidget(row, 1, cell_widget)
                checkbox.toggled.connect(lambda checked, t=testcase_table: self.no_precondition_tests_checkbox(checked, t))
            else:
                label = ClickableLabel(services[row-4])
                label.clicked.connect(lambda r=row: self.open_service_tests(services[r-4]))

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
            credentials_frame.setFixedSize(320, 430)
        credentials_frame.setStyleSheet("""
                    QFrame {
                        border: 2px solid #394d45;
                        border-radius: 10px;
                        background-color: white;
                    }
                    QLineEdit {
                        border: 1px solid #394d45;
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
        if globals.current_name:
            self.name_input.setText(globals.current_name)
        else:
            self.name_input.setPlaceholderText("Name")
        self.name_input.setStyleSheet("margin-bottom: 5px;")
        self.name_input.textChanged.connect(lambda: self.update_run_btn(testcase_table))

        self.email_input = QLineEdit()
        if globals.current_email:
            self.email_input.setText(globals.current_email)
        else:
            self.email_input.setPlaceholderText("Email")
        self.email_input.setStyleSheet("margin-bottom: 5px;")
        self.email_input.textChanged.connect(lambda: self.update_run_btn(testcase_table))

        self.password_input = QLineEdit()
        if globals.current_password:
            self.password_input.setText(globals.current_password)
        else:
            self.password_input.setPlaceholderText("Password")
        self.password_input.setStyleSheet("margin-bottom: 5px;")
        self.password_input.textChanged.connect(lambda: self.update_run_btn(testcase_table))

        self.pin_input = QLineEdit()
        if globals.current_pin:
            self.pin_input.setText(globals.current_pin)
        else:
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

        self.android_btn = QToolButton()
        self.ios_btn = QToolButton()
        self.android_btn.setText("Android")
        self.ios_btn.setText("iOS")

        for btn in (self.android_btn, self.ios_btn):
            btn.setFixedSize(140, 45) if self.screen == 'Monitor' else btn.setFixedSize(120, 30)
            btn.clicked.connect(lambda: self.update_run_btn(testcase_table))
            btn.setCursor(Qt.PointingHandCursor)
            btn.setCheckable(True)
            btn.setStyleSheet("""
                QToolButton {
                    background-color: #e0f1eb;
                    color: #394d45;
                    font-weight: bold;
                    font-size: 12px;
                }
                QToolButton:checked {
                    background-color: #485f56;
                    color: white;
                }
                QTolButton:hover {
                    background-color: #cfd4d2;
                }
            """)

        self.android_btn.clicked.connect(lambda: self._select_platform("android"))
        self.ios_btn.clicked.connect(lambda: self._select_platform("ios"))
        self.android_btn.setChecked(True if globals.phone_type == 'android' else False)
        self.ios_btn.setChecked(True if globals.phone_type == 'ios' else False)

        platform_layout.addWidget(self.android_btn)
        platform_layout.addWidget(self.ios_btn)

        vehicle_type_layout = QHBoxLayout()
        vehicle_type_layout.setSpacing(10)
        vehicle_type_layout.setAlignment(Qt.AlignCenter)

        self.ice_btn = QToolButton()
        self.ice_btn.setText("ICE")
        self.phev_btn = QToolButton()
        self.phev_btn.setText("PHEV")

        for btn in (self.ice_btn, self.phev_btn):
            btn.setFixedSize(140, 45) if self.screen == 'Monitor' else btn.setFixedSize(120, 30)
            btn.setCursor(Qt.PointingHandCursor)
            btn.clicked.connect(lambda: self.update_run_btn(testcase_table))
            btn.setCheckable(True)
            btn.setStyleSheet("""
                QToolButton {
                    background-color: #e0f1eb;
                    color: #394d45;
                    font-weight: bold;
                    font-size: 12px;
                }
                QToolButton:checked {
                    background-color: #485f56;
                    color: white;
                }
                QTolButton:hover {
                    background-color: #cfd4d2;
                }
            """)

        self.ice_btn.clicked.connect(lambda: self._select_car("ice"))
        self.phev_btn.clicked.connect(lambda: self._select_car("phev"))

        self.ice_btn.setChecked(True if globals.vehicle_type == 'ice' else False)
        self.phev_btn.setChecked(True if globals.vehicle_type == 'phev' else False)

        vehicle_type_layout.addWidget(self.ice_btn)
        vehicle_type_layout.addWidget(self.phev_btn)

        form_layout.addLayout(vehicle_type_layout)
        form_layout.addLayout(platform_layout)

        country_layout = QHBoxLayout()
        country_layout.setSpacing(10)
        country_layout.setAlignment(Qt.AlignCenter)

        self.eur_btn = QToolButton()
        self.eur_btn.setText("EUR")
        self.nar_btn = QToolButton()
        self.nar_btn.setText("NAR")
        self.chn_btn = QToolButton()
        self.chn_btn.setText("CHN")

        for btn in (self.eur_btn, self.nar_btn, self.chn_btn):
            btn.setFixedSize(90, 45) if self.screen == 'Monitor' else btn.setFixedSize(77, 30)
            btn.setCursor(Qt.PointingHandCursor)
            btn.clicked.connect(lambda: self.update_run_btn(testcase_table))
            btn.setCheckable(True)
            btn.setStyleSheet("""
                        QToolButton {
                            background-color: #e0f1eb;
                            color: #394d45;
                            font-weight: bold;
                            font-size: 12px;
                        }
                        QToolButton:checked {
                            background-color: #485f56;
                            color: white;
                        }
                        QTolButton:hover {
                            background-color: #cfd4d2;
                        }
                    """)

        self.eur_btn.clicked.connect(lambda: self._select_country("eur"))
        self.nar_btn.clicked.connect(lambda: self._select_country("nar"))
        self.chn_btn.clicked.connect(lambda: self._select_country("chn"))

        self.eur_btn.setChecked(True if globals.country == 'eur' else False)
        self.nar_btn.setChecked(True if globals.country == 'nar' else False)
        self.chn_btn.setChecked(True if globals.country == 'chn' else False)

        country_layout.addWidget(self.eur_btn)
        country_layout.addWidget(self.nar_btn)
        country_layout.addWidget(self.chn_btn)

        form_layout.addLayout(vehicle_type_layout)
        form_layout.addLayout(platform_layout)
        form_layout.addLayout(country_layout)

        middle_side.addWidget(credentials_frame)
        main_container.addWidget(middle_container)

        right_side = QVBoxLayout()
        right_side.setContentsMargins(30, 15 if self.screen == 'Monitor' else 12, 30, 15)
        right_container = QWidget()
        right_container.setLayout(right_side)
        right_container.setStyleSheet("background: transparent;")

        run_frame = QFrame()
        if self.screen == 'Monitor':
            run_frame.setFixedSize(400, 130)
        else:
            run_frame.setFixedSize(300, 100)
        run_frame.setStyleSheet("""
            QFrame {
                border: 2px solid #394d45;
                border-radius: 10px;
                background-color: white;
            }
            QToolButton {
                background-color: #31b7e8;
                color: #394d45;
                font-size: 16px;
                font-weight: bold;
                width: 300px;
                height: 40px;
            }
            QToolButton:disabled {
                background-color: #e0f1eb;
            }
            QToolButton:enabled {
                background-color: #394d45;
                color: white;
            }
            QToolButton:hover {
                background-color: #25312c;

            }
        """)

        self.run_btn = QToolButton()
        self.run_btn.setText("Run")
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
            result_frame.setFixedSize(300, 310)
        result_frame.setStyleSheet("""
                    QFrame {
                        border: 2px solid #394d45;
                        border-radius: 10px;
                        background-color: white;
                    }
                    QToolButton {
                        background-color: #394d45;
                        font-size: 16px;
                        font-weight: bold;
                        width: 300px;
                        height: 40px;
                        color: white;
                    }
                    QToolButton:hover {
                        background-color: #25312c;
                        cursor: pointer;
                    }
                    QToolButton:disabled {
                        background-color: #e0f1eb;
                        color: #394d45;
                    }
                    QLabel {
                        font-size: 18px;
                        color: #394d45;
                        border: 0px solid #394d45;
                    }
                """)

        tests_run = tests_passed = tests_failed = 0
        for service, tests in globals.log_history.items():
            for test in tests:
                tests_run += 1
                did_fail = False
                for log in range(len(globals.log_history[service][test])):
                    if '❌' in globals.log_history[service][test][log]:
                        did_fail = True
                if did_fail:
                    tests_failed += 1
                else:
                    tests_passed += 1
        tests_run_label = QLabel(f"Tests run: {tests_run}")
        tests_passed_label = QLabel(f"Tests passed: {tests_passed}")
        tests_failed_label = QLabel(f"Tests failed: {tests_failed}")

        result_btn = QToolButton()
        result_btn.setText("Results")
        result_btn.setCursor(Qt.PointingHandCursor)
        result_btn.clicked.connect(self.result_btn_clicked)
        export_btn = QToolButton()
        export_btn.setEnabled(False) if tests_run == 0 else export_btn.setEnabled(True)
        export_btn.setText("Export")
        export_btn.setCursor(Qt.PointingHandCursor)
        export_btn.clicked.connect(self.export_result)
        import_btn = QToolButton()
        import_btn.setText("Import")
        import_btn.setCursor(Qt.PointingHandCursor)
        import_btn.clicked.connect(self.import_result)
        if self.screen == 'Laptop':
            result_btn.setFixedHeight(40)
            export_btn.setFixedHeight(40)
            import_btn.setFixedHeight(40)

        result_btn_layout = QVBoxLayout()
        result_btn_layout.addWidget(tests_run_label)
        result_btn_layout.addWidget(tests_passed_label)
        result_btn_layout.addWidget(tests_failed_label)
        result_btn_layout.addWidget(result_btn)
        result_btn_layout.addWidget(export_btn)
        result_btn_layout.addWidget(import_btn)
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
        globals.phone_type = platform

    def _select_car(self, car_type):
        if car_type == "ice":
            self.ice_btn.setChecked(True)
            self.phev_btn.setChecked(False)
        else:
            self.ice_btn.setChecked(False)
            self.phev_btn.setChecked(True)
        globals.vehicle_type = car_type

    def _select_country(self, country):
        if country == "eur":
            self.eur_btn.setChecked(True)
            self.nar_btn.setChecked(False)
            self.chn_btn.setChecked(False)
        elif country == "nar":
            self.eur_btn.setChecked(False)
            self.nar_btn.setChecked(True)
            self.chn_btn.setChecked(False)
        else:
            self.eur_btn.setChecked(False)
            self.nar_btn.setChecked(False)
            self.chn_btn.setChecked(True)
        globals.country = country

    def open_service_tests(self, service):
        self.main_window.show_test_cases(service)

    def all_tests_checkbox(self, checked, table):
        self.clear_checkboxes(table)
        for row in range(4, table.rowCount()):
            cell_widget = table.cellWidget(row, 1)
            if cell_widget:
                cb = cell_widget.findChild(QCheckBox)
                if cb:
                    cb.setChecked(checked)
                    cb.setEnabled(not checked)

    def no_vehicle_tests_checkbox(self, checked, table):
        self.clear_checkboxes(table, 1)
        for row in range(4, table.rowCount()):
            cell_widget = table.cellWidget(row, 0).findChild(QLabel).text()
            plain_text = re.sub('<[^<]+?>', '', cell_widget)
            if plain_text in no_vehicle_services:
                cb = table.cellWidget(row, 1).findChild(QCheckBox)
                if cb:
                    cb.setChecked(checked)
                    cb.setEnabled(not checked)

    def vehicle_tests_checkbox(self, checked, table):
        self.clear_checkboxes(table, 2)
        for row in range(4, table.rowCount()):
            cell_widget = table.cellWidget(row, 0).findChild(QLabel).text()
            plain_text = re.sub('<[^<]+?>', '', cell_widget)
            if plain_text in only_vehicle_services:
                cb = table.cellWidget(row, 1).findChild(QCheckBox)
                if cb:
                    cb.setChecked(checked)
                    cb.setEnabled(not checked)

    def no_precondition_tests_checkbox(self, checked, table):
        self.clear_checkboxes(table, 3)
        for row in range(4, table.rowCount()):
            cell_widget = table.cellWidget(row, 0).findChild(QLabel).text()
            plain_text = re.sub('<[^<]+?>', '', cell_widget)
            if plain_text in no_precondition_services:
                cb = table.cellWidget(row, 1).findChild(QCheckBox)
                if cb:
                    cb.setChecked(checked)
                    cb.setEnabled(not checked)

    def clear_checkboxes(self, table, current=-1):
        for row in range(1, table.rowCount()):
            if row is not current:
                cell_widget = table.cellWidget(row, 1)
                if cell_widget:
                    cb = cell_widget.findChild(QCheckBox)
                    if cb:
                        cb.setChecked(False)
                        cb.setEnabled(True)

    def update_run_btn(self, table):
        name_filled = bool(self.name_input.text().strip())
        email_filled = bool(self.email_input.text().strip())
        password_filled = bool(self.password_input.text().strip())
        pin_filled = bool(self.pin_input.text().strip())
        vehicle_type = self.ice_btn.isChecked() or self.phev_btn.isChecked()
        phone_type = self.ios_btn.isChecked() or self.android_btn.isChecked()
        country = self.chn_btn.isChecked() or self.eur_btn.isChecked() or self.nar_btn.isChecked()
        checkbox_check = False
        for row in range(table.rowCount()):
            cell_widget = table.cellWidget(row, 1)
            if cell_widget:
                cb = cell_widget.findChild(QCheckBox)
                if cb.isChecked():
                    checkbox_check = True

        can_submit = name_filled and email_filled and password_filled and pin_filled and vehicle_type and phone_type and checkbox_check and country

        self.run_btn.setEnabled(can_submit)

    def run_selected_services(self, table):
        globals.log_history = {}
        globals.service_index = 0
        globals.selected_services = []
        for row in range(table.rowCount()):
            cell_widget = table.cellWidget(row, 1)
            if cell_widget:
                cb = cell_widget.findChild(QCheckBox)
                if cb.isChecked():
                    globals.selected_services.append(services[row-4])
        globals.current_name = self.name_input.text()
        globals.current_email = self.email_input.text()
        globals.current_password = self.password_input.text()
        globals.current_pin = self.pin_input.text()

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
        # save_folder = os.path.join(script_dir, "test_results")
        save_folder = globals.sharedrive_path
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

    def import_result(self):
        self.import_window = ImportResult()
        self.import_window.show()