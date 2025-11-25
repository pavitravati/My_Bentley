from common_utils.android_image_comparision import *
from core.log_emitter import log, fail_log, error_log, blocked_log
from core.app_functions import app_login, app_logout_setup, app_login_setup, enable_flight_mode, disable_flight_mode, \
    delete_vin, add_vin, app_refresh
from core.globals import *
from time import sleep
import random
from core.globals import manual_run
from gui.manual_check import manual_check
from common_utils.android_controller import *

img_service = "Customer Enrollment"

def check_services_unavailable(num, service):
    if compare_with_expected_crop("Icons/Remote_Lock_Unavailable.png"):
        log("Remote services not available as expected")
    elif compare_with_expected_crop("Icons/lock_icon.png"):
        fail_log("Remote services still available", num, service)
    else:
        fail_log("Remote services not checked as remote lock not displayed", num, service)

def check_services_available(num, service):
    if compare_with_expected_crop("Icons/lock_icon.png"):
        log("Remote services are available")
    else:
        fail_log("Remote services not available as expected", num, service)

def Customer_Enrollment_001():
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (EUR/NAR)")
        else:
            if controller.is_text_present("LOGIN OR REGISTER"):
                login_check = app_login()
                log("Login successful") if login_check[-1] else fail_log("Login failed", "001", img_service)
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            controller.small_swipe_up()
            if controller.is_text_present("SET YOUR PRIMARY USER"):
                log("User is not primary user as expected")
            else:
                fail_log("Vehicle already has a primary user set", "001", img_service)
            manual_check(
                instruction="In vehicle set primary user for this account\n(HMI->Settings->Users->'Set Primary User'->Enter User Name(Bentley Account ID) and FPIN(i.e. Present in Scratch Tag)->Click on 'Set Primary User')",
                test_id="001",
                service=img_service,
                take_screenshot=False
            )
            if app_refresh("001", img_service):
                controller.click_by_image("Icons/unlock_Icon.png")
                sleep(1)
                controller.enter_pin("1234")

                timeout_check = 0
                while not controller.is_text_present("Successfully unlocked") or compare_with_expected_crop("Icons/Error_Icon.png"):
                    sleep(1)
                    timeout_check += 1
                    if timeout_check > 40:
                        break

                if controller.is_text_present("Successfully unlocked"):
                    log("Unlock message displayed")
                    if controller.wait_for_text("Successfully unlocked"):
                        log("Remote services work as expected")
                    else:
                        fail_log("Remote services do not work as expected", "001", img_service)

    except Exception as e:
        error_log(e, "001", img_service)

def Customer_Enrollment_002():
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (EUR/NAR)")
        else:
            if app_login_setup():
                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
                controller.small_swipe_up()
                if controller.is_text_present("SET YOUR PRIMARY USER"):
                    log("User is not primary user as expected")
                else:
                    fail_log("User is primary user of the vehicle", "002", img_service)
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

def Customer_Enrollment_003():
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (EUR/NAR)")
        else:
            if app_login_setup():
                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
                delete_vin()
                add_vin()
                controller.small_swipe_up()
                log("Set primary user title displayed") if controller.is_text_present("SET YOUR PRIMARY USER") else fail_log("Set primary user title not displayed", "003", img_service)
                if controller.is_text_present("To set yourself as a primary user, a vehicle code will be generated in the next step. Please enter it in your Bentley infotainment system."):
                    log("Set primary user text displayed correctly")
                else:
                    fail_log("Set primary user text not displayed correctly", "003", img_service)
                log("Generate vehicle code button displayed") if controller.is_text_present("GENERATE VEHICLE CODE") else fail_log("Generate vehicle code button not displayed", "003", img_service)
                controller.click_by_image("Icons/info_btn.png")
                if controller.is_text_present("Generate a unique vehicle code* in My Bentley app. "):
                    log("Primary user instructions displayed")
                else:
                    fail_log("Primary user instructions not displayed", "003", img_service)
                controller.click_by_image("Icons/back_icon.png")
                controller.small_swipe_down()
    except Exception as e:
        error_log(e, "003", img_service)
add_vin()
# controller.dump_ui()
def Customer_Enrollment_004():
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (EUR/NAR)")
        else:
            if app_login_setup():
                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
                delete_vin()
                add_vin()
                controller.small_swipe_up()
                controller.click_text("GENERATE VEHICLE CODE")
                if controller.wait_for_text("The vehicle code on the scratch tag will be invalidated"):
                    log("Generate vehicle code confirmation text displayed")
                else:
                    fail_log("Generate vehicle code not displayed", "004", img_service)

                if controller.is_text_present("Cancel") and controller.click_text("Generate vehicle code"):
                    log("Generate vehicle code and cancel buttons displayed")
                else:
                    fail_log("Generate vehicle code or cancel button not displayed", "004", img_service)

                latency_time = time.time()
                if controller.wait_for_text("VEHICLE CODE"):
                    latency_time = time.time() - latency_time
                    if latency_time < 10:
                        log(f"New vehicle code generated and displayed in under 10 seconds ({latency_time} seconds)")
                    else:
                        fail_log(f"New vehicle code generated and displayed but in more than 10 seconds ({latency_time} seconds)", "005", img_service)
                else:
                    fail_log("Vehicle code not displayed", "010", img_service)

                controller.click_by_image("Icons/login_page_x.png")
                controller.small_swipe_down()
    except Exception as e:
        error_log(e, "004", img_service)

def Customer_Enrollment_005():
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (EUR/NAR)")
        else:
            if app_login_setup():
                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
                if app_refresh("005", img_service):
                    controller.small_swipe_up()
                    if controller.click_text("VIEW VEHICLE CODE"):
                        log("View vehicle code button displayed")
                    else:
                        fail_log("View vehicle code button not displayed", "005", img_service)

                    latency_time = time.time()
                    if controller.wait_for_text("VEHICLE CODE"):
                        latency_time = time.time() - latency_time
                        if latency_time < 5:
                            log(f"Vehicle code displayed in under 5 seconds ({latency_time} seconds)")
                        else:
                            fail_log(f"Vehicle code displayed but in more than 5 seconds ({latency_time} seconds)", "005", img_service)
                    else:
                        fail_log("Vehicle code not displayed", "010", img_service)

                    controller.click_by_image("Icons/login_page_x.png")
                    controller.small_swipe_down()

    except Exception as e:
        error_log(e, "005", img_service)

# Guessed
def Customer_Enrollment_006():
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (EUR/NAR)")
        else:
            if app_login_setup():
                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
                delete_vin()
                add_vin()
                enable_flight_mode()
                controller.small_swipe_up()
                if controller.click_text("GENERATE VEHICLE CODE"):
                    controller.click_text("Generate vehicle code")
                    if controller.wait_for_text("Error while generating a vehicle code"):
                        log("Expected error message displayed")
                    else:
                        fail_log("Expected error message not displayed", "006", img_service)
                else:
                    fail_log("GENERATE VEHICLE CODE button not displayed", "006", img_service)
                controller.click_by_image("Icons/Error_Icon.png")
                controller.small_swipe_down()
                disable_flight_mode()
    except Exception as e:
        error_log(e, "006", img_service)

def Customer_Enrollment_007():
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (EUR/NAR)")
        else:
            if app_login_setup():
                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
                if app_refresh("007", img_service):
                    controller.small_swipe_up()
                    if controller.click_text("VIEW VEHICLE CODE"):
                        manual_check(
                            instruction="On vehicle HMI navigate to Primary user page\nSuccessfully set the primary user",
                            test_id="007",
                            service=img_service,
                            take_screenshot=False
                        )
                        if app_refresh("007", img_service):
                            controller.small_swipe_up()
                            if not controller.is_text_present("SET YOUR PRIMARY USER") and compare_with_expected_crop("Icons/lock_icon.png"):
                                log("Primary user set and remote services enabled in the app")
                            else:
                                fail_log("Primary user failed to be set successfully", "007", img_service)
                            controller.small_swipe_up()
                    else:
                        fail_log("View vehicle code button not displayed", "007", img_service)
    except Exception as e:
        error_log(e, "007", img_service)

