from time import sleep
from common_utils.android_image_comparision import *
from core.log_emitter import log, fail_log, metric_log, error_log

img_service = "Data Services"

# Make sure this works using better wifi as it struggles on bad wifi
def Data_Services_001():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        for _ in range(2):
            controller.swipe_up()
        controller.click_text("DATA SERVICES")
        if controller.click_text("VISIT STORE"):
            log("Bentley Support Centre web launched")
            controller.wait_for_text_and_click("AGREE TO ALL")
        else:
            fail_log("Bentley Support Centre web not launched", "001", img_service)
        sleep(5)

        controller.swipe_up()
        controller.click_text("BUY DATA")
        sleep(5)
        if controller.is_text_present("Connect Now"):
            log("Data Service Provider web launched")
        else:
            fail_log("Data Service Provider web not launched", "001", img_service)

        controller.press_home()
        controller.launch_app("uk.co.bentley.mybentley")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "001", img_service)

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