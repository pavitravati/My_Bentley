import time
from time import sleep
from common_utils.android_image_comparision import *
from common_utils.test_result_tracker import TestCaseResult
from common_utils.android_controller import *

controller = DeviceController()
d = u2.connect()

def Preconditions():
    controller.wake_up_unlock_screen()
    controller.press_home()

def Demo_Mode_001():
    test_result = TestCaseResult("Demo_Mode_001")
    test_result.description = "Accessing Demo mode"
    test_result.start_time = time.time()

    try:
        controller.launch_app("uk.co.bentley.mybentley")
        sleep(2)

        if find_icon_in_screen("Images/My_Bentley_Login_Page.png"):
            controller.click_text("DISCOVER MY BENTLEY")
        else:
            controller.click_by_image("Icons/logout_icon.png", threshold=0.80)
            sleep(5)
            controller.click_text("DISCOVER MY BENTLEY")

        if find_icon_in_screen("Images/My_Bentley_Demo_Mode_Page.png"):
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
        controller.launch_app("uk.co.bentley.mybentley")
        sleep(2)

        if find_icon_in_screen("Images/My_Bentley_Login_Page.png"):
            controller.click_text("DISCOVER MY BENTLEY")
        else:
            controller.click_by_image("Icons/logout_icon.png", threshold=0.80)
            sleep(5)
            controller.click_text("DISCOVER MY BENTLEY")

        if find_icon_in_screen("Images/My_Bentley_Demo_Mode_Page.png"):
            test_result.log_step("Demo mode dashboard visible,Demo_Mode_002 passed", True)
        else:
            test_result.log_step("Dashboard screen not detected, Demo_Mode_002 fail", False)
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
            "Images/My_Bentley_Demo_Mode_Page.png",
            "Images/Demo_Vehicle_Image.png",
            "Images/Demo_Greetings.png",
            "Images/Demo_Lock_Button.png",
            "Images/Demo_Unlock_Button.png",
            "Images/Demo_Vehicle_Last_Contact.png",
            "Images/Demo_Vehicle_Name.png"
        ]

        if all(compare_with_expected_crop(img) for img in images):
            test_result.log_step("All initial UI images validated, Demo Mode 003 passed", True)
        else:
            test_result.log_step(" Demo Mode 003 Fail", False)


        for _ in range(2):
            controller.swipe_up()
            sleep(3)
            controller.extract_dashboard_metrics()

        for _ in range(2):
            controller.swipe_down()
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
        controller.click_by_image("Icons/windows_icon.png", threshold=0.80)
        sleep(3)
        if find_icon_in_screen("Images/Demo_Mode_Car_Remote_Screen.png"):
            test_result.log_step("Car Remote screen visible, Demo_Mode_004 Passed",True)
        else:
            test_result.log_step("Demo_Mode_004 Fail", False)
        for _ in range(4):
            controller.extract_dashboard_metrics()
            controller.swipe_up()
            sleep(2)

        for _ in range(2):
            controller.swipe_down()
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
        controller.click_by_image("Icons/my_car_statistics.png", threshold=0.80)
        sleep(3)
        if find_icon_in_screen("Images/Car_Statistics_Screen.png"):
            test_result.log_step("My Car Statistics screen visible, Demo_Mode_005 Passed", True)
        else:
            test_result.log_step("Demo_Mode_005 Fail", False)

        controller.click_by_image("Icons/back_icon.png", threshold=0.80)

    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)

    test_result.end_time = time.time()
    return test_result

def Demo_Mode_006():
    test_result = TestCaseResult("Demo_Mode_006")
    test_result.start_time = time.time()
    test_passed = True

    try:
        test_result.description = "Verify Navigation Screen UI Elements"
        # Step 1: Click on Navigation icon
        controller.click_by_image("Icons/navigation_icon.png", threshold=0.80)
        time.sleep(3)

        # Step 2: Handle "ALLOW" popup
        if find_icon_in_screen("Images/Navigation_Allow.png"):
            controller.click_text("ALLOW")
            time.sleep(3)

        # Step 3: Validate search image
        if compare_with_expected_crop("Images/Navigation_Search_Image.png"):
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

