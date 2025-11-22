from time import sleep
from PythonProject.common_utils.ios_image_comparision import *
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

def Demo_Mode_001(ios):
    test_result = TestCaseResult("Demo_Mode_001")
    test_result.description = "Accessing Demo mode"
    test_result.start_time = time.time()
    try:
        if  find_icon_in_screen_ios(ios, "ios_Images/ios_My_Bentley_Login_Page.png"):
            ios.click_by_text("DISCOVER MY BENTLEY")
            sleep(5)
        else:
            ios.click_by_image("ios_Icons/ios_Logout_Icon.png")
            sleep(5)
            ios.click_by_text("DISCOVER MY BENTLEY")
            sleep(5)

        if find_icon_in_screen_ios(ios,"ios_Images/ios_My_Bentley_Demo_Mode_Page.png"):
            test_result.log_step("Demo_Mode_001 passed", True)
        else:
            test_result.log_step("Dashboard screen not detected, Demo_Mode_001 Failed", False)

    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)

    test_result.end_time = time.time()
    return test_result

def Demo_Mode_002(ios):
    test_result = TestCaseResult("Demo_Mode_002")
    test_result.description = "Verify Demo Mode content"
    test_result.start_time = time.time()
    try:
        if find_icon_in_screen_ios(ios, "ios_Images/ios_My_Bentley_Login_Page.png"):
            ios.click_by_text("DISCOVER MY BENTLEY")
            sleep(2)
        else:
            ios.click_by_image("ios_Icons/ios_Logout_Icon.png")
            sleep(5)
            ios.click_by_text("DISCOVER MY BENTLEY")
            sleep(5)

        if find_icon_in_screen_ios(ios, "ios_Images/ios_My_Bentley_Demo_Mode_Page.png"):
            test_result.log_step("Demo_Mode_002 passed", True)
        else:
            test_result.log_step("Dashboard screen not detected, Demo_Mode_002 Failed", False)
    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)
    test_result.end_time = time.time()
    return test_result

def Demo_Mode_003(ios):
    test_result = TestCaseResult("Demo_Mode_003")
    test_result.description = "Verify Dashboard content"
    test_result.start_time = time.time()

    try:
        images = [
            "ios_Images/ios_My_Bentley_Demo_Mode_Page.png",
            "ios_Images/ios_Demo_Vehicle_Image.png",
            "ios_Images/ios_Demo_Greeting_Message.png",
            "ios_Images/ios_Demo_Lock_Button.png",
            "ios_Images/ios_Demo_Unlock_Button.png",
            "ios_Images/ios_Demo_Last_Contact_Details.png",
            "ios_Images/ios_Demo_Vehicle_Name.png"
        ]

        if all(compare_with_expected_crop_ios(ios,img) for img in images):
            test_result.log_step("All initial UI images validated, Demo Mode 003 passed", True)
        else:
            test_result.log_step(" Demo Mode 003 Fail", False)
        ios.extract_dashboard_metrics_Overview()

        for _ in range(2):
            ios.swipe("up")
            sleep(3)
            ios.extract_dashboard_metrics_Overview()

        for _ in range(2):
            ios.swipe("down")
            sleep(2)
    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)

    test_result.end_time = time.time()
    return test_result

def Demo_Mode_004(ios):
    test_result = TestCaseResult("Demo_Mode_004")
    test_result.description = "Verify Car Remote screen"
    test_result.start_time = time.time()

    try:
        ios.click_by_image("ios_Icons/ios_remote_icon.png", threshold=0.80)
        sleep(3)
        if find_icon_in_screen_ios(ios,"ios_Images/ios_Demo_Mode_Car_Remote_Screen.png"):
            test_result.log_step("Car Remote screen visible, Demo_Mode_004 Passed",True)
        else:
            test_result.log_step("Demo_Mode_004 Fail", False)

        ios.extract_car_statistics()
        ios.extract_battery_charge()
        ios.extract_cabin_comfort()
        ios.swipe("up")
        ios.extract_remote_parking()
        ios.extract_theft_alarm()
        ios.extract_roadside_assistance()
        ios.swipe("up")
        ios.extract_data_services()

        for _ in range(2):
            ios.swipe("down")
            sleep(2)
        ios.click_by_image("ios_Icons/ios_Home.png", threshold=0.80)
    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)

    test_result.end_time = time.time()
    return test_result

def Demo_Mode_005(ios):
    test_result = TestCaseResult("Demo_Mode_005")
    test_result.description = "Verify My Car Statistics screen"
    test_result.start_time = time.time()

    try:
        ios.click_by_image("ios_Icons/ios_remote_icon.png", threshold=0.80)
        sleep(2)
        ios.click_by_text("MY CAR STATISTICS")
        sleep(3)
        if find_icon_in_screen_ios(ios,"ios_Images/ios_Mycar_Statistics.png"):
            test_result.log_step("My Car Statistics screen visible, Demo_Mode_005 Passed", True)
        else:
            test_result.log_step("Demo_Mode_005 Fail", False)

        ios.click_by_image("ios_Icons/ios_Back_Icon.png", threshold=0.80)
        sleep(2)
        ios.click_by_image("ios_Icons/ios_Home.png", threshold=0.80)

    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)

    test_result.end_time = time.time()
    return test_result

