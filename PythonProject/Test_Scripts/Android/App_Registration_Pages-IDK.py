from time import sleep
from common_utils.android_image_comparision import *
from common_utils.android_controller import *
from core.log_emitter import log_emitter

def log(msg):
    log_emitter.log_signal.emit(msg)

def fail_log(msg, num):
    log(f"{msg}")
    controller.take_fail_screenshot(f"App_Registration_Pages-IDK_{msg}_{num}.png")

def error_log(e, num):
    log(f"⚠️ - Unexpected error: {e}")
    controller.take_fail_screenshot(f"App_Registration_Pages-IDK_{e}_{num}.png")

# Need an throwaway emails that can be used
def App_Registration_Pages_001():
    try:
        pass
    except Exception as e:
        error_log(e, "001")

def App_Registration_Pages_002():
    try:
        pass
    except Exception as e:
        error_log(e, "002")

def App_Registration_Pages_003():
    try:
        pass
    except Exception as e:
        error_log(e, "003")

def App_Registration_Pages_004():
    try:
        pass
    except Exception as e:
        error_log(e, "004")

def App_Registration_Pages_005():
    try:
        pass
    except Exception as e:
        error_log(e, "005")

def App_Registration_Pages_006():
    try:
        pass
    except Exception as e:
        error_log(e, "006")

def App_Registration_Pages_007():
    try:
        pass
    except Exception as e:
        error_log(e, "007")

def App_Registration_Pages_008():
    try:
        pass
    except Exception as e:
        error_log(e, "008")

def App_Registration_Pages_009():
    try:
        log("✅ - Cannot complete style guide testcases (temporary)")
    except Exception as e:
        error_log(e, "009")
