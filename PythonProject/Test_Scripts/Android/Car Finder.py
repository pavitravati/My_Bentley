from common_utils.android_image_comparision import *
from core.log_emitter import log, fail_log, error_log, metric_log, blocked_log
from time import sleep
from core.globals import manual_run
from core.app_functions import app_login_setup, identify_car

img_service = "Car Finder"

def Car_Finder_001():
    try:
        if app_login_setup():

            if controller.click_by_image("Icons/navigation_icon.png"):
                controller.click_by_image("Images/Navigation_Allow.png")
                log("Navigation tab displayed")
            else:
                fail_log("Navigation tab not displayed", "001", img_service)
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "001", img_service)

def Car_Finder_002():
    try:
        if app_login_setup():

            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            cars = []
            while True:
                car = identify_car()
                if car:
                    cars.append(car)
                if not controller.click_by_image("Icons/Homescreen_Right_Arrow.png"):
                    break

            while True:
                if not controller.click_by_image("Icons/Homescreen_Left_Arrow.png"):
                    break

            controller.click_by_image("Icons/navigation_icon.png")
            controller.click_by_image("Images/Navigation_Allow.png")
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/imageButton_layout_map_button")
            sleep(1)

            markers = controller.d.xpath('//*[@content-desc="Map Marker"]').all()
            if len(markers) == len(cars) or len(markers) == len(cars)+1:
                log("Car map markers all displayed")
            else:
                fail_log("Car map markers not displayed", "002", img_service)
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "002", img_service)

def Car_Finder_003():
    try:
        if app_login_setup():

            controller.click_by_image("Icons/navigation_icon.png")
            controller.click_by_image("Images/Navigation_Allow.png")

            if controller.click_by_resource_id("uk.co.bentley.mybentley:id/imageButton_map_fragment_my_location"):
                log("User icon displayed on navigation page")
            else:
                fail_log("User icon not displayed on navigation page", "003", img_service)
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "003", img_service)

def Car_Finder_004():
    try:
        if app_login_setup():

            controller.click_by_image("Icons/navigation_icon.png")
            controller.click_by_image("Images/Navigation_Allow.png")
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/imageButton_map_fragment_my_location")
            sleep(1)

            if compare_with_expected_crop("Images/Navigation_User_Icon.png", 0.85):
                log("User location displayed on navigation page")
            else:
                fail_log("User location not displayed on navigation page", "004", img_service)
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "004", img_service)

def Car_Finder_005():
    try:
        if app_login_setup():

            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            cars = []
            while True:
                car = identify_car()
                if car:
                    cars.append(car)
                if not controller.click_by_image("Icons/Homescreen_Right_Arrow.png"):
                    break

            while True:
                if not controller.click_by_image("Icons/Homescreen_Left_Arrow.png"):
                    break

            controller.click_by_image("Icons/navigation_icon.png")
            controller.click_by_image("Images/Navigation_Allow.png")

            controller.click_by_resource_id("uk.co.bentley.mybentley:id/imageButton_map_fragment_my_location")
            sleep(1)
            if compare_with_expected_crop("Images/Navigation_User_Icon.png", 0.85):
                log("User location displayed on navigation page")
            else:
                fail_log("User location not displayed on navigation page", "005", img_service)

            controller.click_by_resource_id("uk.co.bentley.mybentley:id/imageButton_layout_map_button")
            sleep(1)
            markers = controller.d.xpath('//*[@content-desc="Map Marker"]').all()
            if len(markers) == len(cars) or len(markers) == len(cars)+1:
                log("car icon displayed on navigation page")
            else:
                fail_log("car icon displayed on navigation page", "005", img_service)
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "005", img_service)

def Car_Finder_006():
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
                        fail_log("No vehicle visible on navigation page", "006", img_service)
                except Exception as e:
                    fail_log("No vehicle visible on navigation page", "006", img_service)

            controller.click(500, 500)
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "006", img_service)

def Car_Finder_007():
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
                    fail_log("No vehicle visible on navigation page", "007", img_service)

            if controller.click_text("PLAN ROUTE"):
                log("Plan route button clicked")
                sleep(3)
                if controller.is_text_present("Your location") and controller.d.xpath('//*[starts-with(@content-desc, "Destination")]').exists:
                    log("Route created and displayed")
                else:
                    fail_log("Route not created", "007", img_service)
            else:
                fail_log("Plan route button not displayed", "007", img_service)

            controller.launch_app("uk.co.bentley.mybentley")
            controller.click(500, 500)
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "007", img_service)

def Car_Finder_008():
    try:
        blocked_log("Test blocked - Can't check style guide")
    except Exception as e:
        error_log(e, "008", img_service)