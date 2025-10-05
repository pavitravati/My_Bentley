from time import sleep
from common_utils.android_image_comparision import *
from common_utils.android_controller import *
from core.log_emitter import log_emitter

def log(msg):
    log_emitter.log_signal.emit(msg)

def fail_log(msg, num):
    log(f"{msg}")
    controller.take_fail_screenshot(f"MyBentleyAppLogin_{msg}_{num}.png")

def error_log(e, num):
    log(f"⚠️ - Unexpected error: {e}")
    controller.take_fail_screenshot(f"MyBentleyAppLogin_{e}_{num}.png")

def MyBentleyAppLogin_001():
    try:
        controller.launch_app("uk.co.bentley.mybentley")
        sleep(1)

        if controller.click_by_image("Icons/login_register_icon.png"):
            log("✅ - Login button clicked")
        else:
            fail_log("❌ - Login button not clicked", "001")
        sleep(5)

        if compare_with_expected_crop("Icons/bentley_login_logo.png"):
            email = "20601@gqm.anonaddy.com"
            controller.enter_text(email)
            sleep(5)
            password = "Password1!"
            controller.enter_text(password)
            log("✅ - Email and Password entered")
        else:
            fail_log("❌ - Email and Password not entered", "002")
        sleep(5)

        if compare_with_expected_crop("Images/My_Bentley_Dashboard.png"):
            log("✅ - Dashboard screen not launched, MyBentleyAppLogin_001 Passed")
        else:
            fail_log("❌ - Dashboard screen not launched, MyBentleyAppLogin_001 Failed", "001")

    except Exception as e:
        error_log(e, "001")

def MyBentleyAppLogin_002():
    try:
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
            log("✅ - Popup closed, MyBentleyAppLogin_002 Passed")
        else:
            fail_log("❌ - Popup not closed, MyBentleyAppLogin_002 Failed", "002")

        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "002")

# Testcase edited in excel, no second pop up about saved favourites.
def MyBentleyAppLogin_003():
    try:
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
        sleep(2)

        if compare_with_expected_crop("Icons/login_register_icon.png"):
            log("✅ - Signup page displayed, MyBentleyAppLogin_003 Passed")
        else:
            fail_log("❌ - Signup page not displayed, MyBentleyAppLogin_003 Failed", "003")

    except Exception as e:
        error_log(e, "002")