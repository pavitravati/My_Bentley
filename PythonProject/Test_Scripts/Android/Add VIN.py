from common_utils.android_image_comparision import *
from core.log_emitter import log, fail_log, error_log, blocked_log, runtime_log
from time import sleep
import random
from core.globals import current_vin, manual_run, current_email
from gui.manual_check import manual_check
from core.app_functions import app_login_setup, app_logout_setup, add_vin, delete_vin, service_reset, find_car
from core.screenrecord import ScreenRecorder
from core import globals

img_service = "Add VIN"
random_email = f"automation{str(random.random())[2:6]}@gqm.anonaddy.com"
recorder = ScreenRecorder(device_serial=controller.d.serial)

def Add_VIN_001():
    recorder.start(f"{img_service}-001")
    try:
        # if app_logout_setup():
        #
        #     if controller.wait_for_text_and_click("LOGIN OR REGISTER"):
        #         log("Login button clicked")
        #     else:
        #         fail_log("Login button not clicked", "001", img_service)
        #
        #     if controller.wait_for_text("WELCOME", 30):
        #         controller.enter_text(f"%s%s%s%s%s{random_email}")
        #         sleep(2)
        #         password = "Password1!"
        #         controller.enter_text(password)
        #         controller.click_text("CREATE")
        #         while not compare_with_expected_crop("Icons/accept_icon.png"):
        #             sleep(0.5)
        #         if controller.click_by_image("Icons/accept_icon.png"):
        #             log("Email and Password entered")
        #             if controller.wait_for_text("CHECK YOUR INBOX"):
        #                 log("Email verification sent")
        #                 controller.swipe_up()
        #                 controller.click_text("RETURN TO LOGIN")
        #                 while not compare_with_expected_crop("Icons/next_icon.png"):
        #                     sleep(0.5)
        #                 controller.click_by_image("Images/next_icon.png")
        #                 manual_check(
        #                     instruction=f"Verify the email of the new account created ({random_email}).",
        #                     test_id="001",
        #                     service=img_service,
        #                     take_screenshot=False
        #                 )
        #                 controller.enter_text(password)
        #                 sleep(5)
        #                 controller.swipe_up()
        #                 controller.click_text("ALLOW")
        #                 controller.wait_for_text_and_click("ACCEPT")
        #                 if controller.wait_for_text("DASHBOARD"):
        #                     log("New account successfully logged in")
        #                     add_vin("001", img_service, optical_check=True)
        #                 else:
        #                     fail_log("New account failed to be logged in", "001", img_service)
        #             else:
        #                 fail_log("Email verification page not displayed", "001", img_service)
        #         else:
        #             fail_log("Failed to enter email and password", "001", img_service)
        #     else:
        #         fail_log("Failed to create an account", "001", img_service)
        log("temp")
    except Exception as e:
        error_log(e, "001", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        service_reset() if globals.test_failed else None

def Add_VIN_002():
    recorder.start(f"{img_service}-002")
    try:
        # if app_login_setup():
        #     controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        #     delete_vin()
        #     add_vin("002", img_service)
        log("temp")
    except Exception as e:
        error_log(e, "002", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        service_reset() if globals.test_failed else None

def Add_VIN_003():
    recorder.start(f"{img_service}-003")
    try:
        # if app_login_setup():
        #     find_car(True, "003", img_service)
        #     controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        #     while not controller.is_text_present("ADD A VEHICLE"):
        #         controller.click_by_image("Icons/Homescreen_Right_Arrow.png")
        #     controller.small_swipe_up()
        #     sleep(0.2)
        #     controller.click_by_resource_id("uk.co.bentley.mybentley:id/button_add_dashboard_module_add_vehicle")
        #     controller.small_swipe_up()
        #     controller.click_text("Enter VIN manually")
        #     controller.enter_text(current_vin)
        #     if controller.click_by_image("Images/VIN_confirm_btn.png"):
        #         log("Already existing VIN entered")
        #     else:
        #         fail_log("Failed to manually enter existing VIN", "003", img_service)
        #
        #     controller.click_by_image("Icons/Homescreen_Right_Arrow.png")
        #     controller.wait_for_text_and_click("Search by retailer name or location")
        #     controller.enter_text("Manchester")
        #     controller.click_text("Bentley Manchester")
        #     if controller.wait_for_text_and_click("CONFIRM"):
        #         log("Retailer selected")
        #     else:
        #         fail_log("Retailer not selected", "003", img_service)
        #     if controller.wait_for_text("VIN already registered to your account", 60):
        #         log("Existing VIN error message displayed")
        #     else:
        #         fail_log("Expected error message not displayed", "003", img_service)
        #
        #     controller.click_by_image("Icons/login_page_x.png")
        #     controller.click_by_image("Icons/back_icon.png")
        #     controller.small_swipe_down()
        #     while compare_with_expected_crop("Icons/Homescreen_Left_Arrow.png"):
        #         controller.click_by_image("Icons/Homescreen_Left_Arrow.png")
        log("temp")
    except Exception as e:
        error_log(e, "003", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        service_reset() if globals.test_failed else None

def Add_VIN_004():
    recorder.start(f"{img_service}-004")
    try:
        # if app_login_setup():
        #
        #     controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        #     while not controller.is_text_present("ADD A VEHICLE"):
        #         controller.click_by_image("Icons/Homescreen_Right_Arrow.png")
        #         sleep(0.05)
        #     controller.small_swipe_up()
        #     sleep(0.2)
        #     controller.click_by_resource_id("uk.co.bentley.mybentley:id/button_add_dashboard_module_add_vehicle")
        #     controller.small_swipe_up()
        #     controller.click_text("Enter VIN manually")
        #     controller.enter_text("Test")
        #     if not controller.is_text_present("Enter VIN manually"):
        #         controller.click_text("CONFIRM")
        #         if controller.wait_for_text("Vehicle could not be added"):
        #             log("VIN not added due to Invalid VIN")
        #         else:
        #             fail_log("VIN not added error message not displayed", "004", img_service)
        #         controller.click_by_image("Icons/Error_Icon.png")
        #
        #     controller.click_by_image("Icons/back_icon.png")
        #     controller.small_swipe_down()
        #     while compare_with_expected_crop("Icons/Homescreen_Left_Arrow.png"):
        #         controller.click_by_image("Icons/Homescreen_Left_Arrow.png")
        log("temp")
    except Exception as e:
        error_log(e, "004", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        service_reset() if globals.test_failed else None

def Add_VIN_005():
    recorder.start(f"{img_service}-005")
    try:
        # if app_login_setup():
        #
        #     controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        #     while not controller.is_text_present("ADD A VEHICLE"):
        #         controller.click_by_image("Icons/Homescreen_Right_Arrow.png")
        #         sleep(0.05)
        #     controller.small_swipe_up()
        #     sleep(0.2)
        #     controller.click_by_resource_id("uk.co.bentley.mybentley:id/button_add_dashboard_module_add_vehicle")
        #     if controller.click_text("Open Camera") and controller.is_text_present("Centre your VIN in the box above"):
        #         log("Add a vehicle screen opened when 'Open Camera' is pressed")
        #     else:
        #         if controller.click_text("Go to settings"):
        #             controller.click_text("Permissions")
        #             controller.click_text("Camera")
        #             controller.click_text("Allow only while using the app")
        #             controller.launch_app("uk.co.bentley.mybentley")
        #             if controller.click_text("Open Camera") and controller.is_text_present("Centre your VIN in the box above"):
        #                 log("Add a vehicle screen opened when 'Open Camera' is pressed")
        #             else:
        #                 fail_log("Failed to open camera screen", "005", img_service)
        #         else:
        #             fail_log("Failed to open camera screen", "005", img_service)
        #         if compare_with_expected_crop("Icons/flash_clicked.png") or compare_with_expected_crop(
        #                 "Icons/flash_blackbg.png") or compare_with_expected_crop("Icons/flash_whitebg.png"):
        #             log("Flash button displayed")
        #         else:
        #             fail_log("Flash button not displayed", "005", img_service)
        #     controller.click_by_image("Icons/back_icon.png")
        #
        #     controller.small_swipe_up()
        #     if controller.click_text("Enter VIN manually"):
        #         controller.enter_text("test")
        #         if controller.is_text_present("TEST"):
        #             log("Manual VIN entry section displayed and working")
        #         else:
        #             fail_log("Manual VIN entry section displayed but not working as expected", "005", img_service)
        #     else:
        #         fail_log("Manual VIN entry section not displayed", "005", img_service)
        #
        #     if controller.is_text_present("CONFIRM"):
        #         log("Confirm button displayed")
        #     else:
        #         fail_log("Confirm button not displayed", "005", img_service)
        #
        #     controller.click_text("Locating your VIN")
        #     if controller.is_text_present("Locating your VIN") and controller.click_text("OK"):
        #         log("Locating your VIN popup displayed when 'Locating your VIN' is pressed")
        #     else:
        #         fail_log("Locating your VIN popup not displayed", "005", img_service)
        #
        #     controller.click_by_image("Icons/back_icon.png")
        #     controller.small_swipe_down()
        #     while compare_with_expected_crop("Icons/Homescreen_Left_Arrow.png"):
        #         controller.click_by_image("Icons/Homescreen_Left_Arrow.png")
        log("temp")
    except Exception as e:
        error_log(e, "005", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        service_reset() if globals.test_failed else None

def Add_VIN_006():
    recorder.start(f"{img_service}-006")
    try:
        # if app_login_setup():
        #     if manual_run:
        #         controller.d.press("recent")
        #         sleep(0.5)
        #         controller.click_text("Close all")
        #         controller.launch_app("com.android.settings")
        #         if controller.click_by_image("Icons/settings_search.png"):
        #             controller.enter_text("Bentley")
        #         controller.click_text("My Bentley")
        #         sleep(0.2)
        #         controller.click_text("Permissions")
        #         controller.click_text("Camera")
        #         controller.click_text("Allow only while using the app")
        #         controller.launch_app("uk.co.bentley.mybentley")
        #
        #     controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        #     while not controller.is_text_present("ADD A VEHICLE"):
        #         controller.click_by_image("Icons/Homescreen_Right_Arrow.png")
        #         sleep(0.05)
        #     controller.small_swipe_up()
        #     sleep(0.2)
        #     controller.click_by_resource_id("uk.co.bentley.mybentley:id/button_add_dashboard_module_add_vehicle")
        #     if controller.click_text("Open Camera") and controller.is_text_present("Centre your VIN in the box above"):
        #         log("Add a vehicle screen opened when 'Open Camera' is pressed")
        #     else:
        #         fail_log("Failed to open camera screen", "006", img_service)
        #
        #     if controller.click_by_image("Icons/flash_clicked.png"):
        #         log("Flash disabled")
        #     else:
        #         if compare_with_expected_crop("Icons/flash_blackbg.png") or compare_with_expected_crop("Icons/flash_lightbg.png"):
        #             log("Flash disabled")
        #         else:
        #             fail_log("Failed to disable flash", "006", img_service)
        #
        #     manual_check(
        #         instruction=f"Scan the VIN with the flash off.",
        #         test_id="006",
        #         service=img_service,
        #         take_screenshot=False
        #     )
        #
        #     if controller.is_text_present("CONFIRM YOUR VIN") and not controller.is_text_present("Enter VIN manually"):
        #         log("VIN scanned and displayed in VIN field")
        #     else:
        #         fail_log("VIN not scanned successfully or not displayed in VIN field", "006", img_service)
        #
        #     if controller.click_text("Scan VIN again") and controller.wait_for_text("Centre your VIN in the box above"):
        #         log("Scan VIN again button functions as expected")
        #     else:
        #         fail_log("Scan VIN again button does not function as expected", "006", img_service)
        #
        #     controller.click_by_image("Icons/back_icon.png")
        #     controller.click_by_image("Icons/back_icon.png")
        #     controller.click_by_image("Icons/back_icon.png")
        #     controller.small_swipe_down()
        #     while compare_with_expected_crop("Icons/Homescreen_Left_Arrow.png"):
        #         controller.click_by_image("Icons/Homescreen_Left_Arrow.png")
        log("temp")
    except Exception as e:
        error_log(e, "006", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        service_reset() if globals.test_failed else None

def Add_VIN_007():
    recorder.start(f"{img_service}-007")
    try:
        # if app_login_setup():
        #     if manual_run:
        #         controller.d.press("recent")
        #         sleep(0.5)
        #         controller.click_text("Close all")
        #         controller.launch_app("com.android.settings")
        #         if controller.click_by_image("Icons/settings_search.png"):
        #             controller.enter_text("Bentley")
        #         controller.click_text("My Bentley")
        #         sleep(0.2)
        #         controller.click_text("Permissions")
        #         controller.click_text("Camera")
        #         controller.click_text("Allow only while using the app")
        #         controller.launch_app("uk.co.bentley.mybentley")
        #
        #     controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        #     while not controller.is_text_present("ADD A VEHICLE"):
        #         controller.click_by_image("Icons/Homescreen_Right_Arrow.png")
        #         sleep(0.05)
        #     controller.small_swipe_up()
        #     sleep(0.2)
        #     controller.click_by_resource_id("uk.co.bentley.mybentley:id/button_add_dashboard_module_add_vehicle")
        #     if controller.click_text("Open Camera") and controller.is_text_present("Centre your VIN in the box above"):
        #         log("Add a vehicle screen opened when 'Open Camera' is pressed")
        #     else:
        #         fail_log("Failed to open camera screen", "007", img_service)
        #
        #     controller.click(950, 2050)
        #     if not controller.click_by_image("Icons/flash_blackbg.png"):
        #         controller.click_by_image("Icons/flash_lightbg.png")
        #     if compare_with_expected_crop("Icons/flash_clicked.png"):
        #         log("Flash button enabled successfully")
        #     else:
        #         fail_log("Flash button could not be enabled", "007", img_service)
        #
        #     manual_check(
        #         instruction=f"Scan the VIN with the flash on.",
        #         test_id="007",
        #         service=img_service,
        #         take_screenshot=False
        #     )
        #     if controller.is_text_present("CONFIRM YOUR VIN") and not controller.is_text_present("Enter VIN manually"):
        #         log("VIN scanned and displayed in VIN field")
        #     else:
        #         fail_log("VIN not scanned successfully or not displayed in VIN field", "007", img_service)
        #
        #     controller.click_by_image("Icons/back_icon.png")
        #     controller.click_by_image("Icons/back_icon.png")
        #     controller.small_swipe_down()
        #     while compare_with_expected_crop("Icons/Homescreen_Left_Arrow.png"):
        #         controller.click_by_image("Icons/Homescreen_Left_Arrow.png")
        log("temp")
    except Exception as e:
        error_log(e, "007", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        service_reset() if globals.test_failed else None

def Add_VIN_008():
    recorder.start(f"{img_service}-008")
    try:
        # if app_login_setup():
        #     controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        #     delete_vin()
        #     add_vin("008", img_service, optical=True)
        log("temp")
    except Exception as e:
        error_log(e, "008", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        service_reset() if globals.test_failed else None

def Add_VIN_009():
    recorder.start(f"{img_service}-009")
    try:
        if app_login_setup():
            delete_vin()
            controller.d.press("recent")
            sleep(0.5)
            controller.click_text("Close all")
            controller.launch_app("com.android.settings")
            if controller.click_by_image("Icons/settings_search.png"):
                controller.enter_text("Bentley")
            controller.click_text("My Bentley")
            sleep(0.2)
            controller.click_text("Permissions")
            sleep(0.2)
            controller.click_text("Camera")
            controller.click_text("Don't allow")
            controller.launch_app("uk.co.bentley.mybentley")

            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            add_vin("009", img_service, optical=True, settings_check=True)

    except Exception as e:
        error_log(e, "009", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        service_reset() if globals.test_failed else None

def Add_VIN_010():
    recorder.start(f"{img_service}-010")
    try:
        if app_login_setup():
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            while not controller.is_text_present("ADD A VEHICLE"):
                controller.click_by_image("Icons/Homescreen_Right_Arrow.png")
                sleep(0.05)
            controller.small_swipe_up()
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/button_add_dashboard_module_add_vehicle")
            sleep(0.5)
            if controller.click_text("Locating your VIN"):
                log("'Locating your VIN' option displayed")
            else:
                fail_log("'Locating your VIN' option not displayed", "010", img_service)

            if controller.is_text_present("Locating your VIN") and controller.wait_for_text_that_contains("VIN, or chassis number, stands for vehicle") and controller.click_text("OK"):
                log("'Locating your VIN' popup displayed")
            else:
                fail_log("'Locating your VIN' popup not displayed", "010", img_service)

            controller.click_by_image("Icons/back_icon.png")
            controller.small_swipe_down()
            while compare_with_expected_crop("Icons/Homescreen_Left_Arrow.png"):
                controller.click_by_image("Icons/Homescreen_Left_Arrow.png")

    except Exception as e:
        error_log(e, "010", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        service_reset() if globals.test_failed else None

def Add_VIN_011():
    recorder.start(f"{img_service}-011")
    try:
        if app_login_setup():

            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            while not controller.is_text_present("ADD A VEHICLE"):
                controller.click_by_image("Icons/Homescreen_Right_Arrow.png")
            controller.small_swipe_up()
            sleep(0.2)
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/button_add_dashboard_module_add_vehicle")
            controller.small_swipe_up()
            controller.click_text("Enter VIN manually")
            if not controller.click_by_image("Icons/emoji_icon.png"):
                log("Emojis are not able to be entered in VIN section")
            else:
                controller.click(500, 1800)
                if controller.is_text_present("Enter VIN manually"):
                    log("Emojis are not able to be entered in VIN section")
                else:
                    fail_log("Emojis are able to alter the VIN section", "011", img_service)
                    controller.clear_text(5)
            controller.click_by_image("Icons/keyboard_icon.png")
            if controller.click_by_image("Icons/special_char_icon.png"):
                if controller.click_by_image("Icons/!_char_icon.png") and controller.click_by_image("Icons/#_char_icon.png"):
                    if controller.is_text_present("Enter VIN manually"):
                        log("Special characters cannot be entered in the VIN section")
                    else:
                        fail_log("Special characters have altered the VIN section", "011", img_service)
                else:
                    fail_log("Special characters not found", "011", img_service)
            else:
                fail_log("Special characters not found", "011", img_service)
            sleep(1)

            controller.click_by_image("Icons/back_icon.png")
            while compare_with_expected_crop("Icons/Homescreen_Left_Arrow.png"):
                controller.click_by_image("Icons/Homescreen_Left_Arrow.png")

    except Exception as e:
        error_log(e, "011", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        service_reset() if globals.test_failed else None

def Add_VIN_012():
    recorder.start(f"{img_service}-012")
    try:
        if manual_run:
            if app_login_setup():
                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
                add_vin("012", img_service)
                manual_check(
                    instruction=f"Wait for and verify vehicle request email received to {current_email}.",
                    test_id="012",
                    service=img_service,
                    take_screenshot=False
                )
        else:
            manual_check(
                instruction=f"Verify vehicle request email received to {current_email}, from previous testcases.",
                test_id="012",
                service=img_service,
                take_screenshot=False
            )

    except Exception as e:
        error_log(e, "012", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        service_reset() if globals.test_failed else None

def Add_VIN_013():
    recorder.start(f"{img_service}-013")
    try:
        blocked_log("Test blocked - Can't check style guide")
    except Exception as e:
        error_log(e, "013", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        service_reset() if globals.test_failed else None