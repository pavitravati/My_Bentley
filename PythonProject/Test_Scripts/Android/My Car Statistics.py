from common_utils.android_image_comparision import *
from core.log_emitter import log, fail_log, error_log, metric_log
from time import sleep

img_service = "My Car Statistics"

def My_Car_Statistics_001():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        if controller.is_text_present("Last trip"):
            log("Last trip status displayed")
            last_trip = controller.d(resourceId="uk.co.bentley.mybentley:id/textView_info_car_remote_item").get_text()[2:]
            metric_log(f"Last trip: {last_trip}")
        else:
            fail_log("Last trip status not displayed", "001", img_service)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "001", img_service)

def My_Car_Statistics_002():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        controller.click_text("MY CAR STATISTICS")
        if controller.click_text("CONSUMPTION - ELECTRIC"):
            log("Graphical view dropdown menu displayed:")
            log("Consumption - Electric option displayed") if controller.is_text_present("Consumption - electric") else fail_log("Consumption - Electric option not displayed", "002")
            log("Consumption - Combustion option displayed") if controller.is_text_present("Consumption - combustion") else fail_log("Consumption - Combustion option not displayed", "002")
            log("Distance - Driven option displayed") if controller.is_text_present("Distance - driven") else fail_log("Distance - Driven option not displayed", "002")
            log("Distance - Time option displayed") if controller.is_text_present("Distance - time") else fail_log("Distance - Time option not displayed", "002")
            log("Average speed option displayed") if controller.is_text_present("Average speed") else fail_log("Average speed option not displayed", "002")
            controller.click_text("CONSUMPTION - ELECTRIC")
        else:
            fail_log("Dropdown menu not displayed", "002", img_service)

        if controller.d(resourceId="uk.co.bentley.mybentley:id/scrollView_rts_diagram").exists and controller.d(resourceId="uk.co.bentley.mybentley:id/textView_axis_labeling_graph").get_text() == "kWh/100km":
            log("Graphical view of selected option displayed")
        else:
            fail_log("Graphical view of selected option not displayed", "002", img_service)

        if controller.d(resourceId="uk.co.bentley.mybentley:id/textView_info_car_remote_item").exists:
            log("Trip data displayed")
            metric_log(f"Trip data: {controller.d(resourceId="uk.co.bentley.mybentley:id/textView_info_car_remote_item").get_text()[2:]}")
        else:
            fail_log("Trip data not displayed", "002", img_service)

        if compare_with_expected_crop("Icons/consumption_electric_selected.png"):
            log("Selected option displayed in bold")
        else:
            fail_log("Selected option not displayed in bold", "002", img_service)

        controller.click_text("List view")
        if controller.click_text("CONSUMPTION - ELECTRIC"):
            log("List view dropdown menu displayed:")
            log("Consumption - Electric option displayed") if controller.is_text_present("Consumption - electric") else fail_log("Consumption - Electric option not displayed", "002")
            log("Consumption - Combustion option displayed") if controller.is_text_present("Consumption - combustion") else fail_log("Consumption - Combustion option not displayed", "002")
            log("Distance - Driven option displayed") if controller.is_text_present("Distance - driven") else fail_log("Distance - Driven option not displayed", "002")
            log("Distance - Time option displayed") if controller.is_text_present("Distance - time") else fail_log("Distance - Time option not displayed", "002")
            log("Average speed option displayed") if controller.is_text_present("Average speed") else fail_log("Average speed option not displayed", "002")
            controller.click_text("CONSUMPTION - ELECTRIC")
        else:
            fail_log("List view dropdown menu not displayed", "002", img_service)

        if controller.d(resourceId="uk.co.bentley.mybentley:id/textView_rts_trip_info_group_subtitle").exists:
            if controller.d(resourceId="uk.co.bentley.mybentley:id/textView_rts_trip_info_group_subtitle").get_text()[-9:] == "kWh/100km":
                log("List view of selected option displayed")
            else:
                fail_log("List view of selected option not displayed", "002", img_service)
        else:
            fail_log("List view of selected option not displayed", "002", img_service)

        controller.click(110,110)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "002", img_service)

