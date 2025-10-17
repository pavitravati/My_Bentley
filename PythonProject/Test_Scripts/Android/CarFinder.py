from common_utils.android_image_comparision import *
from core.log_emitter import log_emitter
from time import sleep

def log(msg):
    log_emitter.log_signal.emit(msg)

def fail_log(msg, num):
    log(f"{msg}")
    controller.take_fail_screenshot(f"CarFinder-{msg}-{num}.png")

def error_log(e, num):
    log(f"⚠️ - Unexpected error: {e}")
    controller.take_fail_screenshot(f"CarFinder-{e}-{num}.png")

def CarFinder_001():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/navigation_icon.png")
        controller.click_by_image("Images/Navigation_Allow.png")
        if compare_with_expected_crop("Images/Navigation_Car_Image.png"):
            log("✅ - Car icon displayed on navigation page")
        else:
            fail_log("❌ - Car icon not displayed on navigation page", "001")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "001")

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

def CarFinder_002():
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

        for car in cars:
            if compare_with_expected_crop(f"Images/Nav_{car.replace(" ", "")}_Icon.png"):
                log(f"✅ - {car} icon displayed on navigation page")
            else:
                fail_log(f"❌ - {car} icon displayed on navigation page", "002")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "002")

def CarFinder_003():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/navigation_icon.png")
        controller.click_by_image("Images/Navigation_Allow.png")

        if compare_with_expected_crop("Images/Navigation_User_Image.png"):
            log("✅ - User icon displayed on navigation page")
        else:
            fail_log("❌ - User icon not displayed on navigation page", "003")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "003")

def CarFinder_004():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

        controller.click_by_image("Icons/navigation_icon.png")
        controller.click_by_image("Images/Navigation_Allow.png")
        controller.click_by_image("Images/Navigation_User_Image.png")

        if compare_with_expected_crop("Images/Navigation_User_Image.png"):
            log("✅ - User location displayed on navigation page")
        else:
            fail_log("❌ - User location not displayed on navigation page", "004")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "004")

# Is this not a literal repeat of testcase 2 and 4
def CarFinder_005():
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
        if compare_with_expected_crop("Images/Navigation_User_Image.png"):
            log("✅ - User location displayed on navigation page")
        else:
            fail_log("❌ - User location not displayed on navigation page", "005")

        for car in cars:
            if compare_with_expected_crop(f"Images/Nav_{car.replace(" ", "")}_Icon.png"):
                log(f"✅ - {car} icon displayed on navigation page")
            else:
                fail_log(f"❌ - {car} icon displayed on navigation page", "005")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "005")

def CarFinder_006():
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

        car_found = False
        for car in cars:
            if controller.click_by_image(f"Images/Nav_{car.replace(" ", "")}_Icon.png"):
                car_found = True
                break

        if not car_found:
            fail_log("❌ - No vehicle visible on navigation page", "006")
        else:
            log("✅ - Vehicle details displayed on navigation page")
            vehicle_details = controller.extract_navigation_vehicle()
            for metric, stat in vehicle_details:
                log(f"{metric}: {stat}")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "006")

# ASK about how to verify that the route displayed is correct
def CarFinder_007():
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

        car_found = False
        for car in cars:
            if controller.click_by_image(f"Images/Nav_{car.replace(" ", "")}_Icon.png"):
                car_found = True
                break

        if not car_found:
            fail_log("❌ - No vehicle visible on navigation page", "006")
        else:
            controller.click_text("PLAN ROUTE")
            sleep(5)
            controller.click_text("while using the app")
            # HOW TO CHECK
            log("✅ - temp")

        controller.press_home()
        controller.launch_app("uk.co.bentley.mybentley")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "007")

def CarFinder_008():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/navigation_icon.png")
        controller.click_by_image("Images/Navigation_Allow.png")
        controller.click(500, 750)

        # wher ein remote screen is this
    except Exception as e:
        error_log(e, "008")

def CarFinder_009():
    try:
        log("✅ - temp, Cannot check style guide")
    except Exception as e:
        error_log(e, "009")