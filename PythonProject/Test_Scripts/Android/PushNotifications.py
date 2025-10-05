from time import sleep
from common_utils.android_image_comparision import *
from common_utils.android_controller import *
from core.log_emitter import log_emitter

def log(msg):
    log_emitter.log_signal.emit(msg)

def fail_log(msg, num):
    log(f"{msg}")
    controller.take_fail_screenshot(f"Nickname_{msg}_{num}.png")

def error_log(e, num):
    log(f"⚠️ - Unexpected error: {e}")
    controller.take_fail_screenshot(f"Nickname_{e}_{num}.png")

def PushNotifications_001():
    try:
        pass
    except Exception as e:
        error_log(e, "001")

def PushNotifications_002():
    try:
        pass
    except Exception as e:
        error_log(e, "002")

def PushNotifications_003():
    try:
        pass
    except Exception as e:
        error_log(e, "003")

def PushNotifications_004():
    try:
        pass
    except Exception as e:
        error_log(e, "004")

def PushNotifications_005():
    try:
        pass
    except Exception as e:
        error_log(e, "005")

def PushNotifications_006():
    try:
        pass
    except Exception as e:
        error_log(e, "006")

def PushNotifications_007():
    try:
        pass
    except Exception as e:
        error_log(e, "007")

def PushNotifications_008():
    try:
        pass
    except Exception as e:
        error_log(e, "008")

def PushNotifications_009():
    try:
        pass
    except Exception as e:
        error_log(e, "009")

def PushNotifications_010():
    try:
        pass
    except Exception as e:
        error_log(e, "010")
