from time import sleep
from common_utils.android_image_comparision import *
from core.log_emitter import log, metric_log, error_log, fail_log

img_service = "App Log in-Log out"

# This is very dodgy if the phone is slow/slow internet
def App_Log_in_Log_out_001():
    try:
        # If not on the login page, attempts to log out/exit demo mode
        if not compare_with_expected_crop("Images/My_Bentley_Login_Page.png"):
            controller.click_by_image("Icons/Logout_Icon.png")
            controller.click_by_image("Icons/Profile_Icon.png")
            controller.click_text("General")
            controller.click_by_image("Icons/Profile_Logout_Icon.png")
            controller.click_by_image("Icons/Logout_btn.png")
        sleep(5)

        if controller.click_by_image("Icons/login_register_icon.png"):
            log("Login button clicked")
        else:
            fail_log("Login button not clicked", "001", img_service)

        if controller.wait_for_text("WELCOME", 30):
            # add the spaces(%s) so that if first chars get cut off it still works
            email = "%s%s%s%s%s%s%s%stestdrive@gqm.anonaddy.com"
            controller.enter_text(email)
            sleep(5)
            password = "Password1!"
            controller.enter_text(password)
            log("Email and Password entered")
        else:
            fail_log("Email and Password not entered", "001", img_service)

        if controller.wait_for_text("DASHBOARD"):
            log("Dashboard screen not launched")
        else:
            fail_log("Dashboard screen not launched", "001", img_service)

    except Exception as e:
        error_log(e, "001", img_service)

def App_Log_in_Log_out_002():
    try:
        # If not on the login page, attempts to log out/exit demo mode
        if not compare_with_expected_crop("Images/My_Bentley_Login_Page.png"):
            controller.click_by_image("Icons/Logout_Icon.png")
            controller.click_by_image("Icons/Profile_Icon.png")
            controller.click_text("General")
            controller.click_by_image("Icons/Profile_Logout_Icon.png")
            controller.click_by_image("Icons/Logout_btn.png")
        sleep(5)

        if controller.click_by_image("Icons/login_register_icon.png"):
            log("Login button clicked")
        else:
            fail_log("Login button not clicked", "002", img_service)

        if controller.wait_for_text("WELCOME", 30):
            # add the spaces(%s) so that if first chars get cut off it still works
            email = "%s%s%s%s%s%s%s%stestdrive@gqm.anonaddy.com"
            controller.enter_text(email)
            sleep(5)
            controller.enter_text("Wrongpassword")
            log("Email and incorrect Password entered")
        else:
            fail_log("Email and incorrect Password not entered", "002", img_service)

        if controller.wait_for_text("Sorry, wrong password. Please try again"):
            log("Incorrect password error message displayed")
        else:
            fail_log("Incorrect password error message not displayed", "002", img_service)

    except Exception as e:
        error_log(e, "002", img_service)

def App_Log_in_Log_out_003():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/Profile_Icon.png")
        sleep(0.2)
        controller.click_text("General")
        sleep(0.2)
        controller.click_text("Log out")
        sleep(0.2)

        if controller.click_text("Cancel"):
            log("Cancel clicked on popup")
        else:
            fail_log("Cancel not clicked on popup", "003", img_service)

        if compare_with_expected_crop("Images/Profile_Screen.png"):
            log("Popup closed")
        else:
            fail_log("Popup not closed", "003", img_service)

        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "003", img_service)

def App_Log_in_Log_out_004():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        if controller.click_by_image("Icons/Profile_Icon.png"):
            log("Profile icon clicked")
        else:
            fail_log("Profile icon not clicked", "004", img_service)
        sleep(0.2)
        if controller.click_text("General"):
            log("General tab clicked")
        else:
            fail_log("General tab not clicked", "004", img_service)
        sleep(0.2)
        if controller.click_text("Log out"):
            log("Log out button clicked")
        else:
            fail_log("Log out button not clicked", "004", img_service)
        sleep(0.2)
        if controller.click_by_image("Icons/Logout_btn.png"):
            log("Logged out of account")
        else:
            fail_log("Not logged out of account", "004", img_service)
        sleep(5)

        controller.click_by_image("Icons/login_register_icon.png")

    except Exception as e:
        error_log(e, "004", img_service)

def App_Log_in_Log_out_005():
    try:
        if not compare_with_expected_crop("Images/My_Bentley_Login_Page.png"):
            controller.click_by_image("Icons/Logout_Icon.png")
            controller.click_by_image("Icons/Profile_Icon.png")
            controller.click_text("General")
            controller.click_by_image("Icons/Profile_Logout_Icon.png")
        sleep(1)

        if controller.click_by_image("Icons/login_register_icon.png"):
            log("Login button clicked")
        else:
            fail_log("Login button not clicked", "005", img_service)

        sleep(0.2)
        if controller.is_text_present("Login failed"):
            log("Login failed message displayed")
        else:
            fail_log("Login failed message not displayed", "005", img_service)

    except Exception as e:
        error_log(e, "005")

def App_Log_in_Log_out_006():
    try:
        if compare_with_expected_crop("Images/My_Bentley_Login_Page.png"):
            error_log("Not logged in. Cannot login without a network connection", "006", img_service)
        else:
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            if controller.click_by_image("Icons/Profile_Icon.png"):
                log("Successfully opened profile page in flight mode")
            else:
                fail_log("Unsuccessfully opened profile page in flight mode", "006", img_service)

            controller.click_text("General")
            controller.click_by_image("Icons/Profile_Logout_Icon.png")
            controller.click_text("Log out")

            if compare_with_expected_crop("Images/My_Bentley_Login_Page.png"):
                log("Successfully logged out in flight mode")
            else:
                fail_log("Unsuccessfully logged out in flight mode", "006", img_service)

    except Exception as e:
        error_log(e, "006", img_service)

def App_Log_in_Log_out_007():
    try:
        log("Cannot check style guide")
    except Exception as e:
        error_log(e, "007", img_service)