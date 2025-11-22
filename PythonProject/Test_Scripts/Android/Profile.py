from time import sleep
from common_utils.android_image_comparision import *
from core.log_emitter import log, fail_log, error_log, metric_log, blocked_log
from core.app_functions import app_login, app_login_setup
from core.globals import country, manual_run, current_pin

img_service = "Profile"

def Profile_001():
    try:
        if app_login_setup():
            if controller.click_by_image("Icons/Profile_Icon.png"):
                log("Tapped Profile tab")
            else:
                fail_log("Tapped Profile tab failed", "001", img_service)

            if compare_with_expected_crop("Images/Profile_Screen.png"):
                log("Profile Title is present")
            else:
                fail_log("Profile Title is not present", "001", img_service)

            if compare_with_expected_crop("Images/Profile_Screen_User_Icon.png"):
                log("Profile User Icon is present")
            else:
                fail_log("Profile User Icon is not present", "001", img_service)

            if controller.click_by_resource_id("uk.co.bentley.mybentley:id/textView_user_name_profile"):
                log("Profile User Name is present")
            else:
                fail_log("Profile User Name is not present", "001", img_service)

            if controller.is_text_present("My Details"):
                log("Profile 'My details' tab is present")
            else:
                fail_log("'My details' tab is not present", "001", img_service)

            if controller.click_text("Account"):
                log("Tapped Account")
            else:
                fail_log("Tapped Account failed", "001", img_service)

            if controller.is_text_present("Reset password"):
                log("Profile Account screen is present")
            else:
                fail_log("Profile Account screen is not present", "001", img_service)

            if controller.click_text("General"):
                log("Tapped 'General' tab")
            else:
                fail_log("'General' tab not found", "001", img_service)

            if controller.is_text_present("Vehicle connection"):
                log("Profile General screen is present")
            else:
                fail_log("Profile General screen is not present", "001", img_service)

            if compare_with_expected_crop("Images/Profile_Screen_Setting_Icon.png"):
                log("Profile Settings icon is present")
            else:
                fail_log("Profile Settings icon is not present", "001", img_service)

            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "001", img_service)

def Profile_002():
    try:
        if app_login_setup():
            if controller.click_by_image("Icons/Profile_Icon.png"):
                log("Tapped Profile tab")
            else:
                fail_log("Tapped Profile tab failed", "002", img_service)
            controller.click_text("My Details")
            controller.extract_profile_details()
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "002", img_service)

def Profile_003():
    try:
        if app_login_setup():
            controller.click_by_image("Icons/Profile_Icon.png")
            controller.click_by_image("Icons/Profile_Account_Icon.png")
            controller.click_text("Reset password")
            controller.click_by_image("Icons/Reset_Password.png")
            if controller.wait_for_text_and_click("CONFIRMED"):
                log("Reset password email sent")
            else:
                fail_log("Error: Reset password email failed", "003", img_service)

            controller.click_by_image("Icons/back_icon.png")
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "003", img_service)

def Profile_004():
    try:
        if app_login_setup():
            controller.click_by_image("Icons/Profile_Icon.png")
            controller.click_text("Account")

            controller.click_text("PIN")

            controller.click_text("Change PIN")
            controller.click_text("Old PIN")
            controller.enter_pin(current_pin)
            controller.click_text("New PIN")
            controller.enter_pin(current_pin)
            controller.click_text("Enter new PIN again")
            controller.enter_pin(current_pin)
            controller.click_text("CHANGE PIN")

            if controller.wait_for_text("PIN has been changed"):
                log("PIN changed")
            else:
                if controller.click_text("Cancel"):
                    fail_log("Connection failed", "004", img_service)
                log("PIN not changed")
            sleep(5)
            controller.click_by_image("Icons/back_icon.png")
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "004", img_service)

