from time import sleep
from common_utils.android_image_comparision import *
from common_utils.android_controller import *
from core.log_emitter import log_emitter


# Made a copy of the demo mode testcases to try and get them connected to the ui
def log(msg):
    log_emitter.log_signal.emit(msg)

def fail_log(msg, num):
    log(f"{msg}")
    controller.take_fail_screenshot(f"DemoMode_{msg}_{num}.png")

def error_log(e, num):
    log(f"⚠️ - Unexpected error: {e}")
    controller.take_fail_screenshot(f"DemoMode_{e}_{num}.png")

def DemoMode_001():
    try:
        controller.launch_app("uk.co.bentley.mybentley")
        sleep(2)

        if find_icon_in_screen("Images/My_Bentley_Login_Page.png"):
            if controller.click_text("DISCOVER MY BENTLEY"):
                log("✅ - Demo Mode link clicked")
            else:
                fail_log("❌ - Demo Mode link not found", "001")
        else:
            controller.click_by_image("Icons/logout_icon.png")
            sleep(5)
            if controller.click_text("DISCOVER MY BENTLEY"):
                log("✅ - Demo Mode link clicked")
            else:
                fail_log("❌ - Demo Mode link not found", "001")

        sleep(1)
        if find_icon_in_screen("Images/My_Bentley_Demo_Mode_Page.png"):
            log("✅ - Demo Mode Launched successfully, Demo_Mode_001 Passed")
        else:
            fail_log("❌ - Dashboard screen not detected, Demo_Mode_001 Failed", "001")

    except Exception as e:
        error_log(e, "001")

def DemoMode_002():
    try:
        if find_icon_in_screen("Images/My_Bentley_Demo_Mode_Page.png"):
            log("✅ - Demo mode dashboard visible")
            log("✅ - Demo_Mode_002 Passed")
        else:
            fail_log("❌ - Dashboard screen not detected", "002")
            log("❌ - Demo_Mode_002 Failed")
    except Exception as e:
        error_log(e, "002")

def DemoMode_003():
    try:
        images = [
            "Images/My_Bentley_Demo_Mode_Page.png",
            "Images/Demo_Vehicle_Image.png",
            "Images/Demo_Greetings.png",
            "Images/Demo_Lock_Button.png",
            "Images/Demo_Unlock_Button.png",
            "Images/Demo_Vehicle_Last_Contact.png",
            "Images/Demo_Vehicle_Name.png"
        ]

        if all(compare_with_expected_crop(img) for img in images):
            log("✅ - All initial UI images validated")
            log("✅ - Demo_Mode_003 passed")
        else:
            fail_log("❌ - Initial UI images not validated", "003")
            log("❌ - Demo_Mode_003 Failed")
            for img in images:
                if compare_with_expected_crop(img):
                    log(f"{img[7:]} - ✅")
                else:
                    fail_log(f"{img[7:]} - ❌", "003")

        metrics = []
        for _ in range(2):
            controller.swipe_up()
            extracted = controller.extract_dashboard_metrics()
            metrics.extend(extracted.items())

        if metrics:
            log("✅ - Extracted Metrics:")
            for metric, stat in metrics:
                log(f"{metric}: {stat}")
        else:
            fail_log("❌ - Metrics not extracted", "003")

        for _ in range(2):
            controller.swipe_down()

    except Exception as e:
        error_log(e, "003")

def DemoMode_004():
    try:
        controller.click_by_image("Icons/windows_icon.png")
        sleep(1)
        if find_icon_in_screen("Images/Demo_Mode_Car_Remote_Screen.png"):
            log("✅ - Car Remote screen visible")
            log("✅ - Demo_Mode_004 Passed")
        else:
            fail_log("❌ - Car Remote screen not visible", "004")
            log("❌ - Demo_Mode_004 Failed")

        metrics = []
        for _ in range(4):
            extracted = controller.extract_dashboard_metrics()
            metrics.extend(extracted.items())
            controller.swipe_up()

        if metrics:
            log("✅ - Extracted Metrics:")
            for metric, stat in metrics:
                log(f"{metric}: {stat}")
        else:
            fail_log("❌ - Metrics not extracted", "004")

        for _ in range(2):
            controller.swipe_down()

        controller.click_by_image("Icons/home_icon.png")

    except Exception as e:
        error_log(e, "004")

def DemoMode_005():
    try:
        controller.click_by_image("Icons/windows_icon.png")
        sleep(1)
        controller.click_by_image("Icons/my_car_statistics.png")
        sleep(1)
        if find_icon_in_screen("Images/Car_Statistics_Screen.png"):
            log("✅ - My Car Statistics screen visible, Demo_Mode_005 Passed")
        else:
            fail_log("❌ - My Car Statistics screen not visible, Demo_Mode_005 Failed", "005")

        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/home_icon.png")

    except Exception as e:
        error_log(e, "005")

