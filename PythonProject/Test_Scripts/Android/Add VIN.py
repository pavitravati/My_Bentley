from common_utils.android_image_comparision import *
from core.log_emitter import log, fail_log, error_log, blocked_log
from time import sleep
import random
from core.globals import current_VIN

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
                        controller.wait_for_text_and_click("Search by retailer name or location")
                        controller.enter_text("Manchester")
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

        # Automate the process of adding the VIN and checking

    except Exception as e:
        error_log(e, "002", img_service)

def Add_VIN_003():
    try:
        # Automate process of deleting VIN from app so it can be re-added

        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        while not controller.is_text_present("ADD A VEHICLE"):
            controller.click_by_image("Icons/Homescreen_Right_Arrow.png")
            sleep(0.05)
        controller.small_swipe_up()
        sleep(0.2)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/button_add_dashboard_module_add_vehicle")
        controller.small_swipe_up()
        controller.click_text("Enter VIN manually")
        controller.enter_text(current_VIN)
        if controller.click_by_image("Images/VIN_confirm_btn.png"):
            log("VIN entered manually")
        else:
            fail_log("Failed to manually enter VIN", "003", img_service)
        controller.click_by_image("Icons/Homescreen_Right_Arrow.png")
        controller.wait_for_text_and_click("Search by retailer name or location")
        controller.enter_text("Manchester")
        controller.click_text("Bentley Manchester")
        if controller.wait_for_text_and_click("CONFIRM"):
            log("Retailer selected")
        else:
            fail_log("Retailer not selected", "003", img_service)

        # Automate the process of adding a vehicle and checking

    except Exception as e:
        error_log(e, "003", img_service)

def Add_VIN_004():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        while not controller.is_text_present("ADD A VEHICLE"):
            controller.click_by_image("Icons/Homescreen_Right_Arrow.png")
            sleep(0.05)
        controller.small_swipe_up()
        sleep(0.2)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/button_add_dashboard_module_add_vehicle")
        controller.small_swipe_up()
        controller.click_text("Enter VIN manually")
        controller.enter_text(current_VIN)
        if controller.click_by_image("Images/VIN_confirm_btn.png"):
            log("Already existing VIN entered")
        else:
            fail_log("Failed to manually enter existing VIN", "004", img_service)

        controller.click_by_image("Icons/Homescreen_Right_Arrow.png")
        controller.wait_for_text_and_click("Search by retailer name or location")
        controller.enter_text("Manchester")
        controller.click_text("Bentley Manchester")
        if controller.wait_for_text_and_click("CONFIRM"):
            log("Retailer selected")
        else:
            fail_log("Retailer not selected", "004", img_service)
        if controller.wait_for_text("VIN already registered to your account", 60):
            log("Existing VIN error message displayed")
        else:
            fail_log("Expected error message not displayed", "004", img_service)

        controller.click_by_image("Icons/login_page_x.png")
        controller.click_by_image("Icons/back_icon.png")
        controller.small_swipe_down()
        while compare_with_expected_crop("Icons/Homescreen_Left_Arrow.png"):
            controller.click_by_image("Icons/Homescreen_Left_Arrow.png")

    except Exception as e:
        error_log(e, "004", img_service)
Add_VIN_004()

def Add_VIN_005():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        while not controller.is_text_present("ADD A VEHICLE"):
            controller.click_by_image("Icons/Homescreen_Right_Arrow.png")
            sleep(0.05)
        controller.small_swipe_up()
        sleep(0.2)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/button_add_dashboard_module_add_vehicle")
        controller.small_swipe_up()
        controller.click_text("Enter VIN manually")
        controller.enter_text("Test")
        if not controller.is_text_present("Enter VIN manually"):
            controller.click_text("CONFIRM")
            if controller.wait_for_text("Vehicle could not be added"):
                log("VIN not added due to Invalid VIN")
            else:
                fail_log("VIN not added error message not displayed", "005", img_service)
            controller.click_by_image("Icons/Error_Icon.png")

        controller.click_by_image("Icons/back_icon.png")
        controller.small_swipe_down()
        while compare_with_expected_crop("Icons/Homescreen_Left_Arrow.png"):
            controller.click_by_image("Icons/Homescreen_Left_Arrow.png")

    except Exception as e:
        error_log(e, "005", img_service)

def Add_VIN_006():
    try:
        controller.launch_app("com.android.settings")
        if controller.click_by_image("Icons/settings_search.png"):
            controller.enter_text("Bentley")
        controller.click_text("My Bentley")
        sleep(0.2)
        controller.click_text("Permissions")
        controller.click_text("Camera")
        controller.click_text("Allow only while using the app")
        controller.launch_app("uk.co.bentley.mybentley")

        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        while not controller.is_text_present("ADD A VEHICLE"):
            controller.click_by_image("Icons/Homescreen_Right_Arrow.png")
            sleep(0.05)
        controller.small_swipe_up()
        sleep(0.2)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/button_add_dashboard_module_add_vehicle")
        if controller.click_text("Open Camera") and controller.is_text_present("Centre your VIN in the box above"):
            log("Add a vehicle screen opened when 'Open Camera' is pressed")
        else:
            fail_log("Failed to open camera screen", "006", img_service)
        controller.click_by_image("Icons/back_icon.png")

        controller.small_swipe_up()
        if controller.click_text("Enter VIN manually"):
            controller.enter_text("test")
            if controller.is_text_present("TEST"):
                log("Manual VIN entry section displayed and working")
            else:
                fail_log("Manual VIN entry section displayed but not working as expected", "006", img_service)
        else:
            fail_log("Manual VIN entry section not displayed", "006", img_service)

        if controller.is_text_present("CONFIRM"):
            log("Confirm button displayed")
        else:
            fail_log("Confirm button not displayed", "006", img_service)

        controller.click_text("Locating your VIN")
        if controller.is_text_present("Locating your VIN") and controller.click_text("OK"):
            log("Locating your VIN popup displayed when 'Locating your VIN' is pressed")
        else:
            fail_log("'Locating your VIN not displayed or working", "006", img_service)

        controller.click_by_image("Icons/back_icon.png")
        controller.small_swipe_down()
        while compare_with_expected_crop("Icons/Homescreen_Left_Arrow.png"):
            controller.click_by_image("Icons/Homescreen_Left_Arrow.png")

    except Exception as e:
        error_log(e, "006", img_service)

def Add_VIN_007():
    try:
        # if manual:
        controller.launch_app("com.android.settings")
        if controller.click_by_image("Icons/settings_search.png"):
            controller.enter_text("Bentley")
        controller.click_text("My Bentley")
        sleep(0.2)
        controller.click_text("Permissions")
        controller.click_text("Camera")
        controller.click_text("Allow only while using the app")
        controller.launch_app("uk.co.bentley.mybentley")

        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        while not controller.is_text_present("ADD A VEHICLE"):
            controller.click_by_image("Icons/Homescreen_Right_Arrow.png")
            sleep(0.05)
        controller.small_swipe_up()
        sleep(0.2)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/button_add_dashboard_module_add_vehicle")
        if controller.click_text("Open Camera") and controller.is_text_present("Centre your VIN in the box above"):
            log("Add a vehicle screen opened when 'Open Camera' is pressed")
        else:
            fail_log("Failed to open camera screen", "007", img_service)

        if compare_with_expected_crop("Icons/flash_clicked.png") or compare_with_expected_crop("Icons/flash_blackbg.png") or compare_with_expected_crop("Icons/flash_whitebg.png"):
            log("Flash button displayed")
        else:
            fail_log("Flash button not displayed", "007", img_service)

        if controller.is_text_present("Centre your VIN in the box above"):
            log("'Centre your VIN' message displayed")
        else:
            fail_log("'Centre your VIN' message not displayed", "007", img_service)

        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/back_icon.png")
        controller.small_swipe_down()
        while compare_with_expected_crop("Icons/Homescreen_Left_Arrow.png"):
            controller.click_by_image("Icons/Homescreen_Left_Arrow.png")

    except Exception as e:
        error_log(e, "007", img_service)

def Add_VIN_008():
    try:
        # if manual:
        controller.launch_app("com.android.settings")
        if controller.click_by_image("Icons/settings_search.png"):
            controller.enter_text("Bentley")
        controller.click_text("My Bentley")
        sleep(0.2)
        controller.click_text("Permissions")
        controller.click_text("Camera")
        controller.click_text("Allow only while using the app")
        controller.launch_app("uk.co.bentley.mybentley")

        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        while not controller.is_text_present("ADD A VEHICLE"):
            controller.click_by_image("Icons/Homescreen_Right_Arrow.png")
            sleep(0.05)
        controller.small_swipe_up()
        sleep(0.2)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/button_add_dashboard_module_add_vehicle")
        if controller.click_text("Open Camera") and controller.is_text_present("Centre your VIN in the box above"):
            log("Add a vehicle screen opened when 'Open Camera' is pressed")
        else:
            fail_log("Failed to open camera screen", "008", img_service)

        if controller.click_by_image("Icons/flash_clicked.png"):
            log("Flash disabled")
        else:
            if compare_with_expected_crop("Icons/flash_blackbg.png") or compare_with_expected_crop("Icons/flash_lightbg.png"):
                log("Flash disabled")
            else:
                fail_log("Failed to disable flash", "008", img_service)

        if controller.is_text_present("Centre your VIN in the box above"):
            log("'Centre your VIN' message displayed")
        else:
            fail_log("'Centre your VIN' message not displayed", "008", img_service)

        ###########
        # wait for VIN to be scanned
        ###########

        if controller.is_text_present("CONFIRM YOUR VIN") and not controller.is_text_present("Enter VIN manually"):
            log("VIN scanned and displayed in VIN field")
        else:
            fail_log("VIN not scanned successfully or not displayed in VIN field", "009", img_service)

        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/back_icon.png")
        controller.small_swipe_down()
        while compare_with_expected_crop("Icons/Homescreen_Left_Arrow.png"):
            controller.click_by_image("Icons/Homescreen_Left_Arrow.png")

    except Exception as e:
        error_log(e, "008", img_service)

def Add_VIN_009():
    try:
        # if manual:
        controller.launch_app("com.android.settings")
        if controller.click_by_image("Icons/settings_search.png"):
            controller.enter_text("Bentley")
        controller.click_text("My Bentley")
        sleep(0.2)
        controller.click_text("Permissions")
        controller.click_text("Camera")
        controller.click_text("Allow only while using the app")
        controller.launch_app("uk.co.bentley.mybentley")

        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        while not controller.is_text_present("ADD A VEHICLE"):
            controller.click_by_image("Icons/Homescreen_Right_Arrow.png")
            sleep(0.05)
        controller.small_swipe_up()
        sleep(0.2)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/button_add_dashboard_module_add_vehicle")
        if controller.click_text("Open Camera") and controller.is_text_present("Centre your VIN in the box above"):
            log("Add a vehicle screen opened when 'Open Camera' is pressed")
        else:
            fail_log("Failed to open camera screen", "009", img_service)

        controller.click(950, 2050)
        controller.click_by_image("Icons/flash_blackbg.png")
        controller.click_by_image("Icons/flash_lightbg.png")
        if compare_with_expected_crop("Icons/flash_clicked.png"):
            log("Flash button enabled successfully")
        else:
            fail_log("Flash button could not be enabeld", "009", img_service)

        if controller.is_text_present("Centre your VIN in the box above"):
            log("'Centre your VIN' message displayed")
        else:
            fail_log("'Centre your VIN' message not displayed", "009", img_service)

        ###########
        # wait for VIN to be scanned
        ###########

        if controller.is_text_present("CONFIRM YOUR VIN") and not controller.is_text_present("Enter VIN manually"):
            log("VIN scanned and displayed in VIN field")
        else:
            fail_log("VIN not scanned successfully or not displayed in VIN field", "009", img_service)

        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/back_icon.png")
        controller.small_swipe_down()
        while compare_with_expected_crop("Icons/Homescreen_Left_Arrow.png"):
            controller.click_by_image("Icons/Homescreen_Left_Arrow.png")

    except Exception as e:
        error_log(e, "009", img_service)

