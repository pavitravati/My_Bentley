from time import sleep
from PythonProject.common_utils.ios_image_comparision import *
from PythonProject.common_utils.test_result_tracker import TestCaseResult

MAC_IP = "192.168.1.5"
PORT = 8101
UDID = "00008130-0012513918A1401C"
TEAM_ID = "LDD46J9733"
BUNDLE_ID = "uk.co.bentley.MyBentley"  # App to launch

# MAC_IP = "192.168.0.31"
# PORT = 8101
# UDID = "00008110-0002481A1188401E"
# TEAM_ID = "DZDAJ9XWDH"
# BUNDLE_ID = "uk.co.bentley.MyBentley"  # App to launch

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
        #ios.click_by_resource_id("uk.co.bentley.mybentley:id/frameLayout_content_container_bottom_navigation")
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
    test_result.description = "Click bottom navigation on iOS"
    test_result.start_time = time.time()

    try:
        if ios.click_by_accessibility_id("BottomNavigation"):  # replace with real id
            test_result.log_step("Successfully clicked bottom navigation", True)
        else:
            test_result.log_step("Failed to click bottom navigation", False)

    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)

    test_result.end_time = time.time()
    return test_result

