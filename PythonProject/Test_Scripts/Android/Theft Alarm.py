from common_utils.android_image_comparision import *
from core.app_functions import app_login_setup, identify_car, remote_swipe, service_reset
from core.log_emitter import log, fail_log, metric_log, error_log, blocked_log, runtime_log
from time import sleep
from core.globals import country
from core.screenrecord import ScreenRecorder
from core import globals

img_service = "Theft Alarm"
recorder = ScreenRecorder(device_serial=controller.d.serial)

def Theft_Alarm_001():
    recorder.start(f"{img_service}-001")
    try:
        blocked_log("Test blocked - Region locked (GER)")
    except Exception as e:
        error_log(e, "001", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Theft_Alarm_002():
    recorder.start(f"{img_service}-002")
    try:
        blocked_log("Test blocked - Region locked (GER)")
    except Exception as e:
        error_log(e, "002", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Theft_Alarm_003():
    recorder.start(f"{img_service}-003")
    try:
        if country == "eur":
            if app_login_setup():
                controller.click_by_image("Icons/remote_icon.png")
                remote_swipe("STOLEN VEHICLE TRACKING")
                controller.click_text("STOLEN VEHICLE TRACKING")

                if controller.is_text_present("NO MESSAGES"):
                    log("Theft alert page displays correctly when no alerts")
                else:
                    fail_log("Theft alert page displays incorrectly when no alerts", "003", img_service)

                controller.click_by_image("Icons/back_icon.png")
                controller.swipe_down(0.05)
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "003", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

# Only checks uk version for now
def Theft_Alarm_004():
    recorder.start(f"{img_service}-004")
    try:
        if country == "eur":
            if app_login_setup():
                controller.click_by_image("Icons/remote_icon.png")
                remote_swipe("STOLEN VEHICLE TRACKING")
                controller.click_text("STOLEN VEHICLE TRACKING")

                if compare_with_expected_crop("Images/vehicle_alarm_image.png"):
                    log("Theft alert page displays correctly after an alert")
                else:
                    fail_log("Theft alert page displays incorrectly after an alert", "004", img_service)

                controller.click_by_image("Icons/back_icon.png")
                controller.swipe_down(0.05)
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "004", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

# Could not get the notification to be sent
def Theft_Alarm_005():
    recorder.start(f"{img_service}-005")
    try:
        if country == "eur":
            blocked_log("Test blocked - Push notifications not working")
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "005", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Theft_Alarm_006():
    recorder.start(f"{img_service}-006")
    try:
        blocked_log("Test blocked - Region locked (GER)")
    except Exception as e:
        error_log(e, "006", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Theft_Alarm_007():
    recorder.start(f"{img_service}-007")
    try:
        if country == "eur":
            if app_login_setup():
                controller.click_by_image("Icons/remote_icon.png")
                remote_swipe("STOLEN VEHICLE TRACKING")
                controller.click_text("STOLEN VEHICLE TRACKING")

                if compare_with_expected_crop("Images/red_alarm.png"):
                    log("Most recent alert displayed in red banner")
                else:
                    fail_log("Most recent alert not displayed in red banner", "007", img_service)

                alerts = controller.d.xpath('//android.widget.TextView[contains(@text, "alarm") or preceding-sibling::*[contains(@text, "alarm")]]').all()
                if len(alerts) > 0:
                    log("Past alerts displayed")
                    for i in range(2, len(alerts), 2):
                        metric_log(f"{alerts[i].attrib.get("text", "")}: {alerts[i + 1].attrib.get("text", "")}")
                else:
                    fail_log("No alerts displayed", "007", img_service)

                if compare_with_expected_crop("Icons/clear_alert.png"):
                    log("Clear alarm history button displayed")
                else:
                    fail_log("Clear alarm history button not displayed", "007", img_service)

                controller.click_by_image("Icons/back_icon.png")
                controller.swipe_down(0.05)
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "007", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Theft_Alarm_008():
    recorder.start(f"{img_service}-008")
    try:
        if country == "eur":
            if app_login_setup():
                controller.click_by_image("Icons/remote_icon.png")
                remote_swipe("STOLEN VEHICLE TRACKING")
                controller.click_text("STOLEN VEHICLE TRACKING")

                controller.click_by_image("Icons/clear_alert.png")
                if controller.click_text("Clear"):
                    log("Theft alert clear button clicked")
                    sleep(2)
                    if controller.is_text_present("There are no alerts to display"):
                        log("Theft alerts cleared")
                    else:
                        fail_log("Theft alerts not cleared", "008", img_service)
                else:
                    fail_log("Theft alert clear button not found", "008", img_service)

                controller.click_by_image("Icons/back_icon.png")
                controller.swipe_down(0.05)
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "008", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Theft_Alarm_009():
    recorder.start(f"{img_service}-009")
    try:
        if country == "eur":
            blocked_log("Test blocked - Can't check style guide")
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "009", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False
