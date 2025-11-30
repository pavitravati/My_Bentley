from common_utils.android_image_comparision import *
from core.log_emitter import log, fail_log, metric_log, error_log, blocked_log
from time import sleep
from core.app_functions import remote_swipe, enable_flight_mode, disable_flight_mode, app_login_setup, app_logout_setup, \
    app_login, delete_vin, add_vin
from core.globals import current_name, current_email, country, current_pin
from datetime import datetime
from core.globals import manual_run
from gui.manual_check import manual_check

img_service = "Stolen Vehicle Tracking"

def Stolen_Vehicle_Tracking_001():
    try:
        if country == "eur":
            blocked_log("Test blocked - All done in vehicle")#
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "001", img_service)

def Stolen_Vehicle_Tracking_002():
    try:    
        if country == "eur":
            blocked_log("Test blocked - All done in vehicle")#
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "002", img_service)

def Stolen_Vehicle_Tracking_003():
    try:
        if country == "eur":
            if app_login_setup():
                controller.click_by_image("Icons/remote_icon.png")
                if remote_swipe("STOLEN VEHICLE TRACKING"):
                    Stolen_vehicle_tracking = controller.d(text="STOLEN VEHICLE TRACKING")
                    status = Stolen_vehicle_tracking.sibling(resourceId="uk.co.bentley.mybentley:id/textView_status_car_remote_item").get_text()
                    if 'active' in status:
                        log("Stolen vehicle tracking feature is displayed as active")
                    else:
                        fail_log("Stolen vehicle tracking feature is not displayed as active", "003", img_service)
                else:
                    fail_log("Stolen vehicle tracking feature not displayed", "003", img_service)

                manual_check(
                    instruction="Call to VTS Customer Support Centre(i.e. Bentley Connected Car Contact Centre(B4C)) and request for VTS feature availability for 'UK' based vehicle",
                    test_id="003",
                    service=img_service,
                    take_screenshot=False
                )

                controller.swipe_down(0.05)
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "003", img_service)

# Need an account with a non uk vehicle to test this, either get from tester in ui or manually like this
def Stolen_Vehicle_Tracking_004():
    try:
        app_logout_setup()
        app_login("18790-p-live@gqf.33mail.com", "Bentley$2024", True)
        controller.click_by_image("Icons/remote_icon.png")
        if not remote_swipe("STOLEN VEHICLE TRACKING"):
            log("Stolen vehicle tracking service not displayed for vehicle not provisioned for VTS")
        else:
            fail_log("Stolen vehicle tracking service displayed for vehicle not provisioned for VTS", "004", img_service)
        app_logout_setup()
        app_login_setup()
    except Exception as e:
        error_log(e, "004", img_service)

# Need to see full process, manual phone verify but if it is the phone that is used then can be automated
def Stolen_Vehicle_Tracking_005():
    try:
        if country == "eur":
            if app_login_setup():
                delete_vin()
                add_vin("005", img_service)
                controller.click_by_image("Icons/remote_icon.png")
                if remote_swipe("STOLEN VEHICLE TRACKING"):
                    stolen_vehicle_tracking = controller.d(text="STOLEN VEHICLE TRACKING")
                    status = stolen_vehicle_tracking.sibling(resourceId="uk.co.bentley.mybentley:id/textView_status_car_remote_item").get_text()
                    if status == "Not activated":
                        log("SVT status displays as 'Not activated' when stolen vehicle tracking not activated")
                    else:
                        fail_log("SVT status not displayed as 'Not activated' when stolen vehicle tracking not activated", "005", img_service)
                    controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
                    controller.swipe_up()
                    controller.click_text("ACTIVATE")
                    controller.wait_for_text_and_click("Accept Terms & Conditions")
                    controller.wait_for_text_and_click("CONFIRM")
                    first_name = controller.d(resourceId="uk.co.bentley.mybentley:id/editText_registration_name_first_name").get_text()
                    last_name = controller.d(resourceId="uk.co.bentley.mybentley:id/editText_registration_name_last_name").get_text()
                    if controller.is_text_present(current_email) and f"{first_name} {last_name}" == current_name:
                        log("Name and email auto filled when activating SVT")
                    else:
                        fail_log("Name and email not successfully auto filled when activating SVT", "005", img_service)
                        if controller.click_text("First Name"):
                            controller.enter_text(current_name.split()[0])
                        if controller.click_text("Last Name"):
                            controller.enter_text(current_name.split()[1])
                        controller.swipe(500, 500, 500, 100)
                        if controller.click_text("Email address"):
                            controller.enter_text(current_email)
                    controller.wait_for_text_and_click("CONTINUE")

                    if not (controller.is_text_present("Address") and controller.is_text_present("City") and controller.is_text_present("Postcode")):
                        log("Address details auto filled when activating SVT")
                    else:
                        fail_log("Address details not auto filled when activating SVT", "005", img_service)
                        if controller.click_text("Address"):
                            controller.enter_text("25%sPyms%sLane", False)
                        controller.swipe(500, 500, 500, 100)
                        if controller.click_text("City"):
                            controller.enter_text("Crewe")
                        controller.swipe(500, 500, 500, 100)
                        if controller.click_text("Postcode"):
                            controller.enter_text("CW1%s3PL")
                        sleep(0.5)
                    controller.wait_for_text_and_click("CONTINUE")
                    sleep(1)
                    controller.click(500, 500)
                    if not controller.is_text_present("Mobile number"):
                        log("Mobile number successfully auto filled when activating SVT")
                    else:
                        fail_log("Mobile number not auto filled when activating SVT", "005", img_service)
                        manual_check(
                            instruction="Enter the a phone number to continue the SVT activation",
                            test_id="005",
                            service=img_service,
                            take_screenshot=False
                        )
                    controller.wait_for_text_and_click("CONTINUE")
                    controller.wait_for_text_and_click("Confirm")
                    # Look into automating this when the phone used to verify is the phone used in the testing
                    manual_check(
                        instruction="Enter the code sent to the mobile number to activate VTS",
                        test_id="005",
                        service=img_service,
                        take_screenshot=False
                    )
                    ### What happens now
                    # After activating it
                    controller.click_by_image("Icons/remote_icon.png")
                    if remote_swipe("STOLEN VEHICLE TRACKING"):
                        stolen_vehicle_tracking = controller.d(text="STOLEN VEHICLE TRACKING")
                        status = stolen_vehicle_tracking.sibling(resourceId="uk.co.bentley.mybentley:id/textView_status_car_remote_item").get_text()
                        if status == "Licence pending":
                            log("SVT status displays as 'Not activated' when stolen vehicle tracking not activated")
                        else:
                            fail_log("SVT status not displayed as 'Not activated' when stolen vehicle tracking not activated","005", img_service)
                        # whatever is needed for it to then be activated
                        stolen_vehicle_tracking = controller.d(text="STOLEN VEHICLE TRACKING")
                        status = stolen_vehicle_tracking.sibling(resourceId="uk.co.bentley.mybentley:id/textView_status_car_remote_item").get_text()
                        if 'active' in status:
                            log("Stolen vehicle tracking feature is displayed as active")
                        else:
                            fail_log("Stolen vehicle tracking feature is not displayed as active", "005", img_service)
                else:
                    fail_log("Stolen vehicle tracking feature not displayed in car remote screen", "005", img_service)
                controller.swipe_down(0.05)
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "005", img_service)

