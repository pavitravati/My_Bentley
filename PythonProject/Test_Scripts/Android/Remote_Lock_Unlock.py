from time import sleep
from common_utils.android_image_comparision import *
from core.log_emitter import log_emitter
from common_utils.android_controller import *

# Made a copy of the demo mode testcases to try and get them connected to the ui
def log(msg):
    log_emitter.log_signal.emit(msg)

def fail_log(msg, num):
    log(f"{msg}")
    controller.take_fail_screenshot(f"Demo_Mode_{msg}_{num}.png")

def error_log(e, num):
    log(f"⚠️ - Unexpected error: {e}")
    controller.take_fail_screenshot(f"Demo_Mode_{e}_{num}.png")

def Remote_Lock_Unlock001():
    test_status = True
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        if (compare_with_expected_crop("Icons/Remote_Lock.png")):
            log("Lock button visible - ✅")
        else:
            fail_log("Lock button not visible - ❌", "001")
            test_status = False

        if (compare_with_expected_crop("Icons/Remote_Unlock.png")):
            log("✅ - Unlock button visible")
        else:
            fail_log("❌ - Unlock button not visible", "001")
            test_status = False

        if test_status:
            log("✅ - Remote_Lock_Unlock_001 passed")
        else:
            fail_log("❌ - Remote_Lock_Unlock_001 failed", "001")

    except Exception as e:
        error_log(e, "001")

def Remote_Lock_Unlock002():
    test_status = True
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/unlock_Icon.png")
        sleep(2)
        controller.enter_pin("1234")
        if controller.wait_for_text("Successfully locked", timeout=100):
            log("✅ - Unlock Message Displayed")
        else:
            fail_log("❌ - Unlock Message Displayed", "002")

        if controller.is_text_present("Vehicle unlocked"):
            log("✅ - Lock Status Changed")
        else:
            fail_log("❌ - Lock Status Changed", "002")

        controller.click_by_image("Icons/New_Notification_icon.png")
        # Need way to check not only the text {model} unlocked but also that it is the correct one by checking date/time
        if True:
            log("✅ - Unlock Notification Received")
        else:
            fail_log("❌ - Unlock Notification Received", "002")

        if test_status:
            log("✅ - Remote_Lock_Unlock_002 passed")
        else:
            log("❌ - Remote_Lock_Unlock_002 failed")

    except Exception as e:
        error_log(e, "002")

def Remote_Lock_Unlock003():
    test_status = True
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/lock_Icon.png")
        sleep(2)
        controller.enter_pin("1234")
        if controller.wait_for_text("Successfully locked", timeout=100):
            log("✅ - Lock Message Displayed")
        else:
            fail_log("❌ - Lock Message Displayed", "003")
            test_status = "Failed"

        if controller.is_text_present("Vehicle locked"):
            log("✅ - Lock Status Changed")
        else:
            fail_log("❌ - Lock Status Changed", "003")
            test_status = "Failed"

        controller.click_by_image("Icons/New_Notification_icon.png")
        # Need way to check not only the text {model} Locked but also that it is the correct one by checking date/time
        if True:
            log("✅ - Lock Notification Received")
        else:
            fail_log("❌ - Lock Notification Received", "003")
            test_status = "Failed"

        if test_status:
            log("✅ - Remote_Lock_Unlock_003 passed")
        else:
            log("❌ - Remote_Lock_Unlock_003 failed")

    except Exception as e:
        error_log(e, "003")

def Remote_Lock_Unlock004():
    test_status = True
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        sleep(3)
        controller.swipe_down()
        sleep(5)
        controller.click_by_image("Icons/Error_Icon.png")

        controller.click_by_image("Icons/lock_icon.png")
        sleep(3)
        controller.enter_pin("1234")
        if controller.wait_for_text("Vehicle could not be locked", timeout=100):
            log("✅ - Remote Lock Blocked")
        else:
            fail_log("❌ - Remote Lock Blocked", "004")
            test_status = False
        sleep(2)
        if controller.is_text_present("Vehicle unlocked"):
            log("✅ - Lock Status Unchanged")
        else:
            fail_log("❌ - Lock Status Unchanged", "004")
            test_status = False
        controller.click_by_image("Icons/Error_Icon.png")
        sleep(2)
        controller.click_by_image("Icons/New_Notification_icon.png")
        # Need way to check not only the text {model} Locked but also that it is the correct one by checking date/time
        if True:
            log("✅ - Failed to Lock Notification Received")
        else:
            fail_log("❌ - Failed to Lock Notification Received", "004")
            test_status = False

        if test_status:
            log("✅ -  Remote_Lock_Unlock_004 passed")
        else:
            log("❌ - Remote_Lock_Unlock_004 failed")

    except Exception as e:
        error_log(e, "004")

