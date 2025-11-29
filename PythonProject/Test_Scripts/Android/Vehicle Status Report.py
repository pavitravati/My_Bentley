from time import sleep
from common_utils.android_image_comparision import *
from core.app_functions import app_login_setup, identify_car, app_refresh
from core.globals import vehicle_type, fuel_pct, battery_pct
from core.log_emitter import log, metric_log, fail_log, error_log, blocked_log
from datetime import datetime
from core.globals import manual_run
from gui.manual_check import manual_check

img_service = "Vehicle Status Report"

def change_units(units):
    controller.click_by_image("Icons/Profile_Icon.png")
    controller.click_by_image("Icons/Profile_Screen_Setting_Icon.png")
    controller.click_text("Units")
    controller.click_text(units)
    controller.click_by_image("Icons/back_icon.png")
    controller.click_by_image("Icons/back_icon.png")
    controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

def metric_checker(metric, metric_dict,  num):
    if metric in metric_dict:
        return f"\n{metric}: {metric_dict[metric]}"
    else:
        fail_log(f"{metric} data not extracted", num, img_service)
        return ""

def Vehicle_Status_Report_001():
    try:
        if app_login_setup():
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            if controller.is_text_present("DASHBOARD"):
                log("Dashboard page opened")
            else:
                fail_log("Dashboard page not opened", "001", img_service)

            controller.swipe_up()
            if controller.is_text_present("ACTIVATE STOLEN VEHICLE TRACKING"):
                controller.extra_small_swipe_up()
            if controller.is_text_present("Fuel range"):
                log("Status report is displayed")
            else:
                fail_log("Status report is not displayed", "001", img_service)

            controller.swipe_down()
            controller.extra_small_swipe_down()
            controller.click_by_image("Icons/Homescreen_Right_Arrow.png")
            if not controller.is_text_present("ADD A VEHICLE"):
                controller.swipe_up()
                if controller.is_text_present("CONTACT SUPPORT"):
                    log("Second vehicle displayed but status unavailable")
                    controller.small_swipe_down()
                else:
                    if controller.is_text_present("ACTIVATE STOLEN VEHICLE TRACKING"):
                        controller.extra_small_swipe_up()
                    if controller.is_text_present("Fuel range"):
                        log("Status report is displayed for second vehicle on account")
                    else:
                        fail_log("Status report not displayed for second vehicle on account", "001", img_service)
                    controller.swipe_down()
            controller.click_by_image("Icons/Homescreen_Left_Arrow.png")

    except Exception as e:
        error_log(e, "001", img_service)