def Stolen_Vehicle_Tracking_006():
    try:
        if country == "eur":
            blocked_log("Test blocked - Repeat of previous test")
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "006", img_service)

def Stolen_Vehicle_Tracking_007():
    try:
        if country == "eur":
            if app_login_setup():
                controller.click_by_image("Icons/remote_icon.png")
                if remote_swipe("STOLEN VEHICLE TRACKING"):
                    controller.click_text("STOLEN VEHICLE TRACKING")
                    if controller.is_text_present("My Alerts") and controller.is_text_present("Configure") and controller.click_text("My Details"):
                        log("Stolen vehicle tracking page displayed and My details tab clicked")
                    else:
                        fail_log("Stolen vehicle tracking page not displayed", "006", img_service)

                    my_details_metrics = controller.extract_svt_details()
                    if len(my_details_metrics) == 9:
                        log("All Stolen vehicle tracking details extracted")
                    else:
                        fail_log("Failed to extract all stolen vehicle tracking details", "007", img_service)
                    for label, value in my_details_metrics.items():
                        metric_log(f"{label}: {value}")

                    controller.click_text("My Vehicle Security Tracking certificate")
                    if controller.wait_for_text("CERTIFICATE"):
                        log("Certificate can be opened ready to download")
                        controller.click_by_image("Icons/back_icon.png")
                    else:
                        fail_log("Certificate cannot be opened", "006", img_service)
                        controller.click_by_image("Icons/Error_Icon.png")

                else:
                    fail_log("Stolen vehicle tracking feature not displayed", "007", img_service)

                controller.click_by_image("Icons/back_icon.png")
                controller.swipe_down(0.05)
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "007", img_service)

def Stolen_Vehicle_Tracking_008():
    try:
        if country == "eur":
            if app_login_setup():
                controller.click_by_image("Icons/remote_icon.png")
                if remote_swipe("STOLEN VEHICLE TRACKING"):
                    controller.click_text("STOLEN VEHICLE TRACKING")
                    controller.click_text("My Details")
                    if controller.click_text("My Bentley"):
                        log("My Bentley section clicked")
                    else:
                        fail_log("My Bentley section not found", "008", img_service)

                    model = controller.d(resourceId="uk.co.bentley.mybentley:id/dropDown_vts_registration_vehicle_model").get_text()
                    metric_log(f"Vehicle Model: {model}") if model else fail_log("Model not found", "008", img_service)

                    vehicle_colour = controller.d(resourceId="uk.co.bentley.mybentley:id/dropDown_vts_registration_vehicle_color")
                    metric_log(f"Vehicle Colour: {vehicle_colour.get_text()}") if vehicle_colour else fail_log("Vehicle colour not found", "008", img_service)

                    vehicle_country = controller.d(resourceId="uk.co.bentley.mybentley:id/editText_vts_registration_vehicle_country").get_text()
                    metric_log(f"Vehicle Country: {vehicle_country}") if vehicle_country else fail_log("Vehicle country not found", "008", img_service)

                    vehicle_reg = controller.d(resourceId="uk.co.bentley.mybentley:id/editText_vts_registration_vehicle_country")
                    metric_log(f"Vehicle Registration: {vehicle_reg.get_text()}") if vehicle_reg else fail_log("Vehicle registration not found", "008", img_service)

                    if model and vehicle_colour and vehicle_country and vehicle_reg:
                        log("All details extracted from My Bentley page")
                    else:
                        fail_log("Not all details extracted from My Bentley Page", "008", img_service)

                controller.click_by_image("Icons/back_icon.png")
                controller.click_by_image("Icons/back_icon.png")
                controller.swipe_down(0.05)
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "008", img_service)

