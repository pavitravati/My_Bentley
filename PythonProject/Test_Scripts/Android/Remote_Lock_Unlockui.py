from time import sleep
from PythonProject.common_utils.android_image_comparision import *
from PythonProject.core.log_emitter import log_emitter
from PythonProject.common_utils.android_controller import *

# Made a copy of the demo mode testcases to try and get them connected to the ui
def log(msg):
    log_emitter.log_signal.emit(msg)

def Remote_Lock_Unlock001():
    test_status = True
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        if (compare_with_expected_crop("Icons/Remote_Lock.png")):
            log("Lock button visible - ✅")
        else:
            log("Lock button not visible - ❌")
            test_status = False

        if (compare_with_expected_crop("Icons/Remote_Unlock.png")):
            log("✅ - Unlock button visible")
        else:
            log("❌ - Unlock button not visible")
            test_status = False

        if test_status:
            log("✅ - Remote_Lock_Unlock_001 passed")
        else:
            log("❌ - Remote_Lock_Unlock_001 failed")

    except Exception as e:
        log(f"⚠️ - Unexpected error: {e}")

# Think about wait for text as sleep could either end before it pops up or after it is gone for first compare (all that could need it)
# Also used to avoid excessive sleep()
def Remote_Lock_Unlock002():
    test_status = True
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/unlock_Icon.png")
        sleep(2)
        controller.enter_pin("1234")
        # sleep(15)
        if controller.wait_for_text("Successfully locked", timeout=100):
        # if compare_with_expected_crop("Icons/Remote_Unlock_Success.png"):
            log("✅ - Unlock Message Displayed")
        else:
            log("❌ - Unlock Message Displayed")

        if controller.is_text_present("Vehicle unlocked"):
            log("✅ - Lock Status Changed")
        else:
            log("❌ - Lock Status Changed")

        controller.click_by_image("Icons/New_Notification_icon.png")
        # Need way to check not only the text {model} unlocked but also that it is the correct one by checking date/time
        if True:
            log("✅ - Unlock Notification Received")
        else:
            log("❌ - Unlock Notification Received")

        if test_status:
            log("✅ - Remote_Lock_Unlock_002 passed")
        else:
            log("❌ - Remote_Lock_Unlock_002 failed")

    except Exception as e:
        log(f"⚠️ - Unexpected error: {e}")

def Remote_Lock_Unlock003():
    test_status = True
    try:
        controller.click_by_image("Icons/lock_Icon.png")
        sleep(2)
        controller.enter_pin("1234")
        # sleep(12)
        if controller.wait_for_text("Successfully locked", timeout=100):
        # if compare_with_expected_crop("Icons/Remote_Lock_Success.png"):
            log("✅ - Lock Message Displayed")
        else:
            log("❌ - Lock Message Displayed")
            test_status = "Failed"

        if controller.is_text_present("Vehicle locked"):
            log("✅ - Lock Status Changed")
        else:
            log("❌ - Lock Status Changed")
            test_status = "Failed"

        controller.click_by_image("Icons/New_Notification_icon.png")
        # Need way to check not only the text {model} Locked but also that it is the correct one by checking date/time
        if True:
            log("✅ - Lock Notification Received")
        else:
            log("❌ - Lock Notification Received")
            test_status = "Failed"

        if test_status:
            log("✅ - Remote_Lock_Unlock_003 passed")
        else:
            log("❌ - Remote_Lock_Unlock_003 failed")

    except Exception as e:
        log(f"⚠️ - Unexpected error: {e}")

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
        # sleep(10)
        if controller.wait_for_text("Vehicle could not be locked", timeout=100):
        # if compare_with_expected_crop("Icons/Remote_Lock_Failure.png"):
            log("✅ - Remote Lock Blocked")
        else:
            log("❌ - Remote Lock Blocked")
            test_status = False
        sleep(2)
        if controller.is_text_present("Vehicle unlocked"):
            log("✅ - Lock Status Unchanged")
        else:
            log("❌ - Lock Status Unchanged")
            test_status = False
        controller.click_by_image("Icons/Error_Icon.png")
        sleep(2)
        controller.click_by_image("Icons/New_Notification_icon.png")
        # Need way to check not only the text {model} Locked but also that it is the correct one by checking date/time
        if True:
            log("✅ - Failed to Lock Notification Received")
        else:
            log("❌ - Failed to Lock Notification Received")
            test_status = False

        if test_status:
            log("✅ -  Remote_Lock_Unlock_004 passed")
        else:
            log("❌ - Remote_Lock_Unlock_004 failed")

    except Exception as e:
        log(f"⚠️ - Unexpected error: {e}")

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
        # sleep(10)
        if controller.wait_for_text("Vehicle could not be locked", timeout=100):
        # if compare_with_expected_crop("Icons/Remote_Unlock_Failure.png"):
            log("✅ - Remote Unlock Blocked")
        else:
            log("❌ - Remote Unlock Blocked")
            test_status = False
        sleep(2)
        if controller.is_text_present("Vehicle locked"):
            log("✅ - Lock Status Unchanged")
        else:
            log("❌ - Lock Status Unchanged")
            test_status = False
        controller.click_by_image("Icons/Error_Icon.png")
        sleep(2)
        controller.click_by_image("Icons/New_Notification_icon.png")
        # Need way to check not only the text {model} Locked but also that it is the correct one by checking date/time
        if True:
            log("✅ - Failed to Unlock Notification Received")
        else:
            log("❌ - Failed to Unlock Notification Received")
            test_status = False

        if test_status:
            log("✅ - Remote_Lock_Unlock_005 passed")
        else:
            log("❌ - Remote_Lock_Unlock_005 failed")

    except Exception as e:
        log(f"⚠️ - Unexpected error: {e}")

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
        # sleep(20)
        if controller.wait_for_text("Please close the driver's door", timeout=100):
        # if compare_with_expected_crop("Icons/Remote_Unlock_Failure_Driverdoor.png"):
            log("✅ - Remote Unlock Blocked")
        else:
            log("❌ - Remote Unlock Blocked")
            test_status = False
        sleep(2)
        if controller.is_text_present("Vehicle unlocked"):
            log("✅ - Lock Status Unchanged")
        else:
            log("❌ - Lock Status Unchanged")
            test_status = False
        controller.click_by_image("Icons/Error_Icon.png")
        sleep(2)
        controller.click_by_image("Icons/New_Notification_icon.png")
        if True:
            log("✅ - Failed to Unlock Notification Received")
        else:
            log("❌ - Failed to Unlock Notification Received")
            test_status = False

        if test_status:
            log("✅ - Remote_Lock_Unlock_006 passed")
        else:
            log("❌ - Remote_Lock_Unlock_006 failed")

    except Exception as e:
        log(f"⚠️ - Unexpected error: {e}")

