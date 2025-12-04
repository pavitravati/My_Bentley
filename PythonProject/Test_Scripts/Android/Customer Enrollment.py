from common_utils.android_image_comparision import *
from core.log_emitter import log, fail_log, error_log, blocked_log, runtime_log
from core.app_functions import app_login, app_logout_setup, app_login_setup, enable_flight_mode, disable_flight_mode, \
    delete_vin, add_vin, app_refresh, service_reset, find_car
from core.globals import *
from time import sleep
import random
from core import globals
from gui.manual_check import manual_check
from core.screenrecord import ScreenRecorder
from common_utils.android_controller import *

img_service = "Customer Enrollment"
recorder = ScreenRecorder(device_serial=controller.d.serial)

def check_services_unavailable(num):
    if compare_with_expected_crop("Icons/Remote_Lock_Unavailable.png"):
        log("Remote services not available as expected")
    elif compare_with_expected_crop("Icons/lock_icon.png"):
        fail_log("Remote services still available", num, img_service)
    else:
        fail_log("Remote services not checked as remote lock not displayed", num, img_service)

def check_services_available(num):
    if compare_with_expected_crop("Icons/lock_icon.png"):
        log("Remote services are available")
    elif compare_with_expected_crop("Icons/Remote_Lock_Unavailable.png"):
        fail_log("Remote services not available", num, img_service)
    else:
        fail_log("Remote services not checked as remote lock not displayed", num, img_service)

def generate_setup(num):
    controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    find_car(True, num, img_service)
    controller.small_swipe_up()
    if controller.is_text_present("SET YOUR PRIMARY USER"):
        if not controller.is_text_present("GENERATE VEHICLE CODE"):
            controller.small_swipe_down()
            delete_vin()
            add_vin(num, img_service)
            controller.small_swipe_up()
    elif controller.is_text_present("PRIMARY USER ALREADY SET"):
        fail_log("Another user is already set as the primary user", num, img_service)
        return False
    else:
        delete_vin()
        add_vin(num, img_service)
        controller.small_swipe_up()
    return True

def view_setup(num):
    controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    find_car(True, num, img_service)
    controller.small_swipe_up()
    if controller.is_text_present("SET YOUR PRIMARY USER"):
        if not controller.is_text_present("VIEW VEHICLE CODE"):
            controller.click_text("GENERATE VEHICLE CODE")
            controller.wait_for_text_and_click("Generate vehicle code")
            controller.wait_for_text("VEHICLE CODE", 30)
            while not compare_with_expected_crop("Icons/login_page_x.png", 0.9):
                sleep(0.5)
            controller.click_by_image("Icons/login_page_x.png")
            controller.small_swipe_down()
            return True
        controller.small_swipe_down()
    elif controller.is_text_present("PRIMARY USER ALREADY SET"):
        fail_log("Another user is already set as the primary user", num, img_service)
        return False
    else:
        delete_vin()
        add_vin(num, img_service)
        controller.small_swipe_up()
        controller.click_text("GENERATE VEHICLE CODE")
        controller.wait_for_text_and_click("Generate vehicle code")
        controller.wait_for_text("VEHICLE CODE", 30)
        while not compare_with_expected_crop("Icons/login_page_x.png", 0.9):
            sleep(0.5)
        controller.click_by_image("Icons/login_page_x.png")
        controller.small_swipe_down()
    return True

