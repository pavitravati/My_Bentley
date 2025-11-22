from time import sleep
from common_utils.android_image_comparision import *
from core.log_emitter import log, fail_log, error_log, blocked_log
from common_utils.android_controller import *
from core.app_functions import enable_flight_mode, disable_flight_mode, app_login_setup, identify_car
from datetime import datetime, timedelta
from core.globals import manual_run, current_pin

img_service = "Remote Lock-Unlock"

def check_notif(text, num, is_fail=False):
    car = identify_car()
    controller.click_by_image("Icons/New_Notification_icon.png")
    controller.click_by_image("Icons/Notification_icon.png")
    controller.notif_refresh()
    sleep(1)
    while controller.is_text_present("updating..."):
        sleep(1)
    controller.wait_for_text_and_click("Update vehicle data")
    controller.click_by_image("Icons/Error_Icon.png")

    notifications = controller.d.xpath('//android.widget.TextView').all()
    events = []

    if notifications[2].attrib.get("text") == "NOTIFICATIONS":
        notifications.pop(0)
    if "Last updated" in notifications[2].attrib.get("text"):
        notifications.pop(0)
    for i in range(2, 5, 3):
        try:
            title = notifications[i].attrib.get("text", "")
            time = notifications[i + 1].attrib.get("text", "")
            desc = notifications[i + 2].attrib.get("text", "")
            events.append({
                "title": title,
                "time": time,
                "description": desc
            })

        except IndexError:
            break

    now = datetime.now()
    displayed_time = datetime.strptime(events[0]['time'][-5:], "%H:%M")
    same_minute = displayed_time.strftime("%H:%M") == now.strftime("%H:%M")
    last_minute = displayed_time.strftime("%H:%M") == (now - timedelta(minutes=1)).strftime("%H:%M")

    expected_msg = f"{car} {text}" if not is_fail else f"{text} {car}"
    print(events[0]['title'])
    print(expected_msg)
    print(same_minute)
    print(last_minute)
    if events[0]['title'] == expected_msg and (same_minute or last_minute):
        log(f"Remote {text} notification displayed correctly")
    else:
        fail_log(f"Remote {text} notification not displayed", num, img_service)
    controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

def Remote_Lock_Unlock_001():
    try:
        if app_login_setup():
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            if (compare_with_expected_crop("Icons/Remote_Lock.png")):
                log("Lock button visible")
            else:
                fail_log("Lock button not visible", "001", img_service)
    
            if (compare_with_expected_crop("Icons/Remote_Unlock.png")):
                log("Unlock button visible")
            else:
                fail_log("Unlock button not visible", "001", img_service)

    except Exception as e:
        error_log(e, "001", img_service)

# controller.swipe_up()
# if controller.is_text_present("ACTIVATE STOLEN VEHICLE TRACKING"):
#     controller.extra_small_swipe_up()

def Remote_Lock_Unlock_002():
    try:
        if app_login_setup():
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            controller.click_by_image("Icons/lock_Icon.png")
            sleep(1)
            controller.enter_pin(current_pin)

            timeout_check = 0
            while not controller.is_text_present("Successfully locked") or compare_with_expected_crop(
                    "Icons/Error_Icon.png"):
                sleep(1)
                timeout_check += 1
                if timeout_check > 60:
                    fail_log("Remote lock took longer than 60 seconds so test timed out", "002", img_service)
                    break

            if controller.is_text_present("Successfully locked"):
                log("Lock message displayed")
                if controller.wait_for_text("Successfully locked"):
                    log("Lock notification displayed")
                else:
                    fail_log("Lock notification not displayed", "002", img_service)

                if controller.wait_for_text("Vehicle locked"):
                    log("Lock status changed")
                else:
                    fail_log("Lock status not changed", "002", img_service)

                check_notif("locked", "005")
            elif compare_with_expected_crop("Icons/Error_Icon.png"):
                fail_log("Error message displayed when unlocking", "002", img_service)
            else:
                fail_log("Lock message not displayed", "002", img_service)

    except Exception as e:
        error_log(e, "002", img_service)

