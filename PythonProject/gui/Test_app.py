from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
)

services = ['DemoMode', 'Customer_Enrollment', 'App_registration_Pages-IDK', 'Add_VIN', 'MyBentleyLogin',
            'Nickname', 'License(App)', 'VehicleStatusReport', 'RemoteLockUnlock', 'SingleServiceActivation',
            'PHEV-MyCarStatistics', 'PHEV-MyCabinComfort', 'PHEV_MyBatteryCharge', 'RoadsideAssistanceCall(App)',
            'DataServices', 'TheftAlarm', 'Audials(App)', 'CarFinder', 'NavComparison', 'Notifications',
            'Profiles', 'TextStrings', 'PrivacyMode(App)', 'RemoteParkAssist', 'VehicleTrackingSystem']

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        self.setFixedSize(QSize(1800, 950))

        toolbar = QToolBar("Services")
        self.addToolBar(toolbar)

        for service in services:
            button_action = QAction(service, self)
            button_action.setStatusTip(f"{service} button")
            button_action.triggered.connect(self.toolbar_button_clicked)
            button_action.setCheckable(True)
            toolbar.addAction(button_action)

        self.setStatusBar(QStatusBar(self))

    def toolbar_button_clicked(self, s):
        print("click", s)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()