def Vehicle_Status_Report_002():
    try:
        if app_login_setup():
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            car_name = identify_car()
            if controller.is_text_present("DASHBOARD"):
                log("Screen title displayed") if controller.is_text_present("DASHBOARD") else fail_log("Screen title not displayed", "002", img_service)
                log("Vehicle image displayed") if car_name != '' else fail_log("Vehicle image not displayed", "002", img_service)
                info_btn = True if controller.click_by_image("Icons/info_btn.png") else False
                controller.click_by_image("Icons/back_icon.png")
                log("Info icon displayed") if info_btn else fail_log("Info icon not displayed", "002", img_service)
                now = datetime.now()
                current_date = f"{now.strftime('%A')} {now.day} {now.strftime('%B')}"
                log("Greeting message and date displayed") if compare_with_expected_crop("Icons/good.png") and controller.is_text_present(current_date) else fail_log("Greeting message and date not displayed", "002", img_service)
                log("Vehicle name displayed") if controller.is_text_present(car_name.upper()) else fail_log("Vehicle name not displayed", "002", img_service)
                log("Last vehicle contact displayed") if compare_with_expected_crop("Icons/Last_vehicle_contact.png") else fail_log("Last vehicle contact displayed", "002", img_service)
                log("Remote Lock/Unlock button displayed") if compare_with_expected_crop("Icons/Remote_Lock.png") else fail_log("Remote Lock/Unlock button not displayed", "002", img_service)
                log("Vehicle lock status displayed") if controller.is_text_present("Vehicle unlocked") or controller.is_text_present("Vehicle locked") else fail_log("Vehicle lock status not displayed", "002", img_service)
                if vehicle_type == "phev":
                    controller.swipe_up()
                    if controller.is_text_present("ACTIVATE STOLEN VEHICLE TRACKING"):
                        controller.extra_small_swipe_up()
                    log("Combined range section displayed") if controller.is_text_present("Combined range") else fail_log("Combined range section not displayed", "002", img_service)
                elif vehicle_type == "ice":
                    controller.swipe_up()
                    if controller.is_text_present("ACTIVATE STOLEN VEHICLE TRACKING"):
                        controller.extra_small_swipe_up()
                mileage_results = controller.extract_fuel_range_and_level()
                results_str = "("
                for key, value in mileage_results.items():
                    results_str += f"{key}-{value}|"
                results_str += ")"
                log(f"Mileage metrics displayed: {results_str}") if len(mileage_results) == 3 or len(mileage_results) == 6 else fail_log(f"Mileage metrics not displayed: {results_str}", "002", img_service)
                log("Side lights status displayed") if controller.d(text="Lights").exists else fail_log("Side lights status displayed", "002", img_service)
                log("Door status section displayed") if controller.is_text_present("Doors") else fail_log("Combined range section not displayed", "002", img_service)
                door_results = controller.extract_doors_status()
                log(f"Door status displayed: {door_results}") if len(door_results) == 4 else fail_log(f"Door status not displayed: {door_results}", "002", img_service)
                boot_results = controller.extract_boot_bonnet_status()
                log(f"Boot and Bonnet status displayed: {boot_results}") if len(boot_results) == 2 else fail_log(f"Boot and Bonnet status not displayed: {boot_results}", "002", img_service)
                controller.swipe_up()
                log("Window status section displayed") if controller.is_text_present("Windows") else fail_log("Window status not displayed", "002", img_service)
                window_results = controller.extract_window_status()
                log(f"Window status displayed: {window_results}") if len(window_results) >= 4 else fail_log(f"Window status not displayed: {window_results}", "002", img_service)
                service_status = controller.extract_service_status()
                log(f"Service status displayed: {service_status}") if len(service_status) == 4 else fail_log(f"Service status not displayed: {service_status}", "002", img_service)
                controller.swipe_down()
                controller.swipe_down(0.15)
        else:
            fail_log("Dashboard page not opened, and status information is not displayed", "002", img_service)

    except Exception as e:
        error_log(e, "002", img_service)

def Vehicle_Status_Report_003():
    try:
        if app_login_setup():
            app_refresh("003", img_service)

            if vehicle_type == "phev":
                controller.swipe_up()
            elif vehicle_type == "ice":
                controller.swipe_up()
            if controller.is_text_present("ACTIVATE STOLEN VEHICLE TRACKING"):
                controller.extra_small_swipe_up()

            metrics1 = controller.extract_dashboard_metrics()
            controller.swipe_up()
            metrics2 = controller.extract_dashboard_metrics()
            metrics = {**metrics1, **{k: v for k, v in metrics2.items() if k not in metrics1}}

            for key, value in metrics.items():
                metric_log(f"{key} : {value}")

            controller.swipe_down()
            controller.swipe_down(0.15)

    except Exception as e:
        error_log(e, "003", img_service)

def Vehicle_Status_Report_004():
    try:
        if app_login_setup():
            app_refresh("004", img_service, "when ignition is off", 45)

            if vehicle_type == "phev":
                controller.swipe_up()
            elif vehicle_type == "ice":
                controller.swipe_up()
            if controller.is_text_present("ACTIVATE STOLEN VEHICLE TRACKING"):
                controller.extra_small_swipe_up()

            metrics1 = controller.extract_dashboard_metrics()
            controller.swipe_up()
            metrics2 = controller.extract_dashboard_metrics()
            metrics = {**metrics1, **{k: v for k, v in metrics2.items() if k not in metrics1}}

            for key, value in metrics.items():
                metric_log(f"{key} : {value}")

            controller.swipe_down()
            controller.swipe_down(0.15)

    except Exception as e:
        error_log(e, "004", img_service)

