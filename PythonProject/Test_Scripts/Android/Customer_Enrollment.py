from time import sleep
from common_utils.android_image_comparision import *
from common_utils.android_controller import *
from core.log_emitter import log_emitter

def log(msg):
    log_emitter.log_signal.emit(msg)

def fail_log(msg, num):
    log(f"{msg}")
    controller.take_fail_screenshot(f"Customer_Enrollment-{msg}-{num}.png")

def error_log(e, num):
    log(f"⚠️ - Unexpected error: {e}")
    controller.take_fail_screenshot(f"Customer_Enrollment-{e}-{num}.png")

# Obsolete?
def Customer_Enrollment_001():
    try:
        pass
    except Exception as e:
        error_log(e, "001")

# Obsolete?
def Customer_Enrollment_002():
    try:
        pass
    except Exception as e:
        error_log(e, "002")

def Customer_Enrollment_003():
    try:
        pass
    except Exception as e:
        error_log(e, "003")

def Customer_Enrollment_004():
    try:
        pass
    except Exception as e:
        error_log(e, "004")

def Customer_Enrollment_005():
    try:
        pass
    except Exception as e:
        error_log(e, "005")

def Customer_Enrollment_006():
    try:
        pass
    except Exception as e:
        error_log(e, "006")

def Customer_Enrollment_007():
    try:
        pass
    except Exception as e:
        error_log(e, "007")

def Customer_Enrollment_008():
    try:
        pass
    except Exception as e:
        error_log(e, "008")

def Customer_Enrollment_009():
    try:
        pass
    except Exception as e:
        error_log(e, "009")

def Customer_Enrollment_010():
    try:
        pass
    except Exception as e:
        error_log(e, "010")

def Customer_Enrollment_011():
    try:
        pass
    except Exception as e:
        error_log(e, "011")

def Customer_Enrollment_012():
    try:
        pass
    except Exception as e:
        error_log(e, "012")

def Customer_Enrollment_013():
    try:
        pass
    except Exception as e:
        error_log(e, "013")

def Customer_Enrollment_014():
    try:
        pass
    except Exception as e:
        error_log(e, "014")

def Customer_Enrollment_015():
    try:
        pass
    except Exception as e:
        error_log(e, "015")

def Customer_Enrollment_016():
    try:
        pass
    except Exception as e:
        error_log(e, "016")

def Customer_Enrollment_017():
    try:
        pass
    except Exception as e:
        error_log(e, "017")

def Customer_Enrollment_018():
    try:
        pass
    except Exception as e:
        error_log(e, "018")

def Customer_Enrollment_019():
    try:
        pass
    except Exception as e:
        error_log(e, "019")

def Customer_Enrollment_020():
    try:
        pass
    except Exception as e:
        error_log(e, "020")

def Customer_Enrollment_021():
    try:
        pass
    except Exception as e:
        error_log(e, "021")

def Customer_Enrollment_022():
    try:
        pass
    except Exception as e:
        error_log(e, "022")

def Customer_Enrollment_023():
    try:
        pass
    except Exception as e:
        error_log(e, "023")
