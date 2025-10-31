from common_utils.android_image_comparision import *
from core.log_emitter import log, fail_log, error_log, metric_log
from time import sleep

img_service = "Audials"

def Audials_001():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")

        for _ in range(3):
            controller.swipe_up()

        if controller.click_text("AUDIALS"):
            log("Audials section clicked")
        else:
            fail_log("Audials section not clicked", "001", img_service)

        controller.click_text("OK")
        if controller.is_text_present("audials.com"):
            log("Redirected to Audials.com")
        else:
            fail_log("Failed to redirect to Audials.com", "001", img_service)

        controller.press_home()
        controller.launch_app("uk.co.bentley.mybentley")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "001", img_service)

# Font checking test
def Audials_002():
    try:
        log("Cannot check style")
    except Exception as e:
        error_log(e, "002", img_service)