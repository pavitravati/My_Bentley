from time import sleep
from common_utils.android_image_comparision import *
from core.app_functions import remote_swipe, app_login_setup
from core.globals import vehicle_type, country
from core.log_emitter import log, fail_log, metric_log, error_log, blocked_log
from core.globals import manual_run

img_service = "Service Management"

def Service_Management_001():
    try:
        if app_login_setup():
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            controller.click_by_image("Icons/info_btn.png")
            controller.click_text("Service Management")

            service_management = controller.extract_service_management()

            if service_management:
                # At least the three services that show for all regions and cars
                if len(service_management) > 2:
                    log("Services extracted from service management page")
                else:
                    fail_log("Some general services missing", "001", img_service)
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
        if app_login_setup():
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            controller.click_by_image("Icons/info_btn.png")
            controller.click_text("Service Management")

            if controller.click_text("Lock my car"):
                log("Lock my car toggled off")
            else:
                fail_log("Lock my car failed to toggle off", "002", img_service)
            while controller.is_text_present("Deactivating Lock my car"):
                sleep(0.2)

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
            while controller.is_text_present("Activating Lock my car"):
                sleep(0.2)

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
        if app_login_setup():
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            controller.click_by_image("Icons/info_btn.png")
            controller.click_text("Service Management")

            if controller.click_text("Find my car"):
                log("Find my car toggled off")
            else:
                fail_log("Find my car failed to toggle off", "003", img_service)
            while controller.is_text_present("Deactivating Find my car"):
                sleep(0.2)

            controller.click_by_image("Icons/back_icon.png")
            controller.click_by_image("Icons/back_icon.png")
            controller.click_by_image("Icons/navigation_icon.png")
            controller.click_text("ALLOW")

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
            while controller.is_text_present("Activating Find my car"):
                sleep(0.2)

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
        if app_login_setup():
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            controller.click_by_image("Icons/info_btn.png")
            controller.click_text("Service Management")

            if controller.click_text("My car status"):
                log("My car status toggled off")
            else:
                fail_log("My car status failed to toggle off", "004", img_service)
            while controller.is_text_present("Deactivating My car status"):
                sleep(0.2)

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
            while controller.is_text_present("Activating My car status"):
                sleep(0.2)
            controller.click_by_image("Icons/Error_Icon.png")

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
        if vehicle_type == "phev":
            if app_login_setup():
                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
                controller.click_by_image("Icons/info_btn.png")
                controller.click_text("Service Management")
                controller.swipe_up()

                if controller.click_text("My cabin comfort"):
                    log("My cabin comfort toggled off")
                else:
                    fail_log("My cabin comfort failed to toggle off", "005", img_service)
                while controller.is_text_present("Deactivating My cabin comfort"):
                    sleep(0.2)

                controller.click_by_image("Icons/back_icon.png")
                controller.click_by_image("Icons/back_icon.png")
                controller.click_by_image("Icons/windows_icon.png")
                controller.swipe_up(0.3)

                if controller.click_text("MY CABIN COMFORT"):
                    cabin_comfort = controller.d(text="MY CABIN COMFORT")
                    status = cabin_comfort.sibling(resourceId="uk.co.bentley.mybentley:id/textView_status_car_remote_item")
                    if status == "Function disabled":
                        log("My cabin comfort disabled")
                    else:
                        fail_log("My cabin comfort failed to disable", "005", img_service)
                else:
                    fail_log("My cabin comfort not found", "005", img_service)

                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
                controller.click_by_image("Icons/info_btn.png")
                controller.click_text("Service Management")
                controller.swipe_up()
                if controller.click_text("My cabin comfort"):
                    log("My cabin comfort toggled on")
                else:
                    fail_log("My cabin comfort failed to toggle on", "005", img_service)
                while controller.is_text_present("Activating My cabin comfort"):
                    sleep(0.2)

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
        elif vehicle_type == "ice":
            blocked_log("Test blocked - Must be a PHEV vehicle")

    except Exception as e:
        error_log(e, "005", img_service)

