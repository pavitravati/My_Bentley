from common_utils.android_image_comparision import *
from core.log_emitter import log_emitter


def log(msg):
    log_emitter.log_signal.emit(msg)

def fail_log(msg, num):
    log(f"{msg}")
    controller.take_fail_screenshot(f"Push Notifications-{msg}-{num}.png")

def error_log(e, num):
    log(f"⚠️ - Unexpected error: {e}")
    controller.take_fail_screenshot(f"Push Notifications-{e}-{num}.png")

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

# Need to do in car to see what a notificiation is like and how to click
def Push_Notifications_001():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        car_model = identify_car()
        # see if there is a way to swipe down to get full details of notification before cutoff to check full detail
        if controller.wait_for_text_and_click(f"Theft alert {car_model}"):
            log("✅ - Theft alert triggered and clicked")
        else:
            fail_log("❌ - Theft alert not triggered", "001")

        if controller.is_text_present("STOLEN VEHICLE TRACKING"):
            log("✅ - Vehicle theft alert paged opened")
        else:
            fail_log("❌ - Vehicle theft alert page not opened", "001")

    except Exception as e:
        error_log(e, "001")

def Push_Notifications_002():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        car_model = identify_car()

        if controller.click_by_image("Icons/Remote_Lock.png"):
            log("✅ - Remote Lock operation performed")
            controller.click_home()
        else:
            fail_log("❌ - Remote Lock operation not performed", "002")

        # Opens to dashboard not alert screen
        if controller.wait_for_text_and_click(f"Lock my car {car_model} has been locked"):
            log("✅ - Lock notification received")
        else:
            fail_log("❌ - Lock notification not received", "002")

        if controller.wait_for_text("DASHBOARD"):
            log("✅ - Dashboard opened when notification clicked")
        else:
            fail_log("❌ - Dashboard not opened", "002")

    except Exception as e:
        error_log(e, "002")

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
        error_log(e, "003")

# Don't have charger
def Push_Notifications_004():
    try:
        pass
    except Exception as e:
        error_log(e, "004")

# Driving needed
def Push_Notifications_005():
    try:
        pass
    except Exception as e:
        error_log(e, "005")

def Push_Notifications_006():
    try:
        pass
    except Exception as e:
        error_log(e, "006")

def Push_Notifications_007():
    try:
        pass
    except Exception as e:
        error_log(e, "007")

def Push_Notifications_008():
    try:
        pass
    except Exception as e:
        error_log(e, "008")

def Push_Notifications_009():
    try:
        pass
    except Exception as e:
        error_log(e, "009")

def Push_Notifications_010():
    try:
        log("✅ - Cannot complete style guide testcases (temporary)")
    except Exception as e:
        error_log(e, "010")