from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QApplication, QMessageBox
from PySide6.QtGui import QFont, QPixmap, QStandardItemModel
from PySide6.QtCore import Qt
from pathlib import Path
from PySide6.QtWidgets import QApplication
from openpyxl.reader.excel import load_workbook
from excel import load_data
import os
import glob
import globals
import shutil

class ImportResult(QWidget):
    def __init__(self):
        super().__init__()
        screen = QApplication.primaryScreen()
        screen_size = screen.availableGeometry()
        width = int(screen_size.width() * 0.3)
        height = int(screen_size.height() * 0.20)
        self.resize(width, height)
        self.setFixedSize(width, height)
        self.setWindowTitle("Import Results")

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignTop)
        layout.setContentsMargins(20, 20, 20, 20)

        self.info_label = QLabel("No folder selected.")
        self.info_label.setWordWrap(True)
        self.info_label.setStyleSheet("font-size: 18px; font-color:#394d45;")
        self.info_label.setContentsMargins(10, 10, 10, 10)

        self.pick_button = QPushButton("Select Folder")
        self.pick_button.clicked.connect(self.pick_folder)
        self.pick_button.setCursor(Qt.PointingHandCursor)
        self.pick_button.setStyleSheet("""
                    QPushButton {
                        background-color: #394d45;
                        font-size: 16px;
                        font-weight: bold;
                        width: 130px;
                        height: 40px;
                        border: none;
                        border-radius: 10px;
                        padding: 6px 10px;
                        color: white;
                    }
                    QPushButton:hover {
                        background-color: #25312c;
                        cursor: pointer;
                    }
                """)

        layout.addWidget(self.pick_button)
        layout.addWidget(self.info_label)

        self.setLayout(layout)

    def pick_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select a Folder")

        if folder_path:
            # folder_name = os.path.basename(folder_path)
            # script_dir = os.path.dirname(os.path.abspath(__file__))
            # save_folder = os.path.join(script_dir, "test_results", folder_name)
            save_folder = globals.sharedrive_path

            # If it already exists, confirm overwrite
            if os.path.exists(save_folder):
                reply = QMessageBox.question(
                    self,
                    "Overwrite?",
                    f"Folder '{folder_name}' already exists in target directory.\n\nOverwrite?",
                    QMessageBox.Yes | QMessageBox.No,
                    QMessageBox.No
                )
                if reply == QMessageBox.No:
                    return
                shutil.rmtree(save_folder)

            try:
                shutil.copytree(folder_path, save_folder)
                self.info_label.setText(f"✅ Folder '{folder_name}' saved to {script_dir}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to copy folder:\n{e}")
                self.info_label.setText("❌ Error saving folder.")