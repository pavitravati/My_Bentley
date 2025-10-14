from time import sleep
from common_utils.android_image_comparision import *
from common_utils.android_controller import *
from core.log_emitter import log_emitter

def log(msg):
    log_emitter.log_signal.emit(msg)

def fail_log(msg, num):
    log(f"{msg}")
    controller.take_fail_screenshot(f"TheftAlarm-{msg}-{num}.png")

def error_log(e, num):
    log(f"⚠️ - Unexpected error: {e}")
    controller.take_fail_screenshot(f"TheftAlarm-{e}-{num}.png")

def TheftAlarm_001():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        controller.swipe_up()
        if controller.is_text_present("STOLEN VEHICLE TRACKING"):
            log("✅ - Theft Alarm tab displayed")
        else:
            fail_log("❌ - Theft Alarm tab not displayed", "001")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "001")

def TheftAlarm_002():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        controller.swipe_up()
        controller.click_text("STOLEN VEHICLE TRACKING")

        if controller.click_by_image("Icons/clear_alert.png"):
            if controller.click_text("Clear"):
                log("✅ - Alert notifications cleared")
            else:
                fail_log("❌ - Alert notifications could not be cleared", "002")
        else:
            fail_log("❌ - Alert notifications could not be cleared", "002")

        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "002")

def TheftAlarm_003():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        controller.swipe_up()
        controller.click_text("STOLEN VEHICLE TRACKING")

        if controller.is_text_present("NO MESSAGES"):
            log("✅ - Theft alert page displays correctly when no alerts")
        else:
            fail_log("❌ - Theft alert page displays incorrectly when no alerts", "003")

        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "003")

def TheftAlarm_004():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        controller.swipe_up()
        controller.click_text("STOLEN VEHICLE TRACKING")

        if controller.is_text_present("We have detected an interior alarm"):
            log("✅ - Theft alert page displays correctly after an alert")
        else:
            fail_log("❌ - Theft alert page displays incorrectly after an alert", "004")

        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "004")

# Can this be skipped
def TheftAlarm_005():
    try:
        pass
    except Exception as e:
        error_log(e, "005")

# What
def TheftAlarm_006():
    try:
        pass
    except Exception as e:
        error_log(e, "006")

def TheftAlarm_007():
    try:
        log("✅ - Cannot complete style guide testcases (temporary)")
    except Exception as e:
        error_log(e, "007")