# THINK THIS BRAKES THE APP FOR NOW, will finish when it stops destroying everything
def Profile_005():
    try:
        blocked_log("Test blocked - App killer")
        # if app_login_setup():
        #     controller.click_by_image("Icons/Profile_Icon.png")
        #     controller.click_by_image("Icons/Profile_Account_Icon.png")
        #     controller.click_text("PIN")
        #
        #     controller.click_text("Forgotten your PIN?")
        #
        #     controller.click_text("New PIN")
        #     controller.enter_pin("1234")
        #     controller.click_text("Enter new PIN again")
        #     controller.enter_pin("1234")
        #
        #     controller.click_text("RESET PIN")
        #     controller.click_text("Confirm")

    except Exception as e:
        error_log(e, "005", img_service)

def Profile_006():
    try:
        if app_login_setup():
            controller.click_by_image("Icons/Profile_Icon.png")
            controller.click_text("Account")
            if controller.click_text("Bentley ID Terms of Use"):
                log("Bentley ID Terms of Use tab clicked")
            else:
                fail_log("Bentley ID Terms of Use tab not displayed", "006", img_service)

            if controller.is_text_present("BENTLEY ID TERMS OF USE"):
                log("Bentley ID Terms of Use page displayed")
            else:
                fail_log("Bentley ID Terms of Use page not displayed", "006", img_service)
                controller.click_by_image("Icons/Error_Icon.png")
            controller.click_by_image("Icons/back_icon.png")
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "006", img_service)

def Profile_007():
    try:
        if app_login_setup():
            controller.click_by_image("Icons/Profile_Icon.png")
            controller.click_text("Account")
            if controller.click_text("My Bentley Terms of Use"):
                log("My Bentley Terms of Use tab clicked")
            else:
                fail_log("My Bentley Terms of Use tab not displayed", "007", img_service)

            if controller.is_text_present("MY BENTLEY TERMS OF USE"):
                log("My Bentley Terms of Use page displayed")
            else:
                fail_log("My Bentley Terms of Use page not displayed", "007", img_service)
                controller.click_by_image("Icons/Error_Icon.png")
            controller.click_by_image("Icons/back_icon.png")
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "007", img_service)

def Profile_008():
    try:
        if app_login_setup():
            controller.click_by_image("Icons/Profile_Icon.png")
            controller.click_text("Account")
            controller.swipe_up()
            if controller.click_text("Terms and Conditions"):
                log("Terms and Conditions tab clicked")
            else:
                fail_log("Terms and Conditions tab not displayed", "008", img_service)

            if controller.is_text_present("TERMS AND CONDITIONS"):
                log("Terms and Conditions page displayed")
            else:
                fail_log("Terms and Conditions page not displayed", "008", img_service)
                controller.click_by_image("Icons/Error_Icon.png")
            controller.click_by_image("Icons/back_icon.png")
            controller.settings_swipe_down()
            controller.settings_swipe_down()
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "008", img_service)

def Profile_009():
    try:
        if app_login_setup():
            controller.click_by_image("Icons/Profile_Icon.png")
            controller.click_text("Account")
            controller.swipe_up()
            if controller.click_text("Bentley ID Privacy Policy"):
                log("Bentley ID Privacy Policy tab clicked")
            else:
                fail_log("Bentley ID Privacy Policy tab not displayed", "009", img_service)

            if controller.is_text_present("BENTLEY ID PRIVACY POLICY"):
                log("Bentley ID privacy policy page displayed")
            else:
                fail_log("Bentley ID privacy policy page not displayed", "009", img_service)
                controller.click_by_image("Icons/Error_Icon.png")
            controller.click_by_image("Icons/back_icon.png")
            controller.settings_swipe_down()
            controller.settings_swipe_down()
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "009", img_service)

def Profile_010():
    try:
        if app_login_setup():
            controller.click_by_image("Icons/Profile_Icon.png")
            controller.click_text("Account")
            controller.swipe_up()
            if controller.click_text("My Bentley Privacy Policy"):
                log("My Bentley Privacy Policy tab clicked")
            else:
                fail_log("My Bentley Privacy Policy tab not displayed", "010", img_service)

            if controller.is_text_present("MY BENTLEY PRIVACY POLICY"):
                log("My bentley privacy policy page displayed")
            else:
                fail_log("My bentley privacy policy page not displayed", "010", img_service)
                controller.click_by_image("Icons/Error_Icon.png")
            controller.click_by_image("Icons/back_icon.png")
            controller.settings_swipe_down()
            controller.settings_swipe_down()
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "010", img_service)

