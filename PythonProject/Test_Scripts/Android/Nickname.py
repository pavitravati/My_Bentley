from time import sleep
from common_utils.android_image_comparision import *
from core.log_emitter import log, fail_log, error_log, blocked_log
from core.app_functions import app_login, app_login_setup, identify_car, app_logout_setup
from core.globals import manual_run

img_service = "Nickname"

def nickname_page(num):
    if controller.click_by_image("Icons/info_btn.png"):
        log("Info icon clicked")
    else:
        fail_log("Info icon not clicked", num, img_service)

    if controller.click_by_image("Icons/edit_name.png"):
        log("Edit button clicked")
    else:
        fail_log("Edit button not clicked", num, img_service)

def Nickname_001():
    try:
        if app_login_setup():
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            car_name = identify_car()
            controller.click_by_image("Icons/info_btn.png")

            if controller.count_text(text=car_name) == 2 and controller.is_text_present("Vehicle name") and controller.is_text_present("Model"):
                log("Default vehicle details displayed")
            else:
                fail_log("Default vehicle details not displayed", "001", img_service)

            controller.click_by_image("Icons/back_icon.png")

    except Exception as e:
        error_log(e, "001", img_service)

def Nickname_002():
    try:
        if app_login_setup():
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            car_name = identify_car().upper()

            if controller.is_text_present(car_name):
                log("Default vehicle name displayed")
            else:
                fail_log("Default vehicle name not displayed", "002", img_service)

    except Exception as e:
        error_log(e, "002", img_service)

def Nickname_003():
    try:
        if app_login_setup():
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            car_name = identify_car()

            if controller.click_by_image("Icons/info_btn.png"):
                log("Info icon clicked")
            else:
                fail_log("Info icon not clicked", "003", img_service)

            current_nickname = controller.d.xpath('//android.widget.TextView[@text="Vehicle name"]/following-sibling::android.widget.TextView[1]').get_text()
            if not current_nickname == car_name:
                controller.click_by_image("Icons/edit_name.png")
                controller.clear_text(len(current_nickname))
                controller.swipe_down()
                controller.click_by_image("Icons/save_enabled.png")
                sleep(3)

            if controller.click_by_image("Icons/edit_name.png"):
                log("Edit button clicked")
            else:
                fail_log("Edit button not clicked", "003", img_service)

            controller.swipe_down()

            if compare_with_expected_crop("Icons/save_disabled.png"):
                log("Save button is present and disabled when name unedited")
            else:
                fail_log("Save button is not present or disabled when name unedited", "003", img_service)

            controller.click_text(car_name)
            controller.enter_text(f"{car_name}123")
            controller.swipe_down()
            if compare_with_expected_crop("Icons/save_enabled.png"):
                log("Save button is present and disabled when name edited")
            else:
                fail_log("Save button is not present or disabled when name edited", "003", img_service)

            controller.click_by_image("Icons/back_icon.png")
            controller.click_by_image("Icons/back_icon.png")

    except Exception as e:
        error_log(e, "003", img_service)

def Nickname_004():
    try:
        if app_login_setup():
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            car_name = identify_car()
            nickname_page("004")

            controller.enter_text(f"{car_name}123")
            sleep(1)
            if controller.click_by_image("Icons/save_enabled.png"):
                log("Nickname edited successfully")
                sleep(3)
            else:
                fail_log("Nickname edited unsuccessfully", "004", img_service)
                controller.click_by_image("Icons/Homescreen_Left_Arrow.png")
            controller.click_by_image("Icons/back_icon.png")

            if controller.wait_for_text(f"{car_name.upper()}123") and controller.is_text_present("DASHBOARD"):
                log("Nickname displayed successfully")
            else:
                fail_log("Nickname displayed unsuccessfully", "004", img_service)#

            if manual_run:
                nickname_page("004")
                controller.clear_text(len(f"{car_name}123"))
                controller.swipe_down()
                controller.click_by_image("Icons/save_enabled.png")
                sleep(3)
                controller.click_by_image("Icons/back_icon.png")

    except Exception as e:
        error_log(e, "004", img_service)