def My_Car_Statistics_003():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        controller.click_text("MY CAR STATISTICS")
        controller.click_text("CONSUMPTION - ELECTRIC")

        if controller.click_text("Consumption - combustion"):
            log("Consumption - combustion chosen from dropdown")
        else:
            fail_log("Consumption - combustion option not displayed in dropdown", "003", img_service)

        if controller.d(resourceId="uk.co.bentley.mybentley:id/scrollView_rts_diagram").exists and controller.d(resourceId="uk.co.bentley.mybentley:id/textView_axis_labeling_graph").get_text() == "l/100km":
            log("Graphical view of 'Consumption - combustion' option displayed")
        else:
            fail_log("Graphical view of 'Consumption - combustion' option not displayed", "003", img_service)

        if controller.d(resourceId="uk.co.bentley.mybentley:id/textView_info_car_remote_item").exists:
            log("Trip data displayed")
            metric_log(f"Trip data: {controller.d(resourceId="uk.co.bentley.mybentley:id/textView_info_car_remote_item").get_text()[2:]}")
        else:
            fail_log("Trip data not displayed", "003", img_service)

        if compare_with_expected_crop("Icons/consumption_combustion_selected.png"):
            log("Consumption - combustion option displayed in bold")
        else:
            fail_log("Consumption - combustion option not displayed in bold", "003", img_service)

        controller.click_text("List view")
        if controller.is_text_present("CONSUMPTION - COMBUSTION"):
            log("Consumption - combustion chosen from dropdown")
        else:
            fail_log("Consumption - combustion option not chosen in dropdown", "003", img_service)

        if controller.d(resourceId="uk.co.bentley.mybentley:id/textView_rts_trip_info_group_subtitle").exists:
            if controller.d(resourceId="uk.co.bentley.mybentley:id/textView_rts_trip_info_group_subtitle").get_text()[-7:] == "l/100km":
                log("List view of selected option displayed")
            else:
                fail_log("List view of selected option not displayed", "003", img_service)
        else:
            fail_log("List view of selected option not displayed", "003", img_service)

        controller.click(500,800)
        if compare_with_expected_crop("Icons/consumption_combustion_selected.png"):
            log("Consumption - combustion option displayed in bold")
        else:
            fail_log("Consumption - combustion option not displayed in bold", "003", img_service)

        controller.click_text("CONSUMPTION - COMBUSTION")
        controller.click_text("Consumption - electric")
        controller.click(110,110)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "003", img_service)

def My_Car_Statistics_004():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        controller.click_text("MY CAR STATISTICS")

        if controller.is_text_present("CONSUMPTION - ELECTRIC"):
            log("Consumption - Electric chosen from dropdown")
        else:
            fail_log("Consumption - Electric option not displayed in dropdown", "004", img_service)

        if controller.d(resourceId="uk.co.bentley.mybentley:id/scrollView_rts_diagram").exists and controller.d(resourceId="uk.co.bentley.mybentley:id/textView_axis_labeling_graph").get_text() == "kWh/100km":
            log("Graphical view of 'Consumption - electric' option displayed")
        else:
            fail_log("Graphical view of 'Consumption - electric' option not displayed", "004", img_service)

        if controller.d(resourceId="uk.co.bentley.mybentley:id/textView_info_car_remote_item").exists:
            log("Trip data displayed")
            metric_log(f"Trip data: {controller.d(resourceId="uk.co.bentley.mybentley:id/textView_info_car_remote_item").get_text()[2:]}")
        else:
            fail_log("Trip data not displayed", "004", img_service)

        if compare_with_expected_crop("Icons/consumption_electric_selected.png"):
            log("Consumption - electric option displayed in bold")
        else:
            fail_log("Consumption - electric option not displayed in bold", "004", img_service)

        controller.click_text("List view")
        if controller.is_text_present("CONSUMPTION - ELECTRIC"):
            log("Consumption - electric chosen from dropdown")
        else:
            fail_log("Consumption - electric option not chosen in dropdown", "004", img_service)

        if controller.d(resourceId="uk.co.bentley.mybentley:id/textView_rts_trip_info_group_subtitle").exists:
            if controller.d(resourceId="uk.co.bentley.mybentley:id/textView_rts_trip_info_group_subtitle").get_text()[-9:] == "kWh/100km":
                log("List view of selected option displayed")
            else:
                fail_log("List view of selected option not displayed", "004", img_service)
        else:
            fail_log("List view of selected option not displayed", "004", img_service)

        controller.click(500,800)
        if compare_with_expected_crop("Icons/consumption_electric_selected.png"):
            log("Consumption - electric option displayed in bold")
        else:
            fail_log("Consumption - electric option not displayed in bold", "004", img_service)

        controller.click(110,110)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "004", img_service)