def Add_VIN_010():
    try:
        controller.launch_app("com.android.settings")
        if controller.click_by_image("Icons/settings_search.png"):
            controller.enter_text("Bentley")
        controller.click_text("My Bentley")
        sleep(0.2)
        controller.click_text("Permissions")
        controller.click_text("Camera")
        controller.click_text("Don't allow")
        controller.launch_app("uk.co.bentley.mybentley")

        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        while not controller.is_text_present("ADD A VEHICLE"):
            controller.click_by_image("Icons/Homescreen_Right_Arrow.png")
            sleep(0.05)
        controller.small_swipe_up()
        sleep(0.2)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/button_add_dashboard_module_add_vehicle")

        if controller.is_text_present("Open Camera"):
            pass
            ##########
            # Wait for tester to scan VIN
            ##########

            # automate the process of adding vin and checking car is displayed

    except Exception as e:
        error_log(e, "010", img_service)

def Add_VIN_011():
    try:
        # if manual:
        controller.launch_app("com.android.settings")
        if controller.click_by_image("Icons/settings_search.png"):
            controller.enter_text("Bentley")
        controller.click_text("My Bentley")
        sleep(0.2)
        controller.click_text("Permissions")
        controller.click_text("Camera")
        controller.click_text("Don't allow")
        controller.launch_app("uk.co.bentley.mybentley")

        can_add_VIN = False
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        while not controller.is_text_present("ADD A VEHICLE"):
            controller.click_by_image("Icons/Homescreen_Right_Arrow.png")
            sleep(0.05)
        controller.small_swipe_up()
        sleep(0.2)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/button_add_dashboard_module_add_vehicle")

        if controller.click_text("Go to settings"):
            log("'Go to settings' option displayed when camera access disabled")
        else:
            fail_log("'Go to settings' option not displayed when camera access disabled", "011", img_service)

        if controller.is_text_present("Camera permission"):
            if controller.click_text("Allow only while using the app"):
                log("Camera access enabled")
                controller.launch_app("uk.co.bentley.mybentley")
            else:
                fail_log("Camera access cannot be enabled", "011", img_service)
        else:
            if controller.click_text("Permissions"):
                log("Phone settings opened")
            else:
                fail_log("Phone settings not opened", "011", img_service)

            if controller.click_text("Camera") and controller.click_text("Allow only while using the app"):
                log("Camera access enabled")
                controller.launch_app("uk.co.bentley.mybentley")
                if controller.is_text_present("Open Camera"):
                    can_add_VIN = True
                    log("'Open Camera' option displayed when camera access enabled")
                else:
                    fail_log("'Open Camera' option not displayed when camera access enabled, so VIN cannot be added", "011", img_service)
                    controller.launch_app("uk.co.bentley.mybentley")
            else:
                fail_log("Camera access cannot be enabled, so VIN cannot be added", "011", img_service)
                controller.launch_app("uk.co.bentley.mybentley")

        if can_add_VIN:
            controller.click_text("Open Camera")
            ##########
            # Wait for tester to scan VIN
            ##########

            # automate the process of adding vin and checking car is displayed


        controller.click_by_image("Icons/back_icon.png")
        controller.small_swipe_down()
        while compare_with_expected_crop("Icons/Homescreen_Left_Arrow.png"):
            controller.click_by_image("Icons/Homescreen_Left_Arrow.png")

    except Exception as e:
        error_log(e, "011", img_service)

