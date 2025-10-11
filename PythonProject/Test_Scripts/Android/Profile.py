from time import sleep
from common_utils.android_image_comparision import *
from common_utils.android_controller import *
from core.log_emitter import log_emitter

def log(msg):
    log_emitter.log_signal.emit(msg)

def fail_log(msg, num):
    log(f"{msg}")
    controller.take_fail_screenshot(f"Profile_{msg}_{num}.png")

def error_log(e, num):
    log(f"⚠️ - Unexpected error: {e}")
    controller.take_fail_screenshot(f"Profile_{e}_{num}.png")

def Profiles_001():
    test_passed = True  # ✅ Initialize test flag
    try:
        # 1) Open Profile tab
        if controller.click_by_image("Icons/Profile_Icon.png", threshold=0.80):
            log("✅ - Tapped Profile tab")
        else:
            fail_log("❌ - Tapped Profile tab failed")
            test_passed = False
        time.sleep(2)

        # 2) Validate Profile screen header/title
        if compare_with_expected_crop("Images/Profile_Screen.png"):
            log("✅ - Profile Title is present")
        else:
            fail_log("❌ - Profile Title is not present", "001")
            test_passed = False

        # 3) Validate user icon
        if compare_with_expected_crop("Images/Profile_Screen_User_Icon.png"):
            log("✅ - Profile User Icon is present")
        else:
            fail_log("❌ - Profile User Icon is not present", "001")
            test_passed = False

        # 4) Validate user name
        if compare_with_expected_crop("Images/Profile_Screen_User_Name.png"):
            log("✅ - Profile User Name is present")
        else:
            fail_log("❌ - Profile User Name is not present", "001")
            test_passed = False

        # 5) Validate 'My details' tab
        if compare_with_expected_crop("Images/Profile_Screen_MyDetails_Tab.png"):
            log("✅ - Profile 'My details' tab is present")
        else:
            fail_log("❌ - Profile 'My details' tab is not present", "001")
            test_passed = False

        # 6) Navigate to Account
        if controller.click_by_image("Icons/Profile_Account_Icon.png", threshold=0.80):
            log("✅ - Tapped Account")
        else:
            fail_log("❌ - Tapped Account failed", "001")
            test_passed = False
        time.sleep(2)

        if compare_with_expected_crop("Images/Profile_Account_Screen.png"):
            log("✅ - Profile Account screen is present")
        else:
            fail_log("❌ - Profile Account screen is not present", "001")
            test_passed = False

        # 7) Navigate to General
        if controller.click_by_image("Icons/Profile_General_Icon.png", threshold=0.80):
            log("✅ - Tapped General")
        else:
            fail_log("❌ - Tapped General failed", "001")
            test_passed = False
        time.sleep(2)

        if compare_with_expected_crop("Images/Profile_General_Screen.png"):
            log("✅ - Profile General screen is present")
        else:
            fail_log("❌ - Profile General screen is not present", "001")
            test_passed = False

        # 8) Settings icon visible
        if compare_with_expected_crop("Images/Profile_Screen_Setting_Icon.png"):
            log("✅ - Profile Settings icon is present")
        else:
            fail_log("❌ - Profile Settings icon is not present", "001")
            test_passed = False

        # Final status
        if test_passed:
            log("✅ - Profiles_001 passed")
        else:
            fail_log("❌ - Profiles_001 failed", "001")

        # Navigate back to My details tab & dashboard
        controller.click_by_image("Icons/Profile_Mydetails_Icon.png", threshold=0.80)
        time.sleep(2)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        time.sleep(2)

    except Exception as e:
        error_log(e, "001")

def Profiles_002():
    try:
        if controller.click_by_image("Icons/Profile_Icon.png", threshold=0.80):
            log("✅ - Tapped Profile tab")
        else:
            fail_log("❌ - Tapped Profile tab failed", "002")
        time.sleep(2)

        controller.extract_profile_details()

    except Exception as e:
        error_log(e, "002")

def Profiles_003():
    try:
        controller.click_by_image("Icons/Profile_Account_Icon.png")
        sleep(2)
        controller.click_text("Reset password")
        sleep(2)
        controller.click_by_image("Icons/Reset_Password.png")
        sleep(2)
        if compare_with_expected_crop("Images/Email_Confirmation.png"):
            log("✅ - Reset password email sent")
            log("✅ - Profiles_003 passed")
        else:
            fail_log("❌ - Error: Reset password email failed", "003")
            log("❌ - Profiles_003 failed")

    except Exception as e:
        error_log(e, "002")

# some of the text in this test case is not the same as my app version
# need resource id of back button
def Profiles_004():
    current_pin = "0000"
    try:
        if compare_with_expected_crop("Icons/email_reset_x.png"):
            controller.click_by_image("Icons/email_reset_x.png")
            sleep(2)
            controller.click_by_image("Icons/back_icon.png")
            sleep(2)
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
        controller.enter_pin("1234")
        controller.click_text("Enter new PIN again")
        sleep(2)
        controller.enter_pin("1234")
        sleep(2)
        controller.click_text("CHANGE PIN")

        sleep(1)
        if compare_with_expected_crop("Images/PIN_Confirmation.png"):
            log("✅ - PIN changed")
            log("✅ - Profiles_004 passed")
        else:
            sleep(2)
            if controller.click_text("Cancel"):
                fail_log("❌ - Connection failed", "004")
            log("❌ - PIN not changed")
            log("❌ - Profiles_003 failed")
            sleep(1)
            controller.click(110,110) # find out the resource id for the back button and replace with that

    except Exception as e:
        error_log(e, "004")

def Profiles_005():
    try:
        controller.click_text("Forgotten your PIN?")
        sleep(2)

        controller.click_text("New PIN")
        sleep(2)
        controller.enter_pin("1234")
        sleep(2)
        controller.click_text("Enter new PIN again")
        sleep(2)
        controller.enter_pin("1234")
        sleep(2)

        controller.click_text("RESET PIN")
        sleep(2)
        controller.click_text("Confirm")
        # need to be in vehicle to finish, so I can reset primary user

    except Exception as e:
        error_log(e, "005")

def Profile_006():
    test_passed = True  # ✅ Initialize test flag
    try:
        # 1) Open Profile tab
        if controller.click_by_image("Icons/Profile_Icon.png", threshold=0.80):
            log("✅ - Tapped Profile tab")
        else:
            fail_log("❌ - Tapped Profile tab failed", "006")
            test_passed = False
        time.sleep(2)

        if controller.click_by_image("Icons/Profile_Account_Icon.png", threshold=0.80):
            log("✅ - Tapped Account")
        else:
            fail_log("❌ - Tapped Account failed", "006")
            test_passed = False
        time.sleep(2)

        controller.click_text("Bentley ID Terms of Use")
        if compare_with_expected_crop("Images/Bentley_Terms_Usage.png"):
            log("✅ - Terms and Usage screen is present")
        else:
            fail_log("❌ - Terms and Usage screen is not present", "006")
            test_passed = False

    except Exception as e:
        error_log(e, "006")