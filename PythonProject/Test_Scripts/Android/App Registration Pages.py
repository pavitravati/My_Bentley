from common_utils.android_image_comparision import *
from core.log_emitter import log, fail_log, error_log, blocked_log, runtime_log
from time import sleep
import random
from core.globals import current_vin
from gui.manual_check import manual_check
from core.app_functions import app_login_setup, app_logout_setup, service_reset
from core.screenrecord import ScreenRecorder
from core import globals

img_service = "App Registration Pages"
random_email = f"automation{str(random.random())[2:6]}@gqm.anonaddy.com"
recorder = ScreenRecorder(device_serial=controller.d.serial)

def App_Registration_Pages_001():
    recorder.start(f"{img_service}-001")
    try:
        if app_logout_setup():

            if controller.wait_for_text_and_click("LOGIN OR REGISTER"):
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
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        service_reset() if globals.test_failed else None

# Maybe split the part after verification to this part where you login and add vin
def App_Registration_Pages_002():
    recorder.start(f"{img_service}-002")
    try:
        if app_logout_setup():
            if controller.wait_for_text_and_click("LOGIN OR REGISTER"):
                log("Login button clicked")
            else:
                fail_log("Login button not clicked", "002", img_service)

            if controller.wait_for_text("WELCOME", 30):
                controller.enter_text(f"%s%s%s%s%s{random_email}")
                sleep(2)
                password = "Password1!"
                controller.enter_text(password)
                controller.click_text("CREATE")
                while not compare_with_expected_crop("Icons/accept_icon.png"):
                    sleep(0.5)
                if controller.click_by_image("Icons/accept_icon.png"):
                    log("Email and Password entered")
                    if controller.wait_for_text("CHECK YOUR INBOX"):
                        log("Email verification sent")
                        controller.swipe_up()
                        controller.click_text("RETURN TO LOGIN")
                        while not compare_with_expected_crop("Icons/next_icon.png"):
                            sleep(0.5)
                        controller.click_by_image("Images/next_icon.png")
                        manual_check(
                            instruction=f"Wait for new confirmation email and confirm it.",
                            test_id="002",
                            service=img_service,
                            take_screenshot=False
                        )
                        controller.enter_text(password)
                        controller.wait_for_text("Allow access")
                        controller.swipe_up()
                        controller.click_text("ALLOW")
                        controller.wait_for_text("REJECT")
                        log("Returned to login page when T&Cs rejected") if controller.wait_for_text_and_click("LOGIN OR REGISTER") else fail_log("Failed to return to login page when T&Cs rejected", "002", img_service)
                        controller.wait_for_text("WELCOME", 30)
                        controller.enter_text(f"%s%s%s%s%s{random_email}")
                        controller.wait_for_text("Log in – Enter password")
                        controller.enter_text(password)
                        controller.wait_for_text_and_click("ACCEPT")
                        if controller.wait_for_text("DASHBOARD"):
                            log("New account successfully logged in")
                            controller.swipe_up()
                            controller.click_text("ADD A VEHICLE")
                            controller.swipe_up()
                            controller.enter_text(current_vin)
                            log("VIN entered") if controller.wait_for_text("YOUR PREFERRED BENTLEY RETAILER") else fail_log("VIN not entered", "002", img_service)
                            controller.click_by_image("Icons/Homescreen_Right_Arrow.png")
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
                            controller.click_text("Continue")
                            log("Phone number added") if controller.wait_for_text("Request Submitted") else fail_log("Phone number not added", "002", img_service)
                            controller.click_text("CONTINUE")
                            log("Vehicle added to new account") if controller.click_by_image("Icons/Homescreen_Left_Arrow.png") else fail_log("Vehicle not added to new account", "002", img_service)
                            controller.swipe_up()
                            controller.click_text("SET MY PIN")
                            controller.click_text("New PIN")
                            controller.enter_pin("1234")
                            controller.enter_pin("1234")
                            controller.click_text("SET PIN")
                            if controller.is_text_present("PRIMARY USER ALREADY SET"):
                                log("Primary user already set, so cannot verify remote services")
                            else:
                                if compare_with_expected_crop("Icons/lock_icon.png"):
                                    log("Remote service verified")
                                elif compare_with_expected_crop("Icons/Remote_Lock_Unavailable_Icon.png"):
                                    log("Remote services unavailable")
                                else:
                                    controller.swipe_down()
                                    if compare_with_expected_crop("Icons/lock_icon.png"):
                                        log("Remote service verified")
                                    elif compare_with_expected_crop("Icons/Remote_Lock_Unavailable_Icon.png"):
                                        log("Remote services unavailable")
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
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        service_reset() if globals.test_failed else None

def App_Registration_Pages_003():
    recorder.start(f"{img_service}-003")
    try:
        if app_login_setup():

            controller.click_by_image("Icons/Profile_Icon.png")
            controller.click_text("Account")
            controller.click_text("Delete account")
            controller.click_text("DELETE ACCOUNT")
            while compare_with_expected_crop("Images/bentley_loading_image.png"):
                sleep(1)
            sleep(1)
            log("Account deletion process started") if controller.click_by_image("Icons/Cancel_id.png") else fail_log("Account deletion failed to be started", "003", img_service)
            controller.click_by_image("Icons/cancel_checkbox.png")
            controller.click_by_image("Icons/continue_cancel.png")
            log("Account deletion form filled out successfully") if controller.wait_for_text("CANCEL") else fail_log("Account deletion from not filled out successfully", "003", img_service)
            sleep(1)
            password = "Password1!"
            controller.enter_text(password)
            log("Account deletion process completed") if controller.wait_for_text("LOGIN OR REGISTER") else fail_log("Account deletion process failed", "003", img_service)
    except Exception as e:
        error_log(e, "003", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        service_reset() if globals.test_failed else None

def App_Registration_Pages_004():
    try:
        blocked_log("Test blocked - Can't check style guide")
    except Exception as e:
        error_log(e, "004", img_service)
