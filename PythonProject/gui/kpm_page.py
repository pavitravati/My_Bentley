from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, QScrollArea, QToolButton
from PySide6.QtGui import QFont, QPixmap
from pathlib import Path
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt

class KPMPage(QWidget):
    def __init__(self, title: str, kpm: str, parent=None):
        super().__init__(parent)
        if QApplication.primaryScreen().size().width() > 1500:
            self.screen = 'Monitor'
        else:
            self.screen = 'Laptop'

        screen = QApplication.primaryScreen()
        screen_size = screen.availableGeometry()
        if self.screen == 'Monitor':
            width = int(screen_size.width() * 0.4)
            height = int(screen_size.height() * 0.9)
        else:
            width = int(screen_size.width() * 0.4)
            height = int(screen_size.height() * 0.8)

        self.resize(width, height)
        self.setFixedSize(width, height)

        self.setWindowTitle(title)
        layout = QVBoxLayout()
        self.setLayout(layout)

        top_layout = QHBoxLayout()
        top_layout.setContentsMargins(0, 40, 0, 20)

        title = QLabel(title)
        title.setFont(QFont("Arial", 18, QFont.Bold))
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

        self.log_textbox.setPlainText(kpm)
        self.log_textbox.setFont(QFont("Arial", 13))

        detail_layout.addWidget(self.log_textbox)
        layout.addLayout(detail_layout)

        copy_btn = QToolButton()
        copy_btn.setText("Copy KPM")
        copy_btn.setCursor(Qt.PointingHandCursor)
        copy_btn.setStyleSheet("""
                            QToolButton {
                                background-color: #394d45;
                                font-size: 16px;
                                font-weight: bold;
                                width: 180px;
                                height: 40px;
                                color: white;
                            }
                            QToolButton:hover {
                                background-color: #25312c;
                            }
                        """)
        copy_btn.clicked.connect(self.copy_kpm)
        layout.addWidget(copy_btn, alignment=Qt.AlignCenter)

    def copy_kpm(self):
        kpm_text = self.log_textbox.toPlainText()
        QApplication.clipboard().setText(kpm_text)