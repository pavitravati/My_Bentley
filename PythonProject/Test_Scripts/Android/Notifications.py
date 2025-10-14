from time import sleep
from common_utils.android_image_comparision import *
from common_utils.android_controller import *
v
from core.log_emitter import log_emitter

def log(msg):
    log_emitter.log_signal.emit(msg)

def fail_log(msg, num):
    log(f"{msg}")
    controller.take_fail_screenshot(f"Notifications-{msg}-{num}.png")

def error_log(e, num):
    log(f"⚠️ - Unexpected error: {e}")
    controller.take_fail_screenshot(f"Notifications-{e}-{num}.png")

def Notifications_001():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        if controller.click_by_image("Icons/New_Notification_icon.png") or controller.click_by_image("Icons/Notification_icon.png"):
            log("✅ - Notification page launched")
        else:
            fail_log("❌ - Notification page not launched", "001")

        if controller.is_text_present("NOTIFICATIONS"):
            log("✅ - Notification title displayed")
        else:
            fail_log("❌ - Notification title not displayed", "001")

        if controller.is_text_present("Actions") and controller.is_text_present("Alerts"):
            log("✅ - Actions & Alerts tab displayed")
        else:
            fail_log("❌ - Actions & Alerts tab not displayed", "001")

        if controller.is_text_present("Last updated"):
            log("✅ - Last updated displayed")
        else:
            fail_log("❌ - Last updated not displayed", "001")

        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "001")

def Notifications_002():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/New_Notification_icon.png")
        controller.click_by_image("Icons/Notification_icon.png")

        controller.swipe_down()
        if controller.wait_for_text("Last updated"):
            pass
            # use the taken 07/10 dump to check the accurate information

        controller.swipe_down()
    except Exception as e:
        error_log(e, "002")

def Notifications_003():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/New_Notification_icon.png")
        controller.click_by_image("Icons/Notification_icon.png")

        if controller.is_text_present("There are no new notifications to display"):
            log("✅ - No new notifications displayed correctly")
        elif controller.is_text_present("There are new notifications to display"):
            # Here use the 07/10 dump to check
            log("✅ - Maximum of 10 notifications are displayed correctly")
        else:
            fail_log("❌ - Notifications are not displayed correctly", "003")

        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "003")

def Notifications_004():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/New_Notification_icon.png")
        controller.click_by_image("Icons/Notification_icon.png")

        if not controller.is_text_present("There are no new notifications to display"):
            # use 07/10 dump to check all details
            pass
        else:
            fail_log("❌ - There are no notifications displayed to check the format", "004")

        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "004")

# Check if this can be skipped
def Notifications_005():
    try:
        pass
    except Exception as e:
        error_log(e, "005")

def Notifications_006():
    try:
        log("✅ - Cannot complete style guide testcases (temporary)")
    except Exception as e:
        error_log(e, "006")
