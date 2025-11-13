from common_utils.android_image_comparision import *
from core.log_emitter import log, fail_log, metric_log, error_log
from time import sleep
from core.app_functions import remote_swipe, enable_flight_mode, disable_flight_mode
from core.globals import current_name, current_email
from datetime import datetime

img_service = "Stolen Vehicle Tracking"

# Done in car
def Stolen_Vehicle_Tracking_001():
    try:
        pass
    except Exception as e:
        error_log(e, "001", img_service)

#Done in car
def Stolen_Vehicle_Tracking_002():
    try:
        pass
    except Exception as e:
        error_log(e, "002", img_service)

# Tested (no call)
def Stolen_Vehicle_Tracking_003():
    try:
        controller.click_by_image("Icons/windows_icon.png")
        if remote_swipe("STOLEN VEHICLE TRACKING"):
            Stolen_vehicle_tracking = controller.d(text="STOLEN VEHICLE TRACKING")
            status = Stolen_vehicle_tracking.sibling(resourceId="uk.co.bentley.mybentley:id/textView_status_car_remote_item").get_text()
            if 'active' in status:
                log("Stolen vehicle tracking feature is displayed as active")
            else:
                fail_log("Stolen vehicle tracking feature is not displayed as active", "003", img_service)
        else:
            fail_log("Stolen vehicle tracking feature not displayed", "003", img_service)

        # Call can't be automated
        controller.swipe_down(0.05)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "003", img_service)

def Stolen_Vehicle_Tracking_004():
    try:
        # How to have no vts license

        controller.click_by_image("Icons/windows_icon.png")
        if not remote_swipe("STOLfEN VEHICLE TRACKING"):
            log("Stolen vehicle tracking feature not displayed in car remote screen")
        else:
            fail_log("Stolen vehicle tracking section displayed in car remote screen", "004", img_service)
        controller.swipe_down(0.05)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "004", img_service)

def Stolen_Vehicle_Tracking_005():
    try:
        # Best way to add vehicle with vts license

        controller.click_by_image("Icons/windows_icon.png")
        if remote_swipe("STOLfEN VEHICLE TRACKING"):
            log("Stolen vehicle tracking feature displayed in car remote screen")
        else:
            fail_log("Stolen vehicle tracking feature not displayed in car remote screen", "005", img_service)
        controller.swipe_down(0.05)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "005", img_service)

def Stolen_Vehicle_Tracking_006():
    try:
        # No vts license
        controller.click_by_image("Icons/windows_icon.png")
        if remote_swipe("STOLEN VEHICLE TRACKING"):
            Stolen_vehicle_tracking = controller.d(text="STOLEN VEHICLE TRACKING")
            status = Stolen_vehicle_tracking.sibling(resourceId="uk.co.bentley.mybentley:id/textView_status_car_remote_item").get_text()
            # Check what it would actually say
            if 'Not active' in status:
                log("Stolen vehicle tracking feature is displayed as active")
            else:
                fail_log("Stolen vehicle tracking feature is not displayed as active", "006", img_service)
        else:
            fail_log("Stolen vehicle tracking feature not displayed", "006", img_service)
        controller.swipe_down(0.05)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

        # vts license pending
        controller.click_by_image("Icons/windows_icon.png")
        if remote_swipe("STOLEN VEHICLE TRACKING"):
            Stolen_vehicle_tracking = controller.d(text="STOLEN VEHICLE TRACKING")
            status = Stolen_vehicle_tracking.sibling(resourceId="uk.co.bentley.mybentley:id/textView_status_car_remote_item").get_text()
            # Check what it would actually say
            if 'pending' in status:
                log("Stolen vehicle tracking feature is displayed as active")
            else:
                fail_log("Stolen vehicle tracking feature is not displayed as active", "006", img_service)
        else:
            fail_log("Stolen vehicle tracking feature not displayed", "006", img_service)
        controller.swipe_down(0.05)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

        # vts license active
        controller.click_by_image("Icons/windows_icon.png")
        if remote_swipe("STOLEN VEHICLE TRACKING"):
            Stolen_vehicle_tracking = controller.d(text="STOLEN VEHICLE TRACKING")
            status = Stolen_vehicle_tracking.sibling(resourceId="uk.co.bentley.mybentley:id/textView_status_car_remote_item").get_text()
            if 'active' in status:
                log("Stolen vehicle tracking feature is displayed as active")
            else:
                fail_log("Stolen vehicle tracking feature is not displayed as active", "006", img_service)
        else:
            fail_log("Stolen vehicle tracking feature not displayed", "006", img_service)
        controller.swipe_down(0.05)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "006", img_service)

# Tested
def Stolen_Vehicle_Tracking_007():
    try:
        controller.click_by_image("Icons/windows_icon.png")
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
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "007", img_service)

#Tested
def Stolen_Vehicle_Tracking_008():
    try:
        controller.click_by_image("Icons/windows_icon.png")
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
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "008", img_service)

#Tested, lots of things so some false fails
def Stolen_Vehicle_Tracking_009():
    try:
        controller.click_by_image("Icons/windows_icon.png")
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

            address_value = controller.d.xpath('//*[@text="Address"]/following-sibling::android.widget.TextView[1]')
            current_address = address_value.text.replace("\n", ".")
            controller.click_text("Address")
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/textView_vts_registration_address_country")
            log("Country can be changed") if controller.is_text_present("Search for a country or language") else fail_log("Country cannot be changed", "009", img_service)
            controller.click_by_image("Icons/back_icon.png")
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/editText_vts_registration_address_address")
            controller.enter_text("2")
            controller.swipe_down()
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/editText_vts_registration_address_city")
            controller.enter_text("2")
            controller.swipe_down()
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/editText_vts_registration_address_postcode")
            controller.clear_text(1)
            controller.enter_text("a")
            controller.click_text("SAVE CHANGES")
            while controller.is_text_present("Loading..."):
                sleep(1)
            lines = current_address.split(".")
            controller.click_by_image("Icons/back_icon.png")
            controller.click_text("STOLEN VEHICLE TRACKING")
            if controller.wait_for_text(f'{lines[0]}\n{lines[1]}2\n{lines[2]}2\n{lines[3][:-1]}a'):
                log("Address successfully edited")
            else:
                fail_log("Address failed to be edited", "009", img_service)
            controller.click_text("Address")
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/editText_vts_registration_address_address")
            controller.clear_text(1)
            controller.swipe_down()
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/editText_vts_registration_address_city")
            controller.clear_text(1)
            controller.swipe_down()
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/editText_vts_registration_address_postcode")
            controller.clear_text(1)
            controller.enter_text(current_address.split(".")[3][-1])
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
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "009", img_service)

# Tested
def Stolen_Vehicle_Tracking_010():
    try:
        controller.click_by_image("Icons/windows_icon.png")
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
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "010", img_service)

# Tested
def Stolen_Vehicle_Tracking_011():
    try:
        controller.click_by_image("Icons/windows_icon.png")
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
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "011", img_service)

# Tested
def Stolen_Vehicle_Tracking_012():
    try:
        controller.click_by_image("Icons/windows_icon.png")
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
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "012", img_service)

# Tested
def Stolen_Vehicle_Tracking_013():
    try:
        controller.click_by_image("Icons/windows_icon.png")
        if remote_swipe("STOLEN VEHICLE TRACKING"):
            controller.click_text("STOLEN VEHICLE TRACKING")
            controller.click_text("Configure")

            if controller.click_text("Garage mode") and controller.click_text("SYNC TO CAR"):
                log("Garage mode enabled and synced to car")
            else:
                fail_log("Garage mode not enabled or synced to car", "013", img_service)
            controller.enter_pin("1234")
            sleep(2)
            while controller.is_text_present("Sending message to car"):
                sleep(1)
            sleep(0.5)
            controller.click_text("STOLEN VEHICLE TRACKING")
            controller.click_text("My Alerts")
            if controller.is_text_present("GARAGE MODE ENABLED"):
                garage_mode = controller.d(text="GARAGE MODE ENABLED")
                time = garage_mode.sibling(index="1").get_text()
                log(f"Garage mode enabled ({time}) and shown in 'My Alerts' page")
            else:
                fail_log("Garage mode not displayed as enabled in 'My Alerts' page", "012", img_service)

            if enable_flight_mode():
                log("Flight mode enabled on phone")
            else:
                fail_log("Flight mode not eneabled on phone", "013", img_service)
            sleep(1)

            controller.click_text("Configure")
            controller.click_text("Garage mode")
            controller.click_text("SYNC TO CAR")
            controller.enter_pin("1234")
            sleep(1)
            if controller.is_text_present("An error occurred when setting special mode. Please try again."):
                log("Sync to car failed in flight mode")
            else:
                fail_log("Expected erorr message not shown", "013", img_service)
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
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "013", img_service)

# Can't be automated
def Stolen_Vehicle_Tracking_014():
    try:
        log("Can't be automated")
    except Exception as e:
        error_log(e, "014", img_service)

# Done in car
def Stolen_Vehicle_Tracking_015():
    try:
        log("Done in car")
    except Exception as e:
        error_log(e, "015", img_service)

# Done in car
def Stolen_Vehicle_Tracking_016():
    try:
        log("Done in car")
    except Exception as e:
        error_log(e, "016", img_service)

# Done in car
def Stolen_Vehicle_Tracking_017():
    try:
        log("Done in car")
    except Exception as e:
        error_log(e, "017", img_service)

# Done in car
def Stolen_Vehicle_Tracking_018():
    try:
        log("Done in car")
    except Exception as e:
        error_log(e, "018", img_service)

def Stolen_Vehicle_Tracking_019():
    try:
        # After factory reset in vehicle...
        controller.click_by_image("Icons/windows_icon.png")
        if remote_swipe("STOLEN VEHICLE TRACKING"):
            Stolen_vehicle_tracking = controller.d(text="STOLEN VEHICLE TRACKING")
            status = Stolen_vehicle_tracking.sibling(resourceId="uk.co.bentley.mybentley:id/textView_status_car_remote_item").get_text()
            if 'Currently active' in status:
                log("Stolen vehicle tracking feature is displayed as active")
            else:
                fail_log("Stolen vehicle tracking feature is not displayed as active", "019", img_service)

        controller.swipe_down(0.05)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "019", img_service)

# Tested
def Stolen_Vehicle_Tracking_020():
    try:
        controller.click_by_image("Icons/windows_icon.png")
        if remote_swipe("STOLEN VEHICLE TRACKING"):
            controller.click_text("STOLEN VEHICLE TRACKING")
            if controller.click_text("Configure"):
                log("Configure tab clicked")
            else:
                fail_log("Configure tab not found", "020", img_service)
            sleep(0.2)
            controller.click_text("Garage mode")
            controller.click_text("SYNC TO CAR")
            controller.enter_pin("1234")
            sleep(2)
            if controller.is_text_present("Sending message to car"):
                log("Garage mode sent to car")
            else:
                fail_log("Garage mode not sent to car", "020", img_service)
            while controller.is_text_present("Sending message to car"):
                sleep(1)
            sleep(0.2)

        controller.swipe_down(0.05)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "020", img_service)

# Tested
def Stolen_Vehicle_Tracking_021():
    try:
        controller.click_by_image("Icons/windows_icon.png")
        if remote_swipe("STOLEN VEHICLE TRACKING"):
            controller.click_text("STOLEN VEHICLE TRACKING")
            controller.click_text("My Alerts")
            if controller.is_text_present("GARAGE MODE ENABLED"):
                garage_mode = controller.d(text="GARAGE MODE ENABLED")
                time = garage_mode.sibling(index="1").get_text()
                log(f"Garage mode enabled ({time}) and shown in 'My Alerts' page")
            else:
                fail_log("Garage mode not displayed as enabled in 'My Alerts' page", "020", img_service)

        controller.click_by_image("Icons/back_icon.png")
        controller.swipe_down(0.05)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "021", img_service)

# Tested
# This test sleeps till the time in which the timer says it will run out.
def Stolen_Vehicle_Tracking_022():
    try:
        controller.click_by_image("Icons/windows_icon.png")
        if remote_swipe("STOLEN VEHICLE TRACKING"):
            controller.click_text("STOLEN VEHICLE TRACKING")
            controller.click_text("My Alerts")
            if not controller.is_text_present("GARAGE MODE ENABLED"):
                controller.click_text("Configure")
                sleep(0.2)
                controller.click_text("Garage mode")
                controller.click_text("SYNC TO CAR")
                controller.enter_pin("1234")
                sleep(2)
                while controller.is_text_present("Sending message to car"):
                    sleep(1)
                sleep(0.2)
                controller.click_text("STOLEN VEHICLE TRACKING")
                controller.click_text("My Alerts")
            garage_mode = controller.d(text="GARAGE MODE ENABLED")
            time = garage_mode.sibling(index="1").get_text()[13:18]
            now = datetime.now()
            target_time = datetime.strptime(time, "%H:%M").replace(year=now.year, month=now.month, day=now.day)
            time_diff = ((target_time - now).total_seconds())
            sleep(time_diff+5)
            controller.click_text("Configure")
            controller.click_text("Garage mode") if compare_with_expected_crop("Icons/Interior_heating_toggle.png") else None
            controller.click_text("My Alerts")
            if controller.is_text_present("NO MESSAGES"):
                log("Garage mode disabled after timer runs out")
            else:
                fail_log("Garage mode not disabled after timer runs out", "022", img_service)
            controller.click_by_image("Icons/back_icon.png")
            controller.swipe_down(0.05)
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "022", img_service)

