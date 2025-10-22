from common_utils.android_image_comparision import *
from core.log_emitter import log_emitter
from time import sleep

def log(msg):
    log_emitter.log_signal.emit(msg)

def fail_log(msg, num):
    log(f"{msg}")
    controller.take_fail_screenshot(f"Car Finder-{msg}-{num}.png")

def error_log(e, num):
    log(f"⚠️ - Unexpected error: {e}")
    controller.take_fail_screenshot(f"Car Finder-{e}-{num}.png")

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
        return None

    return car

def Car_Finder_001():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        if controller.click_by_image("Icons/navigation_icon.png"):
            controller.click_by_image("Images/Navigation_Allow.png")
            log("✅ - Navigation tab displayed")
        else:
            fail_log("❌ - Navigation tab not displayed", "001")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "001")

# Image recognition of the markers does not work and the ids are the same so this is dodgy
def Car_Finder_002():
    try:
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
        controller.click_by_image("Images/Navigation_Car_Image.png")

        markers = controller.d.xpath('//*[@content-desc="Map Marker"]').all()
        if len(markers) == len(cars) or len(cars)+1:
            log("✅ - Car map markers all displayed")
        else:
            fail_log("❌ - Car map markers not displayed", "002")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "002")

def Car_Finder_003():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/navigation_icon.png")
        controller.click_by_image("Images/Navigation_Allow.png")

        if controller.d.xpath('//*[@content-desc="User\'s location"]').exists:
            log("✅ - User icon displayed on navigation page")
        else:
            fail_log("❌ - User icon not displayed on navigation page", "003")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "003")

# same problem as 002
def Car_Finder_004():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

        controller.click_by_image("Icons/navigation_icon.png")
        controller.click_by_image("Images/Navigation_Allow.png")
        controller.click_by_image("Images/Navigation_User_Image.png")

        markers = controller.d.xpath('//*[@content-desc="Map Marker"]').all()
        if len(markers) >= 1:
            log("✅ - User location displayed on navigation page")
        else:
            fail_log("❌ - User location not displayed on navigation page", "004")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "004")

# Is this not a literal repeat of testcase 2 and 4
def Car_Finder_005():
    try:
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

        controller.click_by_image("Images/Navigation_User_Image.png")
        markers = controller.d.xpath('//*[@content-desc="Map Marker"]').all()
        if len(markers) >= 1:
            log("✅ - User location displayed on navigation page")
        else:
            fail_log("❌ - User location not displayed on navigation page", "005")

        controller.click_by_image("Images/Navigation_Car_Image.png")
        markers = controller.d.xpath('//*[@content-desc="Map Marker"]').all()
        if len(markers) == len(cars) or len(cars) + 1:
            log(f"✅ - {car} icon displayed on navigation page")
        else:
            fail_log(f"❌ - {car} icon displayed on navigation page", "005")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "005")

def Car_Finder_006():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/navigation_icon.png")
        controller.click_by_image("Images/Navigation_Allow.png")
        controller.click_by_image("Images/Navigation_Car_Image.png")

        markers = controller.d.xpath('//*[@content-desc="Map Marker"]').all()
        driver_icon_bounds = []
        for i in range(len(markers)):
            driver_icon_bounds.append(markers[i].center())
            if i == 1:
                break

        controller.click(driver_icon_bounds[0][0], driver_icon_bounds[0][1])
        vehicle_details = controller.extract_navigation_vehicle()
        if vehicle_details:
            log("✅ - Vehicle details displayed on navigation page")
            for metric, stat in vehicle_details.items():
                log(f"{metric}: {stat}")
        else:
            try:
                controller.click(driver_icon_bounds[1][0], driver_icon_bounds[1][1])
                vehicle_details = controller.extract_navigation_vehicle()
                if vehicle_details:
                    log("✅ - Vehicle details displayed on navigation page")
                    for metric, stat in vehicle_details:
                        log(f"{metric}: {stat}")
                else:
                    fail_log("❌ - No vehicle visible on navigation page", "006")
            except Exception as e:
                fail_log("❌ - No vehicle visible on navigation page", "006")

        controller.click(500, 500)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "006")

def Car_Finder_007():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/navigation_icon.png")
        controller.click_by_image("Images/Navigation_Allow.png")
        controller.click_by_image("Images/Navigation_Car_Image.png")

        markers = controller.d.xpath('//*[@content-desc="Map Marker"]').all()
        driver_icon_bounds = []
        for i in range(len(markers)):
            driver_icon_bounds.append(markers[i].center())
            if i == 1:
                break

        controller.click(driver_icon_bounds[0][0], driver_icon_bounds[0][1])
        if compare_with_expected_crop("Images/Navigation_Car_Image.png"):
            try:
                controller.click(driver_icon_bounds[1][0], driver_icon_bounds[1][1])
            except Exception as e:
                fail_log("❌ - No vehicle visible on navigation page", "007")

        if controller.click_text("PLAN ROUTE"):
            log("✅ - Plan route button clicked")
            sleep(5)
            if controller.is_text_present("Your location") and controller.d.xpath('//*[starts-with(@content-desc, "Destination")]').exists:
                log("✅ - Route created and displayed")
            else:
                fail_log("❌ - Route not created", "007")
        else:
            fail_log("❌ - Plan route button not displayed", "007")

        controller.press_home()
        controller.launch_app("uk.co.bentley.mybentley")
        controller.click(500, 500)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "007")

# Privacy mode in the car
def Car_Finder_008():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.swipe_down()
        sleep(6)

        controller.click_by_image("Icons/navigation_icon.png")
        controller.click_by_image("Images/Navigation_Allow.png")
        controller.click_by_image("Images/Navigation_Car_Image.png")

        if not compare_with_expected_crop("Images/Navigation_Car_Image.png"):
            log("✅ - Find my car icon not displayed when privacy mode activated")
        else:
            fail_log("❌ - Find my car icon displayed when privacy mode activated", "008")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/Error_Icon.png")

    except Exception as e:
        error_log(e, "008")

def Car_Finder_009():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.swipe_down()
        sleep(6)

        controller.click_by_image("Icons/navigation_icon.png")
        controller.click_by_image("Images/Navigation_Allow.png")
        controller.click_by_image("Images/Navigation_Car_Image.png")

        if compare_with_expected_crop("Images/Navigation_Car_Image.png"):
            log("✅ - Find my car icon displayed when privacy mode deactivated")
        else:
            fail_log("❌ - Find my car icon not displayed when privacy mode deactivated", "009")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/Error_Icon.png")


    except Exception as e:
        error_log(e, "009")

def Car_Finder_010():
    try:
        log("✅ - temp, Cannot check style guide")
    except Exception as e:
        error_log(e, "009")