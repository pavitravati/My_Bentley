from common_utils.android_image_comparision import *
from core.log_emitter import log_emitter

def log(msg):
    log_emitter.log_signal.emit(msg)

def fail_log(msg, num):
    log(f"{msg}")
    controller.take_fail_screenshot(f"Roadside Assistance-{msg}-{num}.png")

def error_log(e, num):
    log(f"⚠️ - Unexpected error: {e}")
    controller.take_fail_screenshot(f"Roadside Assistance-{e}-{num}.png")

def Roadside_Assistance_001():
    try:
        pass
    except Exception as e:
        error_log(e, "001")

def Roadside_Assistance_002():
    try:
        pass
    except Exception as e:
        error_log(e, "002")

def Roadside_Assistance_003():
    try:
        pass
    except Exception as e:
        error_log(e, "003")

def Roadside_Assistance_004():
    try:
        pass
    except Exception as e:
        error_log(e, "004")