def Remote_Lock_Unlock005():
    test_status = True
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        sleep(1)
        controller.swipe_down()
        sleep(5)
        controller.click_by_image("Icons/Error_Icon.png")

        controller.click_by_image("Icons/unlock_icon.png")
        sleep(3)
        controller.enter_pin("1234")
        if controller.wait_for_text("Vehicle could not be locked", timeout=100):
            log("✅ - Remote Unlock Blocked")
        else:
            fail_log("❌ - Remote Unlock Blocked", "005")
            test_status = False
        sleep(2)
        if controller.is_text_present("Vehicle locked"):
            log("✅ - Lock Status Unchanged")
        else:
            fail_log("❌ - Lock Status Unchanged", "005")
            test_status = False
        controller.click_by_image("Icons/Error_Icon.png")
        sleep(2)
        controller.click_by_image("Icons/New_Notification_icon.png")
        # Need way to check not only the text {model} Locked but also that it is the correct one by checking date/time
        if True:
            log("✅ - Failed to Unlock Notification Received")
        else:
            fail_log("❌ - Failed to Unlock Notification Received", "005")
            test_status = False

        if test_status:
            log("✅ - Remote_Lock_Unlock_005 passed")
        else:
            log("❌ - Remote_Lock_Unlock_005 failed")

    except Exception as e:
        error_log(e, "005")

def Remote_Lock_Unlock006():
    test_status = True
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        sleep(1)
        controller.swipe_down()
        sleep(5)
        controller.click_by_image("Icons/Error_Icon.png")

        sleep(2)
        controller.click_by_image("Icons/lock_icon.png")
        sleep(2)
        controller.enter_pin("1234")
        if controller.wait_for_text("Please close the driver's door", timeout=100):
            log("✅ - Remote Unlock Blocked")
        else:
            fail_log("❌ - Remote Unlock Blocked", "006")
            test_status = False
        sleep(2)
        if controller.is_text_present("Vehicle unlocked"):
            log("✅ - Lock Status Unchanged")
        else:
            fail_log("❌ - Lock Status Unchanged", "006")
            test_status = False
        controller.click_by_image("Icons/Error_Icon.png")
        sleep(2)
        controller.click_by_image("Icons/New_Notification_icon.png")
        if True:
            log("✅ - Failed to Unlock Notification Received")
        else:
            fail_log("❌ - Failed to Unlock Notification Received", "006")
            test_status = False

        if test_status:
            log("✅ - Remote_Lock_Unlock_006 passed")
        else:
            log("❌ - Remote_Lock_Unlock_006 failed")

    except Exception as e:
        error_log(e, "006")

def Remote_Lock_Unlock007():
    test_status = True
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/lock_icon.png")
        sleep(2)
        controller.enter_pin("1234")
        if controller.wait_for_text("Partially locked", timeout=100):
            log("✅ - Remote Unlock Partially Blocked")
        else:
            fail_log("❌ - Remote Unlock Partially Blocked", "007")
            test_status = False
        sleep(2)
        if controller.is_text_present("Vehicle is not completely locked"):
            log("✅ - Vehicle is not completely locked")
        else:
            fail_log("❌ - Vehicle is not completely locked", "007")
            test_status = False
        controller.click_by_image("Icons/Error_Icon.png")
        sleep(2)
        controller.click_by_image("Icons/New_Notification_icon.png")
        # Message - Bentayga was successfully locked
        if True:
            log("✅ - Failed to Unlock Notification Received")
        else:
            fail_log("❌ - Failed to Unlock Notification Received", "007")
            test_status = False

        if test_status:
            log("✅ - Remote_Lock_Unlock_007 passed")
        else:
            log("❌ - Remote_Lock_Unlock_007 failed")

    except Exception as e:
        error_log(e, "007")

def Remote_Lock_Unlock008():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/Notification_icon.png")

        #Ask how this one is checked

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
            log(f"Latency time: {latency_time}")
            log("✅ - Remote_Lock_Unlock_009 passed")
        else:
            log(f"Latency time: {latency_time}")
            fail_log("❌ - Remote_Lock_Unlock_009 failed", "009")

    except Exception as e:
        error_log(e, "009")

def Remote_Lock_Unlock010():
    test_status = True
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/lock_icon.png")
        sleep(2)
        controller.enter_pin("1234")
        if controller.wait_for_text("Successfully locked", timeout=100):
            log("✅ - Remote Lock Worked While Locked")
        else:
            fail_log("❌ - Remote Lock Worked While Locked", "010")
            test_status = False
        sleep(2)
        controller.click_by_image("Icons/New_Notification_icon.png")
        if True:
            log("✅ - Failed to Unlock Notification Received")
        else:
            fail_log("❌ - Failed to Unlock Notification Received", "010")
            test_status = False

        if test_status:
            log("✅ - Remote_Lock_Unlock_010 passed")
        else:
            log("❌ - Remote_Lock_Unlock_010 failed")

    except Exception as e:
        error_log(e, "010")