def Service_Management_006():
    try:
        if vehicle_type == "phev":
            if app_login_setup():
                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
                controller.click_by_image("Icons/info_btn.png")
                controller.click_text("Service Management")
                controller.swipe_up()

                if controller.click_text("My car statistics"):
                    log("My car statistics toggled off")
                else:
                    fail_log("My car statistics failed to toggle off", "006", img_service)
                while controller.is_text_present("Deactivating My car statistics"):
                    sleep(0.2)

                controller.click_by_image("Icons/back_icon.png")
                controller.click_by_image("Icons/back_icon.png")
                controller.click_by_image("Icons/windows_icon.png")

                if controller.click_text("MY CAR STATISTICS"):
                    car_statistics = controller.d(text="MY CAR STATISTICS")
                    status = car_statistics.sibling(resourceId="uk.co.bentley.mybentley:id/textView_status_car_remote_item")
                    if status == "Function disabled":
                        log("My car statistics disabled")
                    else:
                        fail_log("My car statistics failed to disable", "006", img_service)
                else:
                    fail_log("My car statistics not found", "006", img_service)

                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
                controller.click_by_image("Icons/info_btn.png")
                controller.click_text("Service Management")
                controller.swipe_up()
                if controller.click_text("My car statistics"):
                    log("My car statistics toggled on")
                else:
                    fail_log("My car statistics failed to toggle on", "006", img_service)
                while controller.is_text_present("Activating My car statistics"):
                    sleep(0.2)

                controller.click_by_image("Icons/back_icon.png")
                controller.click_by_image("Icons/back_icon.png")
                controller.click_by_image("Icons/windows_icon.png")

                if controller.click_text("MY CAR STATISTICS") and controller.is_text_present("List view"):
                    log("Car statistics successfully enabled")
                    controller.click_by_image("Icons/back_icon.png")
                else:
                    fail_log("Car statistics failed to be enabled", "006", img_service)
                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        elif vehicle_type == "ice":
            blocked_log("Test blocked - Must be a PHEV vehicle")
    except Exception as e:
        error_log(e, "006", img_service)

def Service_Management_007():
    try:
        if vehicle_type == "phev":
            if app_login_setup():
                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
                controller.click_by_image("Icons/info_btn.png")
                controller.click_text("Service Management")

                if controller.click_text("My battery charge"):
                    log("My battery charge toggled off")
                else:
                    fail_log("My battery charge failed to toggle off", "007", img_service)
                while controller.is_text_present("Deactivating My battery charge"):
                    sleep(0.2)

                controller.click_by_image("Icons/back_icon.png")
                controller.click_by_image("Icons/back_icon.png")
                controller.click_by_image("Icons/windows_icon.png")

                if controller.click_text("MY BATTERY CHARGE"):
                    battery_charge = controller.d(text="MY BATTERY CHARGE")
                    status = battery_charge.sibling(resourceId="uk.co.bentley.mybentley:id/textView_status_car_remote_item")
                    if status == "Function disabled":
                        log("My battery charge disabled")
                    else:
                        fail_log("My battery charge failed to disable", "007", img_service)
                else:
                    fail_log("My battery charge not found", "007", img_service)

                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
                controller.click_by_image("Icons/info_btn.png")
                controller.click_text("Service Management")
                if controller.click_text("My battery charge"):
                    log("My battery charge toggled on")
                else:
                    fail_log("My battery charge failed to toggle on", "007", img_service)
                while controller.is_text_present("Activating My battery charge"):
                    sleep(0.2)

                controller.click_by_image("Icons/back_icon.png")
                controller.click_by_image("Icons/back_icon.png")
                controller.click_by_image("Icons/windows_icon.png")

                if controller.click_text("MY BATTERY CHARGE") and controller.is_text_present("Set timer"):
                    log("Battery charge successfully enabled")
                    controller.click_by_image("Icons/back_icon.png")
                else:
                    fail_log("Battery charge failed to be enabled", "007", img_service)
                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        elif vehicle_type == "ice":
            blocked_log("Test blocked - Must be a PHEV vehicle")
    except Exception as e:
        error_log(e, "007", img_service)