# Tested
def Stolen_Vehicle_Tracking_023():
    try:
        controller.click_by_image("Icons/windows_icon.png")
        if remote_swipe("STOLEN VEHICLE TRACKING"):
            controller.click_text("STOLEN VEHICLE TRACKING")
            controller.click_text("My Alerts")
            if not controller.is_text_present("GARAGE MODE ENABLED"):
                controller.click_text("Configure")
                sleep(0.2)
                controller.click_text("Garage mode")
                controller.click_text("SYNC TO CAR")
                controller.enter_pin("1234")
                sleep(2)
                while controller.is_text_present("Sending message to car"):
                    sleep(1)
                sleep(0.2)
                controller.click_text("STOLEN VEHICLE TRACKING")
            sleep(0.2)
            controller.click_text("Garage mode") if compare_with_expected_crop("Icons/Interior_heating_toggle.png") else None
            controller.click_text("SYNC TO CAR")
            controller.enter_pin("1234")
            sleep(2)
            if controller.is_text_present("Sending message to car"):
                log("Disabled garage mode sent to car")
            else:
                fail_log("Disabled garage mode not sending to car", "023", img_service)
            while controller.is_text_present("Sending message to car"):
                sleep(1)
            sleep(0.2)
            controller.click_text("STOLEN VEHICLE TRACKING")
            controller.click_text("My Alerts")
            if controller.is_text_present("NO MESSAGES"):
                log("Garage mode successfully disabled")
            else:
                fail_log("Garage mode not disabled", "023", img_service)
            controller.click_by_image("Icons/back_icon.png")
            controller.swipe_down(0.05)
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "023", img_service)

# Tested
def Stolen_Vehicle_Tracking_024():
    try:
        controller.click_by_image("Icons/windows_icon.png")
        if remote_swipe("STOLEN VEHICLE TRACKING"):
            controller.click_text("STOLEN VEHICLE TRACKING")
            if controller.click_text("Configure"):
                log("Configure tab clicked")
            else:
                fail_log("Configure tab not found", "024", img_service)
            sleep(0.2)
            controller.click_text("Transport mode")
            controller.click_text("SYNC TO CAR")
            controller.enter_pin("1234")
            sleep(2)
            if controller.is_text_present("Sending message to car"):
                log("Transport mode sent to car")
            else:
                fail_log("Transport mode not sent to car", "024", img_service)
            while controller.is_text_present("Sending message to car"):
                sleep(1)
            sleep(0.2)

        controller.swipe_down(0.05)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "024", img_service)

# Tested
def Stolen_Vehicle_Tracking_025():
    try:
        controller.click_by_image("Icons/windows_icon.png")
        if remote_swipe("STOLEN VEHICLE TRACKING"):
            controller.click_text("STOLEN VEHICLE TRACKING")
            controller.click_text("My Alerts")
            if controller.is_text_present("TRANSPORT MODE ENABLED"):
                transport_mode = controller.d(text="TRANSPORT MODE ENABLED")
                time = transport_mode.sibling(index="1").get_text()
                log(f"Transport mode enabled ({time}) and shown in 'My Alerts' page")
            else:
                fail_log("Transport mode not displayed as enabled in 'My Alerts' page", "025", img_service)

        controller.click_by_image("Icons/back_icon.png")
        controller.swipe_down(0.05)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "025", img_service)

# Tested
def Stolen_Vehicle_Tracking_026():
    try:
        controller.click_by_image("Icons/windows_icon.png")
        if remote_swipe("STOLEN VEHICLE TRACKING"):
            controller.click_text("STOLEN VEHICLE TRACKING")
            controller.click_text("My Alerts")
            if not controller.is_text_present("TRANSPORT MODE ENABLED"):
                controller.click_text("Configure")
                sleep(0.2)
                controller.click_text("Transport mode")
                controller.click_text("SYNC TO CAR")
                controller.enter_pin("1234")
                sleep(2)
                while controller.is_text_present("Sending message to car"):
                    sleep(1)
                sleep(0.2)
                controller.click_text("STOLEN VEHICLE TRACKING")
                controller.click_text("My Alerts")
            transport_mode = controller.d(text="TRANSPORT MODE ENABLED")
            time = transport_mode.sibling(index="1").get_text()[13:18]
            now = datetime.now()
            target_time = datetime.strptime(time, "%H:%M").replace(year=now.year, month=now.month, day=now.day)
            time_diff = ((target_time - now).total_seconds())
            sleep(time_diff + 5)
            controller.click_text("Configure")
            controller.click_text("Transport mode") if compare_with_expected_crop(
                "Icons/Interior_heating_toggle.png") else None
            controller.click_text("My Alerts")
            if controller.is_text_present("NO MESSAGES"):
                log("Transport mode disabled after timer runs out")
            else:
                fail_log("Transport mode not disabled after timer runs out", "026", img_service)
            controller.click_by_image("Icons/back_icon.png")
            controller.swipe_down(0.05)
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "026", img_service)

