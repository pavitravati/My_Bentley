from common_utils.android_image_comparision import *
from core.globals import vehicle_type, current_email, current_password
from core.log_emitter import log, fail_log, error_log, blocked_log
from core.app_functions import remote_swipe
from core.app_functions import app_login

img_service = "Roadside Assistance"

def Roadside_Assistance_001():
    try:
        if controller.is_text_present("LOGIN OR REGISTER") and current_email and current_password:
            if current_email and current_password:
                app_login()
            else:
                blocked_log("Test blocked - Account logged out and credentials not provided")

        controller.click_by_image("Icons/remote_icon.png")
        if remote_swipe("ROADSIDE ASSISTANCE"):
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
            if vehicle_type == "phev":
                controller.swipe_down(0.6)
                controller.swipe_down(0.6)
            elif vehicle_type == "ice":
                controller.swipe_down()
            controller.click_by_image("Icons/back_icon.png")

    except Exception as e:
        error_log(e, "001", img_service)

def Roadside_Assistance_002():
    try:
        blocked_log("Test blocked - Cannot be automated")
    except Exception as e:
        error_log(e, "002", img_service)

def Roadside_Assistance_003():
    try:
        blocked_log("Test blocked - Can't check style guide")
    except Exception as e:
        error_log(e, "003", img_service)