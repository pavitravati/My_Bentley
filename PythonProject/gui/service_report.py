from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, QScrollArea, QToolBar, QToolButton, \
    QSizePolicy, QPushButton, QComboBox
from PySide6.QtGui import QFont, QPixmap, QStandardItemModel
from PySide6.QtCore import Qt
from pathlib import Path
from PySide6.QtWidgets import QApplication
from openpyxl.reader.excel import load_workbook
from excel import load_data
import os
import glob
import globals

testcase_map = load_data()

class ServiceReport(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        try:
            self.service = next(iter(globals.log_history))
            self.current_test = True
        except:
            self.service = None
            self.current_test = False

        screen = QApplication.primaryScreen()
        screen_size = screen.availableGeometry()
        width = int(screen_size.width() * 0.8)
        height = int(screen_size.height() * 0.9)
        self.resize(width, height)

        self.setFixedSize(width, height)

        self.setWindowTitle(self.service)
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.build_body_for_service(layout)

    def toolbar_button_clicked(self, svc, layout):
        self.service = svc
        self.refresh_ui(layout)

    def toolbar_button_clicked_import(self, svc, layout, folder_name):
        self.service = svc
        self.refresh_ui(layout, new_folder=True, folder_name=folder_name)

    def refresh_ui(self, current_layout, new_folder=False, folder_name=None):
        # Clear the existing layout (everything except toolbar)
        main_layout = self.layout()

        # Remove all widgets after the toolbar (index 1 onward)
        for i in reversed(range(0, main_layout.count())):
            item = main_layout.itemAt(i)
            widget = item.widget()
            if widget:
                widget.deleteLater()
            else:
                layout = item.layout()
                if layout:
                    while layout.count():
                        sub_item = layout.takeAt(0)
                        sub_widget = sub_item.widget()
                        if sub_widget:
                            sub_widget.deleteLater()
                    main_layout.removeItem(layout)

        if new_folder:
            self.build_body_for_folder(current_layout, folder_name)
        else:
            self.build_body_for_service(current_layout)

    def build_body_for_service(self, layout):
        toolbar = QHBoxLayout()
        self.dropdown = QComboBox()
        if self.current_test:
            self.dropdown.addItem("Current test")
        else:
            self.dropdown.addItem("Select test")
        script_dir = os.path.dirname(os.path.abspath(__file__))
        results_folder = os.path.join(script_dir, "test_results")
        folder_names = [name for name in os.listdir(results_folder) if
                        os.path.isdir(os.path.join(results_folder, name))]
        for folder in folder_names:
            self.dropdown.addItem(f"{folder.replace('+', ':')}")
        self.dropdown.currentTextChanged.connect(lambda text: self.show_test_result(layout, text))

        toolbar.addWidget(self.dropdown)

        for service in globals.log_history:
            toolbar_btn = QPushButton(service)
            toolbar_btn.clicked.connect(lambda checked, svc=service: self.toolbar_button_clicked(svc, layout))
            toolbar.addWidget(toolbar_btn)
        toolbar.addStretch()

        layout.addLayout(toolbar)

        top_layout = QHBoxLayout()
        top_layout.setContentsMargins(0, 40, 0, 20)

        title = QLabel(self.service)
        title.setFont(QFont("Arial", 25, QFont.Bold))
        title.setStyleSheet("margin-left: 20px; margin-bottom: 20px;")
        top_layout.addWidget(title)

        top_layout.addStretch()

        logo = QLabel()
        img_path = Path(__file__).parent / "images" / "bentleylogo.png"
        pixmap = QPixmap(str(img_path))
        logo.setPixmap(pixmap)
        logo.setScaledContents(True)
        logo.setMaximumSize(135, 50)
        logo.setStyleSheet("margin-right: 20px;")
        top_layout.addWidget(logo)

        layout.addLayout(top_layout)

        container_layout = QHBoxLayout()

        # Add all testcases so that they can all be viewed
        testcase_scroll = QScrollArea()
        testcase_scroll.setWidgetResizable(True)
        testcase_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        testcase_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        testcase_scroll.setFixedWidth(340)
        testcase_scroll.setStyleSheet("""
            QScrollArea {
                border: none;
                background: transparent;
            }
            QScrollBar:vertical {
                background: transparent;
                width: 10px;   
                margin: 0px 5px 0px 0px;
                border-radius: 5px;
            }
        """)

        # container that holds buttons
        testcase_container = QWidget()
        testcase_layout = QVBoxLayout(testcase_container)
        testcase_layout.setAlignment(Qt.AlignTop)

        if self.service:
            for row, case in enumerate(globals.log_history[self.service]):
                result = '✅'
                for i in range(len(globals.log_history[self.service][case])):
                    if globals.log_history[self.service][case][i][0] == '❌':
                        result = '❌'
                        break

                btn = QToolButton()
                test_description = testcase_map[self.service][row]['Test Case Description']
                btn.setText(test_description)
                btn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
                btn.setFixedWidth(320)
                btn.setFixedHeight(45)
                btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)

                if result == '✅':
                    btn.setStyleSheet("background-color: #394d45; font-size: 12px; color: white;")
                else:
                    btn.setStyleSheet("background-color: #7d232b; font-size: 12px; color: white;")

                row_logs = globals.log_history[self.service][case]
                logs_combined = "\n".join(row_logs)
                btn.clicked.connect(
                    lambda checked, c=test_description, l=logs_combined, r=row + 1, s=self.service:
                    self.on_test_clicked(c, l, r, s)
                )
                testcase_layout.addWidget(btn)

        testcase_scroll.setWidget(testcase_container)

        container_layout.addWidget(testcase_scroll)

        detail_layout = QVBoxLayout()

        self.log_textbox = QTextEdit()
        parent_height = self.parent().height() if self.parent() else 800
        screen_size = QApplication.primaryScreen().size()
        available_width = screen_size.width()
        if available_width > 1500:
            multi = 0.35
        else:
            multi = 0.25
        self.log_textbox.setFixedHeight(int(parent_height * multi))
        self.log_textbox.setReadOnly(True)
        self.log_textbox.setFont(QFont("Arial", 12))

        detail_layout.addWidget(self.log_textbox)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        container = QWidget()
        self.images_layout = QHBoxLayout(container)
        self.images_layout.setSpacing(5)
        self.images_layout.setContentsMargins(20, 0, 20, 0)

        scroll_area.setWidget(container)

        detail_layout.addWidget(scroll_area)

        container_layout.addLayout(detail_layout)

        layout.addLayout(container_layout)

    def on_test_clicked(self, test_case, logs_combined, row, service, imported_test=False, folder_name=None):
        self.log_textbox.append(test_case)
        if type(logs_combined) == str:
            self.log_textbox.setPlainText(logs_combined)
        else:
            self.log_textbox.setPlainText(str(logs_combined.value))

        while self.images_layout.count():
            item = self.images_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        if imported_test:
            image_dir = os.path.join(folder_name, "images")
        else:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            image_dir = os.path.join(base_dir, "fail_images")
        image_paths = []
        row_num = f"0{row}" if row < 10 else f"{row}"

        for file_path in glob.glob(os.path.join(image_dir, "*.png")):
            filename = os.path.basename(file_path)
            if row_num in filename and service in filename:
                image_paths.append(file_path)

        for img_path_str in image_paths:
            internal_container = QWidget()
            # May need changing to work on laptop and monitor
            internal_container.setFixedWidth(280)
            report_image = QVBoxLayout(internal_container)

            img_path = Path(img_path_str)
            pixmap = QPixmap(str(img_path))
            if pixmap.isNull():
                print(f"Failed to load image: {img_path}")
                continue

            img_label = QLabel()
            img_text = img_path_str.split(" - ")
            if '❌' in img_text[0]:
                img_text = img_text[1].split("-")[0]
            else:
                img_text = img_text[0].split("-")[1].replace('_', ' ').replace('.png', '')
            img_label.setText(img_text)
            img_label.setFont(QFont("Arial", 12))
            img_label.setWordWrap(True)
            report_image.addWidget(img_label)

            image_display = QLabel()

            screen_size = QApplication.primaryScreen().size()
            available_width = screen_size.width()
            if available_width > 1500:
                img_size = 410
            else:
                img_size = 260
            image_display.setPixmap(pixmap.scaled(img_size, img_size, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            image_display.setStyleSheet("margin: 5px;")

            report_image.addWidget(image_display)
            self.images_layout.addWidget(internal_container)

    def show_test_result(self, layout, text):
        if text == 'Current test':
            self.service = next(iter(globals.log_history))
            self.refresh_ui(layout)
        else:
            folder_name = text.replace(':', '+')
            script_dir = os.path.dirname(os.path.abspath(__file__))
            results_folder = os.path.join(script_dir, "test_results")
            test_folder_path = os.path.join(results_folder, folder_name)
            test_result_file = load_workbook(os.path.join(test_folder_path, "test_results.xlsx"))
            self.service = test_result_file.sheetnames[0]
            self.refresh_ui(layout, new_folder=True, folder_name=folder_name)

    def build_body_for_folder(self, layout, folder_name):
        toolbar = QHBoxLayout()
        self.dropdown = QComboBox()
        self.dropdown.addItem(folder_name.replace("+", ":"))
        if self.current_test:
            self.dropdown.addItem("Current test")
        script_dir = os.path.dirname(os.path.abspath(__file__))
        results_folder = os.path.join(script_dir, "test_results")
        folder_names = [name for name in os.listdir(results_folder) if
                        os.path.isdir(os.path.join(results_folder, name)) and folder_name != name]
        for folder in folder_names:
            self.dropdown.addItem(f"{folder.replace('+', ':')}")
        self.dropdown.currentTextChanged.connect(lambda text: self.show_test_result(layout, text))

        toolbar.addWidget(self.dropdown)

        test_folder_path = os.path.join(results_folder, folder_name)
        test_result_file = load_workbook(os.path.join(test_folder_path, "test_results.xlsx"))
        for sheet in test_result_file.sheetnames:
            toolbar_btn = QPushButton(sheet)
            toolbar_btn.clicked.connect(lambda checked, svc=sheet: self.toolbar_button_clicked_import(svc, layout, folder_name))
            toolbar.addWidget(toolbar_btn)
        toolbar.addStretch()

        layout.addLayout(toolbar)

        top_layout = QHBoxLayout()
        top_layout.setContentsMargins(0, 40, 0, 20)

        title = QLabel(self.service)
        title.setFont(QFont("Arial", 25, QFont.Bold))
        title.setStyleSheet("margin-left: 20px; margin-bottom: 20px;")
        top_layout.addWidget(title)

        top_layout.addStretch()

        logo = QLabel()
        img_path = Path(__file__).parent / "images" / "bentleylogo.png"
        pixmap = QPixmap(str(img_path))
        logo.setPixmap(pixmap)
        logo.setScaledContents(True)
        logo.setMaximumSize(135, 50)
        logo.setStyleSheet("margin-right: 20px;")
        top_layout.addWidget(logo)

        layout.addLayout(top_layout)

        container_layout = QHBoxLayout()

        # Add all testcases so that they can all be viewed
        testcase_scroll = QScrollArea()
        testcase_scroll.setWidgetResizable(True)
        testcase_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        testcase_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        testcase_scroll.setFixedWidth(340)
        testcase_scroll.setStyleSheet("""
                    QScrollArea {
                        border: none;
                        background: transparent;
                    }
                    QScrollBar:vertical {
                        background: transparent;
                        width: 10px;   
                        margin: 0px 5px 0px 0px;
                        border-radius: 5px;
                    }
                """)

        # container that holds buttons
        testcase_container = QWidget()
        testcase_layout = QVBoxLayout(testcase_container)
        testcase_layout.setAlignment(Qt.AlignTop)
        current_sheet = test_result_file[self.service]

        for row in range(1, current_sheet.max_row+1):
            cell_value = current_sheet[f'B{row}'].value
            result = '❌' if '❌' in str(cell_value) else '✅'

            btn = QToolButton()
            test_description = str(current_sheet[f'A{row}'].value)
            btn.setText(test_description)
            btn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
            btn.setFixedWidth(320)
            btn.setFixedHeight(45)
            btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)

            if result == '✅':
                btn.setStyleSheet("background-color: #394d45; font-size: 12px; color: white;")
            else:
                btn.setStyleSheet("background-color: #7d232b; font-size: 12px; color: white;")

            row_logs = current_sheet[f'B{row}']
            btn.clicked.connect(
                lambda checked, c=test_description, l=row_logs, r=row, s=self.service:
                self.on_test_clicked(c, l, r, s, True, test_folder_path)
            )
            testcase_layout.addWidget(btn)

        testcase_scroll.setWidget(testcase_container)

        container_layout.addWidget(testcase_scroll)

        detail_layout = QVBoxLayout()

        self.log_textbox = QTextEdit()
        parent_height = self.parent().height() if self.parent() else 800
        screen_size = QApplication.primaryScreen().size()
        available_width = screen_size.width()
        if available_width > 1500:
            multi = 0.35
        else:
            multi = 0.25
        self.log_textbox.setFixedHeight(int(parent_height * multi))
        self.log_textbox.setReadOnly(True)
        self.log_textbox.setFont(QFont("Arial", 12))

        detail_layout.addWidget(self.log_textbox)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        container = QWidget()
        self.images_layout = QHBoxLayout(container)
        self.images_layout.setSpacing(5)
        self.images_layout.setContentsMargins(20, 0, 20, 0)

        scroll_area.setWidget(container)

        detail_layout.addWidget(scroll_area)

        container_layout.addLayout(detail_layout)

        layout.addLayout(container_layout)