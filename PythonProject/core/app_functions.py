from time import sleep
from common_utils.android_image_comparision import *
# from core.globals import current_email, current_password, current_vin, second_email, second_password, current_name
import core.globals as globals
from core.globals import current_vin, current_email
from core.log_emitter import blocked_log, fail_log, log
from gui.manual_check import manual_check

def app_login(email="", password="", safe_type = False):
    if email == "":
        email = globals.current_email
    if password == "":
        password = globals.current_password
    success_tracker = []
    sleep(1)
    success_tracker.append(1) if controller.wait_for_text_and_click("LOGIN OR REGISTER") else success_tracker.append(0)
    controller.wait_for_text("WELCOME", 30)
    while controller.is_text_present("WELCOME"):
        controller.enter_text(f"%s%s%s%s%s{email}")
        sleep(1)
        if controller.is_text_present("Email must be a valid email address"):
            controller.click_by_image("Icons/login_page_x.png")
        controller.wait_for_text_and_click("LOGIN OR REGISTER")
    controller.wait_for_text("Log in – Enter password")
    if not controller.is_text_present("CREATE ACCOUNT"):
        while controller.is_text_present("Log in – Enter password"):
            controller.enter_text(password, safe_type=safe_type)
            sleep(2)
            if controller.is_text_present("Sorry, wrong password. Please try again"):
                success_tracker.append(0)
                return success_tracker
    else:
        controller.click_by_image("Icons/login_page_x.png")
        app_login(email, password)
    success_tracker.append(1) if controller.wait_for_text("DASHBOARD") else success_tracker.append(0)

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
            sleep(1)
            return True
    return False

def app_login_setup(demo=False, second_account=False):
    if controller.is_text_present("LOGIN OR REGISTER"):
        if demo:
            controller.click_text("DISCOVER MY BENTLEY")
            if not controller.wait_for_text("Demo mode"):
                blocked_log("Test blocked - Unable to launch demo mode to begin testcase")
                sleep(1)
                return False
        elif globals.current_email and globals.current_password:
            if not second_account:
                login_check = app_login(globals.current_email, globals.current_password)
            else:
                login_check = app_login(globals.second_email, globals.second_password)
            if 0 in login_check:
                blocked_log("Test blocked - Unable to login to begin testcase")
                sleep(1)
                return False
        else:
            blocked_log("Test blocked - Account logged out and credentials not provided")
            sleep(1)
            return False
    sleep(1)
    dash_check()
    return True

def app_logout_setup():
    if not controller.is_text_present("LOGIN OR REGISTER"):
        if not controller.click_by_image("Icons/Logout_Icon.png"):
            controller.click_by_image("Icons/Profile_Icon.png")
            controller.click_text("General")
            controller.click_text("Log out")
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/button_alert_dialog_positive")

        if not controller.wait_for_text("LOGIN OR REGISTER", 60):
            blocked_log("Test blocked - Unable to logout to begin testcase")
            sleep(1)
            return False
    sleep(1)
    return True

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

def delete_vin():
    while compare_with_expected_crop("Icons/Homescreen_Left_Arrow.png"):
        controller.click_by_image("Icons/Homescreen_Left_Arrow.png")
    while True:
        controller.click_by_image("Icons/info_btn.png")
        if controller.is_text_present(globals.current_vin):
            break
        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/Homescreen_Right_Arrow.png")
        if controller.is_text_present("ADD A VEHICLE"):
            blocked_log("Test blocked - vehicle with given vin not found on account")
            break
    controller.click_text("Delete vehicle")
    if controller.click_text("Delete"):
        if not controller.wait_for_text("Vehicle details successfully submitted. Your request is now being validated. Once confirmed your vehicle will disappear from your virtual garage.", 30):
            blocked_log("Test blocked - Unable to delete vin to complete testcase")
        sleep(1)
    else:
        service_reset()