#Tested, lots of things so some false fails
def Stolen_Vehicle_Tracking_009():
    try:
        if country == "eur":
            if app_login_setup():
                controller.click_by_image("Icons/remote_icon.png")
                if remote_swipe("STOLEN VEHICLE TRACKING"):
                    controller.click_text("STOLEN VEHICLE TRACKING")
                    controller.click_text("My Details")
                    controller.click_text("Name")
                    controller.click_by_resource_id("uk.co.bentley.mybentley:id/editText_registration_name_first_name")
                    controller.enter_text("123")
                    controller.click_text("SAVE CHANGES")
                    if controller.wait_for_text(f"{current_name.split(" ")[0]}123 gqm", 30) and not controller.is_text_present("MY BENTLEY"):
                        log("Name successfully edited")
                    else:
                        fail_log("Name failed to be edited", "009", img_service)
                    sleep(0.5)
                    controller.click_text("Name")
                    controller.click_by_resource_id("uk.co.bentley.mybentley:id/editText_registration_name_first_name")
                    controller.clear_text(3)
                    controller.click_text("SAVE CHANGES")
                    controller.wait_for_text("Name")
                    if not controller.wait_for_text(current_name, 30):
                        fail_log("Name failed to be reset to original name", "009", img_service)

                    controller.click_text("Email Address")
                    controller.click_by_resource_id("uk.co.bentley.mybentley:id/editText_registration_name_email")
                    while controller.d(resourceId="uk.co.bentley.mybentley:id/editText_registration_name_email").get_text() != "Email address":
                        controller.click_by_resource_id("uk.co.bentley.mybentley:id/editText_registration_name_email")
                        controller.clear_text(16)
                    controller.enter_text("newtest@gqm.anonaddy.com")
                    controller.click_text("SAVE CHANGES")
                    while controller.is_text_present("Loading..."):
                        sleep(1)
                    log("Email successfully edited") if controller.wait_for_text(f"newtest@gqm.anonaddy.com") else fail_log("Email failed to be edited", "009", img_service)
                    controller.click_text("Email Address")
                    controller.click_by_resource_id("uk.co.bentley.mybentley:id/editText_registration_name_email")
                    while controller.d(resourceId="uk.co.bentley.mybentley:id/editText_registration_name_email").get_text() != "Email address":
                        controller.click_by_resource_id("uk.co.bentley.mybentley:id/editText_registration_name_email")
                        controller.clear_text(16)
                    controller.enter_text(current_email)
                    controller.click_text("SAVE CHANGES")
                    while controller.is_text_present("Loading..."):
                        sleep(1)
                    if not controller.wait_for_text(current_email, 30):
                        fail_log("Email address failed to be reset to original email", "009", img_service)

                    address_value = controller.d.xpath(
                        '//*[@text="Address"]/following-sibling::android.widget.TextView[1]')
                    current_address = address_value.text.replace("\n", ".")
                    controller.click_text("Address")
                    controller.click_by_resource_id(
                        "uk.co.bentley.mybentley:id/textView_vts_registration_address_country")
                    log("Country can be changed") if controller.is_text_present(
                        "Search for a country or language") else fail_log("Country cannot be changed", "009",
                                                                          img_service)
                    controller.click_by_image("Icons/back_icon.png")
                    controller.click_by_resource_id(
                        "uk.co.bentley.mybentley:id/editText_vts_registration_address_address")
                    controller.enter_text("2")
                    controller.swipe_down()
                    controller.click_text("SAVE CHANGES")
                    while controller.is_text_present("Loading..."):
                        sleep(1)
                    lines = current_address.split(".")
                    controller.click_by_image("Icons/back_icon.png")
                    controller.click_text("STOLEN VEHICLE TRACKING")
                    if controller.wait_for_text(f'{lines[0]}\n{lines[1]}2\n{lines[2]}\n{lines[3]}'):
                        log("Address successfully edited")
                    else:
                        fail_log("Address failed to be edited", "009", img_service)
                    controller.click_text("Address")
                    controller.click_by_resource_id(
                        "uk.co.bentley.mybentley:id/editText_vts_registration_address_address")
                    controller.clear_text(1)
                    controller.swipe_down()
                    controller.click_text("SAVE CHANGES")
                    while controller.is_text_present("Loading..."):
                        sleep(1)
                    controller.click_by_image("Icons/back_icon.png")
                    controller.click_text("STOLEN VEHICLE TRACKING")
                    if not controller.wait_for_text(current_address.replace(".", "\n")):
                        fail_log("Address failed to be reset to original address", "009", img_service)

                    controller.click_text("Primary Mobile Number")
                    controller.click_by_resource_id("uk.co.bentley.mybentley:id/editText_vts_registration_phone_number_input")
                    current_phone = controller.d(resourceId="uk.co.bentley.mybentley:id/editText_vts_registration_phone_number_input").get_text()
                    last_digit = int(current_phone[-1])
                    controller.clear_text(1)
                    controller.enter_text(last_digit+1 if last_digit != 9 else 1)
                    controller.click_text("SAVE CHANGES")
                    log("Mobile number can be edited") if controller.wait_for_text("Confirm your mobile number") else fail_log("Mobile number cannot be edited", "009", img_service)
                    controller.click_text("Edit")
                    controller.click_by_image("Icons/back_icon.png")

                    controller.swipe_up()
                    sleep(0.2)
                    btn = controller.d.xpath('//*[@text="My Security Language"]/following-sibling::android.view.View/android.widget.Button')
                    if btn.exists:
                        controller.click(btn.info['bounds']['left'] + 10, btn.info['bounds']['top'] + 10)
                    if controller.is_text_present(
                            "Sorry, it is not possible to change this. For further information please contact Vodafone."):
                        log("Correct details displayed when security language info button clicked")
                    else:
                        fail_log("Correct details not displayed when security language info button clicked", "009", img_service)
                    controller.click_text("OK")

                    controller.click_text("My Security Question")
                    controller.click_by_resource_id("uk.co.bentley.mybentley:id/editText_vts_registration_security_que_answer")
                    controller.enter_text(1)
                    controller.click_text("SAVE CHANGES")
                    if controller.is_text_present("Confirm and submit"):
                        controller.click_text("Edit")
                        log("Security question answer can be edited")
                    else:
                        fail_log("Security question answer failed to be edited", "009", img_service)
                    controller.click_by_image("Icons/back_icon.png")

                    controller.swipe_down()
                    controller.click_by_image("Icons/back_icon.png")
                    controller.swipe_down(0.05)
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "009", img_service)

