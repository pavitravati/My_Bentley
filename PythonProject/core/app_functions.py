from time import sleep
from common_utils.android_image_comparision import *
from core.globals import current_email, current_password, current_vin, second_email, second_password, current_name
from core.log_emitter import blocked_log, fail_log, log


def app_login(email=current_email, password=current_password):
    success_tracker = []
    sleep(1)
    success_tracker.append(1) if controller.click_by_image("Icons/login_register_icon.png") else success_tracker.append(0)
    controller.wait_for_text("WELCOME", 30)
    while controller.is_text_present("WELCOME"):
        controller.enter_text(f"%s%s%s%s%s{email}")
        sleep(1)
    controller.wait_for_text("Log in – Enter password")
    if not controller.is_text_present("CREATE ACCOUNT"):
        while controller.is_text_present("Log in – Enter password"):
            controller.enter_text(password)
            sleep(2)
            if controller.is_text_present("Sorry, wrong password. Please try again"):
                success_tracker.append(0)
                return success_tracker
    else:
        controller.click_by_image("Icons/login_page_x.png")
        app_login(email, password)
    success_tracker.append(1) if controller.wait_for_text("DASHBOARD") else success_tracker.append(0)

    return success_tracker

def enable_flight_mode():
    controller.swipe_settings()
    if controller.click_by_image("Icons/flight_disabled.png"):
        controller.d.press("back")
        return True
    else:
        controller.d.press("back")
        return False

def disable_flight_mode():
    controller.swipe_settings()
    if controller.click_by_image("Icons/flight_enabled.png"):
        controller.d.press("back")
        return True
    else:
        controller.d.press("back")
        return False

def remote_swipe(service):
    for i in range(5):
        controller.small_swipe_up()
        if controller.is_text_present(service):
            sleep(1)
            return True
    return False

def app_login_setup(second_account=False):
    if controller.is_text_present("LOGIN OR REGISTER"):
        if current_email and current_password:
            if not second_account:
                login_check = app_login()
            else:
                login_check = app_login(second_email, second_password)
            if login_check == "0":
                blocked_log("Test blocked - Unable to login to begin testcase")
                sleep(1)
                return False
        else:
            blocked_log("Test blocked - Account logged out and credentials not provided")
            sleep(1)
            return False
    sleep(1)
    return True

def app_logout_setup(demo=False):
    if not controller.is_text_present("LOGIN OR REGISTER") and not demo:
        if not controller.click_by_image("Icons/Logout_Icon.png"):
            controller.click_by_image("Icons/Profile_Icon.png")
            controller.click_text("General")
            controller.click_by_image("Icons/Profile_Logout_Icon.png")
            controller.click_by_image("Icons/Logout_btn.png")
        if not controller.wait_for_text("LOGIN OR REGISTER", 30):
            blocked_log("Test blocked - Unable to logout to begin testcase")
            sleep(1)
            return False
        if demo:
            controller.wait_for_text_and_click("DISCOVER MY BENTLEY")
            if not controller.wait_for_text("Demo mode"):
                blocked_log("Test blocked - Unable to launch demo mode to begin testcase")
                sleep(1)
                return False
    sleep(1)
    return True

def app_refresh(num, service):
    controller.swipe_down()
    sleep(6)
    if compare_with_expected_crop("Icons/Error_Icon.png"):
        fail_log("Error displayed on refresh", num, service)
        controller.click_by_image("Icons/Error_Icon.png")
        sleep(1)
        return False
    else:
        controller.click_by_image("Icons/Update_Vehicle_data.png")
        if controller.wait_for_text("Vehicle status successfully retrieved", 30):
            log("Vehicle data updated")
            sleep(1)
            return True
        else:
            fail_log("Vehicle data not updated", num, service)
            sleep(1)
            return False

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
        car = ''

    return car

# Finish
def delete_vin():
    controller.click_by_image("Icons/info_btn.png")
    controller.click_text("Delete vehicle")
    controller.click_text("Delete")
    if not controller.wait_for_text("", 30):
        blocked_log("Test blocked - Unable to delete vin to complete testcase")
    sleep(1)


def add_vin():
    if controller.wait_for_text("DASHBOARD"):
        controller.small_swipe_up()
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/button_add_dashboard_module_add_vehicle")
        controller.small_swipe_up()
        controller.click_text("Enter VIN manually")
        controller.enter_text(current_vin)
        controller.click_text("CONFIRM")
        controller.wait_for_text("YOUR PREFERRED BENTLEY RETAILER")
        controller.click_by_image("Icons/Homescreen_Right_Arrow.png")
        while not compare_with_expected_crop("Images/retailer_search.png"):
            sleep(0.5)
        controller.wait_for_text_and_click("Search by retailer name or location")
        controller.enter_text("Manchester")
        controller.click_text("Bentley Manchester")
        controller.wait_for_text_and_click("CONFIRM")
        controller.wait_for_text("ADD YOUR BENTLEY")
        controller.wait_for_text_and_click("Continue")
        controller.click_text("Continue")
        controller.click_by_resource_id("firstname")
        while controller.d(resourceId="firstname").get_text() != "":
            controller.clear_text(1)
        controller.enter_text(current_name.split(" ")[0])
        controller.click_text("Next")
        while controller.d(resourceId="lastname").get_text() != "":
            controller.clear_text(1)
        controller.enter_text(current_name.split(" ")[1])
        controller.click_text("YOUR DETAILS")
        controller.click_text("Continue")
        controller.click_text("Location")
        controller.swipe_up(0.01)
        controller.click_text("United Kingdom")
        controller.click_text("Building")
        controller.enter_text("Bentley")
        controller.click_text("Next")
        controller.enter_text("1")
        controller.click_text("Next")
        controller.enter_text("Pyms%slane")
        controller.click_text("Next")
        controller.enter_text("Crewe")
        controller.click_text("Next")
        controller.enter_text("CW1%s3PJ")
        controller.click_by_image("Icons/vin_progress.png")
        controller.click_text("Continue")
        controller.wait_for_text_and_click("Area Code")
        controller.swipe_up(0.035)
        controller.click_text("+44")
        controller.click_text("Mobile Phone")
        controller.enter_text("07818014437")
        controller.click_text("Continue")
        controller.wait_for_text("Request Submitted")
        controller.click_text("Continue")
        controller.click_by_image("Icons/Homescreen_Left_Arrow.png")
        sleep(1)