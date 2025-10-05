from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, QScrollArea, QPushButton
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtCore import Qt
from pathlib import Path
from PySide6.QtWidgets import QApplication
from excel import load_data
import os
import glob

class ServiceReport(QWidget):
    def __init__(self, service_title: str, logs: dict[int, list], parent=None):
        super().__init__(parent)
        testcase_map = load_data()

        screen = QApplication.primaryScreen()
        screen_size = screen.availableGeometry()
        width = int(screen_size.width() * 0.8)
        height = int(screen_size.height() * 0.9)
        self.resize(width, height)

        self.setFixedSize(width, height)

        self.setWindowTitle(service_title)
        layout = QVBoxLayout()
        self.setLayout(layout)

        top_layout = QHBoxLayout()
        top_layout.setContentsMargins(0, 40, 0, 20)

        title = QLabel(service_title)
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
        testcase_layout = QVBoxLayout()
        for row, case in enumerate(testcase_map[service_title]):
            result = '✅'
            for i in range(len(logs[row+1])):
                if logs[row+1][i][0] == '❌':
                    result = '❌'
            btn = QPushButton(f"{service_title}_0{f"0{row+1}" if row+1 < 10 else f"{row+1}"} - {result}")
            btn.setCursor(Qt.PointingHandCursor)
            btn.setStyleSheet("font-size: 12px; height: 25px; width: 200px; background-color: #394d45; color: white;")
            row_logs = logs[row+1]
            logs_combined = "\n".join(row_logs)
            btn.clicked.connect(
                lambda checked, s=service_title, c=case, l=logs_combined, r=row + 1:
                self.on_test_clicked(s, c, l, r)
            )
            testcase_layout.addWidget(btn)

        container_layout.addLayout(testcase_layout)

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

    # also
    def on_test_clicked(self, test_name, test_case, logs_combined, row):
        print(f"Clicked test case: {test_name} {test_case}")
        self.log_textbox.append(test_case['Test Case Description'])
        self.log_textbox.setPlainText(logs_combined)

        while self.images_layout.count():
            item = self.images_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        base_dir = os.path.dirname(os.path.abspath(__file__))
        image_dir = os.path.join(base_dir, "fail_images")
        image_paths = []
        row_num = f"0{row}" if row < 10 else f"{row}"

        for file_path in glob.glob(os.path.join(image_dir, "*.png")):
            filename = os.path.basename(file_path)
            if row_num in filename:
                image_paths.append(file_path)

        for img_path_str in image_paths:
            img_path = Path(img_path_str)
            pixmap = QPixmap(str(img_path))
            if pixmap.isNull():
                print(f"Failed to load image: {img_path}")
                continue

            label = QLabel()
            screen_size = QApplication.primaryScreen().size()
            available_width = screen_size.width()
            if available_width > 1500:
                img_size = 450
            else:
                img_size = 300
            label.setPixmap(pixmap.scaled(img_size, img_size, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            label.setStyleSheet("margin: 5px;")
            self.images_layout.addWidget(label)