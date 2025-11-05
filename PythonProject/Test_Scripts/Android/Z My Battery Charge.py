from common_utils.android_image_comparision import *
from core.log_emitter import log, fail_log, error_log, metric_log
from time import sleep
from datetime import datetime

img_service = "My Battery Charge"

def My_Battery_Charge_001():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        if compare_with_expected_crop("Images/my_battery_charge.png") or compare_with_expected_crop("Images/my_battery_charge_greyed.png"):
            log("My battery charge section displayed correctly")
        else:
            fail_log("My battery charge section failed to be displayed", "001", img_service)

        metric = controller.d.xpath('//*[@resource-id="uk.co.bentley.mybentley:id/textView_status_car_remote_item"]').all()
        metric_log(f"Charging status: {metric[1].text}")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "001", img_service)

def extract_battery_status():
    metrics = []
    metrics.append(f"Charging status: {controller.d(resourceId="uk.co.bentley.mybentley:id/textView_charging_state_rbc_charge_state").get_text()}")
    metrics.append("Battery progress bar displayed" if controller.d(resourceId="uk.co.bentley.mybentley:id/arcProgressBarView_rbc_charge_state").info.get("enabled") else "Battery progress bar not displayed")
    metrics.append(f"Battery percentage: {controller.d(resourceId="uk.co.bentley.mybentley:id/textView_battery_status_percentage_rbc_charge_state").get_text()}")
    metrics.append(f"Estimated charging time: {controller.d(resourceId="uk.co.bentley.mybentley:id/textView_charge_time_rbc_charge_state").get_text()}")
    return metrics

def My_Battery_Charge_002():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
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
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        else:
            fail_log("My battery charge service failed to open", "002", img_service)
    except Exception as e:
        error_log(e, "002", img_service)

def My_Battery_Charge_003():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        controller.click_text("MY BATTERY CHARGE")

        if controller.click_text("QUICK START"):
            log("Quick start button clicked")
        else:
            fail_log("Quick start button not found", "003", img_service)
        # Finish in car
    except Exception as e:
        error_log(e, "003", img_service)

def My_Battery_Charge_004():
    try:
        pass
        # do in car
    except Exception as e:
        error_log(e, "004", img_service)

def My_Battery_Charge_005():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        controller.click_text("MY BATTERY CHARGE")
        controller.click_text("Set timer")

        if not controller.d(resourceId="uk.co.bentley.mybentley:id/switch_rbc_timer_item").info.get("checked"):
            if controller.click_by_resource_id("uk.co.bentley.mybentley:id/switch_rbc_timer_item"):
                log("Timer enabled")
        else:
            log("Timer is enabled")

        controller.click(500, 520)
        if controller.is_text_present("EDIT TIMER"):
            log("Timer opened and editable")
        else:
            fail_log("Timer not opened or editable", "004", img_service)

        if controller.d(resourceId="uk.co.bentley.mybentley:id/switch_repeat_rbc_timer_setting").info.get("checked"):
            log("Activate repeat enabled for timer")
        else:
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/switch_repeat_rbc_timer_setting")
            controller.click_by_image("Icons/monday_repeat.png")
            log("Activate repeat enabled for timer")

        if controller.click_text("Save"):
            log("Edited timer saved")
        else:
            fail_log("Edited timer not saved", "004", img_service)

        # Do in car

    except Exception as e:
        error_log(e, "005")