def Customer_Enrollment_008():
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (EUR/NAR)")
        else:
            if app_login_setup():
                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
                if app_refresh("008", img_service):
                    controller.small_swipe_up()
                    if controller.is_text_present("SET YOUR PRIMARY USER"):
                        manual_check(
                            instruction="Navigate to the Primary User Nomination page in HMI, enter the email address and the incorrect vehicle code\nPrimary user nomination should be blocked with 10 tries remaining",
                            test_id="008",
                            service=img_service,
                            take_screenshot=False
                        )
                        if app_refresh("015", img_service):
                            controller.small_swipe_up()
                            if controller.is_text_present("SET YOUR PRIMARY USER"):
                                log("Primary user not set as expected")
                            else:
                                fail_log("Primary user is set", "008", img_service)
                            controller.small_swipe_down()
                    else:
                        fail_log("Primary user is already set", "008", img_service)
    except Exception as e:
        error_log(e, "008", img_service)

def Customer_Enrollment_009():
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (EUR/NAR)")
        else:
            if app_login_setup():
                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
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
    except Exception as e:
        error_log(e, "009", img_service)

def Customer_Enrollment_010():
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (EUR/NAR)")
        else:
            if app_login_setup():
                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
                delete_vin()
                add_vin()
                controller.small_swipe_up()
                if controller.click_text("GENERATE VEHICLE CODE"):
                    controller.click_text("Generate vehicle code")
                    controller.d.press("recent")
                    sleep(0.5)
                    controller.click_text("Close all")
                    controller.launch_app("uk.co.bentley.mybentley")
                    if app_refresh("010", img_service):
                        controller.small_swipe_up()
                        if controller.is_text_present("SET YOUR PRIMARY USER"):
                            log("User not primary user as expected")
                            if controller.is_text_present("VIEW VEHICLE CODE"):
                                log("View vehicle code button displayed")
                            elif controller.is_text_present("GENERATE VEHICLE CODE"):
                                log("Generate vehicle code button displayed")
                            else:
                                fail_log(f"Expected vehicle code button not displayed", "010", img_service)
                        else:
                            fail_log("Primary user details not displayed as expected", "010", img_service)
                else:
                    fail_log("Generate vehicle code button not displayed", "010", img_service)
                controller.click_by_image("Icons/login_page_x.png")
                controller.small_swipe_down()
    except Exception as e:
        error_log(e, "010", img_service)

def Customer_Enrollment_011():
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (EUR/NAR)")
        else:
            if app_login_setup():
                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
                delete_vin()
                add_vin()
                controller.small_swipe_up()
                if controller.click_text("GENERATE VEHICLE CODE"):
                    controller.click_text("Generate vehicle code")
                    controller.press_home()
                    controller.d.press("power")
                    sleep(1)
                    controller.d.press("power")
                    controller.swipe_up()
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

def Customer_Enrollment_012():
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (EUR/NAR)")
        else:
            if app_login_setup():
                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
                delete_vin()
                add_vin()
                controller.small_swipe_up()
                manual_check(
                    instruction="Click on 'GENERATE VEHICLE CODE'\nIncoming call/SMS/Alarm received during generation",
                    test_id="012",
                    service=img_service,
                    take_screenshot=False
                )
                controller.d.press("recent")
                sleep(0.5)
                controller.click_text("Close all")
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

def Customer_Enrollment_013():
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
                    controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
                    controller.small_swipe_up()
                    if controller.is_text_present("SET YOUR PRIMARY USER") and controller.click_text("VIEW VEHICLE CODE"):
                        log("Primary user section displayed correctly")
                        if not controller.wait_for_text("VEHICLE CODE"):
                            fail_log("View vehicle code button did not work as expected", "013", img_service)
                        controller.click_by_image("Icons/login_page_x.png")
                    else:
                        fail_log("Primary user section not displayed", "013", img_service)
                    controller.small_swipe_down()

    except Exception as e:
        error_log(e, "013", img_service)

