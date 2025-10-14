from time import sleep
from common_utils.android_image_comparision import *
from common_utils.android_controller import *
from core.log_emitter import log_emitter

def log(msg):
    log_emitter.log_signal.emit(msg)

def fail_log(msg, num):
    log(f"{msg}")
    controller.take_fail_screenshot(f"CarFinder-{msg}-{num}.png")

def error_log(e, num):
    log(f"⚠️ - Unexpected error: {e}")
    controller.take_fail_screenshot(f"CarFinder-{e}-{num}.png")

def CarFinder_001():
    try:
        pass
    except Exception as e:
        error_log(e, "001")

def CarFinder_002():
    try:
        pass
    except Exception as e:
        error_log(e, "002")

def CarFinder_003():
    try:
        pass
    except Exception as e:
        error_log(e, "003")

def CarFinder_004():
    try:
        pass
    except Exception as e:
        error_log(e, "004")

def CarFinder_005():
    try:
        pass
    except Exception as e:
        error_log(e, "005")

def CarFinder_006():
    try:
        pass
    except Exception as e:
        error_log(e, "006")

def CarFinder_007():
    try:
        pass
    except Exception as e:
        error_log(e, "007")

def CarFinder_008():
    try:
        pass
    except Exception as e:
        error_log(e, "008")

def CarFinder_009():
    try:
        pass
    except Exception as e:
        error_log(e, "009")