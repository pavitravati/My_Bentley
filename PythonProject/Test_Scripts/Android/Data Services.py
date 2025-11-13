from time import sleep
from common_utils.android_image_comparision import *
from core.log_emitter import log, fail_log, error_log
from core.globals import current_VIN

img_service = "Data Services"

def Data_Services_001():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        for _ in range(2):
            controller.swipe_up()
        sleep(0.5)
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

        controller.launch_app("uk.co.bentley.mybentley")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "001", img_service)
# Data_Services_001

# Need NAR car
def Data_Services_002():
    try:
        pass
    except Exception as e:
        error_log(e, "002", img_service)

# Need china car
def Data_Services_003():
    try:
        pass
    except Exception as e:
        error_log(e, "003", img_service)

def Data_Services_004():
    try:
        log("Cannot check style guide")
    except Exception as e:
        error_log(e, "004", img_service)