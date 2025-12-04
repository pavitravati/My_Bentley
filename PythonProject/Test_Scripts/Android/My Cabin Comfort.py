from common_utils.android_image_comparision import *
from core.log_emitter import log, fail_log, error_log, metric_log, blocked_log, runtime_log
from time import sleep
import re
from datetime import date, datetime
from core.app_functions import remote_swipe, app_login_setup, service_reset
from core.globals import manual_run, current_pin
from gui.manual_check import manual_check
import core.globals as globals
from core.screenrecord import ScreenRecorder

img_service = "My Cabin Comfort"
recorder = ScreenRecorder(device_serial=controller.d.serial)

def My_Cabin_Comfort_001():
    recorder.start(f"{img_service}-001")
    try:
        if app_login_setup():
            controller.click_by_image("Icons/remote_icon.png")
            remote_swipe("MY CABIN COMFORT")

            cabin_comfort = controller.d(text="MY CABIN COMFORT")
            status = cabin_comfort.sibling(resourceId="uk.co.bentley.mybentley:id/textView_status_car_remote_item")

            if cabin_comfort.exists:
                log("Cabin comfort section displayed")
                if status.exists and status.get_text() == "Not active":
                    log("Status is 'Not active'")
                else:
                    fail_log("Status is not 'Not active'", "001", img_service)
            else:
                fail_log("Cabin comfort section not displayed", "001", img_service)
            controller.swipe_down()

    except Exception as e:
        error_log(e, "001", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def My_Cabin_Comfort_002():
    recorder.start(f"{img_service}-002")
    try:
        if app_login_setup():
            controller.click_by_image("Icons/remote_icon.png")
            remote_swipe("MY CABIN COMFORT")

            if controller.click_text("MY CABIN COMFORT"):
                log("Cabin Comfort section clicked")
            else:
                fail_log("Cabin comfort section could not be found", "002", img_service)

            if controller.is_text_present("Quick start"):
                log("Quick start tab displayed")
                controller.click_by_image("Icons/timer_toggle_off.png")
                if controller.is_text_present("Rear left"):
                    globals.rear_seat_heating = True
            else:
                fail_log("Quick start tab not displayed", "002", img_service)

            if controller.is_text_present("Set timer"):
                log("Set timer tab displayed")
            else:
                fail_log("Set timer tab not displayed", "002", img_service)

            controller.click_by_image("Icons/back_icon.png")
            controller.swipe_down()

    except Exception as e:
        error_log(e, "002", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def My_Cabin_Comfort_003():
    recorder.start(f"{img_service}-003")
    try:
        if app_login_setup():

            controller.click_by_image("Icons/remote_icon.png")
            remote_swipe("MY CABIN COMFORT")

            if controller.click_text("MY CABIN COMFORT"):
                if controller.is_text_present("MY CABIN COMFORT"):
                    log("Cabin comfort title displayed")
                else:
                    fail_log("Cabin comfort title not displayed", "003", img_service)

                if controller.is_text_present("Prepare your Bentley in advance to keep you and all your passengers comfortable from the moment you step inside."):
                    log("Cabin comfort information displayed")
                else:
                    fail_log("Cabin comfort information not displayed", "003", img_service)

                if controller.is_text_present("Target temperature") and controller.d(className="android.widget.SeekBar").exists:
                    log("Target temperature bar displayed")
                else:
                    fail_log("Target temperature bar not displayed", "003", img_service)

                if controller.is_text_present("Interior surface heating") and compare_with_expected_crop("Icons/Interior_heating_toggle.png"):
                    log("Interior surface heating toggle displayed")
                else:
                    fail_log("Interior surface heating toggle not displayed", "003", img_service)

                if controller.is_text_present("START"):
                    log("Start button displayed")
                else:
                    fail_log("Start button not displayed", "003", img_service)
            else:
                fail_log("Cabin comfort section could not be found", "003", img_service)

            controller.click_by_image("Icons/back_icon.png")
            controller.swipe_down()

    except Exception as e:
        error_log(e, "003", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def My_Cabin_Comfort_004():
    recorder.start(f"{img_service}-004")
    try:
        if app_login_setup():
            if not globals.rear_seat_heating:
                blocked_log("Test blocked - Vehicle should support rear heating")
            else:
                controller.click_by_image("Icons/remote_icon.png")
                remote_swipe("MY CABIN COMFORT")

                if controller.click_text("MY CABIN COMFORT"):
                    if compare_with_expected_crop("Images/default_heating.png", 0.99):
                        log("Default seat heating options displayed")
                    else:
                        controller.click_by_image("Icons/Front_right_seat_disabled.png", 1)
                        controller.click_by_image("Icons/Front_left_seat_disabled.png", 1)
                        if compare_with_expected_crop("Images/default_heating.png", 0.99):
                            log("Default seat heating options displayed")
                        else:
                            fail_log("Default seat heating options not displayed", "004", img_service)

                    if controller.click_by_image("Icons/Rear_left_seat_disabled.png") and compare_with_expected_crop("Icons/Rear_left_seat_enabled.png", 0.99):
                        log("Rear seat heating options supported")
                    else:
                        fail_log("Rear seat heating options not supported", "004", img_service)

                else:
                    fail_log("Cabin comfort section could not be found", "004", img_service)

                controller.click_by_image("Icons/back_icon.png")
                controller.swipe_down()
    except Exception as e:
        error_log(e, "004", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

# this is tested using co-ords, so different phones may not work, can't think of another way to interact with bar
def My_Cabin_Comfort_005():
    recorder.start(f"{img_service}-005")
    temperatures = ["16", "17", "18", "19", "21"]
    try:
        if app_login_setup():
            if not globals.rear_seat_heating:
                blocked_log("Test blocked - Vehicle should support rear heating")
            else:
                controller.click_by_image("Icons/remote_icon.png")
                remote_swipe("MY CABIN COMFORT")

                if controller.click_text("MY CABIN COMFORT"):
                    for i in range(1, 6):
                        controller.click((100*i), 930)
                        cabin_comfort = controller.d(text="Target temperature")
                        temp = cabin_comfort.sibling(index="2").get_text()
                        if temp == f"{temperatures[i-1]}.0 °C":
                            log("Target temperature able to be set")
                        else:
                            fail_log("Target temperature unable to be set", "005", img_service)
                else:
                    fail_log("Cabin comfort section could not be found", "005", img_service)

                controller.click_by_image("Icons/back_icon.png")
                controller.swipe_down()
    except Exception as e:
        error_log(e, "005", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def My_Cabin_Comfort_006():
    recorder.start(f"{img_service}-006")
    try:
        if app_login_setup():
            if not globals.rear_seat_heating:
                blocked_log("Test blocked - Vehicle should support rear heating")
            else:
                if not int(globals.fuel_pct) >= 30:
                    blocked_log("Test blocked - Vehicle should have at least 30% Fuel")
                else:
                    controller.click_by_image("Icons/remote_icon.png")
                    remote_swipe("MY CABIN COMFORT")

                    if controller.click_text("MY CABIN COMFORT"):
                        controller.click(200, 930)
                        cabin_comfort = controller.d(text="Target temperature")
                        temp = cabin_comfort.sibling(index="2").get_text()
                        if temp == "17.0 °C":
                            log("Target temperature set successfully")
                        else:
                            fail_log("Target temperature not set", "006", img_service)

                        controller.click_by_image("Icons/Interior_heating_toggle.png")
                        if compare_with_expected_crop("Icons/timer_toggle_off.png"):
                            log("Interior heating disabled")
                        else:
                            fail_log("Interior heating not disabled", "006", img_service)

                        if controller.click_text("START"):
                            log("Start button clicked")
                        else:
                            fail_log("Start button not found", "006", img_service)
                        controller.wait_for_text("Sending message to car")
                        while controller.is_text_present("Sending message to car"):
                            sleep(0.5)
                        if controller.is_text_present("Successfully sent to car"):
                            log("Successfully sent to car status displayed")
                        else:
                            fail_log("Successfully sent to car status not displayed", "006", img_service)
                        controller.wait_for_text("My cabin comfort is active")
                        if controller.is_text_present("My cabin comfort is active") and controller.is_text_present("- 10 min"):
                            log("Active cabin comfort status displayed")
                        else:
                            fail_log("Active cabin comfort not displayed", "006", img_service)
                        controller.click_text("MY CABIN COMFORT")
                        if controller.is_text_present("STOP") and controller.is_text_present("Currently active"):
                            log("Stop button displayed when cabin comfort active")
                            manual_check(
                                instruction=f"Verify the time left matches remote RCP menu\nVerify MY CABIN COMFORT is active in the car",
                                test_id="006",
                                service=img_service,
                                take_screenshot=True
                            )
                            controller.click_text("STOP")
                        else:
                            fail_log("Stop button not found, or cabin comfort not active", "006", img_service)
                    else:
                        fail_log("Cabin comfort section could not be found", "006", img_service)

                    controller.click_text("STOP")
                    controller.wait_for_text("Not active")
                    controller.swipe_down()
    except Exception as e:
        error_log(e, "006", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def My_Cabin_Comfort_007():
    recorder.start(f"{img_service}-007")
    try:
        if app_login_setup():
            if not globals.rear_seat_heating:
                blocked_log("Test blocked - Vehicle should support rear heating")
            else:
                if not int(globals.fuel_pct) >= 30:
                    blocked_log("Test blocked - Vehicle should have at least 30% Fuel")
                else:
                    controller.click_by_image("Icons/remote_icon.png")
                    remote_swipe("MY CABIN COMFORT")

                    if controller.click_text("MY CABIN COMFORT"):
                        controller.click(300, 930)
                        cabin_comfort = controller.d(text="Target temperature")
                        temp = cabin_comfort.sibling(index="2").get_text()
                        if temp == "18.0 °C":
                            log("Target temperature set successfully")
                        else:
                            fail_log("Target temperature not set", "007", img_service)

                        controller.click_by_image("Icons/timer_toggle_off.png")
                        if compare_with_expected_crop("Icons/Interior_heating_toggle.png"):
                            log("Interior heating enabled")
                        else:
                            fail_log("Interior heating not disabled", "007", img_service)

                        if compare_with_expected_crop("Images/default_heating.png", 0.99):
                            log("Default seat heating options displayed")
                        else:
                            fail_log("Default seat heating options not displayed", "007", img_service)

                        if controller.click_by_image("Icons/Front_left_seat_enabled.png") and compare_with_expected_crop("Icons/Front_left_seat_disabled.png", 0.99) and compare_with_expected_crop("Icons/Front_right_seat_enabled.png", 0.99):
                            log("Driver seat heating enabled and passenger seat heating disabled successfully")
                        else:
                            fail_log("Driver seat heating enabled and passenger seat heating disabled unsuccessfully", "007", img_service)

                        if controller.click_text("START"):
                            log("Start button clicked")
                        else:
                            fail_log("Start button not found", "007", img_service)

                        controller.wait_for_text("Sending message to car")
                        while controller.is_text_present("Sending message to car"):
                            sleep(0.5)
                        if controller.is_text_present("Successfully sent to car"):
                            log("Successfully sent to car status displayed")
                        else:
                            fail_log("Successfully sent to car status not displayed", "007", img_service)
                        controller.wait_for_text("My cabin comfort is active")
                        if controller.is_text_present("My cabin comfort is active") and controller.is_text_present("- 10 min"):
                            log("Active cabin comfort status displayed")
                        else:
                            fail_log("Active cabin comfort not displayed", "007", img_service)
                        controller.click_text("MY CABIN COMFORT")
                        if controller.is_text_present("STOP") and controller.is_text_present("Currently active"):
                            log("Stop button displayed when cabin comfort active")
                            manual_check(
                                instruction=f"Verify the time left matches remote RCP menu\nVerify MY CABIN COMFORT is active in the car",
                                test_id="007",
                                service=img_service,
                                take_screenshot=True
                            )
                            controller.click_text("STOP")
                            while controller.is_text_present("Sending message to car"):
                                sleep(0.5)
                        else:
                            fail_log("Stop button not found, or cabin comfort not active", "007", img_service)
                    else:
                        fail_log("Cabin comfort section could not be found", "007", img_service)

                    controller.click_by_image("Icons/back_icon.png")
                    controller.swipe_down()

    except Exception as e:
        error_log(e, "007", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def My_Cabin_Comfort_008():
    recorder.start(f"{img_service}-008")
    try:
        if app_login_setup():
            if not globals.rear_seat_heating:
                blocked_log("Test blocked - Vehicle should support rear heating")
            else:
                if not int(globals.fuel_pct) >= 30:
                    blocked_log("Test blocked - Vehicle should have at least 30% Fuel")
                else:
                    controller.click_by_image("Icons/remote_icon.png")
                    remote_swipe("MY CABIN COMFORT")

                    if controller.click_text("MY CABIN COMFORT"):
                        controller.click(300, 930)
                        cabin_comfort = controller.d(text="Target temperature")
                        temp = cabin_comfort.sibling(index="2").get_text()
                        if temp == "18.0 °C":
                            log("Target temperature set successfully")
                        else:
                            fail_log("Target temperature not set", "008", img_service)

                        controller.click_by_image("Icons/timer_toggle_off.png")
                        if compare_with_expected_crop("Icons/Interior_heating_toggle.png"):
                            log("Interior heating enabled")
                        else:
                            fail_log("Interior heating not disabled", "008", img_service)

                        if compare_with_expected_crop("Images/default_heating.png", 0.99):
                            log("Default seat heating options displayed")
                        else:
                            fail_log("Default seat heating options not displayed", "008", img_service)

                        if controller.click_by_image("Icons/Front_right_seat_enabled.png") and compare_with_expected_crop("Icons/Front_right_seat_disabled.png", 0.99) and compare_with_expected_crop("Icons/Front_left_seat_enabled.png", 0.99):
                            log("Driver seat heating disabled and passenger seat heating enabled successfully")
                        else:
                            fail_log("Driver seat heating disabled and passenger seat heating enabled unsuccessfully", "008")

                        if controller.click_text("START"):
                            log("Start button clicked")
                        else:
                            fail_log("Start button not found", "008", img_service)

                        controller.wait_for_text("Sending message to car")
                        while controller.is_text_present("Sending message to car"):
                            sleep(0.5)
                        if controller.is_text_present("Successfully sent to car"):
                            log("Successfully sent to car status displayed")
                        else:
                            fail_log("Successfully sent to car status not displayed", "008", img_service)
                        controller.wait_for_text("My cabin comfort is active")
                        if controller.is_text_present("My cabin comfort is active") and controller.is_text_present("- 10 min"):
                            log("Active cabin comfort status displayed")
                        else:
                            fail_log("Active cabin comfort not displayed", "008", img_service)
                        controller.click_text("MY CABIN COMFORT")
                        if controller.is_text_present("STOP") and controller.is_text_present("Currently active"):
                            log("Stop button displayed when cabin comfort active")
                            manual_check(
                                instruction=f"Verify the time left matches remote RCP menu\nVerify MY CABIN COMFORT is active in the car",
                                test_id="008",
                                service=img_service,
                                take_screenshot=True
                            )
                            controller.click_text("STOP")
                            while controller.is_text_present("Sending message to car"):
                                sleep(0.5)
                        else:
                            fail_log("Stop button not found, or cabin comfort not active", "008", img_service)
                    else:
                        fail_log("Cabin comfort section could not be found", "008", img_service)

                    controller.click_by_image("Icons/back_icon.png")
                    controller.swipe_down()
    except Exception as e:
        error_log(e, "008", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def My_Cabin_Comfort_009():
    recorder.start(f"{img_service}-009")
    try:
        if app_login_setup():
            if not globals.rear_seat_heating:
                blocked_log("Test blocked - Vehicle should support rear heating")
            else:
                if not int(globals.fuel_pct) >= 30:
                    blocked_log("Test blocked - Vehicle should have at least 30% Fuel")
                else:
                    controller.click_by_image("Icons/remote_icon.png")
                    remote_swipe("MY CABIN COMFORT")

                    if controller.click_text("MY CABIN COMFORT"):
                        controller.click(300, 930)
                        cabin_comfort = controller.d(text="Target temperature")
                        temp = cabin_comfort.sibling(index="2").get_text()
                        if temp == "18.0 °C":
                            log("Target temperature set successfully")
                        else:
                            fail_log("Target temperature not set", "009", img_service)

                        controller.click_by_image("Icons/timer_toggle_off.png")
                        if compare_with_expected_crop("Icons/Interior_heating_toggle.png"):
                            log("Interior heating enabled")
                        else:
                            fail_log("Interior heating not disabled", "009", img_service)

                        if compare_with_expected_crop("Images/default_heating.png", 0.99):
                            log("Default seat heating options displayed")
                        else:
                            fail_log("Default seat heating options not displayed", "009", img_service)

                        if controller.click_by_image("Icons/Rear_left_seat_disabled.png") and controller.click_by_image("Icons/Front_right_seat_enabled.png") and controller.click_by_image("Icons/Front_left_seat_enabled.png") and compare_with_expected_crop("Images/Rear_left_enabled_only.png", 0.99):
                            log("Front seat heating disabled and rear left seat heating enabled successfully")
                        else:
                            fail_log("Front seat heating disabled and rear left seat heating enabled unsuccessfully", "009", img_service)

                        if controller.click_text("START"):
                            log("Start button clicked")
                        else:
                            fail_log("Start button not found", "009", img_service)

                        controller.wait_for_text("Sending message to car")
                        while controller.is_text_present("Sending message to car"):
                            sleep(0.5)
                        if controller.is_text_present("Successfully sent to car"):
                            log("Successfully sent to car status displayed")
                        else:
                            fail_log("Successfully sent to car status not displayed", "009", img_service)
                        controller.wait_for_text("My cabin comfort is active")
                        if controller.is_text_present("My cabin comfort is active") and controller.is_text_present("- 10 min"):
                            log("Active cabin comfort status displayed")
                        else:
                            fail_log("Active cabin comfort not displayed", "009", img_service)
                        controller.click_text("MY CABIN COMFORT")
                        if controller.is_text_present("STOP") and controller.is_text_present("Currently active"):
                            log("Stop button displayed when cabin comfort active")
                            manual_check(
                                instruction=f"Verify the time left matches remote RCP menu\nVerify MY CABIN COMFORT is active in the car",
                                test_id="009",
                                service=img_service,
                                take_screenshot=True
                            )
                            controller.click_text("STOP")
                            while controller.is_text_present("Sending message to car"):
                                sleep(0.5)
                        else:
                            fail_log("Stop button not found, or cabin comfort not active", "009", img_service)
                    else:
                        fail_log("Cabin comfort section could not be found", "009", img_service)

                    controller.click_by_image("Icons/back_icon.png")
                    controller.swipe_down()
    except Exception as e:
        error_log(e, "009", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def My_Cabin_Comfort_010():
    recorder.start(f"{img_service}-010")
    try:
        if app_login_setup():
            if not globals.rear_seat_heating:
                blocked_log("Test blocked - Vehicle should support rear heating")
            else:
                if not int(globals.fuel_pct) >= 30:
                    blocked_log("Test blocked - Vehicle should have at least 30% Fuel")
                else:
                    controller.click_by_image("Icons/remote_icon.png")
                    remote_swipe("MY CABIN COMFORT")

                    if controller.click_text("MY CABIN COMFORT"):
                        controller.click(300, 930)
                        cabin_comfort = controller.d(text="Target temperature")
                        temp = cabin_comfort.sibling(index="2").get_text()
                        if temp == "18.0 °C":
                            log("Target temperature set successfully")
                        else:
                            fail_log("Target temperature not set", "010", img_service)

                        controller.click_by_image("Icons/timer_toggle_off.png")
                        if compare_with_expected_crop("Icons/Interior_heating_toggle.png"):
                            log("Interior heating enabled")
                        else:
                            fail_log("Interior heating not disabled", "010", img_service)

                        if compare_with_expected_crop("Images/default_heating.png", 0.99):
                            log("Default seat heating options displayed")
                        else:
                            fail_log("Default seat heating options not displayed", "010", img_service)

                        if controller.click_by_image("Icons/Rear_right_seat_disabled.png") and controller.click_by_image("Icons/Front_right_seat_enabled.png") and controller.click_by_image("Icons/Front_left_seat_enabled.png") and compare_with_expected_crop("Images/Rear_right_enabled_only.png", 0.99):
                            log("Front seat heating disabled and rear right seat heating enabled successfully")
                        else:
                            fail_log("Front seat heating disabled and rear right seat heating enabled unsuccessfully", "010", img_service)

                        if controller.click_text("START"):
                            log("Start button clicked")
                        else:
                            fail_log("Start button not found", "010", img_service)

                        controller.wait_for_text("Sending message to car")
                        while controller.is_text_present("Sending message to car"):
                            sleep(0.5)
                        if controller.is_text_present("Successfully sent to car"):
                            log("Successfully sent to car status displayed")
                        else:
                            fail_log("Successfully sent to car status not displayed", "010", img_service)
                        controller.wait_for_text("My cabin comfort is active")
                        if controller.is_text_present("My cabin comfort is active") and controller.is_text_present("- 10 min"):
                            log("Active cabin comfort status displayed")
                        else:
                            fail_log("Active cabin comfort not displayed", "010", img_service)
                        controller.click_text("MY CABIN COMFORT")
                        if controller.is_text_present("STOP") and controller.is_text_present("Currently active"):
                            log("Stop button displayed when cabin comfort active")
                            manual_check(
                                instruction=f"Verify the time left matches remote RCP menu\nVerify MY CABIN COMFORT is active in the car",
                                test_id="010",
                                service=img_service,
                                take_screenshot=True
                            )
                            controller.click_text("STOP")
                            while controller.is_text_present("Sending message to car"):
                                sleep(0.5)
                        else:
                            fail_log("Stop button not found, or cabin comfort not active", "010", img_service)
                    else:
                        fail_log("Cabin comfort section could not be found", "010", img_service)

                    controller.click_by_image("Icons/back_icon.png")
                    controller.swipe_down()
    except Exception as e:
        error_log(e, "010", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def My_Cabin_Comfort_011():
    recorder.start(f"{img_service}-011")
    try:
        if app_login_setup():
            if not globals.rear_seat_heating:
                blocked_log("Test blocked - Vehicle should support rear heating")
            else:
                if not int(globals.fuel_pct) >= 30:
                    blocked_log("Test blocked - Vehicle should have at least 30% Fuel")
                else:
                    controller.click_by_image("Icons/remote_icon.png")
                    remote_swipe("MY CABIN COMFORT")

                    if controller.click_text("MY CABIN COMFORT"):
                        controller.click(300, 930)
                        cabin_comfort = controller.d(text="Target temperature")
                        temp = cabin_comfort.sibling(index="2").get_text()
                        if temp == "18.0 °C":
                            log("Target temperature set successfully")
                        else:
                            fail_log("Target temperature not set", "011", img_service)

                        controller.click_by_image("Icons/timer_toggle_off.png")
                        if compare_with_expected_crop("Icons/Interior_heating_toggle.png"):
                            log("Interior heating enabled")
                        else:
                            fail_log("Interior heating not disabled", "011", img_service)

                        if compare_with_expected_crop("Images/default_heating.png", 0.99):
                            log("Default seat heating options displayed")
                        else:
                            fail_log("Default seat heating options not displayed", "011", img_service)

                        if controller.click_by_image("Icons/Rear_right_seat_disabled.png") and controller.click_by_image("Icons/Rear_left_seat_disabled.png") and compare_with_expected_crop("Images/all_seats_enabled.png", 0.99):
                            log("Front seat heating disabled and rear right seat heating enabled successfully")
                        else:
                            fail_log("Front seat heating disabled and rear right seat heating enabled unsuccessfully", "011", img_service)

                        if controller.click_text("START"):
                            log("Start button clicked")
                        else:
                            fail_log("Start button not found", "011", img_service)

                        controller.wait_for_text("Sending message to car")
                        while controller.is_text_present("Sending message to car"):
                            sleep(0.5)
                        if controller.is_text_present("Successfully sent to car"):
                            log("Successfully sent to car status displayed")
                        else:
                            fail_log("Successfully sent to car status not displayed", "011", img_service)
                        controller.wait_for_text("My cabin comfort is active")
                        if controller.is_text_present("My cabin comfort is active") and controller.is_text_present("- 10 min"):
                            log("Active cabin comfort status displayed")
                        else:
                            fail_log("Active cabin comfort not displayed", "011", img_service)
                        controller.click_text("MY CABIN COMFORT")
                        if controller.is_text_present("STOP") and controller.is_text_present("Currently active"):
                            log("Stop button displayed when cabin comfort active")
                            manual_check(
                                instruction=f"Verify the time left matches remote RCP menu\nVerify MY CABIN COMFORT is active in the car",
                                test_id="011",
                                service=img_service,
                                take_screenshot=True
                            )
                            controller.click_text("STOP")
                            while controller.is_text_present("Sending message to car"):
                                sleep(0.5)
                        else:
                            fail_log("Stop button not found, or cabin comfort not active", "011", img_service)
                    else:
                        fail_log("Cabin comfort section could not be found", "010", img_service)

                    controller.click_by_image("Icons/back_icon.png")
                    controller.swipe_down()
    except Exception as e:
        error_log(e, "011", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def My_Cabin_Comfort_012():
    recorder.start(f"{img_service}-012")
    try:
        if app_login_setup():
            if not globals.rear_seat_heating:
                blocked_log("Test blocked - Vehicle should support rear heating")
            else:
                if not int(globals.fuel_pct) >= 30:
                    blocked_log("Test blocked - Vehicle should have at least 30% Fuel")
                else:
                    controller.click_by_image("Icons/remote_icon.png")
                    remote_swipe("MY CABIN COMFORT")

                    if controller.click_text("MY CABIN COMFORT"):
                        if controller.click_text("START"):
                            log("Start button clicked")
                            sleep(0.5)
                            while controller.is_text_present("Sending message to car"):
                                sleep(0.5)
                        controller.wait_for_text_and_click("My cabin comfort is active")

                    if controller.click_text("STOP"):
                        log("Stop button clicked")
                    else:
                        fail_log("Stop button not found", "012", img_service)

                    while controller.is_text_present("Sending message to car"):
                        sleep(0.5)
                    controller.wait_for_text("Not active")
                    controller.click_text("MY CABIN COMFORT")

                    if controller.istext_present("START"):
                        log("Stop button is now the start button")
                    else:
                        fail_log("Start button not found", "012", img_service)

                    controller.click_by_image("Icons/back_icon.png")
                    controller.swipe_down()
    except Exception as e:
        error_log(e, "012", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

# Verifying the timers exist is dodgy as no unique resource ids so used an image of the toggles and then returned the timers as metrics.
def My_Cabin_Comfort_013():
    recorder.start(f"{img_service}-013")
    try:
        if app_login_setup():
            controller.click_by_image("Icons/remote_icon.png")
            remote_swipe("MY CABIN COMFORT")

            if controller.click_text("MY CABIN COMFORT"):
                if controller.click_text("Set timer"):
                    log("Set timer tab clicked")
                else:
                    fail_log("Set timer tab not found", "013", img_service)

                if controller.is_text_present("MY CABIN COMFORT"):
                    log("Cabin comfort title displayed")
                else:
                    fail_log("Cabin comfort title not displayed", "013", img_service)

                if compare_with_expected_crop("Images/timer_toggles.png", 0.99):
                    log("Both timers displayed")
                    time_pattern = re.compile(r"^\d{2}:\d{2}$")
                    timers = {}
                    for i, node in enumerate(controller.d(className="android.widget.TextView")):
                        if time_pattern.match(node.get_text()):
                            time = node.get_text()
                            date = node[i + 1].get_text()
                            timers[time] = date
                    for i, (time, date) in enumerate(timers.items(), start=1):
                        metric_log(f"Timer {i}: {date} - {time}")
                else:
                    fail_log("Timers not displayed", "013", img_service)

                if controller.is_text_present("SETTINGS"):
                    log("Settings button displayed")
                else:
                    fail_log("Settings button not displayed", "013", img_service)

                if controller.d(text="SYNC TO CAR").exists:
                    log("Sync button displayed")
                    if compare_with_expected_crop("Icons/sync_button_disabled.png"):
                        controller.click_by_image("Icons/timer_toggle_off.png")
                        if compare_with_expected_crop("Icons/sync_button_enabled.png"):
                            log("Sync button only clickable when timer enabled")
                        else:
                            fail_log("Sync button not only clickable when timer enabled", "013", img_service)
                    else:
                        fail_log("Sync button not only clickable when timer enabled", "013", img_service)
                else:
                    fail_log("Sync button not displayed", "013", img_service)

            else:
                fail_log("Cabin comfort section could not be found", "013", img_service)

            controller.click_by_image("Icons/back_icon.png")
            controller.swipe_down()
    except Exception as e:
        error_log(e, "013", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def My_Cabin_Comfort_014():
    recorder.start(f"{img_service}-014")
    try:
        if app_login_setup():
            if not globals.rear_seat_heating:
                blocked_log("Test blocked - Vehicle should support rear heating")
            else:
                controller.click_by_image("Icons/remote_icon.png")
                remote_swipe("MY CABIN COMFORT")

                if controller.click_text("MY CABIN COMFORT"):
                    if controller.click_text("Set timer"):
                        if controller.click_text("SETTINGS"):
                            log("Settings button clicked")
                            if controller.is_text_present("Interior surface heating") and compare_with_expected_crop("Icons/Interior_heating_toggle.png"):
                                log("Interior surface heating toggle displayed")
                            else:
                                fail_log("Interior surface heating not displayed", "014", img_service)

                            if compare_with_expected_crop("Images/default_heating.png", 0.985):
                                log("Default seat heating options displayed")
                            else:
                                fail_log("Default seat heating not displayed", "014", img_service)

                            controller.click_by_image("Icons/Interior_heating_toggle.png")
                            if not compare_with_expected_crop("Images/default_heating.png", 0.99):
                                log("Default seat heating options hidden when heating tis toggled off")
                            else:
                                fail_log("Default seat heating options not hidden when heating tis toggled off", "014")
                        else:
                            fail_log("Settings button not clicked", "014", img_service)
                    else:
                        fail_log("Set timer tab not found", "014", img_service)
                else:
                    fail_log("Cabin comfort section could not be found", "014", img_service)

                controller.click_by_image("Icons/back_icon.png")
                controller.click_by_image("Icons/back_icon.png")
                controller.swipe_down()
    except Exception as e:
        error_log(e, "014", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def My_Cabin_Comfort_015():
    recorder.start(f"{img_service}-015")
    try:
        if app_login_setup():
            if not int(globals.fuel_pct) >= 30:
                blocked_log("Test blocked - Vehicle should have at least 30% Fuel")
            else:
                controller.click_by_image("Icons/remote_icon.png")
                remote_swipe("MY CABIN COMFORT")

                if controller.click_text("MY CABIN COMFORT"):
                    controller.click_text("Quick start")
                    controller.click_by_image("Icons/Interior_heating_toggle.png")
                    if compare_with_expected_crop("Icons/timer_toggle_off.png"):
                        log("Interior heating disabled in Quick start")
                    else:
                        fail_log("Interior heating not disabled in Quick start", "015", img_service)
                    if controller.click_text("Set timer"):
                        controller.click_text("SETTINGS")
                        controller.click_by_image("Icons/Interior_heating_toggle.png")
                        if compare_with_expected_crop("Icons/timer_toggle_off.png"):
                            log("Interior heating disabled in timer settings")
                        else:
                            fail_log("Interior heating not disabled in timer settings", "015", img_service)
                        controller.click_by_image("Icons/back_icon.png")

                        controller.click_by_image("Icons/timer_toggle_off.png")
                        controller.click_text("SYNC TO CAR")
                        sleep(0.5)
                        controller.enter_pin(current_pin)
                        sleep(0.5)
                        while controller.is_text_present("Sending message to car"):
                            sleep(0.5)
                        if controller.is_text_present("Successfully sent to car"):
                            log("Successfully sent to car status displayed")
                        else:
                            fail_log("Successfully sent to car status not displayed", "015", img_service)
                        if controller.wait_for_text("My cabin comfort scheduled"):
                            log("My cabin comfort scheduled status displayed")
                        else:
                            fail_log("My cabin comfort scheduled status not displayed", "015", img_service)

                        # Removes the timers
                        count=0
                        while True:
                            count+=1
                            controller.click_text("MY CABIN COMFORT")
                            controller.click_text("Set timer")
                            controller.click_by_image("Icons/Interior_heating_toggle.png")
                            controller.click_by_image("Icons/Interior_heating_toggle.png")
                            controller.click_text("SYNC TO CAR")
                            while controller.is_text_present("Sending message to car"):
                                sleep(0.5)
                            if controller.is_text_present("Successfully sent to car"):
                                break
                            # Stop infinite loop
                            if count > 5:
                                break

                    else:
                        fail_log("Set timer tab not found", "015", img_service)
                else:
                    fail_log("Cabin comfort section could not be found", "015", img_service)

                controller.click_by_image("Icons/back_icon.png")
                controller.swipe_down()
    except Exception as e:
        error_log(e, "015", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def My_Cabin_Comfort_016():
    recorder.start(f"{img_service}-016")
    try:
        if app_login_setup():
            if not int(globals.fuel_pct) >= 30:
                blocked_log("Test blocked - Vehicle should have at least 30% Fuel")
            else:
                controller.click_by_image("Icons/remote_icon.png")
                remote_swipe("MY CABIN COMFORT")

                if controller.click_text("MY CABIN COMFORT"):
                    controller.click_text("Quick start")
                    controller.click(300, 930)
                    cabin_comfort = controller.d(text="Target temperature")
                    temp = cabin_comfort.sibling(index="2").get_text()
                    if temp == "18.0 °C":
                        log("Target temperature set successfully")
                    else:
                        fail_log("Target temperature not set", "016", img_service)
                    controller.click_by_image("Icons/timer_toggle_off.png")
                    if compare_with_expected_crop("Icons/Interior_heating_toggle.png"):
                        log("Interior heating enabled in Quick start")
                    else:
                        fail_log("Interior heating not enabled in Quick start", "016", img_service)
                    if controller.click_text("Set timer"):
                        controller.click_text("SETTINGS")
                        controller.click_by_image("Icons/timer_toggle_off.png")
                        if compare_with_expected_crop("Icons/Interior_heating_toggle.png"):
                            log("Interior heating enabled in timer settings")
                        else:
                            fail_log("Interior heating not enabled in timer settings", "016", img_service)
                        controller.click_by_image("Icons/back_icon.png")

                        controller.click_by_image("Icons/timer_toggle_off.png")
                        controller.click_text("SYNC TO CAR")
                        sleep(0.5)
                        while controller.is_text_present("Sending message to car"):
                            sleep(0.5)
                        if controller.is_text_present("Successfully sent to car"):
                            log("Successfully sent to car status displayed")
                        else:
                            fail_log("Successfully sent to car status not displayed", "016", img_service)
                        if controller.wait_for_text("My cabin comfort scheduled"):
                            log("My cabin comfort scheduled status displayed")
                        else:
                            fail_log("My cabin comfort scheduled status not displayed", "016", img_service)

                        # Removes the timers
                        count = 0
                        while True:
                            count += 1
                            controller.click_text("MY CABIN COMFORT")
                            controller.click_text("Set timer")
                            controller.click_by_image("Icons/Interior_heating_toggle.png")
                            controller.click_by_image("Icons/Interior_heating_toggle.png")
                            controller.click_text("SYNC TO CAR")
                            while controller.is_text_present("Sending message to car"):
                                sleep(0.5)
                            if controller.is_text_present("Successfully sent to car"):
                                break
                            # Stop infinite loop
                            if count > 5:
                                fail_log("Failed to remove timer to allow for automation")
                                break

                    else:
                        fail_log("Set timer tab not found", "015", img_service)
                else:
                    fail_log("Cabin comfort section could not be found", "015", img_service)

                controller.click_by_image("Icons/back_icon.png")
                controller.swipe_down()
    except Exception as e:
        error_log(e, "016", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def My_Cabin_Comfort_017():
    recorder.start(f"{img_service}-017")
    try:
        if app_login_setup():
            manual_check(
                instruction="Set a cabin comfort timer from the vehicle with target temp between 16degC and 26degC and no seat heating\nNow click on 'Temperature - Icon' under 'Immediate Start' section",
                test_id="017",
                service=img_service,
                take_screenshot=False
            )
            controller.click_by_image("Icons/remote_icon.png")
            remote_swipe("MY CABIN COMFORT")
            cabin_comfort = controller.d(text="MY CABIN COMFORT")
            status = cabin_comfort.sibling(resourceId="uk.co.bentley.mybentley:id/textView_status_car_remote_item")
            # Check what status would be
            if status.get_text() == "My cabin comfort is active":
                log("Cabin comfort Status displayed correctly")
            else:
                fail_log("Cabin comfort status not displayed correctly", "017", img_service)
            # Validate 4
            controller.click_text("MY CABIN COMFORT")
            controller.click_text("Set timer")
            manual_check(
                instruction=f"Verify the timer details are what was set in the car",
                test_id="017",
                service=img_service,
                take_screenshot=True
            )
            controller.click_by_image("Icons/Interior_heating_toggle.png")
            controller.click_by_image("Icons/Interior_heating_toggle.png")
            controller.click_text("SYNC TO CAR")
            while controller.is_text_present("Sending message to car"):
                sleep(0.5)
            if not controller.is_text_present("Successfully sent to car"):
                # Removes the timers
                count = 0
                while True:
                    count += 1
                    controller.click_text("MY CABIN COMFORT")
                    controller.click_text("Set timer")
                    controller.click_by_image("Icons/Interior_heating_toggle.png")
                    controller.click_by_image("Icons/Interior_heating_toggle.png")
                    controller.click_text("SYNC TO CAR")
                    while controller.is_text_present("Sending message to car"):
                        sleep(0.5)
                    if controller.is_text_present("Successfully sent to car"):
                        break
                    # Stop infinite loop
                    if count > 5:
                        fail_log("Failed to remove timer to allow for automation")
                        break

            controller.click_by_image("Icons/back_icon.png")
            controller.swipe_down()
    except Exception as e:
        error_log(e, "017", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def My_Cabin_Comfort_018():
    try:
        blocked_log("Test blocked - Can't be automated")
        manual_check(
            instruction="""'Climate - Auxiliary climate' screen should be launched(HMI->Climate->"Climate" screen launched->Select settings button->"Climate - Settings" screen launched->Select "Auxiliary Climate"->"Climate - Auxiliary climate" launched) displaying:
            \nScreen Title: 'Climate - Auxiliary climate'\n'Immediate Start' section: 'Temperature - Icon' button: Clicking on it should activate 'MY CABIN COMFORT'
            \n'Timer Programming' section: Timer 1 & 2 with selection box, clicking them should launch 'Climate - Departure date' screen where user can select
            departure date and a continue button\n'Settings' button: Clicking it should launch 'Climate - Settings' screen where
            user can set:\na. Screen Title: Climate Settings\nb. 'Target Temperature' section: Target Temperature can be set to desired
            value by user in range 16degC to 26degC with 1degC increments/decrements\nc. 'Start climate control after unlocking':
            User can tick/untick for enabling/disabling this option\nd. 'Convenience auxiliary climate' section: User can select/deselect the seat
            heating for all 4 seating zones(Front Right/Front Left/Rear Right/Rear Left)\ne. 'Back' button: Clicking it
            takes focus back to 'Climate - Auxiliary Climate' screen\n'Back' button: Screen focus is taken one step back to 'Climate - Settings' screen""",
            test_id="018",
            service=img_service,
            take_screenshot=False
        )
    except Exception as e:
        error_log(e, "018", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def My_Cabin_Comfort_019():
    recorder.start(f"{img_service}-019")
    try:
        if app_login_setup():
            manual_check(
                instruction="Select 'Settings' button in 'Climate - Auxiliary climate' screen\nGo to 'Target Temperature' section and set the target temperature in the range between 16degC to 26degC with 1degC increments / decrements under (Ex : 22degC)\nSelect the desired seat selection for Seat Heating under 'Convenience auxiliary climate' section(Ex : Rear Right Seat Zone)\nClick on 'Back' button\nClick on 'Temperature - Icon' button under 'Immediate Start' section in 'Climate - Auxiliary Climate' screen",
                test_id="019",
                service=img_service,
                take_screenshot=False
            )
            controller.click_by_image("Icons/remote_icon.png")
            remote_swipe("MY CABIN COMFORT")
            cabin_comfort = controller.d(text="MY CABIN COMFORT")
            status = cabin_comfort.sibling(resourceId="uk.co.bentley.mybentley:id/textView_status_car_remote_item")
            time = cabin_comfort.sibling(resourceId="uk.co.bentley.mybentley:id/textView_info_car_remote_item")
            if status.get_text() == "My cabin comfort is active":
                log("Active cabin comfort status displayed")
            else:
                fail_log("Active cabin comfort status not displayed", "019", img_service)
            controller.click_text("MY CABIN COMFORT")
            controller.click_text("Set timer")
            controller.click_text("SETTINGS")
            manual_check(
                instruction="Verify the Interior surface heating is toggled to what was set in the car",
                test_id="019",
                service=img_service,
                take_screenshot=True
            )
            controller.click_by_image("Icons/back_icon.png")
            controller.click_by_image("Icons/back_icon.png")
            controller.swipe_down()
    except Exception as e:
        error_log(e, "019", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def My_Cabin_Comfort_020():
    recorder.start(f"{img_service}-020")
    try:
        if app_login_setup():
            controller.click_by_image("Icons/remote_icon.png")
            remote_swipe("MY CABIN COMFORT")
            controller.click_text("MY CABIN COMFORT")
            controller.click_text("START")
            controller.wait_for_text("Sending message to car")
            while controller.is_text_present("Sending message to car"):
                sleep(0.5)
            manual_check(
                instruction="Make sure 'MY CABIN COMFORT' is active under 'Climate - Auxiliary climate' screen\nIf not, it has been sent by the app so wait for that or manually activate",
                test_id="020",
                service=img_service,
                take_screenshot=False
            )
            sleep(1)
            manual_check(
                instruction="Click on 'Temperature - Icon' button under 'Immediate Start' section in 'Climate - Auxiliary Climate' screen to deactivate",
                test_id="020",
                service=img_service,
                take_screenshot=False
            )
            controller.click_by_image("Icons/remote_icon.png")
            remote_swipe("MY CABIN COMFORT")
            cabin_comfort = controller.d(text="MY CABIN COMFORT")
            status = cabin_comfort.sibling(resourceId="uk.co.bentley.mybentley:id/textView_status_car_remote_item")
            if status.get_text() == "Not active":
                log("Not active status displayed correctly")
            else:
                fail_log("Not active status not displayed", "020", img_service)
            controller.swipe_down()
    except Exception as e:
        error_log(e, "020", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def My_Cabin_Comfort_021():
    recorder.start(f"{img_service}-021")
    try:
        if app_login_setup():
            manual_check(
                instruction="1. Select either 'Timer-1'/'Timer-2' under 'Timer Programming' section of 'Climate - Auxiliary climate' screen\nSelect 'Timer-1'/'Timer-2' and select the 'Departure date'(Ex : Sun 30 July 2023) and press 'Continue' button\nNow set the 'Departure time'(Ex: 30.07.2023 :: 11:05) and press 'Ok' button\nNotice that the recently updated timer('Timer-1'/'Timer-2') is ticked\nNote: Set a specific temperature and desired seat heating so it can be compared to the app",
                test_id="021 ",
                service=img_service,
                take_screenshot=True
            )
            controller.click_by_image("Icons/remote_icon.png")
            remote_swipe("MY CABIN COMFORT")
            cabin_comfort = controller.d(text="MY CABIN COMFORT")
            status = cabin_comfort.sibling(resourceId="uk.co.bentley.mybentley:id/textView_status_car_remote_item")
            time = cabin_comfort.sibling(resourceId="uk.co.bentley.mybentley:id/textView_info_car_remote_item")
            if status.get_text() == "My cabin comfort scheduled":
                log("Cabin comfort scheduled status displayed correctly")
            else:
                fail_log("Cabin comfort scheduled status not displayed correctly", "021", img_service)
            manual_check(
                instruction=f"Verify the scheduled time in the status is correct",
                test_id="021",
                service=img_service,
                take_screenshot=True
            )
            controller.click_text("MY CABIN COMFORT")
            controller.click_text("Quick start")
            manual_check(
                instruction=f"Verify the temperature and Interior surface heating section are what was set in the car",
                test_id="021",
                service=img_service,
                take_screenshot=True
            )
            controller.click_by_image("Icons/back_icon.png")
            controller.swipe_down()
    except Exception as e:
        error_log(e, "021", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def set_new_timer(index, testcase_idx):
    controller.click_by_resource_id("uk.co.bentley.mybentley:id/textView_date_rpc_timer_setting")
    controller.click_by_image("Icons/Homescreen_Right_Arrow.png")
    current_date = str(datetime.now())
    today = int(current_date[8:10])
    tomorrow = today + 1 if today < 27 else 1
    if tomorrow == 1:
        controller.click_by_image("Icons/Homescreen_Right_Arrow.png")
    controller.click_by_text_id(str(tomorrow))
    controller.click_text("OK")
    time = int(current_date[11:13])
    new_time = time + 1 if time < 23 else 0
    while controller.d(resourceId="uk.co.bentley.mybentley:id/textView_time_rpc_timer_setting").get_text() != f"{str(new_time)}:{"40" if index==1 else "45"}":
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/textView_time_rpc_timer_setting")
        controller.click_by_content_desc(str(new_time))
        controller.click_by_content_desc("40") if index == 1 else controller.click_by_content_desc("45")
        controller.click_text("OK")
    if controller.click_text("Save"):
        log("Timer set")
    else:
        fail_log("Timer not set", testcase_idx, img_service)

# Clicking co-ords as I can find no way to click the timer
def My_Cabin_Comfort_022():
    recorder.start(f"{img_service}-022")
    try:
        if app_login_setup():
            if not int(globals.fuel_pct) >= 30:
                blocked_log("Test blocked - Vehicle should have at least 30% Fuel")
            else:
                controller.click_by_image("Icons/remote_icon.png")
                remote_swipe("MY CABIN COMFORT")

                if controller.click_text("MY CABIN COMFORT"):
                    if controller.click_text("Set timer"):
                        # set first timer
                        controller.click(500, 520)
                        set_new_timer(1, "022")
                        # set second timer
                        controller.click(500, 720)
                        set_new_timer(1, "022")
                        if controller.is_text_present("Duplicate timer"):
                            log("Duplicate timer warning message displayed")
                        else:
                            fail_log("Duplicate timer warning message not displayed", "022", img_service)
                        controller.click_text("OK")
                        controller.click_by_image("Icons/login_page_x.png")
                    else:
                        fail_log("Set timer tab not found", "022", img_service)
                else:
                    fail_log("Cabin comfort section could not be found", "022", img_service)

                controller.click_by_image("Icons/back_icon.png")
                controller.swipe_down()
    except Exception as e:
        error_log(e, "022", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def My_Cabin_Comfort_023():
    recorder.start(f"{img_service}-023")
    try:
        if app_login_setup():
            if not int(globals.fuel_pct) >= 30:
                blocked_log("Test blocked - Vehicle should have at least 30% Fuel")
            else:
                controller.click_by_image("Icons/remote_icon.png")
                remote_swipe("MY CABIN COMFORT")

                if controller.click_text("MY CABIN COMFORT"):
                    if controller.click_text("Set timer"):
                        controller.click(500, 520)
                        set_new_timer(1, "023")
                        controller.click(500, 720)
                        set_new_timer(2, "023")
                        controller.click_text("SYNC TO CAR")
                        sleep(0.5)
                        while controller.is_text_present("Sending message to car"):
                            sleep(0.5)
                        cabin_comfort = controller.d(text="MY CABIN COMFORT")
                        status = cabin_comfort.sibling(resourceId="uk.co.bentley.mybentley:id/textView_status_car_remote_item")
                        if status:
                            log("Successfully sent to car status displayed")
                        else:
                            fail_log("Successfully sent to car status not displayed", "023", img_service)
                        controller.wait_for_text("My cabin comfort is active")
                        cabin_comfort = controller.d(text="MY CABIN COMFORT")
                        status = cabin_comfort.sibling(resourceId="uk.co.bentley.mybentley:id/textView_status_car_remote_item")
                        if status:
                            log("Scheduled timer status displayed")
                        else:
                            fail_log("Scheduled timer status not displayed", "023", img_service)
                    else:
                        fail_log("Set timer tab not found", "023", img_service)
                else:
                    fail_log("Cabin comfort section could not be found", "023", img_service)

                controller.click_by_image("Icons/back_icon.png")
                controller.swipe_down()
    except Exception as e:
        error_log(e, "023", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def My_Cabin_Comfort_024():
    recorder.start(f"{img_service}-024")
    try:
        blocked_log("Test blocked - Can't check style guide")
    except Exception as e:
        error_log(e, "024", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False
