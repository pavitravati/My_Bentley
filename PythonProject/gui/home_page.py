import re
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QTableWidget, QLabel, QCheckBox, QHBoxLayout,
    QHeaderView, QTableWidgetItem, QFrame, QLineEdit, QSizePolicy, QApplication, QToolButton
)
from PySide6.QtGui import QFont, QPixmap, QCursor
from PySide6.QtCore import Qt, Signal
# from gui.excel import resource_path, load_data, services, service_details
from gui.excel import resource_path, load_data
from service_details import all_services, service_requirements
from gui.import_page import ImportResult
from test_case_page import TestCaseTablePage
from service_report import ServiceReport
from openpyxl import Workbook
from datetime import datetime
import shutil
import core.globals as globals
from Test_Scripts.Android.detail_collector import get_details
from common_utils.android_image_comparision import *
from time import sleep

testcase_map = load_data()

class ClickableLabel(QLabel):
    clicked = Signal()
    def __init__(self, text):
        super().__init__(f"<a style='color:black; text-decoration:none; font-size:14px; margin:0px' href='#'>{text}</a>")
        self.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.setOpenExternalLinks(False)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.linkActivated.connect(lambda _: self.clicked.emit())

class BlockedLabel(QLabel):
    def __init__(self, normal_text, hover_text):
        super().__init__(normal_text)
        self.normal_text = normal_text
        self.hover_text = hover_text
        self.setMouseTracking(True)
        self.setStyleSheet("color:gray; font-size:14px;")

    def enterEvent(self, event):
        self.setText(self.hover_text)
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.setText(self.normal_text)
        super().leaveEvent(event)