def Demo_Mode_007():
    test_result = TestCaseResult("Demo_Mode_007")
    test_result.description = "Verify Notification screen"
    test_result.start_time = time.time()

    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_messages")
        sleep(3)
        result = compare_with_expected_crop("Images/Notification_Title.png")
        test_result.log_step("Notification title validated", result)

        controller.extract_dashboard_metrics()

    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)

    test_result.end_time = time.time()
    return test_result

def Demo_Mode_008():
    test_result = TestCaseResult("Demo_Mode_008")
    test_result.description = "Verify Profile screen"
    test_result.start_time = time.time()
    test_passed = True

    try:
        # (Optional) keep a screenshot if you want – but not required for validation
        # controller.take_screenshot("profilescreen.png")

        # 1) Open Profile tab
        ok = controller.click_by_image("Icons/Profile_Icon.png", threshold=0.80)
        test_result.log_step("Tapped Profile tab", ok)
        if not ok:
            test_passed = False
        time.sleep(2)

        # 2) Validate Profile screen header/title
        ok = compare_with_expected_crop("Images/Profile_Screen.png")
        test_result.log_step("Profile Title is present", ok)
        test_passed &= ok

        # 3) Validate user avatar/icon
        ok = compare_with_expected_crop("Images/Profile_Screen_User_Icon.png")
        test_result.log_step("Profile User Icon is present", ok)
        test_passed &= ok

        # 4) Validate user name
        ok = compare_with_expected_crop("Images/Profile_Screen_User_Name.png")
        test_result.log_step("Profile User Name is present", ok)
        test_passed &= ok

        # 5) Validate 'My details' tab
        ok = compare_with_expected_crop("Images/Profile_Screen_MyDetails_Tab.png")  # ensure exact filename
        test_result.log_step("Profile 'My details' tab is present", ok)
        test_passed &= ok

        # 6) Navigate to Account
        ok = controller.click_by_image("Icons/Profile_Account_Icon.png", threshold=0.80)
        test_result.log_step("Tapped Account", ok)
        test_passed &= ok
        time.sleep(2)

        ok = compare_with_expected_crop("Images/Profile_Account_Screen.png")
        test_result.log_step("Profile Account screen is present", ok)
        test_passed &= ok

        # 7) Navigate to General
        ok = controller.click_by_image("Icons/Profile_General_Icon.png", threshold=0.80)
        test_result.log_step("Tapped General", ok)
        test_passed &= ok
        time.sleep(2)

        ok = compare_with_expected_crop("Images/Profile_General_Screen.png")
        test_result.log_step("Profile General screen is present", ok)
        test_passed &= ok

        # 8) Settings icon visible on Profile (if expected on this screen)
        ok = compare_with_expected_crop("Images/Profile_Screen_Setting_Icon.png")
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
        controller.click_by_image("Icons/Profile_Mydetails_Icon.png", threshold=0.80)

    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)

    test_result.end_time = time.time()
    return test_result

def Demo_Mode_009():
    test_result = TestCaseResult("Demo_Mode_009")
    test_result.description = "Verify Setting screen"
    test_result.start_time = time.time()
    try:
        #Click on setting icon in profile screen
        controller.click_by_image("Icons/Profile_Screen_Setting_Icon.png", threshold=0.80)
        sleep(2)
        if compare_with_expected_crop("Images/Setting_Screen.png"):
            test_result.log_step("Demo_Mode_009 passed", True)
        else:
            test_result.log_step("Setting Screen options are not present, Demo_Mode_009 Failed", False)

        controller.click_by_image("Icons/back_icon.png", threshold=0.80)
        sleep(2)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        sleep(2)
    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)

    test_result.end_time = time.time()
    return test_result

