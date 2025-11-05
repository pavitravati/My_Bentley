from time import sleep
from common_utils.android_image_comparision import *
from core.log_emitter import log, metric_log, fail_log, error_log
from datetime import datetime

img_service = "Vehicle Status Report"

def identify_car():
    if compare_with_expected_crop("Icons/Bentayga.png"):
        car = 'Bentayga'
    elif compare_with_expected_crop("Icons/ContinentalGT.png"):
        car = 'Continental GT'
    elif compare_with_expected_crop("Icons/ContinentalGTC.png"):
        car = 'Continental GTC'
    elif compare_with_expected_crop("Icons/FlyingSpur.png"):
        car = 'Flying Spur'
    else:
        car = ''

    return car

def change_units(units):
    controller.click_by_image("Icons/Profile_Icon.png")
    controller.click_by_image("Icons/Profile_Screen_Setting_Icon.png")
    controller.click_text("Units")
    controller.click_text(units)
    controller.click_by_image("Icons/back_icon.png")
    controller.click_by_image("Icons/back_icon.png")
    controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

def Vehicle_Status_Report_001():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        if controller.is_text_present("DASHBOARD"):
            log("Dashboard page opened")
        else:
            fail_log("Dashboard page not opened", "001", img_service)

        controller.swipe_up()
        if controller.is_text_present("Fuel range"):
            log("Status report is displayed")
        else:
            fail_log("Status report is not displayed", "001", img_service)

        controller.swipe_down()
        controller.click_by_image("Icons/Homescreen_Right_Arrow.png")
        if compare_with_expected_crop("Icons/Remote_Lock.png"):
            controller.swipe_up()
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
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        car_name = identify_car()
        if controller.is_text_present("DASHBOARD"):
            log("Dashboard page opened, and status information is displayed")
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
            controller.swipe_up()
            log("Combined range section displayed") if controller.is_text_present("Combined range") else fail_log("Combined range section not displayed", "002", img_service)
            mileage_results = controller.extract_fuel_range_and_level(True)
            log(f"Mileage metrics displayed: {mileage_results}") if len(mileage_results) == 3 or len(mileage_results) == 6 else fail_log(f"Mileage metrics not displayed: {mileage_results}", "002", img_service)
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
            controller.swipe_down()
        else:
            fail_log("Dashboard page not opened, and status information is not displayed", "002", img_service)

    except Exception as e:
        error_log(e, "002", img_service)

def Vehicle_Status_Report_003():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.swipe_down()
        sleep(6)

        controller.click_by_image("Icons/Update_Vehicle_data.png")
        if controller.wait_for_text("Vehicle status successfully retrieved", 30):
            log("Vehicle data updated")
        else:
            fail_log("Vehicle data not updated", "003", img_service)

        controller.swipe_up()
        metrics1 = controller.extract_dashboard_metrics()
        controller.swipe_up()
        metrics2 = controller.extract_dashboard_metrics()
        metrics = {**metrics1, **{k: v for k, v in metrics2.items() if k not in metrics1}}

        for key, value in metrics.items():
            metric_log(f"{key} : {value}")

        controller.swipe_down()
        controller.swipe_down()

    except Exception as e:
        error_log(e, "003", img_service)

def Vehicle_Status_Report_004():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        sleep(45)
        controller.swipe_down()
        sleep(6)

        controller.click_by_image("Icons/Update_Vehicle_data.png")
        if controller.wait_for_text("Vehicle status successfully retrieved", 30):
            log("Vehicle data updated when ignition is off")
        else:
            fail_log("Vehicle data not updated when ignition is off", "004", img_service)

        controller.swipe_up()
        metrics1 = controller.extract_dashboard_metrics()
        controller.swipe_up()
        metrics2 = controller.extract_dashboard_metrics()
        metrics = {**metrics1, **{k: v for k, v in metrics2.items() if k not in metrics1}}

        for key, value in metrics.items():
            metric_log(f"{key} : {value}")

        controller.swipe_down()
        controller.swipe_down()

    except Exception as e:
        error_log(e, "004", img_service)

