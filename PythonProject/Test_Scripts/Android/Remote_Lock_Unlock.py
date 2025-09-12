from time import sleep
from PythonProject.common_utils.android_image_comparision import *
from PythonProject.common_utils.test_result_tracker import TestCaseResult
from PythonProject.common_utils.android_controller import *

def Remote_Lock_Unlock001():
    test_result = TestCaseResult("Remote_Lock_Unlock001")
    test_result.description = "Access Lock & Unlock from App"
    test_result.start_time = time.time()
    test_passed = True  # ✅ Initialize test flag

    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        if (compare_with_expected_crop("Icons/Remote_Lock.png")):
            test_result.log_step("Lock button visible", True)
        else:
            test_result.log_step("Lock button not visible", False)
            test_passed = False

        if (compare_with_expected_crop("Icons/Remote_Unlock.png")):
            test_result.log_step("Unlock button visible", True)
        else:
            test_result.log_step("Unlock button not visible", False)
            test_passed = False

        if (test_passed):
            test_result.log("✅ Remote_Lock_Unlock_001 passed")
        else:
            test_result.log("❌ Remote_Lock_Unlock_001 failed")
            test_result.status = "Failed"


    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)
        test_result.status = "Error"

    test_result.end_time = time.time()
    return test_result

def Remote_Lock_Unlock002():
    test_result = TestCaseResult("Remote_Lock_Unlock002")
    test_result.description = "Verify Remote Unlock functionality"
    test_result.start_time = time.time()

    input("All doors are closed, Vehicle is locked\nPress Enter to proceed...")

    try:
        controller.click_by_image("Icons/unlock_Icon.png", threshold=0.80)
        sleep(2)
        controller.enter_pin("1234")

        # do in vehicle and test that it does everything correctly

    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)
        test_result.status = "Error"

    test_result.end_time = time.time()
    return test_result

def Remote_Lock_Unlock003():
    test_result = TestCaseResult("Remote_Lock_Unlock003")
    test_result.description = "Verify Remote Lock functionality"
    test_result.start_time = time.time()

    input("All doors are closed, Vehicle is unlocked\nPress Enter to proceed...")

    try:
        # if compare_with_expected_crop("Icons/Vehicle_Unlocked.png"):
        #     controller.swipe_up()
        #     metrics = controller.extract_dashboard_metrics()
        #     controller.swipe_down()
        #     if metrics["Doors"] != "Closed":
        #         test_result.log_step("Doors Open", False)
        #         test_result.status = "Failed"
        #         test_result.end_time = time.time()
        #         return test_result
        # else:
        #     test_result.log_step("Vehicle not locked", False)
        #     test_result.status = "Failed"
        #     test_result.end_time = time.time()
        #     return test_result

        controller.click_by_image("Icons/lock_icon.png", threshold=0.80)
        sleep(2)
        controller.enter_pin("1234")

        # do in vehicle and test that it does everything correctly

    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)
        test_result.status = "Error"

    test_result.end_time = time.time()
    return test_result

def Remote_Lock_Unlock004():
    test_result = TestCaseResult("Remote_Lock_Unlock004")
    test_result.description = "Verify Remote Lock, Ignition on"
    test_result.start_time = time.time()

    input("All doors are closed, Vehicle is unlocked, Ignition is on\nPress Enter to proceed...")

    try:
        controller.click_by_image("Icons/lock_icon.png", threshold=0.80)
        sleep(2)
        controller.enter_pin("1234")

        # do in vehicle and test that it does everything correctly

    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)
        test_result.status = "Error"

    test_result.end_time = time.time()
    return test_result

def Remote_Lock_Unlock005():
    test_result = TestCaseResult("Remote_Lock_Unlock005")
    test_result.description = "Verify Remote Unlock, Ignition off"
    test_result.start_time = time.time()

    input("All doors are closed, Vehicle is locked, Ignition is on\nPress Enter to proceed...")

    try:
        controller.click_by_image("Icons/unlock_icon.png", threshold=0.80)
        sleep(2)
        controller.enter_pin("1234")

        # do in vehicle and test that it does everything correctly

    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)
        test_result.status = "Error"

    test_result.end_time = time.time()
    return test_result

