from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, QScrollArea
from PySide6.QtGui import QFont, QPixmap
from pathlib import Path
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt

class MetricPage(QWidget):
    def __init__(self, title: str, logs: list[str], parent=None):
        super().__init__(parent)

        screen = QApplication.primaryScreen()
        screen_size = screen.availableGeometry()
        width = int(screen_size.width() * 0.5)
        height = int(screen_size.height() * 0.5)
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
        print(logs)

        logs_combined = "\n".join(logs)

        self.log_textbox.setPlainText(logs_combined)
        self.log_textbox.setFont(QFont("Arial", 13))

        detail_layout.addWidget(self.log_textbox)

        layout.addLayout(detail_layout)