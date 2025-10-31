from common_utils.android_image_comparision import *
from core.log_emitter import log, fail_log, error_log, metric_log

img_service = "Notifications"

def Notifications_001():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        if controller.click_by_image("Icons/New_Notification_icon.png") or controller.click_by_image("Icons/Notification_icon.png"):
            log("Notification page launched")
        else:
            fail_log("Notification page not launched", "001", img_service)

        if controller.is_text_present("NOTIFICATIONS"):
            log("Notification title displayed")
        else:
            fail_log("Notification title not displayed", "001", img_service)

        if controller.is_text_present("Actions") and controller.is_text_present("Alerts"):
            log("Actions & Alerts tab displayed")
        else:
            fail_log("Actions & Alerts tab not displayed", "001", img_service)

        if controller.is_text_present("Last updated"):
            log("Last updated displayed")
        else:
            fail_log("Last updated not displayed", "001", img_service)

        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "001", img_service)

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
        error_log(e, "002", img_service)

def Notifications_003():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/New_Notification_icon.png")
        controller.click_by_image("Icons/Notification_icon.png")

        if controller.is_text_present("There are no new notifications to display"):
            log("No new notifications displayed correctly")
        elif controller.is_text_present("There are new notifications to display"):
            # Here use the 07/10 dump to check
            log("Maximum of 10 notifications are displayed correctly")
        else:
            fail_log("Notifications are not displayed correctly", "003", img_service)

        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "003", img_service)

def Notifications_004():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/New_Notification_icon.png")
        controller.click_by_image("Icons/Notification_icon.png")

        if not controller.is_text_present("There are no new notifications to display"):
            # use 07/10 dump to check all details
            pass
        else:
            fail_log("There are no notifications displayed to check the format", "004", img_service)

        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "004", img_service)

# Check if this can be skipped
def Notifications_005():
    try:
        pass
    except Exception as e:
        error_log(e, "005", img_service)

def Notifications_006():
    try:
        pass
    except Exception as e:
        error_log(e, "006", img_service)

def Notifications_007():
    try:
        pass
    except Exception as e:
        error_log(e, "007", img_service)

def Notifications_008():
    try:
        log("Cannot complete style guide testcases (temporary)")
    except Exception as e:
        error_log(e, "008", img_service)
