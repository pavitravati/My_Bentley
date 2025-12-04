from common_utils.android_image_comparision import *
from core.log_emitter import log, fail_log, error_log, metric_log, blocked_log, runtime_log
from time import sleep
from core.app_functions import remote_swipe, app_login_setup, app_refresh, service_reset
from core.globals import manual_run, vehicle_type
from core.screenrecord import ScreenRecorder
from core import globals

img_service = "Privacy Mode"
recorder = ScreenRecorder(device_serial=controller.d.serial)

def Privacy_Mode_001():
    recorder.start(f"{img_service}-001")
    try:
        if app_login_setup():
            app_refresh("001", img_service)
            if controller.find_img("Icons/Remote_Lock_Unavailable_Icon.png", 0.75):
                log("Remote lock unlock unavailable")
            elif controller.find_img("Icons/lock_icon.png", 0.75):
                fail_log("Remote lock unlock still available", "001", img_service)

            if controller.is_text_present("My car status unavailable"):
                log("Car status information disabled")
            else:
                fail_log("Car status information still available", "001", img_service)

            controller.click_by_image("Icons/remote_icon.png")
            section_titles = []
            for _ in range(2):
                titles = controller.d.xpath('//android.widget.TextView[''following-sibling::*//*[@text="Function disabled" or @text="Function not available"]]').all()
                section_titles.append([t.attrib.get("text", "") for t in titles if t.attrib.get("text") not in section_titles])
                if _ == 0:
                    controller.swipe_up(0.25)

            section_titles = section_titles[0] + section_titles[1]
            log("My car statistics disabled") if "MY CAR STATISTICS" in section_titles else fail_log("My car statistics not disabled", "001", img_service)
            log("My battery charge disabled") if "MY BATTERY CHARGE" in section_titles else fail_log("My battery charge not disabled", "001", img_service)
            log("My cabin comfort disabled") if "MY CABIN COMFORT" in section_titles else fail_log("My cabin comfort not disabled", "001", img_service)
            log("Remote parking disabled") if "REMOTE PARKING" in section_titles else fail_log("Remote parking not disabled", "001", img_service)

            # check for ice
            log("Theft alarm disabled") if compare_with_expected_crop("Icons/theft_alarm_disabled.png") else fail_log("Theft alarm not disabled", "001", img_service)
            # controller.click_text("STOLEN VEHICLE TRACKING")
            # if compare_with_expected_crop("Icons/privacy_mode_error.png"):
            #     log("Theft alert disabled")
            # else:
            #     fail_log("Theft alert not disabled", "001", img_service)
            # controller.click_by_image("Icons/back_icon.png")
            # controller.swipe_down(0.1)

            controller.click_by_image("Icons/navigation_icon.png")
            controller.click_by_image("Images/Navigation_Allow.png")
            if not controller.d(resourceId="uk.co.bentley.mybentley:id/imageButton_layout_map_button").exists:
                log("Vehicle location not accessible")
            else:
                fail_log("Vehicle location still accessible", "001", img_service)

    except Exception as e:
        error_log(e, "001", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Privacy_Mode_002():
    recorder.start(f"{img_service}-002")
    try:
        if app_login_setup():
            app_refresh("002", img_service)
            if compare_with_expected_crop("Icons/Remote_Lock_Grey.png", 0.9):
                log("Remote lock unlock unavailable when privacy mode activated")
            else:
                fail_log("Remote lock unlock failed to be disabled when privacy mode activated", "002", img_service)

    except Exception as e:
        error_log(e, "002", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Privacy_Mode_003():
    recorder.start(f"{img_service}-003")
    try:
        if vehicle_type == "phev":
            if app_login_setup():
                app_refresh("003", img_service)
                controller.click_by_image("Icons/remote_icon.png")
                remote_swipe("MY CABIN COMFORT")
                if compare_with_expected_crop("Images/cabin_comfort_disabled.png"):
                    log("Cabin comfort disabled in privacy mode")
                else:
                    fail_log("Cabin comfort not disabled in privacy mode", "003", img_service)

                controller.swipe_down()
        else:
            blocked_log("Test blocked - vehicle must be a phev")
    except Exception as e:
        error_log(e, "003", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Privacy_Mode_004():
    recorder.start(f"{img_service}-004")
    try:
        if vehicle_type == "phev":
            if app_login_setup():
                # app_refresh("004", img_service)
                controller.click_by_image("Icons/remote_icon.png")
                if compare_with_expected_crop("Images/batterycharge_disabled.png"):
                    log("My battery charge service disabled in privacy mode")
                else:
                    fail_log("My battery charge service not disabled in privacy mode", "004", img_service)
        else:
            blocked_log("Test blocked - vehicle must be a phev")
    except Exception as e:
        error_log(e, "004", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Privacy_Mode_005():
    recorder.start(f"{img_service}-005")
    try:
        if app_login_setup():
            app_refresh("005", img_service)

            controller.click_by_image("Icons/navigation_icon.png")
            controller.click_by_image("Images/Navigation_Allow.png")

            if not controller.d(resourceId="uk.co.bentley.mybentley:id/imageButton_layout_map_button").exists:
                log("Find my car icon not displayed when privacy mode activated")
            else:
                fail_log("Find my car icon displayed when privacy mode activated", "005", img_service)

            markers = controller.d.xpath('//*[@content-desc="Map Marker"]').all()
            driver_icon_bounds = []
            for i in range(len(markers)):
                driver_icon_bounds.append(markers[i].center())
                if i == 1:
                    break
            for i in range(len(driver_icon_bounds)):
                controller.click(driver_icon_bounds[i][0], driver_icon_bounds[i][1])
                if controller.is_text_present("PLAN ROUTE"):
                    fail_log("Car location marker still shown in privacy mode", "005", img_service)
                    controller.click(500, 500)
                    controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
                    return
    except Exception as e:
        error_log(e, "005", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Privacy_Mode_006():
    recorder.start(f"{img_service}-006")
    try:
        if vehicle_type == "phev":
            if app_login_setup():
                app_refresh("006", img_service)
                controller.click_by_image("Icons/remote_icon.png")
                if compare_with_expected_crop("Images/carstatistics_disabled.png"):
                    log("My car statistics service disabled in remote screen")
                else:
                    fail_log("My car statistics service not disabled in remote screen", "006", img_service)
                    controller.click(110,110)
        else:
            blocked_log("Test blocked - vehicle must be a phev")
    except Exception as e:
        error_log(e, "006", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Privacy_Mode_007():
    recorder.start(f"{img_service}-007")
    try:
        blocked_log("Test blocked - Cannot be automated")
        # controller.click_by_image("Icons/remote_icon.png")
        # if remote_swipe("ROADSIDE ASSISTANCE"):
        #     if controller.click_text("ROADSIDE ASSISTANCE"):
        #         log("Roadside assistance section clicked")
        #         controller.click_text("CALL NOW")
        #         manual_check(
        #             instruction="""Verify Breakdown Call initiation Form My Bentley App\nTry to establish call to the region specific contact number
        #                             \nTwo way communication between Agent and Customer should be successful and call should end without issues""",
        #             test_id="007",
        #             service=img_service,
        #             take_screenshot=False
        #         )
        #         service_reset()
    except Exception as e:
        error_log(e, "007", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

# The next 3 test cases all have actions to be done/checked in the HMI
def Privacy_Mode_008():
    recorder.start(f"{img_service}-008")
    try:
        if app_login_setup():
            app_refresh("008", img_service)
            if controller.find_img("Icons/Remote_Lock_Unavailable_Icon.png", 0.75):
                log("Remote lock unlock unavailable")
            elif controller.find_img("Icons/lock_icon.png", 0.75):
                fail_log("Remote lock unlock still available", "008", img_service)

            if controller.is_text_present("My car status unavailable"):
                log("Car status information disabled")
            else:
                fail_log("Car status information still available", "008", img_service)

            controller.click_by_image("Icons/remote_icon.png")
            section_titles = []
            for _ in range(2):
                titles = controller.d.xpath('//android.widget.TextView[''following-sibling::*//*[@text="Function disabled" or @text="Function not available"]]').all()
                section_titles.append([t.attrib.get("text", "") for t in titles if t.attrib.get("text") not in section_titles])
                if _ == 0:
                    controller.swipe_up(0.25)

            section_titles = section_titles[0] + section_titles[1]
            log("My car statistics disabled") if "MY CAR STATISTICS" in section_titles else fail_log("My car statistics not disabled", "008", img_service)
            log("My battery charge disabled") if "MY BATTERY CHARGE" in section_titles else fail_log("My battery charge not disabled", "008", img_service)
            log("My cabin comfort disabled") if "MY CABIN COMFORT" in section_titles else fail_log("My cabin comfort not disabled", "008", img_service)
            log("Remote parking disabled") if "REMOTE PARKING" in section_titles else fail_log("Remote parking not disabled", "008", img_service)

            # check for ice
            log("Theft alarm disabled") if compare_with_expected_crop("Icons/theft_alarm_disabled.png") else fail_log("Theft alarm not disabled", "008", img_service)
            # controller.click_text("STOLEN VEHICLE TRACKING")
            # if compare_with_expected_crop("Icons/privacy_mode_error.png"):
            #     log("Theft alert disabled")
            # else:
            #     fail_log("Theft alert not disabled", "008", img_service)
            # controller.click_by_image("Icons/back_icon.png")
            controller.swipe_down(0.1)

            controller.click_by_image("Icons/navigation_icon.png")
            controller.click_by_image("Images/Navigation_Allow.png")
            if not controller.d(resourceId="uk.co.bentley.mybentley:id/imageButton_layout_map_button").exists:
                log("Vehicle location not accessible")
            else:
                fail_log("Vehicle location still accessible", "008", img_service)

    except Exception as e:
        error_log(e, "008", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Privacy_Mode_009():
    recorder.start(f"{img_service}-009")
    try:
        if app_login_setup():
            app_refresh("009", img_service)

            controller.click_by_image("Icons/navigation_icon.png")
            controller.click_by_image("Images/Navigation_Allow.png")
            if not controller.d(resourceId="uk.co.bentley.mybentley:id/imageButton_layout_map_button").exists:
                log("Vehicle location not accessible")
            else:
                fail_log("Vehicle location still accessible", "009", img_service)
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

            if controller.find_img("Icons/Remote_Lock_Unavailable_Icon.png", 0.75):
                log("Remote lock unlock unavailable")
            elif controller.find_img("Icons/lock_icon.png", 0.75):
                fail_log("Remote lock unlock still available", "009", img_service)

            if not controller.is_text_present("My car status unavailable"):
                log("Car status information accessible")
            else:
                fail_log("Car status information still unavailable", "009", img_service)

            controller.click_by_image("Icons/remote_icon.png")
            section_titles = []
            for _ in range(2):
                titles = controller.d.xpath('//android.widget.TextView[''following-sibling::*//*[@text="Function disabled" or @text="Function not available"]]').all()
                section_titles.append([t.attrib.get("text", "") for t in titles if t.attrib.get("text") not in section_titles])
                if _ == 0:
                    controller.swipe_up(0.25)

            section_titles = section_titles[0] + section_titles[1]
            log("My car statistics accessible") if "MY CAR STATISTICS" not in section_titles else fail_log("My car statistics still disabled", "009", img_service)
            log("My battery charge accessible") if "MY BATTERY CHARGE" not in section_titles else fail_log("My battery charge still disabled", "009", img_service)
            log("My cabin comfort accessible") if "MY CABIN COMFORT" not in section_titles else fail_log("My cabin comfort still disabled", "009", img_service)
            log("Remote parking accessible") if "REMOTE PARKING" not in section_titles else fail_log("Remote parking still disabled", "009", img_service, img_service)

            # check for ice
            log("Theft alarm accessible") if not compare_with_expected_crop("Icons/theft_alarm_disabled.png") else fail_log("Theft alarm still disabled", "009", img_service)
            # controller.click_text("STOLEN VEHICLE TRACKING")
            # if not compare_with_expected_crop("Icons/privacy_mode_error.png"):
            #     log("Theft alert not disabled")
            # else:
            #     fail_log("Theft alert still disabled", "009", img_service)
            # controller.click_by_image("Icons/back_icon.png")
            controller.swipe_down(0.1)

    except Exception as e:
        error_log(e, "009", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Privacy_Mode_010():
    recorder.start(f"{img_service}-010")
    try:
        if app_login_setup():
            app_refresh("010", img_service)

            controller.click_by_image("Icons/navigation_icon.png")
            controller.click_by_image("Images/Navigation_Allow.png")
            if not controller.d(resourceId="uk.co.bentley.mybentley:id/imageButton_layout_map_button").exists:
                log("Vehicle location not accessible")
            else:
                fail_log("Vehicle location still accessible", "010", img_service)
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

            if controller.find_img("Icons/lock_icon.png", 0.75):
                log("Remote lock unlock available")
            elif controller.find_img("Icons/Remote_Lock_Unavailable_Icon.png", 0.75):
                fail_log("Remote lock unlock unavailable", "010", img_service)

            if not controller.is_text_present("My car status unavailable"):
                log("Car status information accessible")
            else:
                fail_log("Car status information still unavailable", "010", img_service)

            controller.click_by_image("Icons/remote_icon.png")
            section_titles = []
            for _ in range(2):
                titles = controller.d.xpath(
                    '//android.widget.TextView[''following-sibling::*//*[@text="Function disabled" or @text="Function not available"]]').all()
                section_titles.append(
                    [t.attrib.get("text", "") for t in titles if t.attrib.get("text") not in section_titles])
                if _ == 0:
                    controller.swipe_up(0.25)

            section_titles = section_titles[0] + section_titles[1]
            log("My car statistics accessible") if "MY CAR STATISTICS" not in section_titles else fail_log(
                "My car statistics still disabled", "010", img_service)
            log("My battery charge accessible") if "MY BATTERY CHARGE" not in section_titles else fail_log(
                "My battery charge still disabled", "010", img_service)
            log("My cabin comfort accessible") if "MY CABIN COMFORT" not in section_titles else fail_log(
                "My cabin comfort still disabled", "010", img_service)
            log("Remote parking accessible") if "REMOTE PARKING" not in section_titles else fail_log(
                "Remote parking still disabled", "010", img_service)

            # check for ice
            log("Theft alarm accessible") if not compare_with_expected_crop("Icons/theft_alarm_disabled.png") else fail_log("Theft alarm still disabled", "010", img_service)
            # controller.click_text("STOLEN VEHICLE TRACKING")
            # if not compare_with_expected_crop("Icons/privacy_mode_error.png"):
            #     log("Theft alert not disabled")
            # else:
            #     fail_log("Theft alert still disabled", "010", img_service)
            # controller.click_by_image("Icons/back_icon.png")
            controller.swipe_down(0.1)

    except Exception as e:
            error_log(e, "010", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Privacy_Mode_011():
    recorder.start(f"{img_service}-011")
    try:
        if app_login_setup():
            # app_refresh("011", img_service)

            controller.click_by_image("Icons/navigation_icon.png")
            controller.click_by_image("Images/Navigation_Allow.png")
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/imageButton_layout_map_button")

            if not controller.d(resourceId="uk.co.bentley.mybentley:id/imageButton_layout_map_button").exists:
                log("Find my car icon displayed when privacy mode deactivated")
            else:
                fail_log("Find my car icon not displayed when privacy mode deactivated", "011", img_service)

            markers = controller.d.xpath('//*[@content-desc="Map Marker"]').all()
            driver_icon_bounds = []
            for i in range(len(markers)):
                driver_icon_bounds.append(markers[i].center())
                if i == 1:
                    break
            for i in range(len(driver_icon_bounds)):
                controller.click(driver_icon_bounds[i][0], driver_icon_bounds[i][1])
                if controller.is_text_present("PLAN ROUTE"):
                    fail_log("Car location marker still shown in privacy mode", "011", img_service)
                    controller.click(500, 500)
                    return

    except Exception as e:
        error_log(e, "011", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Privacy_Mode_012():
    recorder.start(f"{img_service}-012")
    try:
        if vehicle_type == "phev":
            if app_login_setup():
                app_refresh("012", img_service)
                controller.click_by_image("Icons/remote_icon.png")
                controller.click_text("MY CAR STATISTICS")
                if controller.is_text_present("Graphical view"):
                    log("My car statistics screen accessible")
                    controller.click(110,110)
                else:
                    fail_log("My car statistics screen not accessible", "012", img_service)
        else:
            blocked_log("Test blocked - Vehicle must be a phev")
    except Exception as e:
        error_log(e, "012", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Privacy_Mode_013():
    recorder.start(f"{img_service}-013")
    try:
        blocked_log("Test blocked - Can't check style guide")
    except Exception as e:
        error_log(e, "013", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False