def My_Car_Statistics_005():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        controller.click_text("MY CAR STATISTICS")
        controller.click_text("CONSUMPTION - ELECTRIC")

        if controller.click_text("Distance - driven"):
            log("Distance - driven chosen from dropdown")
        else:
            fail_log("Distance - driven option not displayed in dropdown", "005", img_service)

        if controller.d(resourceId="uk.co.bentley.mybentley:id/scrollView_rts_diagram").exists and controller.d(resourceId="uk.co.bentley.mybentley:id/textView_axis_labeling_graph").get_text() == "km":
            log("Graphical view of 'Distance - driven' option displayed")
        else:
            fail_log("Graphical view of 'Distance - driven' option not displayed", "005", img_service)

        if controller.d(resourceId="uk.co.bentley.mybentley:id/textView_info_car_remote_item").exists:
            log("Trip data displayed")
            metric_log(f"Trip data: {controller.d(resourceId="uk.co.bentley.mybentley:id/textView_info_car_remote_item").get_text()[2:]}")
        else:
            fail_log("Trip data not displayed", "005", img_service)

        if compare_with_expected_crop("Icons/distance_driven_selected.png"):
            log("Distance - driven option displayed in bold")
        else:
            fail_log("Distance - driven option not displayed in bold", "005", img_service)

        controller.click_text("List view")
        if controller.is_text_present("DISTANCE - DRIVEN"):
            log("Distance - driven chosen from dropdown")
        else:
            fail_log("Distance - driven option not chosen in dropdown", "005", img_service)

        if controller.d(resourceId="uk.co.bentley.mybentley:id/textView_rts_trip_info_group_subtitle").exists:
            if controller.d(resourceId="uk.co.bentley.mybentley:id/textView_rts_trip_info_group_subtitle").get_text()[-2:] == "km":
                log("List view of selected option displayed")
            else:
                fail_log("List view of selected option not displayed", "005", img_service)
        else:
            fail_log("List view of selected option not displayed", "005", img_service)

        controller.click(500, 800)
        if compare_with_expected_crop("Icons/distance_driven_selected.png"):
            log("Distance - driven option displayed in bold")
        else:
            fail_log("Distance - driven option not displayed in bold", "005", img_service)

        controller.click_text("DISTANCE - DRIVEN")
        controller.click_text("Consumption - electric")
        controller.click(110, 110)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "005", img_service)

