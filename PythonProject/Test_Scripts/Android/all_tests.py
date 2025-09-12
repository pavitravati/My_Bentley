from PythonProject.Test_Scripts.Android.Profile import *
from PythonProject.Test_Scripts.Android.Demo_Mode import *
from PythonProject.Test_Scripts.Android.Remote_Lock_Unlock import *

controller = DeviceController()
d = u2.connect()

def Preconditions():
    controller.wake_up_unlock_screen()
    controller.press_home()