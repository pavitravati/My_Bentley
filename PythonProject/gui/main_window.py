from PySide6.QtWidgets import (
    QApplication, QMainWindow, QToolBar
)
from PySide6.QtGui import QAction
from excel import services
from test_case_page import TestCaseTablePage
import sys

# Class of the Main window where the table is placed
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Test Case Viewer")
        self.setStyleSheet("background-color: white;")

        # Set the test case table as the central widget
        self.setCentralWidget(TestCaseTablePage())

        # Adds toolbar to the top which is how you would move through different services
        toolbar = QToolBar("Services")
        toolbar.setMovable(False)
        self.addToolBar(toolbar)
        toolbar.setStyleSheet("background-color: #394d45; color: white;")

        # Adds each service to the toolbar
        for service in services:
            button_action = QAction(service, self)
            button_action.setStatusTip(f"{service} button")
            button_action.triggered.connect(self.toolbar_button_clicked)
            button_action.setCheckable(True)
            toolbar.addAction(button_action)

    # Currently indicates if toolbar is interacted with
    def toolbar_button_clicked(self, s):
        print("click", s)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec())