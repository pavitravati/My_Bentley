from time import sleep
from common_utils.android_image_comparision import *
from common_utils.android_controller import *
from core.log_emitter import log, fail_log, error_log, metric_log

img_service = "Profile"

def Profile_001():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        # 1) Open Profile tab
        if controller.click_by_image("Icons/Profile_Icon.png", threshold=0.80):
            log("Tapped Profile tab")
        else:
            fail_log("Tapped Profile tab failed", "001", img_service)
        time.sleep(2)

        # 2) Validate Profile screen header/title
        if compare_with_expected_crop("Images/Profile_Screen.png"):
            log("Profile Title is present")
        else:
            fail_log("Profile Title is not present", "001", img_service)

        # 3) Validate user icon
        if compare_with_expected_crop("Images/Profile_Screen_User_Icon.png"):
            log("Profile User Icon is present")
        else:
            fail_log("Profile User Icon is not present", "001", img_service)

        # 4) Validate user name
        if compare_with_expected_crop("Images/Profile_Screen_User_Name.png"):
            log("Profile User Name is present")
        else:
            fail_log("Profile User Name is not present", "001", img_service)

        # 5) Validate 'My details' tab
        if compare_with_expected_crop("Images/Profile_Screen_MyDetails_Tab.png"):
            log("Profile 'My details' tab is present")
        else:
            fail_log("Profile 'My details' tab is not present", "001", img_service)

        # 6) Navigate to Account
        if controller.click_by_image("Icons/Profile_Account_Icon.png", threshold=0.80):
            log("Tapped Account")
        else:
            fail_log("Tapped Account failed", "001", img_service)
        time.sleep(2)

        if compare_with_expected_crop("Images/Profile_Account_Screen.png"):
            log("Profile Account screen is present")
        else:
            fail_log("Profile Account screen is not present", "001", img_service)

        # 7) Navigate to General
        if controller.click_by_image("Icons/Profile_General_Icon.png", threshold=0.80):
            log("Tapped General")
        else:
            fail_log("Tapped General failed", "001", img_service)
        time.sleep(2)

        if compare_with_expected_crop("Images/Profile_General_Screen.png"):
            log("Profile General screen is present")
        else:
            fail_log("Profile General screen is not present", "001", img_service)

        # 8) Settings icon visible
        if compare_with_expected_crop("Images/Profile_Screen_Setting_Icon.png"):
            log("Profile Settings icon is present")
        else:
            fail_log("Profile Settings icon is not present", "001", img_service)

        # Navigate back to My details tab & dashboard
        controller.click_by_image("Icons/Profile_Mydetails_Icon.png", threshold=0.80)
        time.sleep(2)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        time.sleep(2)

    except Exception as e:
        error_log(e, "001", img_service)

def Profile_002():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        if controller.click_by_image("Icons/Profile_Icon.png", threshold=0.80):
            log("Tapped Profile tab")
        else:
            fail_log("Tapped Profile tab failed", "002", img_service)
        time.sleep(2)
        controller.extract_profile_details()
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "002", img_service)

def Profile_003():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/Profile_Icon.png")

        controller.click_by_image("Icons/Profile_Account_Icon.png")
        sleep(2)
        controller.click_text("Reset password")
        sleep(2)
        controller.click_by_image("Icons/Reset_Password.png")
        sleep(2)
        if compare_with_expected_crop("Images/Email_Confirmation.png"):
            log("Reset password email sent")
        else:
            fail_log("Error: Reset password email failed", "003", img_service)

        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "003", img_service)

