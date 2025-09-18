from time import sleep
from PythonProject.common_utils.android_image_comparision import *
from PythonProject.common_utils.android_controller import *
from PythonProject.core.log_emitter import log_emitter


# Made a copy of the demo mode testcases to try and get them connected to the ui
def log(msg):
    log_emitter.log_signal.emit(msg)

# if a testcase fails/error need something that can get it to a state for the next test case because the aim is for
# each one to run into the other so one failing could disrupt that flow
def fail_reload():
    controller.launch_app("uk.co.bentley.mybentley")
    sleep(2)

    if find_icon_in_screen("Images/My_Bentley_Login_Page.png"):
        controller.click_text("DISCOVER MY BENTLEY")
    else:
        controller.click_by_image("Icons/Logout_icon.png")
        sleep(5)
        controller.click_text("DISCOVER MY BENTLEY")

def Demo_Mode_001():
    try:
        controller.launch_app("uk.co.bentley.mybentley")
        sleep(2)

        if find_icon_in_screen("Images/My_Bentley_Login_Page.png"):
            if controller.click_text("DISCOVER MY BENTLEY"):
                log("✅ - Demo Mode link clicked")
            else:
                log("❌ - Demo Mode link not found")
        else:
            controller.click_by_image("Icons/logout_icon.png")
            sleep(5)
            if controller.click_text("DISCOVER MY BENTLEY"):
                log("✅ - Demo Mode link clicked")
            else:
                log("❌ - Demo Mode link not found")

        if find_icon_in_screen("Images/My_Bentley_Demo_Mode_Page.png"):
            log("✅ - Demo Mode Launched successfully, Demo_Mode_001 Passed")
        else:
            log("❌ - Dashboard screen not detected, Demo_Mode_001 Failed")

    except Exception as e:
        log(f"⚠️ - Unexpected error: {e}")

def Demo_Mode_002():
    try:
        if find_icon_in_screen("Images/My_Bentley_Demo_Mode_Page.png"):
            log("✅ - Demo mode dashboard visible,Demo_Mode_002 Passed")
        else:
            log("❌ - Dashboard screen not detected, Demo_Mode_002 Failed")
    except Exception as e:
        log(f"⚠️ - Unexpected error: {e}")

def Demo_Mode_003():
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
            log("✅ - All initial UI images validated, Demo_Mode_003 passed")
        else:
            log("❌ - Demo_Mode_003 Failed")
            for img in images:
                log(f"{img[7:]} - {"✅" if compare_with_expected_crop(img) else "❌"}")

        metrics = []
        for _ in range(2):
            controller.swipe_up()
            sleep(3)
            metrics += controller.extract_dashboard_metrics()

        if metrics:
            log("Extracted Metrics:")
            for metric, stat in metrics:
                log(f"{metric}: {stat}")

        for _ in range(2):
            controller.swipe_down()
            sleep(2)

    except Exception as e:
        log(f"⚠️ - Unexpected error: {e}")

def Demo_Mode_004():
    try:
        controller.click_by_image("Icons/windows_icon.png")
        sleep(3)
        if find_icon_in_screen("Images/Demo_Mode_Car_Remote_Screen.png"):
            log("✅ - Car Remote screen visible, Demo_Mode_004 Passed")
        else:
            log("❌ - Car Remote screen not visible, Demo_Mode_004 Failed")

        metrics = []
        for _ in range(4):
            metrics += controller.extract_dashboard_metrics()
            controller.swipe_up()
            sleep(2)

        if metrics:
            log("Extracted Metrics:")
            for metric, stat in metrics:
                log(f"{metric}: {stat}")

        for _ in range(2):
            controller.swipe_down()
            sleep(2)

    except Exception as e:
        log(f"⚠️ - Unexpected error: {e}")

def Demo_Mode_005():
    try:
        controller.click_by_image("Icons/my_car_statistics.png")
        sleep(3)
        if find_icon_in_screen("Images/Car_Statistics_Screen.png"):
            log("✅ - My Car Statistics screen visible, Demo_Mode_005 Passed")
        else:
            log("❌ - My Car Statistics screen not visible, Demo_Mode_005 Fail")

        controller.click_by_image("Icons/back_icon.png")

    except Exception as e:
        log(f"⚠️ - Unexpected error: {e}")

