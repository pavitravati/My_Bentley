from common_utils.android_image_comparision import *
from core.log_emitter import log, fail_log, metric_log, error_log
from time import sleep

img_service = "Theft Alarm"

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

# Need german vehicle
def Theft_Alarm_001():
    try:
        pass
    except Exception as e:
        error_log(e, "001", img_service)

# Need german vehicle
def Theft_Alarm_002():
    try:
        pass
    except Exception as e:
        error_log(e, "002", img_service)

def Theft_Alarm_003():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        controller.swipe_up()
        controller.click_text("STOLEN VEHICLE TRACKING")

        if controller.is_text_present("NO MESSAGES"):
            log("Theft alert page displays correctly when no alerts")
        else:
            fail_log("Theft alert page displays incorrectly when no alerts", "003", img_service)

        controller.click_by_image("Icons/back_icon.png")
        controller.swipe_down()
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "003", img_service)

# Only checks uk version for now
def Theft_Alarm_004():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        car = identify_car()
        controller.click_by_image("Icons/windows_icon.png")
        controller.swipe_up()
        controller.click_text("STOLEN VEHICLE TRACKING")

        if controller.is_text_present(f"We have detected an interior alarm on your {car}. Please check your vehicle."):
            log("Theft alert page displays correctly after an alert")
        else:
            fail_log("Theft alert page displays incorrectly after an alert", "004", img_service)

        controller.click_by_image("Icons/back_icon.png")
        controller.swipe_down()
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "004", img_service)

# Could not get the notification to be sent
def Theft_Alarm_005():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        controller.swipe_up()
        controller.click_text("STOLEN VEHICLE TRACKING")
        # Check what the notification is in car

    except Exception as e:
        error_log(e, "005", img_service)

# Need german vehicle
def Theft_Alarm_006():
    try:
        pass
    except Exception as e:
        error_log(e, "006", img_service)

def Theft_Alarm_007():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        controller.swipe_up()
        controller.click_text("STOLEN VEHICLE TRACKING")
        # Check what this looks like

    except Exception as e:
        error_log(e, "007", img_service)

def Theft_Alarm_008():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        controller.swipe_up()
        controller.click_text("STOLEN VEHICLE TRACKING")

        controller.click_by_image("Icons/clear_alert.png")
        if controller.click_text("Clear"):
            log("Theft alert clear button clicked")
            if controller.is_text_present("There are no alerts to display"):
                log("Theft alerts cleared")
            else:
                fail_log("Theft alerts not cleared", "008", img_service)
        else:
            fail_log("Theft alert clear button not found", "008", img_service)
        controller.swipe_down()
    except Exception as e:
        error_log(e, "008", img_service)

def Theft_Alarm_009():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/info_btn.png")
        controller.click_text("Service Management")
        if controller.click_text("Theft alert"):
            log("Theft alert service disabled in service management")
            sleep(3)
        else:
            fail_log("Theft alert service failed to be disabled in service management", "009", img_service)
        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/back_icon.png")

        controller.click_by_image("Icons/windows_icon.png")
        controller.swipe_up()
        controller.click_text("STOLEN VEHICLE TRACKING")

        if controller.is_text_present("This service is unavailable. It can be switched on in the Service Management screen for this vehicle."):
            log("Theft alert service successfully disabled")
        else:
            fail_log("Theft alert service not disabled", "009", img_service)
        controller.click_by_image("Icons/back_icon.png")
        controller.swipe_down()
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

        # Re-activate the service
        controller.click_by_image("Icons/info_btn.png")
        controller.click_text("Service Management")
        controller.click_text("Theft alert")
        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/back_icon.png")
    except Exception as e:
        error_log(e, "009", img_service)

def Theft_Alarm_010():
    try:
        log("✅ - Cannot complete style guide testcases (temporary)")
    except Exception as e:
        error_log(e, "010", img_service)