def Vehicle_Status_Report_005():
    try:
        if app_login_setup():
            if not int(fuel_pct) > 0:
                blocked_log("Test blocked - Car must have some fuel")
            else:
                app_refresh("005", img_service)

                if vehicle_type == "phev":
                    controller.swipe_up()
                elif vehicle_type == "ice":
                    controller.swipe_up()
                if controller.is_text_present("ACTIVATE STOLEN VEHICLE TRACKING"):
                    controller.extra_small_swipe_up()

                fuel_details = controller.extract_fuel_range_and_level()
                if fuel_details:
                    log("Fuel level and range data extracted")
                    metric_check = "Verify the data in the kombi matches the extracted metrics"
                    metric_check += metric_checker("fuel level", fuel_details, "005")
                    metric_check += metric_checker("fuel range", fuel_details, "005")
                    manual_check(
                        instruction=metric_check,
                        test_id="005",
                        service=img_service,
                        take_screenshot=False
                    )
                controller.swipe_down(0.15)

    except Exception as e:
        error_log(e, "005", img_service)

def Vehicle_Status_Report_006():
    try:
        if vehicle_type == "phev":
            if app_login_setup():
                if not int(fuel_pct) > 0 and not int(battery_pct) > 0:
                    blocked_log("Test blocked - Car must have some fuel and battery charge")
                else:
                    app_refresh("006", img_service)
                    controller.swipe_up()
                    if controller.is_text_present("ACTIVATE STOLEN VEHICLE TRACKING"):
                        controller.extra_small_swipe_up()

                    fuel_details = controller.extract_fuel_range_and_level()
                    if fuel_details:
                        log("Fuel and electricity data extracted")
                        metric_check = "Verify the data in the kombi matches the extracted metrics"
                        metric_check += metric_checker("fuel level", fuel_details, "006")
                        metric_check += metric_checker("fuel range", fuel_details, "006")
                        metric_check += metric_checker("elec level", fuel_details, "006")
                        metric_check += metric_checker("elec range", fuel_details, "006")
                        metric_check += metric_checker("combined range", fuel_details, "006")

                        manual_check(
                            instruction=metric_check,
                            test_id="006",
                            service=img_service,
                            take_screenshot=False
                        )
                    else:
                        fail_log("Fuel and electricity data not extracted", "006", img_service)
                    controller.swipe_down(0.15)
        elif vehicle_type == "ice":
            blocked_log("Test blocked - Must be a PHEV vehicle")

    except Exception as e:
        error_log(e, "006", img_service)

def Vehicle_Status_Report_007():
    try:
        if app_login_setup():
            app_refresh("007", img_service)

            if vehicle_type == "phev":
                controller.swipe_up()
            elif vehicle_type == "ice":
                controller.swipe_up()
            if controller.is_text_present("ACTIVATE STOLEN VEHICLE TRACKING"):
                controller.extra_small_swipe_up()

            fuel_details = controller.extract_fuel_range_and_level()
            if fuel_details:
                log("Mileage data extracted")
                metric_check = "Verify the data in the kombi matches the extracted metrics"
                metric_check += metric_checker("total mileage", fuel_details, "005")
                metric_check += metric_checker("combined range", fuel_details, "005")
                manual_check(
                    instruction=metric_check,
                    test_id="007",
                    service=img_service,
                    take_screenshot=False
                )
            else:
                fail_log("Mileage status data not extracted", "007", img_service)

            controller.swipe_down(0.15)

    except Exception as e:
        error_log(e, "007", img_service)

def Vehicle_Status_Report_008():
    try:
        if app_login_setup():
            change_units("Kilometres")

            if vehicle_type == "phev":
                controller.swipe_up()
            elif vehicle_type == "ice":
                controller.swipe_up()
            if controller.is_text_present("ACTIVATE STOLEN VEHICLE TRACKING"):
                controller.extra_small_swipe_up()

            if controller.check_units("km"):
                log("Metrics displayed in metric units")
            else:
                fail_log("Metrics not displayed in metric units", "008", img_service)
            controller.swipe_down(0.15)

            # Test this???
            # manual_check(
            #     instruction="In MMI/Kombi change to metric units\nCheck that the units displayed are changed to km/litre",
            #     test_id="008",
            #     service=img_service,
            #     take_screenshot=False
            # )

    except Exception as e:
        error_log(e, "008", img_service)

