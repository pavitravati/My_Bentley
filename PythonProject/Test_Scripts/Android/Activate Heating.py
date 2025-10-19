from time import sleep
from common_utils.android_image_comparision import *
from common_utils.android_controller import *
from core.log_emitter import log_emitter

# Made a copy of the demo mode testcases to try and get them connected to the ui
def log(msg):
    log_emitter.log_signal.emit(msg)

def fail_log(msg, num):
    log(f"{msg}")
    controller.take_fail_screenshot(f"Activate Heating-{msg}-{num}.png")

def error_log(e, num):
    log(f"⚠️ - Unexpected error: {e}")
    controller.take_fail_screenshot(f"Activate Heating-{e}-{num}.png")

# Need different car
def Activate_Heating_001():
    try:
        pass
    except Exception as e:
        error_log(e, "001")

def Activate_Heating_002():
    try:
        pass
    except Exception as e:
        error_log(e, "002")

def Activate_Heating_003():
    try:
        pass
    except Exception as e:
        error_log(e, "003")

def Activate_Heating_004():
    try:
        pass
    except Exception as e:
        error_log(e, "004")

def Activate_Heating_005():
    try:
        pass
    except Exception as e:
        error_log(e, "005")

def Activate_Heating_006():
    try:
        pass
    except Exception as e:
        error_log(e, "006")

def Activate_Heating_007():
    try:
        pass
    except Exception as e:
        error_log(e, "007")

def Activate_Heating_008():
    try:
        log("✅ - temp, can't check style guide")
    except Exception as e:
        error_log(e, "008")