def Vehicle_Status_Report_005():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        sleep(45)
        controller.swipe_down()
        sleep(6)

        controller.click_by_image("Icons/Update_Vehicle_data.png")
        if controller.wait_for_text("Vehicle status successfully retrieved", 30):
            log("Vehicle data updated when ignition is on")
        else:
            fail_log("Vehicle data not updated when ignition is on", "005", img_service)

        controller.swipe_up()
        metrics1 = controller.extract_dashboard_metrics()
        controller.swipe_up()
        metrics2 = controller.extract_dashboard_metrics()
        metrics = {**metrics1, **{k: v for k, v in metrics2.items() if k not in metrics1}}

        for key, value in metrics.items():
            log(f"{key} : {value}")

        controller.swipe_down()
        controller.swipe_down()

    except Exception as e:
        error_log(e, "005", img_service)

def Vehicle_Status_Report_006():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        sleep(45)
        controller.swipe_down()
        sleep(6)

        controller.click_by_image("Icons/Update_Vehicle_data.png")
        if controller.wait_for_text("Vehicle status successfully retrieved", 30):
            log("Vehicle data updated when engine is running")
        else:
            fail_log("Vehicle data not updated when engine is running", "006", img_service)


        controller.swipe_up()
        metrics1 = controller.extract_dashboard_metrics()
        controller.swipe_up()
        metrics2 = controller.extract_dashboard_metrics()
        metrics = {**metrics1, **{k: v for k, v in metrics2.items() if k not in metrics1}}

        for key, value in metrics.items():
            metric_log(f"{key} : {value}")

        controller.swipe_down()
        controller.swipe_down()

    except Exception as e:
        error_log(e, "006", img_service)

def Vehicle_Status_Report_007():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.swipe_down()
        sleep(6)

        controller.click_by_image("Icons/Update_Vehicle_data.png")
        if controller.wait_for_text("Vehicle status successfully retrieved", 30):
            log("Vehicle data updated")
        else:
            fail_log("Vehicle data not updated", "007", img_service)

        controller.swipe_up()
        fuel_details = controller.extract_fuel_range_and_level()
        try:
            metric_log(f"Fuel level: {fuel_details["fuel level"]}")
            metric_log(f"Fuel range: {fuel_details['fuel range']}")
            log("Fuel level and range data extracted")

        except Exception as e:
            error_log(e, "007", img_service)

        controller.swipe_down()

    except Exception as e:
        error_log(e, "007", img_service)

def Vehicle_Status_Report_008():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.swipe_down()
        sleep(6)

        controller.click_by_image("Icons/Update_Vehicle_data.png")
        if controller.wait_for_text("Vehicle status successfully retrieved", 30):
            log("Vehicle data updated")
        else:
            fail_log("Vehicle data not updated", "008", img_service)

        controller.swipe_up()
        fuel_details = controller.extract_fuel_range_and_level(phev=True)
        try:
            metric_log(f"Fuel level: {fuel_details["fuel level"]}")
            metric_log(f"Fuel range: {fuel_details['fuel range']}")
            metric_log(f"Electricity level: {fuel_details['elec level']}")
            metric_log(f"Electricity range: {fuel_details['elec range']}")
            metric_log(f"Combined range: {fuel_details['combined range']}")
            log("All fuel and electricity data extracted")
        except Exception as e:
            error_log(e, "008", img_service)
        controller.swipe_down()

    except Exception as e:
        error_log(e, "008", img_service)

def Vehicle_Status_Report_009():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.swipe_down()
        sleep(6)

        controller.click_by_image("Icons/Update_Vehicle_data.png")
        if controller.wait_for_text("Vehicle status successfully retrieved", 30):
            log("Vehicle data updated")
        else:
            fail_log("Vehicle data not updated", "009", img_service)

        controller.swipe_up()
        fuel_details = controller.extract_fuel_range_and_level(phev=True)
        try:
            metric_log(f"Total mileage: {fuel_details["total mileage"]}")
            metric_log(f"Combined range: {fuel_details["combined range"]}")
            log("Total mileage and combined range data extracted")
        except Exception as e:
            error_log(e, "009", img_service)
        controller.swipe_down()

    except Exception as e:
        error_log(e, "009", img_service)

