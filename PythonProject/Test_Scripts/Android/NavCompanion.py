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

def NavCompanion_001():
    try:
        pass
    except Exception as e:
        error_log(e, "001")

def NavCompanion_002():
    try:
        pass
    except Exception as e:
        error_log(e, "002")

def NavCompanion_003():
    try:
        pass
    except Exception as e:
        error_log(e, "003")

def NavCompanion_004():
    try:
        pass
    except Exception as e:
        error_log(e, "004")

def NavCompanion_005():
    try:
        pass
    except Exception as e:
        error_log(e, "005")

def NavCompanion_006():
    try:
        pass
    except Exception as e:
        error_log(e, "006")

def NavCompanion_007():
    try:
        pass
    except Exception as e:
        error_log(e, "007")

def NavCompanion_008():
    try:
        pass
    except Exception as e:
        error_log(e, "008")

def NavCompanion_009():
    try:
        pass
    except Exception as e:
        error_log(e, "009")

def NavCompanion_010():
    try:
        pass
    except Exception as e:
        error_log(e, "010")

def NavCompanion_011():
    try:
        pass
    except Exception as e:
        error_log(e, "011")

def NavCompanion_012():
    try:
        pass
    except Exception as e:
        error_log(e, "012")

def NavCompanion_013():
    try:
        pass
    except Exception as e:
        error_log(e, "013")

def NavCompanion_014():
    try:
        pass
    except Exception as e:
        error_log(e, "014")

def NavCompanion_015():
    try:
        pass
    except Exception as e:
        error_log(e, "015")
