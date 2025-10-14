from time import sleep
from common_utils.android_image_comparision import *
from core.log_emitter import log_emitter
from common_utils.android_controller import *

# Made a copy of the demo mode testcases to try and get them connected to the ui
def log(msg):
    log_emitter.log_signal.emit(msg)

def fail_log(msg, num):
    log(f"{msg}")
    controller.take_fail_screenshot(f"Remote_Lock_Unlock-{msg}-{num}.png")

def error_log(e, num):
    log(f"⚠️ - Unexpected error: {e}")
    controller.take_fail_screenshot(f"Remote_Lock_Unlock-{e}-{num}.png")

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

def Remote_Lock_Unlock001():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        if (compare_with_expected_crop("Icons/Remote_Lock.png")):
            log("✅ -  button visible")
        else:
            fail_log("❌ - Lock button not visible", "001")

        if (compare_with_expected_crop("Icons/Remote_Unlock.png")):
            log("✅ - Unlock button visible")
        else:
            fail_log("❌ - Unlock button not visible", "001")

    except Exception as e:
        error_log(e, "001")

def Remote_Lock_Unlock002():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/unlock_Icon.png")
        sleep(2)
        controller.enter_pin("1234")
        if controller.wait_for_text("Successfully locked", timeout=100):
            log("✅ - Unlock message displayed")
        else:
            fail_log("❌ - Unlock message not displayed", "002")

        if controller.is_text_present("Vehicle unlocked"):
            log("✅ - Lock status changed")
        else:
            fail_log("❌ - Lock status not changed", "002")

        if controller.wait_for_text("Successfully unlocked"):
            log("✅ - Unlock notification displayed")
        else:
            fail_log("❌ - Unlock notification not displayed", "002")

    except Exception as e:
        error_log(e, "002")

def Remote_Lock_Unlock003():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/lock_Icon.png")
        sleep(2)
        controller.enter_pin("1234")
        if controller.wait_for_text("Successfully locked", timeout=100):
            log("✅ - Lock message displayed")
        else:
            fail_log("❌ - Lock message not displayed", "003")

        if controller.is_text_present("Vehicle locked"):
            log("✅ - Lock status changed")
        else:
            fail_log("❌ - Lock status not changed", "003")

        if controller.wait_for_text("Successfully locked"):
            log("✅ - Lock notification displayed")
        else:
            fail_log("❌ - Lock notification not displayed", "002")

    except Exception as e:
        error_log(e, "003")

def Remote_Lock_Unlock004():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

        controller.click_by_image("Icons/lock_icon.png")
        sleep(2)
        controller.enter_pin("1234")
        if controller.wait_for_text("Vehicle could not be locked", timeout=100):
            log("✅ - Remote lock blocked")
        else:
            fail_log("❌ - Remote lock not blocked", "004")
        sleep(2)
        if controller.is_text_present("Vehicle unlocked"):
            log("✅ - Lock status unchanged")
        else:
            fail_log("❌ - Lock status not unchanged", "004")
        controller.click_by_image("Icons/Error_Icon.png")
        sleep(2)

    except Exception as e:
        error_log(e, "004")

def Remote_Lock_Unlock005():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

        controller.click_by_image("Icons/unlock_icon.png")
        sleep(2)
        controller.enter_pin("1234")
        if controller.wait_for_text("Vehicle could not be locked", timeout=100):
            log("✅ - Remote unlock blocked")
        else:
            fail_log("❌ - Remote unlock not blocked", "005")
        sleep(2)
        if controller.is_text_present("Vehicle locked"):
            log("✅ - Lock status unchanged")
        else:
            fail_log("❌ - Lock status not unchanged", "005")
        controller.click_by_image("Icons/Error_Icon.png")

    except Exception as e:
        error_log(e, "005")

def Remote_Lock_Unlock006():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

        controller.click_by_image("Icons/lock_icon.png")
        sleep(2)
        controller.enter_pin("1234")
        if controller.wait_for_text("Please close the driver's door", timeout=100):
            log("✅ - Remote unlock blocked")
        else:
            fail_log("❌ - Remote unlock not blocked", "006")
        sleep(2)
        if controller.is_text_present("Vehicle unlocked"):
            log("✅ - Lock status unchanged")
        else:
            fail_log("❌ - Lock status not unchanged", "006")
        controller.click_by_image("Icons/Error_Icon.png")

    except Exception as e:
        error_log(e, "006")

