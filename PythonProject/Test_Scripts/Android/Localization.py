from core.log_emitter import blocked_log, error_log

img_service = "Localization"

def Localization_001():
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "001", img_service)

def Localization_002():
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "002", img_service)