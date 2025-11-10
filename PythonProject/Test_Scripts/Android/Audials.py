from common_utils.android_image_comparision import *
from core.log_emitter import log, fail_log, error_log, metric_log
from time import sleep

img_service = "Audials"

def Audials_001():
    try:
        # controller.click_by_image("Icons/windows_icon.png")
        # controller.swipe_up(0.2)
        # controller.swipe_up(0.2)
        # sleep(0.2)
        # if controller.click_text("AUDIALS"):
        #     log("Audials section clicked")
        # else:
        #     controller.swipe_up(0.2)
        #     sleep(0.2)
        #     if controller.click_text("AUDIALS"):
        #         log("Audials section clicked")
        #     else:
        #         fail_log("Audials section not clicked", "001", img_service)
        #
        # controller.click_text("OK")
        # if controller.wait_for_text_that_contains("audials.com"):
        #     log("Redirected to Audials.com")
        # else:
        #     fail_log("Failed to redirect to Audials.com", "001", img_service)
        #
        # controller.launch_app("uk.co.bentley.mybentley")
        # controller.swipe_down(0.19)
        # controller.swipe_down(0.19)
        # controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        log("temp")
    except Exception as e:
        error_log(e, "001", img_service)

def Audials_002():
    try:
        log("Cannot check style")
    except Exception as e:
        error_log(e, "002", img_service)