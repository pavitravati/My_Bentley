from time import sleep
from common_utils.android_image_comparision import *
from common_utils.android_controller import *
from core.log_emitter import log_emitter

def log(msg):
    log_emitter.log_signal.emit(msg)

def fail_log(msg, num):
    log(f"{msg}")
    controller.take_fail_screenshot(f"Nickname_{msg}_{num}.png")

def error_log(e, num):
    log(f"⚠️ - Unexpected error: {e}")
    controller.take_fail_screenshot(f"Nickname_{e}_{num}.png")

def SingleServiceActivation_001():
    try:
        pass
    except Exception as e:
        error_log(e, "001")

def SingleServiceActivation_002():
    try:
        pass
    except Exception as e:
        error_log(e, "002")

def SingleServiceActivation_003():
    try:
        pass
    except Exception as e:
        error_log(e, "003")

def SingleServiceActivation_004():
    try:
        pass
    except Exception as e:
        error_log(e, "004")

def SingleServiceActivation_005():
    try:
        pass
    except Exception as e:
        error_log(e, "005")

def SingleServiceActivation_006():
    try:
        pass
    except Exception as e:
        error_log(e, "006")

def SingleServiceActivation_007():
    try:
        pass
    except Exception as e:
        error_log(e, "007")

def SingleServiceActivation_008():
    try:
        pass
    except Exception as e:
        error_log(e, "008")

def SingleServiceActivation_009():
    try:
        pass
    except Exception as e:
        error_log(e, "009")

def SingleServiceActivation_010():
    try:
        pass
    except Exception as e:
        error_log(e, "010")
