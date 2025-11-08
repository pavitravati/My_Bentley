from common_utils.android_image_comparision import *
from core.log_emitter import log, fail_log, error_log, metric_log

img_service = "Push Notifications"

def identify_car():

    if compare_with_expected_crop("Icons/Bentayga.png"):
        car = 'Bentayga'
    elif compare_with_expected_crop("Icons/ContinentalGT.png"):
        car = 'Continental GT'
    elif compare_with_expected_crop("Icons/ContinentalGTC.png"):
        car = 'Continental GTC'
    elif compare_with_expected_crop("Icons/FlyingSpur.png"):
        car = 'Flying Spur'
    else:
        car = ''

    return car

# Having alot of problems with android notifications, need to ask about this and find out if its a lost cause

# Need to do in car to see what a notification is like and how to click
def Push_Notifications_001():
    try:
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

    except Exception as e:
        error_log(e, "001", img_service)

def Push_Notifications_002():
    try:
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
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")

        controller.swipe_up()
        controller.click_text("MY CABIN COMFORT")
        controller.click_text("START")
        controller.click_home()

        controller.wait_for_text_and_click("")
    except Exception as e:
        error_log(e, "003", img_service)

# Don't have charger
def Push_Notifications_004():
    try:
        pass
    except Exception as e:
        error_log(e, "004", img_service)

# Can't automate
def Push_Notifications_005():
    try:
        log("Can't automate")
    except Exception as e:
        error_log(e, "005", img_service)

# Can't automate
def Push_Notifications_006():
    try:
        log("Can't automate")
    except Exception as e:
        error_log(e, "006", img_service)

def Push_Notifications_007():
    try:
        pass
    except Exception as e:
        error_log(e, "007", img_service)

def Push_Notifications_008():
    try:
        pass
    except Exception as e:
        error_log(e, "008", img_service)

def Push_Notifications_009():
    try:
        pass
    except Exception as e:
        error_log(e, "009", img_service)

def Push_Notifications_010():
    try:
        log("Cannot complete style guide testcases (temporary)")
    except Exception as e:
        error_log(e, "010", img_service)