def Remote_Lock_Unlock_003():
    try:
        if app_login_setup():
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            controller.click_by_image("Icons/lock_icon.png")
            sleep(1)
            controller.enter_pin(current_pin)
            timeout_check = 0
            while not controller.is_text_present("Vehicle could not be locked") or not compare_with_expected_crop(
                    "Icons/Error_Icon.png"):
                sleep(1)
                timeout_check += 1
                if timeout_check > 60:
                    fail_log("Remote lock took longer than 60 seconds so test timed out", "003", img_service)
                    break
            if controller.is_text_present("Vehicle could not be locked"):
                log("Remote lock blocked when ignition on")
                if controller.wait_for_text("Vehicle unlocked"):
                    log("Lock status unchanged")
                else:
                    fail_log("Lock status not unchanged", "003", img_service)
                controller.click_by_image("Icons/Error_Icon.png")

                check_notif("Failed to lock", "003", True)
            else:
                fail_log("Remote lock not blocked", "003", img_service)

    except Exception as e:
        error_log(e, "003", img_service)

def Remote_Lock_Unlock_004():
    try:
        if app_login_setup():
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            controller.click_by_image("Icons/lock_icon.png")
            sleep(1)
            controller.enter_pin("0000" if current_pin != "0000" else "0001")
            if controller.wait_for_text("Invalid PIN. Please try again."):
                log("Remote lock/unlock invalid PIN message displayed")
            else:
                fail_log("Remote lock/unlock invalid PIN message not displayed", "004", img_service)
            controller.click(500, 500)

    except Exception as e:
        error_log(e, "004", img_service)

def Remote_Lock_Unlock_005():
    try:
        if app_login_setup():
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            controller.click_by_image("Icons/unlock_icon.png")
            sleep(1)
            controller.enter_pin(current_pin)
            timeout_check = 0
            while not controller.is_text_present("Vehicle could not be unlocked") or not compare_with_expected_crop(
                    "Icons/Error_Icon.png"):
                sleep(1)
                timeout_check += 1
                if timeout_check > 60:
                    fail_log("Remote lock took longer than 60 seconds so test timed out", "005", img_service)
                    break
            if controller.is_text_present("Vehicle could not be unlocked"):
                log("Remote unlock blocked when ignition on")
                if controller.wait_for_text("Vehicle locked"):
                    log("Lock status unchanged")
                else:
                    fail_log("Lock status not unchanged", "005", img_service)
                controller.click_by_image("Icons/Error_Icon.png")

                check_notif("Failed to unlock", "005", True)
            else:
                fail_log("Remote lock not blocked", "005", img_service)

    except Exception as e:
        error_log(e, "005", img_service)

def Remote_Lock_Unlock_006():
    try:
        if app_login_setup():
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            controller.click_by_image("Icons/unlock_Icon.png")
            sleep(1)
            controller.enter_pin(current_pin)
    
            timeout_check=0
            while not controller.is_text_present("Successfully unlocked") or compare_with_expected_crop("Icons/Error_Icon.png"):
                sleep(1)
                timeout_check += 1
                if timeout_check > 60:
                    fail_log("Remote lock took longer than 60 seconds so test timed out", "006", img_service)
                    break

            if controller.is_text_present("Successfully unlocked"):
                log("Unlock message displayed")
                if controller.wait_for_text("Successfully unlocked"):
                    log("Unlock notification displayed")
                else:
                    fail_log("Unlock notification not displayed", "006", img_service)
    
                if controller.wait_for_text("Vehicle unlocked"):
                    log("Lock status changed")
                else:
                    fail_log("Lock status not changed", "006", img_service)
    
                check_notif("unlocked", "006")
            elif compare_with_expected_crop("Icons/Error_Icon.png"):
                fail_log("Error message displayed when unlocking", "006", img_service)
            else:
                fail_log("Unlock message not displayed", "006", img_service)

    except Exception as e:
        error_log(e, "006", img_service)

def Remote_Lock_Unlock_007():
    try:
        if app_login_setup():
            controller.click_by_image("Icons/New_Notification_icon.png")
            controller.click_by_image("Icons/Notification_icon.png")

            notifs = controller.d.xpath('//android.widget.TextView[following-sibling::*[1][contains(@text, ":")] or contains(@text, ":") or preceding-sibling::*[1][contains(@text, ":")]]').all()
            if len(notifs) > 2:
                log("Past notifications displayed")
                start = 2 if "Last updated" in notifs[1].attrib.get("text") else 1
                for i in range(start, len(notifs), 3):
                    if i + 2 < len(notifs):
                        log(f"{notifs[i].attrib.get("text")} - {notifs[i + 2].attrib.get("text")} ({notifs[i + 1].attrib.get("text")})")
            else:
                fail_log("Past notifications not displayed", "007", img_service)
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "007", img_service)

