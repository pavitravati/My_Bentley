from time import sleep
from common_utils.android_image_comparision import *
from common_utils.android_controller import *
from core.log_emitter import error_log, fail_log, metric_log, log
from datetime import datetime

img_service = "Activate Heating"

def Activate_Heating_001():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")

        activate_heating = controller.d(text="ACTIVATE HEATING")
        status = activate_heating.sibling(resourceId="uk.co.bentley.mybentley:id/textView_status_car_remote_item")

        if activate_heating.exists:
            log("Activate heating section displayed")
            if status.exists and status.get_text() == "Not active":
                log("Status is 'Not active'")
            else:
                fail_log("Status is not 'Not active'", "001", img_service)
        else:
            fail_log("Activate heating section not displayed", "001", img_service)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "001", img_service)

def Activate_Heating_002():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")

        controller.click_text("ACTIVATE HEATING")
        if controller.is_text_present("Quick start") and controller.is_text_present("Timers"):
            log("'Quick start' and 'Timers' tabs displayed")
        else:
            fail_log("'Quick start' and 'Timers' tabs not displayed", "002", img_service)

    except Exception as e:
        error_log(e, "002", img_service)

def Activate_Heating_003():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        controller.click_text("ACTIVATE HEATING")

        if controller.is_text_present("ACTIVATE HEATING") and controller.is_text_present("Quick start"):
            log("Activate heating title displayed")
        else:
            fail_log("Activate heating title not displayed", "003", img_service)

        if controller.is_text_present("Prepare your Bentley in advance to keep you and all your passengers comfortable from the moment you step inside."):
            log("Activate heating description displayed")
        else:
            fail_log("Activate heating description not displayed", "003", img_service)

        all_durations = controller.swipe_heating_duration()
        duration = True
        for i in range(1, 7):
            if not all_durations[i-1] == str(i*10):
                duration = False
                break
        if duration:
            log("Correct duration options displayed")
        else:
            fail_log(f"Incorrect duration options displayed: {all_durations}", "003", img_service)

        if controller.is_text_present("STARAT"):
            log("Start button displayed")
        else:
            fail_log("Start button not displayed", "003", img_service)

        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "003", img_service)

def Activate_Heating_004():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        controller.click_text("ACTIVATE HEATING")

        if controller.click_text("Timers"):
            log("Timers tab clicked")
            if controller.is_text_present("ACTIVATE HEATING"):
                log("Activate heating title displayed")
            else:
                fail_log("Activate heating title not displayed", "004", img_service)

            node = controller.d(resourceId="uk.co.bentley.mybentley:id/textView_time_rah_timer_item")
            if node.exists:
                if node.info.get("visibleToUser"):
                    log("Departure time is displayed")
                else:
                    fail_log("Departure time is not displayed", "004", img_service)
            else:
                fail_log("Departure time is not displayed", "004", img_service)

            node = controller.d(resourceId="uk.co.bentley.mybentley:id/switch_rah_timer_item")
            if node.exists:
                if node.info.get("visibleToUser"):
                    log("Departure time toggle button is displayed")
                else:
                    fail_log("Departure time toggle button is not displayed", "004", img_service)
            else:
                fail_log("Departure time is not displayed", "004", img_service)

            if controller.is_text_present("SYNC TO CAR"):
                log("SYNC TO CAR button is displayed")
            else:
                fail_log("SYNC TO CAR button is not displayed", "004", img_service)
        else:
            fail_log("Timers tab not displayed", "004", img_service)

        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "004", img_service)

def Activate_Heating_005():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        controller.click_text("ACTIVATE HEATING")

        if controller.click_text("START"):
            log("Start button clicked")
        else:
            fail_log("Start button not displayed", "005", img_service)

        # This is all guessing, do in vehicle to check
        if controller.click_text("VEHICLE IS PARKED SAFELY"):
            log("Safety status confirmed")
        else:
            fail_log("Safety status not confirmed", "005", img_service)
        controller.enter_pin()
        if controller.wait_for_text("Successfully sent to the car"):
            log("Heating information successfully sent to the car")
        else:
            fail_log("Heating information not sent to the car", "005", img_service)

        controller.click_by_image("Icons/back_icon.png")
        activate_heating = controller.d(text="ACTIVATE HEATING")
        status = activate_heating.sibling(resourceId="uk.co.bentley.mybentley:id/textView_status_car_remote_item")
        if status.exists and status.get_text() == "Active":
            log("Status is 'Active'")
        else:
            fail_log("Status is not 'Active'", "005", img_service)

        controller.click_text("ACTIVATE HEATING")
        if controller.is_text_present("STOP"):
            log("Stop button displayed")
        else:
            fail_log("Stop button not displayed", "005", img_service)
        #Don't know what the remote park heating means part means

        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "005", img_service)

def Activate_Heating_006():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        controller.click_text("ACTIVATE HEATING")

        if controller.click_text("STOP"):
            log("Stop button clicked")
        else:
            fail_log("Stop button not displayed", "006", img_service)

        if controller.is_text_present("START"):
            log("Start button displayed")
        else:
            fail_log("Start button not displayed", "006", img_service)

        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "006", img_service)

def Activate_Heating_007():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        controller.click_text("ACTIVATE HEATING")
        controller.click_text("Timers")

        if controller.click_by_resource_id("uk.co.bentley.mybentley:id/textView_time_rah_timer_item"):
            current_date = str(datetime.now())
            print(current_date)
            today = int(current_date[8:10])
            controller.click_by_text_id(str(today))
            controller.click_text("OK")

            controller.click_by_resource_id("uk.co.bentley.mybentley:id/textView_time_rah_timer_setting")
            hour = int(current_date[11:13])
            minute = int(current_date[14:16])
            new_hour = hour if minute < 40 else hour+1
            controller.click_by_content_desc(str(new_hour))
            new_minute = minute+20 if minute < 40 else 0
            controller.click_by_content_desc(str(new_minute))
            controller.click_text("OK")
            if controller.click_text("Save"):
                log("Timer set")
            else:
                fail_log("Timer not set", "007", img_service)

            if compare_with_expected_crop("Icons/timer_toggle_off.png"):
                controller.click_by_resource_id("uk.co.bentley.mybentley:id/switch_rah_timer_item")

            if controller.click_text("SYNC TO CAR"):
                if controller.click_text("VEHICLE IS PARKED SAFELY"):
                    if controller.enter_pin():
                        sleep(5)
                        activate_heating = controller.d(text="ACTIVATE HEATING")
                        status = activate_heating.sibling(resourceId="uk.co.bentley.mybentley:id/textView_status_car_remote_item")
                        if status.exists and status.get_text() == "Scheduled":
                            log("Status is 'Scheduled'")
                        else:
                            fail_log("Status is not 'Scheduled'", "007", img_service)
                    else:
                        fail_log("Failed to enter PIN", "007", img_service)
                else:
                    fail_log("Parked safely button not displayed", "007", img_service)
            else:
                fail_log("Sync to car button not displayed", "007", img_service)
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "007", img_service)

def Activate_Heating_008():
    try:
        log("✅ - temp, can't check style guide")
    except Exception as e:
        error_log(e, "008", img_service)