def Nickname_005():
    try:
        if app_login_setup():
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            car_name = identify_car()

            if controller.click_by_image("Icons/info_btn.png"):
                log("Info icon clicked")
            else:
                fail_log("Info icon not clicked", "005", img_service)

            current_nickname = controller.d.xpath('//android.widget.TextView[@text="Vehicle name"]/following-sibling::android.widget.TextView[1]').get_text()
            if current_nickname == car_name:
                controller.click_by_image("Icons/edit_name.png")
                controller.clear_text(len(current_nickname))
                controller.enter_text(f"{car_name}123")
                controller.swipe_down()
                controller.click_by_image("Icons/save_enabled.png")
                sleep(3)

            if controller.click_by_image("Icons/edit_name.png"):
                log("Edit button clicked")
            else:
                fail_log("Edit button not clicked", "005", img_service)
            controller.swipe_down()

            if compare_with_expected_crop("Icons/save_disabled.png"):
                log("Save button is present and disabled when name unedited")
            else:
                fail_log("Save button is not present or disabled when name unedited", "005", img_service)

            controller.click_by_image("Icons/back_icon.png")
            controller.click_by_image("Icons/edit_name.png")
            controller.clear_text(1)
            controller.swipe_down()
            if compare_with_expected_crop("Icons/save_enabled.png"):
                log("Save button is present and enabled when name edited")
            else:
                fail_log("Save button is not present or enabled when name edited", "005", img_service)

            controller.click_by_image("Icons/back_icon.png")
            controller.click_by_image("Icons/back_icon.png")

            if manual_run:
                nickname_page("005")
                controller.clear_text(len(f"{car_name}123"))
                controller.swipe_down()
                controller.click_by_image("Icons/save_enabled.png")
                sleep(3)
                controller.click_by_image("Icons/back_icon.png")

    except Exception as e:
        error_log(e, "005", img_service)

def Nickname_006():
    try:
        if app_login_setup():
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            if controller.click_by_image("Icons/info_btn.png"):
                log("Info icon clicked")
            else:
                fail_log("Info icon not clicked", "006", img_service)

            current_nickname = controller.d.xpath('//android.widget.TextView[@text="Vehicle name"]/following-sibling::android.widget.TextView[1]').get_text()

            if controller.click_by_image("Icons/edit_name.png"):
                log("Edit button clicked")
            else:
                fail_log("Edit button not clicked", "006", img_service)
            controller.clear_text(len(current_nickname))
            controller.enter_text("testingnickname12345")
            sleep(1)

            if controller.click_by_image("Icons/save_enabled.png"):
                log("19 Character nickname edited successfully")
                sleep(3)
            else:
                fail_log("19 Character nickname edited unsuccessfully", "006", img_service)
                controller.click_by_image("Icons/Homescreen_Left_Arrow.png")
            controller.click_by_image("Icons/back_icon.png")
            if controller.is_text_present("TESTINGNICKNAME1234") and controller.is_text_present("DASHBOARD"):
                log("19 Character nickname displayed successfully")
            else:
                fail_log("19 Character nickname displayed unsuccessfully", "006", img_service)

            if manual_run:
                nickname_page("006")
                controller.clear_text(len(f"testingnickname1234"))
                controller.swipe_down()
                controller.click_by_image("Icons/save_enabled.png")
                sleep(3)
                controller.click_by_image("Icons/back_icon.png")

    except Exception as e:
        error_log(e, "006", img_service)

# text function can't do special chars so this is dodgy using pics of the keyboard
def Nickname_007():
    try:
        if app_login_setup():
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            if controller.click_by_image("Icons/info_btn.png"):
                log("Info icon clicked")
            else:
                fail_log("Info icon not clicked", "007", img_service)

            current_nickname = controller.d.xpath('//android.widget.TextView[@text="Vehicle name"]/following-sibling::android.widget.TextView[1]').get_text()

            if controller.click_by_image("Icons/edit_name.png"):
                log("Edit button clicked")
            else:
                fail_log("Edit button not clicked", "007", img_service)
            controller.clear_text(len(current_nickname))
            controller.click_by_image("Icons/special_char_icon.png")
            controller.click_text("!")
            controller.click_by_image("Icons/emoji_icon.png")
            controller.click(500, 1800)
            controller.swipe_down()

            if controller.click_by_image("Icons/save_enabled.png"):
                log("Special character nickname edited successfully")
                sleep(3)
            else:
                fail_log("Special character nickname edited unsuccessfully", "007", img_service)
                controller.click_by_image("Icons/Homescreen_Left_Arrow.png")
            controller.click_by_image("Icons/back_icon.png")

            if compare_with_expected_crop("Icons/special_char_name.png"):
                log("Special character nickname displayed successfully")
            else:
                fail_log("Special character nickname displayed unsuccessfully", "007", img_service)

            if manual_run:
                nickname_page("007")
                controller.clear_text(2)
                controller.swipe_down()
                controller.click_by_image("Icons/save_enabled.png")
                sleep(3)
                controller.click_by_image("Icons/back_icon.png")

    except Exception as e:
        error_log(e, "007", img_service)