def Demo_Mode_010():
    test_result = TestCaseResult("Demo_Mode_010")
    test_result.description = "Verify Add vehicle screen"
    test_result.start_time = time.time()
    try:
        for _ in range(4):
            controller.click_by_image("Icons/Homescreen_Right_Arrow.png", threshold=0.80)
            sleep(2)
        if compare_with_expected_crop("Images/Add_Vehicle_Information_Screen.png"):
            test_result.log_step("Demo_Mode_010 passed", True)
        else:
            test_result.log_step("Vehicle info Screen options are not present, Demo_Mode_010 Failed", False)
        for _ in range(4):
            controller.click_by_image("Icons/Homescreen_Left_Arrow.png", threshold=0.80)
            sleep(2)
    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)

    test_result.end_time = time.time()
    return test_result

def Demo_Mode_011():
    test_result = TestCaseResult("Demo_Mode_011")
    test_result.description = "Verify all the screen with Bentley style guide."
    test_result.start_time = time.time()
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
            test_result.log_step("All initial UI images validated,Demo_mode_011 Passed", True)
        else:
            test_result.log_step("Demo_mode_011 Fail", False)
    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)

    test_result.end_time = time.time()
    return test_result

def Demo_Mode_012():
    test_result = TestCaseResult("Demo_Mode_012")
    test_result.description = ("Verification of Log out")
    test_result.start_time = time.time()
    try:
        controller.click_by_image("Icons/Profile_Icon.png", threshold=0.80)
        sleep(2)
        compare_with_expected_crop("Images/Profile_Screen.png")
        controller.click_by_image("Icons/Profile_General_Icon.png", threshold=0.80)
        sleep(2)
        compare_with_expected_crop("Images/Profile_General_Screen.png")
        controller.click_by_image("Icons/Profile_Logout_Icon.png", threshold=0.80)
        sleep(5)
        if compare_with_expected_crop("Images/My_Bentley_Login_Page.png"):
            test_result.log_step("Sign in page is visible,Demo_mode_012 Passed", True)
        else:
            test_result.log_step("Demo_mode_012 Fail", False)

        find_icon_in_screen("Images/My_Bentley_Login_Page.png")
        controller.click_text("DISCOVER MY BENTLEY")
        sleep(5)
    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)

    test_result.end_time = time.time()
    return test_result

def Demo_Mode_013():
    test_result = TestCaseResult("Demo_Mode_013")
    test_result.description = ("Verification of Log out")
    test_result.start_time = time.time()
    try:
        controller.click_by_image("Icons/logout_icon.png", threshold=0.80)
        sleep(5)
        if compare_with_expected_crop("Images/My_Bentley_Login_Page.png"):
            test_result.log_step("Sign in page is visible,Demo_mode_013 Passed", True)
        else:
            test_result.log_step("Demo_mode_013 Fail", False)
    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)

    test_result.end_time = time.time()
    return test_result