# Tested
def Stolen_Vehicle_Tracking_027():
    try:
        controller.click_by_image("Icons/windows_icon.png")
        if remote_swipe("STOLEN VEHICLE TRACKING"):
            controller.click_text("STOLEN VEHICLE TRACKING")
            controller.click_text("My Alerts")
            if not controller.is_text_present("TRANSPORT MODE ENABLED"):
                controller.click_text("Configure")
                sleep(0.2)
                controller.click_text("Transport mode")
                controller.click_text("SYNC TO CAR")
                controller.enter_pin("1234")
                sleep(2)
                while controller.is_text_present("Sending message to car"):
                    sleep(1)
                sleep(0.2)
                controller.click_text("STOLEN VEHICLE TRACKING")
            sleep(0.2)
            controller.click_text("Transport mode") if compare_with_expected_crop(
                "Icons/Interior_heating_toggle.png") else None
            controller.click_text("SYNC TO CAR")
            controller.enter_pin("1234")
            sleep(2)
            if controller.is_text_present("Sending message to car"):
                log("Disabled transport mode sent to car")
            else:
                fail_log("Disabled transport mode not sending to car", "027", img_service)
            while controller.is_text_present("Sending message to car"):
                sleep(1)
            sleep(0.2)
            controller.click_text("STOLEN VEHICLE TRACKING")
            controller.click_text("My Alerts")
            if controller.is_text_present("NO MESSAGES"):
                log("Transport mode successfully disabled")
            else:
                fail_log("Transport mode not disabled", "027", img_service)
            controller.click_by_image("Icons/back_icon.png")
            controller.swipe_down(0.05)
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "027", img_service)

def Stolen_Vehicle_Tracking_028():
    try:
        controller.click_by_image("Icons/windows_icon.png")
        if remote_swipe("STOLEN VEHICLE TRACKING"):
            controller.click_text("STOLEN VEHICLE TRACKING")
            if controller.click_text("Configure"):
                log("Configure tab clicked")
            else:
                fail_log("Configure tab not found", "028", img_service)
            sleep(0.2)
            controller.swipe_up()
            controller.click_text("Deactivation mode")
            controller.swipe_down()
            controller.click_text("SYNC TO CAR")
            controller.enter_pin("1234")
            sleep(2)
            if controller.is_text_present("Sending message to car"):
                log("Deactivation mode sent to car")
            else:
                fail_log("Deactivation mode not sent to car", "028", img_service)
            while controller.is_text_present("Sending message to car"):
                sleep(1)
            sleep(0.2)

        controller.swipe_down(0.05)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "028", img_service)

# Tested
def Stolen_Vehicle_Tracking_029():
    try:
        controller.click_by_image("Icons/windows_icon.png")
        if remote_swipe("STOLEN VEHICLE TRACKING"):
            controller.click_text("STOLEN VEHICLE TRACKING")
            controller.click_text("My Alerts")
            if controller.is_text_present("DEACTIVATION MODE ENABLED"):
                deactivation_mode = controller.d(text="DEACTIVATION MODE ENABLED")
                time = deactivation_mode.sibling(index="1").get_text()
                log(f"Deactivation mode enabled ({time}) and shown in 'My Alerts' page")
            else:
                fail_log("Deactivation mode not displayed as enabled in 'My Alerts' page", "029", img_service)

        controller.click_by_image("Icons/back_icon.png")
        controller.swipe_down(0.05)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "029", img_service)

# Tested
def Stolen_Vehicle_Tracking_030():
    try:
        controller.click_by_image("Icons/windows_icon.png")
        if remote_swipe("STOLEN VEHICLE TRACKING"):
            controller.click_text("STOLEN VEHICLE TRACKING")
            controller.click_text("My Alerts")
            if not controller.is_text_present("DEACTIVATION MODE ENABLED"):
                controller.click_text("Configure")
                sleep(0.2)
                controller.swipe_up()
                controller.click_text("Deactivation mode")
                controller.swipe_down()
                controller.click_text("SYNC TO CAR")
                controller.enter_pin("1234")
                sleep(2)
                while controller.is_text_present("Sending message to car"):
                    sleep(1)
                sleep(0.2)
                controller.click_text("STOLEN VEHICLE TRACKING")
                controller.click_text("My Alerts")
            deactivation_mode = controller.d(text="DEACTIVATION MODE ENABLED")
            time = deactivation_mode.sibling(index="1").get_text()[13:18]
            now = datetime.now()
            target_time = datetime.strptime(time, "%H:%M").replace(year=now.year, month=now.month, day=now.day)
            time_diff = ((target_time - now).total_seconds())
            sleep(time_diff + 5)
            controller.click_text("Configure")
            controller.swipe_up()
            controller.click_text("Deactivation mode") if compare_with_expected_crop(
                "Icons/Interior_heating_toggle.png") else None
            controller.swipe_down()
            controller.click_text("My Alerts")
            if controller.is_text_present("NO MESSAGES"):
                log("Deactivation mode disabled after timer runs out")
            else:
                fail_log("Deactivation mode not disabled after timer runs out", "030", img_service)
            controller.click_by_image("Icons/back_icon.png")
            controller.swipe_down(0.05)
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "030", img_service)

