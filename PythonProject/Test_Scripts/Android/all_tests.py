from Test_Scripts.Android.Profile import *
from Test_Scripts.Android.DemoMode import *
from Test_Scripts.Android.Remote_Lock_Unlock import *

controller = DeviceController()
d = u2.connect()

def Preconditions():
    controller.wake_up_unlock_screen()
    controller.press_home()