from common_utils.android_image_comparision import *
from core.globals import vehicle_type, current_email, current_password, country
from core.log_emitter import log, fail_log, error_log, blocked_log, runtime_log
from core.app_functions import remote_swipe, service_reset, app_login_setup, app_refresh
from core.app_functions import app_login
from core.screenrecord import ScreenRecorder
from core import globals
from gui.manual_check import manual_check

img_service = "Roadside Assistance"
recorder = ScreenRecorder(device_serial=controller.d.serial)

def Roadside_Assistance_001():
    recorder.start(f"{img_service}-001")
    try:
        if app_login_setup():
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

                    if country == "chn":
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
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Roadside_Assistance_002():
    recorder.start(f"{img_service}-002")
    try:
        blocked_log("Test blocked - Cannot be automated")
        # controller.click_by_image("Icons/remote_icon.png")
        # if remote_swipe("ROADSIDE ASSISTANCE"):
        #     if controller.click_text("ROADSIDE ASSISTANCE"):
        #         log("Roadside assistance section clicked")
        #         controller.click_text("CALL NOW")
        #         manual_check(
        #             instruction="""Verify Breakdown Call initiation Form My Bentley App\nTry to establish call to the region specific contact number
        #                             \nTwo way communication between Agent and Customer should be successful and call should end without issues""",
        #             test_id="002",
        #             service=img_service,
        #             take_screenshot=False
        #         )
        #         service_reset()
    except Exception as e:
        error_log(e, "002", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Roadside_Assistance_003():
    recorder.start(f"{img_service}-003")
    try:
        blocked_log("Test blocked - Can't check style guide")
    except Exception as e:
        error_log(e, "003", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False