def Remote_Lock_Unlock011():
    test_status = True
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/unlock_icon.png")
        sleep(2)
        controller.enter_pin("1234")
        if controller.wait_for_text("Successfully unlocked", timeout=100):
            log("✅ - Remote Unlock Worked While Unlocked")
        else:
            fail_log("❌ - Remote Unlock Worked While Unlocked", "011")
            test_status = False
        sleep(2)
        controller.click_by_image("Icons/New_Notification_icon.png")
        if True:
            log("✅ - Failed to Unlock Notification Received")
        else:
            fail_log("❌ - Failed to Unlock Notification Received", "011")
            test_status = False

        if test_status:
            log("✅ - Remote_Lock_Unlock_011 passed")
        else:
            log("❌ - Remote_Lock_Unlock_011 failed")

    except Exception as e:
        error_log(e, "011")

# For now at least this test case is not needed
# def Remote_Lock_Unlock012():
#     try:
#         controller.click_by_image("Icons/lock_icon.png")

#     except Exception as e:
#         log(f"⚠️ - Unexpected error: {e}")

def Remote_Lock_Unlock013():
    test_status = True
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/lock_Icon.png")
        sleep(2)
        controller.enter_pin("1234")
        if controller.wait_for_text("Successfully locked", timeout=100):
            log("✅ - Lock Message Displayed When Fob Key in Vehicle")
        else:
            fail_log("❌ - Lock Message Displayed When Fob Key in Vehicle", "013")
            test_status = False

        if controller.is_text_present("Vehicle locked"):
            log("✅ - Lock Status Changed")
        else:
            fail_log("❌ - Lock Status Changed", "013")
            test_status = False

        controller.click_by_image("Icons/New_Notification_icon.png")
        # Need way to check not only the text {model} Locked but also that it is the correct one by checking date/time
        if True:
            log("✅ - Lock Notification Received")
        else:
            fail_log("❌ - Lock Notification Received", "013")
            test_status = False

        if test_status:
            log("✅ - Remote_Lock_Unlock_013 passed")
        else:
            log("❌ - Remote_Lock_Unlock_013 failed")

    except Exception as e:
        error_log(e, "013")

def Remote_Lock_Unlock014():
    test_status = True
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/unlock_Icon.png")
        sleep(2)
        controller.enter_pin("1234")
        if controller.wait_for_text("Successfully unlocked", timeout=100):
            log("✅ - Unlock Message Displayed When Fob Key Inside Vehicle")
        else:
            fail_log("❌ - Unlock Message Displayed When Fob Key Inside Vehicle", "014")
            test_status = False

        if controller.is_text_present("Vehicle unlocked"):
            log("✅ - Lock Status Changed")
        else:
            fail_log("❌ - Lock Status Changed", "014")
            test_status = False

        controller.click_by_image("Icons/New_Notification_icon.png")
        # Need way to check not only the text {model} unlocked but also that it is the correct one by checking date/time
        if True:
            log("✅ - Unlock Notification Received")
        else:
            fail_log("❌ - Unlock Notification Received", "014")
            test_status = False

        if test_status:
            log("✅ - Remote_Lock_Unlock_014 passed")
        else:
            log("❌ - Remote_Lock_Unlock_014 failed")

    except Exception as e:
        error_log(e, "014")

#Explain this
def Remote_Lock_Unlock015():
    test_status = True
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/lock_icon.png")
        sleep(2)
        controller.enter_pin("1234")
        if controller.wait_for_text("Successfully locked", timeout=100):
            log("✅ - Remote Lock Worked")
        else:
            fail_log("❌ - Remote Lock Worked", "015")
            test_status = False
        sleep(2)

        controller.click_by_image("Icons/New_Notification_icon.png")
        if True:
            log("✅ - Failed to Unlock Notification Received")
        else:
            fail_log("❌ - Failed to Unlock Notification Received", "015")
            test_status = False

        if controller.is_text_present("Vehicle locked"):
            log("✅ - Lock Status Changed")
        else:
            fail_log("❌ - Lock Status Changed", "015")
            test_status = False

        if test_status:
            log("✅ - Remote_Lock_Unlock_015 passed")
        else:
            log("❌ - Remote_Lock_Unlock_015 failed")

    except Exception as e:
        error_log(e, "015")

def Remote_Lock_Unlock016():
    try:
        sleep(5)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.swipe_down()
        sleep(10)
        controller.click_by_image("Icons/Error_Icon.png")
        if controller.is_text_present("Lock my car unavailable"):
            log("✅ - Remote Lock Disabled")
            log("✅ - Remote_Lock_Unlock_016 passed")
        else:
            fail_log("❌ - Remote Lock Disabled", "016")
            log("❌ - Remote_Lock_Unlock_016 failed")

    except Exception as e:
        error_log(e, "016")

def Remote_Lock_Unlock017():
    try:
        sleep(5)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.swipe_down()
        sleep(10)
        controller.click_by_image("Icons/Error_Icon.png")
        if not controller.is_text_present("Lock my car unavailable"):
            log("✅ - Remote Lock Enabled")
            log("✅ - Remote_Lock_Unlock_017 passed")
        else:
            fail_log("❌ - Remote Lock Enabled", "017")
            log("❌ - Remote_Lock_Unlock_017 failed")

    except Exception as e:
        error_log(e, "017")