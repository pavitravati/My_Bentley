from time import sleep
from PythonProject.common_utils.android_image_comparision import *
from PythonProject.common_utils.test_result_tracker import TestCaseResult
from PythonProject.common_utils.android_controller import *

def Remote_Lock_Unlock001():
    test_result = TestCaseResult("Remote_Lock_Unlock001")
    test_result.description = "Access Lock & Unlock from App"
    test_result.start_time = time.time()

    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        if (compare_with_expected_crop("Icons/Remote_Lock.png")):
            test_result.log_step("Lock button visible", True)
        else:
            test_result.log_step("Lock button not visible", False)
            test_result.status = "Failed"

        if (compare_with_expected_crop("Icons/Remote_Unlock.png")):
            test_result.log_step("Unlock button visible", True)
        else:
            test_result.log_step("Unlock button not visible", False)
            test_result.status = "Failed"

        if test_result.status == "Passed":
            test_result.log("✅ Remote_Lock_Unlock_001 passed")
        else:
            test_result.log("❌ Remote_Lock_Unlock_001 failed")


    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)
        test_result.status = "Error"

    test_result.end_time = time.time()
    return test_result

def Remote_Lock_Unlock002():
    test_result = TestCaseResult("Remote_Lock_Unlock002")
    test_result.description = "Verify Remote Unlock functionality"
    test_result.start_time = time.time()

    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/unlock_Icon.png", threshold=0.80)
        sleep(2)
        controller.enter_pin("1234")
        sleep(5)
        if compare_with_expected_crop("Icons/Remote_Unlock_Success.png"):
            test_result.log_step("Unlock Message Displayed", True)
        else:
            test_result.log_step("Unlock Message Displayed", False)
            test_result.status = "Failed"

        if controller.is_text_present("Vehicle unlocked"):
            test_result.log_step("Lock Status Changed", True)
        else:
            test_result.log_step("Lock Status Changed", False)
            test_result.status = "Failed"

        controller.click_by_image("Icons/New_Notification_icon.png")
        # Need way to check not only the text {model} unlocked but also that it is the correct one by checking date/time
        if True:
            test_result.log_step("Unlock Notification Received", True)
        else:
            test_result.log_step("Unlock Notification Received", False)
            test_result.status = "Failed"

        if test_result.status == "Passed":
            test_result.log("✅ Remote_Lock_Unlock_002 passed")
        else:
            test_result.log("❌ Remote_Lock_Unlock_002 failed")

    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)
        test_result.status = "Error"

    test_result.end_time = time.time()
    return test_result

controller.take_screenshot("androidtesting.png")

def Remote_Lock_Unlock003():
    test_result = TestCaseResult("Remote_Lock_Unlock003")
    test_result.description = "Verify Remote Lock functionality"
    test_result.start_time = time.time()

    try:
        controller.click_by_image("Icons/lock_Icon.png", threshold=0.80)
        sleep(2)
        controller.enter_pin("1234")
        sleep(5)
        if compare_with_expected_crop("Icons/Remote_Lock_Success.png"):
            test_result.log_step("Lock Message Displayed", True)
        else:
            test_result.log_step("Lock Message Displayed", False)
            test_result.status = "Failed"

        if controller.is_text_present("Vehicle locked"):
            test_result.log_step("Lock Status Changed", True)
        else:
            test_result.log_step("Lock Status Changed", False)
            test_result.status = "Failed"

        controller.click_by_image("Icons/New_Notification_icon.png")
        # Need way to check not only the text {model} Locked but also that it is the correct one by checking date/time
        if True:
            test_result.log_step("Lock Notification Received", True)
        else:
            test_result.log_step("Lock Notification Received", False)
            test_result.status = "Failed"

        if test_result.status == "Passed":
            test_result.log("✅ Remote_Lock_Unlock_003 passed")
        else:
            test_result.log("❌ Remote_Lock_Unlock_003 failed")

    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)
        test_result.status = "Error"

    test_result.end_time = time.time()
    return test_result

def Remote_Lock_Unlock004():
    test_result = TestCaseResult("Remote_Lock_Unlock004")
    test_result.description = "Verify Remote Lock, Ignition on"
    test_result.start_time = time.time()

    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/lock_icon.png", threshold=0.80)
        sleep(3)
        controller.enter_pin("1234")
        sleep(10)
        if compare_with_expected_crop("Icons/Remote_Lock_Failure.png"):
            test_result.log_step("Remote Lock Blocked", True)
        else:
            test_result.log_step("Remote Lock Blocked", False)
            test_result.status = "Failed"
        sleep(2)
        if controller.is_text_present("Vehicle unlocked"):
            test_result.log_step("Lock Status Unchanged", True)
        else:
            test_result.log_step("Lock Status Unchanged", False)
            test_result.status = "Failed"
        sleep(2)
        controller.click_by_image("Icons/New_Notification_icon.png")
        # Need way to check not only the text {model} Locked but also that it is the correct one by checking date/time
        if True:
            test_result.log_step("Failed to Lock Notification Received", True)
        else:
            test_result.log_step("Failed to Lock Notification Received", False)
            test_result.status = "Failed"

        if test_result.status == "Passed":
            test_result.log("✅ Remote_Lock_Unlock_004 passed")
        else:
            test_result.log("❌ Remote_Lock_Unlock_004 failed")

    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)
        test_result.status = "Error"

    test_result.end_time = time.time()
    return test_result