def Stolen_Vehicle_Tracking_010():
    try:
        if country == "eur":
            if app_login_setup():
                controller.click_by_image("Icons/remote_icon.png")
                if remote_swipe("STOLEN VEHICLE TRACKING"):
                    controller.click_text("STOLEN VEHICLE TRACKING")
                    controller.click_text("My Details")

                    controller.click_text("My Bentley")
                    current_colour = controller.d(resourceId="uk.co.bentley.mybentley:id/dropDown_vts_registration_vehicle_color").get_text()
                    controller.click_by_resource_id("uk.co.bentley.mybentley:id/dropDown_vts_registration_vehicle_color")
                    if current_colour == "Beige":
                        new_colour = "Black"
                        controller.click_text("Black")
                    else:
                        new_colour = "Beige"
                        controller.click_text("Beige")
                    controller.click_by_resource_id("uk.co.bentley.mybentley:id/editText_vts_registration_vehicle_registration_number")
                    current_reg = controller.d(resourceId="uk.co.bentley.mybentley:id/editText_vts_registration_vehicle_registration_number").get_text()
                    controller.clear_text(1)
                    if current_reg[-1] != 'A':
                        reg_end = 'A'
                        controller.enter_text(reg_end)
                    else:
                        reg_end = 'B'
                        controller.enter_text(reg_end)
                    current_model = controller.d(resourceId="uk.co.bentley.mybentley:id/dropDown_vts_registration_vehicle_model").get_text()
                    controller.click_text("SAVE CHANGES")
                    while controller.is_text_present("Loading..."):
                        sleep(1)
                    if controller.wait_for_text(f"{new_colour}, {current_model}, {current_reg[:-1]}{reg_end}"):
                        log("My Bentley details successfully edited")
                    else:
                        fail_log("My Bentley details not successfully edited", "010", img_service)
                    controller.click_text("My Bentley")
                    controller.click_by_resource_id("uk.co.bentley.mybentley:id/dropDown_vts_registration_vehicle_color")
                    sleep(0.5)
                    if not controller.click_text(current_colour):
                        controller.swipe_up()
                        controller.click_text(current_colour)
                    controller.click_by_resource_id("uk.co.bentley.mybentley:id/editText_vts_registration_vehicle_registration_number")
                    controller.clear_text(1)
                    controller.enter_text(current_reg[-1])
                    controller.click_text("SAVE CHANGES")
                    while controller.is_text_present("Loading..."):
                        sleep(1)
                    sleep(2)
                    if not controller.is_text_present(f"{current_colour}, {current_model}, {current_reg}"):
                        fail_log("My Bentley details set to original details", "010", img_service)

                controller.click_by_image("Icons/back_icon.png")
                controller.swipe_down(0.05)
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "010", img_service)

def Stolen_Vehicle_Tracking_011():
    try:
        if country == "eur":
            if app_login_setup():
                controller.click_by_image("Icons/remote_icon.png")
                if remote_swipe("STOLEN VEHICLE TRACKING"):
                    controller.click_text("STOLEN VEHICLE TRACKING")
                    controller.click_text("My Details")
                    controller.swipe_up()

                    if controller.click_text("My Security Question"):
                        log("My security questions tab clicked")
                        controller.click_text("What was the name of your first school?")
                        controller.click_by_resource_id("uk.co.bentley.mybentley:id/editText_vts_registration_security_que_answer")
                        controller.enter_text("test1")
                        controller.click_text("SAVE CHANGES")
                        controller.click_text("Confirm and submit")
                        while controller.is_text_present("Loading..."):
                            sleep(1)
                        controller.click_text("My Security Question")
                        if controller.is_text_present("test1"):
                            log("First security question is editable")
                        else:
                            fail_log("First security question failed to be edited", "011", img_service)

                        controller.click_text("Where is your place of birth?")
                        controller.click_by_resource_id("uk.co.bentley.mybentley:id/editText_vts_registration_security_que_answer")
                        controller.enter_text("test2")
                        controller.click_text("SAVE CHANGES")
                        controller.click_text("Confirm and submit")
                        while controller.is_text_present("Loading..."):
                            sleep(1)
                        controller.click_text("My Security Question")
                        if controller.is_text_present("test2"):
                            log("Second security question is editable")
                        else:
                            fail_log("Second security question failed to be edited", "011", img_service)

                        controller.click_text("What is the name of your first pet?")
                        controller.click_by_resource_id("uk.co.bentley.mybentley:id/editText_vts_registration_security_que_answer")
                        controller.enter_text("test3")
                        controller.click_text("SAVE CHANGES")
                        controller.click_text("Confirm and submit")
                        while controller.is_text_present("Loading..."):
                            sleep(1)
                        controller.click_text("My Security Question")
                        if controller.is_text_present("test3"):
                            log("Third security question is editable")
                        else:
                            fail_log("Third security question failed to be edited", "011", img_service)

                        # Set second answer back to 'Crewe'
                        controller.click_text("Where is your place of birth?")
                        controller.click_by_resource_id("uk.co.bentley.mybentley:id/editText_vts_registration_security_que_answer")
                        controller.enter_text("Crewe")
                        controller.click_text("SAVE CHANGES")
                        controller.click_text("Confirm and submit")
                        while controller.is_text_present("Loading..."):
                            sleep(1)
                        sleep(0.5)
                        controller.swipe_down()
                    else:
                        fail_log("My security questions tab not found", "011", img_service)

                controller.click_by_image("Icons/back_icon.png")
                controller.swipe_down(0.05)
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "011", img_service)

def Stolen_Vehicle_Tracking_012():
    try:
        if country == "eur":
            if app_login_setup():
                controller.click_by_image("Icons/remote_icon.png")
                if remote_swipe("STOLEN VEHICLE TRACKING"):
                    controller.click_text("STOLEN VEHICLE TRACKING")
                    if controller.click_text("Configure"):
                        log("Configure tab clicked")
                    else:
                        fail_log("Configure tab not found", "012", img_service)
                    controller.swipe_up()

                    if controller.is_text_present("Garage mode") and controller.is_text_present("Transport mode") and controller.click_text("Deactivation mode"):
                        log("Configure page displayed")
                    else:
                        fail_log("Configure page not displayed successfully", "012", img_service)
                    controller.click_text("SYNC TO CAR")
                    controller.enter_pin("1234")
                    sleep(2)

                    while controller.is_text_present("Sending message to car"):
                        sleep(1)
                    sleep(0.2)
                    controller.click_text("STOLEN VEHICLE TRACKING")
                    controller.click_text("My Alerts")
                    if controller.is_text_present("DEACTIVATION MODE ENABLED"):
                        deactivation_mode = controller.d(text="DEACTIVATION MODE ENABLED")
                        time = deactivation_mode.sibling(index="1").get_text()
                        log(f"Deactivation mode enabled ({time}) and shown in 'My Alerts' page")
                    else:
                        fail_log("Deactivation mode not displayed as enabled in 'My Alerts' page", "012", img_service)
                    if manual_run:
                        controller.click_text("Configure")
                        controller.click_text("Deactivation mode")
                        controller.swipe_down()
                        controller.click_text("SYNC TO CAR")
                        controller.enter_pin("1234")
                        sleep(2)
                        while controller.is_text_present("Sending message to car"):
                            sleep(1)
                        sleep(0.5)

                controller.click_by_image("Icons/back_icon.png")
                controller.swipe_down(0.05)
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "012", img_service)

