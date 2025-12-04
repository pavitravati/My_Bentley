from time import sleep
from common_utils.android_image_comparision import *
from common_utils.android_controller import *
from core.app_functions import service_reset
from core.globals import country
from core.log_emitter import log, fail_log, metric_log, error_log, blocked_log, runtime_log
from core.globals import manual_run
from core.screenrecord import ScreenRecorder

img_service = "Stolen Vehicle Locator"
recorder = ScreenRecorder(device_serial=controller.d.serial)


def Stolen_Vehicle_Locator_001():
    recorder.start(f"{img_service}-001")
    try:
        if country == "eur":
            blocked_log("Test blocked - Region locked (NAR/CHN)")
        else:
            blocked_log("Test blocked - Not written (NAR/CHN)")
    except Exception as e:
        error_log(e, "001", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Stolen_Vehicle_Locator_002():
    recorder.start(f"{img_service}-002")
    try:
        if country == "eur":
            blocked_log("Test blocked - Region locked (NAR/CHN)")
        else:
            blocked_log("Test blocked - Not written (NAR/CHN)")
    except Exception as e:
        error_log(e, "002", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Stolen_Vehicle_Locator_003():
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