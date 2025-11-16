from time import sleep
from common_utils.android_image_comparision import *
from common_utils.android_controller import *
from core.globals import country
from core.log_emitter import log, fail_log, metric_log, error_log, blocked_log

img_service = "Stolen Vehicle Locator"

def Stolen_Vehicle_Locator_001():
    try:
        if country == "eur":
            blocked_log("Test blocked - Region locked (NAR/CHN)")
        else:
            pass
    except Exception as e:
        error_log(e, "001", img_service)

def Stolen_Vehicle_Locator_002():
    try:
        if country == "eur":
            blocked_log("Test blocked - Region locked (NAR/CHN)")
        else:
            pass
    except Exception as e:
        error_log(e, "002", img_service)

def Stolen_Vehicle_Locator_003():
    try:
        if country == "eur":
            blocked_log("Test blocked - Region locked (NAR/CHN)")
        else:
            blocked_log("Test blocked - Can't check style guide")
    except Exception as e:
        error_log(e, "003", img_service)