class HomePage(QWidget):
    def __init__(self, main_window, parent=None):
        super().__init__(parent)
        self.main_window = main_window
        QApplication.primaryScreen().size().width()
        if QApplication.primaryScreen().size().width() > 1500:
            self.screen = 'Monitor'
        else:
            self.screen = 'Laptop'

        globals.manual_run = True

        # try:
        #     controller.d.press("recent")
        #     sleep(0.5)
        #     controller.click_text("Close all")
        #     controller.launch_app("uk.co.bentley.mybentley")
        #     while not controller.is_text_present("DASHBOARD") and not controller.is_text_present("LOGIN OR REGISTER"):
        #         sleep(0.2)
        # except:
        #     pass

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
        testcase_table.setRowCount(len(all_services)+4)
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

        for row in range(len(all_services)+4):
            checkbox = QCheckBox()
            # checkbox.clicked.connect(lambda: self.update_run_btn(testcase_table))
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
                checkbox.clicked.connect(lambda checked, t=testcase_table: self.all_tests_checkbox(checked, t))
                checkbox.clicked.connect(lambda: self.update_run_btn(testcase_table))
            elif row == 1:
                item = QTableWidgetItem("No Vehicle services")
                item.setFont(QFont("Arial", 12, QFont.Bold))
                testcase_table.setItem(row, 0, item)
                testcase_table.setCellWidget(row, 1, cell_widget)
                checkbox.clicked.connect(lambda checked, t=testcase_table: self.no_vehicle_tests_checkbox(checked, t))
                checkbox.clicked.connect(lambda: self.update_run_btn(testcase_table))
            elif row == 2:
                item = QTableWidgetItem("Only Vehicle services")
                item.setFont(QFont("Arial", 12, QFont.Bold))
                testcase_table.setItem(row, 0, item)
                testcase_table.setCellWidget(row, 1, cell_widget)
                checkbox.clicked.connect(lambda checked, t=testcase_table: self.vehicle_tests_checkbox(checked, t))
                checkbox.clicked.connect(lambda: self.update_run_btn(testcase_table))
            elif row == 3:
                item = QTableWidgetItem("No precondition services")
                item.setFont(QFont("Arial", 12, QFont.Bold))
                testcase_table.setItem(row, 0, item)
                testcase_table.setCellWidget(row, 1, cell_widget)
                checkbox.clicked.connect(lambda checked, t=testcase_table: self.no_precondition_tests_checkbox(checked, t))
                checkbox.clicked.connect(lambda: self.update_run_btn(testcase_table))
            else:
                if service_requirements[all_services[row - 4]]['requirements']['reason_for_block'] == "":
                    label = ClickableLabel(all_services[row - 4])
                    label.clicked.connect(lambda r=row: self.open_service_tests(all_services[r - 4]))
                    checkbox.clicked.connect(lambda _=None, check=service_requirements[all_services[row-4]]['fields'], t=testcase_table: self.enable_credentials(check, t))
                    checkbox.clicked.connect(lambda: self.update_run_btn(testcase_table))
                else:
                    label = BlockedLabel(all_services[row - 4], service_requirements[all_services[row - 4]]['requirements']['reason_for_block'])
                    checkbox.setDisabled(True)


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
                    QLineEdit:disabled {
                        background-color: #F4F6F6;
                        color: #C9CACA;
                        border: 1px solid #D9DADA;
                    }
                """)

        form_layout = QVBoxLayout(credentials_frame)
        form_header = QHBoxLayout()
        form_header.setAlignment(Qt.AlignCenter)

        form_title = QLabel("Credentials")
        form_title.setFont(QFont("Arial", 22, QFont.Bold))
        form_title.setStyleSheet("color: #394d45; border: 0px solid #394d45;")
        form_header.addWidget(form_title)

        self.fill_req_details_btn = QToolButton()
        self.fill_req_details_btn.setText("Get details")
        self.fill_req_details_btn.setEnabled(False)
        self.fill_req_details_btn.setCursor(Qt.PointingHandCursor)
        self.fill_req_details_btn.clicked.connect(lambda: self.get_account_details())
        self.fill_req_details_btn.setStyleSheet("""
                QToolButton {
                    background-color: #485f56;
                    color: white;
                    font-weight: bold;
                    font-size: 12px;
                }
                QToolButton:hover {
                    background-color: #25312c;
                }
                QToolButton:disabled {
                    background-color: #F4F6F6;
                    color: #D9DADA;
                }
            """)
        form_header.addWidget(self.fill_req_details_btn)
        form_layout.addLayout(form_header)

        def cred_field(text, global_var):
            text_input = QLineEdit()
            if global_var:
                text_input.setText(global_var)
            else:
                text_input.setPlaceholderText(text)
            text_input.setStyleSheet("margin-bottom: 5px;")
            text_input.textChanged.connect(lambda: self.update_globals(text.lower(), text_input.text()))
            text_input.textChanged.connect(lambda: self.update_run_btn(testcase_table))
            return text_input

        self.email_input = cred_field("Email", globals.current_email)
        self.password_input = cred_field("Password", globals.current_password)
        self.pin_input = cred_field("PIN", globals.current_pin)
        self.name_input = cred_field("Name", globals.current_name)
        self.vin_input = cred_field("VIN", globals.current_vin)

        form_layout.addWidget(self.email_input)
        form_layout.addWidget(self.password_input)
        form_layout.addWidget(self.pin_input)
        form_layout.addWidget(self.name_input)
        form_layout.addWidget(self.vin_input)
        form_layout.setContentsMargins(30, 30, 30, 30)

        platform_layout = QHBoxLayout()
        platform_layout.setSpacing(10)
        platform_layout.setAlignment(Qt.AlignCenter)

        self.android_btn = QToolButton()
        self.ios_btn = QToolButton()
        self.android_btn.setText("Android")
        self.ios_btn.setText("iOS")

        self.android_btn.clicked.connect(lambda: self._select_platform("android"))
        self.ios_btn.clicked.connect(lambda: self._select_platform("ios"))

        platform_layout.addWidget(self.android_btn)
        platform_layout.addWidget(self.ios_btn)

        vehicle_type_layout = QHBoxLayout()
        vehicle_type_layout.setSpacing(10)
        vehicle_type_layout.setAlignment(Qt.AlignCenter)

        self.ice_btn = QToolButton()
        self.ice_btn.setText("ICE")
        self.phev_btn = QToolButton()
        self.phev_btn.setText("PHEV")

        for btn in (self.ice_btn, self.phev_btn, self.android_btn, self.ios_btn):
            btn.setFixedSize(140, 45) if self.screen == 'Monitor' else btn.setFixedSize(120, 30)

        self.ice_btn.clicked.connect(lambda: self._select_car("ice"))
        self.phev_btn.clicked.connect(lambda: self._select_car("phev"))

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

        for btn in (self.eur_btn, self.nar_btn, self.chn_btn, self.ice_btn, self.phev_btn, self.android_btn, self.ios_btn):
            btn.setCheckable(True)
            btn.setCursor(Qt.PointingHandCursor)
            btn.clicked.connect(lambda _=None, selected_btn=btn: self.update_globals(selected_btn))
            btn.clicked.connect(lambda: self.update_run_btn(testcase_table))
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
                QToolButton:hover {
                    background-color: #cfd4d2;
                }
                QToolButton:checked:hover {
                    background-color: #25312c;
                }
                QToolButton:disabled {
                    background-color: #F4F6F6;
                    color: #D9DADA;
                }
            """)


        self.eur_btn.clicked.connect(lambda: self._select_country("eur"))
        self.nar_btn.clicked.connect(lambda: self._select_country("nar"))
        self.chn_btn.clicked.connect(lambda: self._select_country("chn"))

        self.eur_btn.setChecked(True if globals.country == 'eur' else False)
        self.nar_btn.setChecked(True if globals.country == 'nar' else False)
        self.chn_btn.setChecked(True if globals.country == 'chn' else False)
        self.android_btn.setChecked(True if globals.phone_type == 'android' else False)
        self.ios_btn.setChecked(True if globals.phone_type == 'ios' else False)
        self.ice_btn.setChecked(True if globals.vehicle_type == 'ice' else False)
        self.phev_btn.setChecked(True if globals.vehicle_type == 'phev' else False)

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
        fields = [globals.current_name, globals.current_email, globals.current_password, globals.current_pin, globals.current_vin, globals.vehicle_type, globals.phone_type, globals.country]
        stored = service_requirements[service]['fields'].values()

        if not any(not f and s for f, s in zip(fields, stored)) and globals.get_account_details_called:
            self.main_window.show_test_cases(service)

    def all_tests_checkbox(self, checked, table):
        self.clear_checkboxes(table)
        self.enable_credentials(checked, table=table)
        table.cellWidget(0, 1).findChild(QCheckBox).setChecked(checked)
        for row in range(4, table.rowCount()):
            cell_widget = table.cellWidget(row, 1)
            if cell_widget:
                cb = cell_widget.findChild(QCheckBox)
                text_widget = table.cellWidget(row, 0).findChild(QLabel).text()
                plain_text = re.sub('<[^<]+?>', '', text_widget)
                if cb and service_requirements[plain_text]['requirements']['reason_for_block'] == "":
                    cb.setChecked(checked)
                    cb.setEnabled(not checked)

    def no_vehicle_tests_checkbox(self, checked, table):
        self.clear_checkboxes(table)
        self.enable_credentials(checked, table=table)
        table.cellWidget(1, 1).findChild(QCheckBox).setChecked(checked)
        for row in range(4, table.rowCount()):
            cell_widget = table.cellWidget(row, 0).findChild(QLabel).text()
            plain_text = re.sub('<[^<]+?>', '', cell_widget)
            if not service_requirements[plain_text]['requirements']['needs_vehicle'] and not service_requirements[plain_text]['requirements']['reason_for_block']:
                cb = table.cellWidget(row, 1).findChild(QCheckBox)
                if cb:
                    cb.setChecked(checked)
                    cb.setEnabled(not checked)

    def vehicle_tests_checkbox(self, checked, table):
        self.clear_checkboxes(table)
        self.enable_credentials(checked, table=table)
        table.cellWidget(2, 1).findChild(QCheckBox).setChecked(checked)
        for row in range(4, table.rowCount()):
            cell_widget = table.cellWidget(row, 0).findChild(QLabel).text()
            plain_text = re.sub('<[^<]+?>', '', cell_widget)
            if service_requirements[plain_text]['requirements']['needs_vehicle'] and not service_requirements[plain_text]['requirements']['reason_for_block']:
                cb = table.cellWidget(row, 1).findChild(QCheckBox)
                if cb:
                    cb.setChecked(checked)
                    cb.setEnabled(not checked)

    def no_precondition_tests_checkbox(self, checked, table):
        self.clear_checkboxes(table)
        self.enable_credentials(checked, table=table)
        table.cellWidget(3, 1).findChild(QCheckBox).setChecked(checked)
        for row in range(4, table.rowCount()):
            cell_widget = table.cellWidget(row, 0).findChild(QLabel).text()
            plain_text = re.sub('<[^<]+?>', '', cell_widget)
            if not service_requirements[plain_text]['requirements']['has_preconditions'] and not service_requirements[plain_text]['requirements']['reason_for_block']:
                cb = table.cellWidget(row, 1).findChild(QCheckBox)
                if cb:
                    cb.setChecked(checked)
                    cb.setEnabled(not checked)

    def clear_checkboxes(self, table):
        for row in range(0, table.rowCount()):
            cell_widget = table.cellWidget(row, 1)
            if cell_widget:
                cb = cell_widget.findChild(QCheckBox)
                if cb:
                    cb.setChecked(False)
                    if row > 3:
                        if service_requirements[all_services[row - 4]]['requirements']['reason_for_block'] == "":
                            cb.setEnabled(True)
                        else:
                            cb.setDisabled(True)

    def enable_credentials(self, checker=(1,1,1,1,1,1,1,1), table=None):
        total_checked = (0,0,0,0,0,0,0,0)
        min_checked = False
        for row in range(table.rowCount()):
            cell_widget = table.cellWidget(row, 1)
            if cell_widget:
                cb = cell_widget.findChild(QCheckBox)
                if cb.isChecked() and row < 4:
                    min_checked = True
                    total_checked = (1,1,1,1,1,1,1,1)
                elif cb.isChecked():
                    min_checked = True
                    total_checked = tuple(a or b for a, b in zip(total_checked, service_requirements[all_services[row-4]]['fields'].values()))

        widget_groups = [
            [self.name_input],
            [self.email_input],
            [self.password_input],
            [self.pin_input],
            [self.vin_input],
            [self.ice_btn, self.phev_btn],
            [self.android_btn, self.ios_btn],
            [self.chn_btn, self.eur_btn, self.nar_btn]
        ]

        for flag, group in zip(total_checked, widget_groups):
            for widget in group:
                if not min_checked:
                    widget.setEnabled(True)
                else:
                    widget.setEnabled(True if flag==1 else False)

    def update_run_btn(self, table):
        name_filled = bool(self.name_input.text().strip() != '' or not self.name_input.isEnabled())
        email_filled = bool(self.email_input.text().strip() or not self.email_input.isEnabled())
        password_filled = bool(self.password_input.text().strip() or not self.password_input.isEnabled())
        pin_filled = bool(self.pin_input.text().strip() or not self.pin_input.isEnabled())
        vehicle_type = self.ice_btn.isChecked() or self.phev_btn.isChecked() or not self.ice_btn.isEnabled()
        phone_type = self.ios_btn.isChecked() or self.android_btn.isChecked() or not self.ios_btn.isEnabled()
        country = self.chn_btn.isChecked() or self.eur_btn.isChecked() or self.nar_btn.isChecked() or not self.chn_btn.isEnabled()
        checkbox_check = False
        for row in range(table.rowCount()):
            cell_widget = table.cellWidget(row, 1)
            if cell_widget:
                cb = cell_widget.findChild(QCheckBox)
                if cb.isChecked():
                    checkbox_check = True

        can_submit = name_filled and email_filled and password_filled and pin_filled and vehicle_type and phone_type and checkbox_check and country and globals.get_account_details_called
        can_autofill = (globals.current_email != "" and globals.current_password != "")

        self.fill_req_details_btn.setEnabled(can_autofill)
        self.run_btn.setEnabled(can_submit)

    def run_selected_services(self, table):
        globals.log_history = {}
        globals.service_index = 0
        globals.selected_services = []
        globals.manual_run = False
        for row in range(table.rowCount()):
            cell_widget = table.cellWidget(row, 1)
            if cell_widget:
                cb = cell_widget.findChild(QCheckBox)
                if cb.isChecked():
                    if len(service_requirements[all_services[row-4]]['requirements']['region_locks']) == 0 or globals.country in service_requirements[all_services[row-4]]['requirements']['region_locks']:
                        globals.selected_services.append(all_services[row - 4])

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

    def update_globals(self, key, value="btn"):
        match key:
            case "name":
                globals.current_name = value
            case "email":
                globals.current_email = value
            case "password":
                globals.current_password = value
            case "pin":
                globals.current_pin = value
            case "vin":
                globals.current_vin = value
            case "ICE":
                globals.vehicle_type = "ice"
            case "PHEV":
                globals.vehicle_type = "phev"
            case "Android":
                globals.phone_type = "android"
            case "iOS":
                globals.phone_type = "ios"
            case "EUR":
                globals.country = "eur"
            case "NAR":
                globals.country = "nar"
            case "CHN":
                globals.country = "chn"

    def get_account_details(self):
        globals.get_account_details_called = True
        QApplication.setOverrideCursor(Qt.WaitCursor)
        self.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        get_details()
        self.setAttribute(Qt.WA_TransparentForMouseEvents, False)
        QApplication.restoreOverrideCursor()
        self.vin_input.setText(globals.current_vin)
        self.name_input.setText(globals.current_name)
        if globals.vehicle_type == "phev":
            self.phev_btn.setChecked(True)
        elif globals.vehicle_type == "ice":
            self.ice_btn.setChecked(True)
        QApplication.restoreOverrideCursor()
