from common_utils.android_image_comparision import *
from core.log_emitter import log_emitter

def log(msg):
    log_emitter.log_signal.emit(msg)

def fail_log(msg, num):
    log(f"{msg}")
    controller.take_fail_screenshot(f"Add_VIN-{msg}-{num}.png")

def error_log(e, num):
    log(f"⚠️ - Unexpected error: {e}")
    controller.take_fail_screenshot(f"Add_VIN-{e}-{num}.png")

def Add_VIN_001():
    try:
        pass
    except Exception as e:
        error_log(e, "001")

def Add_VIN_002():
    try:
        pass
    except Exception as e:
        error_log(e, "002")

def Add_VIN_003():
    try:
        pass
    except Exception as e:
        error_log(e, "003")

def Add_VIN_004():
    try:
        pass
    except Exception as e:
        error_log(e, "004")

def Add_VIN_005():
    try:
        pass
    except Exception as e:
        error_log(e, "005")

def Add_VIN_006():
    try:
        pass
    except Exception as e:
        error_log(e, "006")

def Add_VIN_007():
    try:
        pass
    except Exception as e:
        error_log(e, "007")

def Add_VIN_008():
    try:
        pass
    except Exception as e:
        error_log(e, "008")

def Add_VIN_009():
    try:
        pass
    except Exception as e:
        error_log(e, "009")

def Add_VIN_010():
    try:
        pass
    except Exception as e:
        error_log(e, "010")

def Add_VIN_011():
    try:
        pass
    except Exception as e:
        error_log(e, "011")

def Add_VIN_012():
    try:
        pass
    except Exception as e:
        error_log(e, "012")

def Add_VIN_013():
    try:
        pass
    except Exception as e:
        error_log(e, "013")

def Add_VIN_014():
    try:
        pass
    except Exception as e:
        error_log(e, "014")

def Add_VIN_015():
    try:
        pass
    except Exception as e:
        error_log(e, "015")

def Add_VIN_016():
    try:
        pass
    except Exception as e:
        error_log(e, "016")

def Add_VIN_017():
    try:
        pass
    except Exception as e:
        error_log(e, "017")

def Add_VIN_018():
    try:
        pass
    except Exception as e:
        error_log(e, "018")