def add_vin(num , img_service, optical=False, settings_check=False, optical_check=False):
    if controller.wait_for_text("DASHBOARD"):
        while not controller.is_text_present("ADD A VEHICLE"):
            controller.click_by_image("Icons/Homescreen_Right_Arrow.png")
        controller.small_swipe_up()
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/button_add_dashboard_module_add_vehicle")
        if optical or optical_check:
            if not controller.click_text("Open Camera"):
                if controller.click_text("Go to settings"):
                    log("Camera permissions not enabled")
                else:
                    fail_log("Camera option not displayed", num, img_service)
                if settings_check and controller.click_text("Permissions"):
                    log("Settings page opens on expected page")
                elif settings_check and not controller.click_text("Permissions"):
                    fail_log("Settings page does not open on expected page", num, img_service)
                controller.click_text("Camera")
                controller.click_text("Allow only while using the app")
                controller.launch_app("uk.co.bentley.mybentley")
            if controller.click_text("Open Camera"):
                log("Camera permissions enabled")
            else:
                fail_log("Camera option not displayed after enabling permission", num, img_service)
            if controller.is_text_present("Centre your VIN in the box above"):
                log("Optical character recognition opened as expected")
            else:
                fail_log("Optical character recognition failed to be opened", num, img_service)
            manual_check(
                instruction="Scan the VIN via 'Optical Character Recognition(OCR)",
                test_id=num,
                service=img_service,
                take_screenshot=False
            )
            if optical_check:
                controller.click_by_image("Icons/back_icon.png")
                controller.click_by_text("ADD A VEHICLE")
                controller.small_swipe_up()
                controller.click_text("Enter VIN manually")
                controller.enter_text(globals.current_vin)
        else:
            controller.small_swipe_up()
            controller.click_text("Enter VIN manually")
            controller.enter_text(globals.current_vin)
        controller.click_text("CONFIRM")
        log("VIN entered") if controller.wait_for_text("YOUR PREFERRED BENTLEY RETAILER") else fail_log("VIN not entered", num, img_service)
        controller.click_by_image("Icons/Homescreen_Right_Arrow.png")
        while not compare_with_expected_crop("Images/retailer_search.png"):
            sleep(0.5)
        controller.wait_for_text_and_click("Search by retailer name or location")
        controller.enter_text("Manchester")
        controller.click_text("Bentley Manchester")
        controller.wait_for_text_and_click("CONFIRM")
        log("Retailer selected") if controller.wait_for_text("ADD YOUR BENTLEY", 60) else fail_log("Retailer failed to be selected", num, img_service)
        controller.wait_for_text_and_click("Continue")
        if controller.is_text_present("VIN"):
            controller.click_text("Continue")
        first_name = controller.d(resourceId="firstname").get_text()
        if not first_name == globals.current_name.split(" ")[0]:
            controller.click_by_resource_id("firstname")
            controller.clear_text(len(first_name))
            controller.enter_text(globals.current_name.split(" ")[0])
            controller.click_text("YOUR DETAILS")
        last_name = controller.d(resourceId="lastname").get_text()
        if not last_name == globals.current_name.split(" ")[1]:
            controller.click_by_resource_id("lastname")
            controller.clear_text(len(last_name))
            controller.enter_text(globals.current_name.split(" ")[1])
            controller.click_text("YOUR DETAILS")
        log("Name entered") if controller.click_text("Continue") else fail_log("Name not entered", num, img_service)
        if not controller.is_text_present("YOUR ADDRESS"):
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
        else:
            controller.click_text("Continue")
            controller.swipe_up(0.01)
        controller.click_text("Continue")
        controller.wait_for_text("Your Mobile Number")
        log("Location details entered") if controller.wait_for_text_and_click("Your Mobile Number") else fail_log("Location details not entered", num, img_service)
        if controller.click_text("Area Code"):
            controller.swipe_up(0.035)
            controller.click_text("+44")
            controller.click_text("Mobile Phone")
            controller.enter_text("07123456789")
        else:
            controller.click_text("Continue")
        controller.click_text("Continue")
        timeout_check = 0
        while not controller.is_text_present("Request Submitted"):
            sleep(0.5)
            timeout_check += 1
            if timeout_check > 100:
                break
        log("Phone number added") if controller.is_text_present("Request Submitted") else fail_log("Phone number not added", num, img_service)
        controller.click_text("Continue")
        log("Vehicle added to new account") if controller.is_text_present("DASHBOARD") else fail_log("Vehicle not added to new account", num, img_service)
        sleep(1)
        return find_car()

