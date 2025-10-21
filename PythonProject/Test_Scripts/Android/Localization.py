from common_utils.android_image_comparision import *
from core.log_emitter import log_emitter
from time import sleep

def log(msg):
    log_emitter.log_signal.emit(msg)

def fail_log(msg, num):
    log(f"{msg}")
    controller.take_fail_screenshot(f"Localization-{msg}-{num}.png")

def error_log(e, num):
    log(f"⚠️ - Unexpected error: {e}")
    controller.take_fail_screenshot(f"Localization-{e}-{num}.png")

def Localization_001():
    try:
        log("✅ - test")
    except Exception as e:
        error_log(e, "001")

def Localization_002():
    try:
        fail_log("❌ - dsafad", "002")
    except Exception as e:
        error_log(e, "002")