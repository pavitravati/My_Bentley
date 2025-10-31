from time import sleep
from common_utils.android_image_comparision import *
from core.log_emitter import log, fail_log, error_log, metric_log
from common_utils.android_controller import *

img_service = "Remote Lock-Unlock"

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

# ADD A CHECK TO ALOT OF THESE THAT CHECKS IF THE MOST RECENT NOTIF IS WHAT THE TEST CASE JUST DID AND TIMESTAMP IS WITHIN THE MINUTE
# FIX ENTER PIN SO THAT IT DOES IT TILL IT WORKS
# ASK IF WHEN CHECKING NOTIF IF DOING AS A METRIC AND THEN TESTER LOOKS IF NECESSARY
def Remote_Lock_Unlock_001():
    try:
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

def Remote_Lock_Unlock_002():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/unlock_Icon.png")
        sleep(1)
        controller.enter_pin("1234")
        if controller.wait_for_text("Successfully unlocked", timeout=100):
            log("Unlock message displayed")
        else:
            fail_log("Unlock message not displayed", "002", img_service)

        if controller.wait_for_text("Successfully unlocked"):
            log("Unlock notification displayed")
        else:
            fail_log("Unlock notification not displayed", "002", img_service)

        if controller.wait_for_text("Vehicle unlocked"):
            log("Lock status changed")
        else:
            fail_log("Lock status not changed", "002", img_service)

    except Exception as e:
        error_log(e, "002", img_service)

def Remote_Lock_Unlock_003():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/lock_Icon.png")
        sleep(1)
        controller.enter_pin("1234")
        if controller.wait_for_text("Successfully locked", timeout=100):
            log("Lock message displayed")
        else:
            fail_log("Lock message not displayed", "003", img_service)

        if controller.wait_for_text("Successfully locked"):
            log("Lock notification displayed")
        else:
            fail_log("Lock notification not displayed", "002", img_service)

        if controller.wait_for_text("Vehicle locked"):
            log("Lock status changed")
        else:
            fail_log("Lock status not changed", "003", img_service)

    except Exception as e:
        error_log(e, "003", img_service)

# Why all the preconditions?
# def Remote_Lock_Unlock_004():
    # try:
        # controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        #
        # controller.click_by_image("Icons/lock_icon.png")
        # sleep(1)
        # controller.enter_pin("0000")
        # if controller.wait_for_text("Invalid PIN. Please try again."):
        #     print("Remote lock/unlock invalid PIN message displayed")
        # else:
        #     fail_log("Remote lock/unlock invalid PIN message not displayed", "004", img_service)
        #
        # controller.click(500,500)

    # except Exception as e:
    #     error_log(e, "004", img_service)

# For following test cases when refreshing screen the lock/unlock below the buttons does not change an get error at top
# check if this is because of bad wifi, if not find a way to fix
def Remote_Lock_Unlock_005():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

        controller.click_by_image("Icons/lock_icon.png")
        sleep(1)
        controller.enter_pin("1234")
        if controller.wait_for_text("Vehicle could not be locked", timeout=100):
            log("Remote lock blocked when ignition on")
        else:
            fail_log("Remote lock not blocked", "005", img_service)
        controller.click_by_image("Icons/Error_Icon.png")

        if controller.wait_for_text("Vehicle unlocked"):
            log("Lock status unchanged")
        else:
            fail_log("Lock status not unchanged", "005", img_service)

    except Exception as e:
        error_log(e, "005", img_service)

def Remote_Lock_Unlock_006():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

        controller.click_by_image("Icons/unlock_icon.png")
        sleep(1)
        controller.enter_pin("1234")
        if controller.wait_for_text("Vehicle could not be unlocked", timeout=100):
            log("Remote unlock blocked when ignition on")
        else:
            fail_log("Remote lock not blocked", "006", img_service)
        controller.click_by_image("Icons/Error_Icon.png")

        if controller.wait_for_text("Vehicle locked"):
            log("Lock status unchanged")
        else:
            fail_log("Lock status not unchanged", "006", img_service)

    except Exception as e:
        error_log(e, "006", img_service)

def Remote_Lock_Unlock_007():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

        controller.click_by_image("Icons/lock_icon.png")
        sleep(1)
        controller.enter_pin("1234")
        # below has error message is it always going to happen
        # if controller.wait_for_text("Please close the driver's door", timeout=100):
        if controller.wait_for_text("Vehicle could not be locked", timeout=100):
            log("Remote lock blocked when driver's door open")
        else:
            fail_log("Remote lock not blocked", "007", img_service)
        controller.click_by_image("Icons/Error_Icon.png")

        if controller.wait_for_text("Vehicle unlocked"):
            log("Lock status unchanged")
        else:
            fail_log("Lock status not unchanged", "007", img_service)

    except Exception as e:
        error_log(e, "007", img_service)

def Remote_Lock_Unlock_008():
    car = identify_car()
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/lock_icon.png")
        sleep(1)
        controller.enter_pin("1234")
        if controller.wait_for_text("Partially locked", timeout=100):
            log("Remote unlock partially locked")
        else:
            fail_log("Remote unlock not partially locked", "008", img_service)

        if controller.wait_for_text("Vehicle is not completely locked"):
            log("Vehicle is not completely locked")
        else:
            fail_log("Vehicle is not completely locked", "008", img_service)
        controller.click_by_image("Icons/Error_Icon.png")
        sleep(2)
        controller.click_by_image("Icons/New_Notification_icon.png")
        # CHECK IF MOST RECENT NOTIF IS {CAR} LOCKED
        # if controller.is_text_present(f"{car} was successfully locked"):
        #     log("Failed to unlock notification received")
        # else:
        #     fail_log("Failed to unlock notification not received", "008", img_service)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "008", img_service)