def service_reset():
    controller.d.press("recent")
    sleep(0.5)
    controller.wait_for_text_and_click("Close all")
    controller.launch_app("uk.co.bentley.mybentley")
    while not controller.is_text_present("DASHBOARD") and not controller.is_text_present("LOGIN OR REGISTER"):
        sleep(0.2)

def dash_check():
    if not (compare_with_expected_crop("Icons/navigation_icon.png", 0.9) or compare_with_expected_crop("Icons/home_icon.png", 0.9)):
        service_reset()

def app_refresh(num, img_service, msg="", wait=0):
    controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    sleep(wait)
    controller.swipe_down()

    while (not compare_with_expected_crop("Icons/Error_Icon.png") and not controller.is_text_present("Update vehicle data")) or controller.is_text_present("Updating..."):
        sleep(3)

    if compare_with_expected_crop("Icons/Error_Icon.png"):
        fail_log("Error displayed on refresh", num, img_service)
        controller.click_by_image("Icons/Error_Icon.png")
    else:
        controller.click_text("Update vehicle data")
        sleep(1)
        while controller.is_text_present("Updating..."):
            sleep(1)
        while not compare_with_expected_crop("Icons/Error_Icon.png") and not controller.is_text_present("Vehicle status successfully retrieved"):
            sleep(1)
        if controller.is_text_present("Vehicle status successfully retrieved"):
            log(f"Vehicle data updated {msg}")
        else:
            fail_log(f"Vehicle data not updated {msg}", num, img_service)
        controller.click_by_image("Icons/Error_Icon.png")

def find_car(add_car=False, num=None, img_service=None):
    timeout_check = 0
    while controller.is_text_present("ADD A VEHICLE"):
        sleep(1)
        timeout_check += 1
        if timeout_check > 10:
            break
    controller.click_by_image("Icons/info_btn.png")
    if not controller.is_text_present(current_vin):
        controller.click_by_image("Icons/back_icon.png")
    else:
        controller.click_by_image("Icons/back_icon.png")
        return True
    while controller.click_by_image("Icons/Homescreen_Left_Arrow.png"):
        pass
    while compare_with_expected_crop("Icons/Homescreen_Right_Arrow.png"):
        if controller.click_by_image("Icons/info_btn.png"):
            if not controller.is_text_present(current_vin):
                controller.click_by_image("Icons/back_icon.png")
            else:
                controller.click_by_image("Icons/back_icon.png")
                return True
        else:
            break
        controller.click_by_image("Icons/Homescreen_Right_Arrow.png")
    if add_car:
        return add_vin(num, img_service)
    else:
        return False

def primary_user_check(num, img_service, vts_check=True):
    find_car(True, num, img_service)
    controller.small_swipe_up()
    if controller.is_text_present("PRIMARY USER ALREADY SET"):
        fail_log("Another user is already primary user for this VIN", num, img_service)
        return False
    if controller.is_text_present("SET YOUR PRIMARY USER"):
        if not controller.is_text_present("VIEW VEHICLE CODE"):
            controller.click_text("GENERATE VEHICLE CODE")
            controller.wait_for_text_and_click("Generate vehicle code")
            controller.wait_for_text("VEHICLE CODE", 30)
        else:
            controller.click_text("VIEW VEHICLE CODE")
            controller.wait_for_text("VEHICLE CODE", 30)
        vehicle_code = controller.d.xpath('//*[@text="Please enter following vehicle code in your Bentley infotainment system to set your primary user:"]/following-sibling::android.widget.TextView[1]').get_text()
        manual_check(
            instruction=f"On vehicle HMI navigate to Primary user page\nSuccessfully set the primary user for the vin({current_vin}) using the vehicle code: {vehicle_code} and email: {current_email}",
            test_id=num,
            service=img_service,
            take_screenshot=False
        )
        service_reset()
        if vts_check:
            controller.small_swipe_up()
            if controller.is_text_present("ACTIVATE STOLEN VEHICLE TRACKING"):
                fail_log("Stolen vehicle tracking not activated", num, img_service)
                return False
        return True
    else:
        if controller.is_text_present("ACTIVATE STOLEN VEHICLE TRACKING"):
            fail_log("Stolen vehicle tracking not activated", num, img_service)
            return False
        controller.small_swipe_down()
        return True