def Stolen_Vehicle_Tracking_013():
    try:
        if country == "eur":
            if app_login_setup():
                controller.click_by_image("Icons/remote_icon.png")
                if remote_swipe("STOLEN VEHICLE TRACKING"):
                    controller.click_text("STOLEN VEHICLE TRACKING")
                    if manual_run:
                        controller.click_text("Configure")
                        controller.swipe_up()
                        if controller.click_text("Deactivation mode") and controller.click_text("SYNC TO CAR"):
                            log("Deactivation mode enabled and synced to car")
                        else:
                            fail_log("Deactivation mode not enabled or synced to car", "013", img_service)
                        controller.enter_pin(current_pin)
                        sleep(2)
                        while controller.is_text_present("Sending message to car"):
                            sleep(1)
                        sleep(0.5)
                        controller.click_text("STOLEN VEHICLE TRACKING")
                    controller.click_text("My Alerts")
                    if controller.is_text_present("DEACTIVATION MODE ENABLED"):
                        garage_mode = controller.d(text="DEACTIVATION MODE ENABLED")
                        time = garage_mode.sibling(index="1").get_text()
                        log(f"Deactivation mode enabled ({time}) and shown in 'My Alerts' page")
                    else:
                        fail_log("Deactivation mode not displayed as enabled in 'My Alerts' page", "013", img_service)

                    if enable_flight_mode():
                        log("Flight mode enabled on phone")
                    else:
                        fail_log("Flight mode not enabled on phone", "013", img_service)
                    sleep(1)

                    controller.click_text("Configure")
                    controller.click_text("Garage mode")
                    controller.click_text("SYNC TO CAR")
                    controller.enter_pin("1234")
                    sleep(1)
                    if controller.is_text_present("An error occurred when setting special mode. Please try again."):
                        log("Sync to car failed in flight mode")
                    else:
                        fail_log("Expected error message not shown", "013", img_service)
                    controller.click_text("Cancel")

                    # Disable flight mode and then the special mode
                    disable_flight_mode()
                    sleep(5)
                    controller.click_text("SYNC TO CAR")
                    controller.enter_pin("1234")
                    sleep(2)
                    while controller.is_text_present("Sending message to car"):
                        sleep(1)

                controller.swipe_down(0.05)
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "013", img_service)

def Stolen_Vehicle_Tracking_014():
    try:
        if country == "eur":
            blocked_log("Test blocked - Can't be automated")
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "014", img_service)

def Stolen_Vehicle_Tracking_015():
    try:
        if country == "eur":
            blocked_log("Test blocked - All done in car")
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "015", img_service)

def Stolen_Vehicle_Tracking_016():
    try:
        if country == "eur":
            blocked_log("Test blocked - All done in car")
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "016", img_service)

def Stolen_Vehicle_Tracking_017():
    try:
        if country == "eur":
            blocked_log("Test blocked - All done in car")
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "017", img_service)

def Stolen_Vehicle_Tracking_018():
    try:
        if country == "eur":
            blocked_log("Test blocked - All done in car")
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "018", img_service)

def Stolen_Vehicle_Tracking_019():
    try:
        if country == "eur":
            if app_login_setup():
                # manual_check(
                #     instruction="Go to vehicle Settings and successfully perform full factory reset",
                #     test_id="019",
                #     service=img_service,
                #     take_screenshot=False
                # )
                controller.click_by_image("Icons/remote_icon.png")
                if remote_swipe("STOLEN VEHICLE TRACKING"):
                    Stolen_vehicle_tracking = controller.d(text="STOLEN VEHICLE TRACKING")
                    status = Stolen_vehicle_tracking.sibling(resourceId="uk.co.bentley.mybentley:id/textView_status_car_remote_item").get_text()
                    if 'Currently active' in status:
                        log("Stolen vehicle tracking feature is displayed as active")
                    else:
                        fail_log("Stolen vehicle tracking feature is not displayed as active", "019", img_service)

                controller.swipe_down(0.05)
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "019", img_service)

def special_mode_check(mode, num):
    controller.click_text("STOLEN VEHICLE TRACKING")
    if controller.click_text("Configure"):
        log("Configure tab clicked")
    else:
        fail_log("Configure tab not found", num, img_service)
    sleep(0.2)
    if mode == "Deactivation mode":
        controller.swipe_up()
    else:
        controller.swipe_down()
        if not controller.is_text_present(mode):
            controller.small_swipe_up()
    controller.click_text(f"{mode}")
    controller.click_text("SYNC TO CAR")
    controller.enter_pin(current_pin)
    sleep(2)
    if controller.is_text_present("Sending message to car"):
        log(f"{mode} mode sent to car")
    else:
        fail_log(f"{mode} not sent to car", num, img_service)
    while controller.is_text_present("Sending message to car"):
        sleep(1)
    sleep(0.2)

    controller.click_text("STOLEN VEHICLE TRACKING")
    controller.click_text("My Alerts")
    if controller.is_text_present(f"{mode.upper()} ENABLED"):
        special_mode = controller.d(text=f"{mode.upper()} ENABLED")
        time = special_mode.sibling(index="1").get_text()
        log(f"{mode} enabled ({time}) and shown in 'My Alerts' page")
    else:
        fail_log(f"{mode} not displayed as enabled in 'My Alerts' page", num, img_service)

    controller.click_text("Configure")
    if mode == "Deactivation mode":
        controller.swipe_up()
    else:
        controller.swipe_down()
        if not controller.is_text_present(mode):
            controller.small_swipe_up()
    controller.click_text(f"{mode}") if compare_with_expected_crop("Icons/Interior_heating_toggle.png") else None
    controller.click_text("SYNC TO CAR")
    controller.enter_pin(current_pin)
    sleep(2)
    if controller.is_text_present("Sending message to car"):
        log(f"Disabled {mode} sent to car")
    else:
        fail_log(f"Disabled {mode} not sending to car", num, img_service)
    while controller.is_text_present("Sending message to car"):
        sleep(1)
    sleep(0.2)
    controller.click_text("STOLEN VEHICLE TRACKING")
    controller.click_text("My Alerts")
    if controller.is_text_present("NO MESSAGES"):
        log(f"{mode} successfully disabled")
    else:
        fail_log(f"{mode} not disabled", num, img_service)

