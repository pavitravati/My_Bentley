from common_utils.android_image_comparision import *
from core.log_emitter import log, fail_log, error_log, metric_log

def Nav_Companion_001():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        if controller.click_by_image("Icons/navigation_icon.png"):
            log("Clicked on navigation tab")
        else:
            fail_log("Clicked on navigation tab", "001")

        controller.click_by_image("Images/Navigation_Allow.png")

        if controller.is_text_present("NAVIGATION"):
            log("Navigation screen launched")
        else:
            fail_log("Navigation screen not launched", "001")

        if compare_with_expected_crop("Images/Navigation_Search_Image.png"):
            log("Search Window displayed")
        else:
            fail_log("Search Window not displayed", "001")

        car_icon = False
        car_names = ['Bentayga', 'FlyingSpur', 'ContinentalGT', 'ContinentalGTC']
        for _ in range(4):
            if compare_with_expected_crop(f"Images/Navigation_{car_names[_]}_Image.png"):
                car_icon = True

        if controller.click_by_image("Images/Navigation_Car_Image.png"):
            if car_icon:
                log("Car Icon displayed and shows current location of vehicle")
            else:
                fail_log("Car Icon displayed but does not show current location of vehicle", "001")
        else:
            fail_log("Car Icon not displayed", "001")

        if controller.click_by_image("Images/Navigation_User_Image.png") and compare_with_expected_crop("Images/Navigation_User_Icon.png"):
            log("User Icon displayed and shows current location of user")
        else:
            fail_log("User Icon not displayed", "001")

        if controller.click_by_image("Images/Navigation_Info_Image.png"):
            if controller.is_text_present("Satellite") and controller.is_text_present("Show real time traffic data"):
                log("Option to enable 'Satellite' and 'Real time traffic' displayed")
            else:
                fail_log("Option to enable 'Satellite' and 'Real time traffic' not displayed", "001")
        else:
            fail_log("Option to enable 'Satellite' and 'Real time traffic' not displayed", "001")

    except Exception as e:
        error_log(e, "001")

def Nav_Companion_002():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/navigation_icon.png")
        controller.click_by_image("Images/Navigation_Allow.png")

        if controller.click_by_image("Images/Navigation_Search_Image.png"):
            controller.enter_text("London")
            log("Searched for a location")
        else:
            fail_log("Searched for a location", "002")

        # Check what shows when it searches successfully

    except Exception as e:
        error_log(e, "002")

def Nav_Companion_003():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/navigation_icon.png")
        controller.click_by_image("Images/Navigation_Allow.png")

    except Exception as e:
        error_log(e, "003")

def Nav_Companion_004():
    try:
        pass
    except Exception as e:
        error_log(e, "004")

def Nav_Companion_005():
    try:
        pass
    except Exception as e:
        error_log(e, "005")

def Nav_Companion_006():
    try:
        pass
    except Exception as e:
        error_log(e, "006")

def Nav_Companion_007():
    try:
        pass
    except Exception as e:
        error_log(e, "007")

def Nav_Companion_008():
    try:
        pass
    except Exception as e:
        error_log(e, "008")

def Nav_Companion_009():
    try:
        pass
    except Exception as e:
        error_log(e, "009")

def Nav_Companion_010():
    try:
        pass
    except Exception as e:
        error_log(e, "010")

def Nav_Companion_011():
    try:
        pass
    except Exception as e:
        error_log(e, "011")

def Nav_Companion_012():
    try:
        pass
    except Exception as e:
        error_log(e, "012")

def Nav_Companion_013():
    try:
        pass
    except Exception as e:
        error_log(e, "013")

def Nav_Companion_014():
    try:
        log("Cannot complete style guide testcases (temporary)")
    except Exception as e:
        error_log(e, "014")
