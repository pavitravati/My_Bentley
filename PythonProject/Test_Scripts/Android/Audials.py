from common_utils.android_image_comparision import *
from core.log_emitter import log, fail_log, error_log, blocked_log, runtime_log
from core.app_functions import remote_swipe, app_login_setup, service_reset
from core.globals import vehicle_type, country
from core.screenrecord import ScreenRecorder
from core import globals

img_service = "Audials"
recorder = ScreenRecorder(device_serial=controller.d.serial)

def Audials_001():
    recorder.start(f"{img_service}-001")
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (NAR/EUR)")
        else:
            if app_login_setup():

                controller.click_by_image("Icons/remote_icon.png")
                if remote_swipe("AUDIALS"):
                    if controller.click_text("AUDIALS"):
                        log("Audials section clicked")

                    controller.click_text("OK")
                    if controller.wait_for_text_that_contains("audials.com"):
                        log("Redirected to Audials.com")
                    else:
                        fail_log("Failed to redirect to Audials.com", "001", img_service)

                    controller.launch_app("uk.co.bentley.mybentley")
                    if vehicle_type == "phev":
                        controller.swipe_down(0.19)
                        controller.swipe_down(0.19)
                    elif vehicle_type == "ice":
                        controller.swipe_down(0.1)
                    controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "001", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Audials_002():
    recorder.start(f"{img_service}-002")
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (NAR/EUR)")
        else:
            blocked_log("Test blocked - Can't check style guide")
    except Exception as e:
        error_log(e, "002", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False