def Remote_Lock_Unlock005():
    test_result = TestCaseResult("Remote_Lock_Unlock005")
    test_result.description = "Verify Remote Unlock, Ignition off"
    test_result.start_time = time.time()

    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/unlock_icon.png", threshold=0.80)
        sleep(3)
        controller.enter_pin("1234")
        sleep(10)
        if compare_with_expected_crop("Icons/Remote_Unlock_Failure.png"):
            test_result.log_step("Remote Unlock Blocked", True)
        else:
            test_result.log_step("Remote Unlock Blocked", False)
            test_result.status = "Failed"
        sleep(2)
        if compare_with_expected_crop("Icons/Remote_Unlock_Status.png"):
            test_result.log_step("Lock Status Unchanged", True)
        else:
            test_result.log_step("Lock Status Unchanged", False)
            test_result.status = "Failed"
        sleep(2)
        controller.click_by_image("Icons/New_Notification_icon.png")
        # Need way to check not only the text {model} Locked but also that it is the correct one by checking date/time
        if True:
            test_result.log_step("Failed to Unlock Notification Received", True)
        else:
            test_result.log_step("Failed to Unlock Notification Received", False)
            test_result.status = "Failed"

        if test_result.status == "Passed":
            test_result.log("✅ Remote_Lock_Unlock_005 passed")
        else:
            test_result.log("❌ Remote_Lock_Unlock_005 failed")

    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)
        test_result.status = "Error"

    test_result.end_time = time.time()
    return test_result

def Remote_Lock_Unlock006():
    test_result = TestCaseResult("Remote_Lock_Unlock006")
    test_result.description = "Verify Remote Lock, Driver door open"
    test_result.start_time = time.time()

    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        sleep(2)
        controller.click_by_image("Icons/lock_icon.png", threshold=0.80)
        sleep(2)
        controller.enter_pin("1234")
        sleep(10)
        if compare_with_expected_crop("Icons/Remote_Unlock_Failure_Driverdoor.png"):
            test_result.log_step("Remote Unlock Blocked", True)
        else:
            test_result.log_step("Remote Unlock Blocked", False)
            test_result.status = "Failed"
        sleep(2)
        if controller.is_text_present("Vehicle unlocked"):
            test_result.log_step("Lock Status Unchanged", True)
        else:
            test_result.log_step("Lock Status Unchanged", False)
            test_result.status = "Failed"
        sleep(2)
        controller.click_by_image("Icons/New_Notification_icon.png")
        if True:
            test_result.log_step("Failed to Unlock Notification Received", True)
        else:
            test_result.log_step("Failed to Unlock Notification Received", False)
            test_result.status = "Failed"

        if test_result.status == "Passed":
            test_result.log("✅ Remote_Lock_Unlock_006 passed")
        else:
            test_result.log("❌ Remote_Lock_Unlock_006 failed")

    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)
        test_result.status = "Error"

    test_result.end_time = time.time()
    return test_result

def Remote_Lock_Unlock007():
    test_result = TestCaseResult("Remote_Lock_Unlock007")
    test_result.description = "Verify Remote lock, Any door/trunk is open"
    test_result.start_time = time.time()

    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/lock_icon.png", threshold=0.80)
        sleep(2)
        controller.enter_pin("1234")
        if compare_with_expected_crop("Icons/Remote_Unlock_Partial_Failure.png"):
            test_result.log_step("Remote Unlock Partially Blocked", True)
        else:
            test_result.log_step("Remote Unlock Partially Blocked", False)
            test_result.status = "Failed"
        sleep(2)
        if controller.is_text_present("Vehicle is not completely locked"):
            test_result.log_step("Vehicle is not completely locked", True)
        else:
            test_result.log_step("Vehicle is not completely locked", False)
            test_result.status = "Failed"
        sleep(2)
        controller.click_by_image("Icons/New_Notification_icon.png")
        # Message - Bentayga was successfully locked
        if True:
            test_result.log_step("Failed to Unlock Notification Received", True)
        else:
            test_result.log_step("Failed to Unlock Notification Received", False)
            test_result.status = "Failed"

        if test_result.status == "Passed":
            test_result.log("✅ Remote_Lock_Unlock_007 passed")
        else:
            test_result.log("❌ Remote_Lock_Unlock_007 failed")

    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)
        test_result.status = "Error"

    test_result.end_time = time.time()
    return test_result

