from common_utils.android_image_comparision import *
from core.log_emitter import log, fail_log, error_log, metric_log
from time import sleep
import re

def My_Cabin_Comfort_001():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        controller.swipe_up(0.6)

        cabin_comfort = controller.d(text="MY CABIN COMFORT")
        status = cabin_comfort.sibling(resourceId="uk.co.bentley.mybentley:id/textView_status_car_remote_item")

        if cabin_comfort.exists:
            log("Cabin comfort section displayed")
            if status.exists and status.get_text() == "Not active":
                log("Status is 'Not active'")
            else:
                fail_log("Status is not 'Not active'", "001")
        else:
            fail_log("Cabin comfort section not displayed", "001")

        controller.swipe_down()
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "001")

def My_Cabin_Comfort_002():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        controller.swipe_up(0.6)

        if controller.click_text("MY CABIN COMFORT"):
            log("Cabin Comfort section clicked")
        else:
            fail_log("Cabin comfort section could not be found", "002")

        if controller.is_text_present("Quick start"):
            log("Quick start tab displayed")
        else:
            fail_log("Quick start tab not displayed", "002")

        if controller.is_text_present("Set timer"):
            log("Set timer tab displayed")
        else:
            fail_log("Set timer tab not displayed", "002")

        controller.click_by_image("Icons/back_icon.png")
        controller.swipe_down()
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "002")

def My_Cabin_Comfort_003():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        controller.swipe_up(0.6)

        if controller.click_text("MY CABIN COMFORT"):
            if controller.is_text_present("MY CABIN COMFORT"):
                log("Cabin comfort title displayed")
            else:
                fail_log("Cabin comfort title not displayed", "003")

            if controller.is_text_present("Prepare your Bentley in advance to keep you and all your passengers comfortable from the moment you step inside."):
                log("Cabin comfort information displayed")
            else:
                fail_log("Cabin comfort information not displayed", "003")

            if controller.is_text_present("Target temperature") and controller.d(className="android.widget.SeekBar").exists:
                log("Target temperature bar displayed")
            else:
                fail_log("Target temperature bar not displayed", "003")

            if controller.is_text_present("Interior surface heating") and compare_with_expected_crop("Icons/Interior_heating_toggle.png"):
                log("Interior surface heating toggle displayed")
            else:
                fail_log("Interior surface heating toggle not displayed", "003")

            if controller.is_text_present("START"):
                log("Start button displayed")
            else:
                fail_log("Start button not displayed", "003")
        else:
            fail_log("Cabin comfort section could not be found", "003")

        controller.click_by_image("Icons/back_icon.png")
        controller.swipe_down()
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "003")

def My_Cabin_Comfort_004():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        controller.swipe_up(0.6)

        if controller.click_text("MY CABIN COMFORT"):
            if compare_with_expected_crop("Images/default_heating.png", 0.99):
                log("Default seat heating options displayed")
            else:
                fail_log("Default seat heating options not displayed", "004")

            if controller.click_by_image("Icons/Rear_left_seat_disabled.png") and compare_with_expected_crop("Icons/Rear_left_seat_enabled.png", 0.99):
                log("Rear seat heating options supported")
            else:
                fail_log("Rear seat heating options not supported", "004")

        else:
            fail_log("Cabin comfort section could not be found", "004")

        controller.click_by_image("Icons/back_icon.png")
        controller.swipe_down()
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "004")

# this is tested using co-ords, so different phones may not work, can't think of another way to interact with bar
def My_Cabin_Comfort_005():
    temperatures = ["16", "17", "18", "19", "21"]
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        controller.swipe_up(0.6)

        if controller.click_text("MY CABIN COMFORT"):
            for i in range(1, 6):
                controller.click((100*i), 930)
                cabin_comfort = controller.d(text="Target temperature")
                temp = cabin_comfort.sibling(index="2").get_text()
                if temp == f"{temperatures[i-1]}.0 °C":
                    log("Target temperature able to be set")
                else:
                    fail_log("Target temperature unable to be set", "005")
        else:
            fail_log("Cabin comfort section could not be found", "005")

        controller.click_by_image("Icons/back_icon.png")
        controller.swipe_down()
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "005")