def Customer_Enrollment_014():
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
                controller.small_swipe_up()
                if controller.is_text_present("SET YOUR PRIMARY USER") and controller.is_text_present("VIEW VEHICLE CODE"):
                    log("Set primary user section and vehicle code button displayed")
                else:
                    fail_log("Set primary user section not displayed", "014", img_service)
                controller.small_swipe_down()
    except Exception as e:
        error_log(e, "014", img_service)

# Check which account should be for which part (all testcases with multiple users), use add_vin() if the second account probably isn't going to have the correct car
def Customer_Enrollment_015():
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (EUR/NAR)")
        else:
            if app_logout_setup():
                if app_login_setup(second_account=True):
                    if app_refresh("015", img_service):
                        if compare_with_expected_crop("Icons/lock_icon.png"):
                            log("Remote services available")
                        else:
                            fail_log("Remote services not available", "015", img_service)
                    if app_logout_setup():
                        if app_login_setup():
                            if app_refresh("015", img_service):
                                check_services_unavailable("015", img_service)
                                controller.small_swipe_up()
                                # Guessed this, check the correct text
                                if controller.is_text_present("Primary User Already Set") and controller.is_text_present("B4C call button"):
                                    log("Primary user section displayed correctly and user is prompted to call B4C")
                                else:
                                    fail_log("Primary user section not displayed correctly", "015", img_service)
                                controller.small_swipe_down()
    except Exception as e:
        error_log(e, "015", img_service)

def Customer_Enrollment_016():
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (EUR/NAR)")
        else:
            if app_logout_setup():
                if app_login_setup(second_account=True):
                    if app_refresh("016", img_service):
                        check_services_available("016", img_service)
                        manual_check(
                            instruction="Navigate to the Primary User Nomination page and select 'Revoke Primary User",
                            test_id="016",
                            service=img_service,
                            take_screenshot=False
                        )
                        if app_refresh("016", img_service):
                            check_services_unavailable("016", img_service)
                            controller.small_swipe_up()
                            if controller.is_text_present("VIEW VEHICLE CODE"):
                                log("View vehicle code button displayed")
                            else:
                                fail_log("View vehicle code button not displayed", "016", img_service)
                            if app_logout_setup():
                                if app_login_setup():
                                    if app_refresh("016", img_service):
                                        check_services_unavailable("016", img_service)
                                        controller.small_swipe_up()
                                        # Guessed
                                        if controller.is_text_present("Primary User Already Set"):
                                            log("Primary user section displayed correctly")
                                        else:
                                            fail_log("Primary user section not displayed correctly", "016", img_service)
                                        controller.small_swipe_down()
    except Exception as e:
        error_log(e, "016", img_service)

def Customer_Enrollment_017():
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (EUR/NAR)")
        else:
            if app_login_setup():
                if app_refresh("017", img_service):
                    check_services_unavailable("017", img_service)
                    controller.small_swipe_up()
                    if controller.is_text_present("VIEW VEHICLE CODE"):
                        log("View vehicle code button displayed")
                    else:
                        fail_log("View vehicle code button not displayed", "017", img_service)
                    controller.small_swipe_down()
                    delete_vin()
                    add_vin()
                    if app_refresh("017", img_service):
                        check_services_unavailable("017", img_service)
                        controller.small_swipe_up()
                        if controller.is_text_present("GENERATE VEHICLE CODE"):
                            log("Generate vehicle code button displayed")
                        else:
                            fail_log("Generate vehicle code button not displayed", "017", img_service)
                        controller.small_swipe_down()
    except Exception as e:
        error_log(e, "017", img_service)

