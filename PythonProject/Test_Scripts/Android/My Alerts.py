from common_utils.android_image_comparision import controller
from core.app_functions import service_reset
from core.log_emitter import error_log, blocked_log, runtime_log
from core.globals import country
from core.screenrecord import ScreenRecorder

img_service = "My Alerts"
recorder = ScreenRecorder(device_serial=controller.d.serial)

def My_Alerts_001():
    recorder.start(f"{img_service}-001")
    try:
        if country == "NAR":
            blocked_log("Test blocked - Not written (NAR)")
        else:
            blocked_log("Test blocked - Region locked (NAR)")
    except Exception as e:
        error_log(e, "001", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def My_Alerts_002():
    recorder.start(f"{img_service}-002")
    try:
        if country == "NAR":
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


def My_Alerts_003():
    recorder.start(f"{img_service}-003")
    try:
        if country == "NAR":
            blocked_log("Test blocked - Not written (NAR)")
        else:
            blocked_log("Test blocked - Region locked (NAR)")
    except Exception as e:
        error_log(e, "003", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def My_Alerts_004():
    recorder.start(f"{img_service}-004")
    try:
        if country == "NAR":
            blocked_log("Test blocked - Not written (NAR)")
        else:
            blocked_log("Test blocked - Region locked (NAR)")
    except Exception as e:
        error_log(e, "004", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def My_Alerts_005():
    recorder.start(f"{img_service}-005")
    try:
        if country == "NAR":
            blocked_log("Test blocked - Not written (NAR)")
        else:
            blocked_log("Test blocked - Region locked (NAR)")
    except Exception as e:
        error_log(e, "005", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def My_Alerts_006():
    recorder.start(f"{img_service}-006")
    try:
        if country == "NAR":
            blocked_log("Test blocked - Not written (NAR)")
        else:
            blocked_log("Test blocked - Region locked (NAR)")
    except Exception as e:
        error_log(e, "006", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def My_Alerts_007():
    recorder.start(f"{img_service}-007")
    try:
        if country == "NAR":
            blocked_log("Test blocked - Not written (NAR)")
        else:
            blocked_log("Test blocked - Region locked (NAR)")
    except Exception as e:
        error_log(e, "007", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def My_Alerts_008():
    recorder.start(f"{img_service}-008")
    try:
        if country == "NAR":
            blocked_log("Test blocked - Not written (NAR)")
        else:
            blocked_log("Test blocked - Region locked (NAR)")
    except Exception as e:
        error_log(e, "008", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def My_Alerts_009():
    recorder.start(f"{img_service}-009")
    try:
        if country == "NAR":
            blocked_log("Test blocked - Not written (NAR)")
        else:
            blocked_log("Test blocked - Region locked (NAR)")
    except Exception as e:
        error_log(e, "009", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def My_Alerts_010():
    recorder.start(f"{img_service}-010")
    try:
        if country == "NAR":
            blocked_log("Test blocked - Not written (NAR)")
        else:
            blocked_log("Test blocked - Region locked (NAR)")
    except Exception as e:
        error_log(e, "010", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def My_Alerts_011():
    recorder.start(f"{img_service}-011")
    try:
        if country == "NAR":
            blocked_log("Test blocked - Not written (NAR)")
        else:
            blocked_log("Test blocked - Region locked (NAR)")
    except Exception as e:
        error_log(e, "011", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def My_Alerts_012():
    recorder.start(f"{img_service}-012")
    try:
        if country == "NAR":
            blocked_log("Test blocked - Not written (NAR)")
        else:
            blocked_log("Test blocked - Region locked (NAR)")
    except Exception as e:
        error_log(e, "012", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def My_Alerts_013():
    recorder.start(f"{img_service}-013")
    try:
        if country == "NAR":
            blocked_log("Test blocked - Not written (NAR)")
        else:
            blocked_log("Test blocked - Region locked (NAR)")
    except Exception as e:
        error_log(e, "013", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def My_Alerts_014():
    recorder.start(f"{img_service}-014")
    try:
        if country == "NAR":
            blocked_log("Test blocked - Not written (NAR)")
        else:
            blocked_log("Test blocked - Region locked (NAR)")
    except Exception as e:
        error_log(e, "014", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def My_Alerts_015():
    recorder.start(f"{img_service}-015")
    try:
        if country == "NAR":
            blocked_log("Test blocked - Not written (NAR)")
        else:
            blocked_log("Test blocked - Region locked (NAR)")
    except Exception as e:
        error_log(e, "015", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def My_Alerts_016():
    recorder.start(f"{img_service}-016")
    try:
        if country == "NAR":
            blocked_log("Test blocked - Not written (NAR)")
        else:
            blocked_log("Test blocked - Region locked (NAR)")
    except Exception as e:
        error_log(e, "016", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def My_Alerts_017():
    recorder.start(f"{img_service}-017")
    try:
        if country == "NAR":
            blocked_log("Test blocked - Can't check style guide")
        else:
            blocked_log("Test blocked - Region locked (NAR)")
    except Exception as e:
        error_log(e, "017", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False