def My_Cabin_Comfort_006():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        controller.swipe_up(0.6)

        if controller.click_text("MY CABIN COMFORT"):
            controller.click(200, 930)
            cabin_comfort = controller.d(text="Target temperature")
            temp = cabin_comfort.sibling(index="2").get_text()
            if temp == "62.0 °C":
                log("Target temperature set successfully")
            else:
                fail_log("Target temperature not set", "006")

            if controller.click_text("START"):
                log("Start button clicked")
            else:
                fail_log("Start button not found", "006")

            #rest in car
        else:
            fail_log("Cabin comfort section could not be found", "006")

        controller.click_by_image("Icons/back_icon.png")
        controller.swipe_down()
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "006")

def My_Cabin_Comfort_007():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        controller.swipe_up(0.6)

        if controller.click_text("MY CABIN COMFORT"):
            controller.click(300, 930)
            cabin_comfort = controller.d(text="Target temperature")
            temp = cabin_comfort.sibling(index="2").get_text()
            if temp == "18.0 °C":
                log("Target temperature set successfully")
            else:
                fail_log("Target temperature not set", "007")

            if compare_with_expected_crop("Images/default_heating.png", 0.99):
                log("Default seat heating options displayed")
            else:
                fail_log("Default seat heating options not displayed", "007")

            if controller.click_by_image("Icons/Front_left_seat_enabled.png") and compare_with_expected_crop("Icons/Front_left_seat_disabled.png", 0.99) and compare_with_expected_crop("Icons/Front_right_seat_enabled.png", 0.99):
                log("Driver seat heating enabled and passenger seat heating disabled successfully")
            else:
                fail_log("Driver seat heating enabled and passenger seat heating disabled unsuccessfully", "007")

            if controller.click_text("START"):
                log("Start button clicked")
            else:
                fail_log("Start button not found", "007")

            # rest in car
        else:
            fail_log("Cabin comfort section could not be found", "007")

        controller.click_by_image("Icons/back_icon.png")
        controller.swipe_down()
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "007")

def My_Cabin_Comfort_008():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        controller.swipe_up(0.6)

        if controller.click_text("MY CABIN COMFORT"):
            controller.click(300, 930)
            cabin_comfort = controller.d(text="Target temperature")
            temp = cabin_comfort.sibling(index="2").get_text()
            if temp == "18.0 °C":
                log("Target temperature set successfully")
            else:
                fail_log("Target temperature not set", "008")

            if compare_with_expected_crop("Images/default_heating.png", 0.99):
                log("Default seat heating options displayed")
            else:
                fail_log("Default seat heating options not displayed", "008")

            if controller.click_by_image("Icons/Front_right_seat_enabled.png") and compare_with_expected_crop("Icons/Front_right_seat_disabled.png", 0.99) and compare_with_expected_crop("Icons/Front_left_seat_enabled.png", 0.99):
                log("Driver seat heating disabled and passenger seat heating enabled successfully")
            else:
                fail_log("Driver seat heating disabled and passenger seat heating enabled unsuccessfully", "008")

            if controller.click_text("START"):
                log("Start button clicked")
            else:
                fail_log("Start button not found", "008")

            # rest in car
        else:
            fail_log("Cabin comfort section could not be found", "008")

        controller.click_by_image("Icons/back_icon.png")
        controller.swipe_down()
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "008")

def My_Cabin_Comfort_009():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        controller.swipe_up(0.6)

        if controller.click_text("MY CABIN COMFORT"):
            controller.click(300, 930)
            cabin_comfort = controller.d(text="Target temperature")
            temp = cabin_comfort.sibling(index="2").get_text()
            if temp == "18.0 °C":
                log("Target temperature set successfully")
            else:
                fail_log("Target temperature not set", "009")

            if compare_with_expected_crop("Images/default_heating.png", 0.99):
                log("Default seat heating options displayed")
            else:
                fail_log("Default seat heating options not displayed", "009")

            if controller.click_by_image("Icons/Rear_left_seat_disabled.png") and controller.click_by_image("Icons/Front_right_seat_enabled.png") and controller.click_by_image("Icons/Front_left_seat_enabled.png") and compare_with_expected_crop("Images/Rear_left_enabled_only.png", 0.99):
                log("Front seat heating disabled and rear left seat heating enabled successfully")
            else:
                fail_log("Front seat heating disabled and rear left seat heating enabled unsuccessfully", "009")

            if controller.click_text("START"):
                log("Start button clicked")
            else:
                fail_log("Start button not found", "009")

            # rest in car
        else:
            fail_log("Cabin comfort section could not be found", "009")

        controller.click_by_image("Icons/back_icon.png")
        controller.swipe_down()
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "009")

