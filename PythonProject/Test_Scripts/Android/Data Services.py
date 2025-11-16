from time import sleep
from common_utils.android_image_comparision import *
from core.log_emitter import log, fail_log, error_log, blocked_log
from core.globals import current_VIN, vehicle_type, country
from core.app_functions import remote_swipe

img_service = "Data Services"

def Data_Services_001():
    try:
        if country == "EUR":
            controller.click_by_image("Icons/windows_icon.png")
            if remote_swipe("DATA SERVICES"):
                controller.click_text("DATA SERVICES")
                if controller.click_text("VISIT STORE"):
                    log("Bentley Support Centre web launched")
                    controller.wait_for_text_and_click("AGREE TO ALL")
                else:
                    fail_log("Bentley Support Centre web not launched", "001", img_service)

                controller.swipe_up(0.7)
                controller.click_text("BUY DATA")
                sleep(1)
                if controller.click_text("Connect Now"):
                    log("Data Service Provider web launched")
                else:
                    fail_log("Data Service Provider web not launched", "001", img_service)

                controller.enter_text(current_VIN)
                controller.click_text("Verify")
                # Finish when the VIN is recognised

                if vehicle_type == "phev":
                    controller.swipe_down(0.19)
                    controller.swipe_down(0.19)
                elif vehicle_type == "ice":
                    controller.swipe_down(0.1)
            controller.launch_app("uk.co.bentley.mybentley")
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "001", img_service)

# Need NAR car
def Data_Services_002():
    try:
        if country == "nar":
            pass
        else:
            blocked_log("Test blocked - Region locked (NAR)")
    except Exception as e:
        error_log(e, "002", img_service)

# Need china car
def Data_Services_003():
    try:
        if country == "chn":
            pass
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "003", img_service)

def Data_Services_004():
    try:
        blocked_log("Test blocked - Can't check style guide")
    except Exception as e:
        error_log(e, "004", img_service)