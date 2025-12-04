from common_utils.android_image_comparision import *
from core.app_functions import app_login_setup, service_reset
from core.log_emitter import log, fail_log, error_log, metric_log, blocked_log, runtime_log
from time import sleep
from datetime import datetime
from core.globals import manual_run
from gui.manual_check import manual_check
from core.screenrecord import ScreenRecorder
from core import globals

img_service = "My Battery Charge"
recorder = ScreenRecorder(device_serial=controller.d.serial)

def extract_battery_status():
    metrics = []
    metrics.append(f"Charging status: {controller.d(resourceId="uk.co.bentley.mybentley:id/textView_charging_state_rbc_charge_state").get_text()}")
    metrics.append("Battery progress bar displayed" if controller.d(resourceId="uk.co.bentley.mybentley:id/arcProgressBarView_rbc_charge_state").info.get("enabled") else "Battery progress bar not displayed")
    metrics.append(f"Battery percentage: {controller.d(resourceId="uk.co.bentley.mybentley:id/textView_battery_status_percentage_rbc_charge_state").get_text()}")
    metrics.append(f"Estimated charging time: {controller.d(resourceId="uk.co.bentley.mybentley:id/textView_charge_time_rbc_charge_state").get_text()}")
    return metrics

# Make sure that these actually do the preconditions
def charger_schedule_check(turn_off=False, turn_on=False, timer_switch=False):
    controller.click_by_image("Icons/remote_icon.png")
    controller.click_text("MY BATTERY CHARGE")
    controller.click_text("Set timer")
    if compare_with_expected_crop("Icons/Interior_heating_toggle.png"):
        if turn_off:
            while compare_with_expected_crop("Icons/Interior_heating_toggle.png"):
                controller.click_by_image("Icons/Interior_heating_toggle.png.png")
            controller.click_text("SYNC TO CAR")
            timeout_check = 0
            while not controller.is_text_present("Successfully sent to car"):
                sleep(0.5)
                timeout_check += 1
                if timeout_check > 80:
                    break
            if controller.is_text_present("Successfully sent to car"):
                return True
            else:
                return False
        else:
            return True
    elif turn_on:
        controller.click_by_image("Icons/timer_toggle_off.png")
        controller.click_text("SYNC TO CAR")
        timeout_check = 0
        while not controller.is_text_present("Successfully sent to car"):
            sleep(0.5)
            timeout_check += 1
            if timeout_check > 80:
                break
        if controller.is_text_present("Successfully sent to car"):
            if timer_switch:
                controller.click_text("MY BATTERY CHARGE")
                controller.click_text("Battery charge")
                controller.click_text("SWITCH TO TIMER MODE")
            return True
        else:
            return False
    else:
        if timer_switch:
            controller.click_text("Battery charge")
            controller.click_text("SWITCH TO TIMER MODE")
        return False if not turn_off else True