def Demo_Mode_006():
    test_passed = True
    try:
        # Step 1: Click on Navigation icon
        controller.click_by_image("Icons/navigation_icon.png")
        time.sleep(3)

        # Step 2: Handle "ALLOW" popup
        if find_icon_in_screen("Images/Navigation_Allow.png"):
            controller.click_text("ALLOW")
            time.sleep(3)

        # Step 3: Validate search image
        if compare_with_expected_crop("Images/Navigation_Search_Image.png"):
            log("Search image matched - ✅")
        else:
            log("Search image not matched - ❌")
            test_passed = False

        # Step 4: Validate Car icon
        if controller.d(resourceId="uk.co.bentley.mybentley:id/tab_vehicle_dashboard").exists:
            log("Car icon is visible - ✅")
        else:
            log("Car icon is missing - ❌")
            test_passed = False

        # Step 5: Validate Profile icon
        if controller.d(resourceId="uk.co.bentley.mybentley:id/tab_profile").exists:
            log("Profile icon is visible - ✅")
        else:
            log("Profile icon is missing - ❌")
            test_passed = False

        # Step 6: Validate Satellite Traffic screen
        controller.click_by_image("Icons/satellite_icon.png")
        time.sleep(2)
        if compare_with_expected_crop("Images/Satellite_Traffic_Screen.png"):
            log("Satellite traffic screen matched - ✅")
        else:
            log("Satellite traffic screen did not match - ❌")
            test_passed = False

        # Step 7: Final result
        if test_passed:
            log("✅ - Demo_Mode_006 passed")
        else:
            log("❌ - Demo_Mode_006 failed")

    except Exception as e:
        log(f"⚠️ - Unexpected error: {e}")

def Demo_Mode_007():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_messages")
        sleep(3)
        if compare_with_expected_crop("Images/Notification_Title.png"):
            log("✅ - Notification title validated")
        else:
            log("❌ - Notification title not validated")

        controller.extract_dashboard_metrics()

        metrics = []
        if metrics:
            log("✅ - Extracted Metrics:")
            for metric, stat in metrics:
                log(f"{metric}: {stat}")
        else:
            log("❌ - No Metrics extracted")

    except Exception as e:
        log(f"⚠️ - Unexpected error: {e}")

def Demo_Mode_008():
    test_passed = True
    try:
        # (Optional) keep a screenshot if you want – but not required for validation
        # controller.take_screenshot("profilescreen.png")

        # 1) Open Profile tab
        ok = controller.click_by_image("Icons/Profile_Icon.png")
        if ok:
            log("✅ - Tapped Profile tab")
        if not ok:
            log("❌ - Profile tab not tapped")
            test_passed = False
        time.sleep(2)

        # 2) Validate Profile screen header/title
        ok = compare_with_expected_crop("Images/Profile_Screen.png")
        if ok:
            log("Profile Title is present - ✅")
        if not ok:
            log("Profile Title is not present - ❌")
            test_passed = False

        # 3) Validate user avatar/icon
        ok = compare_with_expected_crop("Images/Profile_Screen_User_Icon.png")
        if ok:
            log("Profile User Icon is present - ✅")
        if not ok:
            log("Profile User Icon is not present - ❌")
            test_passed = False

        # 4) Validate user name
        ok = compare_with_expected_crop("Images/Profile_Screen_User_Name.png")
        if ok:
            log("Profile User Name is present - ✅")
        if not ok:
            log("Profile User Name is not present - ❌")
            test_passed = False


        # 5) Validate 'My details' tab
        ok = compare_with_expected_crop("Images/Profile_Screen_MyDetails_Tab.png")  # ensure exact filename
        if ok:
            log("Profile 'My details' tab is present - ✅")
        if not ok:
            log("Profile 'My details' tab is not present - ❌")
            test_passed = False

        # 6) Navigate to Account
        ok = controller.click_by_image("Icons/Profile_Account_Icon.png")
        if ok:
            log("Tapped Account - ✅")
        if not ok:
            log("Account not tapped - ❌")
            test_passed = False
        time.sleep(2)

        ok = compare_with_expected_crop("Images/Profile_Account_Screen.png")
        if ok:
            log("Profile Account screen is present - ✅")
        if not ok:
            log("Profile Account screen is not present - ❌")
            test_passed = False

        # 7) Navigate to General
        ok = controller.click_by_image("Icons/Profile_General_Icon.png")
        if ok:
            log("Tapped General - ✅")
        if not ok:
            log("General not tapped - ❌")
            test_passed = False
        time.sleep(2)

        ok = compare_with_expected_crop("Images/Profile_General_Screen.png")
        if ok:
            log("Profile General screen is present - ✅")
        if not ok:
            log("Profile General screen is not present - ❌")
            test_passed = False

        # 8) Settings icon visible on Profile (if expected on this screen)
        ok = compare_with_expected_crop("Images/Profile_Screen_Setting_Icon.png")
        if ok:
            log("Profile Settings icon is present - ✅")
        if not ok:
            log("Profile Settings icon is not present - ❌")
            test_passed = False

        # Final status (kept for readability in the report)
        if test_passed:
            log("✅ - Demo_Mode_008 passed")
        else:
            log("❌ - Demo_Mode_008 failed")

        #Come back to my details tab in profile screen
        controller.click_by_image("Icons/Profile_Mydetails_Icon.png")

    except Exception as e:
        log(f"⚠️ - Unexpected error: {e}")