def My_Cabin_Comfort_010():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        controller.swipe_up(0.6)

        if controller.click_text("MY CABIN COMFORT"):
            controller.click(300, 930)
            cabin_comfort = controller.d(text="Target temperature")
            temp = cabin_comfort.sibling(index="2").get_text()
            if temp == "18.0 °C":
                log("Target temperature set successfully")
            else:
                fail_log("Target temperature not set", "010")

            if compare_with_expected_crop("Images/default_heating.png", 0.99):
                log("Default seat heating options displayed")
            else:
                fail_log("Default seat heating options not displayed", "010")

            if controller.click_by_image("Icons/Rear_right_seat_disabled.png") and controller.click_by_image("Icons/Front_right_seat_enabled.png") and controller.click_by_image("Icons/Front_left_seat_enabled.png") and compare_with_expected_crop("Images/Rear_right_enabled_only.png", 0.99):
                log("Front seat heating disabled and rear right seat heating enabled successfully")
            else:
                fail_log("Front seat heating disabled and rear right seat heating enabled unsuccessfully", "010")

            if controller.click_text("START"):
                log("Start button clicked")
            else:
                fail_log("Start button not found", "010")

            # rest in car
        else:
            fail_log("Cabin comfort section could not be found", "010")

        controller.click_by_image("Icons/back_icon.png")
        controller.swipe_down()
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "010")

def My_Cabin_Comfort_011():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        controller.swipe_up(0.6)

        if controller.click_text("MY CABIN COMFORT"):
            controller.click(300, 930)
            cabin_comfort = controller.d(text="Target temperature")
            temp = cabin_comfort.sibling(index="2").get_text()
            if temp == "18.0 °C":
                log("Target temperature set successfully")
            else:
                fail_log("Target temperature not set", "011")

            if compare_with_expected_crop("Images/default_heating.png", 0.99):
                log("Default seat heating options displayed")
            else:
                fail_log("Default seat heating options not displayed", "011")

            if controller.click_by_image("Icons/Rear_right_seat_disabled.png") and controller.click_by_image("Icons/Rear_left_seat_disabled.png") and compare_with_expected_crop("Images/all_seats_enabled.png", 0.99):
                log("Front seat heating disabled and rear right seat heating enabled successfully")
            else:
                fail_log("Front seat heating disabled and rear right seat heating enabled unsuccessfully", "011")

            if controller.click_text("START"):
                log("Start button clicked")
            else:
                fail_log("Start button not found", "011")

            # rest in car
        else:
            fail_log("Cabin comfort section could not be found", "010")

        controller.click_by_image("Icons/back_icon.png")
        controller.swipe_down()
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "011")

def My_Cabin_Comfort_012():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        controller.swipe_up(0.6)

        cabin_comfort = controller.d(text="MY CABIN COMFORT")
        status = cabin_comfort.sibling(resourceId="uk.co.bentley.mybentley:id/textView_status_car_remote_item")
        if cabin_comfort.exists:
            log("Cabin comfort section displayed")
            if status.exists and status.get_text() == "Not active":
                log("Status is 'Not active'")
            else:
                fail_log("Status is not 'Not active'", "012")

        # guessing, do all in car
        if controller.click_text("MY CABIN COMFORT"):
            if controller.click_text("STOP"):
                log("Stop button clicked")
            else:
                fail_log("Stop button not found", "012")

            if controller.istext_present("START"):
                log("Stop button is now the start button")
            else:
                fail_log("Start button not found", "012")
        else:
            fail_log("Cabin comfort section could not be found", "012")

        controller.click_by_image("Icons/back_icon.png")
        controller.swipe_down()
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "012")