def Demo_Mode_006(ios):
    test_result = TestCaseResult("Demo_Mode_006")
    test_result.start_time = time.time()
    test_passed = True

    try:
        test_result.description = "Verify Navigation Screen UI Elements"
        # Step 1: Click on Navigation icon
        ios.click_by_image("ios_Icons/ios_Navigation_Icon.png", threshold=0.80)
        time.sleep(3)

        # Step 2: Handle "ALLOW" popup
        if find_icon_in_screen_ios(ios, "ios_Images/ios_Navigation_Allow.png"):
            ios.click_by_image("ios_Images/ios_Navigation_Allow.png", threshold=0.80)
            time.sleep(3)

        # Step 3: Validate search image
        if compare_with_expected_crop_ios(ios,"ios_Images/ios_Navigation_Search.png"):
            test_result.log("Search image matched")
        else:
            test_result.log("Search image not matched")
            test_passed = False

        # Step 4: Validate Car icon
        if compare_with_expected_crop_ios(ios,"ios_Images/ios_Navigation_Car_Icon.png"):
            test_result.log("Car image matched")
        else:
            test_result.log("Car image not matched")
            test_passed = False

        # Step 5: Validate Profile icon
        if compare_with_expected_crop_ios(ios, "ios_Images/ios_Navigation_User_Icon.png"):
            test_result.log("User image matched")
        else:
            test_result.log("User image not matched")
            test_passed = False

        # Step 6: Validate Satellite Traffic screen
        ios.click_by_image("ios_Icons/ios_Navigation_Satellite_icon.png", threshold=0.80)
        time.sleep(2)
        if compare_with_expected_crop_ios(ios,"ios_Images/ios_Satellite_Traffic_Screen.png"):
            test_result.log("Satellite traffic screen matched")
        else:
            test_result.log("Satellite traffic screen did not match")
            test_passed = False

        # Step 7: Final result
        if test_passed:
            test_result.log("✅ Demo_Mode_006 passed")
            test_result.status = "Passed"
        else:
            test_result.log("❌ Demo_Mode_006 failed")
            test_result.status = "Failed"

    except Exception as e:
        test_result.log(f"❌ Unexpected error: {e}")
        test_result.status = "Failed"

    test_result.end_time = time.time()
    return test_result


def Demo_Mode_007(ios):
    test_result = TestCaseResult("Demo_Mode_007")
    test_result.description = "Verify Notification screen"
    test_result.start_time = time.time()

    try:
        ios.click_element_generic("accessibility_id", "Notifications")
        sleep(3)
        result = compare_with_expected_crop_ios(ios,"ios_Images/ios_Notification_Title.png")
        test_result.log_step("Notification title validated", result)
        ios.extract_last_updated()

    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)

    test_result.end_time = time.time()
    return test_result

def Demo_Mode_008(ios):
    test_result = TestCaseResult("Demo_Mode_008")
    test_result.description = "Verify Profile screen"
    test_result.start_time = time.time()
    test_passed = True

    try:
        # 1) Open Profile tab
        ios.click_element_generic("accessibility_id", "Profile")

        # 2) Validate Profile screen header/title
        ok = compare_with_expected_crop_ios(ios,"ios_Images/ios_Profile_Screen.png")
        test_result.log_step("Profile Title is present", ok)
        test_passed &= ok

        # 3) Validate user avatar/icon
        ok = compare_with_expected_crop_ios(ios,"ios_Images/ios_Profile_Screen_User_Icon.png")
        test_result.log_step("Profile User Icon is present", ok)
        test_passed &= ok

        # 4) Validate user name
        ok = compare_with_expected_crop_ios(ios,"ios_Images/ios_Profile_Screen_User_Name.png")
        test_result.log_step("Profile User Name is present", ok)
        test_passed &= ok

        # 5) Validate 'My details' tab
        ok = compare_with_expected_crop_ios(ios,"ios_Images/ios_Profile_Screen_MyDetails_Tab.png")  # ensure exact filename
        test_result.log_step("Profile 'My details' tab is present", ok)
        test_passed &= ok

        # 6) Navigate to Account
        ios.click_by_text("Account")

        ok = compare_with_expected_crop_ios(ios,"ios_Images/ios_Profile_Account_Screen.png")
        test_result.log_step("Profile Account screen is present", ok)
        test_passed &= ok

        # 7) Navigate to General
        ios.click_by_text("General")

        ok = compare_with_expected_crop_ios(ios,"ios_Images/ios_Profile_General_Screen.png")
        test_result.log_step("Profile General screen is present", ok)
        test_passed &= ok

        # 8) Settings icon visible on Profile (if expected on this screen)
        ok = compare_with_expected_crop_ios(ios,"ios_Images/ios_Profile_Screen_Setting_Icon.png")
        test_result.log_step("Profile Settings icon is present", ok)
        test_passed &= ok

        # Final status (kept for readability in the report)
        if test_passed:
            test_result.log("✅ Demo_Mode_008 passed")
            test_result.status = "Passed"
        else:
            test_result.log("❌ Demo_Mode_008 failed")
            test_result.status = "Failed"

        #Come back to my details tab in profile screen
        ios.click_by_text("My Details")
        sleep(2)
        ios.click_by_image("ios_Icons/ios_Home.png", threshold=0.80)

    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)

    test_result.end_time = time.time()
    return test_result