def special_mode_timer_check(mode, num):
    controller.click_text("STOLEN VEHICLE TRACKING")
    controller.click_text("My Alerts")
    if not controller.is_text_present(f"{mode.upper()} ENABLED"):
        controller.click_text("Configure")
        sleep(0.2)
        if mode == "Deactivation mode":
            controller.swipe_up()
        else:
            controller.swipe_down()
            if not controller.is_text_present(mode):
                controller.small_swipe_up()
        controller.click_text(f"{mode}")
        controller.click_text("SYNC TO CAR")
        controller.enter_pin(current_pin)
        sleep(2)
        while controller.is_text_present("Sending message to car"):
            sleep(1)
        sleep(0.2)
        controller.click_text("STOLEN VEHICLE TRACKING")
        controller.click_text("My Alerts")
    special_mode = controller.d(text=f"{mode.upper()} ENABLED")
    time = special_mode.sibling(index="1").get_text()[13:18]
    now = datetime.now()
    target_time = datetime.strptime(time, "%H:%M").replace(year=now.year, month=now.month, day=now.day)
    time_diff = ((target_time - now).total_seconds())
    sleep(time_diff + 5)
    controller.click_text("Configure")
    if mode == "Deactivation mode":
        controller.swipe_up()
    else:
        controller.swipe_down()
        if not controller.is_text_present(mode):
            controller.small_swipe_up()
    controller.click_text(f"{mode}") if compare_with_expected_crop("Icons/Interior_heating_toggle.png") else None
    controller.click_text("My Alerts")
    if controller.is_text_present("NO MESSAGES"):
        log(f"{mode} disabled after timer runs out")
    else:
        fail_log(f"{mode} not disabled after timer runs out", num, img_service)

def Stolen_Vehicle_Tracking_020():
    try:
        if country == "eur":
            if app_login_setup():
                controller.click_by_image("Icons/remote_icon.png")
                if remote_swipe("STOLEN VEHICLE TRACKING"):
                    special_mode_check("Garage mode", "020")

                controller.click_by_image("Icons/back_icon.png")
                controller.swipe_down(0.05)
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "020", img_service)

# This test sleeps till the time in which the timer says it will run out. ask if this should be changed this so that it just check timer set
def Stolen_Vehicle_Tracking_021():
    try:
        if country == "eur":
            if app_login_setup():
                controller.click_by_image("Icons/remote_icon.png")
                if remote_swipe("STOLEN VEHICLE TRACKING"):
                    special_mode_timer_check("Garage mode", "021")
                    controller.click_by_image("Icons/back_icon.png")
                    controller.swipe_down(0.05)
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "021", img_service)

def Stolen_Vehicle_Tracking_022():
    try:
        if country == "eur":
            if app_login_setup():
                controller.click_by_image("Icons/remote_icon.png")
                if remote_swipe("STOLEN VEHICLE TRACKING"):
                    special_mode_check("Transport mode", "022")

                controller.click_by_image("Icons/back_icon.png")
                controller.swipe_down(0.05)
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "022", img_service)

def Stolen_Vehicle_Tracking_023():
    try:
        if country == "eur":
            if app_login_setup():
                controller.click_by_image("Icons/remote_icon.png")
                if remote_swipe("STOLEN VEHICLE TRACKING"):
                    special_mode_timer_check("Transport mode", "023")
                    controller.click_by_image("Icons/back_icon.png")
                    controller.swipe_down(0.05)
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "023", img_service)

def Stolen_Vehicle_Tracking_024():
    try:
        if country == "eur":
            if app_login_setup():
                controller.click_by_image("Icons/remote_icon.png")
                if remote_swipe("STOLEN VEHICLE TRACKING"):
                    special_mode_check("Deactivation mode", "024")

                controller.click_by_image("Icons/back_icon.png")
                controller.swipe_down(0.05)
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "024", img_service)

def Stolen_Vehicle_Tracking_025():
    try:
        if country == "eur":
            if app_login_setup():
                controller.click_by_image("Icons/remote_icon.png")
                if remote_swipe("STOLEN VEHICLE TRACKING"):
                    special_mode_timer_check("Deactivation mode", "025")
                    controller.click_by_image("Icons/back_icon.png")
                    controller.swipe_down(0.05)
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "025", img_service)

