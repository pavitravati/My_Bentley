from common_utils.android_image_comparision import *
from core.log_emitter import log, fail_log, error_log, metric_log, blocked_log
from time import sleep
import random

img_service = "App Registration Pages"
random_email = f"automation{str(random.random())[2:6]}@gqm.anonaddy.com"

def login():
    controller.click_by_image("Icons/login_register_icon.png")
    if controller.wait_for_text("WELCOME", 30):
        controller.enter_text(random_email)
        sleep(5)
        password = "Password1!"
        controller.enter_text(password)

    if controller.wait_for_text("DASHBOARD"):
        return True
    else:
        return False

# Need throwaway emails that can be used
def App_Registration_Pages_001():
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
            controller.enter_text(f"%s%s%s%s%s{random_email}")
            sleep(2)
            password = "Password1!"
            controller.enter_text(password)
            controller.click_text("CREATE")
            log("Email and Password entered")
            sleep(1)
            if controller.click_by_image("Icons/decline_icon.png"):
                log("Decline button clicked")
                if controller.wait_for_text("WELCOME"):
                    log("Registration canceled after declining")
                else:
                    fail_log("Registration cancellation failed after declining", "001", img_service)
            else:
                fail_log("Decline button not found", "001", img_service)
        else:
            fail_log("Failed to create an account", "001", img_service)

        controller.click_by_image("Icons/login_page_x.png")

    except Exception as e:
        error_log(e, "001", img_service)

# only done EU, CHN is different - Test at home
def App_Registration_Pages_002():
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
            controller.enter_text(f"%s%s%s%s%s{random_email}")
            sleep(2)
            password = "Password1!"
            controller.enter_text(password)
            controller.click_text("CREATE")
            sleep(1)
            if controller.click_by_image("Icons/accept_icon.png"):
                log("Email and Password entered")
                if controller.wait_for_text("CHECK YOUR INBOX"):
                    log("Email verification sent")
                    controller.swipe_up()
                    controller.click_text("RETURN TO LOGIN")
                    controller.click_text("NEXT")
                    ############
                    # Wait for tester to click email verified
                    ############
                    controller.enter_text(password)
                    sleep(5)
                    controller.swipe_up()
                    controller.click_text("ALLOW")
                    controller.wait_for_text("REJECT")
                    log("Returned to login page when T&Cs rejected") if controller.wait_for_text_and_click("LOGIN OR REGISTER") else fail_log("Failed to return to login page when T&Cs rejected", "002", img_service)
                    controller.enter_text(f"%s%s%s%s%s{random_email}")
                    sleep(5)
                    password = "Password1!"
                    controller.enter_text(password)
                    controller.wait_for_text_and_click("ACCEPT")
                    if controller.wait_for_text("DASHBOARD"):
                        log("New account successfully logged in")
                        controller.swipe_up()
                        controller.click_text("ADD A VEHICLE")
                        controller.swipe_up()
                        vin = 'SJAAE14V3TC029739'
                        controller.enter_text(vin)
                        log("VIN entered") if controller.wait_for_text("YOUR PREFERRED BENTLEY RETAILER") else fail_log("VIN not entered", "002", img_service)
                        controller.click("Icons/Homescreen_Right_Arrow.png")
                        controller.wait_for_text_and_click("Search by retailer name or location")
                        controller.enter_text("Manchester")
                        controller.click_text("Bentley Manchester")
                        controller.click_text("CONFIRM")
                        log("Retailer selected") if controller.wait_for_text("ADD YOUR BENTLEY") else fail_log("Retailer failed to be selected", "002", img_service)
                        controller.click_text("CONTINUE")
                        controller.click_text("First Name")
                        controller.enter_text("first")
                        controller.click_text("Next")
                        controller.enter_text("last")
                        controller.click_text("YOUR DETAILS")
                        controller.click_text("CONTINUE")
                        log("Name entered") if controller.click_text("Location") else fail_log("Name not entered", "002", img_service)
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
                        controller.click_text("CONTINUE")
                        log("Location details entered") if controller.wait_for_text_and_click("Area Code") else fail_log("Location details not entered", "002", img_service)
                        controller.swipe_up(0.035)
                        controller.click_text("+44")
                        controller.click_text("Mobile Phone")
                        controller.enter_text("07818014437")
                        # controller.click() # What to click
                        controller.click_text("Continue")
                        log("Phone number added") if controller.wait_for_text("Request Submitted") else fail_log("Phone number not added", "002", img_service)
                        controller.click_text("CONTINUE")
                        log("Vehicle added to new account") if controller.click_by_image("Icons/Homescreen_Left_Arrow.png") else fail_log("Vehicle not added to new account", "002", img_service)
                    else:
                        fail_log("New account failed to be logged in", "002", img_service)
                else:
                    fail_log("Email verification page not displayed", "002", img_service)
            else:
                fail_log("Failed to enter email and password", "002", img_service)
        else:
            fail_log("Failed to create an account", "002", img_service)
    except Exception as e:
        error_log(e, "002", img_service)