def My_Car_Statistics_006():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        controller.click_text("MY CAR STATISTICS")
        controller.click_text("CONSUMPTION - ELECTRIC")

        if controller.click_text("Distance - time"):
            log("Distance - time chosen from dropdown")
        else:
            fail_log("Distance - time option not displayed in dropdown", "006", img_service)

        if controller.d(resourceId="uk.co.bentley.mybentley:id/scrollView_rts_diagram").exists and controller.d(resourceId="uk.co.bentley.mybentley:id/textView_axis_labeling_graph").get_text() == "h":
            log("Graphical view of 'Distance - time' option displayed")
        else:
            fail_log("Graphical view of 'Distance - time' option not displayed", "006", img_service)

        if controller.d(resourceId="uk.co.bentley.mybentley:id/textView_info_car_remote_item").exists:
            log("Trip data displayed")
            metric_log(f"Trip data: {controller.d(resourceId="uk.co.bentley.mybentley:id/textView_info_car_remote_item").get_text()[2:]}")
        else:
            fail_log("Trip data not displayed", "006", img_service)

        if compare_with_expected_crop("Icons/distance_time_selected.png"):
            log("Distance - time option displayed in bold")
        else:
            fail_log("Distance - time option not displayed in bold", "006", img_service)

        controller.click_text("List view")
        if controller.is_text_present("DISTANCE - TIME"):
            log("Distance - time chosen from dropdown")
        else:
            fail_log("Distance - time option not chosen in dropdown", "006", img_service)

        if controller.d(resourceId="uk.co.bentley.mybentley:id/textView_rts_trip_info_group_subtitle").exists:
            if controller.d(resourceId="uk.co.bentley.mybentley:id/textView_rts_trip_info_group_subtitle").get_text()[-1:] == "h":
                log("List view of selected option displayed")
            else:
                fail_log("List view of selected option not displayed", "006", img_service)
        else:
            fail_log("List view of selected option not displayed", "006", img_service)

        controller.click(500, 800)
        if compare_with_expected_crop("Icons/distance_time_selected.png"):
            log("Distance - time option displayed in bold")
        else:
            fail_log("Distance - time option not displayed in bold", "006", img_service)

        controller.click_text("DISTANCE - TIME")
        controller.click_text("Consumption - electric")
        controller.click(110, 110)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "006", img_service)

def My_Car_Statistics_007():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        controller.click_text("MY CAR STATISTICS")
        controller.click_text("CONSUMPTION - ELECTRIC")

        if controller.click_text("Average speed"):
            log("Average speed chosen from dropdown")
        else:
            fail_log("Average speed option not displayed in dropdown", "007", img_service)

        if controller.d(resourceId="uk.co.bentley.mybentley:id/scrollView_rts_diagram").exists and controller.d(resourceId="uk.co.bentley.mybentley:id/textView_axis_labeling_graph").get_text() == "km/h":
            log("Graphical view of 'Average speed' option displayed")
        else:
            fail_log("Graphical view of 'Average speed' option not displayed", "007", img_service)

        if controller.d(resourceId="uk.co.bentley.mybentley:id/textView_info_car_remote_item").exists:
            log("Trip data displayed")
            log(controller.d(resourceId="uk.co.bentley.mybentley:id/textView_info_car_remote_item").get_text()[2:])
        else:
            fail_log("Trip data not displayed", "007", img_service)

        controller.swipe_up()
        if compare_with_expected_crop("Icons/average_speed_selected.png"):
            log("Average speed option displayed in bold")
        else:
            fail_log("Average speed option not displayed in bold", "007", img_service)

        controller.click_text("List view")
        if controller.is_text_present("AVERAGE SPEED"):
            log("Average speed chosen from dropdown")
        else:
            fail_log("Average speed option not chosen in dropdown", "007", img_service)

        if controller.d(resourceId="uk.co.bentley.mybentley:id/textView_rts_trip_info_group_subtitle").exists:
            if controller.d(resourceId="uk.co.bentley.mybentley:id/textView_rts_trip_info_group_subtitle").get_text()[-4:] == "km/h":
                log("List view of selected option displayed")
            else:
                fail_log("List view of selected option not displayed", "007", img_service)
        else:
            fail_log("List view of selected option not displayed", "007", img_service)

        controller.click(500, 800)
        if compare_with_expected_crop("Icons/average_speed_selected.png"):
            log("Average speed option displayed in bold")
        else:
            fail_log("Average speed option not displayed in bold", "007", img_service)

        controller.click_text("AVERAGE SPEED")
        controller.click_text("Consumption - electric")
        controller.click(110, 110)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "007", img_service)