def DemoMode_006():
    test_passed = True
    try:
        # Step 1: Click on Navigation icon
        controller.click_by_image("Icons/navigation_icon.png")
        time.sleep(1)

        # Step 2: Handle "ALLOW" popup
        if find_icon_in_screen("Images/Navigation_Allow.png"):
            controller.click_text("ALLOW")
            time.sleep(1)

        # Step 3: Validate search image
        if compare_with_expected_crop("Images/Navigation_Search_Image.png"):
            log("Search image matched - ✅")
        else:
            fail_log("Search image not matched - ❌", "006")
            test_passed = False

        # Step 4: Validate Car icon
        if controller.d(resourceId="uk.co.bentley.mybentley:id/tab_vehicle_dashboard").exists:
            log("Car icon is visible - ✅")
        else:
            fail_log("Car icon is missing - ❌", "006")
            test_passed = False

        # Step 5: Validate Profile icon
        if controller.d(resourceId="uk.co.bentley.mybentley:id/tab_profile").exists:
            log("Profile icon is visible - ✅")
        else:
            fail_log("Profile icon is missing - ❌", "006")
            test_passed = False

        # Step 6: Validate Satellite Traffic screen
        controller.click_by_image("Icons/satellite_icon.png")
        time.sleep(1)
        if compare_with_expected_crop("Images/Satellite_Traffic_Screen.png"):
            log("Satellite traffic screen matched - ✅")
        else:
            fail_log("Satellite traffic screen did not match - ❌", "006")
            test_passed = False

        # Step 7: Final result
        if test_passed:
            log("✅ - Demo_Mode_006 passed")
        else:
            log("❌ - Demo_Mode_006 failed")

        controller.click_by_image("Icons/home_icon.png")

    except Exception as e:
        error_log(e, "006")

def DemoMode_007():
    try:
        controller.click_by_image("Icons/New_Notification_icon.png")
        controller.click_by_image("Icons/Notification_icon.png")
        sleep(1)
        if compare_with_expected_crop("Images/Notification_Title.png"):
            log("✅ - Notification title validated")
        else:
            fail_log("❌ - Notification title not validated", "007")

        # sleep(1)
        metrics = controller.extract_dashboard_metrics()

        if metrics:
            log("✅ - Extracted Metrics:")
            for metric, stat in metrics.items():
                log(f"{metric}: {stat}")
        else:
            fail_log("❌ - No Metrics extracted", "007")

        controller.click_by_image("Icons/home_icon.png")

    except Exception as e:
        error_log(e, "007")

def DemoMode_008():
    test_passed = True
    try:
        # 1) Open Profile tab
        ok = controller.click_by_image("Icons/Profile_Icon.png")
        if ok:
            log("✅ - Tapped Profile tab")
        if not ok:
            fail_log("❌ - Profile tab not tapped", "008")
            test_passed = False
        time.sleep(1)

        # 2) Validate Profile screen header/title
        ok = compare_with_expected_crop("Images/Profile_Screen.png")
        if ok:
            log("Profile Title is present - ✅")
        if not ok:
            fail_log("Profile Title is not present - ❌", "008")
            test_passed = False

        # 3) Validate user avatar/icon
        ok = compare_with_expected_crop("Images/Profile_Screen_User_Icon.png")
        if ok:
            log("Profile User Icon is present - ✅")
        if not ok:
            fail_log("Profile User Icon is not present - ❌", "008")
            test_passed = False

        # 4) Validate user name
        ok = compare_with_expected_crop("Images/Profile_Screen_User_Name.png")
        if ok:
            log("Profile User Name is present - ✅")
        if not ok:
            fail_log("Profile User Name is not present - ❌", "008")
            test_passed = False


        # 5) Validate 'My details' tab
        ok = compare_with_expected_crop("Images/Profile_Screen_MyDetails_Tab.png")  # ensure exact filename
        if ok:
            log("Profile 'My details' tab is present - ✅")
        if not ok:
            fail_log("Profile 'My details' tab is not present - ❌", "008")
            test_passed = False

        # 6) Navigate to Account
        ok = controller.click_by_image("Icons/Profile_Account_Icon.png")
        if ok:
            log("Tapped Account - ✅")
        if not ok:
            fail_log("Account not tapped - ❌", "008")
            test_passed = False
        time.sleep(1)

        ok = compare_with_expected_crop("Images/Profile_Account_Screen.png")
        if ok:
            log("Profile Account screen is present - ✅")
        if not ok:
            fail_log("Profile Account screen is not present - ❌", "008")
            test_passed = False

        # 7) Navigate to General
        ok = controller.click_by_image("Icons/Profile_General_Icon.png")
        if ok:
            log("Tapped General - ✅")
        if not ok:
            fail_log("General not tapped - ❌", "008")
            test_passed = False
        time.sleep(1)

        ok = compare_with_expected_crop("Images/Profile_General_Screen.png")
        if ok:
            log("Profile General screen is present - ✅")
        if not ok:
            fail_log("Profile General screen is not present - ❌", "008")
            test_passed = False

        # 8) Settings icon visible on Profile (if expected on this screen)
        ok = compare_with_expected_crop("Images/Profile_Screen_Setting_Icon.png")
        if ok:
            log("Profile Settings icon is present - ✅")
        if not ok:
            fail_log("Profile Settings icon is not present - ❌", "008")
            test_passed = False

        # Final status (kept for readability in the report)
        if test_passed:
            log("✅ - Demo_Mode_008 passed")
        else:
            log("❌ - Demo_Mode_008 failed")

        #Come back to my details tab in profile screen
        controller.click_by_image("Icons/Profile_Mydetails_Icon.png")
        sleep(1)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "008")

