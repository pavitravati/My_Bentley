from time import sleep
from common_utils.android_image_comparision import *
import core.globals as globals

def app_logout():
    controller.click_by_image("Icons/Logout_Icon.png")
    controller.click_by_image("Icons/Profile_Icon.png")
    controller.click_text("General")
    controller.click_by_image("Icons/Profile_Logout_Icon.png")
    controller.click_by_image("Icons/Logout_btn.png")
    if controller.wait_for_text("LOGIN OR REGISTER", 30):
        return True
    else:
        return False

def app_login(email=globals.current_email, password=globals.current_password):
    success_tracker = []
    sleep(1)
    success_tracker.append(True) if controller.click_by_image("Icons/login_register_icon.png") else success_tracker.append(False)
    controller.wait_for_text("WELCOME", 30)
    while controller.is_text_present("WELCOME"):
        controller.enter_text(f"%s%s%s%s%s{email}")
        sleep(1)
    # sleep(2)
    controller.wait_for_text("Log in – Enter password")
    if not controller.is_text_present("CREATE ACCOUNT"):
        while controller.is_text_present("Log in – Enter password"):
            controller.enter_text(password)
            sleep(2)
            if controller.is_text_present("Sorry, wrong password. Please try again"):
                success_tracker.append(False)
                return success_tracker
    else:
        controller.click_by_image("Icons/login_page_x.png")
        app_login(email, password)
    success_tracker.append(True) if controller.wait_for_text("DASHBOARD") else success_tracker.append(False)

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
            sleep(0.5)
            return True
    return False