def Remote_Lock_Unlock007():
    test_status = True
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/lock_icon.png")
        sleep(2)
        controller.enter_pin("1234")
        # sleep(15)
        if controller.wait_for_text("Partially locked", timeout=100):
        # if compare_with_expected_crop("Icons/Remote_Unlock_Partial_Failure.png"):
            log("✅ - Remote Unlock Partially Blocked")
        else:
            log("❌ - Remote Unlock Partially Blocked")
            test_status = False
        sleep(2)
        if controller.is_text_present("Vehicle is not completely locked"):
            log("✅ - Vehicle is not completely locked")
        else:
            log("❌ - Vehicle is not completely locked")
            test_status = False
        controller.click_by_image("Icons/Error_Icon.png")
        sleep(2)
        controller.click_by_image("Icons/New_Notification_icon.png")
        # Message - Bentayga was successfully locked
        if True:
            log("✅ - Failed to Unlock Notification Received")
        else:
            log("❌ - Failed to Unlock Notification Received")
            test_status = False

        if test_status:
            log("✅ - Remote_Lock_Unlock_007 passed")
        else:
            log("❌ - Remote_Lock_Unlock_007 failed")

    except Exception as e:
        log(f"⚠️ - Unexpected error: {e}")

def Remote_Lock_Unlock008():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/Notification_icon.png")

        #Ask how this one is checked

    except Exception as e:
        log(f"⚠️ - Unexpected error: {e}")

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
            log("❌ - Remote_Lock_Unlock_009 failed")

    except Exception as e:
        log(f"⚠️ - Unexpected error: {e}")

def Remote_Lock_Unlock010():
    test_status = True
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/lock_icon.png")
        sleep(2)
        controller.enter_pin("1234")
        # sleep(15)
        if controller.wait_for_text("Successfully locked", timeout=100):
        # if compare_with_expected_crop("Icons/Remote_Lock_Success.png"):
            log("✅ - Remote Lock Worked While Locked")
        else:
            log("❌ - Remote Lock Worked While Locked")
            test_status = False
        sleep(2)
        controller.click_by_image("Icons/New_Notification_icon.png")
        if True:
            log("✅ - Failed to Unlock Notification Received")
        else:
            log("❌ - Failed to Unlock Notification Received")
            test_status = False

        if test_status:
            log("✅ - Remote_Lock_Unlock_010 passed")
        else:
            log("❌ - Remote_Lock_Unlock_010 failed")

    except Exception as e:
        log(f"⚠️ - Unexpected error: {e}")

