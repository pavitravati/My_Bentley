from time import sleep
from common_utils.android_image_comparision import *
from common_utils.android_controller import *
from core.log_emitter import log, fail_log, error_log, metric_log

img_service = "My Alerts"

def My_Alerts_001():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
    except Exception as e:
        error_log(e, "001", img_service)

def My_Alerts_002():
    try:
        pass
    except Exception as e:
        error_log(e, "002", img_service)

def My_Alerts_003():
    try:
        pass
    except Exception as e:
        error_log(e, "003", img_service)

def My_Alerts_004():
    try:
        pass
    except Exception as e:
        error_log(e, "004", img_service)

def My_Alerts_005():
    try:
        pass
    except Exception as e:
        error_log(e, "005", img_service)

def My_Alerts_006():
    try:
        pass
    except Exception as e:
        error_log(e, "006", img_service)

def My_Alerts_007():
    try:
        pass
    except Exception as e:
        error_log(e, "007", img_service)

def My_Alerts_008():
    try:
        pass
    except Exception as e:
        error_log(e, "008", img_service)

def My_Alerts_009():
    try:
        pass
    except Exception as e:
        error_log(e, "009", img_service)

def My_Alerts_010():
    try:
        pass
    except Exception as e:
        error_log(e, "010", img_service)

def My_Alerts_011():
    try:
        pass
    except Exception as e:
        error_log(e, "011", img_service)

def My_Alerts_012():
    try:
        pass
    except Exception as e:
        error_log(e, "012", img_service)

def My_Alerts_013():
    try:
        pass
    except Exception as e:
        error_log(e, "013", img_service)

def My_Alerts_014():
    try:
        pass
    except Exception as e:
        error_log(e, "014", img_service)

def My_Alerts_015():
    try:
        pass
    except Exception as e:
        error_log(e, "015", img_service)

def My_Alerts_016():
    try:
        pass
    except Exception as e:
        error_log(e, "016", img_service)

def My_Alerts_017():
    try:
        log("✅ - temp, can't check style guide")
    except Exception as e:
        error_log(e, "017", img_service)