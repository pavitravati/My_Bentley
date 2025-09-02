from time import sleep
from common_utils.ios_image_comparision import *
from common_utils.test_result_tracker import TestCaseResult

MAC_IP = "192.168.1.4"
PORT = 8101
UDID = "00008130-0012513918A1401C"
TEAM_ID = "LDD46J9733"
BUNDLE_ID = "uk.co.bentley.MyBentley"  # App to launch

# Initialize and start session (app launches automatically)
ios = IOSController(mac_ip=MAC_IP, port=PORT, udid=UDID, team_id=TEAM_ID, bundle_id=BUNDLE_ID)
ios.start_session()


def Demo_Mode_001():
    test_result = TestCaseResult("Demo_Mode_001")
    test_result.description = "Accessing Demo mode"
    test_result.start_time = time.time()
    try:
        if  find_icon_in_screen_ios(ios, "ios_Images/ios_My_Bentley_Login_Page.png"):
            ios.click_by_text("DISCOVER MY BENTLEY")
            sleep(2)
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

def Demo_Mode_002():
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

def Demo_Mode_003():
    test_result = TestCaseResult("Demo_Mode_003")
    test_result.description = "Verify Dashboard content"
    test_result.start_time = time.time()

    try:
        images = [
            "ios_My_Bentley_Demo_Mode_Page.png",
            "ios_Demo_Vehicle_Image.png",
            "ios_Demo_Greeting_Message.png",
            "ios_Demo_Lock_Button.png",
            "ios_Demo_Unlock_Button.png",
            "ios_Demo_Last_Contact_Details.png",
            "ios_Demo_Vehicle_Name.png"
        ]

        if all(compare_with_expected_crop_ios(ios,img) for img in images):
            test_result.log_step("All initial UI images validated, Demo Mode 003 passed", True)
        else:
            test_result.log_step(" Demo Mode 003 Fail", False)
        ios.extract_dashboard_metrics_Overview()

    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)

    test_result.end_time = time.time()
    return test_result

def Demo_Mode_004():
    test_result = TestCaseResult("Demo_Mode_004")
    test_result.description = "Verify Car Remote screen"
    test_result.start_time = time.time()

    try:
        ios.click_by_image("ios_Icons/ios_Windows_Icon.png", threshold=0.80)
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
    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)

    test_result.end_time = time.time()
    return test_result

def Demo_Mode_005():
    test_result = TestCaseResult("Demo_Mode_005")
    test_result.description = "Verify My Car Statistics screen"
    test_result.start_time = time.time()

    try:
        ios.click_by_image("ios_Icons/ios_my_car_statistics.png", threshold=0.80)
        sleep(3)
        if find_icon_in_screen_ios(ios,"ios_Images/ios_Car_Statistics_Screen.png"):
            test_result.log_step("My Car Statistics screen visible, Demo_Mode_005 Passed", True)
        else:
            test_result.log_step("Demo_Mode_005 Fail", False)

        ios.click_by_image("ios_Icons/back_icon.png", threshold=0.80)

    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)

    test_result.end_time = time.time()
    return test_result

def Demo_Mode_006():
    test_result = TestCaseResult("Demo_Mode_006")
    test_result.start_time = time.time()
    test_passed = True

    try:
        test_result.description = "Verify Navigation screen"
        # Step 1: Click on Navigation icon
        ios.click_by_image("ios_images/ios_navigation_icon.png", threshold=0.80)
        time.sleep(3)
        # Step 2: Handle "ALLOW" popup
        if find_icon_in_screen_ios(ios, "ios_Images/ios_Navigation_Allow.png"):
            ios.click_by_text("ALLOW")
            time.sleep(3)

        # Step 3: Validate search image
        if compare_with_expected_crop_ios(ios,"ios_Images/ios_Navigation_Search_Image.png"):
            test_result.log("Search image matched")
        else:
            test_result.log("Search image not matched")
            test_passed = False

        # Step 4: Validate Car icon
        if controller.d(resourceId="uk.co.bentley.mybentley:id/tab_vehicle_dashboard").exists:
            test_result.log("Car icon is visible")
        else:
            test_result.log("Car icon is missing")
            test_passed = False

        # Step 5: Validate Profile icon
        if controller.d(resourceId="uk.co.bentley.mybentley:id/tab_profile").exists:
            test_result.log("Profile icon is visible")
        else:
            test_result.log("Profile icon is missing")
            test_passed = False

        # Step 6: Validate Satellite Traffic screen
        controller.click_by_image("Icons/satellite_icon.png", threshold=0.80)
        time.sleep(2)
        if compare_with_expected_crop("Images/Satellite_Traffic_Screen.png"):
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

def dummy():
    sleep(3)
    ios.take_screenshot("dummy.png")

Demo_Mode_004()