def Vehicle_Status_Report_010():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        change_units("Kilometres")

        controller.swipe_up()
        if controller.check_units("km"):
            log("Metrics displayed in metric units")
        else:
            fail_log("Metrics not displayed in metric units", "010", img_service)
        controller.swipe_down()

    except Exception as e:
        error_log(e, "010", img_service)

def Vehicle_Status_Report_011():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        change_units("Miles")

        controller.swipe_up()
        if controller.check_units("mi"):
            log("Metrics displayed in imperial units")
        else:
            fail_log("Metrics not displayed in imperial units", "011", img_service)
        controller.swipe_down()

    except Exception as e:
        error_log(e, "011", img_service)

def Vehicle_Status_Report_012():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.swipe_down()
        sleep(6)

        controller.click_by_image("Icons/Update_Vehicle_data.png")
        if controller.wait_for_text("Vehicle status successfully retrieved", 30):
            log("Vehicle data updated")
        else:
            fail_log("Vehicle data not updated", "012", img_service)

        controller.swipe_up()
        door_details = controller.extract_doors_status()
        try:
            if door_details['front right'] == 'Open' and door_details['front left'] == 'Closed' and door_details['rear right'] == 'Closed' and door_details['rear left'] == 'Closed':
                log("Door data updated successfully")
            else:
                fail_log("Door data not updated successfully", "012", img_service)
                metric_log(f"Driver door: {door_details['front right']}")
                metric_log(f"Front Co Passenger door: {door_details['front left']}")
                metric_log(f"Rear Left door: {door_details['rear left']}")
                metric_log(f"Rear right door: {door_details['rear right']}")
        except Exception as e:
            error_log(e, "012", img_service)

        controller.swipe_down()

    except Exception as e:
        error_log(e, "012", img_service)
Vehicle_Status_Report_012()

def Vehicle_Status_Report_013():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.swipe_down()
        sleep(6)

        controller.click_by_image("Icons/Update_Vehicle_data.png")
        if controller.wait_for_text("Vehicle status successfully retrieved", 30):
            log("Vehicle data updated")
        else:
            fail_log("Vehicle data not updated", "013", img_service)

        controller.swipe_up()
        door_details = controller.extract_doors_status()
        try:
            if door_details['front right'] == 'Open' and door_details['front left'] == 'Open' and door_details['rear right'] == 'Closed' and door_details['rear left'] == 'Closed':
                log("Door data updated successfully")
            else:
                fail_log("Door data not updated successfully", "013", img_service)
                metric_log(f"Driver door: {door_details['front right']}")
                metric_log(f"Front Co Passenger door: {door_details['front left']}")
                metric_log(f"Rear Left door: {door_details['rear left']}")
                metric_log(f"Rear right door: {door_details['rear right']}")

        except Exception as e:
            error_log(e, "013", img_service)

        controller.swipe_down()

    except Exception as e:
        error_log(e, "013", img_service)

def Vehicle_Status_Report_014():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.swipe_down()
        sleep(6)

        controller.click_by_image("Icons/Update_Vehicle_data.png")
        if controller.wait_for_text("Vehicle status successfully retrieved", 30):
            log("Vehicle data updated")
        else:
            fail_log("Vehicle data not updated", "014", img_service)

        controller.swipe_up()
        door_details = controller.extract_doors_status()
        try:
            if door_details['front right'] == 'Open' and door_details['front left'] == 'Open' and door_details[
                'rear right'] == 'Closed' and door_details['rear left'] == 'Open':
                log("Door data updated successfully")
            else:
                fail_log("Door data not updated successfully", "015", img_service)
                metric_log(f"Driver door: {door_details['front right']}")
                metric_log(f"Front Co Passenger door: {door_details['front left']}")
                metric_log(f"Rear Left door: {door_details['rear left']}")
                metric_log(f"Rear right door: {door_details['rear right']}")

        except Exception as e:
            error_log(e, "014", img_service)

        controller.swipe_down()

    except Exception as e:
        error_log(e, "014", img_service)