def Customer_Enrollment_018():
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (EUR/NAR)")
        else:
            if app_logout_setup():
                if app_login_setup(second_account=True):
                    if app_refresh("018", img_service):
                        check_services_available("017", img_service)
                        if app_logout_setup():
                            if app_login_setup():
                                if app_refresh("018", img_service):
                                    check_services_unavailable("018", img_service)
                                    controller.small_swipe_up()
                                    # Guessed
                                    if controller.is_text_present("Primary User Already Set"):
                                        log("Primary user section displayed correctly")
                                    else:
                                        fail_log("Primary user section not displayed correctly", "018", img_service)
                                    if app_logout_setup():
                                        if app_login_setup(second_account=True):
                                            delete_vin()
                                            if app_logout_setup():
                                                if app_login_setup():
                                                    if app_refresh("018", img_service):
                                                        check_services_unavailable("018", img_service)
                                                        controller.small_swipe_up()
                                                        if controller.is_text_present("GENERATE VEHICLE CODE"):
                                                            log("Generate vehicle code button displayed")
                                                        else:
                                                            fail_log("Generate vehicle code button not displayed", "018", img_service)
                                                        controller.small_swipe_down()
    except Exception as e:
        error_log(e, "018", img_service)

def Customer_Enrollment_019():
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (EUR/NAR)")
        else:
            manual_check(
                instruction="User 2: Refresh the app and confirm remote services are available",
                test_id="019",
                service=img_service,
                take_screenshot=False
            )
            if app_login_setup():
                if app_refresh("019", img_service):
                    check_services_unavailable("019", img_service)
                    controller.small_swipe_up()
                    # Guessed
                    if controller.is_text_present("Primary User Already Set"):
                        log("Primary user section displayed correctly")
                    else:
                        fail_log("Primary user section not displayed correctly", "019", img_service)
                    controller.small_swipe_down()
                    manual_check(
                        instruction="User 2: Uninstall the My Bentley app",
                        test_id="019",
                        service=img_service,
                        take_screenshot=False
                    )
                    if app_refresh("019", img_service):
                        check_services_unavailable("019", img_service)
                        controller.small_swipe_up()
                        # Guessed
                        if controller.is_text_present("Primary User Already Set"):
                            log("Primary user section displayed correctly")
                        else:
                            fail_log("Primary user section not displayed correctly", "019", img_service)
                        controller.small_swipe_down()
    except Exception as e:
        error_log(e, "019", img_service)

def Customer_Enrollment_020():
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (EUR/NAR)")
        else:
            if app_refresh("020", img_service):
                check_services_unavailable("020", img_service)
                controller.small_swipe_up()
                if controller.click_text("VIEW VEHICLE BUTTON"):
                    log("View Vehicle Button displayed")
                    if controller.wait_for_text("VEHICLE CODE"):
                        log("Vehicle code page displayed")
                        controller.click_by_image("info_btn.png")
                        if controller.wait_for_text("SET YOUR PRIMARY USER") and controller.wait_for_text_that_contains("Generate a unique vehicle code"):
                            log("Primary user instruction page displayed correctly")
                        else:
                            fail_log("Primary user instruction page not displayed", "020", img_service)
                        controller.click_by_image("back_icon.png")
                    else:
                        fail_log("Vehicle code page not displayed", "020", img_service)
                    controller.click_by_image("login_page_x.png")
                else:
                    fail_log("View Vehicle Button not displayed", "020", img_service)
                controller.small_swipe_down()
    except Exception as e:
        error_log(e, "020", img_service)

def Customer_Enrollment_021():
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (EUR/NAR)")
        else:
            # Maybe replace with automation if easily integratable with future ios automation
            manual_check(
                instruction="iOS device: Refresh the app and confirm the 'VIEW VEHICLE BUTTON' is displayed and remote services are disabled",
                test_id="021",
                service=img_service,
                take_screenshot=False
            )
            if app_login_setup():
                if app_refresh("021", img_service):
                    check_services_unavailable("021", img_service)
                    controller.small_swipe_up()
                    if controller.is_text_present("VIEW VEHICLE CODE"):
                        log("View Vehicle code button displayed")
                    else:
                        fail_log("View vehicle code button not displayed", "021", img_service)
                    controller.small_swipe_down()

    except Exception as e:
        error_log(e, "021", img_service)