def Vehicle_Status_Report_009():
    try:
        if app_login_setup():
            change_units("Miles")

            if vehicle_type == "phev":
                controller.swipe_up()
            elif vehicle_type == "ice":
                controller.swipe_up()
            if controller.is_text_present("ACTIVATE STOLEN VEHICLE TRACKING"):
                controller.extra_small_swipe_up()

            if controller.check_units("mi"):
                log("Metrics displayed in imperial units")
            else:
                fail_log("Metrics not displayed in imperial units", "009", img_service)
            controller.swipe_down(0.15)

            # Test this???
            # manual_check(
            #     instruction="In MMI/Kombi change to imperial units\nCheck that the units displayed are changed to miles/gallons",
            #     test_id="009",
            #     service=img_service,
            #     take_screenshot=False
            # )

    except Exception as e:
        error_log(e, "009", img_service)

def Vehicle_Status_Report_010():
    try:
        if app_login_setup():
            app_refresh("004", img_service, "when ignition is on", 45)

            if vehicle_type == "phev":
                controller.swipe_up()
            elif vehicle_type == "ice":
                controller.swipe_up(0.3)
            if controller.is_text_present("ACTIVATE STOLEN VEHICLE TRACKING"):
                controller.extra_small_swipe_up()

            metrics1 = controller.extract_dashboard_metrics()
            controller.swipe_up()
            metrics2 = controller.extract_dashboard_metrics()
            metrics = {**metrics1, **{k: v for k, v in metrics2.items() if k not in metrics1}}

            for key, value in metrics.items():
                log(f"{key} : {value}")

            controller.swipe_down()
            controller.swipe_down(0.15)

    except Exception as e:
        error_log(e, "010", img_service)

def Vehicle_Status_Report_011():
    try:
        if app_login_setup():
            app_refresh("011", img_service, "when engine is running", 45)

            if vehicle_type == "phev":
                controller.swipe_up()
            elif vehicle_type == "ice":
                controller.swipe_up(0.3)
            if controller.is_text_present("ACTIVATE STOLEN VEHICLE TRACKING"):
                controller.extra_small_swipe_up()

            metrics1 = controller.extract_dashboard_metrics()
            controller.swipe_up()
            metrics2 = controller.extract_dashboard_metrics()
            metrics = {**metrics1, **{k: v for k, v in metrics2.items() if k not in metrics1}}

            for key, value in metrics.items():
                metric_log(f"{key} : {value}")

            controller.swipe_down()
            controller.swipe_down(0.15)

    except Exception as e:
        error_log(e, "011", img_service)

def door_status_check(expected_status, num):
    controller.swipe_up()
    if controller.is_text_present("ACTIVATE STOLEN VEHICLE TRACKING"):
        controller.extra_small_swipe_up()

    door_details = controller.extract_doors_status()
    if "front right" in door_details and "front left" in door_details and "rear right" in door_details and "rear left" in door_details:
        if door_details['front right'] == expected_status[0] and door_details['front left'] == expected_status[1] and door_details[
            'rear right'] == expected_status[2] and door_details['rear left'] == expected_status[3]:
            log("Door data updated successfully")
        else:
            fail_log("Door data not updated successfully", num, img_service)
            metric_log(f"Driver door: {door_details['front right']}")
            metric_log(f"Front Co Passenger door: {door_details['front left']}")
            metric_log(f"Rear Left door: {door_details['rear left']}")
            metric_log(f"Rear right door: {door_details['rear right']}")
    else:
        fail_log("Door data not extracted", num, img_service)

    controller.swipe_down(0.15)

def Vehicle_Status_Report_012():
    try:
        if app_login_setup():
            app_refresh("012", img_service)
            door_status_check(['Open', 'Closed', 'Closed', 'Closed'], "012")

            controller.swipe_down(0.15)

    except Exception as e:
        error_log(e, "012", img_service)

def Vehicle_Status_Report_013():
    try:
        if app_login_setup():
            app_refresh("013", img_service)
            door_status_check(['Open', 'Open', 'Closed', 'Closed'], "013")

    except Exception as e:
        error_log(e, "013", img_service)

def Vehicle_Status_Report_014():
    try:
        if app_login_setup():
            app_refresh("014", img_service)
            door_status_check(['Open', 'Open', 'Closed', 'Open'], "014")

    except Exception as e:
        error_log(e, "014", img_service)

def Vehicle_Status_Report_015():
    try:
        if app_login_setup():
            app_refresh("015", img_service)
            door_status_check(['Open', 'Open', 'Open', 'Open'], "015")

    except Exception as e:
        error_log(e, "015", img_service)

