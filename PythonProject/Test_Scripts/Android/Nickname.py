from time import sleep
from common_utils.android_image_comparision import *
from core.log_emitter import log_emitter

# Swapped around testcase 4 and 5 here and in the Excel sheet I used

def log(msg):
    log_emitter.log_signal.emit(msg)

def fail_log(msg, num):
    log(f"{msg}")
    controller.take_fail_screenshot(f"Nickname-{msg}-{num}.png")

def error_log(e, num):
    log(f"⚠️ - Unexpected error: {e}")
    controller.take_fail_screenshot(f"Nickname-{e}-{num}.png")

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

def nickname_page(num):
    if controller.click_by_image("Icons/info_btn.png"):
        log("✅ - Info icon clicked")
    else:
        fail_log("❌ - Info icon not clicked", num)

    if controller.click_by_image("Icons/edit_name.png"):
        log("✅ - Edit button clicked")
    else:
        fail_log("❌ - Edit button not clicked", num)

def Nickname_001():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        car_name = identify_car()
        controller.click_by_image("Icons/info_btn.png")

        if controller.count_text(text=car_name) == 2 and controller.is_text_present("Vehicle name") and controller.is_text_present("Model"):
            log("✅ - Default vehicle details displayed")
        else:
            fail_log("❌ - Default vehicle details not displayed", "001")

        controller.click_by_image("Icons/back_icon.png")

    except Exception as e:
        error_log(e, "001")

def Nickname_002():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        car_name = identify_car().upper()

        if controller.is_text_present(car_name):
            log("✅ - Default vehicle name displayed")
        else:
            fail_log("❌ - Default vehicle name not displayed", "002")

    except Exception as e:
        error_log(e, "002")

Nickname_002()

def Nickname_003():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        car_name = identify_car()

        nickname_page("003")

        controller.swipe_down()

        if compare_with_expected_crop("Icons/save_disabled.png"):
            log("✅ - Save button is present and disabled when name unedited")
        else:
            fail_log("❌ - Save button is not present or disabled when name unedited", "003")

        controller.click_text(car_name)
        controller.enter_text(f"{car_name}123")
        controller.swipe_down()
        if compare_with_expected_crop("Icons/save_enabled.png"):
            log("✅ - Save button is present and disabled when name edited")
        else:
            fail_log("❌ - Save button is not present or disabled when name edited", "003")

        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/back_icon.png")

    except Exception as e:
        error_log(e, "003")

def Nickname_004():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        car_name = identify_car()
        nickname_page("004")

        controller.enter_text(f"{car_name}123")
        controller.swipe_down()

        if controller.click_by_image("Icons/save_enabled.png"):
            log("✅ - Nickname edited successfully")
            sleep(5)
            controller.click_by_image("Icons/back_icon.png")
            controller.swipe_down()
        else:
            fail_log("❌ - Nickname edited unsuccessfully", "004")
            controller.click_by_image("Icons/Homescreen_Left_Arrow.png")
            controller.click_by_image("Icons/Homescreen_Left_Arrow.png")

        if controller.wait_for_text(f"{car_name}123"):
            log("✅ - Nickname displayed successfully")
        else:
            fail_log("❌ - Nickname displayed unsuccessfully", "004")

    except Exception as e:
        error_log(e, "004")

def Nickname_005():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        nickname_page("005")
        controller.swipe_down()

        if compare_with_expected_crop("Icons/save_disabled.png"):
            log("✅ - Save button is present and disabled when name unedited")
        else:
            fail_log("❌ - Save button is not present or disabled when name unedited", "005")

        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/back_icon.png")

    except Exception as e:
        error_log(e, "005")

def Nickname_006():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        nickname_page("006")
        controller.clear_text(19)
        controller.enter_text("testingnickname1234")
        controller.swipe_down()

        if controller.click_by_image("Icons/save_enabled.png"):
            log("✅ - 19 Character nickname edited successfully")
            sleep(5)
        else:
            fail_log("❌ - 19 Character nickname edited unsuccessfully", "006")
            controller.click_by_image("Icons/Homescreen_Left_Arrow.png")

        controller.click_by_image("Icons/back_icon.png")
        controller.swipe_down()
        sleep(3)

        if controller.is_text_present("testingnickname1234"):
            log("✅ - 19 Character nickname displayed successfully")
        else:
            fail_log("❌ - 19 Character nickname displayed unsuccessfully", "006")

        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/back_icon.png")

    except Exception as e:
        error_log(e, "006")

def Nickname_007():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        nickname_page("007")

        controller.clear_text(19)
        controller.enter_text("!?#£✅❌")
        controller.swipe_down()

        if controller.click_by_image("Icons/save_enabled.png"):
            log("✅ - Special character nickname edited successfully")
            sleep(5)
        else:
            fail_log("❌ - Special character nickname edited unsuccessfully", "007")
            controller.click_by_image("Icons/Homescreen_Left_Arrow.png")

        controller.click_by_image("Icons/back_icon.png")
        controller.swipe_down()
        sleep(3)

        if controller.is_text_present("!?#£✅❌"):
            log("✅ - Special character nickname displayed successfully")
        else:
            fail_log("❌ - Special character nickname displayed unsuccessfully", "007")

    except Exception as e:
        error_log(e, "007")

def Nickname_008():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        nickname_page("008")

        controller.clear_text(19)
        controller.enter_text(" ")
        controller.swipe_down()

        if compare_with_expected_crop("Icons/save_disabled.png"):
            log("✅ - Save disabled for nickname with space")
            sleep(5)
        elif compare_with_expected_crop("Icons/save_enabled.png"):
            fail_log("❌ - Save disabled for nickname with space", "008")

        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/back_icon.png")


    except Exception as e:
        error_log(e, "008")

def Nickname_009():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        car_name = identify_car()

        nickname_page("009")

        controller.clear_text(19)
        controller.enter_text(f"{car_name}123")
        controller.swipe_down()
        if controller.click_by_image("Icons/save_enabled.png"):
            log("✅ - Nickname edited successfully")
        else:
            fail_log("❌ - Nickname edited unsuccessfully", "009")
        sleep(5)

        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/Profile_Icon.png")
        controller.click_text("General")
        if controller.click_text("Log out"):
            log("✅ - Logged out")
        else:
            log("❌ - Failed to log out")

        controller.click_by_image("Icons/login_register_icon.png")
        sleep(5)
        email = "20601@gqm.anonaddy.com"
        controller.enter_text(email)
        sleep(5)
        password = "Password1!"
        controller.enter_text(password)
        sleep(5)
        if compare_with_expected_crop("Images/My_Bentley_Dashboard.png"):
            log("✅ - Logged in")
        else:
            fail_log("❌ - Failed to login", "009")

        if controller.is_text_present(f"{car_name}123"):
            log("✅ - Nickname displayed in dashboard screen successfully")
        else:
            fail_log("❌ - Nickname displayed in dashboard screen unsuccessfully", "009")

        controller.click_by_image("Icons/info_btn.png")
        if controller.is_text_present(f"{car_name}123"):
            log("✅ - Nickname displayed in vehicle details screen successfully")
        else:
            fail_log("❌ - Nickname displayed in vehicle details screen unsuccessfully", "009")

        controller.click_by_image("Icons/back_icon.png")

    except Exception as e:
        error_log(e, "009")

def Nickname_010():
    try:
        log("✅ - Cannot check style guide")
    except Exception as e:
        error_log(e, "010")