# Tested
def Stolen_Vehicle_Tracking_031():
    try:
        controller.click_by_image("Icons/windows_icon.png")
        if remote_swipe("STOLEN VEHICLE TRACKING"):
            controller.click_text("STOLEN VEHICLE TRACKING")
            controller.click_text("My Alerts")
            if not controller.is_text_present("DEACTIVATION MODE ENABLED"):
                controller.click_text("Configure")
                sleep(0.2)
                controller.swipe_up()
                if not compare_with_expected_crop("Icons/Interior_heating_toggle.png"):
                    controller.click_text("Deactivation mode")
                controller.click_text("SYNC TO CAR")
                controller.enter_pin("1234")
                sleep(2)
                while controller.is_text_present("Sending message to car"):
                    sleep(1)
                sleep(0.2)
                controller.click_text("STOLEN VEHICLE TRACKING")
            sleep(0.2)
            controller.click_text("Deactivation mode") if compare_with_expected_crop(
                "Icons/Interior_heating_toggle.png") else None
            controller.swipe_down()
            controller.click_text("SYNC TO CAR")
            controller.enter_pin("1234")
            sleep(2)
            if controller.is_text_present("Sending message to car"):
                log("Disabled deactivation mode sent to car")
            else:
                fail_log("Disabled deactivation mode not sending to car", "031", img_service)
            while controller.is_text_present("Sending message to car"):
                sleep(1)
            sleep(0.2)
            controller.click_text("STOLEN VEHICLE TRACKING")
            controller.click_text("My Alerts")
            if controller.is_text_present("NO MESSAGES"):
                log("Deactivation mode successfully disabled")
            else:
                fail_log("Deactivation mode not disabled", "031", img_service)
            controller.click_by_image("Icons/back_icon.png")
            controller.swipe_down(0.05)
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "031", img_service)

# Tested
def Stolen_Vehicle_Tracking_032():
    try:
        controller.click_by_image("Icons/windows_icon.png")
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
                fail_log("Garage mode not blocked with transport mode enabled", "032", img_service)
            controller.click_text("OK")
            sleep(0.2)
            controller.click_text("Transport mode")
            controller.click_text("SYNC TO CAR")
            controller.enter_pin("1234")
            sleep(2)
            if controller.is_text_present("Sending message to car"):
                log("Transport mode disabled")
            else:
                fail_log("Transport mode not disabled", "032", img_service)
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
                fail_log("Garage mode not enabled", "032", img_service)
            while controller.is_text_present("Sending message to car"):
                sleep(1)
            sleep(0.2)
            controller.click_text("STOLEN VEHICLE TRACKING")
            controller.click_text("My Alerts")
            sleep(0.2)
            if controller.is_text_present("GARAGE MODE ENABLED"):
                log("Garage mode enabled successfully")
            else:
                fail_log("Garage mode not enabled successfully", "032", img_service)
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
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "032", img_service)

# Tested without call
def Stolen_Vehicle_Tracking_033():
    try:
        # After call completed
        controller.click_by_image("Icons/windows_icon.png")
        if remote_swipe("STOLEN VEHICLE TRACKING"):
            controller.click_text("STOLEN VEHICLE TRACKING")
            controller.click_text("My Alerts")
            if controller.is_text_present("TRANSPORT MODE ENABLED"):
                log("Transport mode enabled")
            else:
                fail_log("Transport mode not enabled", "033", img_service)

        controller.click_by_image("Icons/back_icon.png")
        controller.swipe_down(0.05)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "033", img_service)