def Vehicle_Status_Report_015():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.swipe_down()
        sleep(6)

        controller.click_by_image("Icons/Update_Vehicle_data.png")
        if controller.wait_for_text("Vehicle status successfully retrieved", 30):
            log("Vehicle data updated")
        else:
            fail_log("Vehicle data not updated", "015", img_service)

        controller.swipe_up()
        door_details = controller.extract_doors_status()
        try:
            if door_details['front right'] == 'Open' and door_details['front left'] == 'Open' and door_details[
                'rear right'] == 'Open' and door_details['rear left'] == 'Open':
                log("Door data updated successfully")
            else:
                fail_log("Door data not updated successfully", "015", img_service)
                metric_log(f"Driver door: {door_details['front right']}")
                metric_log(f"Front Co Passenger door: {door_details['front left']}")
                metric_log(f"Rear Left door: {door_details['rear left']}")
                metric_log(f"Rear right door: {door_details['rear right']}")

        except Exception as e:
            error_log(e, "015", img_service)

        controller.swipe_down()

    except Exception as e:
        error_log(e, "015", img_service)

def Vehicle_Status_Report_016():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.swipe_down()
        sleep(6)

        controller.click_by_image("Icons/Update_Vehicle_data.png")
        if controller.wait_for_text("Vehicle status successfully retrieved", 30):
            log("Vehicle data updated")
        else:
            fail_log("Vehicle data not updated", "016", img_service)

        controller.swipe_up()
        door_details = controller.extract_doors_status()
        try:
            if door_details['front right'] == 'Closed' and door_details['front left'] == 'Closed' and door_details[
                'rear right'] == 'Closed' and door_details['rear left'] == 'Closed':
                log("Door data updated successfully")
            else:
                fail_log("Door data not updated successfully", "017", img_service)
                metric_log(f"Driver door: {door_details['front right']}")
                metric_log(f"Front Co Passenger door: {door_details['front left']}")
                metric_log(f"Rear Left door: {door_details['rear left']}")
                metric_log(f"Rear right door: {door_details['rear right']}")
        except Exception as e:
            error_log(e, "016", img_service)

        controller.swipe_down()

    except Exception as e:
        error_log(e, "016", img_service)

def Vehicle_Status_Report_017():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.swipe_down()
        sleep(6)

        controller.click_by_image("Icons/Update_Vehicle_data.png")
        if controller.wait_for_text("Vehicle status successfully retrieved", 30):
            log("Vehicle data updated")
        else:
            fail_log("Vehicle data not updated", "012", img_service)

        controller.swipe_up()
        controller.swipe_up()

        window_details = controller.extract_window_status()
        try:
            if window_details['front right'] == 'Open' and window_details['front left'] == 'Closed' and window_details[
                'rear right'] == 'Closed' and window_details['rear left'] == 'Closed' and window_details['sunroof'] == 'Closed':
                log("Window data updated successfully")
            else:
                fail_log("Door data not updated successfully", "017", img_service)
                metric_log(f"Driver window: {window_details['front right']}")
                metric_log(f"Front Co Passenger window: {window_details['front left']}")
                metric_log(f"Rear Left window: {window_details['rear left']}")
                metric_log(f"Rear right window: {window_details['rear right']}")
                metric_log(f"Sunroof: {window_details['sunroof']}")
        except Exception as e:
            error_log(e, "017", img_service)

        controller.swipe_down()
        controller.swipe_down()

    except Exception as e:
        error_log(e, "017", img_service)