def Remote_Lock_Unlock_008():
    try:
        if app_login_setup():
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            latency_time = time.time()
            controller.click_by_image("Icons/lock_icon.png")
            sleep(1)
            controller.enter_pin(current_pin)
            timeout_check=0
            while not controller.is_text_present("Successfully locked") or not compare_with_expected_crop("Icons/Error_Icon.png"):
                sleep(1)
                timeout_check += 1
                if timeout_check > 60:
                    fail_log("Remote lock took longer than 60 seconds so test timed out", "008", img_service)
                    break
            if controller.is_text_present("Successfully locked"):
                latency_time = time.time() - latency_time
                if latency_time < 40:
                    log(f"Latency time: {latency_time}")
                else:
                    fail_log(f"Latency time: {latency_time}", "008", img_service)
            else:
                fail_log("Timed out - Car took too long", "008", img_service)

    except Exception as e:
        error_log(e, "008", img_service)

def Remote_Lock_Unlock_009():
    try:
        if app_login_setup():
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            controller.click_by_image("Icons/lock_icon.png")
            sleep(1)
            controller.enter_pin(current_pin)
            timeout_check = 0
            while not controller.is_text_present("Successfully locked") or not compare_with_expected_crop("Icons/Error_Icon.png"):
                sleep(1)
                timeout_check += 1
                if timeout_check > 60:
                    fail_log("Remote lock took longer than 60 seconds so test timed out", "009", img_service)
                    break
            if controller.is_text_present("Successfully locked"):
                log("Remote lock worked while locked")
                # Check what is said in the notif
                check_notif("lock", "009")
            else:
                fail_log("Remote lock failed while locked", "009", img_service)

    except Exception as e:
        error_log(e, "009", img_service)

def Remote_Lock_Unlock_010():
    try:
        if app_login_setup():
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            controller.click_by_image("Icons/unlock_icon.png")
            sleep(1)
            controller.enter_pin(current_pin)
            timeout_check = 0
            while not controller.is_text_present("Successfully unlocked") or not compare_with_expected_crop("Icons/Error_Icon.png"):
                sleep(1)
                timeout_check += 1
                if timeout_check > 60:
                    fail_log("Remote lock took longer than 60 seconds so test timed out", "010", img_service)
                    break
            if controller.is_text_present("Successfully unlocked"):
                log("Remote unlock worked while unlocked")
                # Check what is said in the notif
                check_notif("unlock", "010")
            else:
                fail_log("Remote unlock failed while unlocked", "010", img_service)

    except Exception as e:
        error_log(e, "010", img_service)

def Remote_Lock_Unlock_011():
    try:
        if app_login_setup():
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            enable_flight_mode()
            sleep(1)
            controller.click_by_image("Icons/lock_icon.png")
            sleep(1)
            controller.enter_pin(current_pin)

            if controller.wait_for_text("Vehicle could not be locked"):
                log("Remote lock failed without network connection")
            else:
                fail_log("Remote lock failed without network connection", "011", img_service)

            controller.click_text("Cancel")
            disable_flight_mode()
            sleep(1)

    except Exception as e:
        error_log(f"⚠️ - Unexpected error: {e}", "011", img_service)

def Remote_Lock_Unlock_012():
    try:
        if app_login_setup():
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            controller.click_by_image("Icons/lock_Icon.png")
            sleep(1)
            controller.enter_pin(current_pin)
            timeout_check = 0
            while not controller.is_text_present("Successfully unlocked") or not compare_with_expected_crop("Icons/Error_Icon.png"):
                sleep(1)
                timeout_check += 1
                if timeout_check > 60:
                    fail_log("Remote lock took longer than 60 seconds so test timed out", "012", img_service)
                    break
            if controller.is_text_present("Successfully unlocked"):
                log("Lock message displayed when fob key in vehicle")
                if controller.wait_for_text("Vehicle locked"):
                    log("Lock status changed")
                else:
                    fail_log("Lock status not changed", "012", img_service)

                # Check what is said in the notif
                check_notif("lock", "012")
            else:
                fail_log("Lock message not displayed when fob key in vehicle", "012", img_service)

    except Exception as e:
        error_log(e, "012", img_service)