def Remote_Lock_Unlock006():
    test_result = TestCaseResult("Remote_Lock_Unlock006")
    test_result.description = "Verify Remote Lock, Driver door open"
    test_result.start_time = time.time()

    input("Driver door open rest closed, Vehicle is unlocked, Ignition is off\nPress Enter to proceed...")

    try:
        controller.click_by_image("Icons/lock_icon.png", threshold=0.80)
        sleep(2)
        controller.enter_pin("1234")

    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)
        test_result.status = "Error"

    test_result.end_time = time.time()
    return test_result

def Remote_Lock_Unlock007():
    test_result = TestCaseResult("Remote_Lock_Unlock007")
    test_result.description = "Verify Remote lock, Any door/trunk is open"
    test_result.start_time = time.time()

    input("A door/bonnet is open other than driver door, Vehicle is unlocked, Ignition is on\nPress Enter to proceed...")

    try:
        controller.click_by_image("Icons/lock_icon.png", threshold=0.80)
        sleep(2)
        controller.enter_pin("1234")

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

    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)

    test_result.end_time = time.time()
    return test_result

def Remote_Lock_Unlock009():
    test_result = TestCaseResult("Remote_Lock_Unlock009")
    test_result.description = "Verify Remote Unlock functionality"
    test_result.start_time = time.time()

    input("All doors are closed, Vehicle is unlocked, Ignition is off\nPress Enter to proceed...")

    try:
        latency_time = time.time()
        controller.click_by_image("Icons/lock_icon.png", threshold=0.80)
        sleep(2)
        controller.enter_pin("1234")
        # Need to know if completion is logged by tester via input or using the app indication
        latency_time = time.time() - latency_time

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

    input("All doors are closed, Vehicle is locked, Ignition is off\nPress Enter to proceed...")

    try:
        controller.click_by_image("Icons/lock_icon.png", threshold=0.80)
        sleep(2)
        controller.enter_pin("1234")

    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)
        test_result.status = "Error"

    test_result.end_time = time.time()
    return test_result

def Remote_Lock_Unlock011():
    test_result = TestCaseResult("Remote_Lock_Unlock011")
    test_result.description = "Verify Remote Unlock, vehicle unlocked"
    test_result.start_time = time.time()

    input("All doors are closed, Vehicle is unlocked, Ignition is off\nPress Enter to proceed...")

    try:
        controller.click_by_image("Icons/unlocked_icon.png", threshold=0.80)
        sleep(2)
        controller.enter_pin("1234")

    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)

    test_result.end_time = time.time()
    return test_result

def Remote_Lock_Unlock012():
    test_result = TestCaseResult("Remote_Lock_Unlock012")
    test_result.description = "Verify Remote Lock timeout, no network connection"
    test_result.start_time = time.time()

    input("All doors are closed, Vehicle is unlocked, Ignition is off, Disconnect vehicle from netowrk/flight mode on app\nPress Enter to proceed...")

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

    input("Vehicle is unlocked, Ignition is off, Fob key inside vehicle\nPress Enter to proceed...")

    try:
        controller.click_by_image("Icons/lock_icon.png", threshold=0.80)
        sleep(2)
        controller.enter_pin("1234")

    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)

    test_result.end_time = time.time()
    return test_result

def Remote_Lock_Unlock014():
    test_result = TestCaseResult("Remote_Lock_Unlock014")
    test_result.description = "Verify Remote Unlock, Fob keys left inside vehicle"
    test_result.start_time = time.time()

    input("Vehicle is locked, Ignition is off, Fob key inside vehicle\nPress Enter to proceed...")

    try:
        controller.click_by_image("Icons/unlock_icon.png", threshold=0.80)
        sleep(2)
        controller.enter_pin("1234")

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