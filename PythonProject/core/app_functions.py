from time import sleep
from common_utils.android_image_comparision import *
import gui.globals as globals

def app_logout():
    controller.click_by_image("Icons/Profile_Icon.png")
    controller.click_text("General")
    controller.click_by_image("Icons/Profile_Logout_Icon.png")
    controller.click_by_image("Icons/Logout_btn.png")
    if controller.wait_for_text("LOGIN OR REGISTER"):
        return True
    else:
        return False

def app_login(email=globals.current_email, password=globals.current_password):
    controller.click_by_image("Icons/login_register_icon.png")
    controller.wait_for_text("WELCOME", 30)
    while controller.is_text_present("WELCOME"):
        controller.enter_text(email)
        sleep(1)
    sleep(5)
    if not controller.is_text_present("CREATE ACCOUNT"):
        while controller.is_text_present("Log in – Enter password"):
            controller.enter_text(password)
            sleep(1)
    else:
        controller.click_by_image("Icons/login_page_x.png")
        app_login()
    if controller.wait_for_text("DASHBOARD"):
        return True
    else:
        return False