def My_Car_Statistics_008():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        controller.click_text("MY CAR STATISTICS")

        if controller.click_by_image("Icons/share_icon.png"):
            log("Share button displayed")
            if not compare_with_expected_crop("Icons/consumption_electric_selected.png"):
                log("Trip data can be shared")
            else:
                fail_log("Trip date cannot be shared", "008", img_service)
        else:
            fail_log("Share button not displayed", "008", img_service)

        controller.click(500, 800)
        controller.click(110, 110)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "008", img_service)

def My_Car_Statistics_009():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/info_btn.png")
        controller.click_text("Service Management")
        controller.swipe_up()
        if controller.click_text("My car statistics"):
            log("My car statistics service disabled")
            sleep(5)
        else:
            fail_log("My car statistics service not disabled", "009", img_service)

        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/back_icon.png")

        controller.click_by_image("Icons/windows_icon.png")
        if controller.is_text_present("Function disabled"):
            controller.click_text("MY CAR STATISTICS")
            if controller.is_text_present("CAR REMOTE"):
                log("My car statistics service disabled in remote screen")
            else:
                fail_log("My car statistics service not disabled in remote screen", "009", img_service)
        else:
            fail_log("My car statistics service not disabled in remote screen", "009", img_service)

        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/info_btn.png")
        controller.click_text("Service Management")
        controller.swipe_up()
        controller.click_text("My car statistics")
        sleep(5)
        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/back_icon.png")

    except Exception as e:
        error_log(e, "009", img_service)

def My_Car_Statistics_010():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.swipe_down()
        # sleep(8)
        controller.wait_for_text("Data successfully updated")
        sleep(3)
        controller.click_by_image("Icons/windows_icon.png")

        if compare_with_expected_crop("Images/car_statistics_disabled.png"):
            log("My car statistics service disabled in remote screen")
        else:
            fail_log("My car statistics service not disabled in remote screen", "010", img_service)
            controller.click(110,110)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "010")

def My_Car_Statistics_011():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.swipe_down()
        sleep(8)
        controller.click_by_image("Icons/Error_Icon.png")
        controller.click_by_image("Icons/windows_icon.png")
        controller.click_by_image("Icons/windows_icon.png")

        controller.click_text("MY CAR STATISTICS")
        if controller.is_text_present("Graphical view"):
            log("My car statistics screen accessible")
            controller.click(110,110)
        else:
            fail_log("My car statistics screen not accessible", "011", img_service)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "011", img_service)

def My_Car_Statistics_012():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/Profile_Icon.png")
        controller.click_by_image("Icons/Profile_Screen_Setting_Icon.png")
        controller.click_text("Units")

        controller.click_text("Miles")
        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/windows_icon.png")
        controller.click_text("MY CAR STATISTICS")

        if controller.d(resourceId="uk.co.bentley.mybentley:id/textView_axis_labeling_graph").get_text() == "kWh/100mi":
            log("Units changed in My car statistics screen")
        else:
            fail_log("Units not changed in My car statistics screen", "012", img_service)

        controller.click(110,110)
        controller.click_by_image("Icons/Profile_Icon.png")
        controller.click_by_image("Icons/Profile_Screen_Setting_Icon.png")
        controller.click_text("Units")
        controller.click_text("Kilometres")
        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_image("Icons/back_icon.png")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "012", img_service)

def My_Car_Statistics_013():
    try:
        log("Cannot check style guide")

    except Exception as e:
        error_log(e, "013", img_service)
