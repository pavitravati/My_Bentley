from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel,
    QTextEdit, QApplication, QToolButton,
)
from PySide6.QtCore import Qt, Signal, QObject, Slot, QMutex, QWaitCondition
from PySide6.QtGui import QFont, QPixmap
from core.log_emitter import log, fail_log
import os
from datetime import datetime
from pathlib import Path

class ClickableLabel(QLabel):
    clicked = Signal()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit()

class ImagePopup(QDialog):
    def __init__(self, pixmap, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Image Viewer")

        layout = QVBoxLayout(self)
        label = QLabel()
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignCenter)

        layout.addWidget(label)
        self.setMinimumSize(600, 400)


class ManualCheckDialog(QDialog):
    def __init__(self, instruction, screenshot_path=None, parent=None):
        super().__init__(parent)
        self.passed = False
        self.notes = ""
        self.setup_ui(instruction, screenshot_path)

    def setup_ui(self, instruction, screenshot_path):
        self.setWindowTitle("Manual Check Required")
        self.setModal(True)
        self.setMinimumSize(600, 400)

        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        top_layout = QHBoxLayout()
        top_layout.setContentsMargins(0, 40, 0, 20)

        title = QLabel("Manual Verification Required")
        title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setStyleSheet("margin-left: 20px; margin-bottom: 20px;")
        top_layout.addWidget(title)

        top_layout.addStretch()

        logo = QLabel()
        img_path = Path(__file__).parent / "images" / "bentleylogo.png"
        pixmap = QPixmap(str(img_path))
        logo.setPixmap(pixmap)
        logo.setScaledContents(True)
        logo.setMaximumSize(108, 40)
        logo.setStyleSheet("margin-right: 20px;")
        top_layout.addWidget(logo)

        layout.addLayout(top_layout)

        instruction_label = QLabel("Instructions:")
        instruction_label.setFont(QFont("Arial", 10, QFont.Bold))
        layout.addWidget(instruction_label)

        instruction_text = QLabel(instruction)
        instruction_text.setWordWrap(True)
        instruction_text.setStyleSheet("padding: 10px; background-color: #f0f0f0; border-radius: 5px;")
        layout.addWidget(instruction_text)

        if screenshot_path and os.path.exists(screenshot_path):
            screenshot_label = QLabel("Current Screen:")
            screenshot_label.setFont(QFont("Arial", 10, QFont.Bold))
            layout.addWidget(screenshot_label)

            pixmap = QPixmap(screenshot_path)
            if not pixmap.isNull():
                scaled_pixmap = pixmap.scaled(560, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                large_pixmap = pixmap.scaled(1960, 700, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                image_label = ClickableLabel()
                image_label.setPixmap(scaled_pixmap)
                image_label.setAlignment(Qt.AlignCenter)
                image_label.setStyleSheet("border: 1px solid #ccc; background-color: white;")
                image_label.clicked.connect(lambda: self.open_image_popup(large_pixmap))

                layout.addWidget(image_label)

        notes_label = QLabel("Notes (optional):")
        notes_label.setFont(QFont("Arial", 10, QFont.Bold))
        layout.addWidget(notes_label)

        self.notes_field = QTextEdit()
        self.notes_field.setPlaceholderText("Enter any observations or notes here...")
        self.notes_field.setMaximumHeight(80)
        layout.addWidget(self.notes_field)

        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)

        self.pass_btn = QToolButton()
        self.pass_btn.setText("Pass")
        self.pass_btn.setFixedHeight(40)
        self.pass_btn.setFixedWidth(200)
        self.pass_btn.setStyleSheet("""
            QToolButton {
                background-color: #394d45;
                color: white;
                font-size: 14px;
                font-weight: bold;
            }
        """)
        self.pass_btn.setCursor(Qt.PointingHandCursor)
        self.pass_btn.clicked.connect(self.on_pass)

        self.fail_btn = QToolButton()
        self.fail_btn.setText("Fail")
        self.fail_btn.setFixedHeight(40)
        self.fail_btn.setFixedWidth(200)
        self.fail_btn.setStyleSheet("""
            QToolButton {
                background-color: #7d232b;
                color: white;
                font-size: 14px;
                font-weight: bold;
            }
        """)
        self.fail_btn.setCursor(Qt.PointingHandCursor)
        self.fail_btn.clicked.connect(self.on_fail)

        button_layout.addWidget(self.pass_btn)
        button_layout.addWidget(self.fail_btn)

        layout.addLayout(button_layout)

    def on_pass(self):
        self.passed = True
        self.notes = self.notes_field.toPlainText()
        self.accept()

    def on_fail(self):
        self.passed = False
        self.notes = self.notes_field.toPlainText()
        self.accept()

    def open_image_popup(self, image):
        popup = ImagePopup(image, self)
        popup.exec()

class ManualCheckManager(QObject):
    request_check = Signal(str, str)

    def __init__(self):
        super().__init__()
        self.mutex = QMutex()
        self.wait_condition = QWaitCondition()
        self.result = None

        self.request_check.connect(self._show_dialog, Qt.BlockingQueuedConnection)

    @Slot(str, str)
    def _show_dialog(self, instruction, screenshot_path):
        app = QApplication.instance()
        parent = app.activeWindow() if app else None

        dialog = ManualCheckDialog(instruction, screenshot_path, parent)
        dialog.exec()

        self.mutex.lock()
        self.result = (dialog.passed, dialog.notes)
        self.wait_condition.wakeAll()
        self.mutex.unlock()

    def show_and_wait(self, instruction, screenshot_path):
        self.result = None

        self.request_check.emit(instruction, screenshot_path or "")

        return self.result if self.result else (False, "No result")

_manager = None

def _get_manager():
    global _manager
    if _manager is None:
        _manager = ManualCheckManager()
        app = QApplication.instance()
        if app:
            _manager.moveToThread(app.thread())
    return _manager


def _take_screenshot(test_id, service):
    try:
        from common_utils.android_image_comparision import controller

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        base_dir = os.path.dirname(os.path.abspath(__file__))
        screenshot_dir = os.path.join(base_dir, "manual_check_screenshots")
        os.makedirs(screenshot_dir, exist_ok=True)

        filename = f"manual_check_{service.replace(' ', '_')}_{test_id}_{timestamp}.png"
        screenshot_path = os.path.join(screenshot_dir, filename)

        controller.take_screenshot(screenshot_path)
        return screenshot_path if os.path.exists(screenshot_path) else None
    except Exception as e:
        print(f"Warning: Could not take screenshot: {e}")
        return None


def manual_check(instruction, test_id=None, service=None, take_screenshot=True):
    screenshot_path = None
    if take_screenshot and test_id and service:
        screenshot_path = _take_screenshot(test_id, service)

    manager = _get_manager()
    passed, notes = manager.show_and_wait(instruction, screenshot_path)

    if passed:
        log_msg = f"Manual check PASSED: {instruction}"
        if notes:
            log_msg += f" | Notes: {notes}"
        log(log_msg)
        return True
    else:
        log_msg = f"Manual check FAILED: {instruction}"
        if notes:
            log_msg += f" | Notes: {notes}"
        if test_id and service:
            fail_log(log_msg, test_id, service, False)
        return False