def DemoMode_009():
    try:
        controller.click_by_image("Icons/Profile_Icon.png")
        sleep(1)
        #Click on setting icon in profile screen
        controller.click_by_image("Icons/Profile_Screen_Setting_Icon.png")
        sleep(1)
        if compare_with_expected_crop("Images/Setting_Screen.png"):
            log("✅ - Demo_Mode_009 passed")
        else:
            fail_log("❌ - Setting Screen options are not present, Demo_Mode_008 failed", "009")

        controller.click_by_image("Icons/back_icon.png")
        sleep(1)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "009")

def DemoMode_010():
    try:
        for _ in range(4):
            controller.click_by_image("Icons/Homescreen_Right_Arrow.png")
            sleep(0.2)
        if compare_with_expected_crop("Images/Add_Vehicle_Information_Screen.png"):
            log("✅ - Demo_Mode_010 passed")
        else:
            fail_log("❌ - Vehicle info Screen options are not present, Demo_Mode_010 Failed", "010")
        for _ in range(4):
            controller.click_by_image("Icons/Homescreen_Left_Arrow.png")

        controller.click_by_image("Icons/home_icon.png")

    except Exception as e:
        error_log(e, "010")

def DemoMode_011():
    try:
        images = [
            "Images/My_Bentley_Demo_Mode_Page.png",
            "Images/Demo_Vehicle_Image.png",
            "Images/Demo_Greetings.png",
            "Images/Demo_Lock_Button.png",
            "Images/Demo_Unlock_Button.png",
            "Images/Demo_Vehicle_Last_Contact.png",
            "Images/Demo_Vehicle_Name.png"
        ]

        if all(compare_with_expected_crop(img) for img in images):
            log("✅ - All initial UI images validated, Demo_mode_011 Passed")
        else:
            fail_log("❌ - Demo_Mode_011 Failed", "011")
            for img in images:
                if compare_with_expected_crop(img):
                    log(f"{img[7:]} - ✅")
                else:
                    fail_log(f"{img[7:]} - ❌", "011")

    except Exception as e:
        error_log(e, "011")

def DemoMode_012():
    try:
        controller.click_by_image("Icons/Profile_Icon.png")
        sleep(1)
        compare_with_expected_crop("Images/Profile_Screen.png")
        controller.click_by_image("Icons/Profile_General_Icon.png")
        sleep(1)
        compare_with_expected_crop("Images/Profile_General_Screen.png")
        if controller.click_by_image("Icons/Profile_Logout_Icon.png"):
            log("✅ - Demo mode exiting")
        else:
            fail_log("❌ - Demo mode not exiting", "012")
        print(123)
        sleep(1)
        if compare_with_expected_crop("Images/My_Bentley_Login_Page.png"):
            log("✅ - Sign in page is visible, Demo_mode_012 Passed")
        else:
            fail_log("❌ - Demo_mode_012 Fail", "012")

        find_icon_in_screen("Images/My_Bentley_Login_Page.png")
        controller.click_text("DISCOVER MY BENTLEY")
        sleep(1)

    except Exception as e:
        error_log(e, "012")

def DemoMode_013():
    try:
        if controller.click_by_image("Icons/logout_icon.png"):
            log("✅ - Demo mode exiting")
        else:
            fail_log("❌ - Demo mode not exiting", "013")
        sleep(1)
        if compare_with_expected_crop("Images/My_Bentley_Login_Page.png"):
            log("✅ - Sign in page is visible,Demo_mode_013 Passed")
        else:
            fail_log("❌ - Demo_mode_013 Fail", "013")
    except Exception as e:
        error_log(e, "013")