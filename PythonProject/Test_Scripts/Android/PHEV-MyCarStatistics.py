from common_utils.android_image_comparision import *
from core.log_emitter import log_emitter

def log(msg):
    log_emitter.log_signal.emit(msg)

def fail_log(msg, num):
    log(f"{msg}")
    controller.take_fail_screenshot(f"PHEV-MyCarStatistics-{msg}-{num}.png")

def error_log(e, num):
    log(f"⚠️ - Unexpected error: {e}")
    controller.take_fail_screenshot(f"PHEV-MyCarStatistics-{e}-{num}.png")

def PHEV_MyCarStatistics_001():
    try:
        pass
    except Exception as e:
        error_log(e, "001")

def PHEV_MyCarStatistics_002():
    try:
        pass
    except Exception as e:
        error_log(e, "002")

def PHEV_MyCarStatistics_003():
    try:
        pass
    except Exception as e:
        error_log(e, "003")

def PHEV_MyCarStatistics_004():
    try:
        pass
    except Exception as e:
        error_log(e, "004")

def PHEV_MyCarStatistics_005():
    try:
        pass
    except Exception as e:
        error_log(e, "005")

def PHEV_MyCarStatistics_006():
    try:
        pass
    except Exception as e:
        error_log(e, "006")

def PHEV_MyCarStatistics_007():
    try:
        pass
    except Exception as e:
        error_log(e, "007")

def PHEV_MyCarStatistics_008():
    try:
        pass
    except Exception as e:
        error_log(e, "008")

def PHEV_MyCarStatistics_009():
    try:
        pass
    except Exception as e:
        error_log(e, "009")

def PHEV_MyCarStatistics_010():
    try:
        pass
    except Exception as e:
        error_log(e, "010")

def PHEV_MyCarStatistics_011():
    try:
        pass
    except Exception as e:
        error_log(e, "011")

def PHEV_MyCarStatistics_012():
    try:
        pass
    except Exception as e:
        error_log(e, "012")
