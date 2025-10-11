from time import sleep
from common_utils.android_image_comparision import *
from common_utils.android_controller import *
from core.log_emitter import log_emitter

def log(msg):
    log_emitter.log_signal.emit(msg)

def fail_log(msg, num):
    log(f"{msg}")
    controller.take_fail_screenshot(f"PHEV-MyCabinComfort_{msg}_{num}.png")

def error_log(e, num):
    log(f"⚠️ - Unexpected error: {e}")
    controller.take_fail_screenshot(f"PHEV-MyCabinComfort_{e}_{num}.png")

def PHEV_MyCabinComfort_001():
    try:
        pass
    except Exception as e:
        error_log(e, "001")

def PHEV_MyCabinComfort_002():
    try:
        pass
    except Exception as e:
        error_log(e, "002")

def PHEV_MyCabinComfort_003():
    try:
        pass
    except Exception as e:
        error_log(e, "003")

def PHEV_MyCabinComfort_004():
    try:
        pass
    except Exception as e:
        error_log(e, "004")

def PHEV_MyCabinComfort_005():
    try:
        pass
    except Exception as e:
        error_log(e, "005")

def PHEV_MyCabinComfort_006():
    try:
        pass
    except Exception as e:
        error_log(e, "006")

def PHEV_MyCabinComfort_007():
    try:
        pass
    except Exception as e:
        error_log(e, "007")

def PHEV_MyCabinComfort_008():
    try:
        pass
    except Exception as e:
        error_log(e, "008")

def PHEV_MyCabinComfort_009():
    try:
        pass
    except Exception as e:
        error_log(e, "009")

def PHEV_MyCabinComfort_010():
    try:
        pass
    except Exception as e:
        error_log(e, "010")

def PHEV_MyCabinComfort_011():
    try:
        pass
    except Exception as e:
        error_log(e, "011")

def PHEV_MyCabinComfort_012():
    try:
        pass
    except Exception as e:
        error_log(e, "012")

def PHEV_MyCabinComfort_013():
    try:
        pass
    except Exception as e:
        error_log(e, "013")

def PHEV_MyCabinComfort_014():
    try:
        pass
    except Exception as e:
        error_log(e, "014")

def PHEV_MyCabinComfort_015():
    try:
        pass
    except Exception as e:
        error_log(e, "015")

def PHEV_MyCabinComfort_016():
    try:
        pass
    except Exception as e:
        error_log(e, "016")

def PHEV_MyCabinComfort_017():
    try:
        pass
    except Exception as e:
        error_log(e, "017")

def PHEV_MyCabinComfort_018():
    try:
        pass
    except Exception as e:
        error_log(e, "018")

def PHEV_MyCabinComfort_019():
    try:
        pass
    except Exception as e:
        error_log(e, "019")

def PHEV_MyCabinComfort_020():
    try:
        pass
    except Exception as e:
        error_log(e, "020")

def PHEV_MyCabinComfort_021():
    try:
        pass
    except Exception as e:
        error_log(e, "021")

def PHEV_MyCabinComfort_022():
    try:
        pass
    except Exception as e:
        error_log(e, "022")

def PHEV_MyCabinComfort_023():
    try:
        pass
    except Exception as e:
        error_log(e, "023")

def PHEV_MyCabinComfort_024():
    try:
        pass
    except Exception as e:
        error_log(e, "024")

def PHEV_MyCabinComfort_025():
    try:
        pass
    except Exception as e:
        error_log(e, "025")

def PHEV_MyCabinComfort_026():
    try:
        pass
    except Exception as e:
        error_log(e, "026")
