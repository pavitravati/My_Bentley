from common_utils.android_image_comparision import *
from core.log_emitter import log, fail_log, error_log, metric_log
from time import sleep

img_service = "Localization"

def Localization_001():
    try:
        log("Cannot check this service")
    except Exception as e:
        error_log(e, "001", img_service)

def Localization_002():
    try:
        log("Cannot check this service")
    except Exception as e:
        error_log(e, "002", img_service)