def Customer_Enrollment_001():
    recorder.start(f"{img_service}-001")
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (EUR/NAR)")
        else:
            if app_login_setup():
                if generate_setup("001"):

                    manual_check(
                        instruction="In vehicle set primary user for this account\n(HMI->Settings->Users->'Set Primary User'->Enter User Name(Bentley Account ID) and FPIN(i.e. Present in Scratch Tag)->Click on 'Set Primary User')",
                        test_id="001",
                        service=img_service,
                        take_screenshot=False
                    )
                    app_refresh("001", img_service)
                    controller.swipe_up()
                    status_refresh = True if not controller.is_text_present("My car status unavailable") else False
                    if compare_with_expected_crop("Icons/unlock_Icon.png") and status_refresh:
                        log("Remote services work as expected")
                    else:
                        fail_log("Remote services do not work as expected", "001", img_service)

    except Exception as e:
        error_log(e, "001", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Customer_Enrollment_002():
    recorder.start(f"{img_service}-002")
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (EUR/NAR)")
        else:
            if app_login_setup():
                if generate_setup("002"):

                    manual_check(
                        instruction="In vehicle set primary user for this account with incorrect FPIN\n(HMI->Settings->Users->'Set Primary User'->Enter User Name(Bentley Account ID) and FPIN(i.e. Present in Scratch Tag)->Click on 'Set Primary User')\nNumber attempts remaining should be 10",
                        test_id="002",
                        service=img_service,
                        take_screenshot=False
                    )
                    controller.swipe_down()
                    if app_refresh("015", img_service):
                        if controller.is_text_present("SET YOUR PRIMARY USER"):
                            log("User is not primary user as expected")
                        else:
                            fail_log("User is primary user of the vehicle", "002", img_service)

    except Exception as e:
        error_log(e, "002", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Customer_Enrollment_003():
    recorder.start(f"{img_service}-003")
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (EUR/NAR)")
        else:
            if app_login_setup():
                if generate_setup("003"):
                    log("Set primary user title displayed") if controller.is_text_present("SET YOUR PRIMARY USER") else fail_log("Set primary user title not displayed", "003", img_service)
                    if controller.is_text_present("To set yourself as a primary user, a vehicle code will be generated in the next step. Please enter it in your Bentley infotainment system."):
                        log("Set primary user text displayed correctly")
                    else:
                        fail_log("Set primary user text not displayed correctly", "003", img_service)
                    log("Generate vehicle code button displayed") if controller.is_text_present("GENERATE VEHICLE CODE") else fail_log("Generate vehicle code button not displayed", "003", img_service)
                    controller.click_by_image("Icons/info_btn.png")
                    if controller.is_text_present("Generate a unique vehicle code* in My Bentley app. "):
                        log("Primary user instructions page displayed")
                        if compare_with_expected_crop("Images/primary_user_instructions.png"):
                            log("Primary user instructions are displayed as expected")
                        else:
                            fail_log("Primary user instructions are not displayed as expected", "003", img_service)
                    else:
                        fail_log("Primary user instructions page not displayed", "003", img_service)
                    controller.click_by_image("Icons/back_icon.png")
                    controller.small_swipe_down()
    except Exception as e:
        error_log(e, "003", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Customer_Enrollment_004():
    recorder.start(f"{img_service}-004")
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (EUR/NAR)")
        else:
            if app_login_setup():
                if generate_setup("004"):
                    enable_flight_mode()
                    if controller.wait_for_text_and_click("GENERATE VEHICLE CODE"):
                        controller.wait_for_text_and_click("Generate vehicle code")
                        if controller.wait_for_text("Error while generating a vehicle code"):
                            log("Expected error message displayed")
                        else:
                            fail_log("Expected error message not displayed", "004", img_service)
                    else:
                        fail_log("GENERATE VEHICLE CODE button not displayed", "004", img_service)
                    controller.click_by_image("Icons/Error_Icon.png")
                    while not compare_with_expected_crop("Icons/login_page_x.png", 0.9):
                        sleep(0.5)
                    controller.click_by_image("Icons/login_page_x.png")
                    controller.small_swipe_down()
                    disable_flight_mode()
    except Exception as e:
        error_log(e, "004", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Customer_Enrollment_005():
    recorder.start(f"{img_service}-005")
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (EUR/NAR)")
        else:
            if app_login_setup():
                if generate_setup("005"):
                    controller.click_text("GENERATE VEHICLE CODE")
                    if controller.wait_for_text("The vehicle code on the scratch tag will be invalidated"):
                        log("Generate vehicle code confirmation text displayed")
                    else:
                        fail_log("Generate vehicle code not displayed", "005", img_service)

                    if controller.wait_for_text("Cancel") and controller.wait_for_text_and_click("Generate vehicle code"):
                        log("Generate vehicle code and cancel buttons displayed")
                    else:
                        fail_log("Generate vehicle code or cancel button not displayed", "005", img_service)

                    latency_time = time.time()
                    if controller.wait_for_text("VEHICLE CODE", 30):
                        latency_time = time.time() - latency_time
                        if latency_time < 10:
                            log(f"New vehicle code generated and displayed in under 10 seconds ({latency_time} seconds)")
                        else:
                            fail_log(f"New vehicle code generated and displayed but in more than 10 seconds ({latency_time} seconds)", "005", img_service)
                    else:
                        fail_log("Vehicle code not displayed", "010", img_service)

                    while not compare_with_expected_crop("Icons/login_page_x.png", 0.9):
                        sleep(0.5)
                    controller.click_by_image("Icons/login_page_x.png")
                    controller.small_swipe_down()
    except Exception as e:
        error_log(e, "005", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Customer_Enrollment_006():
    recorder.start(f"{img_service}-006")
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (EUR/NAR)")
        else:
            if app_login_setup():
                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
                if app_refresh("006", img_service):
                    if view_setup("006"):
                        print(123)
                        controller.small_swipe_up()
                        if controller.click_text("VIEW VEHICLE CODE"):
                            log("View vehicle code button displayed")
                        else:
                            fail_log("View vehicle code button not displayed", "006", img_service)

                        latency_time = time.time()
                        if controller.wait_for_text("VEHICLE CODE", 30):
                            latency_time = time.time() - latency_time
                            if latency_time < 5:
                                log(f"Vehicle code displayed in under 5 seconds ({latency_time} seconds)")
                            else:
                                fail_log(f"Vehicle code displayed but in more than 5 seconds ({latency_time} seconds)", "006", img_service)
                        else:
                            fail_log("Vehicle code not displayed", "010", img_service)

                        while not compare_with_expected_crop("Icons/login_page_x.png", 0.9):
                            sleep(0.5)
                        controller.click_by_image("Icons/login_page_x.png")
                        controller.small_swipe_down()

    except Exception as e:
        error_log(e, "006", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Customer_Enrollment_007():
    recorder.start(f"{img_service}-007")
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (EUR/NAR)")
        else:
            if app_login_setup():
                view_setup("007")
                if app_refresh("007", img_service):
                    controller.small_swipe_up()
                    if controller.is_text_present("SET YOUR PRIMARY USER"):
                        manual_check(
                            instruction="Navigate to the Primary User Nomination page in HMI, enter the email address and the incorrect vehicle code\nPrimary user nomination should be blocked with 10 tries remaining",
                            test_id="007",
                            service=img_service,
                            take_screenshot=False
                        )
                        controller.small_swipe_down()
                        if app_refresh("007", img_service):
                            controller.small_swipe_up()
                            if controller.is_text_present("SET YOUR PRIMARY USER"):
                                log("Primary user not set as expected")
                            else:
                                fail_log("Primary user is set", "007", img_service)
                            controller.small_swipe_down()
                    else:
                        fail_log("Primary user is already set", "007", img_service)
    except Exception as e:
        error_log(e, "007", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Customer_Enrollment_008():
    recorder.start(f"{img_service}-008")
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (EUR/NAR)")
        else:
            if app_login_setup():
                view_setup("008")
                if app_refresh("008", img_service):
                    controller.small_swipe_up()
                    if controller.wait_for_text_and_click("VIEW VEHICLE CODE"):
                        controller.wait_for_text("VEHICLE CODE", 30)
                        vehicle_code = controller.d.xpath(
                            '//*[@text="Please enter following vehicle code in your Bentley infotainment system to set your primary user:"]/following-sibling::android.widget.TextView[1]').get_text()
                        manual_check(
                            instruction=f"On vehicle HMI navigate to Primary user page\nSuccessfully set the primary user using the vehicle code: {vehicle_code} and email: {current_email}",
                            test_id="008",
                            service=img_service,
                            take_screenshot=False
                        )
                        while not compare_with_expected_crop("Icons/login_page_x.png", 0.9):
                            sleep(0.5)
                        controller.click_by_image("Icons/login_page_x.png")
                        controller.small_swipe_down()
                        if app_refresh("008", img_service):
                            controller.small_swipe_up()
                            if not controller.is_text_present("SET YOUR PRIMARY USER") and compare_with_expected_crop("Icons/lock_icon.png"):
                                log("Primary user set and remote services enabled in the app")
                            else:
                                fail_log("Primary user failed to be set successfully", "008", img_service)
                            controller.small_swipe_up()
                    else:
                        fail_log("View vehicle code button not displayed", "008", img_service)
    except Exception as e:
        error_log(e, "008", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Customer_Enrollment_009():
    recorder.start(f"{img_service}-009")
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (EUR/NAR)")
        else:
            if app_login_setup():
                view_setup("009")
                controller.small_swipe_up()
                if controller.is_text_present("SET YOUR PRIMARY USER"):
                    if app_refresh("009", img_service):
                        controller.small_swipe_up()
                        if controller.is_text_present("SET YOUR PRIMARY USER"):
                            manual_check(
                                instruction="Navigate to the Primary User Nomination page in HMI, enter the email address and the incorrect vehicle code for 10 times\nPrimary user nomination should be blocked after 10 times",
                                test_id="009",
                                service=img_service,
                                take_screenshot=False
                            )
                            controller.small_swipe_down()
                        else:
                            fail_log("Primary user is already set", "009", img_service)
                else:
                    fail_log("Primary user is already set", "009", img_service)
    except Exception as e:
        error_log(e, "009", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Customer_Enrollment_010():
    recorder.start(f"{img_service}-010")
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (EUR/NAR)")
        else:
            if app_login_setup():
                generate_setup("010")
                if controller.click_text("GENERATE VEHICLE CODE"):
                    controller.wait_for_text_and_click("Generate vehicle code")
                    service_reset()
                    if app_refresh("010", img_service):
                        controller.small_swipe_up()
                        if controller.is_text_present("SET YOUR PRIMARY USER"):
                            log("User not primary user as expected")
                            if controller.is_text_present("VIEW VEHICLE CODE"):
                                log("View vehicle code button displayed")
                            elif controller.is_text_present("GENERATE VEHICLE CODE"):
                                log("Generate vehicle code button displayed")
                            else:
                                fail_log("Expected vehicle code button not displayed", "010", img_service)
                        else:
                            fail_log("Primary user details not displayed as expected", "010", img_service)
                else:
                    fail_log("Generate vehicle code button not displayed", "010", img_service)
                while not compare_with_expected_crop("Icons/login_page_x.png", 0.9):
                    sleep(0.5)
                controller.click_by_image("Icons/login_page_x.png")
                controller.small_swipe_down()
    except Exception as e:
        error_log(e, "010", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Customer_Enrollment_011():
    recorder.start(f"{img_service}-011")
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (EUR/NAR)")
        else:
            if app_login_setup():
                generate_setup("011")
                if controller.click_text("GENERATE VEHICLE CODE"):
                    controller.wait_for_text_and_click("Generate vehicle code")
                    controller.press_home()
                    controller.d.press("power")
                    sleep(1)
                    controller.d.press("power")
                    controller.swipe_up()
                    controller.launch_app("uk.co.bentley.mybentley")
                    if not controller.is_text_present("DASHBOARD"):
                        manual_check(
                            instruction="Unlock the phone",
                            test_id="011",
                            service=img_service,
                            take_screenshot=False
                        )
                        controller.launch_app("uk.co.bentley.mybentley")
                    if app_refresh("011", img_service):
                        controller.small_swipe_up()
                        if controller.is_text_present("SET YOUR PRIMARY USER"):
                            log("User not primary user as expected")
                            if controller.is_text_present("VIEW VEHICLE CODE"):
                                log("View vehicle code button displayed")
                            elif controller.is_text_present("GENERATE VEHICLE CODE"):
                                log("Generate vehicle code button displayed")
                            else:
                                fail_log("Expected vehicle code button not displayed", "011", img_service)
                        else:
                            fail_log("Primary user details not displayed as expected", "011", img_service)
                else:
                    fail_log("Generate vehicle code button not displayed", "011", img_service)
    except Exception as e:
        error_log(e, "011", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Customer_Enrollment_012():
    recorder.start(f"{img_service}-012")
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (EUR/NAR)")
        else:
            if app_login_setup():
                generate_setup("012")
                manual_check(
                    instruction="Click on 'GENERATE VEHICLE CODE'\nIncoming call/SMS/Alarm received during generation",
                    test_id="012",
                    service=img_service,
                    take_screenshot=False
                )
                controller.launch_app("uk.co.bentley.mybentley")
                controller.small_swipe_up()
                if controller.is_text_present("VIEW VEHICLE CODE"):
                    log("View vehicle code button displayed")
                elif controller.is_text_present("GENERATE VEHICLE CODE"):
                    log("Generate vehicle code button displayed")
                else:
                    fail_log("Expected vehicle code button not displayed", "012", img_service)
                controller.small_swipe_down()
    except Exception as e:
        error_log(e, "012", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Customer_Enrollment_013():
    recorder.start(f"{img_service}-013")
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (EUR/NAR)")
        else:
            if app_logout_setup():
                manual_check(
                    instruction="Remove the primary user in vehicle (In HMI->Settings->Users->Select the Primary User->Click on Gear Icon->'Remove Primary User')",
                    test_id="013",
                    service=img_service,
                    take_screenshot=False
                )
                if app_login_setup():
                    find_car("013", img_service)
                    controller.small_swipe_up()
                    if controller.wait_for_text("SET YOUR PRIMARY USER") and controller.click_text("VIEW VEHICLE CODE"):
                        log("Primary user section displayed correctly")
                        if not controller.wait_for_text("VEHICLE CODE"):
                            fail_log("View vehicle code button did not work as expected", "013", img_service)
                        while not compare_with_expected_crop("Icons/login_page_x.png", 0.9):
                            sleep(0.5)
                        controller.click_by_image("Icons/login_page_x.png")
                    else:
                        fail_log("Primary user section not displayed", "013", img_service)
                    controller.small_swipe_down()

    except Exception as e:
        error_log(e, "013", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Customer_Enrollment_014():
    recorder.start(f"{img_service}-014")
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (EUR/NAR)")
        else:
            if app_login_setup():
                manual_check(
                    instruction="Remove the primary user in vehicle (In HMI->Settings->Users->Select the Primary User->Click on Gear Icon->'Remove Primary User')",
                    test_id="014",
                    service=img_service,
                    take_screenshot=False
                )
                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
                app_refresh("014", img_service)
                find_car("014", img_service)
                controller.small_swipe_up()
                if controller.is_text_present("SET YOUR PRIMARY USER") and controller.is_text_present("VIEW VEHICLE CODE"):
                    log("Set primary user section and vehicle code button displayed")
                else:
                    fail_log("Set primary user section not displayed", "014", img_service)
                controller.small_swipe_down()
    except Exception as e:
        error_log(e, "014", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

# Check which account should be for which part (all testcases with multiple users), use add_vin() if the second account probably isn't going to have the correct car
def Customer_Enrollment_015():
    recorder.start(f"{img_service}-015")
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (EUR/NAR)")
        else:
            if app_login_setup():
                find_car(add_car=True, num="015", img_service=img_service)
                if compare_with_expected_crop("Icons/lock_icon.png"):
                    log("User 1 is primary user and remote services enabled")
                else:
                    controller.small_swipe_up()
                    if controller.is_text_present("SET YOUR PRIMARY USER"):
                        if not controller.click_text("VIEW VEHICLE CODE"):
                            controller.click_text("GENERATE VEHICLE CODE")
                            controller.wait_for_text_and_click("Generate Vehicle Code")
                            controller.wait_for_text("VEHICLE CODE", 30)
                        vehicle_code = controller.d.xpath(
                            '//*[@text="Please enter following vehicle code in your Bentley infotainment system to set your primary user:"]/following-sibling::android.widget.TextView[1]').get_text()
                        manual_check(
                            instruction=f"On vehicle HMI navigate to Primary user page\nSuccessfully set the primary user using the vehicle code: {vehicle_code} and email: {current_email}",
                            test_id="015",
                            service=img_service,
                            take_screenshot=False
                        )
                    app_refresh("015", img_service)
                    if compare_with_expected_crop("Icons/lock_icon.png"):
                        log("User 1 is primary user and remote services enabled")
                    else:
                        fail_log("User 1 has been set as primary user but remote services are still not enabled", "015", img_service)
            if app_logout_setup():
                if app_login_setup(second_account=True):
                    if app_refresh("015", img_service):
                        find_car(add_car=True, num="015", img_service=img_service)
                        controller.small_swipe_up()
                        if controller.is_text_present("PRIMARY USER ALREADY SET") and compare_with_expected_crop("Icons/Remote_Lock_Grey.png", 0.9):
                            log("Primary user is already set for the other account and remote services are disabled")
                        else:
                            fail_log("Primary user is not displayed as already set for the other account", "015", img_service)
                        if controller.click_text("CONTACT SUPPORT"):
                            log("Contact support button displayed")
                            if compare_with_expected_crop("Icons/call_btn.png"):
                                log("User is prompted to call support")
                        else:
                            fail_log("Contact support button not displayed", "015", img_service)
                        controller.launch_app("uk.co.bentley.mybentley")
                        controller.small_swipe_down()
            app_logout_setup()
            app_login_setup()
    except Exception as e:
        error_log(e, "015", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Customer_Enrollment_016():
    recorder.start(f"{img_service}-016")
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (EUR/NAR)")
        else:
            if app_logout_setup():
                if app_login_setup():
                    find_car(add_car=True, num="016", img_service=img_service)
                    if app_refresh("016", img_service):
                        check_services_available("016")
                        manual_check(
                            instruction="Navigate to the Primary User Nomination page and select 'Revoke Primary User",
                            test_id="016",
                            service=img_service,
                            take_screenshot=False
                        )
                        if app_refresh("016", img_service):
                            check_services_unavailable("016")
                            controller.small_swipe_up()
                            if controller.wait_for_text_and_click("VIEW VEHICLE CODE"):
                                log("View vehicle code button displayed")
                                controller.wait_for_text("VEHICLE CODE", 30)
                                vehicle_code = controller.d.xpath(
                                    '//*[@text="Please enter following vehicle code in your Bentley infotainment system to set your primary user:"]/following-sibling::android.widget.TextView[1]').get_text()
                                manual_check(
                                    instruction=f"On vehicle HMI navigate to Primary user page\nSuccessfully set the primary user using the vehicle code: {vehicle_code} and email: {current_email}",
                                    test_id="016",
                                    service=img_service,
                                    take_screenshot=False
                                )
                                if app_refresh("016", img_service):
                                    check_services_available("016")
                            else:
                                fail_log("View vehicle code button not displayed", "016", img_service)

                            if app_logout_setup():
                                if app_login_setup(second_account=True):
                                    if app_refresh("016", img_service):
                                        find_car(add_car=True, num="016", img_service=img_service)
                                        check_services_unavailable("016")
                                        controller.small_swipe_up()
                                        if controller.is_text_present("PRIMARY USER ALREADY SET"):
                                            log("Primary user section displayed correctly")
                                        else:
                                            fail_log("Primary user section not displayed correctly", "016", img_service)
                                        controller.small_swipe_down()
            app_logout_setup()
            app_login_setup()
    except Exception as e:
        error_log(e, "016", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Customer_Enrollment_017():
    recorder.start(f"{img_service}-017")
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (EUR/NAR)")
        else:
            if app_login_setup():
                find_car(add_car=True, num="017", img_service=img_service)
                if app_refresh("017", img_service):
                    if view_setup("017"):
                        check_services_unavailable("017")
                        controller.small_swipe_up()
                        if controller.is_text_present("VIEW VEHICLE CODE"):
                            log("View vehicle code button displayed")
                        else:
                            fail_log("View vehicle code button not displayed", "017", img_service)
                        controller.small_swipe_down()
                        delete_vin()
                        add_vin("017", img_service)
                        if app_refresh("017", img_service):
                            check_services_unavailable("017")
                            controller.small_swipe_up()
                            if controller.is_text_present("GENERATE VEHICLE CODE"):
                                log("Generate vehicle code button displayed")
                            else:
                                fail_log("Generate vehicle code button not displayed", "017", img_service)
                            controller.small_swipe_down()
    except Exception as e:
        error_log(e, "017", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Customer_Enrollment_018():
    recorder.start(f"{img_service}-018")
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (EUR/NAR)")
        else:
            if app_logout_setup():
                if app_login_setup():
                    find_car(add_car=True, num="018", img_service=img_service)
                    if not compare_with_expected_crop("Icons/lock_icon.png"):
                        controller.small_swipe_up()
                        if controller.is_text_present("CONTACT SUPPORT"):
                            fail_log("Another user is already set as primary user", "018", img_service)
                        else:
                            if not controller.click_text("VIEW VEHICLE CODE"):
                                controller.click_text("GENERATE VEHICLE CODE")
                                controller.wait_for_text_and_click("Generate Vehicle Code")
                            controller.wait_for_text("VEHICLE CODE", 30)
                            vehicle_code = controller.d.xpath(
                                '//*[@text="Please enter following vehicle code in your Bentley infotainment system to set your primary user:"]/following-sibling::android.widget.TextView[1]').get_text()
                            manual_check(
                                instruction=f"On vehicle HMI navigate to Primary user page\nSuccessfully set the primary user using the vehicle code: {vehicle_code} and email: {current_email}",
                                test_id="018",
                                service=img_service,
                                take_screenshot=False
                            )
                            controller.click_by_image("Icons/login_page_x.png")
                            controller.small_swipe_down()
                            if app_refresh("018", img_service):
                                check_services_available("018")
                    else:
                        check_services_available("018")
                    app_logout_setup()
                if app_login_setup(second_account=True):
                    find_car(add_car=True, num="018", img_service=img_service)
                    if app_refresh("018", img_service):
                        check_services_unavailable("018")
                        controller.small_swipe_up()
                        if controller.is_text_present("PRIMARY USER ALREADY SET"):
                            log("Second account shows that another account is set as primary user")
                        else:
                            fail_log("Second account shows that another account is not set as primary user", "018", img_service)
                        if app_logout_setup():
                            if app_login_setup():
                                if app_refresh("018", img_service):
                                    delete_vin()
                                    if app_logout_setup():
                                        if app_login_setup(second_account=True):
                                            find_car(add_car=True, num="018", img_service=img_service)
                                            if app_refresh("018", img_service):
                                                check_services_unavailable("018")
                                                controller.small_swipe_up()
                                                if controller.is_text_present("GENERATE VEHICLE CODE"):
                                                    log("Generate Vehicle code button displayed")
                                                else:
                                                    fail_log("Generate Vehicle code button not displayed", "018", img_service)
                                                if controller.is_text_present("SET YOUR PRIMARY USER"):
                                                    log("Set primary user section and vehicle code button displayed")
                                                else:
                                                    fail_log("Set primary user section not displayed", "018",img_service)
            app_logout_setup()
            app_login_setup()
    except Exception as e:
        error_log(e, "018", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Customer_Enrollment_019():
    recorder.start(f"{img_service}-019")
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (EUR/NAR)")
        else:
            manual_check(
                instruction="User 2: Refresh the app and confirm remote services are available and user is set as primary user",
                test_id="019",
                service=img_service,
                take_screenshot=False
            )
            if app_login_setup():
                if app_refresh("019", img_service):
                    check_services_unavailable("019")
                    controller.small_swipe_up()
                    if controller.is_text_present("PRIMARY USER ALREADY SET"):
                        log("Second account shows that another account is set as primary user")
                    else:
                        fail_log("Second account shows that another account is not set as primary user", "019", img_service)
                    manual_check(
                        instruction="User 2: Uninstall the My Bentley app",
                        test_id="019",
                        service=img_service,
                        take_screenshot=False
                    )
                    if app_refresh("019", img_service):
                        check_services_unavailable("019")
                        controller.small_swipe_up()
                        if controller.is_text_present("PRIMARY USER ALREADY SET"):
                            log("Second account shows that another account is set as primary user")
                        else:
                            fail_log("Second account shows that another account is not set as primary user", "019", img_service)
                        controller.small_swipe_down()
    except Exception as e:
        error_log(e, "019", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Customer_Enrollment_020():
    recorder.start(f"{img_service}-020")
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (EUR/NAR)")
        else:
            # Maybe replace with automation if easily integratable with future ios automation
            manual_check(
                instruction="iOS device: Refresh the app and confirm the 'VIEW VEHICLE BUTTON' is displayed and remote services are disabled",
                test_id="020",
                service=img_service,
                take_screenshot=False
            )
            if app_login_setup():
                if app_refresh("020", img_service):
                    check_services_unavailable("020")
                    controller.small_swipe_up()
                    if controller.is_text_present("VIEW VEHICLE CODE"):
                        log("View Vehicle code button displayed")
                    else:
                        fail_log("View vehicle code button not displayed", "020", img_service)
                    controller.small_swipe_down()

    except Exception as e:
        error_log(e, "020", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Customer_Enrollment_021():
    recorder.start(f"{img_service}-021")
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (EUR/NAR)")
        else:
            android_vehicle_code = "Vehicle code failed to be extracted"
            if app_login_setup():
                find_car(add_car=True, num="021", img_service=img_service)
                if app_refresh("021", img_service):
                    check_services_unavailable("021")
                    controller.small_swipe_up()
                    if controller.click_text("VIEW VEHICLE CODE"):
                        log("View Vehicle code button displayed")
                        static_text = "Please enter following vehicle code in your Bentley infotainment system to set your primary user:"
                        android_vehicle_code = controller.d.xpath(f"//android.widget.TextView[@text=\"{static_text}\"]/following-sibling::*[1]").get_text()
                        controller.click_by_text("Icons/login_page_x.png")
                    else:
                        fail_log("View vehicle code button not displayed", "021", img_service)
                        android_vehicle_code = "Vehicle code failed to be extracted"
                    controller.small_swipe_down()
            # Maybe replace with automation if easily integratable with future ios automation
            manual_check(
                instruction=f"iOS device: Refresh the app and confirm remote services are disabled, the 'VIEW VEHICLE BUTTON' is displayed and the code matches the android code ({android_vehicle_code})",
                test_id="021",
                service=img_service,
                take_screenshot=False
            )
    except Exception as e:
        error_log(e, "021", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Customer_Enrollment_022():
    recorder.start(f"{img_service}-022")
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (EUR/NAR)")
        else:
            blocked_log("Test blocked - Requires retailer")
    except Exception as e:
        error_log(e, "022", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Customer_Enrollment_023():
    recorder.start(f"{img_service}-023")
    try:
        if country == "chn":
            blocked_log("Test blocked - Can't be automated")
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "039", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Customer_Enrollment_024():
    recorder.start(f"{img_service}-024")
    try:
        if country == "chn":
            blocked_log("Test blocked - Not written (CHN)")
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "024", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Customer_Enrollment_025():
    recorder.start(f"{img_service}-025")
    try:
        if country == "chn":
            blocked_log("Test blocked - Not written (CHN)")
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "025", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Customer_Enrollment_026():
    recorder.start(f"{img_service}-026")
    try:
        if country == "chn":
            blocked_log("Test blocked - Not written (CHN)")
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "026", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Customer_Enrollment_027():
    recorder.start(f"{img_service}-027")
    try:
        if country == "chn":
            blocked_log("Test blocked - Not written (CHN)")
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "027", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Customer_Enrollment_028():
    recorder.start(f"{img_service}-028")
    try:
        if country == "chn":
            blocked_log("Test blocked - Not written (CHN)")
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "028", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Customer_Enrollment_029():
    recorder.start(f"{img_service}-029")
    try:
        if country == "chn":
            blocked_log("Test blocked - Not written (CHN)")
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "029", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Customer_Enrollment_030():
    recorder.start(f"{img_service}-030")
    try:
        if country == "chn":
            blocked_log("Test blocked - Not written (CHN)")
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "030", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Customer_Enrollment_031():
    recorder.start(f"{img_service}-031")
    try:
        if country == "chn":
            blocked_log("Test blocked - Not written (CHN)")
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "031", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Customer_Enrollment_032():
    recorder.start(f"{img_service}-032")
    try:
        if country == "chn":
            blocked_log("Test blocked - Not written (CHN)")
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "032", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Customer_Enrollment_033():
    recorder.start(f"{img_service}-033")
    try:
        if country == "chn":
            blocked_log("Test blocked - Not written (CHN)")
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "033", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Customer_Enrollment_034():
    recorder.start(f"{img_service}-034")
    try:
        if country == "chn":
            blocked_log("Test blocked - Not written (CHN)")
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "034", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Customer_Enrollment_035():
    recorder.start(f"{img_service}-035")
    try:
        if country == "chn":
            blocked_log("Test blocked - Not written (CHN)")
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "035", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Customer_Enrollment_036():
    recorder.start(f"{img_service}-036")
    try:
        if country == "chn":
            blocked_log("Test blocked - Not written (CHN)")
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "036", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Customer_Enrollment_037():
    recorder.start(f"{img_service}-037")
    try:
        if country == "chn":
            blocked_log("Test blocked - Not written (CHN)")
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "037", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Customer_Enrollment_038():
    recorder.start(f"{img_service}-038")
    try:
        if country == "chn":
            blocked_log("Test blocked - Not written (CHN)")
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "038", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Customer_Enrollment_039():
    recorder.start(f"{img_service}-039")
    try:
        blocked_log("Test blocked - Can't check style guide")
    except Exception as e:
        error_log(e, "039", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False