App_Registration_Pages_002()

def App_Registration_Pages_003():
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
            fail_log("Login button not clicked", "003", img_service)

        if controller.wait_for_text("WELCOME", 30):
            controller.enter_text(f"%s%s%s%s%s{random_email}")
            sleep(5)
            password = "Password1!"
            controller.enter_text(password)
            log("Email and Password entered")
        else:
            fail_log("Email and Password not entered", "003", img_service)

        if controller.wait_for_text("DASHBOARD"):
            log("Login successful")
        else:
            fail_log("Login failed", "003", img_service)

    except Exception as e:
        error_log(e, "003", img_service)

#MOVE TO BETTER ORDER
def App_Registration_Pages_004():
    try:
        controller.click_by_image("Icons/Logout_Icon.png")
        controller.click_by_image("Icons/Profile_Icon.png")
        controller.click_text("General")
        controller.click_by_image("Icons/Profile_Logout_Icon.png")
        controller.click_by_image("Icons/Logout_btn.png")
        log("Successfully logged out") if controller.wait_for_text("LOGIN OR REGISTER") else fail_log("Failed to log out", "004", img_service)
        login()
    except Exception as e:
        error_log(e, "004", img_service)

def App_Registration_Pages_005():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/Profile_Logout_Icon.png")
        controller.click_text("Account")
        controller.click_text("Reset password")
        controller.click_text("RESET")
        log("Password reset email sent") if controller.is_text_present("CONFIRMED") else fail_log("Password reset email not sent", "005", img_service)
        controller.click_text("CLOSE")
    except Exception as e:
        error_log(e, "005", img_service)

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

def App_Registration_Pages_006():
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
            fail_log("Login button not clicked", "006", img_service)

        if controller.wait_for_text("WELCOME", 30):
            controller.enter_text(f"%s%s%s%s%s{random_email}")
            sleep(5)
            password = "Password1!"
            controller.enter_text(password)
            log("Email and Password entered")
        else:
            fail_log("Email and Password not entered", "006", img_service)

        if controller.wait_for_text("DASHBOARD"):
            log("Login successful")
        else:
            fail_log("Login failed", "006", img_service)

        log("Car is shown in the account") if identify_car() else fail_log("Car failed to show in the account", "006", img_service)

    except Exception as e:
        error_log(e, "006", img_service)

def App_Registration_Pages_007():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        if controller.is_text_present("DASHBOARD"):
            login()

        controller.click_by_image("Icons/Profile_Icon.png")
        controller.click_text("Account")
        controller.click_text("Delete account")
        controller.click_text("DELETE ACCOUNT")
        while compare_with_expected_crop("Images/loading_img.png"):
            sleep(2)
        log("Account deletion process started through logged in account") if controller.click_by_image("Icons/Cancel_id.png") else fail_log("Account deletion process not started", "007", img_service)
        controller.click_by_image("Icons/cancel_checkbox.png")
        controller.click_by_image("Icons/continue_cancel.png")
        log("Account deletion form filled out successfully") if controller.wait_for_text("CANCEL") else fail_log("Account deletion from not filled out successfully", "007", img_service)
        password = "Password1!"
        controller.enter_text(password)
        log("Account deletion process completed") if controller.wait_for_text("LOGIN OR REGISTER") else fail_log("Account deletion process failed", "007", img_service)
    except Exception as e:
        error_log(e, "007", img_service)

def App_Registration_Pages_008():
    try:
        blocked_log("Test blocked - Can't check style guide")
    except Exception as e:
        error_log(e, "008", img_service)