def Remote_Lock_Unlock_013():
    try:
        if app_login_setup():
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            controller.click_by_image("Icons/unlock_Icon.png")
            sleep(1)
            controller.enter_pin(current_pin)
            timeout_check = 0
            while not controller.is_text_present("Successfully unlocked") or not compare_with_expected_crop("Icons/Error_Icon.png"):
                sleep(1)
                timeout_check += 1
                if timeout_check > 60:
                    fail_log("Remote lock took longer than 60 seconds so test timed out", "013", img_service)
                    break
            if controller.wait_for_text("Successfully unlocked"):
                log("Unlock message displayed when fob key inside vehicle")
                if controller.wait_for_text("Vehicle unlocked"):
                    log("Lock status changed")
                else:
                    fail_log("Lock status not changed", "013", img_service)

                # Check what is said in the notif
                check_notif("unlock", "013")
            else:
                fail_log("Unlock message not displayed when fob key inside vehicle", "013", img_service)

    except Exception as e:
        error_log(e, "013", img_service)

def Remote_Lock_Unlock_014():
    try:
        if app_login_setup():
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            controller.click_by_image("Icons/lock_Icon.png")
            sleep(1)
            controller.enter_pin(current_pin)
            timeout_check = 0
            while not controller.is_text_present("Successfully locked") or not compare_with_expected_crop("Icons/Error_Icon.png"):
                sleep(1)
                timeout_check += 1
                if timeout_check > 60:
                    fail_log("Remote lock took longer than 60 seconds so test timed out", "014", img_service)
                    break
            if controller.wait_for_text("Successfully locked"):
                log("Lock message displayed when fob key inside vehicle")
                if controller.wait_for_text("Vehicle locked"):
                    log("Lock status changed")
                else:
                    fail_log("Lock status not changed", "014", img_service)

                # Check what is said in the notif
                check_notif("lock", "014")
            else:
                fail_log("Lock message not displayed when fob key inside vehicle", "014", img_service)

    except Exception as e:
        error_log(e, "014", img_service)

def Remote_Lock_Unlock_015():
    try:
        if app_login_setup():
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            controller.click_by_image("Icons/lock_icon.png")
            sleep(1)
            controller.enter_pin(current_pin)
            timeout_check=0
            while not controller.is_text_present("Vehicle could not be locked") or not compare_with_expected_crop("Icons/Error_Icon.png"):
                sleep(1)
                timeout_check += 1
                if timeout_check > 60:
                    fail_log("Remote lock took longer than 60 seconds so test timed out", "015", img_service)
                    break
            # below has error message is it always going to happen
            if controller.wait_for_text_that_contains("Please close the driver's door"):
                log("Remote lock blocked when driver's door open")
                if controller.wait_for_text("Vehicle unlocked"):
                    log("Lock status unchanged")
                else:
                    fail_log("Lock status not unchanged", "015", img_service)
                controller.click_by_image("Icons/Error_Icon.png")

                # Check what is said in the notif
                check_notif("Failed to lock", "015", True)
            else:
                fail_log("Remote lock not blocked", "015", img_service)

    except Exception as e:
        error_log(e, "015", img_service)

def Remote_Lock_Unlock_016():
    try:
        if app_login_setup():
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            controller.click_by_image("Icons/lock_icon.png")
            sleep(1)
            controller.enter_pin(current_pin)
            timeout_check=0
            while not controller.is_text_present("Partially locked") or not compare_with_expected_crop("Icons/Error_Icon.png"):
                sleep(1)
                timeout_check += 1
                if timeout_check > 60:
                    fail_log("Remote lock took longer than 60 seconds so test timed out", "016", img_service)
                    break
            if controller.is_text_present("Partially locked"):
                log("The vehicle was partially locked")
                if controller.wait_for_text("Vehicle is not completely locked"):
                    log("Status correctly displays 'vehicle is not completely locked'")
                else:
                    fail_log("Vehicle is not completely locked", "016", img_service)
                controller.click_by_image("Icons/Error_Icon.png")
    
                # Check what is said in the notif
                check_notif("locked", "016")
            else:
                fail_log("Remote unlock not partially locked", "016", img_service)

    except Exception as e:
        error_log(e, "016", img_service)

def Remote_Lock_Unlock_017():
    try:
        blocked_log("Test blocked - Can't check style guide")
    except Exception as e:
        error_log(e, "017", img_service)