def Remote_Lock_Unlock_009():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/New_Notification_icon.png")
        controller.click_by_image("Icons/Notification_icon.png")

        # extract as metrics, pass if there are some fail if none
        log("✅")

    except Exception as e:
        error_log(e, "009", img_service)

def Remote_Lock_Unlock_010():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        latency_time = time.time()
        controller.click_by_image("Icons/lock_icon.png")
        sleep(1)
        controller.enter_pin("1234")
        if controller.wait_for_text("Successfully locked", timeout=100):
            latency_time = time.time() - latency_time
        else:
            raise Exception("Timed out - Car took too long")

        if latency_time < 40:
            log(f"Latency time: {latency_time}")
        else:
            fail_log(f"Latency time: {latency_time}", "010", img_service)

    except Exception as e:
        error_log(e, "010", img_service)

def Remote_Lock_Unlock_011():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/lock_icon.png")
        sleep(1)
        controller.enter_pin("1234")
        if controller.wait_for_text("Successfully locked", timeout=100):
            log("Remote lock worked while locked")
        else:
            fail_log("Remote lock failed while locked", "011", img_service)

    except Exception as e:
        error_log(e, "011", img_service)

def Remote_Lock_Unlock_012():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/unlock_icon.png")
        sleep(1)
        controller.enter_pin("1234")
        if controller.wait_for_text("Successfully unlocked", timeout=100):
            log("Remote unlock worked while unlocked")
        else:
            fail_log("Remote unlock failed while unlocked", "012", img_service)

    except Exception as e:
        error_log(e, "012", img_service)

def Remote_Lock_Unlock_013():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/lock_icon.png")
        sleep(1)
        controller.enter_pin("1234")

        if controller.wait_for_text("Vehicle could not be locked"):
        #check what is in the dump
        # if controller.wait_for_text("Connection failed. Please check your Internet connection. (Error 10.6)"):
            log("Remote lock failed without network connection")
        else:
            fail_log("Remote lock failed without network connection", "013", img_service)

        controller.click_text("Cancel")

    except Exception as e:
        error_log(f"⚠️ - Unexpected error: {e}")

def Remote_Lock_Unlock_014():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/lock_Icon.png")
        sleep(1)
        controller.enter_pin("1234")
        if controller.wait_for_text("Successfully locked", timeout=100):
            log("Lock message displayed when fob key in vehicle")
        else:
            fail_log("Lock message not displayed when fob key in vehicle", "014", img_service)

        if controller.wait_for_text("Vehicle locked"):
            log("Lock status changed")
        else:
            fail_log("Lock status not changed", "014", img_service)

    except Exception as e:
        error_log(e, "014", img_service)

def Remote_Lock_Unlock_015():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/unlock_Icon.png")
        sleep(1)
        controller.enter_pin("1234")
        if controller.wait_for_text("Successfully unlocked", timeout=100):
            log("Unlock message displayed when fob key inside vehicle")
        else:
            fail_log("Unlock message not displayed when fob key inside vehicle", "015", img_service)

        if controller.wait_for_text("Vehicle unlocked"):
            log("Lock status changed")
        else:
            fail_log("Lock status not changed", "015", img_service)

    except Exception as e:
        error_log(e, "015", img_service)

def Remote_Lock_Unlock_016():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/lock_Icon.png")
        sleep(1)
        controller.enter_pin("1234")
        if controller.wait_for_text("Successfully locked", timeout=100):
            log("Lock message displayed when fob key inside vehicle")
        else:
            fail_log("Lock message not displayed when fob key inside vehicle", "016", img_service)

        if controller.wait_for_text("Vehicle locked"):
            log("Lock status changed")
        else:
            fail_log("Lock status not changed", "016", img_service)

    except Exception as e:
        error_log(e, "016", img_service)

# Fix these two, images are not working
def Remote_Lock_Unlock_017():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.swipe_down()
        sleep(5)

        if compare_with_expected_crop("Icons\grey_lock.png"):
            log("Remote lock unlock unavailable when privacy mode activated")
        else:
            fail_log("Remote lock unlock failed to be disabled when privacy mode activated", "017", img_service)

        controller.click_by_image("Icons/Error_Icon.png")

    except Exception as e:
        error_log(e, "017", img_service)

def Remote_Lock_Unlock_018():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.swipe_down()
        sleep(5)

        if compare_with_expected_crop("Icons/Remote_Lock_Available.png"):
            log("Remote lock unlock available when privacy mode deactivated")
        else:
            fail_log("Remote lock unlock failed to be enabled when privacy mode deactivated", "018", img_service)

        controller.click_by_image("Icons/Error_Icon.png")

    except Exception as e:
        error_log(e, "018", img_service)

def Remote_Lock_Unlock_019():
    try:
        log("Cannot check style guide")
    except Exception as e:
        error_log(e, "019", img_service)