from common_utils.android_image_comparision import controller
from core.app_functions import service_reset
from core.log_emitter import blocked_log, error_log, runtime_log
from core.screenrecord import ScreenRecorder

img_service = "Localization"
recorder = ScreenRecorder(device_serial=controller.d.serial)

def Localization_001():
    recorder.start(f"{img_service}-001")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "001", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Localization_002():
    recorder.start(f"{img_service}-002")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "002", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False