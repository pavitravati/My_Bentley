from time import sleep
from common_utils.android_image_comparision import *
from core.log_emitter import log, fail_log, metric_log, error_log

img_service = "Service Management"

def Service_Management_001():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/info_btn.png")
        controller.click_text("Service Management")

        service_management = controller.extract_service_management()

        if service_management:
            # At least the three services that show for all regions and cars
            if len(service_management) > 2:
                log("Services extracted from service management page")
            else:
                fail_log("Some general services missing")
            for service in service_management:
                metric_log(f"{service} displayed")
        else:
            fail_log("Could not extract services from service management page", "001", img_service)

        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/back_icon.png")

    except Exception as e:
        error_log(e, "001", img_service)

def Service_Management_002():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/info_btn.png")
        controller.click_text("Service Management")

        if controller.click_text("Lock my car"):
            log("Lock my car toggled off")
        else:
            fail_log("Lock my car failed to toggle off", "002", img_service)
        sleep(3)

        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/back_icon.png")
        if compare_with_expected_crop("Icons/Remote_Lock_Grey.png", 0.8):
            log("Remote lock/unlock successfully disabled")
        else:
            fail_log("Remote lock unlock failed to disable", "002", img_service)

        controller.click_by_image("Icons/info_btn.png")
        controller.click_text("Service Management")
        if controller.click_text("Lock my car"):
            log("Lock my car toggled on")
        else:
            fail_log("Lock my car failed to toggle on", "002", img_service)
        sleep(3)

        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/back_icon.png")
        if compare_with_expected_crop("Icons/Remote_Lock.png"):
            log("Remote lock/unlock successfully enabled")
        else:
            fail_log("Remote lock unlock failed to be enabled", "002", img_service)

    except Exception as e:
        error_log(e, "002", img_service)

def Service_Management_003():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/info_btn.png")
        controller.click_text("Service Management")

        if controller.click_text("Find my car"):
            log("Find my car toggled off")
        else:
            fail_log("Find my car failed to toggle off", "003", img_service)
        sleep(3)

        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/navigation_icon.png")

        if not controller.d(resourceId="uk.co.bentley.mybentley:id/imageButton_layout_map_button").exists:
            log("Car finder successfully disabled")
        else:
            fail_log("Car finder failed to disable", "003", img_service)

        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/info_btn.png")
        controller.click_text("Service Management")
        if controller.click_text("Find my car"):
            log("Find my car toggled on")
        else:
            fail_log("Find my car failed to toggle on", "003", img_service)
        sleep(3)

        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/navigation_icon.png")

        if controller.d(resourceId='uk.co.bentley.mybentley:id/imageButton_layout_map_button').exists:
            log("Car finder successfully enabled")
        else:
            fail_log("Car finder failed to be enabled", "003", img_service)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "003", img_service)

def Service_Management_004():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/info_btn.png")
        controller.click_text("Service Management")

        if controller.click_text("My car status"):
            log("My car status toggled off")
        else:
            fail_log("My car status failed to toggle off", "004", img_service)
        sleep(3)

        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/back_icon.png")
        controller.swipe_up()

        if controller.is_text_present("My car status unavailable"):
            log("Car status successfully disabled")
        else:
            fail_log("Car status failed to disable", "004", img_service)
        controller.swipe_down()

        controller.click_by_image("Icons/info_btn.png")
        controller.click_text("Service Management")
        if controller.click_text("My car status"):
            log("My car status toggled on")
        else:
            fail_log("My car status failed to toggle on", "004", img_service)
        sleep(3)

        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/back_icon.png")
        controller.swipe_up()

        if controller.d(text='Fuel range').exists:
            log("Car status successfully enabled")
        else:
            fail_log("Car status failed to be enabled", "004", img_service)
        controller.swipe_down()

    except Exception as e:
        error_log(e, "004", img_service)

def Service_Management_005():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/info_btn.png")
        controller.click_text("Service Management")
        controller.swipe_up()

        if controller.click_text("My cabin comfort"):
            log("My cabin comfort toggled off")
        else:
            fail_log("My cabin comfort failed to toggle off", "005", img_service)
        sleep(3)

        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/windows_icon.png")
        controller.swipe_up(0.3)

        if controller.click_text("MY CABIN COMFORT") and controller.is_text_present("Function disabled"):
            log("Cabin comfort successfully disabled")
        else:
            fail_log("Cabin comfort failed to be disabled", "005", img_service)

        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/info_btn.png")
        controller.click_text("Service Management")
        controller.swipe_up()
        if controller.click_text("My cabin comfort"):
            log("My cabin comfort toggled on")
        else:
            fail_log("My cabin comfort failed to toggle on", "005", img_service)
        sleep(3)

        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/windows_icon.png")

        if controller.click_text("MY CABIN COMFORT"):
            log("Cabin comfort successfully enabled")
            controller.click_by_image("Icons/back_icon.png")
        else:
            fail_log("Cabin comfort failed to be enabled", "005", img_service)

        controller.swipe_down()
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "005", img_service)

def Service_Management_006():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/info_btn.png")
        controller.click_text("Service Management")
        controller.swipe_up()

        if controller.click_text("My car statistics"):
            log("My car statistics toggled off")
        else:
            fail_log("My car statistics failed to toggle off", "006", img_service)
        sleep(3)

        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/windows_icon.png")

        if controller.is_text_present("Function disabled"):
            log("Car statistics successfully disabled")
        else:
            fail_log("Car statistics failed to disable", "006", img_service)

        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/info_btn.png")
        controller.click_text("Service Management")
        controller.swipe_up()
        if controller.click_text("My car statistics"):
            log(" My car statistics toggled on")
        else:
            fail_log(" My car statistics failed to toggle on", "006", img_service)
        sleep(3)

        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/windows_icon.png")

        if controller.click_text("MY CAR STATISTICS"):
            log("Car statistics successfully enabled")
            controller.click_text("List view")
            controller.click_by_image("Icons/back_icon.png")
        else:
            fail_log("Car statistics failed to be enabled", "006", img_service)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "006", img_service)

def Service_Management_007():
    try:
        pass
    except Exception as e:
        error_log(e, "007", img_service)

def Service_Management_008():
    try:
        pass
    except Exception as e:
        error_log(e, "008", img_service)

def Service_Management_009():
    try:
        pass
    except Exception as e:
        error_log(e, "009", img_service)

def Service_Management_010():
    try:
        log("Cannot complete style guide testcases (temporary)")
    except Exception as e:
        error_log(e, "010", img_service)