def Customer_Enrollment_022():
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (EUR/NAR)")
        else:
            android_vehicle_code = "Vehicle code failed to be extracted"
            if app_login_setup():
                if app_refresh("022", img_service):
                    check_services_unavailable("022", img_service)
                    controller.small_swipe_up()
                    if controller.click_text("VIEW VEHICLE CODE"):
                        log("View Vehicle code button displayed")
                        static_text = "Please enter following vehicle code in your Bentley infotainment system to set your primary user:"
                        android_vehicle_code = controller.d.xpath(f"//android.widget.TextView[@text=\"{static_text}\"]/following-sibling::*[1]").get_text()
                        controller.click_by_text("Icons/login_page_x.png")
                    else:
                        fail_log("View vehicle code button not displayed", "022", img_service)
                        android_vehicle_code = "Vehicle code failed to be extracted"
                    controller.small_swipe_down()
            # Maybe replace with automation if easily integratable with future ios automation
            manual_check(
                instruction=f"iOS device: Refresh the app and confirm remote services are disabled, the 'VIEW VEHICLE BUTTON' is displayed and the code matches the android code ({android_vehicle_code})",
                test_id="022",
                service=img_service,
                take_screenshot=False
            )
    except Exception as e:
        error_log(e, "022", img_service)

def Customer_Enrollment_023():
    try:
        if country == "chn":
            blocked_log("Test blocked - Region locked (EUR/NAR)")
        else:
            if app_logout_setup():
                random_email = f"automation{str(random.random())[2:6]}@gqm.anonaddy.com"
                controller.enter_text(f"%s%s%s%s%s{random_email}")
                sleep(2)
                password = "Password1!"
                controller.enter_text(password)
                controller.click_text("CREATE")
                controller.wait_for_text("ACCEPT")
                if controller.click_by_image("Icons/accept_icon.png"):
                    if controller.wait_for_text("CHECK YOUR INBOX"):
                        controller.swipe_up()
                        controller.click_text("RETURN TO LOGIN")
                        controller.click_text("NEXT")
                        manual_check(
                            instruction=f"Wait for new confirmation email and confirm it.",
                            test_id="023",
                            service=img_service,
                            take_screenshot=False
                        )
                        controller.enter_text(password)
                        controller.wait_for_text("Allow access")
                        controller.swipe_up()
                        controller.click_text("ALLOW")
                        controller.wait_for_text_and_click("ACCEPT")
                        if controller.wait_for_text("DASHBOARD"):
                            log("New account successfully logged in")
                            controller.swipe_up()
                            controller.click_text("ADD A VEHICLE")
                            controller.swipe_up()
                            controller.enter_text(current_vin)
                            controller.wait_for_text("YOUR PREFERRED BENTLEY RETAILER")
                            controller.click("Icons/Homescreen_Right_Arrow.png")
                            controller.wait_for_text_and_click("Search by retailer name or location")
                            controller.enter_text("Manchester")
                            controller.click_text("Bentley Manchester")
                            controller.click_text("CONFIRM")
                            controller.wait_for_text("ADD YOUR BENTLEY")
                            controller.click_text("CONTINUE")
                            controller.click_text("First Name")
                            controller.enter_text("first")
                            controller.click_text("Next")
                            controller.enter_text("last")
                            controller.click_text("YOUR DETAILS")
                            controller.click_text("CONTINUE")
                            controller.click_text("Location")
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
                            controller.wait_for_text_and_click("Area Code")
                            controller.swipe_up(0.035)
                            controller.click_text("+44")
                            controller.click_text("Mobile Phone")
                            controller.enter_text("07818014437")
                            controller.click_text("Continue")
                            controller.wait_for_text("Request Submitted")
                            controller.click_text("CONTINUE")
                            log("Vehicle added to new account") if controller.click_by_image(
                                "Icons/Homescreen_Left_Arrow.png") else fail_log("Vehicle not added to new account",
                                                                                 "002", img_service)
                            controller.swipe_up()
                            controller.click_text("SET MY PIN")
                            controller.click_text("New PIN")
                            controller.enter_pin("1234")
                            controller.enter_pin("1234")
                            log("New pin set") if controller.click_text("SET PIN") else fail_log("Failed to set a new pin", "023", img_service)
                            controller.small_swipe_up()
                            if controller.click_text("GENERATE VEHICLE CODE"):
                                log("Generate vehicle code button displayed")
                                controller.click_text("Generate vehicle code")
                                controller.wait_for_text("VEHICLE CODE")
                                static_text = "Please enter following vehicle code in your Bentley infotainment system to set your primary user:"
                                android_vehicle_code = controller.d.xpath(f"//android.widget.TextView[@text=\"{static_text}\"]/following-sibling::*[1]").get_text()
                                manual_check(
                                    instruction=f"In Vehicle HMI->Settings->Users->'Set Primary User'->Enter User Name({current_email}) and vehicle code({android_vehicle_code})-> Click on 'Set Primary User'",
                                    test_id="023",
                                    service=img_service,
                                    take_screenshot=False
                                )
                                if app_refresh("023", img_service):
                                    check_services_available("023", img_service)
                            else:
                                fail_log("Generate vehicle code button displayed", "002", img_service)
    except Exception as e:
        error_log(e, "023", img_service)