def Vehicle_Status_Report_016():
    try:
        if app_login_setup():
            app_refresh("016", img_service)
            door_status_check(['Closed', 'Closed', 'Closed', 'Closed'], "016")

    except Exception as e:
        error_log(e, "016", img_service)

def window_status_check(expected_status, num, sunroof=False):
    controller.swipe_up()
    if controller.is_text_present("ACTIVATE STOLEN VEHICLE TRACKING"):
        controller.extra_small_swipe_up()
    controller.swipe_up()

    window_details = controller.extract_window_status()
    if "front right" in window_details and "front left" in window_details and "rear right" in window_details and "rear left" in window_details:
        if (window_details['front right'] == expected_status[0] and window_details['front left'] == expected_status[1] and window_details['rear right']== expected_status[2]
            and window_details['rear left'] == expected_status[3] and (window_details['sunroof'] == expected_status[4] if sunroof else True)):
            log("Window data updated successfully")
        else:
            fail_log("Door data not updated successfully", num, img_service)
            metric_log(f"Driver window: {window_details['front right']}")
            metric_log(f"Front Co Passenger window: {window_details['front left']}")
            metric_log(f"Rear Left window: {window_details['rear left']}")
            metric_log(f"Rear right window: {window_details['rear right']}")
            if sunroof:
                metric_log(f"Sunroof: {window_details['sunroof']}")
    else:
        if sunroof:
            if 'front right' not in window_details:
                fail_log("Window data not extracted", "021", img_service)
            elif 'sunroof' not in window_details:
                fail_log("Car does not have a sunroof to check", "021", img_service)
        else:
            fail_log("Window data not extracted", num, img_service)

    controller.swipe_down()
    controller.swipe_down(0.15)

def Vehicle_Status_Report_017():
    try:
        if app_login_setup():
            app_refresh("017", img_service)
            window_status_check(["Open", "Closed", "Closed", "Closed"], "017")

    except Exception as e:
        error_log(e, "017", img_service)

def Vehicle_Status_Report_018():
    try:
        if app_login_setup():
            app_refresh("018", img_service)
            window_status_check(["Open", "Open", "Closed", "Closed"], "018")

    except Exception as e:
        error_log(e, "018", img_service)

def Vehicle_Status_Report_019():
    try:
        if app_login_setup():
            app_refresh("019", img_service)
            window_status_check(["Open", "Open", "Closed", "Open"], "019")

    except Exception as e:
        error_log(e, "019", img_service)

def Vehicle_Status_Report_020():
    try:
        if app_login_setup():
            app_refresh("020", img_service)
            window_status_check(["Open", "Open", "Open", "Open"], "020")

    except Exception as e:
        error_log(e, "020", img_service)

def Vehicle_Status_Report_021():
    try:
        if app_login_setup():
            app_refresh("021", img_service)
            window_status_check(["Open", "Open", "Open", "Open", "Sunroof Open"], "021", sunroof=True)

    except Exception as e:
        error_log(e, "021", img_service)

def Vehicle_Status_Report_022():
    try:
        if app_login_setup():
            app_refresh("022", img_service)
            window_status_check(["Closed", "Closed", "Closed", "Closed", "Sunroof Closed"], "022", sunroof=True)

    except Exception as e:
        error_log(e, "022", img_service)

def boot_bonnet_status_check(expected_status, num):
    controller.swipe_up()
    if controller.is_text_present("ACTIVATE STOLEN VEHICLE TRACKING"):
        controller.extra_small_swipe_up()
    boot_bonnet_status = controller.extract_boot_bonnet_status()

    if 'Boot' in boot_bonnet_status and 'Bonnet' in boot_bonnet_status:
        if boot_bonnet_status["Boot"] == expected_status[0] and boot_bonnet_status["Bonnet"] == expected_status[1]:
            log("Boot/Bonnet data updated successfully")
        else:
            fail_log("Boot or Bonnet data not updated successfully", num, img_service)
            metric_log(f"Boot: {boot_bonnet_status['Boot']}")
            metric_log(f"Bonnet: {boot_bonnet_status['Bonnet']}")
    else:
        fail_log("Boot and bonnet data not extracted", num, img_service)

    controller.swipe_down(0.15)

def Vehicle_Status_Report_023():
    try:
        if app_login_setup():
            app_refresh("023", img_service)
            boot_bonnet_status_check(["Open", "Closed"], "023")

    except Exception as e:
        error_log(e, "023", img_service)