def My_Battery_Charge_006():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        controller.click_text("MY BATTERY CHARGE")
        controller.click_text("Set timer")
        if controller.d(resourceId="uk.co.bentley.mybentley:id/textView_periodic_time_rbc_timer_item").exists:
            buttons = controller.d.xpath(
                '//*[@resource-id="uk.co.bentley.mybentley:id/textView_periodic_time_rbc_timer_item"]').all()
            buttons[0].click()

            if not controller.d(resourceId="uk.co.bentley.mybentley:id/switch_electric_climatisation_setting").info.get("checked"):
                if controller.click_by_resource_id("uk.co.bentley.mybentley:id/switch_electric_climatisation_setting"):
                    log("Cabin comfort activated")
                else:
                    fail_log("Cabin comfort could not be activated", "006", img_service)

            if controller.click_text("Save"):
                log("Timer saved")
            else:
                fail_log("Timer not saved", "006", img_service)

            if not controller.d(resourceId="uk.co.bentley.mybentley:id/switch_rbc_timer_item").info.get("checked"):
                if controller.click_by_resource_id("uk.co.bentley.mybentley:id/switch_rbc_timer_item"):
                    log("Timer enabled")
                else:
                    fail_log("Timer could not be enabled", "006", img_service)

            # controller.click_text("SYNC TO CAR")
            # Finish in car
        else:
            fail_log("Timers not displayed", "006", img_service)
    except Exception as e:
        error_log(e, "006", img_service)

def My_Battery_Charge_007():
    try:
        pass
    except Exception as e:
        error_log(e, "007", img_service)

def set_duplicate_timer():
    controller.click_by_resource_id("uk.co.bentley.mybentley:id/textView_periodic_time_rbc_timer_setting")
    current_date = str(datetime.now())
    time = int(current_date[11:13])
    new_time = time + 1 if time < 23 else 0
    controller.click_by_content_desc(str(new_time))
    controller.click_by_content_desc("40")
    if controller.click_text("OK"):
        log("Timer time set")
    else:
        fail_log("Timer time not set", "008", img_service)

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

    # controller.click_by_image("Icons/Repeat_days/monday_disable.png")
    # controller.click_by_image("Icons/Repeat_days/wednesday_disable.png")
    controller.click_by_resource_id("uk.co.bentley.mybentley:id/weekdayCircularLabel_six_rbc_timer_setting")
    controller.click_by_resource_id("uk.co.bentley.mybentley:id/weekdayCircularLabel_seven_rbc_timer_setting")
    if compare_with_expected_crop("Icons/Repeat_days/monday_wednesday_only.png"):
        log("Repeat days selected")
    else:
        fail_log("Repeat days not selected", "008", img_service)

    controller.click_by_resource_id("uk.co.bentley.mybentley:id/textView_preferred_charging_timer_from_timer")
    controller.click_by_content_desc(str(new_time))
    controller.click_by_content_desc("45")
    if controller.click_text("OK"):
        log("Starting time set")
    else:
        fail_log("Starting time unable to be set", "008", img_service)

    controller.click_by_resource_id("uk.co.bentley.mybentley:id/textView_preferred_charging_timer_until_timer")
    controller.click_by_content_desc(str(new_time))
    controller.click_by_content_desc("50")
    if controller.click_text("OK"):
        log("Finishing time set")
    else:
        fail_log("Finishing time unable to be set", "008", img_service)

    if controller.click_text("Save"):
        log("Timer saved")
    else:
        fail_log("Timer not saved", "008", img_service)

# Does not work, does not set the correct days
def My_Battery_Charge_008():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        controller.click_text("MY BATTERY CHARGE")
        if controller.click_text("Set timer"):
            if controller.d(resourceId="uk.co.bentley.mybentley:id/textView_periodic_time_rbc_timer_item").exists:
                buttons = controller.d.xpath('//*[@resource-id="uk.co.bentley.mybentley:id/textView_periodic_time_rbc_timer_item"]').all()
                if len(buttons) == 2:
                    buttons[0].click()
                    set_duplicate_timer()

                    buttons[1].click()
                    set_duplicate_timer()
                else:
                    fail_log("There is not two timers, so cannot set duplicate timers", "008", img_service)
            else:
                fail_log("Timers not displayed", "008", img_service)
        else:
            fail_log("My battery charge page not displayed", "008", img_service)
    except Exception as e:
        error_log(e, "008", img_service)

My_Battery_Charge_008()

