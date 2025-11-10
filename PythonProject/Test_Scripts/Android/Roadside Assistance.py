from common_utils.android_image_comparision import *
from core.log_emitter import log, fail_log, metric_log, error_log
from time import sleep

img_service = "Roadside Assistance"

def Roadside_Assistance_001():
    try:
        controller.click_by_image("Icons/windows_icon.png")
        controller.swipe_up(0.1)
        sleep(1)
        if controller.click_text("ROADSIDE ASSISTANCE"):
            log("Roadside assistance section clicked")
            controller.click_text("CALL NOW")
            if controller.is_text_present("+44 800 316 1333"):
                log("UK assistance number validated")
            else:
                fail_log("UK assistance number not validated", "001", img_service)

            if controller.is_text_present("+49 221 802471854"):
                log("EU assistance number validated")
            else:
                fail_log("EU assistance number not validated", "001", img_service)

            if controller.is_text_present("+1 800 455 5045"):
                log("NA assistance number validated")
            else:
                fail_log("NA assistance number not validated", "001", img_service)

            # check that is how its actually displayed
            if controller.is_text_present("+864000032877"):
                log("China assistance number validated")
            else:
                fail_log("China assistance number not validated", "001", img_service)

            controller.click_text("Cancel")
            controller.click_by_image("Icons/back_icon.png")
        else:
            fail_log("Roadside assistance section not found", "001", img_service)
        controller.swipe_down(0.6)
        controller.swipe_down(0.6)
        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "001", img_service)

def Roadside_Assistance_002():
    try:
        log("Can't be automated")
    except Exception as e:
        error_log(e, "002", img_service)

def Roadside_Assistance_003():
    try:
        log("Can't be automated")
    except Exception as e:
        error_log(e, "003", img_service)

def Roadside_Assistance_004():
    try:
        log("Can't check style guide")
    except Exception as e:
        error_log(e, "004", img_service)