def Vehicle_Status_Report_018():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.swipe_down()
        sleep(6)

        controller.click_by_image("Icons/Update_Vehicle_data.png")
        if controller.wait_for_text("Vehicle status successfully retrieved", 30):
            log("Vehicle data updated")
        else:
            fail_log("Vehicle data not updated", "018", img_service)

        controller.swipe_up()
        controller.swipe_up()

        window_details = controller.extract_window_status()
        try:
            if window_details['front right'] == 'Open' and window_details['front left'] == 'Open' and window_details[
                'rear right'] == 'Closed' and window_details['rear left'] == 'Closed' and window_details['sunroof'] == 'Closed':
                log("Window data updated successfully")
            else:
                fail_log("Door data not updated successfully", "018", img_service)
                metric_log(f"Driver window: {window_details['front right']}")
                metric_log(f"Front Co Passenger window: {window_details['front left']}")
                metric_log(f"Rear Left window: {window_details['rear left']}")
                metric_log(f"Rear right window: {window_details['rear right']}")
                metric_log(f"Sunroof: {window_details['sunroof']}")
        except Exception as e:
            error_log(e, "018", img_service)

        controller.swipe_down()
        controller.swipe_down()

    except Exception as e:
        error_log(e, "018", img_service)

def Vehicle_Status_Report_019():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.swipe_down()
        sleep(6)

        controller.click_by_image("Icons/Update_Vehicle_data.png")
        if controller.wait_for_text("Vehicle status successfully retrieved", 30):
            log("Vehicle data updated")
        else:
            fail_log("Vehicle data not updated", "019", img_service)

        controller.swipe_up()
        controller.swipe_up()

        window_details = controller.extract_window_status()
        try:
            if window_details['front right'] == 'Open' and window_details['front left'] == 'Open' and window_details[
                'rear right'] == 'Closed' and window_details['rear left'] == 'Open' and window_details['sunroof'] == 'Closed':
                log("Window data updated successfully")
            else:
                fail_log("Door data not updated successfully", "019", img_service)
                metric_log(f"Driver window: {window_details['front right']}")
                metric_log(f"Front Co Passenger window: {window_details['front left']}")
                metric_log(f"Rear Left window: {window_details['rear left']}")
                metric_log(f"Rear right window: {window_details['rear right']}")
                metric_log(f"Sunroof: {window_details['sunroof']}")
        except Exception as e:
            error_log(e, "019", img_service)

        controller.swipe_down()
        controller.swipe_down()

    except Exception as e:
        error_log(e, "019", img_service)

def Vehicle_Status_Report_020():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.swipe_down()
        sleep(6)

        controller.click_by_image("Icons/Update_Vehicle_data.png")
        if controller.wait_for_text("Vehicle status successfully retrieved", 30):
            log("Vehicle data updated")
        else:
            fail_log("Vehicle data not updated", "020", img_service)

        controller.swipe_up()
        controller.swipe_up()

        window_details = controller.extract_window_status()
        try:
            if window_details['front right'] == 'Open' and window_details['front left'] == 'Open' and window_details[
                'rear right'] == 'Open' and window_details['rear left'] == 'Open' and window_details[
                'sunroof'] == 'Closed':
                log("Window data updated successfully")
            else:
                fail_log("Door data not updated successfully", "021", img_service)
                metric_log(f"Driver window: {window_details['front right']}")
                metric_log(f"Front Co Passenger window: {window_details['front left']}")
                metric_log(f"Rear Left window: {window_details['rear left']}")
                metric_log(f"Rear right window: {window_details['rear right']}")
                metric_log(f"Sunroof: {window_details['sunroof']}")
        except Exception as e:
            error_log(e, "020", img_service)

        controller.swipe_down()
        controller.swipe_down()

    except Exception as e:
        error_log(e, "020", img_service)

def Vehicle_Status_Report_021():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.swipe_down()
        sleep(6)

        controller.click_by_image("Icons/Update_Vehicle_data.png")
        if controller.wait_for_text("Vehicle status successfully retrieved", 30):
            log("Vehicle data updated")
        else:
            fail_log("Vehicle data not updated", "021", img_service)

        controller.swipe_up()
        controller.swipe_up()

        window_details = controller.extract_window_status()
        try:
            if window_details['front right'] == 'Open' and window_details['front left'] == 'Open' and window_details[
                'rear right'] == 'Open' and window_details['rear left'] == 'Open' and window_details[
                'sunroof'] == 'Open':
                log("Window data updated successfully")
            else:
                fail_log("Door data not updated successfully", "021", img_service)
                metric_log(f"Driver window: {window_details['front right']}")
                metric_log(f"Front Co Passenger window: {window_details['front left']}")
                metric_log(f"Rear Left window: {window_details['rear left']}")
                metric_log(f"Rear right window: {window_details['rear right']}")
                metric_log(f"Sunroof: {window_details['sunroof']}")
        except Exception as e:
            error_log(e, "021", img_service)

        controller.swipe_down()
        controller.swipe_down()

    except Exception as e:
        error_log(e, "021", img_service)

