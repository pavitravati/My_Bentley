from time import sleep
from PythonProject.common_utils.ios_image_comparision import *
from PythonProject.common_utils.test_result_tracker import TestCaseResult
from PythonProject.common_utils.test_result_tracker import TestCaseResult


# iOS session details
ios = IOSController(
    mac_ip="192.168.1.5",
    port=8101,
    udid="00008130-0012513918A1401C",
    team_id="LDD46J9733",
    bundle_id="uk.co.bentley.MyBentley"
)

# Start single session
ios.start_session()
# ---------------------------
# Demo Mode Test Cases (iOS)
# ---------------------------

def Profiles_001():
    test_result = TestCaseResult("Profiles_001")
    test_result.description = "Accessing Profile screen via My Bentley App"
    test_result.start_time = time.time()

    test_passed = True  # ✅ Initialize test flag

    try:
        # 1) Open Profile tab
        ok = ios.click_by_image("ios_Icons/ios_Profile_Icon.png", threshold=0.80)
        test_result.log_step("Tapped Profile tab", ok)
        test_passed &= ok
        time.sleep(2)

        # 2) Validate Profile screen header/title
        ok = compare_with_expected_crop_ios(ios, "ios_Images/ios_Profile_Screen.png")
        test_result.log_step("Profile Title is present", ok)
        test_passed &= ok

        # 3) Validate user icon
        ok = compare_with_expected_crop_ios(ios, "ios_Images/ios_Profile_Screen_User_Icon.png")
        test_result.log_step("Profile User Icon is present", ok)
        test_passed &= ok

        # 4) Validate user name
        ok = compare_with_expected_crop_ios(ios, "ios_Images/ios_Profile_Screen_User_Name.png")
        test_result.log_step("Profile User Name is present", ok)
        test_passed &= ok

        # 5) Validate 'My details' tab
        ok = compare_with_expected_crop_ios(ios, "ios_Images/ios_Profile_Screen_MyDetails_Tab.png")
        test_result.log_step("Profile 'My details' tab is present", ok)
        test_passed &= ok

        # 6) Navigate to Account
        ok = ios.click_by_image("ios_Icons/ios_Profile_Account_Icon.png", threshold=0.80)
        test_result.log_step("Tapped Account", ok)
        test_passed &= ok
        time.sleep(2)

        ok = compare_with_expected_crop_ios(ios, "ios_Images/ios_Profile_Account_Screen.png")
        test_result.log_step("Profile Account screen is present", ok)
        test_passed &= ok

        # 7) Navigate to General
        ok = ios.click_by_image("ios_Icons/ios_Profile_General_Icon.png", threshold=0.80)
        test_result.log_step("Tapped General", ok)
        test_passed &= ok
        time.sleep(2)

        ok = compare_with_expected_crop_ios(ios, "ios_Images/ios_Profile_General_Screen.png")
        test_result.log_step("Profile General screen is present", ok)
        test_passed &= ok

        # 8) Settings icon visible
        ok = compare_with_expected_crop_ios(ios, "ios_Images/ios_Profile_Screen_Setting_Icon.png")
        test_result.log_step("Profile Settings icon is present", ok)
        test_passed &= ok

        # ✅ Final test result
        if test_passed:
            test_result.log("✅ Profiles_001 passed")
            test_result.status = "Passed"
        else:
            test_result.log("❌ Profiles_001 failed")
            test_result.status = "Failed"

    except Exception as e:
        # ❗ Log full traceback for better debugging
        test_result.log_step(f"Unexpected error: {traceback.format_exc()}", False)
        test_result.status = "Error"

    finally:
        # Always navigate back to dashboard
        try:
            ios.click_by_image("ios_Icons/ios_Profile_Mydetails_Icon.png", threshold=0.80)
            time.sleep(2)
            ios.click_by_image("ios_Icons/ios_Home.png", threshold=0.80)
            time.sleep(2)
        except Exception as e:
            test_result.log_step(f"Navigation back failed: {e}", False)

        test_result.end_time = time.time()

    return test_result

def Profiles_002():
    test_result = TestCaseResult("Profiles_002")
    test_result.description = "Verify My Details in Profile screen"
    test_result.start_time = time.time()
    test_passed = True  # ✅ Initialize test flag
    try:
        ok = controller.click_by_image("Icons/Profile_Icon.png", threshold=0.80)
        test_result.log_step("Tapped Profile tab", ok)
        test_passed &= ok
        time.sleep(2)

        controller.extract_profile_details()

    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)
        test_result.status = "Error"

    test_result.end_time = time.time()
    return test_result

######################################################################
# Have not finished my ones for this as these are the ones that disconect and break the app

def Profiles_003():
    test_result = TestCaseResult("Profiles_003")
    test_result.description = ("Verify Password Resetting")
    test_result.start_time = time.time()

    try:
        controller.click_by_image("Icons/Profile_Account_Icon.png")
        sleep(2)

        controller.click_text("Reset password")
        sleep(2)
        controller.click_by_image("Icons/Reset_Password.png")
        sleep(2)
        if compare_with_expected_crop("Images/Email_Confirmation.png"):
            test_result.log_step("Reset password email sent", True)
            test_result.log("✅ Profiles_003 passed")
        else:
            test_result.log_step("Error: Reset password email failed", False)
            test_result.log("❌ Profiles_003 failed")
            test_result.status = "Failed"

    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)
        test_result.status = "Error"

    test_result.end_time = time.time()
    return test_result

# some of the text in this test case is not the same as my app version
# need resource id of back button
def Profiles_004():
    test_result = TestCaseResult("Profiles_004")
    test_result.description = ("Verify Changing the PIN")
    test_result.start_time = time.time()
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
            test_result.log_step("PIN changed", True)
            test_result.log("✅ Profiles_004 passed")
        else:
            sleep(2)
            ok = controller.click_text("Cancel")
            if ok:
                test_result.log_step("Connection failed", False)
            test_result.log_step("PIN not changed", False)
            test_result.log("❌ Profiles_003 failed")
            test_result.status = "Failed"
            sleep(1)
            controller.click(110,110) # find out the resource id for the back button and replace with that

    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)
        test_result.status = "Error"

    test_result.end_time = time.time()
    return test_result

# Removes the car from app so need someone who can add back quickly to finish this one
def Profiles_005():
    test_result = TestCaseResult("Profiles_005")
    test_result.description = ("Verify Changing the PIN")
    test_result.start_time = time.time()

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
        test_result.log_step(f"Unexpected error: {e}", False)
        test_result.status = "Error"

####################################################################################

def Profile_006():
    test_result = TestCaseResult("Profiles_002")
    test_result.description = "Verify My Details in Profile screen"
    test_result.start_time = time.time()
    test_passed = True  # ✅ Initialize test flag

    try:
        # 1) Open Profile tab
        ok = controller.click_by_image("Icons/Profile_Icon.png", threshold=0.80)
        test_result.log_step("Tapped Profile tab", ok)
        test_passed &= ok
        time.sleep(2)

        ok = controller.click_by_image("Icons/Profile_Account_Icon.png", threshold=0.80)
        test_result.log_step("Tapped Account", ok)
        test_passed &= ok
        time.sleep(2)

        controller.click_text("Bentley ID Terms of Use")
        ok = compare_with_expected_crop("Images/Bentley_Terms_Usage.png")
        test_result.log_step("Terms and Usage screen is present", ok)
        test_passed &= ok



    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)
        test_result.status = "Error"

    test_result.end_time = time.time()
    return test_result

def dummy():
    ios.take_screenshot("temp.png")

Profiles_001()