# Verifying the timers exist is dodgey as no unqiue resourceids so used an image of the toggles and then returned the timers as metrics.
def My_Cabin_Comfort_013():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        controller.swipe_up(0.6)

        if controller.click_text("MY CABIN COMFORT"):
            if controller.click_text("Set timer"):
                log("Set timer tab clicked")
            else:
                fail_log("Set timer tab not found", "013")

            if controller.is_text_present("MY CABIN COMFORT"):
                log("Cabin comfort title displayed")
            else:
                fail_log("Cabin comfort title not displayed", "013")

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
                fail_log("Timers not displayed", "013")

            if controller.is_text_present("SETTINGS"):
                log("Settings button displayed")
            else:
                fail_log("Settings button not displayed", "013")

            if controller.d(text="SYNC TO CAR").exists:
                log("Sync button displayed")
                if compare_with_expected_crop("Icons/sync_button_disabled.png"):
                    controller.click_by_image("Icons/timer_toggle_off.png")
                    if compare_with_expected_crop("Icons/sync_button_enabled.png"):
                        log("Sync button only clickable when timer enabled")
                    else:
                        fail_log("Sync button not only clickable when timer enabled", "013")
                else:
                    fail_log("Sync button not only clickable when timer enabled", "013")
            else:
                fail_log("Sync button not displayed", "013")

        else:
            fail_log("Cabin comfort section could not be found", "013")

        controller.click_by_image("Icons/back_icon.png")
        controller.swipe_down()
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "013")

def My_Cabin_Comfort_014():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        controller.swipe_up(0.6)

        if controller.click_text("MY CABIN COMFORT"):
            if controller.click_text("Set timer"):
                if controller.click_text("SETTINGS"):
                    log("Settings button clicked")
                    if controller.is_text_present("Interior surface heating") and compare_with_expected_crop("Icons/Interior_heating_toggle.png"):
                        log("Interior surface heating toggle displayed")
                    else:
                        fail_log("Interior surface heating not displayed", "014")

                    if compare_with_expected_crop("Images/default_heating.png", 0.985):
                        log("Default seat heating options displayed")
                    else:
                        fail_log("Default seat heating not displayed", "014")

                    controller.click_by_image("Icons/Interior_heating_toggle.png")
                    if not compare_with_expected_crop("Images/default_heating.png", 0.99):
                        log("Default seat heating options hidden when heating tis toggled off")
                    else:
                        fail_log("Default seat heating options not hidden when heating tis toggled off", "014")
                else:
                    fail_log("Settings button not clicked", "014")
            else:
                fail_log("Set timer tab not found", "014")
        else:
            fail_log("Cabin comfort section could not be found", "014")

        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/back_icon.png")
        controller.swipe_down()
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "014")

def My_Cabin_Comfort_015():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        controller.swipe_up(0.6)

        if controller.click_text("MY CABIN COMFORT"):
            controller.click_by_image("Icons/Interior_heating_toggle.png")
            if controller.click_text("Set timer"):
                controller.click_text("SETTINGS")
                controller.click_by_image("Icons/Interior_heating_toggle.png")
                controller.click_by_image("Icons/back_icon.png")

                # ask about this one

            else:
                fail_log("Set timer tab not found", "014")
        else:
            fail_log("Cabin comfort section could not be found", "014")

        controller.click_by_image("Icons/back_icon.png")
        controller.swipe_down()
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "015")

def My_Cabin_Comfort_016():
    try:
        pass
    except Exception as e:
        error_log(e, "016")

def My_Cabin_Comfort_017():
    try:
        pass
    except Exception as e:
        error_log(e, "017")

def My_Cabin_Comfort_018():
    try:
        pass
    except Exception as e:
        error_log(e, "018")

def My_Cabin_Comfort_019():
    try:
        pass
    except Exception as e:
        error_log(e, "019")

def My_Cabin_Comfort_020():
    try:
        pass
    except Exception as e:
        error_log(e, "020")

def My_Cabin_Comfort_021():
    try:
        pass
    except Exception as e:
        error_log(e, "021")

def My_Cabin_Comfort_022():
    try:
        pass
    except Exception as e:
        error_log(e, "022")

def My_Cabin_Comfort_023():
    try:
        pass
    except Exception as e:
        error_log(e, "023")

def My_Cabin_Comfort_024():
    try:
        pass
    except Exception as e:
        error_log(e, "024")

def My_Cabin_Comfort_025():
    try:
        pass
    except Exception as e:
        error_log(e, "025")

def My_Cabin_Comfort_026():
    try:
        pass
    except Exception as e:
        error_log(e, "026")