def Stolen_Vehicle_Tracking_026():
    try:
        if country == "eur":
            if app_login_setup():
                controller.click_by_image("Icons/remote_icon.png")
                if remote_swipe("STOLEN VEHICLE TRACKING"):
                    controller.click_text("STOLEN VEHICLE TRACKING")
                    controller.click_text("My Alerts")
                    if controller.is_text_present("NO MESSAGES"):
                        controller.click_text("Configure")
                        sleep(0.2)
                        controller.click_text("Transport mode")
                        controller.click_text("SYNC TO CAR")
                        controller.enter_pin("1234")
                        sleep(2)
                        while controller.is_text_present("Sending message to car"):
                            sleep(1)
                        sleep(0.2)
                    log("Transport mode enabled")
                    controller.click_text("STOLEN VEHICLE TRACKING")
                    controller.click_text("Configure")
                    sleep(0.2)
                    controller.click_text("Garage mode")
                    if controller.is_text_present("Please disable active mode"):
                        log("Garage mode blocked with transport mode enabled")
                    else:
                        fail_log("Garage mode not blocked with transport mode enabled", "026", img_service)
                    controller.click_text("OK")
                    sleep(0.2)
                    controller.click_text("Transport mode")
                    controller.click_text("SYNC TO CAR")
                    controller.enter_pin("1234")
                    sleep(2)
                    if controller.is_text_present("Sending message to car"):
                        log("Transport mode disabled")
                    else:
                        fail_log("Transport mode not disabled", "026", img_service)
                    while controller.is_text_present("Sending message to car"):
                        sleep(1)
                    sleep(0.2)
                    controller.click_text("STOLEN VEHICLE TRACKING")
                    controller.click_text("Garage mode")
                    controller.click_text("SYNC TO CAR")
                    controller.enter_pin("1234")
                    sleep(2)
                    if controller.is_text_present("Sending message to car"):
                        log("Garage mode enabled")
                    else:
                        fail_log("Garage mode not enabled", "026", img_service)
                    while controller.is_text_present("Sending message to car"):
                        sleep(1)
                    sleep(0.2)
                    controller.click_text("STOLEN VEHICLE TRACKING")
                    controller.click_text("My Alerts")
                    sleep(0.2)
                    if controller.is_text_present("GARAGE MODE ENABLED"):
                        log("Garage mode enabled successfully")
                    else:
                        fail_log("Garage mode not enabled successfully", "026", img_service)
                    controller.click_text("Configure")
                    sleep(0.2)
                    controller.click_text("Garage mode")
                    controller.click_text("SYNC TO CAR")
                    controller.enter_pin("1234")
                    sleep(2)
                    while controller.is_text_present("Sending message to car"):
                        sleep(1)
                    sleep(0.2)

                controller.swipe_down(0.05)
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "026", img_service)

def Stolen_Vehicle_Tracking_027():
    try:
        if country == "eur":
            if app_login_setup():
                manual_check(
                    instruction="1. Initiate a call to VTS Customer Support Team\n2. Request the VTS Customer Support Team to activate 'Transport Mode'",
                    test_id="027",
                    service=img_service,
                    take_screenshot=False
                )
                controller.click_by_image("Icons/remote_icon.png")
                if remote_swipe("STOLEN VEHICLE TRACKING"):
                    controller.click_text("STOLEN VEHICLE TRACKING")
                    controller.click_text("My Alerts")
                    if controller.is_text_present("TRANSPORT MODE ENABLED"):
                        log("Transport mode enabled")
                    else:
                        fail_log("Transport mode not enabled", "027", img_service)

                if manual_run:
                    controller.click_text("Configure")
                    controller.click_text("Transport mode")
                    controller.click_text("SYNC TO CAR")
                    controller.enter_pin(current_pin)
                    sleep(2)
                    while controller.is_text_present("Sending message to car"):
                        sleep(1)
                    sleep(0.2)

                controller.click_by_image("Icons/back_icon.png")
                controller.swipe_down(0.05)
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "027", img_service)

def Stolen_Vehicle_Tracking_028():
    try:
        if country == "eur":
            if app_login_setup():
                controller.click_by_image("Icons/remote_icon.png")
                if remote_swipe("STOLEN VEHICLE TRACKING"):
                    controller.click_text("STOLEN VEHICLE TRACKING")
                    controller.click_text("My Alerts")
                    if controller.is_text_present("NO MESSAGES"):
                        controller.click_text("Configure")
                        sleep(0.2)
                        controller.click_text("Transport mode")
                        controller.click_text("SYNC TO CAR")
                        controller.enter_pin(current_pin)
                        sleep(2)
                        while controller.is_text_present("Sending message to car"):
                            sleep(1)
                        sleep(0.2)
                        manual_check(
                            instruction="1. Initiate a call to VTS Customer Support Team\n2. Request the VTS Customer Support Team to deactivate 'Garage Mode'/'Transport Mode'/'Deactivation Mode' (Transport mode should be active)",
                            test_id="028",
                            service=img_service,
                            take_screenshot=False
                        )
                    controller.click_text("STOLEN VEHICLE TRACKING")
                    controller.click_text("My Alerts")
                    sleep(0.2)
                    if controller.is_text_present("NO MESSAGES"):
                        log("Special mode deactivated")
                    else:
                        fail_log("Special mode not deactivated", "028", img_service)

                controller.click_by_image("Icons/back_icon.png")
                controller.swipe_down(0.05)
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "028", img_service)

def Stolen_Vehicle_Tracking_029():
    try:
        if country == "eur":
            blocked_log("Test blocked - Can't be automated")
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "029", img_service)

def Stolen_Vehicle_Tracking_030():
    try:
        if country == "eur":
            blocked_log("Test blocked - Can't be automated")
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "030", img_service)

def Stolen_Vehicle_Tracking_031():
    try:
        if country == "eur":
            blocked_log("Test blocked - Can't be automated")
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "031", img_service)

def Stolen_Vehicle_Tracking_032():
    try:
        if country == "eur":
            blocked_log("Test blocked - Can't be automated")
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "032", img_service)

def Stolen_Vehicle_Tracking_033():
    try:
        if country == "eur":
            blocked_log("Test blocked - Can't be automated")
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "033", img_service)

def Stolen_Vehicle_Tracking_034():
    try:
        if country == "eur":
            blocked_log("Test blocked - Can't be automated")
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "034", img_service)

def Stolen_Vehicle_Tracking_035():
    try:
        if country == "eur":
            blocked_log("Test blocked - Can't be automated")
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "035", img_service)

def Stolen_Vehicle_Tracking_036():
    try:
        if country == "eur":
            blocked_log("Test blocked - Can't be automated")
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "036", img_service)

def Stolen_Vehicle_Tracking_037():
    try:
        if country == "eur":
            blocked_log("Test blocked - Can't be automated")
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "037", img_service)

def Stolen_Vehicle_Tracking_038():
    try:
        if country == "eur":
            blocked_log("Test blocked - Can't be automated")
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "038", img_service)

def Stolen_Vehicle_Tracking_039():
    try:
        if country == "eur":
            blocked_log("Test blocked - Can't be automated")
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "039", img_service)

def Stolen_Vehicle_Tracking_040():
    try:
        if country == "eur":
            blocked_log("Test blocked - Can't be automated")
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "040", img_service)

def Stolen_Vehicle_Tracking_041():
    try:
        if country == "eur":
            blocked_log("Test blocked - Can't be automated")
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "041", img_service)