def Vehicle_Status_Report_022():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.swipe_down()
        sleep(6)

        controller.click_by_image("Icons/Update_Vehicle_data.png")
        if controller.wait_for_text("Vehicle status successfully retrieved", 30):
            log("Vehicle data updated")
        else:
            fail_log("Vehicle data not updated", "022", img_service)

        controller.swipe_up()
        controller.swipe_up()

        window_details = controller.extract_window_status()
        try:
            if window_details['front right'] == 'Closed' and window_details['front left'] == 'Closed' and window_details[
                'rear right'] == 'Closed' and window_details['rear left'] == 'Closed' and window_details[
                'sunroof'] == 'Closed':
                log("Window data updated successfully")
            else:
                fail_log("Door data not updated successfully", "022", img_service)
                metric_log(f"Driver window: {window_details['front right']}")
                metric_log(f"Front Co Passenger window: {window_details['front left']}")
                metric_log(f"Rear Left window: {window_details['rear left']}")
                metric_log(f"Rear right window: {window_details['rear right']}")
                metric_log(f"Sunroof: {window_details['sunroof']}")
        except Exception as e:
            error_log(e, "022", img_service)

        controller.swipe_down()
        controller.swipe_down()

    except Exception as e:
        error_log(e, "022", img_service)

def Vehicle_Status_Report_023():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.swipe_down()
        sleep(6)

        controller.click_by_image("Icons/Update_Vehicle_data.png")
        if controller.wait_for_text("Vehicle status successfully retrieved", 30):
            log("Vehicle data updated")
        else:
            fail_log("Vehicle data not updated", "023", img_service)

        controller.swipe_up()
        boot_bonnet_status = controller.extract_boot_bonnet_status()

        try:
            if boot_bonnet_status["boot"] == "Opened" and boot_bonnet_status["bonnet"] == "Closed":
                log("Boot/Bonnet data updated successfully")
            else:
                fail_log("Boot or Bonnet data not updated successfully", "023", img_service)
                metric_log(f"Boot: {boot_bonnet_status['boot']}")
                metric_log(f"Bonnet: {boot_bonnet_status['bonnet']}")
        except Exception as e:
            error_log(e, "023", img_service)

        controller.swipe_down()

    except Exception as e:
        error_log(e, "023", img_service)

def Vehicle_Status_Report_024():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.swipe_down()
        sleep(6)

        controller.click_by_image("Icons/Update_Vehicle_data.png")
        if controller.wait_for_text("Vehicle status successfully retrieved", 30):
            log("Vehicle data updated")
        else:
            fail_log("Vehicle data not updated", "024", img_service)

        controller.swipe_up()
        boot_bonnet_status = controller.extract_boot_bonnet_status()

        try:
            if boot_bonnet_status["boot"] == "Opened" and boot_bonnet_status["bonnet"] == "Opened":
                log("Boot/Bonnet data updated successfully")
            else:
                fail_log("Boot or Bonnet data not updated successfully", "024", img_service)
                metric_log(f"Boot: {boot_bonnet_status['boot']}")
                metric_log(f"Bonnet: {boot_bonnet_status['bonnet']}")
        except Exception as e:
            error_log(e, "024", img_service)

        controller.swipe_down()

    except Exception as e:
        error_log(e, "024", img_service)

