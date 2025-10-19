from common_utils.android_image_comparision import *
from core.log_emitter import log_emitter

def log(msg):
    log_emitter.log_signal.emit(msg)

def fail_log(msg, num):
    log(f"{msg}")
    controller.take_fail_screenshot(f"My Car Statistics-{msg}-{num}.png")

def error_log(e, num):
    log(f"⚠️ - Unexpected error: {e}")
    controller.take_fail_screenshot(f"My Car Statistics-{e}-{num}.png")

def My_Car_Statistics_001():
    try:
        pass
    except Exception as e:
        error_log(e, "001")

def My_Car_Statistics_002():
    try:
        pass
    except Exception as e:
        error_log(e, "002")

def My_Car_Statistics_003():
    try:
        pass
    except Exception as e:
        error_log(e, "003")

def My_Car_Statistics_004():
    try:
        pass
    except Exception as e:
        error_log(e, "004")

def My_Car_Statistics_005():
    try:
        pass
    except Exception as e:
        error_log(e, "005")

def My_Car_Statistics_006():
    try:
        pass
    except Exception as e:
        error_log(e, "006")

def My_Car_Statistics_007():
    try:
        pass
    except Exception as e:
        error_log(e, "007")

def My_Car_Statistics_008():
    try:
        pass
    except Exception as e:
        error_log(e, "008")

def My_Car_Statistics_009():
    try:
        pass
    except Exception as e:
        error_log(e, "009")

def My_Car_Statistics_010():
    try:
        pass
    except Exception as e:
        error_log(e, "010")

def My_Car_Statistics_011():
    try:
        pass
    except Exception as e:
        error_log(e, "011")

def My_Car_Statistics_012():
    try:
        pass
    except Exception as e:
        error_log(e, "012")

def My_Car_Statistics_013():
    try:
        pass
    except Exception as e:
        error_log(e, "013")