# Tested without call
def Stolen_Vehicle_Tracking_034():
    try:
        controller.click_by_image("Icons/windows_icon.png")
        if remote_swipe("STOLEN VEHICLE TRACKING"):
            controller.click_text("STOLEN VEHICLE TRACKING")
            controller.click_text("My Alerts")
            if controller.is_text_present("NO MESSAGES"):
                controller.click_text("Configure")
                sleep(0.2)
                controller.click_text("Garage mode")
                controller.click_text("SYNC TO CAR")
                controller.enter_pin("1234")
                sleep(2)
                while controller.is_text_present("Sending message to car"):
                    sleep(1)
                sleep(0.2)
            else:
                controller.click_text("Configure")
                sleep(0.2)
                if not controller.click_by_image("Icons/Interior_heating_toggle.png"):
                    controller.swipe_up()
                    controller.click_by_image("Icons/Interior_heating_toggle.png")
                controller.click_text("SYNC TO CAR")
                controller.enter_pin("1234")
                sleep(2)
                while controller.is_text_present("Sending message to car"):
                    sleep(1)
                sleep(0.2)
                controller.click_text("STOLEN VEHICLE TRACKING")
                controller.click_text("Garage mode")
                controller.click_text("SYNC TO CAR")
                controller.enter_pin("1234")
                sleep(2)
                while controller.is_text_present("Sending message to car"):
                    sleep(1)
                sleep(0.2)
                ##############
                # Wait for call
                ##############
            controller.click_text("STOLEN VEHICLE TRACKING")
            controller.click_text("My Alerts")
            sleep(0.2)
            if controller.is_text_present("NO MESSAGES"):
                log("Special mode deactivated")
            else:
                fail_log("Special mode not deactivated", "034", img_service)

        controller.click_by_image("Icons/back_icon.png")
        controller.swipe_down(0.05)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "034", img_service)

# Continuous call, so can't be automated
def Stolen_Vehicle_Tracking_035():
    try:
        log("Can't be automated")
    except Exception as e:
        error_log(e, "035", img_service)

def Stolen_Vehicle_Tracking_036():
    try:
        log("Can't be automated")
    except Exception as e:
        error_log(e, "036", img_service)

def Stolen_Vehicle_Tracking_037():
    try:
        log("Can't be automated")
    except Exception as e:
        error_log(e, "037", img_service)

def Stolen_Vehicle_Tracking_038():
    try:
        log("Can't be automated")
    except Exception as e:
        error_log(e, "038", img_service)

def Stolen_Vehicle_Tracking_039():
    try:
        log("Can't be automated")
    except Exception as e:
        error_log(e, "039", img_service)

def Stolen_Vehicle_Tracking_040():
    try:
        log("Can't be automated")
    except Exception as e:
        error_log(e, "040", img_service)

def Stolen_Vehicle_Tracking_041():
    try:
        log("Can't be automated")
    except Exception as e:
        error_log(e, "041", img_service)

def Stolen_Vehicle_Tracking_042():
    try:
        log("Can't be automated")
    except Exception as e:
        error_log(e, "042", img_service)

def Stolen_Vehicle_Tracking_043():
    try:
        log("Can't be automated")
    except Exception as e:
        error_log(e, "043", img_service)

def Stolen_Vehicle_Tracking_044():
    try:
        log("Can't be automated")
    except Exception as e:
        error_log(e, "044", img_service)

def Stolen_Vehicle_Tracking_045():
    try:
        log("Can't be automated")
    except Exception as e:
        error_log(e, "045", img_service)

def Stolen_Vehicle_Tracking_046():
    try:
        log("Can't be automated")
    except Exception as e:
        error_log(e, "046", img_service)

def Stolen_Vehicle_Tracking_047():
    try:
        log("Can't be automated")
    except Exception as e:
        error_log(e, "047", img_service)

def Stolen_Vehicle_Tracking_048():
    try:
        log("Can't be automated")
    except Exception as e:
        error_log(e, "048", img_service)

# Tested
def Stolen_Vehicle_Tracking_049():
    try:
        controller.click_by_image("Icons/windows_icon.png")
        if remote_swipe("STOLEN VEHICLE TRACKING"):
            controller.click_text("STOLEN VEHICLE TRACKING")
            controller.click_text("My Details")
            sleep(0.2)
            controller.click_text("My Vehicle Security Tracking certificate")
            if controller.wait_for_text("CERTIFICATE"):
                log("Certificate displayed")
            else:
                fail_log("Certificate not displayed", "049", img_service)
            sleep(1)
            if compare_with_expected_crop("Icons/certificate_share_icon.png"):
                log("Certificate can be downloaded")
            else:
                fail_log("Certificate cannot be downloaded", "049", img_service)
            controller.click_by_image("Icons/back_icon.png")

        controller.click_by_image("Icons/back_icon.png")
        controller.swipe_down(0.05)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "049", img_service)

