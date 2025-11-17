from common_utils.android_image_comparision import *
from core.log_emitter import blocked_log, error_log
from time import sleep
from core.globals import manual_run

img_service = "Localization"

def Localization_001():
    try:
        blocked_log("Cannot check this service")
    except Exception as e:
        error_log(e, "001", img_service)

def Localization_002():
    try:
        blocked_log("Cannot check this service", "002" ,img_service)
    except Exception as e:
        error_log(e, "002", img_service)