def Demo_Mode_009(ios):
    test_result = TestCaseResult("Demo_Mode_009")
    test_result.description = "Verify Setting screen"
    test_result.start_time = time.time()
    try:
        # 1) Open Profile tab
        ios.click_element_generic("accessibility_id", "Profile")
        sleep(2)
        #Click on setting icon in profile screen
        ios.click_by_image("ios_Icons/ios_Profile_Screen_Setting_Icon.png", threshold=0.80)
        sleep(2)
        if compare_with_expected_crop_ios(ios,"ios_Images/ios_Setting_Screen.png"):
            test_result.log_step("Demo_Mode_009 passed", True)
        else:
            test_result.log_step("Setting Screen options are not present, Demo_Mode_009 Failed", False)

        ios.click_by_image("ios_Icons/ios_Back_Icon.png", threshold=0.80)
        sleep(2)
        ios.click_by_image("ios_Icons/ios_Home.png", threshold=0.80)
        sleep(2)
    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)

    test_result.end_time = time.time()
    return test_result

def Demo_Mode_010(ios):
    test_result = TestCaseResult("Demo_Mode_010")
    test_result.description = "Verify Add vehicle screen"
    test_result.start_time = time.time()
    try:
        for _ in range(4):
            ios.click_by_image("ios_Icons/ios_Homescreen_Right_Arrow.png", threshold=0.80)
            sleep(2)
        if compare_with_expected_crop_ios(ios,"ios_Images/ios_Add_Vehicle_Information_Screen.png"):
            test_result.log_step("Demo_Mode_010 passed", True)
        else:
            test_result.log_step("Vehicle info Screen options are not present, Demo_Mode_010 Failed", False)
        for _ in range(4):
            ios.click_by_image("ios_Icons/ios_Homescreen_Left_Arrow.png", threshold=0.80)
            sleep(2)
    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)

    test_result.end_time = time.time()
    return test_result

def Demo_Mode_011(ios):
    test_result = TestCaseResult("Demo_Mode_011")
    test_result.description = "Verify all the screen with Bentley style guide."
    test_result.start_time = time.time()
    try:
        images = [
            "ios_Images/ios_My_Bentley_Demo_Mode_Page.png",
            "ios_Images/ios_Demo_Vehicle_Image.png",
            "ios_Images/ios_Demo_Greeting_Message.png",
            "ios_Images/ios_Demo_Lock_Button.png",
            "ios_Images/ios_Demo_Unlock_Button.png",
            "ios_Images/ios_Demo_Last_Contact_Details.png",
            "ios_Images/ios_Demo_Vehicle_Name.png"
        ]
        if all(compare_with_expected_crop_ios(ios, img) for img in images):
            test_result.log_step("All initial UI images validated,Demo_mode_011 Passed", True)
        else:
            test_result.log_step("Demo_mode_011 Fail", False)
    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)

    test_result.end_time = time.time()
    return test_result

def Demo_Mode_012(ios):
    test_result = TestCaseResult("Demo_Mode_012")
    test_result.description = ("Verification of Log out")
    test_result.start_time = time.time()
    try:
        ios.click_element_generic("accessibility_id", "Profile")
        sleep(2)
        compare_with_expected_crop_ios(ios,"ios_Images/ios_Profile_Screen.png")
        ios.click_by_text("General")
        sleep(2)
        compare_with_expected_crop_ios(ios,"ios_Images/ios_Profile_General_Screen.png")
        ios.click_by_text("Log out")
        sleep(5)
        if compare_with_expected_crop_ios(ios,"ios_Images/ios_My_Bentley_Login_Page.png"):
            test_result.log_step("Sign in page is visible,Demo_mode_012 Passed", True)
        else:
            test_result.log_step("Demo_mode_012 Fail", False)

        find_icon_in_screen_ios(ios,"ios_Images/ios_My_Bentley_Login_Page.png")
        ios.click_by_text("DISCOVER MY BENTLEY")
        sleep(5)
    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)

    test_result.end_time = time.time()
    return test_result

def Demo_Mode_013(ios):
    test_result = TestCaseResult("Demo_Mode_013")
    test_result.description = ("Verification of Log out")
    test_result.start_time = time.time()
    try:
        ios.click_by_image("ios_Icons/ios_Logout_Icon.png")
        sleep(5)
        if compare_with_expected_crop_ios(ios,"ios_Images/ios_My_Bentley_Login_Page.png"):
            test_result.log_step("Sign in page is visible,Demo_mode_013 Passed", True)
        else:
            test_result.log_step("Demo_mode_013 Fail", False)
    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)

    test_result.end_time = time.time()
    return test_result

Demo_Mode_001(ios)