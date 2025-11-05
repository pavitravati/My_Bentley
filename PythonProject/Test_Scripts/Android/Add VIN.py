from common_utils.android_image_comparision import *
from core.log_emitter import log, fail_log, error_log, metric_log
from time import sleep
import random
from core.app_functions import app_login

img_service = "Add VIN"
random_email = f"automation{str(random.random())[2:6]}@gqm.anonaddy.com"

def Add_VIN_001():
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
                    controller.wait_for_text_and_click("ACCEPT")
                    if controller.wait_for_text("DASHBOARD"):
                        log("New account successfully logged in")
                        controller.swipe_up()
                        controller.click_text("ADD A VEHICLE")
                        controller.swipe_up()
                        vin = 'SJAAE14V3TC029739'
                        # vin = globals.current_VIN
                        controller.enter_text(vin)
                        log("VIN entered") if controller.wait_for_text("YOUR PREFERRED BENTLEY RETAILER") else fail_log("VIN not entered", "001", img_service)
                        controller.click("Icons/Homescreen_Right_Arrow.png")
                        controller.click_text("Bentley Manchester")
                        controller.click_text("CONFIRM")
                        log("Retailer selected") if controller.wait_for_text("ADD YOUR BENTLEY") else fail_log("Retailer failed to be selected", "001", img_service)
                        controller.click_text("CONTINUE")
                        controller.click_text("First Name")
                        controller.enter_text("first")
                        controller.click_text("Next")
                        controller.enter_text("last")
                        controller.click_text("YOUR DETAILS")
                        controller.click_text("CONTINUE")
                        log("Name entered") if controller.click_text("Location") else fail_log("Name not entered","001", img_service)
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
                        log("Location details entered") if controller.wait_for_text_and_click(
                            "Area Code") else fail_log("Location details not entered", "001", img_service)
                        controller.swipe_up(0.035)
                        controller.click_text("+44")
                        controller.click_text("Mobile Phone")
                        controller.enter_text("07818014437")
                        # controller.click() # What to click
                        controller.click_text("Continue")
                        log("Phone number added") if controller.wait_for_text("Request Submitted") else fail_log("Phone number not added", "001", img_service)
                        controller.click_text("CONTINUE")
                        log("Vehicle added to new account") if controller.click_by_image("Icons/Homescreen_Left_Arrow.png") else fail_log("Vehicle not added to new account", "001", img_service)
                    else:
                        fail_log("New account failed to be logged in", "001", img_service)
                else:
                    fail_log("Email verification page not displayed", "001", img_service)
            else:
                fail_log("Failed to enter email and password", "001", img_service)
        else:
            fail_log("Failed to create an account", "001", img_service)
    except Exception as e:
        error_log(e, "001", img_service)

def Add_VIN_002():
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
                    controller.wait_for_text_and_click("ACCEPT")
                    if controller.wait_for_text("DASHBOARD"):
                        log("New account successfully logged in")
                        controller.swipe_up()
                        controller.click_text("ADD A VEHICLE")
                        controller.swipe_up()
                        # Check how to add VIN this way
                        log("VIN entered") if controller.wait_for_text("YOUR PREFERRED BENTLEY RETAILER") else fail_log("VIN not entered", "002", img_service)
                        controller.click("Icons/Homescreen_Right_Arrow.png")
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
                        log("Vehicle added to new account") if controller.click_by_image(
                            "Icons/Homescreen_Left_Arrow.png") else fail_log("Vehicle not added to new account", "002", img_service)
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

def Add_VIN_003():
    try:
        if compare_with_expected_crop("Images/My_Bentley_Login_Page.png"):
            app_login()



    except Exception as e:
        error_log(e, "003", img_service)

def Add_VIN_004():
    try:
        pass
    except Exception as e:
        error_log(e, "004", img_service)

def Add_VIN_005():
    try:
        pass
    except Exception as e:
        error_log(e, "005", img_service)

def Add_VIN_006():
    try:
        pass
    except Exception as e:
        error_log(e, "006", img_service)

def Add_VIN_007():
    try:
        pass
    except Exception as e:
        error_log(e, "007", img_service)

def Add_VIN_008():
    try:
        pass
    except Exception as e:
        error_log(e, "008", img_service)

def Add_VIN_009():
    try:
        pass
    except Exception as e:
        error_log(e, "009", img_service)

def Add_VIN_010():
    try:
        pass
    except Exception as e:
        error_log(e, "010", img_service)

def Add_VIN_011():
    try:
        pass
    except Exception as e:
        error_log(e, "011", img_service)

def Add_VIN_012():
    try:
        pass
    except Exception as e:
        error_log(e, "012", img_service)

def Add_VIN_013():
    try:
        pass
    except Exception as e:
        error_log(e, "013", img_service)

def Add_VIN_014():
    try:
        pass
    except Exception as e:
        error_log(e, "014", img_service)

def Add_VIN_015():
    try:
        pass
    except Exception as e:
        error_log(e, "015", img_service)

def Add_VIN_016():
    try:
        pass
    except Exception as e:
        error_log(e, "016", img_service)

def Add_VIN_017():
    try:
        pass
    except Exception as e:
        error_log(e, "017", img_service)