def Customer_Enrollment_024():
    try:
        if country == "chn":
            blocked_log("Test blocked - Not written (CHN)")
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "024", img_service)

def Customer_Enrollment_025():
    try:
        if country == "chn":
            blocked_log("Test blocked - Not written (CHN)")
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "025", img_service)

def Customer_Enrollment_026():
    try:
        if country == "chn":
            blocked_log("Test blocked - Not written (CHN)")
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "026", img_service)

def Customer_Enrollment_027():
    try:
        if country == "chn":
            blocked_log("Test blocked - Not written (CHN)")
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "027", img_service)

def Customer_Enrollment_028():
    try:
        if country == "chn":
            blocked_log("Test blocked - Not written (CHN)")
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "028", img_service)

def Customer_Enrollment_029():
    try:
        if country == "chn":
            blocked_log("Test blocked - Not written (CHN)")
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "029", img_service)

def Customer_Enrollment_030():
    try:
        if country == "chn":
            blocked_log("Test blocked - Not written (CHN)")
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "030", img_service)

def Customer_Enrollment_031():
    try:
        if country == "chn":
            blocked_log("Test blocked - Not written (CHN)")
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "031", img_service)

def Customer_Enrollment_032():
    try:
        if country == "chn":
            blocked_log("Test blocked - Not written (CHN)")
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "032", img_service)

def Customer_Enrollment_033():
    try:
        if country == "chn":
            blocked_log("Test blocked - Not written (CHN)")
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "033", img_service)

def Customer_Enrollment_034():
    try:
        if country == "chn":
            blocked_log("Test blocked - Not written (CHN)")
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "034", img_service)

def Customer_Enrollment_035():
    try:
        if country == "chn":
            blocked_log("Test blocked - Not written (CHN)")
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "035", img_service)

def Customer_Enrollment_036():
    try:
        if country == "chn":
            blocked_log("Test blocked - Not written (CHN)")
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "036", img_service)

def Customer_Enrollment_037():
    try:
        if country == "chn":
            blocked_log("Test blocked - Not written (CHN)")
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "037", img_service)

def Customer_Enrollment_038():
    try:
        if country == "chn":
            blocked_log("Test blocked - Not written (CHN)")
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "038", img_service)

def Customer_Enrollment_039():
    try:
        if country == "chn":
            blocked_log("Test blocked - Can't be automated")
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "039", img_service)

def Customer_Enrollment_040():
    try:
        blocked_log("Test blocked - Can't check style guide")
    except Exception as e:
        error_log(e, "040", img_service)