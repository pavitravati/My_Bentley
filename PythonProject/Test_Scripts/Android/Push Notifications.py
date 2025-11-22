from common_utils.android_image_comparision import *
from core.app_functions import app_login_setup, identify_car
from core.log_emitter import log, fail_log, error_log, blocked_log
from core.globals import country
from core.globals import manual_run

img_service = "Push Notifications"

# Having a lot of problems with android notifications, need to ask about this and find out if it's a lost cause

# Need to do in car to see what a notification is like and how to click
def Push_Notifications_001():
    try:
        if country == "eur":
            if app_login_setup():
                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
                car_model = identify_car()
                # see if there is a way to swipe down to get full details of notification before cutoff to check full detail
                if controller.wait_for_text_and_click(f"Theft alert {car_model}"):
                    log("Theft alert triggered and clicked")
                else:
                    fail_log("Theft alert not triggered", "001", img_service)

                if controller.is_text_present("STOLEN VEHICLE TRACKING"):
                    log("Vehicle theft alert paged opened")
                else:
                    fail_log("Vehicle theft alert page not opened", "001", img_service)
        else:
            blocked_log("Test blocked - Region locked (EUR)")

    except Exception as e:
        error_log(e, "001", img_service)

def Push_Notifications_002():
    try:
        if app_login_setup():
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            car_model = identify_car()

            if controller.click_by_image("Icons/Remote_Lock.png"):
                log("Remote Lock operation performed")
                controller.click_home()
            else:
                fail_log("Remote Lock operation not performed", "002", img_service)

            # Opens to dashboard not alert screen
            if controller.wait_for_text_and_click(f"Lock my car {car_model} has been locked"):
                log("Lock notification received")
            else:
                fail_log("Lock notification not received", "002", img_service)

            if controller.wait_for_text("DASHBOARD"):
                log("Dashboard opened when notification clicked")
            else:
                fail_log("Dashboard not opened", "002", img_service)

    except Exception as e:
        error_log(e, "002", img_service)

# Get the notification but says cannot be done as vehicle error
def Push_Notifications_003():
    try:
        if app_login_setup():
            controller.click_by_image("Icons/windows_icon.png")

            controller.swipe_up()
            controller.click_text("MY CABIN COMFORT")
            controller.click_text("START")
            controller.click_home()

            controller.wait_for_text_and_click("")
    except Exception as e:
        error_log(e, "003", img_service)

def Push_Notifications_004():
    try:
        blocked_log("Test blocked - Not written due to error")
    except Exception as e:
        error_log(e, "004", img_service)

def Push_Notifications_005():
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "005", img_service)

def Push_Notifications_006():
    try:
        if country == "nar":
            blocked_log("Test blocked - Not written (NAR)")
        else:
            blocked_log("Test blocked - Region locked (NAR)")
    except Exception as e:
        error_log(e, "006", img_service)

def Push_Notifications_007():
    try:
        if country == "nar":
            blocked_log("Test blocked - Not written (NAR)")
        else:
            blocked_log("Test blocked - Region locked (NAR)")
    except Exception as e:
        error_log(e, "007", img_service)

def Push_Notifications_008():
    try:
        if country == "nar":
            blocked_log("Test blocked - Not written (NAR)")
        else:
            blocked_log("Test blocked - Region locked (NAR)")
    except Exception as e:
        error_log(e, "008", img_service)

def Push_Notifications_009():
    try:
        if country == "nar":
            blocked_log("Test blocked - Not written (NAR)")
        else:
            blocked_log("Test blocked - Region locked (NAR)")
    except Exception as e:
        error_log(e, "009", img_service)

def Push_Notifications_010():
    try:
        blocked_log("Test blocked - Can't check style guide")
    except Exception as e:
        error_log(e, "010", img_service)