def Remote_Lock_Unlock007():
    car = identify_car()
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/lock_icon.png")
        sleep(2)
        controller.enter_pin("1234")
        if controller.wait_for_text("Partially locked", timeout=100):
            log("✅ - Remote unlock partially blocked")
        else:
            fail_log("❌ - Remote unlock not partially blocked", "007")
        sleep(2)
        if controller.is_text_present("Vehicle is not completely locked"):
            log("✅ - Vehicle is not completely locked")
        else:
            fail_log("❌ - Vehicle is not completely locked", "007")
        controller.click_by_image("Icons/Error_Icon.png")
        sleep(2)
        controller.click_by_image("Icons/New_Notification_icon.png")
        # CHECK THIS IS CORRECT
        if controller.is_text_present(f"{car} was successfully locked"):
            log("✅ - Failed to unlock notification received")
        else:
            fail_log("❌ - Failed to unlock notification not received", "007")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "007")

def Remote_Lock_Unlock008():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/New_Notification_icon.png")
        controller.click_by_image("Icons/Notification_icon.png")

        # Check if the lock and unlocks done so far in previous test cases on this run are there

    except Exception as e:
        error_log(e, "008")

def Remote_Lock_Unlock009():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        latency_time = time.time()
        controller.click_by_image("Icons/lock_icon.png")
        sleep(2)
        controller.enter_pin("1234")
        if controller.wait_for_text("Successfully locked", timeout=100):
            latency_time = time.time() - latency_time
        else:
            raise Exception("Timed out - Car took too long")

        if latency_time < 40:
            log(f"✅ - Latency time: {latency_time}")
        else:
            fail_log(f"❌ - Latency time: {latency_time}", "009")

    except Exception as e:
        error_log(e, "009")

def Remote_Lock_Unlock010():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/lock_icon.png")
        sleep(2)
        controller.enter_pin("1234")
        if controller.wait_for_text("Successfully locked", timeout=100):
            log("✅ - Remote lock worked while locked")
        else:
            fail_log("❌ - Remote lock failed while locked", "010")

    except Exception as e:
        error_log(e, "010")

def Remote_Lock_Unlock011():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/unlock_icon.png")
        sleep(2)
        controller.enter_pin("1234")
        if controller.wait_for_text("Successfully unlocked", timeout=100):
            log("✅ - Remote unlock worked while unlocked")
        else:
            fail_log("❌ - Remote unlock failed while unlocked", "011")

    except Exception as e:
        error_log(e, "011")

# For now at least this test case is not needed
# def Remote_Lock_Unlock012():
#     try:
#         controller.click_by_image("Icons/lock_icon.png")

#     except Exception as e:
#         log(f"⚠️ - Unexpected error: {e}")

def Remote_Lock_Unlock013():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/lock_Icon.png")
        sleep(2)
        controller.enter_pin("1234")
        if controller.wait_for_text("Successfully locked", timeout=100):
            log("✅ - Lock message displayed when fob key in vehicle")
        else:
            fail_log("❌ - Lock message not displayed when fob key in vehicle", "013")

        if controller.is_text_present("Vehicle locked"):
            log("✅ - Lock status changed")
        else:
            fail_log("❌ - Lock status not changed", "013")

    except Exception as e:
        error_log(e, "013")

def Remote_Lock_Unlock014():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/unlock_Icon.png")
        sleep(2)
        controller.enter_pin("1234")
        if controller.wait_for_text("Successfully unlocked", timeout=100):
            log("✅ - Unlock message displayed when fob key inside vehicle")
        else:
            fail_log("❌ - Unlock message not displayed when fob key inside vehicle", "014")

        if controller.is_text_present("Vehicle unlocked"):
            log("✅ - Lock status changed")
        else:
            fail_log("❌ - Lock status not changed", "014")

    except Exception as e:
        error_log(e, "014")

#Explain this
def Remote_Lock_Unlock015():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/lock_icon.png")
        sleep(2)
        controller.enter_pin("1234")
        if controller.wait_for_text("Successfully locked", timeout=100):
            log("✅ - Remote lock worked")
        else:
            fail_log("❌ - Remote lock failed", "015")

        if controller.is_text_present("Vehicle locked"):
            log("✅ - Lock status changed")
        else:
            fail_log("❌ - Lock status not changed", "015")

    except Exception as e:
        error_log(e, "015")

def Remote_Lock_Unlock016():
    try:
        sleep(5)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        if controller.is_text_present("Lock my car unavailable"):
            log("✅ - Remote lock disabled")
        else:
            fail_log("❌ - Remote lock not disabled", "016")

    except Exception as e:
        error_log(e, "016")

def Remote_Lock_Unlock017():
    try:
        sleep(5)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        if not controller.is_text_present("Lock my car unavailable"):
            log("✅ - Remote lock enabled")
        else:
            fail_log("❌ - Remote lock enabled", "017")

    except Exception as e:
        error_log(e, "017")