def My_Battery_Charge_009():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.swipe_up()

        dashboard_metrics = controller.extract_dashboard_metrics()
        if dashboard_metrics:
            extracted = True
            if dashboard_metrics['Fuel Range']:
                metric_log(f"Fuel range: {dashboard_metrics['Fuel Range']}")
            else:
                extracted = False
            if dashboard_metrics['Fuel pct']:
                metric_log(f"Fuel range: {dashboard_metrics['Fuel pct']}")
            else:
                extracted = False
            if dashboard_metrics['Battery Range']:
                metric_log(f"Fuel range: {dashboard_metrics['Battery Range']}")
            else:
                extracted = False
            if dashboard_metrics['Battery pct']:
                metric_log(f"Fuel range: {dashboard_metrics['Battery pct']}")
            else:
                extracted = False

            if extracted:
                log("SOC and Fuel status displayed")
            else:
                fail_log("SOC and Fuel status not all displayed", "009", img_service)
        else:
            fail_log("Dashboard metrics not found", "009", img_service)
        controller.swipe_down()

    except Exception as e:
        error_log(e, "009", img_service)

def My_Battery_Charge_010():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/info_btn.png")
        controller.click_text("Service Management")
        if controller.click_text("My battery charge"):
            log("My battery charge service disabled in service management")
            sleep(3)
        else:
            fail_log("My battery charge service not found in service management", "010", img_service)
        controller.click_image("icons/back_icon.png")
        controller.click_image("icons/back_icon.png")

        controller.click_by_image("Icons/windows_icon.png")
        if controller.click_text("MY BATTERY CHARGE") and controller.is_text_present("Function disabled") and not controller.is_text_present("Set timer"):
            log("My battery charge successfully disabled")
        else:
            fail_log("My battery charge failed to be disabled", "010", img_service)

    except Exception as e:
        error_log(e, "010", img_service)

def My_Battery_Charge_011():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/navigation_icon.png")
        controller.click_by_image("Images/Navigation_Allow.png")
        controller.click_by_image("Images/Navigation_Car_Image.png")

        markers = controller.d.xpath('//*[@content-desc="Map Marker"]').all()
        if markers:
            log("Vehicle location found")
            driver_icon_bounds = []
            for i in range(len(markers)):
                driver_icon_bounds.append(markers[i].center())
                if i == 1:
                    break

            controller.click(driver_icon_bounds[0][0], driver_icon_bounds[0][1])
            vehicle_details = controller.extract_navigation_vehicle()
            if vehicle_details:
                log("PHEV Vehicle details displayed in Car Finder feature")
                for metric, stat in vehicle_details.items():
                    metric_log(f"{metric}: {stat}")
            else:
                try:
                    controller.click(driver_icon_bounds[1][0], driver_icon_bounds[1][1])
                    vehicle_details = controller.extract_navigation_vehicle()
                    print(vehicle_details)
                    if vehicle_details:
                        log("PHEV Vehicle details displayed in Car Finder feature")
                        for metric, stat in vehicle_details:
                            metric_log(f"{metric}: {stat}")
                    else:
                        fail_log("PHEV Vehicle details not in Car Finder feature", "011", img_service)
                except Exception as e:
                    fail_log("No vehicle visible on navigation page", "011", img_service)
            controller.click(500, 500)
        else:
            fail_log("Vehicle location cannot be found", "011", img_service)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "011", img_service)

def My_Battery_Charge_012():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.swipe_down()
        sleep(8)
        controller.wait_for_text("Data successfully updated")
        controller.click_by_image("Icons/windows_icon.png")

        if compare_with_expected_crop("Images/battery_charge_disabled.png"):
            log("My battery charge service disabled in privacy mode")
        else:
            fail_log("My battery charge service not disabled in privacy mode", "012", img_service)

        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "012", img_service)

def My_Battery_Charge_013():
    try:
        log("Cannot check style guide")
    except Exception as e:
        error_log(e, "013", img_service)