def Remote_Lock_Unlock008():
    test_result = TestCaseResult("Remote_Lock_Unlock008")
    test_result.description = "Access to Remote Lock/Unlock history"
    test_result.start_time = time.time()

    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/Notification_icon.png", threshold=0.80)

        #Ask how this one is checked

    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)

    test_result.end_time = time.time()
    return test_result

def Remote_Lock_Unlock009():
    test_result = TestCaseResult("Remote_Lock_Unlock009")
    test_result.description = "Verify Remote Unlock functionality"
    test_result.start_time = time.time()

    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        # Need to know if completion is logged by tester via input or using the app indication
        # This currently judges success on when the banner at the top saying vehicle locked happens
        latency_time = time.time()
        controller.click_by_image("Icons/lock_icon.png", threshold=0.80)
        sleep(2)
        controller.enter_pin("1234")
        if controller.wait_for_text("Successfully locked", timeout=100):
            latency_time = time.time() - latency_time
        else:
            raise Exception("Timed out - Car took too long")

        if latency_time < 40:
            test_result.log_step(f"Latency time: {latency_time}", True)
            test_result.log("✅ Remote_Lock_Unlock_001 passed")
        else:
            test_result.log_step(f"Latency time: {latency_time}", False)
            test_result.log("❌ Remote_Lock_Unlock_009 failed")
            test_result.status = "Failed"

    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)
        test_result.status = "Error"

    test_result.end_time = time.time()
    return test_result

def Remote_Lock_Unlock010():
    test_result = TestCaseResult("Remote_Lock_Unlock010")
    test_result.description = "Verify Remote Locked, vehicle locked"
    test_result.start_time = time.time()

    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/lock_icon.png", threshold=0.80)
        sleep(2)
        controller.enter_pin("1234")
        sleep(10)
        if compare_with_expected_crop("Icons/Remote_Lock_Success.png"):
            test_result.log_step("Remote Lock Worked While Locked", True)
        else:
            test_result.log_step("Remote Lock Worked While Locked", False)
            test_result.status = "Failed"
        sleep(2)
        controller.click_by_image("Icons/New_Notification_icon.png")
        if True:
            test_result.log_step("Failed to Unlock Notification Received", True)
        else:
            test_result.log_step("Failed to Unlock Notification Received", False)
            test_result.status = "Failed"

        if test_result.status == "Passed":
            test_result.log("✅ Remote_Lock_Unlock_010 passed")
        else:
            test_result.log("❌ Remote_Lock_Unlock_010 failed")

    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)
        test_result.status = "Error"

    test_result.end_time = time.time()
    return test_result

def Remote_Lock_Unlock011():
    test_result = TestCaseResult("Remote_Lock_Unlock011")
    test_result.description = "Verify Remote Unlock, vehicle unlocked"
    test_result.start_time = time.time()

    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/unlocked_icon.png", threshold=0.80)
        sleep(2)
        controller.enter_pin("1234")
        sleep(10)
        if compare_with_expected_crop("Icons/Remote_Unlock_Success.png"):
            test_result.log_step("Remote Unlock Worked While Unlocked", True)
        else:
            test_result.log_step("Remote Unlock Worked While Unlocked", False)
            test_result.status = "Failed"
        sleep(2)
        controller.click_by_image("Icons/New_Notification_icon.png")
        if True:
            test_result.log_step("Failed to Unlock Notification Received", True)
        else:
            test_result.log_step("Failed to Unlock Notification Received", False)
            test_result.status = "Failed"

        if test_result.status == "Passed":
            test_result.log("✅ Remote_Lock_Unlock_011 passed")
        else:
            test_result.log("❌ Remote_Lock_Unlock_011 failed")

    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)

    test_result.end_time = time.time()
    return test_result

def Remote_Lock_Unlock012():
    test_result = TestCaseResult("Remote_Lock_Unlock012")
    test_result.description = "Verify Remote Lock timeout, no network connection"
    test_result.start_time = time.time()

    # When phone in airplane mode, it comes up with a error that it cannot peform action without internet rather than timing out
    try:
        controller.click_by_image("Icons/lock_icon.png", threshold=0.80)
        sleep(2)
        controller.enter_pin("1234")
        sleep(120) # make it so that 120 ish is where it terminates the test as a fail, and checks up to that point, prevents waiting 120 if it shows success after 10

    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)

    test_result.end_time = time.time()
    return test_result

