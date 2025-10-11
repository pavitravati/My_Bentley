from time import sleep
from common_utils.android_image_comparision import *
from common_utils.android_controller import *
from core.log_emitter import log_emitter

def log(msg):
    log_emitter.log_signal.emit(msg)

def fail_log(msg, num):
    log(f"{msg}")
    controller.take_fail_screenshot(f"SingleServiceActivation_{msg}_{num}.png")

def error_log(e, num):
    log(f"⚠️ - Unexpected error: {e}")
    controller.take_fail_screenshot(f"SingleServiceActivation_{e}_{num}.png")

def SingleServiceActivation_001():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/info_btn.png")
        controller.click_text("Service Management")

        service_management = controller.extract_service_management()

        if service_management:
            # At least the three services that show for all regions and cars
            if len(service_management) > 2:
                print("✅ - Services extracted from service management page")
            else:
                print("❌ - Some general services missing")
            for service in service_management:
                print(f"{service} displayed")
        else:
            print("❌ - Could not extract services from service management page", "001")

        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/back_icon.png")

    except Exception as e:
        error_log(e, "001")

def SingleServiceActivation_002():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/info_btn.png")
        controller.click_text("Service Management")

        if controller.click_text("Lock my car"):
            log("✅ - Lock my car toggled off")
        else:
            fail_log("❌ - Lock my car failed to toggle off", "002")
        sleep(3)

        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/back_icon.png")
        if compare_with_expected_crop("Icons/Remote_Lock_Grey.png", 0.8):
            log("✅ - Remote lock/unlock successfully disabled")
        else:
            fail_log("❌ - Remote lock unlock failed to disable", "002")

        controller.click_by_image("Icons/info_btn.png")
        controller.click_text("Service Management")
        if controller.click_text("Lock my car"):
            log("✅ - Lock my car toggled on")
        else:
            fail_log("❌ - Lock my car failed to toggle on", "002")
        sleep(3)

        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/back_icon.png")
        if compare_with_expected_crop("Icons/Remote_Lock.png"):
            log("✅ - Remote lock/unlock successfully enabled")
        else:
            fail_log("❌ - Remote lock unlock failed to be enabled", "002")

    except Exception as e:
        error_log(e, "002")

def SingleServiceActivation_003():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/info_btn.png")
        controller.click_text("Service Management")

        if controller.click_text("Find my car"):
            log("✅ - Find my car toggled off")
        else:
            fail_log("❌ - Find my car failed to toggle off", "003")
        sleep(3)

        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/navigation_icon.png")

        if not controller.d(resourceId="uk.co.bentley.mybentley:id/imageButton_layout_map_button").exists:
            log("✅ - Car finder successfully disabled")
        else:
            fail_log("❌ - Car finder failed to disable", "003")

        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/info_btn.png")
        controller.click_text("Service Management")
        if controller.click_text("Find my car"):
            log("✅ - Find my car toggled on")
        else:
            fail_log("❌ - Find my car failed to toggle on", "003")
        sleep(3)

        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/navigation_icon.png")

        if controller.d(resourceId='uk.co.bentley.mybentley:id/imageButton_layout_map_button').exists:
            log("✅ - Car finder successfully enabled")
        else:
            fail_log("❌ - Car finder failed to be enabled", "003")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "003")

def SingleServiceActivation_004():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/info_btn.png")
        controller.click_text("Service Management")

        if controller.click_text("My car status"):
            log("✅ - My car status toggled off")
        else:
            fail_log("❌ - My car status failed to toggle off", "004")
        sleep(3)

        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/back_icon.png")
        controller.swipe_up()

        if controller.is_text_present("My car status unavailable"):
            log("✅ - Car status successfully disabled")
        else:
            fail_log("❌ - Car status failed to disable", "004")

        controller.click_by_image("Icons/info_btn.png")
        controller.click_text("Service Management")
        if controller.click_text("My car status"):
            log("✅ - My car status toggled on")
        else:
            fail_log("❌ - My car status failed to toggle on", "004")
        sleep(3)

        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/back_icon.png")
        controller.swipe_up()

        if controller.d(text='Fuel range').exists:
            log("✅ - Car status successfully enabled")
        else:
            fail_log("❌ - Car status failed to be enabled", "004")
        controller.swipe_down()
        controller.swipe_down()

    except Exception as e:
        error_log(e, "004")

def SingleServiceActivation_005():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/info_btn.png")
        controller.click_text("Service Management")
        controller.swipe_up()

        if controller.click_text("My cabin comfort"):
            log("✅ - My cabin comfort toggled off")
        else:
            fail_log("❌ - My cabin comfort failed to toggle off", "005")
        sleep(3)

        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/windows_icon.png")
        controller.swipe_up(0.3)

        if controller.is_text_present("Function disabled"):
            log("✅ - Cabin comfort successfully disabled")
        else:
            fail_log("❌ - Cabin comfort failed to disable", "005")

        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/info_btn.png")
        controller.click_text("Service Management")
        controller.swipe_up()
        if controller.click_text("My cabin comfort"):
            log("✅ - My cabin comfort toggled on")
        else:
            fail_log("❌ - My cabin comfort failed to toggle on", "005")
        sleep(3)

        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/windows_icon.png")

        if controller.click_text("MY CABIN COMFORT"):
            log("✅ - Cabin comfort successfully enabled")
            controller.click_by_image("Icons/back_icon.png")
        else:
            fail_log("❌ - Cabin comfort failed to be enabled", "005")

        controller.swipe_down()
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "005")

def SingleServiceActivation_006():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/info_btn.png")
        controller.click_text("Service Management")
        controller.swipe_up()

        if controller.click_text("My car statistics"):
            log("✅ - My car statistics toggled off")
        else:
            fail_log("❌ - My car statistics failed to toggle off", "006")
        sleep(3)

        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/windows_icon.png")

        if controller.is_text_present("Function disabled"):
            log("✅ - Car statistics successfully disabled")
        else:
            fail_log("❌ - Car statistics failed to disable", "006")

        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/info_btn.png")
        controller.click_text("Service Management")
        controller.swipe_up()
        if controller.click_text("My car statistics"):
            log("✅ -  My car statistics toggled on")
        else:
            fail_log("❌ -  My car statistics failed to toggle on", "006")
        sleep(3)

        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/windows_icon.png")

        if controller.click_text("MY CAR STATISTICS"):
            log("✅ - Car statistics successfully enabled")
            controller.click_text("List view")
            controller.click_by_image("Icons/back_icon.png")
        else:
            fail_log("❌ - Car statistics failed to be enabled", "006")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "006")

def SingleServiceActivation_007():
    try:
        pass
    except Exception as e:
        error_log(e, "007")

def SingleServiceActivation_008():
    try:
        pass
    except Exception as e:
        error_log(e, "008")

def SingleServiceActivation_009():
    try:
        pass
    except Exception as e:
        error_log(e, "009")

def SingleServiceActivation_010():
    try:
        log("✅ - Cannot complete style guide testcases (temporary)")
    except Exception as e:
        error_log(e, "010")
