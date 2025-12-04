from common_utils.android_image_comparision import *
from core.log_emitter import log, fail_log, error_log, metric_log, blocked_log, runtime_log
from time import sleep
from core.app_functions import app_login_setup, identify_car, service_reset
from core.screenrecord import ScreenRecorder
from core import globals

img_service = "Car Finder"
recorder = ScreenRecorder(device_serial=controller.d.serial)

def Car_Finder_001():
    recorder.start(f"{img_service}-001")
    try:
        if app_login_setup():
            if controller.click_by_image("Icons/navigation_icon.png"):
                controller.click_by_image("Images/Navigation_Allow.png")
                log("Navigation tab displayed")
            else:
                fail_log("Navigation tab not displayed", "001", img_service)

    except Exception as e:
        error_log(e, "001", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Car_Finder_002():
    recorder.start(f"{img_service}-002")
    try:
        if app_login_setup():
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            cars = []
            while not controller.is_text_present("ADD A VEHICLE"):
                car = identify_car()
                if car and not controller.is_text_present("Lock my car unavailable"):
                    cars.append(car)
                if not controller.click_by_image("Icons/Homescreen_Right_Arrow.png"):
                    break

            while True:
                if not controller.click_by_image("Icons/Homescreen_Left_Arrow.png"):
                    break

            if cars:
                controller.click_by_image("Icons/navigation_icon.png")
                controller.click_by_image("Images/Navigation_Allow.png")
                if controller.click_by_resource_id("uk.co.bentley.mybentley:id/imageButton_layout_map_button"):
                    log("'Car' Icon clicked")
                    sleep(1)

                    markers = controller.d.xpath('//*[@content-desc="Map Marker"]').all()
                    car_count = len(markers)-1 if compare_with_expected_crop("Images/Navigation_User_Icon.png", 0.8) else len(markers)
                    if car_count == len(cars):
                        log("Expected car markers displayed")
                    else:
                        fail_log("Expected car markers not displayed", "002", img_service)
                else:
                    fail_log("'Car' Icon not displayed", "002", img_service)
            else:
                fail_log("No cars on the account will be displayed on the map (Possibly caused by no primary user)", "002", img_service)

    except Exception as e:
        error_log(e, "002", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Car_Finder_003():
    recorder.start(f"{img_service}-003")
    try:
        if app_login_setup():
            controller.click_by_image("Icons/navigation_icon.png")
            controller.click_by_image("Images/Navigation_Allow.png")

            if controller.click_by_resource_id("uk.co.bentley.mybentley:id/imageButton_map_fragment_my_location"):
                log("Bottom right user icon displayed")
            else:
                fail_log("Bottom right user icon not displayed", "003", img_service)
            sleep(0.5)

            if compare_with_expected_crop("Images/Navigation_User_Icon.png", 0.8):
                log("User location displayed on navigation page")
            else:
                fail_log("User location not displayed on navigation page", "003", img_service)

    except Exception as e:
        error_log(e, "003", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Car_Finder_004():
    recorder.start(f"{img_service}-004")
    try:
        if app_login_setup():
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            cars = []
            while not controller.is_text_present("ADD A VEHICLE"):
                car = identify_car()
                if car and not controller.is_text_present("Lock my car unavailable"):
                    cars.append(car)
                if not controller.click_by_image("Icons/Homescreen_Right_Arrow.png"):
                    break

            while True:
                if not controller.click_by_image("Icons/Homescreen_Left_Arrow.png"):
                    break

            controller.click_by_image("Icons/navigation_icon.png")
            controller.click_by_image("Images/Navigation_Allow.png")
            if cars:
                if controller.click_by_resource_id("uk.co.bentley.mybentley:id/imageButton_layout_map_button"):
                    log("'Car' Icon clicked")
                    sleep(1)
                    markers = controller.d.xpath('//*[@content-desc="Map Marker"]').all()
                    car_count = len(markers)-1 if compare_with_expected_crop("Images/Navigation_User_Icon.png", 0.8) else len(markers)
                    if car_count == len(cars):
                        log("Expected car markers displayed")
                    else:
                        fail_log("Expected car markers not displayed", "004", img_service)
                else:
                    fail_log("'Car' Icon not displayed", "002", img_service)
            else:
                fail_log("No cars on the account will be displayed on the map (Possibly caused by no primary user)", "004", img_service)
            if controller.click_by_resource_id("uk.co.bentley.mybentley:id/imageButton_map_fragment_my_location"):
                log("Bottom right user icon displayed")
                sleep(0.5)
                if compare_with_expected_crop("Images/Navigation_User_Icon.png", 0.85):
                    log("User location displayed on navigation page")
                else:
                    fail_log("User location not displayed on navigation page", "004", img_service)
            else:
                fail_log("Bottom right user icon not displayed", "003", img_service)

    except Exception as e:
        error_log(e, "004", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Car_Finder_005():
    recorder.start(f"{img_service}-005")
    try:
        if app_login_setup():
            controller.click_by_image("Icons/navigation_icon.png")
            controller.click_by_image("Images/Navigation_Allow.png")
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/imageButton_layout_map_button")
            sleep(1)

            markers = controller.d.xpath('//*[@content-desc="Map Marker"]').all()
            driver_icon_bounds = []
            for i in range(len(markers)):
                driver_icon_bounds.append(markers[i].center())
                if i == 1:
                    break

            controller.click(driver_icon_bounds[0][0], driver_icon_bounds[0][1])
            sleep(0.5)
            vehicle_details = controller.extract_navigation_vehicle()
            if vehicle_details:
                log("Vehicle details displayed on navigation page")
                for metric, stat in vehicle_details.items():
                    metric_log(f"{metric}: {stat}")
            else:
                try:
                    controller.click(driver_icon_bounds[1][0], driver_icon_bounds[1][1])
                    sleep(0.5)
                    vehicle_details = controller.extract_navigation_vehicle()
                    if vehicle_details:
                        log("Vehicle details displayed on navigation page")
                        for metric, stat in vehicle_details:
                            metric_log(f"{metric}: {stat}")
                    else:
                        fail_log("No vehicle visible on navigation page", "005", img_service)
                except Exception as e:
                    fail_log("No vehicle visible on navigation page", "005", img_service)

            controller.click(500, 500)

    except Exception as e:
        error_log(e, "005", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Car_Finder_006():
    recorder.start(f"{img_service}-006")
    try:
        if app_login_setup():

            controller.click_by_image("Icons/navigation_icon.png")
            controller.click_by_image("Images/Navigation_Allow.png")
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/imageButton_layout_map_button")
            sleep(0.5)

            markers = controller.d.xpath('//*[@content-desc="Map Marker"]').all()
            driver_icon_bounds = []
            for i in range(len(markers)):
                driver_icon_bounds.append(markers[i].center())
                if i == 1:
                    break

            controller.click(driver_icon_bounds[0][0], driver_icon_bounds[0][1])
            if not controller.is_text_present("PLAN ROUTE"):
                try:
                    controller.click(driver_icon_bounds[1][0], driver_icon_bounds[1][1])
                except Exception as e:
                    fail_log("No vehicle visible on navigation page", "006", img_service)

            if controller.click_text("PLAN ROUTE"):
                log("Plan route button clicked")
                sleep(3)
                if controller.is_text_present("Your location") and controller.d.xpath('//*[starts-with(@content-desc, "Destination")]').exists:
                    log("Route created and displayed")
                else:
                    fail_log("Route not created", "006", img_service)
            else:
                fail_log("Plan route button not displayed", "006", img_service)

            controller.launch_app("uk.co.bentley.mybentley")
            controller.click(500, 500)

    except Exception as e:
        error_log(e, "006", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Car_Finder_007():
    recorder.start(f"{img_service}-007")
    try:
        blocked_log("Test blocked - Can't check style guide")
    except Exception as e:
        error_log(e, "007", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False