# some of the text in this test case is not the same as my app version
# need resource id of back button
def Profile_004():
    current_pin = "1234"
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/Profile_Icon.png")
        controller.click_by_image("Icons/Profile_Account_Icon.png")

        controller.click_text("PIN")
        sleep(2)

        controller.click_text("Change PIN")
        sleep(2)
        controller.click_text("Old PIN")
        sleep(2)
        controller.enter_pin(current_pin)
        sleep(2)
        controller.click_text("New PIN")
        sleep(2)
        controller.enter_pin(current_pin)
        controller.click_text("Enter new PIN again")
        sleep(2)
        controller.enter_pin(current_pin)
        sleep(2)
        controller.click_text("CHANGE PIN")

        sleep(1)
        if compare_with_expected_crop("Images/PIN_Confirmation.png"):
            log("PIN changed")
        else:
            sleep(2)
            if controller.click_text("Cancel"):
                fail_log("Connection failed", "004", img_service)
            log("PIN not changed")
            sleep(3)
            controller.click(110,110) # find out the resource id for the back button and replace with that
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "004", img_service)

# THINK THIS BRAKES THE APP FOR NOW, will finish when it stops destroying everything
# def Profile_005():
#     try:
#         controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
#         controller.click_by_image("Icons/Profile_Icon.png")
#         controller.click_by_image("Icons/Profile_Account_Icon.png")
#         controller.click_text("PIN")
#
#         controller.click_text("Forgotten your PIN?")
#         sleep(2)
#
#         controller.click_text("New PIN")
#         sleep(2)
#         controller.enter_pin("1234")
#         sleep(2)
#         controller.click_text("Enter new PIN again")
#         sleep(2)
#         controller.enter_pin("1234")
#         sleep(2)
#
#         controller.click_text("RESET PIN")
#         sleep(2)
#         controller.click_text("Confirm")
#         # need to be in vehicle to finish, so I can reset primary user
#
#     except Exception as e:
#         error_log(e, "005", img_service)

def Profile_006():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        # 1) Open Profile tab
        if controller.click_by_image("Icons/Profile_Icon.png", threshold=0.80):
            log("Tapped Profile tab")
        else:
            fail_log("Tapped Profile tab failed", "006", img_service)
        time.sleep(2)

        if controller.click_by_image("Icons/Profile_Account_Icon.png", threshold=0.80):
            log("Tapped Account")
        else:
            fail_log("Tapped Account failed", "006", img_service)
        time.sleep(2)

        controller.click_text("Bentley ID Terms of Use")
        if compare_with_expected_crop("Images/Bentley_Terms_Usage.png"):
            log("Terms and Usage screen is present")
        else:
            fail_log("Terms and Usage screen is not present", "006", img_service)

        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "006", img_service)

def Profile_007():
    try:
        pass
    except Exception as e:
        error_log(e, "007", img_service)

def Profile_007():
    try:
        pass
    except Exception as e:
        error_log(e, "007", img_service)

def Profile_008():
    try:
        pass
    except Exception as e:
        error_log(e, "008", img_service)

def Profile_009():
    try:
        pass
    except Exception as e:
        error_log(e, "009", img_service)

def Profile_010():
    try:
        pass
    except Exception as e:
        error_log(e, "010", img_service)

def Profile_011():
    try:
        pass
    except Exception as e:
        error_log(e, "011", img_service)

def Profile_012():
    try:
        pass
    except Exception as e:
        error_log(e, "012", img_service)

def Profile_013():
    try:
        pass
    except Exception as e:
        error_log(e, "013", img_service)

def Profile_014():
    try:
        pass
    except Exception as e:
        error_log(e, "014", img_service)

def Profile_015():
    try:
        pass
    except Exception as e:
        error_log(e, "015", img_service)

def Profile_016():
    try:
        pass
    except Exception as e:
        error_log(e, "016", img_service)

def Profile_017():
    try:
        pass
    except Exception as e:
        error_log(e, "017", img_service)

def Profile_018():
    try:
        pass
    except Exception as e:
        error_log(e, "018", img_service)

def Profile_019():
    try:
        pass
    except Exception as e:
        error_log(e, "019", img_service)

def Profile_020():
    try:
        pass
    except Exception as e:
        error_log(e, "020", img_service)