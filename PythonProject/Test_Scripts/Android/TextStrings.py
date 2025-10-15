from common_utils.android_image_comparision import *
from core.log_emitter import log_emitter

def log(msg):
    log_emitter.log_signal.emit(msg)

def fail_log(msg, num):
    log(f"{msg}")
    controller.take_fail_screenshot(f"TextStrings-{msg}-{num}.png")

def error_log(e, num):
    log(f"⚠️ - Unexpected error: {e}")
    controller.take_fail_screenshot(f"TextStrings-{e}-{num}.png")

def TextStrings_001():
    try:
        pass
    except Exception as e:
        error_log(e, "001")

def TextStrings_002():
    try:
        pass
    except Exception as e:
        error_log(e, "002")