def Profiles_001():
    test_result = TestCaseResult("Profiles_001")
    test_result.description = ("Accessing Profile screen via My Bentley App")
    test_result.start_time = time.time()
    try:
            # (Optional) keep a screenshot if you want – but not required for validation
            # controller.take_screenshot("profilescreen.png")

            # 1) Open Profile tab
            ok = controller.click_by_image("Icons/Profile_Icon.png", threshold=0.80)
            test_result.log_step("Tapped Profile tab", ok)
            if not ok:
                test_passed = False
            time.sleep(2)

            # 2) Validate Profile screen header/title
            ok = compare_with_expected_crop("Images/Profile_Screen.png")
            test_result.log_step("Profile Title is present", ok)
            test_passed &= ok

            # 3) Validate user avatar/icon
            ok = compare_with_expected_crop("Images/Profile_Screen_User_Icon.png")
            test_result.log_step("Profile User Icon is present", ok)
            test_passed &= ok

            # 4) Validate user name
            ok = compare_with_expected_crop("Images/Profile_Screen_User_Name.png")
            test_result.log_step("Profile User Name is present", ok)
            test_passed &= ok

            # 5) Validate 'My details' tab
            ok = compare_with_expected_crop("Images/Profile_Screen_MyDetails_Tab.png")  # ensure exact filename
            test_result.log_step("Profile 'My details' tab is present", ok)
            test_passed &= ok

            # 6) Navigate to Account
            ok = controller.click_by_image("Icons/Profile_Account_Icon.png", threshold=0.80)
            test_result.log_step("Tapped Account", ok)
            test_passed &= ok
            time.sleep(2)

            ok = compare_with_expected_crop("Images/Profile_Account_Screen.png")
            test_result.log_step("Profile Account screen is present", ok)
            test_passed &= ok

            # 7) Navigate to General
            ok = controller.click_by_image("Icons/Profile_General_Icon.png", threshold=0.80)
            test_result.log_step("Tapped General", ok)
            test_passed &= ok
            time.sleep(2)

            ok = compare_with_expected_crop("Images/Profile_General_Screen.png")
            test_result.log_step("Profile General screen is present", ok)
            test_passed &= ok

            # 8) Settings icon visible on Profile (if expected on this screen)
            ok = compare_with_expected_crop("Images/Profile_Screen_Setting_Icon.png")
            test_result.log_step("Profile Settings icon is present", ok)
            test_passed &= ok

            # Final status (kept for readability in the report)
            if test_passed:
                test_result.log("✅ Demo_Mode_008 passed")
                test_result.status = "Passed"
            else:
                test_result.log("❌ Demo_Mode_008 failed")
                test_result.status = "Failed"

            # Come back to my details tab in profile screen
            controller.click_by_image("Icons/Profile_Mydetails_Icon.png", threshold=0.80)

    except Exception as e:
        test_result.log_step(f"Unexpected error: {e}", False)

        test_result.end_time = time.time()
        return test_result



# def Remote_lock():
#     test_result = TestCaseResult("Remote_lock")
#     try:
#         controller.wake_up_unlock_screen()
#         controller.press_home()
#         controller.launch_app("uk.co.bentley.mybentley")
#         sleep(2)
#         test_result.log_step("App launched successfully", True)
#         actual_path = controller.take_screenshot("temp.png")
#         dashboard_visible = find_icon_in_screen("Images/My_Bentley_Dashboard.png", actual_path)
#         test_result.log_step("Dashboard screen detected", dashboard_visible)
#         icon_clicked = controller.click_by_image("Icons/lock_icon.png", threshold=0.85)
#         test_result.log_step("Lock icon clicked", icon_clicked)
#         locked = controller.enter_pin("1234")
#         sleep(2)
#         test_result.log_step("car got locked", locked)
#     except Exception as e:
#         test_result.log_step(f"Unexpected error: {e}", False)
#
#     # Final summary
#     test_result.finalize()
#
# def Remote_unlock():
#     test_result = TestCaseResult("Remote_unlock")
#     try:
#         controller.wake_up_unlock_screen()
#         controller.press_home()
#         controller.launch_app("uk.co.bentley.mybentley")
#         sleep(2)
#         test_result.log_step("App launched successfully", True)
#         actual_path = controller.take_screenshot("temp.png")
#         dashboard_visible = find_icon_in_screen("Images/My_Bentley_Dashboard.png", actual_path)
#         test_result.log_step("Dashboard screen detected", dashboard_visible)
#         icon_clicked = controller.click_by_image("Icons/unlock_icon.png", threshold=0.85)
#         test_result.log_step("Unlock icon clicked", icon_clicked)
#         locked = controller.enter_pin("1234", press_enter=False)
#         sleep(2)
#         test_result.log_step("car got locked", locked)
#     except Exception as e:
#         test_result.log_step(f"Unexpected error: {e}", False)
#
    # Final summary
#test_result.finalize()




