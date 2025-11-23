from PySide6.QtWidgets import (
    QApplication, QMainWindow, QToolBar
)
from PySide6.QtGui import QAction, QActionGroup, QIcon
# from excel import services, service_details
from service_details import service_details, services
from test_case_page import TestCaseTablePage
from core import globals
from home_page import HomePage
import sys
import os, glob
import core.globals as globals

def cleanup_images():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    image_dir = os.path.join(base_dir, "fail_images")

    for file in glob.glob(os.path.join(image_dir, "*.png")):
        os.remove(file)

    base_dir = os.path.dirname(os.path.abspath(__file__))
    image_dir = os.path.join(base_dir, "manual_check_screenshots")

    for file in glob.glob(os.path.join(image_dir, "*.png")):
        os.remove(file)

# Class of the Main window where the table is placed
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Test Case Viewer")
        self.setStyleSheet("background-color: white;")

        # Adds toolbar to the top which is how you would move through different services
        toolbar = QToolBar("Services")
        toolbar.setMovable(False)
        self.addToolBar(toolbar)
        toolbar.setStyleSheet("background-color: #394d45; color: white;")

        action_group = QActionGroup(self)
        action_group.setExclusive(True)

        # Adds each service to the toolbar
        for service in services:
            action = QAction(service, self)
            action.setCheckable(True)
            action.triggered.connect(lambda checked, svc=service: self.toolbar_button_clicked(svc))
            toolbar.addAction(action)
            action_group.addAction(action)

        self.setCentralWidget(HomePage(self))

    def toolbar_button_clicked(self, service):
        fields = [globals.current_name, globals.current_email, globals.current_password, globals.current_pin, globals.vehicle_type, globals.phone_type, globals.country]
        stored = service_details[service]['fields'].values()

        if not any(not f and s for f, s in zip(fields, stored)):
            self.service = service
            self.setCentralWidget(TestCaseTablePage(self, service, auto_run=False))

    def show_homepage(self, auto_cancel=False):
        if auto_cancel:
            globals.log_history.popitem()
        self.setCentralWidget(HomePage(self))

    def show_test_cases(self, service):
        self.setCentralWidget(TestCaseTablePage(self, service, auto_run=False))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    scrollbar_style = """
    QScrollBar:vertical {
        border: none;
        background: #2b2b2b;
        width: 11px;
        margin: 0px 0px 0px 0px;
    }
    QScrollBar::handle:vertical {
        background: #53665e;
        min-height: 20px;
        border-radius: 5px;
    }
    QScrollBar::handle:vertical:hover {
        background: #46534e;
    }
    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
        height: 0px;
    }
    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
        background: none;
    }

    QScrollBar:horizontal {
        border: none;
        background: #blue;
        height: 11px;
        margin: 0px 0px 0px 0px;
    }
    QScrollBar::handle:horizontal {
        background: #53665e;
        min-width: 20px;
        border-radius: 5px;
    }
    QScrollBar::handle:horizontal:hover {
        background: #46534e;
    }
    QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
        width: 0px;
    }
    QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
        background: none;
    """

    app.setStyleSheet(scrollbar_style)
    app.setStyle("Fusion")
    icon_path = os.path.join(os.path.dirname(__file__), "images", "bentleyicon.png")
    app.setWindowIcon(QIcon(icon_path))
    window = MainWindow()
    window.showMaximized()
    app.aboutToQuit.connect(cleanup_images)
    sys.exit(app.exec())