# Tested
def Stolen_Vehicle_Tracking_050():
    try:
        controller.click_by_image("Icons/windows_icon.png")
        if remote_swipe("STOLEN VEHICLE TRACKING"):
            controller.click_text("STOLEN VEHICLE TRACKING")
            controller.click_text("My Details")
            sleep(0.2)
            controller.click_by_image("Icons/phone_icon.png")
            if controller.wait_for_text("Call now"):
                log("'Call now' pop up displayed")
            else:
                fail_log("'Call now' pop up not displayed", "050", img_service)
            sleep(1)
            if controller.is_text_present("+44 333 122 2222"):
                log("Vodafone contact details displayed")
            else:
                fail_log("Vodafone contact details not displayed", "050", img_service)
            controller.click_text("Cancel")

        controller.click_by_image("Icons/back_icon.png")
        controller.swipe_down(0.05)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "050", img_service)

def Stolen_Vehicle_Tracking_051():
    try:
        controller.click_by_image("Icons/windows_icon.png")
        if remote_swipe("STOLEN VEHICLE TRACKING"):
            controller.click_text("STOLEN VEHICLE TRACKING")
            controller.click_text("My Details")
            sleep(0.2)
            controller.click_by_image("Icons/phone_icon.png")
            controller.wait_for_text("Call now")
            controller.click_text("+44 333 122 2222")
            ##########
            # After call
            ##########
            controller.launch_app("uk.co.bentley.mybentley")
            controller.click_text("Cancel")
        controller.click_by_image("Icons/back_icon.png")
        controller.swipe_down(0.05)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "051", img_service)

def Stolen_Vehicle_Tracking_052():
    try:
        log("Can't be automated")
    except Exception as e:
        error_log(e, "052", img_service)

def Stolen_Vehicle_Tracking_053():
    try:
        log("Can't be automated")
    except Exception as e:
        error_log(e, "053", img_service)

def Stolen_Vehicle_Tracking_054():
    try:
        log("Can't be automated")
    except Exception as e:
        error_log(e, "054", img_service)

# Tested
def Stolen_Vehicle_Tracking_055():
    try:
        controller.click_by_image("Icons/windows_icon.png")
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
                fail_log("My Security Language changes page when clicked", "055", img_service)
            sleep(0.2)
            btn = controller.d.xpath('//*[@text="My Security Language"]/following-sibling::android.view.View/android.widget.Button')
            if btn.exists:
                controller.click(btn.info['bounds']['left']+10, btn.info['bounds']['top']+10)

            if controller.is_text_present("Sorry, it is not possible to change this. For further information please contact Vodafone."):
                log("Correct details displayed when info button clicked")
            else:
                fail_log("Correct details not displayed when info button clicked", "055", img_service)
            controller.click_text("OK")
            controller.swipe_down()

        controller.click_by_image("Icons/back_icon.png")
        controller.swipe_down(0.05)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "055", img_service)

def Stolen_Vehicle_Tracking_056():
    try:
        controller.click_by_image("Icons/windows_icon.png")
        if remote_swipe("STOLEN VEHICLE TRACKING"):
            controller.click_text("STOLEN VEHICLE TRACKING")
            controller.click_text("My Details")
            controller.click_text("My Bentley")
            controller.click_by_image("Icons/info_btn.png",0.7)
            if controller.is_text_present("Sorry, it is not possible to change this. For further information please contact Vodafone."):
                log("Country section cannot be clicked or edited")
            else:
                fail_log("Country section not unclickable like expected", "056", img_service)
            controller.click_text("OK")
            if not compare_with_expected_crop("Icons/Homescreen_Right_Arrow.png"):
                log("Model edit arrow not displayed")
            else:
                fail_log("Model edit arrow displayed", "056", img_service)
            controller.click_by_image("Icons/back_icon.png")

        controller.click_by_image("Icons/back_icon.png")
        controller.swipe_down(0.05)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "056", img_service)

# How to have unactivated VTS
def Stolen_Vehicle_Tracking_057():
    try:
        log("temp")
    except Exception as e:
        error_log(e, "057", img_service)

# How to have unactivated VTS
def Stolen_Vehicle_Tracking_058():
    try:
        log("temp")
    except Exception as e:
        error_log(e, "058", img_service)

# How to have unactivated VTS
def Stolen_Vehicle_Tracking_059():
    try:
        log("temp")
    except Exception as e:
        error_log(e, "059", img_service)

def Stolen_Vehicle_Tracking_060():
    try:
        log("Cannot check style guide")
    except Exception as e:
        error_log(e, "060", img_service)