def Demo_Mode_009():
    try:
        #Click on setting icon in profile screen
        controller.click_by_image("Icons/Profile_Screen_Setting_Icon.png")
        sleep(2)
        if compare_with_expected_crop("Images/Setting_Screen.png"):
            log("✅ - Demo_Mode_009 passed")
        else:
            log("❌ - Setting Screen options are not present, Demo_Mode_008 failed")

        controller.click_by_image("Icons/back_icon.png")
        sleep(2)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        sleep(2)

    except Exception as e:
        log(f"⚠️ - Unexpected error: {e}")

def Demo_Mode_010():
    try:
        for _ in range(4):
            controller.click_by_image("Icons/Homescreen_Right_Arrow.png")
            sleep(2)
        if compare_with_expected_crop("Images/Add_Vehicle_Information_Screen.png"):
            log("✅ - Demo_Mode_010 passed")
        else:
            log("❌ - Vehicle info Screen options are not present, Demo_Mode_010 Failed")
        for _ in range(4):
            controller.click_by_image("Icons/Homescreen_Left_Arrow.png")
            sleep(2)

    except Exception as e:
        log(f"⚠️ - Unexpected error: {e}")

def Demo_Mode_011():
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
            log("❌ - Demo_Mode_011 Failed")
            for img in images:
                log(f"{img[7:]} - {"✅" if compare_with_expected_crop(img) else "❌"}")

    except Exception as e:
        log(f"⚠️ - Unexpected error: {e}")

def Demo_Mode_012():
    try:
        controller.click_by_image("Icons/Profile_Icon.png")
        sleep(2)
        compare_with_expected_crop("Images/Profile_Screen.png")
        controller.click_by_image("Icons/Profile_General_Icon.png")
        sleep(2)
        compare_with_expected_crop("Images/Profile_General_Screen.png")
        if controller.click_by_image("Icons/Profile_Logout_Icon.png"):
            log("✅ - Demo mode exiting")
        else:
            log("❌ - Demo mode not exiting")
        sleep(5)
        if compare_with_expected_crop("Images/My_Bentley_Login_Page.png"):
            log("✅ - Sign in page is visible, Demo_mode_012 Passed")
        else:
            log("❌ - Demo_mode_012 Fail")

        find_icon_in_screen("Images/My_Bentley_Login_Page.png")
        controller.click_text("DISCOVER MY BENTLEY")
        sleep(5)

    except Exception as e:
        log(f"⚠️ - Unexpected error: {e}")

def Demo_Mode_013():
    try:
        if controller.click_by_image("Icons/logout_icon.png"):
            log("✅ - Demo mode exiting")
        else:
            log("❌ - Demo mode not exiting")
        sleep(5)
        if compare_with_expected_crop("Images/My_Bentley_Login_Page.png"):
            log("✅ - Sign in page is visible,Demo_mode_013 Passed")
        else:
            log("❌ - Demo_mode_013 Fail")
    except Exception as e:
        log(f"⚠️ - Unexpected error: {e}")