def My_Battery_Charge_001():
    recorder.start(f"{img_service}-001")
    try:
        if app_login_setup():
            controller.click_by_image("Icons/remote_icon.png")
            if compare_with_expected_crop("Images/my_battery_charge.png") or compare_with_expected_crop("Images/my_battery_charge_greyed.png"):
                log("My battery charge section displayed correctly")
            else:
                fail_log("My battery charge section failed to be displayed", "001", img_service)

            metric = controller.d.xpath('//*[@resource-id="uk.co.bentley.mybentley:id/textView_status_car_remote_item"]').all()
            metric_log(f"Charging status: {metric[1].text}")
    except Exception as e:
        error_log(e, "001", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def My_Battery_Charge_002():
    recorder.start(f"{img_service}-002")
    try:
        if app_login_setup():
            # Why is a timer needed to be set?
            if not charger_schedule_check(False, True, True):
                manual_check(
                    instruction="Make sure that car there is a RBC Charge Timer scheduled and timer mode enabled",
                    test_id="002",
                    service=img_service,
                    take_screenshot=False
                )
            controller.click_by_image("Icons/remote_icon.png")
            controller.click_text("MY BATTERY CHARGE")

            if controller.is_text_present("Set timer"):
                log("My battery charge service opened")
                log("My battery charge title displayed") if controller.is_text_present("MY BATTERY CHARGE") else fail_log("My battery charge title not displayed", "002", img_service)
                battery_status = extract_battery_status()
                if len(battery_status) == 4:
                    log("My battery charge status displayed")
                else:
                    fail_log("My battery charge status not displayed", "002", img_service)
                for metric in battery_status:
                    metric_log(metric)
                if controller.is_text_present("QUICK START"):
                    log("Quick start button displayed")
                else:
                    fail_log("Quick start button not displayed", "002", img_service)

                if controller.click_text("Set timer"):
                    log("Set timer tab clicked")
                    log("My battery charge title displayed in 'Set timer' section") if controller.is_text_present("MY BATTERY CHARGE") else fail_log("My battery charge title not displayed in 'Set timer' section", "002")
                    if compare_with_expected_crop("Images/timer_toggles_battery.png"):
                        log("Both timers displayed and toggleable")
                    elif compare_with_expected_crop("Images/timer_toggle.png"):
                        fail_log("One timer missing, other displayed and toggleable", "002", img_service)
                    else:
                        fail_log("Timers not displayed", "002", img_service)
                else:
                    fail_log("Set timer tab not found", "002", img_service)
                controller.click_by_image("icons/back_icon.png")
            else:
                fail_log("My battery charge service failed to open", "002", img_service)
    except Exception as e:
        error_log(e, "002", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def My_Battery_Charge_003():
    recorder.start(f"{img_service}-003")
    try:
        if app_login_setup():
            if not charger_schedule_check(False, True, True):
                manual_check(
                    instruction="Make sure that car there is a RBC Charge Timer scheduled and timer mode enabled",
                    test_id="003",
                    service=img_service,
                    take_screenshot=False
                )
            controller.click_by_image("Icons/remote_icon.png")
            controller.click_text("MY BATTERY CHARGE")

            if controller.click_text("QUICK START"):
                log("Quick start button clicked")
            else:
                fail_log("Quick start button not found", "003", img_service)
            sleep(1)

            if controller.is_text_present("Sending message to car"):
                log("Quick start sent to the car")
            else:
                fail_log("Quick start not sent to the car", "003", img_service)
            timeout_check = 0
            while not controller.is_text_present("Successfully sent to car"):
                sleep(0.5)
                timeout_check += 1
                if timeout_check > 80:
                    break

            if controller.is_text_present("Successfully sent to car"):
                log("Quick start successfully sent to the car")
            else:
                fail_log("Quick start not sent to the car", "003", img_service)

            controller.click_text("MY BATTERY CHARGE")

            if controller.wait_for_text("SWITCH TO TIMER MODE"):
                log("Quick start button now displays 'SWITCH TO TIMER MODE' after clicked")
            else:
                fail_log("'SWITCH TO TIMER MODE' button not displayed after Quick start button clicked", "003", img_service)
            controller.click_by_image("icons/back_icon.png")
            manual_check(
                instruction=f"Verify the battery has started charging and status displayed in kombi",
                test_id="003",
                service=img_service,
                take_screenshot=False
            )
    except Exception as e:
        error_log(e, "003", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def My_Battery_Charge_004():
    recorder.start(f"{img_service}-004")
    try:
        if app_login_setup():
            if not charger_schedule_check(False, True):
                manual_check(
                    instruction=f"Make sure that car there is a RBC Charge Timer scheduled",
                    test_id="004",
                    service=img_service,
                    take_screenshot=False
                )
            controller.click_by_image("Icons/remote_icon.png")
            controller.click_text("MY BATTERY CHARGE")
            if manual_run:
                if controller.click_text("QUICK START"):
                    timeout_check = 0
                    while not controller.is_text_present("Successfully sent to car"):
                        sleep(0.5)
                        timeout_check += 1
                        if timeout_check > 80:
                            break
                    controller.click_text("MY BATTERY CHARGE")

            if controller.click_text("SWITCH TO TIMER MODE"):
                log("Timer mode button clicked")
            else:
                fail_log("Timer mode button not found", "004", img_service)
            sleep(1)

            if controller.is_text_present("Sending message to car"):
                log("Timer mode sent to the car")
            else:
                fail_log("Timer mode not sent to the car", "004", img_service)
            timeout_check = 0
            while not controller.is_text_present("Successfully sent to car"):
                sleep(0.5)
                timeout_check += 1
                if timeout_check > 80:
                    break

            if controller.is_text_present("Successfully sent to car"):
                log("Timer mode successfully sent to the car")
            else:
                fail_log("Timer mode not sent to the car", "004", img_service)

            controller.click_text("MY BATTERY CHARGE")

            if controller.wait_for_text("QUICK START"):
                log("Timer mode button now displays 'QUICK START' after clicked")
            else:
                fail_log("'QUICK START' button not displayed after Timer mode button clicked", "004", img_service)
            controller.click_by_image("icons/back_icon.png")
            manual_check(
                instruction=f"Verify charging status not displayed in kombi",
                test_id="004",
                service=img_service,
                take_screenshot=False
            )
    except Exception as e:
        error_log(e, "004", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def My_Battery_Charge_005():
    recorder.start(f"{img_service}-005")
    try:
        blocked_log("Test blocked - Selecting days does not work")
        # if app_login_setup():
        #     if not charger_schedule_check(True):
        #         manual_check(
        #             instruction=f"Make sure that car there is no RBC Charge Timer scheduled",
        #             test_id="006",
        #             service=img_service,
        #             take_screenshot=False
        #         )
            # controller.click_by_image("Icons/remote_icon.png")
            # controller.click_text("MY BATTERY CHARGE")
            # controller.click_text("Set timer")
            #
            # if not controller.d(resourceId="uk.co.bentley.mybentley:id/switch_rbc_timer_item").info.get("checked"):
            #     if controller.click_by_resource_id("uk.co.bentley.mybentley:id/switch_rbc_timer_item"):
            #         log("Timer enabled")
            # else:
            #     log("Timer is enabled")
            #
            # controller.click(500, 520)
            # if controller.is_text_present("EDIT TIMER"):
            #     log("Timer opened and editable")
            # else:
            #     fail_log("Timer not opened or editable", "005", img_service)
            #
            # controller.click_by_resource_id("uk.co.bentley.mybentley:id/textView_periodic_time_rbc_timer_setting")
            # sleep(0.2)
            # controller.click_by_content_desc("13")
            # sleep(0.2)
            # controller.click_by_content_desc("0")
            # sleep(0.2)
            # controller.click_text("OK")
            # if controller.is_text_present("13:00"):
            #     log("Time set to correct time")
            # else:
            #     fail_log("Time failed to be set to correct time", "005", img_service)
            #
            # if controller.d(resourceId="uk.co.bentley.mybentley:id/switch_repeat_rbc_timer_setting").info.get("checked"):
            #     log("Activate repeat enabled for timer")
            # else:
            #     controller.click_by_resource_id("uk.co.bentley.mybentley:id/switch_repeat_rbc_timer_setting")
            #     log("Activate repeat enabled for timer")
            #
            # controller.click_by_resource_id("uk.co.bentley.mybentley:id/weekdayCircularLabel_one_rbc_timer_setting") if compare_with_expected_crop("Icons/repeat_days/monday_enable.png") else None
            # controller.click_by_resource_id("uk.co.bentley.mybentley:id/weekdayCircularLabel_two_rbc_timer_setting") if compare_with_expected_crop("Icons/repeat_days/tuesday_enable.png") else None
            # controller.click_by_resource_id("uk.co.bentley.mybentley:id/weekdayCircularLabel_three_rbc_timer_setting") if compare_with_expected_crop("Icons/repeat_days/wednesday_enable.png") else None
            # controller.click_by_resource_id("uk.co.bentley.mybentley:id/weekdayCircularLabel_four_rbc_timer_setting") if compare_with_expected_crop("Icons/repeat_days/thursday_enable.png") else None
            # controller.click_by_resource_id("uk.co.bentley.mybentley:id/weekdayCircularLabel_five_rbc_timer_setting") if compare_with_expected_crop("Icons/repeat_days/friday_enable.png") else None
            # controller.click_by_resource_id("uk.co.bentley.mybentley:id/weekdayCircularLabel_six_rbc_timer_setting") if compare_with_expected_crop("Icons/repeat_days/saturday_enable.png") else None
            # controller.click_by_resource_id("uk.co.bentley.mybentley:id/weekdayCircularLabel_seven_rbc_timer_setting") if compare_with_expected_crop("Icons/repeat_days/sunday_enable.png") else None
            #
            # days = {'Monday': 'one', 'Tuesday': 'two', 'Wednesday': 'three', 'Thursday': 'four', 'Friday': 'five',
            #         'Saturday': 'six', 'Sunday': 'seven'}
            # tomorrow = datetime.now() + timedelta(days=1)
            # tomorrow = tomorrow.strftime("%A")
            #
            # controller.click_by_resource_id(f"uk.co.bentley.mybentley:id/weekdayCircularLabel_{days[tomorrow]}_rbc_timer_setting")
            #
            # if controller.d(resourceId="uk.co.bentley.mybentley:id/switch_electric_climatisation_setting").info.get("checked"):
            #     controller.click_by_resource_id("uk.co.bentley.mybentley:id/switch_electric_climatisation_setting")
            #     log("Cabin comfort disabled for timer")
            #
            # if controller.click_text("Save"):
            #     log("Edited timer saved")
            # else:
            #     fail_log("Edited timer not saved", "005", img_service)
            #
            # controller.click_text("SYNC TO CAR")
            # sleep(1)
            #
            # if controller.is_text_present("Sending message to car"):
            #     log("Sent timer mode to the car")
            # else:
            #     fail_log("Timer mode not sent to the car", "005", img_service)
            # timeout_check = 0
            # while not controller.is_text_present("Successfully sent to car"):
            #     sleep(0.5)
            #     timeout_check += 1
            #     if timeout_check > 80:
            #         break
            #
            # if controller.is_text_present("Successfully sent to car"):
            #     log("Timer mode successfully sent to the car")
            # else:
            #     fail_log("Timer mode not sent to the car", "005", img_service)
            #
            # if controller.is_text_present("Timer scheduled - Tomorrow 13:00"):
            #     log("Set timer status is displayed")
            # else:
            #     fail_log("Set timer status is not displayed", "005", img_service)

    except Exception as e:
        error_log(e, "005", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def My_Battery_Charge_006():
    recorder.start(f"{img_service}-006")
    try:
        blocked_log("Test blocked - Selecting days does not work")
        # if app_login_setup():
        #     if not int(globals.fuel_pct) >= 30:
        #         if not charger_schedule_check(True):
        #             manual_check(
        #                 instruction=f"Make sure that car there is no RBC Charge Timer scheduled",
        #                 test_id="006",
        #                 service=img_service,
        #                 take_screenshot=False
        #             )
        #         controller.click_by_image("Icons/remote_icon.png")
        #         controller.click_text("MY BATTERY CHARGE")
        #         controller.click_text("Set timer")
        #         if controller.d(resourceId="uk.co.bentley.mybentley:id/textView_periodic_time_rbc_timer_item").exists:
        #             buttons = controller.d.xpath(
        #                 '//*[@resource-id="uk.co.bentley.mybentley:id/textView_periodic_time_rbc_timer_item"]').all()
        #             buttons[0].click()
        #
        #             controller.click_by_resource_id("uk.co.bentley.mybentley:id/textView_periodic_time_rbc_timer_setting")
        #             sleep(0.2)
        #             controller.click_by_content_desc("14")
        #             sleep(0.2)
        #             controller.click_by_content_desc("0")
        #             sleep(0.2)
        #             controller.click_text("OK")
        #             if controller.is_text_present("14:00"):
        #                 log("Time set to correct time")
        #             else:
        #                 fail_log("Time failed to be set to correct time", "006", img_service)
        #
        #             if controller.d(resourceId="uk.co.bentley.mybentley:id/switch_repeat_rbc_timer_setting").info.get(
        #                     "checked"):
        #                 log("Activate repeat enabled for timer")
        #             else:
        #                 controller.click_by_resource_id("uk.co.bentley.mybentley:id/switch_repeat_rbc_timer_setting")
        #                 log("Activate repeat enabled for timer")
        #
        #             controller.click_by_resource_id(
        #                 "uk.co.bentley.mybentley:id/weekdayCircularLabel_one_rbc_timer_setting") if compare_with_expected_crop(
        #                 "Icons/repeat_days/monday_enable.png") else None
        #             controller.click_by_resource_id(
        #                 "uk.co.bentley.mybentley:id/weekdayCircularLabel_two_rbc_timer_setting") if compare_with_expected_crop(
        #                 "Icons/repeat_days/tuesday_enable.png") else None
        #             controller.click_by_resource_id(
        #                 "uk.co.bentley.mybentley:id/weekdayCircularLabel_three_rbc_timer_setting") if compare_with_expected_crop(
        #                 "Icons/repeat_days/wednesday_enable.png") else None
        #             controller.click_by_resource_id(
        #                 "uk.co.bentley.mybentley:id/weekdayCircularLabel_four_rbc_timer_setting") if compare_with_expected_crop(
        #                 "Icons/repeat_days/thursday_enable.png") else None
        #             controller.click_by_resource_id(
        #                 "uk.co.bentley.mybentley:id/weekdayCircularLabel_five_rbc_timer_setting") if compare_with_expected_crop(
        #                 "Icons/repeat_days/friday_enable.png") else None
        #             controller.click_by_resource_id(
        #                 "uk.co.bentley.mybentley:id/weekdayCircularLabel_six_rbc_timer_setting") if compare_with_expected_crop(
        #                 "Icons/repeat_days/saturday_enable.png") else None
        #             controller.click_by_resource_id(
        #                 "uk.co.bentley.mybentley:id/weekdayCircularLabel_seven_rbc_timer_setting") if compare_with_expected_crop(
        #                 "Icons/repeat_days/sunday_enable.png") else None
        #
        #             days = {'Monday': 'one', 'Tuesday': 'two', 'Wednesday': 'three', 'Thursday': 'four', 'Friday': 'five',
        #                     'Saturday': 'six', 'Sunday': 'seven'}
        #             tomorrow = datetime.now() + timedelta(days=1)
        #             tomorrow = tomorrow.strftime("%A")
        #
        #             controller.click_by_resource_id(
        #                 f"uk.co.bentley.mybentley:id/weekdayCircularLabel_{days[tomorrow]}_rbc_timer_setting")
        #
        #             if not controller.d(resourceId="uk.co.bentley.mybentley:id/switch_electric_climatisation_setting").info.get("checked"):
        #                 if controller.click_by_resource_id("uk.co.bentley.mybentley:id/switch_electric_climatisation_setting"):
        #                     log("Cabin comfort activated")
        #                 else:
        #                     fail_log("Cabin comfort could not be activated", "006", img_service)
        #             else:
        #                 fail_log("Cabin comfort activated", "006", img_service)
        #
        #             if controller.click_text("Save") and controller.is_text_present("MY BATTERY CHARGE"):
        #                 log("Timer saved")
        #             else:
        #                 fail_log("Timer not saved", "006", img_service)
        #
        #             if not controller.d(resourceId="uk.co.bentley.mybentley:id/switch_rbc_timer_item").info.get("checked"):
        #                 if controller.click_by_resource_id("uk.co.bentley.mybentley:id/switch_rbc_timer_item"):
        #                     log("Timer enabled")
        #                 else:
        #                     fail_log("Timer could not be enabled", "006", img_service)
        #
        #             controller.click_text("SYNC TO CAR")
        #             sleep(1)
        #
        #             if controller.is_text_present("Sending message to car"):
        #                 log("Sent timer mode to the car")
        #             else:
        #                 fail_log("Timer mode not sent to the car", "006", img_service)
        #             timeout_check = 0
        #             while not controller.is_text_present("Successfully sent to car"):
        #                 sleep(0.5)
        #                 timeout_check += 1
        #                 if timeout_check > 80:
        #                     break
        #
        #             if controller.is_text_present("Successfully sent to car"):
        #                 log("Timer mode successfully sent to the car")
        #             else:
        #                 fail_log("Timer mode not sent to the car", "006", img_service)
        #
        #             if controller.is_text_present(f"Timer scheduled - Tomorrow 14:00"):
        #                 log("Set timer status is displayed")
        #             else:
        #                 fail_log("Set timer status is displayed", "006", img_service)
        # else:
        #     fail_log("Timers not displayed", "006", img_service)
    except Exception as e:
        error_log(e, "006", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def My_Battery_Charge_007():
    recorder.start(f"{img_service}-007")
    try:
        if app_login_setup():
            manual_check(
                instruction=f"Set a timer in the vehicle for the battery charge service (always edit and set the first timer",
                test_id="007",
                service=img_service,
                take_screenshot=False
            )

            controller.click_by_image("Icons/remote_icon.png")
            controller.click_text("MY BATTERY CHARGE")
            controller.click_text("Set timer")
            if controller.d(resourceId="uk.co.bentley.mybentley:id/textView_periodic_time_rbc_timer_item").exists:
                buttons = controller.d.xpath(
                    '//*[@resource-id="uk.co.bentley.mybentley:id/textView_periodic_time_rbc_timer_item"]').all()
                buttons[0].click()

            manual_check(
                instruction=f"Verify the timer details show what was set in the car",
                test_id="007",
                service=img_service,
                take_screenshot=True
            )

            controller.click_by_image("Icons/login_page_x.png")
            controller.click_by_image("icons/back_icon.png")
    except Exception as e:
        error_log(e, "007", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def set_duplicate_timer(num):
    controller.click_by_resource_id("uk.co.bentley.mybentley:id/textView_periodic_time_rbc_timer_setting")
    current_date = str(datetime.now())
    time = int(current_date[11:13])
    new_time = time + 1 if time < 23 else 0
    controller.click_by_content_desc(str(new_time))
    controller.click_by_content_desc("40")
    if controller.click_text("OK"):
        log("Timer time set")
    else:
        fail_log("Timer time not set", num, img_service)

    controller.click_by_image("Icons/Repeat_days/monday_enable.png")
    if compare_with_expected_crop("Icons/Repeat_days/tuesday_enable.png"):
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/weekdayCircularLabel_two_rbc_timer_setting")
    controller.click_by_image("Icons/Repeat_days/wednesday_enable.png")
    if compare_with_expected_crop("Icons/Repeat_days/thursday_enable.png"):
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/weekdayCircularLabel_four_rbc_timer_setting")
    controller.click_by_image("Icons/Repeat_days/friday_enable.png")
    if compare_with_expected_crop("Icons/Repeat_days/saturday_enable.png"):
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/weekdayCircularLabel_six_rbc_timer_setting")
    if compare_with_expected_crop("Icons/Repeat_days/sunday_enable.png"):
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/weekdayCircularLabel_seven_rbc_timer_setting")

    controller.click_by_resource_id("uk.co.bentley.mybentley:id/weekdayCircularLabel_six_rbc_timer_setting")
    controller.click_by_resource_id("uk.co.bentley.mybentley:id/weekdayCircularLabel_seven_rbc_timer_setting")
    if compare_with_expected_crop("Icons/Repeat_days/monday_wednesday_only.png"):
        log("Repeat days selected")
    else:
        fail_log("Repeat days not selected", num, img_service)

    controller.click_by_resource_id("uk.co.bentley.mybentley:id/textView_preferred_charging_timer_from_timer")
    controller.click_by_content_desc(str(new_time))
    controller.click_by_content_desc("45")
    if controller.click_text("OK"):
        log("Starting time set")
    else:
        fail_log("Starting time unable to be set", num, img_service)

    controller.click_by_resource_id("uk.co.bentley.mybentley:id/textView_preferred_charging_timer_until_timer")
    controller.click_by_content_desc(str(new_time))
    controller.click_by_content_desc("50")
    if controller.click_text("OK"):
        log("Finishing time set")
    else:
        fail_log("Finishing time unable to be set", num, img_service)

    if controller.click_text("Save"):
        log("Timer saved")
    else:
        fail_log("Timer not saved", num, img_service)

def My_Battery_Charge_008():
    recorder.start(f"{img_service}-008")
    try:
        blocked_log("Test blocked - Selecting days does not work")
        # if app_login_setup():
        #     if not int(globals.fuel_pct) >= 30:
        #         controller.click_by_image("Icons/remote_icon.png")
        #         controller.click_text("MY BATTERY CHARGE")
        #         if controller.click_text("Set timer"):
        #             if controller.d(resourceId="uk.co.bentley.mybentley:id/textView_periodic_time_rbc_timer_item").exists:
        #                 buttons = controller.d.xpath('//*[@resource-id="uk.co.bentley.mybentley:id/textView_periodic_time_rbc_timer_item"]').all()
        #                 if len(buttons) == 2:
        #                     buttons[0].click()
        #                     set_duplicate_timer("008")
        #
        #                     buttons[1].click()
        #                     set_duplicate_timer("008")
        #                 else:
        #                     fail_log("There is not two timers, so cannot set duplicate timers", "008", img_service)
        #             else:
        #                 fail_log("Timers not displayed", "008", img_service)
        #         else:
        #             fail_log("My battery charge page not displayed", "008", img_service)
    except Exception as e:
        error_log(e, "008", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def My_Battery_Charge_009():
    recorder.start(f"{img_service}-009")
    try:
        blocked_log("Test blocked - Can't check style guide")
    except Exception as e:
        error_log(e, "009", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False