def Add_VIN_012():
    try:
        log("Done in 011")
    except Exception as e:
        error_log(e, "012", img_service)

def Add_VIN_013():
    try:
        controller.launch_app("com.android.settings")
        if controller.click_by_image("Icons/settings_search.png"):
            controller.enter_text("Bentley")
        controller.click_text("My Bentley")
        sleep(0.2)
        controller.click_text("Permissions")
        controller.click_text("Camera")
        controller.click_text("Allow only while using the app")
        controller.launch_app("uk.co.bentley.mybentley")

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
            fail_log("'Locating your VIN' option not displayed", "013", img_service)

        if controller.is_text_present("Locating your VIN") and controller.click_text("OK"):
            log("'Locating your VIN' popup displayed")
        else:
            fail_log("'Locating your VIN' popup not displayed", "013", img_service)

        controller.click_by_image("Icons/back_icon.png")
        controller.small_swipe_down()
        while compare_with_expected_crop("Icons/Homescreen_Left_Arrow.png"):
            controller.click_by_image("Icons/Homescreen_Left_Arrow.png")

    except Exception as e:
        error_log(e, "013", img_service)

def Add_VIN_014():
    try:
        # if manual:
        controller.launch_app("com.android.settings")
        if controller.click_by_image("Icons/settings_search.png"):
            controller.enter_text("Bentley")
        controller.click_text("My Bentley")
        sleep(0.2)
        controller.click_text("Permissions")
        controller.click_text("Camera")
        controller.click_text("Allow only while using the app")
        controller.launch_app("uk.co.bentley.mybentley")

        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        while not controller.is_text_present("ADD A VEHICLE"):
            controller.click_by_image("Icons/Homescreen_Right_Arrow.png")
        controller.small_swipe_up()
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/button_add_dashboard_module_add_vehicle")
        controller.click_text("Open Camera")

        ################
        # Wait for tester to scan
        ################

        if controller.click_text("Scan VIN again"):
            log("Scan again message displayed")
        else:
            fail_log("Scan again message not displayed", "014", img_service)
        sleep(0.5)
        if controller.is_text_present("Centre your VIN in the box above"):
            log("VIN scan screen displayed")
        else:
            fail_log("VIN scan screen not displayed", "014", img_service)

        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/back_icon.png")
        controller.small_swipe_down()
        while compare_with_expected_crop("Icons/Homescreen_Left_Arrow.png"):
            controller.click_by_image("Icons/Homescreen_Left_Arrow.png")
    except Exception as e:
        error_log(e, "014", img_service)

def Add_VIN_015():
    try:
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
                fail_log("Emojis are able to alter the VIN section", "015", img_service)
                controller.clear_text(5)
        controller.click_by_image("Icons/keyboard_icon.png")
        if controller.click_by_image("Icons/special_char_icon.png"):
            if controller.click_by_image("Icons/!_char_icon.png") and controller.click_by_image("Icons/#_char_icon.png"):
                if controller.is_text_present("Enter VIN manually"):
                    log("Special characters cannot be entered in the VIN section")
                else:
                    fail_log("Special characters have altered the VIN section", "015", img_service)
            else:
                fail_log("Special characters not found", "015", img_service)
        else:
            fail_log("Special characters not found", "015", img_service)
        sleep(1)

        controller.click_by_image("Icons/back_icon.png")
        while compare_with_expected_crop("Icons/Homescreen_Left_Arrow.png"):
            controller.click_by_image("Icons/Homescreen_Left_Arrow.png")

    except Exception as e:
        error_log(e, "015", img_service)

def Add_VIN_016():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "016", img_service)

def Add_VIN_017():
    try:
        blocked_log("Test blocked - Can't check style guide")
    except Exception as e:
        error_log(e, "017", img_service)