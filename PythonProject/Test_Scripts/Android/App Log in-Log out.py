from time import sleep
from common_utils.android_image_comparision import *
from core.log_emitter import log_emitter

def log(msg):
    log_emitter.log_signal.emit(msg)

def fail_log(msg, num):
    log(f"{msg}")
    controller.take_fail_screenshot(f"App Log in-Log out-{msg}-{num}.png")

def error_log(e, num):
    log(f"⚠️ - Unexpected error: {e}")
    controller.take_fail_screenshot(f"App Log in-Log out-{e}-{num}.png")

# This is very dodgy if the phone is slow/slow internet
def App_Log_in_Log_out_001():
    try:
        # If not on the login page, attempts to log out/exit demo mode
        if not compare_with_expected_crop("Images/My_Bentley_Login_Page.png"):
            controller.click_by_image("Icons/Logout_Icon.png")
            controller.click_by_image("Icons/Profile_Icon.png")
            controller.click_text("General")
            controller.click_by_image("Icons/Profile_Logout_Icon.png")
        sleep(1)

        if controller.click_by_image("Icons/login_register_icon.png"):
            log("✅ - Login button clicked")
        else:
            fail_log("❌ - Login button not clicked", "001")

        if controller.wait_for_text("WELCOME", 30):
            # add the spaces(%s) so that if first chars get cut off it still works
            email = "%s%s%s%s%s%s%s%stestdrive@gqm.anonaddy.com"
            controller.enter_text(email)
            sleep(5)
            password = "Password1!"
            controller.enter_text(password)
            log("✅ - Email and Password entered")
        else:
            fail_log("❌ - Email and Password not entered", "001")

        if controller.wait_for_text("DASHBOARD"):
            log("✅ - Dashboard screen not launched")
        else:
            fail_log("❌ - Dashboard screen not launched", "001")

    except Exception as e:
        error_log(e, "001")

def App_Log_in_Log_out_002():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/Profile_Icon.png")
        sleep(0.2)
        controller.click_text("General")
        sleep(0.2)
        controller.click_text("Log out")
        sleep(0.2)

        if controller.click_text("Cancel"):
            log("✅ - Cancel clicked on popup")
        else:
            fail_log("❌ - Cancel not clicked on popup", "002")

        if compare_with_expected_crop("Images/Profile_Screen.png"):
            log("✅ - Popup closed")
        else:
            fail_log("❌ - Popup not closed", "002")

        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "002")

# Testcase edited in excel, no second pop up about saved favourites.
def App_Log_in_Log_out_003():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        if controller.click_by_image("Icons/Profile_Icon.png"):
            log("✅ - Profile icon clicked")
        else:
            fail_log("❌ - Profile icon not clicked", "003")
        sleep(0.2)
        if controller.click_text("General"):
            log("✅ - General tab clicked")
        else:
            fail_log("❌ - General tab not clicked", "003")
        sleep(0.2)
        if controller.click_text("Log out"):
            log("✅ - Log out button clicked")
        else:
            fail_log("❌ - Log out button not clicked", "003")
        sleep(0.2)
        if controller.click_by_image("Icons/Logout_btn.png"):
            log("✅ - Logged out of account")
        else:
            fail_log("❌ - Not logged out of account", "003")
        sleep(5)

        controller.click_by_image("Icons/login_register_icon.png")

        # Logs in so test case finishes on dashboard
        if controller.wait_for_text("WELCOME", 30):
            email = "%s%s%s%s%s%s%s%stestdrive@gqm.anonaddy.com"
            controller.enter_text(email)
            sleep(5)
            password = "Password1!"
            controller.enter_text(password)

    except Exception as e:
        error_log(e, "003")

def App_Log_in_Log_out_004():
    try:
        pass
    except Exception as e:
        error_log(e, "004")

def App_Log_in_Log_out_005():
    try:
        pass
    except Exception as e:
        error_log(e, "005")

def App_Log_in_Log_out_006():
    try:
        pass
    except Exception as e:
        error_log(e, "006")

def App_Log_in_Log_out_007():
    try:
        pass
    except Exception as e:
        error_log(e, "007")