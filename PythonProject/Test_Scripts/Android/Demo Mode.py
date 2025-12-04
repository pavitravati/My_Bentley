from time import sleep
from common_utils.android_image_comparision import *
from core.globals import current_email
from core.log_emitter import log, fail_log, metric_log, error_log, blocked_log, runtime_log
from core.app_functions import app_logout_setup, app_login, app_login_setup, dash_check, service_reset
from core import globals
from core.screenrecord import ScreenRecorder
from gui.manual_check import manual_check

img_service = "Demo Mode"
recorder = ScreenRecorder(device_serial=controller.d.serial)

def Demo_Mode_001():
    recorder.start(f"{img_service}-001")
    try:
        # if app_logout_setup():
        #     if controller.wait_for_text_and_click("DISCOVER MY BENTLEY"):
        #         log("Demo Mode link clicked")
        #     else:
        #         fail_log("Demo Mode link not found", "001", img_service)
        #     sleep(1)
        #
        #     if find_icon_in_screen("Images/My_Bentley_Demo_Mode_Page.png"):
        #         log("Demo Mode Launched successfully")
        #     else:
        #         fail_log("Dashboard screen not detected", "001", img_service)
        fail_log("test", "001", img_service)

    except Exception as e:
        error_log(e, "001", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Demo_Mode_002():
    recorder.start(f"{img_service}-002")
    try:
        if not controller.wait_for_text("Demo mode"):
            app_logout_setup()
            app_login_setup(True)

        if controller.wait_for_text("Demo mode"):
            if find_icon_in_screen("Images/My_Bentley_Demo_Mode_Page.png"):
                log("Demo mode dashboard visible")
            else:
                fail_log("Dashboard screen not detected", "002", img_service)
    except Exception as e:
        error_log(e, "002", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False


def Demo_Mode_003():
    recorder.start(f"{img_service}-003")
    try:
        if not controller.is_text_present("Demo mode"):
            app_logout_setup()
            app_login_setup(True)
        else:
            dash_check()

        if controller.wait_for_text("Demo mode"):
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

            log("Demo Mode dashboard visible") if controller.is_text_present("DASHBOARD") else fail_log("Demo Mode dashboard not visible", "003", img_service)
            log("Vehicle image displayed") if compare_with_expected_crop("Images/Demo_Vehicle_Image.png", 0.9) else fail_log("Vehicle image not displayed", "003", img_service)
            log("Greeting message displayed") if controller.wait_for_text_that_contains("Good", 3) else fail_log("Greeting message not displayed", "003", img_service)
            log("Vehicle name displayed") if controller.wait_for_text("BENTAYGA", 3) else fail_log("Vehicle name not displayed", "003", img_service)
            log("Last contact message displayed") if controller.wait_for_text_that_contains("Last vehicle contact", 3) else fail_log("Last contact message displayed", "003", img_service)
            if (compare_with_expected_crop("Images/Demo_Lock.png", 0.9) and compare_with_expected_crop("Images/Demo_Unlock.png", 0.9)) or (compare_with_expected_crop("Images/Demo_Lock_2.png", 0.9) and compare_with_expected_crop("Images/Demo_Unlock_2.png", 0.9)):
                log("Demo lock and unlock button displayed")
            else:
                fail_log("Demo lock and unlock buttons not displayed", "003", img_service)

            metrics = []
            for _ in range(2):
                controller.swipe_up()
                extracted = controller.extract_dashboard_metrics()
                metrics.extend(extracted.items())

            if metrics:
                metric_log("Extracted Metrics:\n")
                for metric, stat in metrics:
                    metric_log(f"{metric}: {stat}")
            else:
                fail_log("Metrics not extracted", "003", img_service)

            for _ in range(2):
                controller.swipe_down()
    except Exception as e:
        error_log(e, "003", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Demo_Mode_004():
    recorder.start(f"{img_service}-004")
    try:
        if not controller.is_text_present("Demo mode"):
            app_logout_setup()
            app_login_setup(True)
        else:
            dash_check()

        if controller.wait_for_text("Demo mode"):
            controller.click_by_image("Icons/remote_icon.png")
            sleep(1)
            if find_icon_in_screen("Images/Demo_Mode_Car_Remote_Screen.png"):
                log("Car Remote screen visible")
            else:
                fail_log("Car Remote screen not visible", "004", img_service)

            remote_images = [
                "Images/Demo_Remote/statistics.png",
                "Images/Demo_Remote/battery.png",
                "Images/Demo_Remote/comfort.png",
                "Images/Demo_Remote/parking.png",
                "Images/Demo_Remote/alarm.png",
                "Images/Demo_Remote/assistance.png",
                "Images/Demo_Remote/data.png",
                "Images/Demo_Remote/audials.png",
            ]

            log("My car statistics displayed") if compare_with_expected_crop(remote_images[0], 0.9) else fail_log("My car statistics not displayed", "004", img_service)
            log("My battery charge displayed") if compare_with_expected_crop(remote_images[1], 0.9) else fail_log("My battery charge not displayed", "004", img_service)
            controller.small_swipe_up()
            log("My cabin comfort displayed") if compare_with_expected_crop(remote_images[2], 0.9) else fail_log("My cabin comfort not displayed", "004", img_service)
            log("Remote parking displayed") if compare_with_expected_crop(remote_images[3], 0.9) else fail_log("Remote parking not displayed", "004", img_service)
            controller.small_swipe_up()
            log("Theft alarm displayed") if compare_with_expected_crop(remote_images[4], 0.9) else fail_log("Theft alarm not displayed", "004", img_service)
            if not compare_with_expected_crop(remote_images[5]):
                controller.extra_small_swipe_up()
            log("Roadside assistance displayed") if compare_with_expected_crop(remote_images[5], 0.9) else fail_log("Roadside assistance not displayed", "004", img_service)
            controller.swipe_up()
            log("Data services displayed") if compare_with_expected_crop(remote_images[6], 0.9) else fail_log("Data services not displayed", "004", img_service)
            log("Audials displayed") if compare_with_expected_crop(remote_images[7], 0.9) else fail_log("Audials not displayed", "004", img_service)

            for _ in range(2):
                controller.swipe_down(0.1)
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "004", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Demo_Mode_005():
    recorder.start(f"{img_service}-005")
    try:
        if not controller.is_text_present("Demo mode"):
            app_logout_setup()
            app_login_setup(True)
        else:
            dash_check()

        if controller.wait_for_text("Demo mode"):
            controller.click_by_image("Icons/remote_icon.png")
            sleep(1)
            if controller.click_text("MY BATTERY CHARGE"):
                screen_text = ['MY BATTERY CHARGE', 'Battery charge', 'Set timer', 'Battery status', 'Time remaining', 'QUICK START']
                text_present = True
                for text in screen_text:
                    if not controller.is_text_present(text):
                        text_present = False
                        fail_log(f"text: '{text}' not displayed", "005", img_service)

                if text_present:
                    log("My Battery Charge screen and details displayed")
                else:
                    fail_log("My Battery Charge screen and details not displayed correctly", "005", img_service)
            else:
                fail_log("My Battery Charge not displayed in remote screen", "005", img_service)

            controller.click_by_image("Icons/back_icon.png")
            controller.click_by_image("Icons/home_icon.png")
    except Exception as e:
        error_log(e, "005", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Demo_Mode_006():
    recorder.start(f"{img_service}-006")
    try:
        if not controller.is_text_present("Demo mode"):
            app_logout_setup()
            app_login_setup(True)
        else:
            dash_check()

        if controller.wait_for_text("Demo mode"):
            controller.click_by_image("Icons/navigation_icon.png")
            controller.click_text("ALLOW")

            if compare_with_expected_crop("Images/Navigation_Search_Image.png"):
                log("Navigation search image matched")
            else:
                fail_log("Search image not matched", "006", img_service)

            if controller.d(resourceId="uk.co.bentley.mybentley:id/tab_vehicle_dashboard").exists:
                log("Car icon is visible")
            else:
                fail_log("Car icon is missing", "006", img_service)

            if controller.d(resourceId="uk.co.bentley.mybentley:id/tab_profile").exists:
                log("Profile icon is visible")
            else:
                fail_log("Profile icon is missing", "006", img_service)

            controller.click_by_image("Icons/satellite_icon.png")
            sleep(1)
            if compare_with_expected_crop("Images/Satellite_Traffic_Screen.png"):
                log("Satellite traffic screen matched")
            else:
                fail_log("Satellite traffic screen did not match", "006", img_service)

            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "006", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Demo_Mode_007():
    recorder.start(f"{img_service}-007")
    try:
        if not controller.is_text_present("Demo mode"):
            app_logout_setup()
            app_login_setup(True)
        else:
            dash_check()

        if controller.wait_for_text("Demo mode"):
            controller.click_by_image("Icons/New_Notification_icon.png")
            controller.click_by_image("Icons/Notification_icon.png")
            sleep(1)
            if compare_with_expected_crop("Images/Notification_Title.png"):
                log("Notification title validated")
            else:
                fail_log("Notification title not validated", "007", img_service)

            metrics = controller.extract_dashboard_metrics()
            if metrics:
                metric_log("Extracted Metrics:\n")
                for metric, stat in metrics.items():
                    metric_log(f"{metric}: {stat}")
                    break
            else:
                fail_log("No Metrics extracted", "007", img_service)

            notif_details = ['Bentayga locked', '1 March 11:05', 'Bentayga was successfully locked', 'Continental GT unlocked', '1 May 11:29', 'Continental GT was successfully unlocked']
            notif_displayed = True
            for detail in notif_details:
                if not controller.is_text_present(detail):
                    notif_displayed = False

            if notif_displayed:
                log("Notifications are displayed")
            else:
                fail_log("Notifications are not displayed", "007", img_service)

            if controller.is_text_present("Actions") and controller.click_text("Alerts"):
                log("Actions and Alerts tabs displayed")
            else:
                fail_log("Actions and Alerts tabs not displayed", "007", img_service)

            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "007", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Demo_Mode_008():
    recorder.start(f"{img_service}-008")
    try:
        if not controller.is_text_present("Demo mode"):
            app_logout_setup()
            app_login_setup(True)
        else:
            dash_check()

        if controller.wait_for_text("Demo mode"):
            if controller.click_by_image("Icons/Profile_Icon.png"):
                log("Tapped Profile tab")
            else:
                fail_log("Profile tab not tapped", "008", img_service)

            if compare_with_expected_crop("Images/Profile_Screen.png"):
                log("Profile Title is present")
            else:
                fail_log("Profile Title is not present", "008", img_service)

            if compare_with_expected_crop("Images/Profile_Screen_User_Icon.png"):
                log("Profile User Icon is present")
            else:
                fail_log("Profile User Icon is not present", "008", img_service)

            if compare_with_expected_crop("Images/Profile_Screen_User_Name.png"):
                log("Profile User Name is present")
            else:
                fail_log("Profile User Name is not present", "008", img_service)

            if compare_with_expected_crop("Images/Profile_Screen_MyDetails_Tab.png"):
                log("Profile 'My details' tab is present")
            else:
                fail_log("Profile 'My details' tab is not present", "008", img_service)

            if controller.click_by_image("Icons/Profile_Account_Icon.png"):
                log("Tapped Account")
            else:
                fail_log("Account not tapped", "008", img_service)

            if compare_with_expected_crop("Images/Profile_Account_Screen.png"):
                log("Profile Account screen is present")
            else:
                fail_log("Profile Account screen is not present", "008", img_service)

            if controller.click_by_image("Icons/Profile_General_Icon.png"):
                log("Tapped General")
            else:
                fail_log("General not tapped", "008", img_service)

            if compare_with_expected_crop("Images/Profile_General_Screen.png"):
                log("Profile General screen is present")
            else:
                fail_log("Profile General screen is not present", "008", img_service)

            if compare_with_expected_crop("Images/Profile_Screen_Setting_Icon.png"):
                log("Profile Settings icon is present")
            else:
                fail_log("Profile Settings icon is not present", "008", img_service)

            controller.click_text("My Details")
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "008", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Demo_Mode_009():
    recorder.start(f"{img_service}-009")
    try:
        if not controller.is_text_present("Demo mode"):
            app_logout_setup()
            app_login_setup(True)
        else:
            dash_check()

        if controller.wait_for_text("Demo mode"):
            controller.click_by_image("Icons/Profile_Icon.png")
            controller.click_by_image("Icons/Profile_Screen_Setting_Icon.png")
            log("User tracking section displayed") if controller.is_text_present("User tracking") else fail_log("User tracking section not displayed", "009", img_service)
            log("Google maps consent section displayed") if controller.is_text_present("User tracking") else fail_log("Google maps consent section not displayed", "009", img_service)
            log("Units section displayed") if controller.is_text_present("User tracking") else fail_log("Units section not displayed", "009", img_service)
            log("Permissions section displayed") if controller.is_text_present("User tracking") else fail_log("Permissions section not displayed", "009", img_service)
            if controller.is_text_present("User tracking") and compare_with_expected_crop("Icons/Interior_heating_toggle.png"):
                log("Last mile notification section and toggle displayed")
            else:
                fail_log("Last mile notification section and toggle not displayed", "009", img_service)

            controller.click_by_image("Icons/back_icon.png")
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "009", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Demo_Mode_010():
    recorder.start(f"{img_service}-010")
    try:
        if not controller.is_text_present("Demo mode"):
            app_logout_setup()
            app_login_setup(True)
        else:
            dash_check()

        if controller.wait_for_text("Demo mode"):
            for _ in range(4):
                controller.click_by_image("Icons/Homescreen_Right_Arrow.png")

            if compare_with_expected_crop("Images/Add_Vehicle_Information_Screen.png"):
                log("Vehicle info Screen options are present")
            else:
                fail_log("Vehicle info Screen options not present", "010", img_service)

            controller.click_by_image("Icons/info_btn.png")
            if controller.is_text_present("Locating your VIN"):
                log("Locating VIN information displayed")
            else:
                fail_log("Locating VIN information not displayed", "010", img_service)
            controller.click_text("OK")

            controller.swipe_up()
            if controller.is_text_present("ADD A VEHICLE"):
                log("Add vehicle button displayed")
            else:
                fail_log("Add vehicle button not displayed", "010", img_service)
            controller.small_swipe_down()

            for _ in range(4):
                controller.click_by_image("Icons/Homescreen_Left_Arrow.png")

            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "010", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Demo_Mode_011():
    recorder.start(f"{img_service}-011")
    try:
        blocked_log("Test blocked - Can't check style guide")
    except Exception as e:
        error_log(e, "011", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Demo_Mode_012():
    recorder.start(f"{img_service}-012")
    try:
        if not controller.is_text_present("Demo mode"):
            app_logout_setup()
            app_login_setup(True)
        else:
            dash_check()

        if controller.wait_for_text("Demo mode"):
            controller.click_by_image("Icons/Profile_Icon.png")
            compare_with_expected_crop("Images/Profile_Screen.png")
            controller.click_by_image("Icons/Profile_General_Icon.png")
            compare_with_expected_crop("Images/Profile_General_Screen.png")
            if controller.click_text("Log out"):
                log("Demo mode exiting")
            else:
                fail_log("Demo mode not exiting", "012", img_service)
            sleep(2)

            if controller.wait_for_text_and_click("DISCOVER MY BENTLEY", 30):
                log("Sign in page is visible")
            else:
                fail_log("Sign in page not visible", "012", img_service)
            controller.wait_for_text("Demo mode", 30)
    except Exception as e:
        error_log(e, "012", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Demo_Mode_013():
    recorder.start(f"{img_service}-013")
    try:
        if not controller.is_text_present("Demo mode"):
            app_logout_setup()
            app_login_setup(True)
        else:
            dash_check()

        if controller.wait_for_text("Demo mode"):
            if controller.click_by_image("Icons/logout_icon.png"):
                log("Demo mode exiting")
            else:
                fail_log("Demo mode not exiting", "013", img_service)
            sleep(1)
            if controller.wait_for_text("DISCOVER MY BENTLEY", 30):
                log("Sign in page is visible")
            else:
                fail_log("Sign in page is visible", "013", img_service)

            if not globals.manual_run and current_email != "":
                app_login()
    except Exception as e:
        error_log(e, "013", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Demo_Mode_014():
    recorder.start(f"{img_service}-014")
    try:
        blocked_log("Test blocked - Can't check style guide")
    except Exception as e:
        error_log(e, "014", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False