def Stolen_Vehicle_Tracking_042():
    try:
        if country == "eur":
            blocked_log("Test blocked - Can't be automated")
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "042", img_service)

def Stolen_Vehicle_Tracking_043():
    try:
        if country == "eur":
            if app_login_setup():
                controller.click_by_image("Icons/remote_icon.png")
                if remote_swipe("STOLEN VEHICLE TRACKING"):
                    controller.click_text("STOLEN VEHICLE TRACKING")
                    controller.click_text("My Details")
                    sleep(0.2)
                    controller.click_text("My Vehicle Security Tracking certificate")
                    if controller.wait_for_text("CERTIFICATE"):
                        log("Certificate displayed")
                    else:
                        fail_log("Certificate not displayed", "043", img_service)
                    sleep(1)
                    if compare_with_expected_crop("Icons/certificate_share_icon.png"):
                        log("Certificate can be downloaded")
                    else:
                        fail_log("Certificate cannot be downloaded", "043", img_service)
                    controller.click_by_image("Icons/back_icon.png")

                controller.click_by_image("Icons/back_icon.png")
                controller.swipe_down(0.05)
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "043", img_service)

def Stolen_Vehicle_Tracking_044():
    try:
        if country == "eur":
            if app_login_setup():
                controller.click_by_image("Icons/remote_icon.png")
                if remote_swipe("STOLEN VEHICLE TRACKING"):
                    controller.click_text("STOLEN VEHICLE TRACKING")
                    controller.click_text("My Details")
                    sleep(0.2)
                    controller.click_by_image("Icons/phone_icon.png")
                    if controller.wait_for_text("Call now"):
                        log("'Call now' pop up displayed")
                    else:
                        fail_log("'Call now' pop up not displayed", "044", img_service)
                    sleep(1)
                    if controller.is_text_present("+44 333 122 2222"):
                        log("Vodafone contact details displayed")
                    else:
                        fail_log("Vodafone contact details not displayed", "044", img_service)
                    controller.click_text("Cancel")

                controller.click_by_image("Icons/back_icon.png")
                controller.swipe_down(0.05)
                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "044", img_service)

def Stolen_Vehicle_Tracking_045():
    try:
        if country == "eur":
            if app_login_setup():
                controller.click_by_image("Icons/remote_icon.png")
                if remote_swipe("STOLEN VEHICLE TRACKING"):
                    controller.click_text("STOLEN VEHICLE TRACKING")
                    controller.click_text("My Details")
                    sleep(0.2)
                    controller.click_by_image("Icons/phone_icon.png")
                    controller.wait_for_text("Call now")
                    controller.click_text("+44 333 122 2222")
                    manual_check(
                        instruction="Check call should is initiated successfully to VTS Customer Care Centre",
                        test_id="045",
                        service=img_service,
                        take_screenshot=False
                    )
                    controller.launch_app("uk.co.bentley.mybentley")
                    controller.click_text("Cancel")
                controller.click_by_image("Icons/back_icon.png")
                controller.swipe_down(0.05)
                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "045", img_service)

def Stolen_Vehicle_Tracking_046():
    try:
        if country == "eur":
            blocked_log("Test blocked - Can't be automated")
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "046", img_service)

def Stolen_Vehicle_Tracking_047():
    try:
        if country == "eur":
            blocked_log("Test blocked - Can't be automated")
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "047", img_service)

def Stolen_Vehicle_Tracking_048():
    try:
        if country == "eur":
            blocked_log("Test blocked - Can't be automated")
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "048", img_service)


def Stolen_Vehicle_Tracking_049():
    try:
        if country == "eur":
            if app_login_setup():
                controller.click_by_image("Icons/remote_icon.png")
                if remote_swipe("STOLEN VEHICLE TRACKING"):
                    controller.click_text("STOLEN VEHICLE TRACKING")
                    controller.click_text("My Details")
                    sleep(0.2)
                    controller.swipe_up()
                    controller.click_text("My Security Language")
                    sleep(3)
                    if controller.is_text_present("STOLEN VEHICLE TRACKING"):
                        log("My Security Language not clickable")
                    else:
                        fail_log("My Security Language changes page when clicked", "049", img_service)
                    sleep(0.2)
                    btn = controller.d.xpath('//*[@text="My Security Language"]/following-sibling::android.view.View/android.widget.Button')
                    if btn.exists:
                        controller.click(btn.info['bounds']['left']+10, btn.info['bounds']['top']+10)

                    if controller.is_text_present("Sorry, it is not possible to change this. For further information please contact Vodafone."):
                        log("Correct details displayed when info button clicked")
                    else:
                        fail_log("Correct details not displayed when info button clicked", "049", img_service)
                    controller.click_text("OK")
                    controller.swipe_down()

                controller.click_by_image("Icons/back_icon.png")
                controller.swipe_down(0.05)
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "049", img_service)

def Stolen_Vehicle_Tracking_050():
    try:
        if country == "eur":
            if app_login_setup():
                controller.click_by_image("Icons/remote_icon.png")
                if remote_swipe("STOLEN VEHICLE TRACKING"):
                    controller.click_text("STOLEN VEHICLE TRACKING")
                    controller.click_text("My Details")
                    controller.click_text("My Bentley")
                    controller.click_by_image("Icons/info_btn.png",0.7)
                    if controller.is_text_present("Sorry, it is not possible to change this. For further information please contact Vodafone."):
                        log("Country section cannot be clicked or edited")
                    else:
                        fail_log("Country section not unclickable like expected", "050", img_service)
                    controller.click_text("OK")
                    if not compare_with_expected_crop("Icons/Homescreen_Right_Arrow.png"):
                        log("Model edit arrow not displayed")
                    else:
                        fail_log("Model edit arrow displayed", "050", img_service)
                    controller.click_by_image("Icons/back_icon.png")

                controller.click_by_image("Icons/back_icon.png")
                controller.swipe_down(0.05)
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "050", img_service)

def Stolen_Vehicle_Tracking_051():
    try:
        if country == "eur":
            blocked_log("Test blocked - Can't check style guide")
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "051", img_service)