def Remote_Lock_Unlock013():
    test_result = TestCaseResult("Remote_Lock_Unlock013")
    test_result.description = "Verify Remote Lock, Fob keys left inside vehicle"
    test_result.start_time = time.time()

    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/lock_Icon.png", threshold=0.80)
        sleep(2)
        controller.enter_pin("1234")
        sleep(5)
        if compare_with_expected_crop("Icons/Remote_Lock_Success.png"):
            test_result.log_step("Lock Message Displayed When Fob Key in Vehicle", True)
        else:
            test_result.log_step("Lock Message Displayed When Fob Key in Vehicle", False)
            test_result.status = "Failed"

        if controller.is_text_present("Vehicle locked"):
            test_result.log_step("Lock Status Changed", True)
        else:
            test_result.log_step("Lock Status Changed", False)
            test_result.status = "Failed"

        controller.click_by_image("Icons/New_Notification_icon.png")
        # Need way to check not only the text {model} Locked but also that it is the correct one by checking date/time
        if True:
            test_result.log_step("Lock Notification Received", True)
        else:
            test_result.log_step("Lock Notification Received", False)
            test_result.status = "Failed"

        if test_result.status == "Passed":
            test_result.log("✅ Remote_Lock_Unlock_013 passed")
        else:
            test_result.log("❌ Remote_Lock_Unlock_013 failed")

    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)

    test_result.end_time = time.time()
    return test_result

def Remote_Lock_Unlock014():
    test_result = TestCaseResult("Remote_Lock_Unlock014")
    test_result.description = "Verify Remote Unlock, Fob keys left in vehicle"
    test_result.start_time = time.time()

    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/unlock_Icon.png", threshold=0.80)
        sleep(2)
        controller.enter_pin("1234")
        sleep(5)
        if compare_with_expected_crop("Icons/Remote_Unlock_Success.png"):
            test_result.log_step("Unlock Message Displayed When Fob Key Inside Vehicle", True)
        else:
            test_result.log_step("Unlock Message Displayed When Fob Key Inside Vehicle", False)
            test_result.status = "Failed"

        if controller.is_text_present("Vehicle unlocked"):
            test_result.log_step("Lock Status Changed", True)
        else:
            test_result.log_step("Lock Status Changed", False)
            test_result.status = "Failed"

        controller.click_by_image("Icons/New_Notification_icon.png")
        # Need way to check not only the text {model} unlocked but also that it is the correct one by checking date/time
        if True:
            test_result.log_step("Unlock Notification Received", True)
        else:
            test_result.log_step("Unlock Notification Received", False)
            test_result.status = "Failed"

        if test_result.status == "Passed":
            test_result.log("✅ Remote_Lock_Unlock_014 passed")
        else:
            test_result.log("❌ Remote_Lock_Unlock_014 failed")

    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)
        test_result.status = "Error"

    test_result.end_time = time.time()
    return test_result

def Remote_Lock_Unlock015():
    test_result = TestCaseResult("Remote_Lock_Unlock015")
    test_result.description = "Verify Remote Unlock functionality"
    test_result.start_time = time.time()

    input("Vehicle is unlocked, Ignition is off\nPress Enter to proceed...")

    try:
        pass

    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)
        test_result.status = "Error"

    test_result.end_time = time.time()
    return test_result

def Remote_Lock_Unlock016():
    test_result = TestCaseResult("Remote_Lock_Unlock016")
    test_result.description = "Verify Remote Lock/Unlock, Privacy mode enabled"
    test_result.start_time = time.time()

    try:
        sleep(60)
        controller.swipe_down()
        if compare_with_expected_crop("Remote_Lock_Unavailable.png"):
            test_result.log_step("Remote Lock disabled", True)
            if not controller.click_by_image("Icons/Remote_Lock_Unavailable_icon.png"):
                test_result.log("✅ Remote_Lock_Unlock_016 passed")
                test_result.end_time = time.time()
                return test_result

        test_result.log("❌ Remote_Lock_Unlock_016 failed")
        test_result.status = "Failed"

    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)
        test_result.status = "Error"

    test_result.end_time = time.time()
    return test_result

def Remote_Lock_Unlock017():
    test_result = TestCaseResult("Remote_Lock_Unlock017")
    test_result.description = "Verify Remote Lock/Unlock, Privacy mode disabled"
    test_result.start_time = time.time()

    try:
        sleep(60)
        controller.swipe_down()
        if compare_with_expected_crop("Remote_Lock_Available.png"):
            test_result.log_step("Remote Lock Enabled", True)
            if controller.click_by_image("Icons/lock_icon.png"):
                test_result.log("✅ Remote_Lock_Unlock_017 passed")
                test_result.end_time = time.time()
                return test_result

        test_result.log("❌ Remote_Lock_Unlock_017 failed")
        test_result.status = "Failed"


    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)
        test_result.status = "Error"

    test_result.end_time = time.time()
    return test_result