def Vehicle_Status_Report_025():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.swipe_down()
        sleep(6)

        controller.click_by_image("Icons/Update_Vehicle_data.png")
        if controller.wait_for_text("Vehicle status successfully retrieved", 30):
            log("Vehicle data updated")
        else:
            fail_log("Vehicle data not updated", "025", img_service)

        controller.swipe_up()
        boot_bonnet_status = controller.extract_boot_bonnet_status()

        try:
            if boot_bonnet_status["boot"] == "Closed" and boot_bonnet_status["bonnet"] == "Closed":
                log("Boot/Bonnet data updated successfully")
            else:
                fail_log("Boot or Bonnet data not updated successfully", "025", img_service)
                metric_log(f"Boot: {boot_bonnet_status['boot']}")
                metric_log(f"Bonnet: {boot_bonnet_status['bonnet']}")
        except Exception as e:
            error_log(e, "025", img_service)

        controller.swipe_down()

    except Exception as e:
        error_log(e, "025", img_service)

def Vehicle_Status_Report_026():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.swipe_down()
        sleep(6)

        controller.click_by_image("Icons/Update_Vehicle_data.png")
        if controller.wait_for_text("Vehicle status successfully retrieved", 30):
            log("Vehicle data updated")
        else:
            fail_log("Vehicle data not updated", "026", img_service)

        controller.swipe_up()
        light_status = controller.extract_boot_bonnet_status()

        try:
            if light_status["lights"] == "On":
                log("Lights data updated successfully")
            else:
                fail_log("Lights data not updated successfully", "026", img_service)
                metric_log(f"Lights: {light_status['lights']}")
        except Exception as e:
            error_log(e, "026", img_service)

        controller.swipe_down()

    except Exception as e:
        error_log(e, "026", img_service)

def Vehicle_Status_Report_027():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.swipe_down()
        sleep(6)

        controller.click_by_image("Icons/Update_Vehicle_data.png")
        if controller.wait_for_text("Vehicle status successfully retrieved", 30):
            log("Vehicle data updated")
        else:
            fail_log("Vehicle data not updated", "027", img_service)

        controller.swipe_up()
        light_status = controller.extract_boot_bonnet_status()

        try:
            if light_status["lights"] == "Off":
                log("Lights data updated successfully")
            else:
                fail_log("Lights data not updated successfully", "027", img_service)
                metric_log(f"Lights: {light_status['lights']}")
        except Exception as e:
            error_log(e, "027", img_service)

        controller.swipe_down()

    except Exception as e:
            error_log(e, "027", img_service)

def Vehicle_Status_Report_028():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.swipe_down()
        sleep(6)

        controller.click_by_image("Icons/Update_Vehicle_data.png")
        if controller.wait_for_text("Vehicle status successfully retrieved", 30):
            log("Vehicle data updated")
        else:
            fail_log("Vehicle data not updated", "028", img_service)

        controller.swipe_up()
        controller.swipe_up()

        oil_status = controller.extract_service_status()
        try:
            if oil_status["oil level"] and oil_status["oil change"] and oil_status["service"]:
                log("Service status displayed")
                metric_log(f"Oil level: {oil_status["oil level"]}")
                metric_log(f"Oil change: {oil_status["oil change"]}")
                metric_log(f"Service: {oil_status['service']}")
            else:
                fail_log("Service status not displayed", "028", img_service)
        except Exception as e:
            error_log(e, "028", img_service)

        controller.swipe_down()
        controller.swipe_down()

    except Exception as e:
        error_log(e, "028", img_service)

def Vehicle_Status_Report_029():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.swipe_down()
        sleep(6)

        controller.click_by_image("Icons/Update_Vehicle_data.png")
        if controller.wait_for_text("Vehicle status successfully retrieved", 30):
            log("Vehicle data updated")
        else:
            fail_log("Vehicle data not updated", "029", img_service)

        controller.swipe_up()
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
        controller.swipe_down()

    except Exception as e:
        error_log(e, "029", img_service)

# No notifications received
def Vehicle_Status_Report_030():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.swipe_down()
        sleep(6)

        controller.click_by_image("Icons/Update_Vehicle_data.png")
        controller.wait_for_text("Vehicle status successfully retrieved", 30)
        controller.press_home()

        fail_log("Not getting a notification", "030", img_service)
    except Exception as e:
        error_log(e, "030", img_service)

def Vehicle_Status_Report_031():
    try:
        log("Can't check style guide")
    except Exception as e:
        error_log(e, "031", img_service)