# Again uses pics of keyboard, picture only works for uk keyboard.
def Nickname_008():
    try:
        if app_login_setup():
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            if controller.click_by_image("Icons/info_btn.png"):
                log("Info icon clicked")
            else:
                fail_log("Info icon not clicked", "008", img_service)

            current_nickname = controller.d.xpath('//android.widget.TextView[@text="Vehicle name"]/following-sibling::android.widget.TextView[1]').get_text()

            if controller.click_by_image("Icons/edit_name.png"):
                log("Edit button clicked")
            else:
                fail_log("Edit button not clicked", "008", img_service)
            controller.clear_text(len(current_nickname))
            controller.click_by_image("Icons/uk_space_icon.png")
            controller.swipe_down()

            if compare_with_expected_crop("Icons/save_disabled.png"):
                log("Save disabled for nickname with space")
            elif compare_with_expected_crop("Icons/save_enabled.png"):
                fail_log("Save disabled for nickname with space", "008", img_service)

            controller.click_by_image("Icons/back_icon.png")
            controller.click_by_image("Icons/back_icon.png")

    except Exception as e:
        error_log(e, "008", img_service)

def Nickname_009():
    try:
        if app_login_setup():
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            car_name = identify_car()

            if controller.click_by_image("Icons/info_btn.png"):
                log("Info icon clicked")
            else:
                fail_log("Info icon not clicked", "009", img_service)

            current_nickname = controller.d.xpath('//android.widget.TextView[@text="Vehicle name"]/following-sibling::android.widget.TextView[1]').get_text()

            if controller.click_by_image("Icons/edit_name.png"):
                log("Edit button clicked")
            else:
                fail_log("Edit button not clicked", "009", img_service)
            controller.clear_text(len(current_nickname))
            controller.enter_text(f"{car_name}123")
            sleep(1)
            if controller.click_by_image("Icons/save_enabled.png"):
                log("Nickname edited successfully")
            else:
                fail_log("Nickname edited unsuccessfully", "009", img_service)
                controller.click_by_image("Icons/back_icon.png")
            sleep(3)
            controller.click_by_image("Icons/back_icon.png")

            if app_logout_setup():
                log("Logged out")
            else:
                log("Failed to log out")

            app_login()
            if compare_with_expected_crop("Images/My_Bentley_Dashboard.png"):
                log("Logged in")
            else:
                fail_log("Failed to login", "009", img_service)

            if controller.is_text_present(f"{car_name.upper()}123"):
                log("Nickname displayed in dashboard screen successfully")
            else:
                fail_log("Nickname displayed in dashboard screen unsuccessfully", "009", img_service)

            controller.click_by_image("Icons/info_btn.png")
            if controller.is_text_present(f"{car_name.upper()}123"):
                log("Nickname displayed in vehicle details screen successfully")
            else:
                fail_log("Nickname displayed in vehicle details screen unsuccessfully", "009", img_service)

            #Reset the nickname
            controller.click_by_image("Icons/edit_name.png")
            controller.clear_text(12)
            controller.swipe_down()
            controller.click_text("SAVE")
            sleep(3)
            controller.click_by_image("Icons/back_icon.png")

    except Exception as e:
        error_log(e, "009", img_service)

def Nickname_010():
    try:
        blocked_log("Test blocked - Can't check style guide")
    except Exception as e:
        error_log(e, "010", img_service)