def Service_Management_008():
    try:
        if country == "eur":
            if app_login_setup():
                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
                controller.click_by_image("Icons/info_btn.png")
                controller.click_text("Service Management")

                if controller.click_text("Theft alert"):
                    log("Theft alert toggled off")
                else:
                    fail_log("Theft alert failed to toggle off", "008", img_service)
                while controller.is_text_present("Deactivating Theft alert"):
                    sleep(0.2)

                controller.click_by_image("Icons/back_icon.png")
                controller.click_by_image("Icons/back_icon.png")
                controller.click_by_image("Icons/windows_icon.png")

                remote_swipe("STOLEN VEHICLE TRACKING")
                controller.click_text("STOLEN VEHICLE TRACKING")
                controller.click_text("My Alerts")
                if controller.is_text_present("This service is unavailable. It can be switched on in the Service Management screen for this vehicle."):
                    log("Theft alert disabled")
                else:
                    fail_log("Theft alert failed to disable", "008", img_service)
                controller.click_by_image("Icons/back_icon.png")

                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
                controller.click_by_image("Icons/info_btn.png")
                controller.click_text("Service Management")
                if controller.click_text("Theft alert"):
                    log("Theft alert toggled on")
                else:
                    fail_log("Theft alert failed to toggle on", "008", img_service)
                while controller.is_text_present("Activating Theft alert"):
                    sleep(0.2)

                controller.click_by_image("Icons/back_icon.png")
                controller.click_by_image("Icons/back_icon.png")
                controller.click_by_image("Icons/windows_icon.png")

                controller.click_text("STOLEN VEHICLE TRACKING")
                controller.click_text("My Alerts")
                if not controller.is_text_present("This service is unavailable. It can be switched on in the Service Management screen for this vehicle."):
                    log("Theft alert successfully enabled")
                else:
                    fail_log("Theft alert failed to be enabled", "008", img_service)
                controller.click_by_image("Icons/back_icon.png")
                controller.swipe_down(0.05)
                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "008", img_service)

def Service_Management_009():
    try:
        if country == "nar":
            blocked_log("Test blocked - Not written (NAR)")
        else:
            blocked_log("Test blocked - Region locked (NAR)")
    except Exception as e:
        error_log(e, "009", img_service)

def Service_Management_010():
    try:
        if country == "nar":
            blocked_log("Test blocked - Not written (NAR)")
        else:
            blocked_log("Test blocked - Region locked (NAR)")
    except Exception as e:
        error_log(e, "010", img_service)

def Service_Management_011():
    try:
        if country == "nar":
            blocked_log("Test blocked - Not written (NAR)")
        else:
            blocked_log("Test blocked - Region locked (NAR)")
    except Exception as e:
        error_log(e, "011", img_service)

def Service_Management_012():
    try:
        if country == "eur":
            if vehicle_type == "ice":
                if app_login_setup():
                    controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
                    controller.click_by_image("Icons/info_btn.png")
                    controller.click_text("Service Management")

                    if controller.click_text("Activate heating"):
                        log("Activate heating toggled off")
                    else:
                        fail_log("Activate heating failed to toggle off", "012", img_service)
                    while controller.is_text_present("Deactivating Activate heating"):
                        sleep(0.2)

                    controller.click_by_image("Icons/back_icon.png")
                    controller.click_by_image("Icons/back_icon.png")
                    controller.click_by_image("Icons/windows_icon.png")

                    if controller.click_text("ACTIVATE HEATING"):
                        activate_heating = controller.d(text="ACTIVATE HEATING")
                        status = activate_heating.sibling(resourceId="uk.co.bentley.mybentley:id/textView_status_car_remote_item")
                        if status == "Function disabled":
                            log("Activate heating disabled")
                        else:
                            fail_log("Activate heating failed to disable", "012", img_service)
                    else:
                        fail_log("Activate heating not found", "012", img_service)

                    controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
                    controller.click_by_image("Icons/info_btn.png")
                    controller.click_text("Service Management")
                    if controller.click_text("Activate heating"):
                        log("Activate heating toggled on")
                    else:
                        fail_log("Activate heating failed to toggle on", "012", img_service)
                    while controller.is_text_present("Activating Activate heating"):
                        sleep(0.2)

                    controller.click_by_image("Icons/back_icon.png")
                    controller.click_by_image("Icons/back_icon.png")
                    controller.click_by_image("Icons/windows_icon.png")

                    controller.click_text("ACTIVATE HEATING")
                    if controller.click_text("ACTIVATE HEATING") and controller.is_text_present("Quick start"):
                        log("Activate heating successfully enabled")
                        controller.click_by_image("Icons/back_icon.png")
                    else:
                        fail_log("Activate heating failed to be enabled", "012", img_service)
                    controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            elif vehicle_type == "phev":
                blocked_log("Test blocked - Must be an ICE vehicle")
        else:
            blocked_log("Test blocked - Region locked (EUR)")

    except Exception as e:
        error_log(e, "012", img_service)

def Service_Management_013():
    try:
        blocked_log("Test blocked - Can't check style guide")
    except Exception as e:
        error_log(e, "013", img_service)
