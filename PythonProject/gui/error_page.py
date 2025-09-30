from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, QScrollArea
from PySide6.QtGui import QFont, QPixmap
from pathlib import Path
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt

class ErrorPage(QWidget):
    def __init__(self, title: str, logs: list[str], images: list[str], parent=None):
        super().__init__(parent)

        screen = QApplication.primaryScreen()
        screen_size = screen.availableGeometry()
        width = int(screen_size.width() * 0.7)
        height = int(screen_size.height() * 0.7)
        self.resize(width, height)

        self.setFixedSize(width, height)

        self.setWindowTitle(title)
        layout = QVBoxLayout()
        self.setLayout(layout)

        top_layout = QHBoxLayout()
        top_layout.setContentsMargins(0, 40, 0, 20)

        title = QLabel(title)
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

        detail_layout = QHBoxLayout()

        self.log_textbox = QTextEdit()
        self.log_textbox.setReadOnly(True)

        logs_combined = "\n".join(logs)

        self.log_textbox.setPlainText(logs_combined)
        self.log_textbox.setFont(QFont("Arial", 12))

        detail_layout.addWidget(self.log_textbox)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        container = QWidget()
        images_layout = QHBoxLayout(container)
        images_layout.setSpacing(5)  # space between widgets
        images_layout.setContentsMargins(20, 0, 20, 0)  # remove extra layout margins

        for img_path_str in images:
            img_path = Path(img_path_str)
            pixmap = QPixmap(str(img_path))
            if pixmap.isNull():
                print(f"Failed to load image: {img_path}")
                continue

            label = QLabel()
            label.setPixmap(pixmap.scaled(500, 500, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            label.setStyleSheet("margin: 5px;")
            images_layout.addWidget(label)

        scroll_area.setWidget(container)

        detail_layout.addWidget(scroll_area)

        layout.addLayout(detail_layout)