def Vehicle_Status_Report_024():
    try:
        if app_login_setup():
            app_refresh("024", img_service)
            boot_bonnet_status_check(["Open", "Open"], "024")

    except Exception as e:
        error_log(e, "024", img_service)

def Vehicle_Status_Report_025():
    try:
        if app_login_setup():
            app_refresh("025", img_service)
            boot_bonnet_status_check(["Closed", "Closed"], "025")

    except Exception as e:
        error_log(e, "025", img_service)

def Vehicle_Status_Report_026():
    try:
        if app_login_setup():
            app_refresh("026", img_service)

            controller.swipe_up()
            if controller.is_text_present("ACTIVATE STOLEN VEHICLE TRACKING"):
                controller.extra_small_swipe_up()
            light_status = controller.extract_lights_status()

            if light_status == "On":
                log("Lights data updated successfully")
            else:
                fail_log("Lights data not updated successfully", "026", img_service)
                metric_log(f"Lights: {light_status}")

            controller.swipe_down(0.15)

    except Exception as e:
        error_log(e, "026", img_service)

def Vehicle_Status_Report_027():
    try:
        if app_login_setup():
            app_refresh("027", img_service)

            controller.swipe_up()
            if controller.is_text_present("ACTIVATE STOLEN VEHICLE TRACKING"):
                controller.extra_small_swipe_up()
            light_status = controller.extract_lights_status()

            if light_status == "Off":
                log("Lights data updated successfully")
            else:
                fail_log("Lights data not updated successfully", "027", img_service)
                metric_log(f"Lights: {light_status}")

            controller.swipe_down(0.15)

    except Exception as e:
            error_log(e, "027", img_service)

def Vehicle_Status_Report_028():
    try:
        if app_login_setup():
            app_refresh("028", img_service)

            controller.swipe_up()
            if controller.is_text_present("ACTIVATE STOLEN VEHICLE TRACKING"):
                controller.extra_small_swipe_up()
            controller.swipe_up()

            oil_status = controller.extract_service_status()
            if 'Oil level' in oil_status and 'Oil change' in oil_status and 'Service' in oil_status:
                log("Service status displayed")
                metric_log(f"Oil level: {oil_status["Oil level"]}")
                metric_log(f"Oil change: {oil_status["Oil change"]}")
                metric_log(f"Service: {oil_status['Service']}")
            else:
                fail_log("Service status not displayed", "028", img_service)

            controller.swipe_down()
            controller.swipe_down(0.15)

    except Exception as e:
        error_log(e, "028", img_service)

def Vehicle_Status_Report_029():
    try:
        if app_login_setup():
            app_refresh("029", img_service)

            controller.swipe_up()
            if controller.is_text_present("ACTIVATE STOLEN VEHICLE TRACKING"):
                controller.extra_small_swipe_up()
            controller.swipe_up()
            controller.click_text("Cluster warnings")

            if controller.is_text_present("No cluster warnings"):
                log("Cluster warnings status displayed")
                metric_log("No cluster warnings")
            else:
                pass
                # What happens if there are cluster warnings.

            controller.click_by_image("Icons/back_icon.png")
            controller.swipe_down()
            controller.swipe_down(0.15)

    except Exception as e:
        error_log(e, "029", img_service)
Vehicle_Status_Report_029()

# No notifications received
def Vehicle_Status_Report_030():
    try:
        blocked_log("Test blocked - Push notification not working")
        # if app_login_setup():
        #     controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        #     controller.swipe_down()
        #     sleep(6)
        #     if compare_with_expected_crop("Icons/Error_Icon.png"):
        #         fail_log("Error displayed on refresh", "003", img_service)
        #         controller.click_by_image("Icons/Error_Icon.png")
        #     else:
        #         controller.click_by_image("Icons/Update_Vehicle_data.png")
        #         controller.wait_for_text("Vehicle status successfully retrieved", 30)
        #         controller.press_home()
        #
        #     fail_log("Not getting a notification", "030", img_service)
    except Exception as e:
        error_log(e, "030", img_service)

def Vehicle_Status_Report_031():
    try:
        blocked_log("Test blocked - Can't check style guide")
    except Exception as e:
        error_log(e, "031", img_service)