from common_utils.android_image_comparision import *
from core.log_emitter import log_emitter

def log(msg):
    log_emitter.log_signal.emit(msg)

def fail_log(msg, num):
    log(f"{msg}")
    controller.take_fail_screenshot(f"Privacy Mode-{msg}-{num}.png")

def error_log(e, num):
    log(f"⚠️ - Unexpected error: {e}")
    controller.take_fail_screenshot(f"Privacy Mode-{e}-{num}.png")

# Feels redundant
def Privacy_Mode_001():
    try:
        pass
    except Exception as e:
        error_log(e, "001")

def Privacy_Mode_002():
    try:
        pass
    except Exception as e:
        error_log(e, "002")

def Privacy_Mode_003():
    try:
        pass
    except Exception as e:
        error_log(e, "003")

def Privacy_Mode_004():
    try:
        pass
    except Exception as e:
        error_log(e, "004")

def Privacy_Mode_005():
    try:
        pass
    except Exception as e:
        error_log(e, "005")

def Privacy_Mode_006():
    try:
        log("✅ - temp can't check style guide")
    except Exception as e:
        error_log(e, "006")
