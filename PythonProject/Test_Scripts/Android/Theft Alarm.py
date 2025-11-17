from common_utils.android_image_comparision import *
from core.log_emitter import log, fail_log, metric_log, error_log, blocked_log
from time import sleep
from core.globals import country
from core.globals import manual_run

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

def Theft_Alarm_001():
    try:
        blocked_log("Test blocked - Region locked (GER)")
    except Exception as e:
        error_log(e, "001", img_service)

def Theft_Alarm_002():
    try:
        blocked_log("Test blocked - Region locked (GER)")
    except Exception as e:
        error_log(e, "002", img_service)

def Theft_Alarm_003():
    try:
        if country == "eur":
            controller.click_by_image("Icons/windows_icon.png")
            sleep(0.5)
            controller.swipe_up(0.1)
            sleep(1)
            controller.click_text("STOLEN VEHICLE TRACKING")

            if controller.is_text_present("NO MESSAGES"):
                log("Theft alert page displays correctly when no alerts")
            else:
                fail_log("Theft alert page displays incorrectly when no alerts", "003", img_service)

            controller.click_by_image("Icons/back_icon.png")
            controller.swipe_down(0.05)
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "003", img_service)

# Only checks uk version for now
def Theft_Alarm_004():
    try:
        if country == "eur":
            controller.click_by_image("Icons/windows_icon.png")
            sleep(0.5)
            controller.swipe_up(0.1)
            sleep(1)
            controller.click_text("STOLEN VEHICLE TRACKING")

            if compare_with_expected_crop("Images/vehicle_alarm_image.png"):
                log("Theft alert page displays correctly after an alert")
            else:
                fail_log("Theft alert page displays incorrectly after an alert", "004", img_service)

            controller.click_by_image("Icons/back_icon.png")
            controller.swipe_down(0.05)
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "004", img_service)

# Could not get the notification to be sent
def Theft_Alarm_005():
    try:
        if country == "eur":
            controller.click_by_image("Icons/windows_icon.png")
            controller.swipe_up()
            controller.click_text("STOLEN VEHICLE TRACKING")
            # Check what the notification is in car
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "005", img_service)

def Theft_Alarm_006():
    try:
        blocked_log("Test blocked - Region locked (GER)")
    except Exception as e:
        error_log(e, "006", img_service)

def Theft_Alarm_007():
    try:
        if country == "eur":
            controller.click_by_image("Icons/windows_icon.png")
            controller.swipe_up()
            sleep(0.5)
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
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "007", img_service)

def Theft_Alarm_008():
    try:
        if country == "eur":
            controller.click_by_image("Icons/windows_icon.png")
            controller.swipe_up()
            sleep(0.5)
            controller.click_text("STOLEN VEHICLE TRACKING")

            controller.click_by_image("Icons/clear_alert.png")
            if controller.click_text("Clear"):
                log("Theft alert clear button clicked")
                sleep(3)
                if controller.is_text_present("There are no alerts to display"):
                    log("Theft alerts cleared")
                else:
                    fail_log("Theft alerts not cleared", "008", img_service)
            else:
                fail_log("Theft alert clear button not found", "008", img_service)

            controller.click_by_image("Icons/back_icon.png")
            controller.swipe_down(0.05)
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "008", img_service)

def Theft_Alarm_009():
    try:
        if country == "eur":
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            controller.click_by_image("Icons/info_btn.png")
            controller.click_text("Service Management")
            if controller.click_text("Theft alert"):
                log("Theft alert service disabled in service management")
                sleep(6)
            else:
                fail_log("Theft alert service failed to be disabled in service management", "009", img_service)
            controller.click_by_image("Icons/back_icon.png")
            controller.click_by_image("Icons/back_icon.png")

            controller.click_by_image("Icons/windows_icon.png")
            controller.swipe_up()
            sleep(0.5)
            controller.click_text("STOLEN VEHICLE TRACKING")

            if controller.is_text_present("This service is unavailable. It can be switched on in the Service Management screen for this vehicle."):
                log("Theft alert service successfully disabled")
            else:
                fail_log("Theft alert service not disabled", "009", img_service)
            controller.click_by_image("Icons/back_icon.png")
            controller.swipe_down(0.05)
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

            controller.click_by_image("Icons/info_btn.png")
            controller.click_text("Service Management")
            controller.click_text("Theft alert")
            sleep(6)
            controller.click_by_image("Icons/back_icon.png")
            controller.click_by_image("Icons/back_icon.png")
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "009", img_service)

def Theft_Alarm_010():
    try:
        if country == "eur":
            blocked_log("Test blocked - Can't check style guide")
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "010", img_service)
