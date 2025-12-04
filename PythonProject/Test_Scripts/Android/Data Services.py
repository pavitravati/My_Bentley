from common_utils.android_image_comparision import *
from core.log_emitter import log, fail_log, error_log, blocked_log, runtime_log
from core.globals import current_vin, vehicle_type, country
from core import globals
from core.app_functions import remote_swipe, app_login_setup, service_reset
from core.screenrecord import ScreenRecorder

img_service = "Data Services"
recorder = ScreenRecorder(device_serial=controller.d.serial)

def Data_Services_001():
    recorder.start(f"{img_service}-001")
    try:
        if country == "EUR":
            if app_login_setup():
                controller.click_by_image("Icons/remote_icon.png")
                if remote_swipe("DATA SERVICES"):
                    controller.click_text("DATA SERVICES")
                    if controller.click_text("VISIT STORE"):
                        log("Bentley Support Centre web launched")
                        controller.wait_for_text_and_click("AGREE TO ALL")
                    else:
                        fail_log("Bentley Support Centre web not launched", "001", img_service)

                    controller.swipe_up(0.7)
                    controller.click_text("BUY DATA")
                    if controller.wait_for_text_and_click("Connect Now"):
                        log("Data Service Provider web launched")
                    else:
                        fail_log("Data Service Provider web not launched", "001", img_service)

                    controller.enter_text(current_vin)
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
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Data_Services_002():
    recorder.start(f"{img_service}-002")
    try:
        if country == "nar":
            blocked_log("Test blocked - Not written (NAR)")
        else:
            blocked_log("Test blocked - Region locked (NAR)")
    except Exception as e:
        error_log(e, "002", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Data_Services_003():
    recorder.start(f"{img_service}-003")
    try:
        if country == "chn":
            blocked_log("Test blocked - Not written (CHN)")
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "003", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Data_Services_004():
    recorder.start(f"{img_service}-004")
    try:
        blocked_log("Test blocked - Can't check style guide")
    except Exception as e:
        error_log(e, "004", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False