def Profile_011():
    try:
        if app_login_setup():
            if country == "eur":
                controller.click_by_image("Icons/Profile_Icon.png")
                controller.click_text("Account")
                controller.swipe_up()
                if controller.click_text("Vehicle Tracking Terms and Conditions"):
                    log("Vehicle tracking terms and conditions tab clicked")
                else:
                    fail_log("Vehicle tracking terms and conditions tab not displayed", "011", img_service)

                # Getting an error
                if controller.is_text_present("Whatever pops up when successful"):
                    log("Vehicle tracking terms and conditions page displayed")
                else:
                    fail_log("Failed to display Vehicle tracking terms and conditions", "011", img_service)
                    controller.click_by_image("Icons/Error_Icon.png")
                controller.click_by_image("Icons/back_icon.png")
                controller.settings_swipe_down()
                controller.settings_swipe_down()
                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            else:
                blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "011", img_service)

def Profile_012():
    try:
        if app_login_setup():
            controller.click_by_image("Icons/Profile_Icon.png")
            controller.click_text("Account")
            controller.swipe_up()
            if controller.click_text("Copyright"):
                log("Copyright tab clicked")
            else:
                fail_log("Copyright tab not displayed", "012", img_service)

            if controller.is_text_present("COPYRIGHT"):
                log("Copyright page displayed")
            else:
                fail_log("Copyright page not displayed", "012", img_service)
            controller.click_by_image("Icons/back_icon.png")
            controller.settings_swipe_down()
            controller.settings_swipe_down()
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "012", img_service)

def Profile_013():
    try:
        if app_login_setup():
            controller.click_by_image("Icons/Profile_Icon.png")
            controller.click_text("General")
            if controller.click_text("Vehicle connection"):
                log("Vehicle connection tab clicked")
            else:
                fail_log("Vehicle connection tab not displayed", "013", img_service)

            screen_text = ['Wi-Fi', 'Bluetooth', 'Internet', 'My Bentley app', 'BMS']
            display = True
            for text in screen_text:
                if not controller.is_text_present(text):
                    display = False
                    fail_log(f"Text not found: {text}", "013", img_service)
            if display:
                log("Vehicle connection screen displayed correctly")
            else:
                fail_log("Vehicle connection screen displayed incorrectly", "013", img_service)
            controller.click_by_image("Icons/back_icon.png")
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "013", img_service)

#IOS only
def Profile_014():
    try:
        blocked_log("Test blocked - iOS only test")
    except Exception as e:
        error_log(e, "014", img_service)

def Profile_015():
    try:
        if app_login_setup():
            controller.click_by_image("Icons/Profile_Icon.png")
            controller.click_text("General")
            if controller.click_text("Contact"):
                log("Contact clicked")
            else:
                fail_log("Contact tab not displayed", "015", img_service)

            if controller.click_text("My Bentley") and controller.is_text_present("contactbentley@contact.bentleymotors.com") and controller.is_text_present("+44 (0) 1270 444 474"):
                log("My Bentley support contact details displayed")
            else:
                fail_log("My Bentley support contact details not displayed", "015", img_service)

            if controller.click_text("General") and controller.is_text_present("+44 (0) 1270 653 653"):
                log("Bentley Motors contact details displayed")
            else:
                fail_log("Bentley motors contact details not displayed", "015", img_service)
            controller.click_by_image("Icons/back_icon.png")
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "015", img_service)