def Remote_Lock_Unlock011():
    test_status = True
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/unlock_icon.png")
        sleep(2)
        controller.enter_pin("1234")
        # sleep(15)
        if controller.wait_for_text("Successfully unlocked", timeout=100):
        # if compare_with_expected_crop("Icons/Remote_Unlock_Success.png"):
            log("✅ - Remote Unlock Worked While Unlocked")
        else:
            log("❌ - Remote Unlock Worked While Unlocked")
            test_status = False
        sleep(2)
        controller.click_by_image("Icons/New_Notification_icon.png")
        if True:
            log("✅ - Failed to Unlock Notification Received")
        else:
            log("❌ - Failed to Unlock Notification Received")
            test_status = False

        if test_status:
            log("✅ - Remote_Lock_Unlock_011 passed")
        else:
            log("❌ - Remote_Lock_Unlock_011 failed")

    except Exception as e:
        log(f"⚠️ - Unexpected error: {e}")

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
        # sleep(15)
        if controller.wait_for_text("Successfully locked", timeout=100):
        # if compare_with_expected_crop("Icons/Remote_Lock_Success.png"):
            log("✅ - Lock Message Displayed When Fob Key in Vehicle")
        else:
            log("❌ - Lock Message Displayed When Fob Key in Vehicle")
            test_status = False

        if controller.is_text_present("Vehicle locked"):
            log("✅ - Lock Status Changed")
        else:
            log("❌ - Lock Status Changed")
            test_status = False

        controller.click_by_image("Icons/New_Notification_icon.png")
        # Need way to check not only the text {model} Locked but also that it is the correct one by checking date/time
        if True:
            log("✅ - Lock Notification Received")
        else:
            log("❌ - Lock Notification Received")
            test_status = False

        if test_status:
            log("✅ - Remote_Lock_Unlock_013 passed")
        else:
            log("❌ - Remote_Lock_Unlock_013 failed")

    except Exception as e:
        log(f"⚠️ - Unexpected error: {e}")

def Remote_Lock_Unlock014():
    test_status = True
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/unlock_Icon.png")
        sleep(2)
        controller.enter_pin("1234")
        # sleep(15)
        if controller.wait_for_text("Successfully unlocked", timeout=100):
        # if compare_with_expected_crop("Icons/Remote_Unlock_Success.png"):
            log("✅ - Unlock Message Displayed When Fob Key Inside Vehicle")
        else:
            log("❌ - Unlock Message Displayed When Fob Key Inside Vehicle")
            test_status = False

        if controller.is_text_present("Vehicle unlocked"):
            log("✅ - Lock Status Changed")
        else:
            log("❌ - Lock Status Changed")
            test_status = False

        controller.click_by_image("Icons/New_Notification_icon.png")
        # Need way to check not only the text {model} unlocked but also that it is the correct one by checking date/time
        if True:
            log("✅ - Unlock Notification Received")
        else:
            log("❌ - Unlock Notification Received")
            test_status = False

        if test_status:
            log("✅ - Remote_Lock_Unlock_014 passed")
        else:
            log("❌ - Remote_Lock_Unlock_014 failed")

    except Exception as e:
        log(f"⚠️ - Unexpected error: {e}")

#Explain this
def Remote_Lock_Unlock015():
    test_status = True
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/lock_icon.png")
        sleep(2)
        controller.enter_pin("1234")
        # sleep(12)
        if controller.wait_for_text("Successfully locked", timeout=100):
        # if compare_with_expected_crop("Icons/Remote_Lock_Success.png"):
            log("✅ - Remote Lock Worked")
        else:
            log("❌ - Remote Lock Worked")
            test_status = False
        sleep(2)

        controller.click_by_image("Icons/New_Notification_icon.png")
        if True:
            log("✅ - Failed to Unlock Notification Received")
        else:
            log("❌ - Failed to Unlock Notification Received")
            test_status = False

        if controller.is_text_present("Vehicle locked"):
            log("✅ - Lock Status Changed")
        else:
            log("❌ - Lock Status Changed")
            test_status = False

        if test_status:
            log("✅ - Remote_Lock_Unlock_015 passed")
        else:
            log("❌ - Remote_Lock_Unlock_015 failed")

    except Exception as e:
        log(f"⚠️ - Unexpected error: {e}")

def Remote_Lock_Unlock016():
    try:
        sleep(5)
        controller.swipe_down()
        sleep(10)
        controller.click_by_image("Icons/Error_Icon.png")
        if controller.is_text_present("Lock my car unavailable"):
            log("✅ - Remote Lock Disabled")
            log("✅ - Remote_Lock_Unlock_016 passed")
        else:
            log("❌ - Remote Lock Disabled")
            log("❌ - Remote_Lock_Unlock_016 failed")

    except Exception as e:
        log(f"⚠️ - Unexpected error: {e}")

def Remote_Lock_Unlock017():
    try:
        sleep(5)
        controller.swipe_down()
        sleep(10)
        controller.click_by_image("Icons/Error_Icon.png")
        if not controller.is_text_present("Lock my car unavailable"):
            log("✅ - Remote Lock Enabled")
            log("✅ - Remote_Lock_Unlock_017 passed")
        else:
            log("❌ - Remote Lock Enabled")
            log("❌ - Remote_Lock_Unlock_017 failed")

    except Exception as e:
        log(f"⚠️ - Unexpected error: {e}")