def Profile_016():
    try:
        if app_login_setup():
            controller.click_by_image("Icons/Profile_Icon.png")
            controller.click_by_image("Icons/Profile_Screen_Setting_Icon.png")
            if controller.click_text("Units") and controller.is_text_present("UNITS"):
                log("Units section is displayed and page opened")
            else:
                fail_log("Units section not displayed and page opened", "016", img_service)

            if (controller.click_text("Miles") and compare_with_expected_crop("Icons/Miles_selected.png")) and (controller.click_text("Kilometres") and compare_with_expected_crop("Icons/Kilometres_selected.png")):
                log("Units displayed and able to be selected and deselected")
            else:
                fail_log("Units section not displayed or selectable", "016", img_service)

            if (controller.click_text("km/kWh") and compare_with_expected_crop("Icons/kmkwh_selected.png")) and (controller.click_text("kWh/100km") and compare_with_expected_crop("Icons/kwh100km_selected.png")):
                log("Electric consumption units displayed and able to be selected and deselected")
            else:
                fail_log("Electric consumption units section not displayed or selectable", "016", img_service)

            if (controller.click_text("km/l") and compare_with_expected_crop("Icons/kml_selected.png")) and (controller.click_text("l/100km") and compare_with_expected_crop("Icons/l100km_selected.png")):
                log("Consumption units displayed and able to be selected and deselected")
            else:
                fail_log("Consumption units section not displayed or selectable", "016", img_service)

            if (controller.click_text("psi") and compare_with_expected_crop("Icons/psi_selected.png")) and (controller.click_text("kPa") and compare_with_expected_crop("Icons/kpa_selected.png")) and (controller.click_text("bar") and compare_with_expected_crop("Icons/bar_selected.png")):
                log("Pressure units displayed and able to be selected and deselected")
            else:
                fail_log("Pressure units section not displayed or selectable", "016", img_service)

            if (controller.click_text("Fahrenheit") and compare_with_expected_crop("Icons/fahrenheit_selected.png")) and (controller.click_text("Celsius") and compare_with_expected_crop("Icons/celsius_selected.png")):
                log("Temperature units displayed and able to be selected and deselected")
            else:
                fail_log("Temperature units not displayed or selectable", "016", img_service)
            controller.click_by_image("Icons/back_icon.png")
            controller.click_by_image("Icons/back_icon.png")
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "016", img_service)

def Profile_017():
    try:
        if app_login_setup():
            controller.click_by_image("Icons/Profile_Icon.png")
            controller.click_by_image("Icons/Profile_Screen_Setting_Icon.png")
            if controller.click_text("Permissions"):
                log("Permissions section is displayed")
            else:
                fail_log("Permissions section not displayed", "017", img_service)

            if controller.is_text_present("Permissions") and controller.click_text("Location"):
                log("Permissions page is displayed and statuses is listed")
            else:
                fail_log("Permissions page not displayed", "017", img_service)
            controller.click_by_image("Icons/back_icon.png")
            controller.click_by_image("Icons/back_icon.png")
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "017", img_service)

def Profile_018():
    try:
        if app_login_setup():
            controller.click_by_image("Icons/Profile_Icon.png")
            controller.click_by_image("Icons/Profile_Screen_Setting_Icon.png")

            if controller.is_text_present("Last mile notification"):
                log("Last mile notification section is displayed")
            else:
                fail_log("Last mile notification section not displayed", "006", img_service)

            if controller.click_by_image("Icons/Interior_heating_toggle.png"):
                sleep(0.2)
                if controller.click_by_image("Icons/timer_toggle_off.png"):
                    log("Last mile notification can be disabled/enabled")
                else:
                    fail_log("Last mile notification cannot be disabled/enabled", "006", img_service)
            elif controller.click_by_image("Icons/timer_toggle_off.png"):
                sleep(0.2)
                if controller.click_by_image("Icons/Interior_heating_toggle.png"):
                    log("Last mile notification can be disabled/enabled")
                else:
                    fail_log("Last mile notification cannot be disabled/enabled", "006", img_service)
            controller.click_by_image("Icons/back_icon.png")
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "018", img_service)

def Profile_019():
    try:
        blocked_log("Test blocked - Can't check style guide")
    except Exception as e:
        error_log(e, "019", img_service)

def Profile_020():
    try:
        if app_login_setup():
            controller.click_by_image("Icons/Profile_Icon.png")
            controller.click_text("Log out")
            if controller.click_text("Log out"):
                log("Log out process started")
            else:
                fail_log("Could not find log out button", "020", img_service)

            if controller.wait_for_text("LOGIN OR REGISTER"):
                log("Successfully logged out")
            else:
                fail_log("Log out process failed", "020", img_service)

            # End the test case back logged in
            app_login()
    except Exception as e:
        error_log(e, "020", img_service)