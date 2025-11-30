from common_utils.android_image_comparision import *
from core.app_functions import app_login_setup, identify_car
from core.log_emitter import log, fail_log, error_log, metric_log, blocked_log
from gui.manual_check import manual_check
from time import sleep
from core.globals import manual_run
import core.globals as globals

img_service = "Nav Companion"

def Nav_Companion_001():
    try:
        if app_login_setup():
            if controller.click_by_image("Icons/navigation_icon.png"):
                log("Clicked on navigation tab")
            else:
                fail_log("Clicked on navigation tab", "001", img_service)

            controller.click_by_image("Images/Navigation_Allow.png")

            if controller.is_text_present("NAVIGATION"):
                log("Navigation screen launched")
            else:
                fail_log("Navigation screen not launched", "001", img_service)

            if compare_with_expected_crop("Images/Navigation_Search_Image.png"):
                log("Search Window displayed")
            else:
                fail_log("Search Window not displayed", "001", img_service)

            if controller.click_by_image("Images/Navigation_Car_Image.png"):
                car_icon = False
                car_names = ['Bentayga', 'FlyingSpur', 'ContinentalGT', 'ContinentalGTC']
                for _ in range(4):
                    if compare_with_expected_crop(f"Images/Nav_{car_names[_]}_Icon.png", 0.9):
                        car_icon = True
                if car_icon:
                    log("Car Icon displayed and shows current location of vehicle")
                else:
                    fail_log("Car Icon displayed but does not show current location of vehicle", "001", img_service)
            else:
                fail_log("Car Icon not displayed", "001", img_service)

            if controller.click_by_image("Images/Navigation_User_Image.png") and compare_with_expected_crop("Images/Navigation_User_Icon.png", 0.85):
                log("User Icon displayed and shows current location of user")
            else:
                fail_log("User Icon not displayed", "001", img_service)

            if controller.click_by_image("Images/Navigation_Info_Image.png"):
                if controller.is_text_present("Satellite") and controller.is_text_present("Show real time traffic data"):
                    log("Option to enable 'Satellite' and 'Real time traffic' displayed")
                else:
                    fail_log("Option to enable 'Satellite' and 'Real time traffic' not displayed", "001", img_service)
            else:
                fail_log("Option to enable 'Satellite' and 'Real time traffic' not displayed", "001", img_service)
            controller.click_by_image("Images/Navigation_Info_Image.png")
    except Exception as e:
        error_log(e, "001", img_service)

def Nav_Companion_002():
    try:
        if app_login_setup():
            controller.click_by_image("Icons/navigation_icon.png")
            controller.click_by_image("Images/Navigation_Allow.png")

            if controller.click_by_image("Images/Navigation_Search_Image.png"):
                if controller.enter_text("London"):
                    log("Searched for a location")
                    log("Location appears after searching") if controller.wait_for_text("London, UK") else fail_log("Location did not appear after searching", "002", img_service)
                else:
                    fail_log("Failed to search for a location", "002", img_service)
            else:
                fail_log("Failed to search for a location", "002", img_service)
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/textView_list_item_poi_title")
            if controller.click_text("SEND TO CAR"):
                log("Location sent to car")
            else:
                fail_log("Send to car button not displayed", "002", img_service)

            if controller.wait_for_text(f"London sent successfully to {globals.current_car}"):
                log("Location sent confirmation message received")
            else:
                fail_log("Location sent confirmation message not received", "002", img_service)
            controller.click_by_image("Icons/location_back.png")

            manual_check(
                instruction="Check whether the recently sent location to vehicle via My Bentley App can be accessed in vehicle",
                test_id="002",
                service=img_service,
                take_screenshot = False
            )

            controller.delete_sent_location()
            if controller.wait_for_text("Currently no places found. To find a destination use the search field."):
                log("Sent location deleted from app")
            else:
                fail_log("Sent location not deleted from app", "002", img_service)

            manual_check(
                instruction="Check whether the recently deleted location via My Bentley App is deleted from vehicle",
                test_id="002",
                service=img_service,
                take_screenshot = False
            )
            controller.click_by_image("Icons/location_back.png")


    except Exception as e:
        error_log(e, "002", img_service)

def Nav_Companion_003():
    try:
        if app_login_setup():
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            car = identify_car()
            controller.click_by_image("Icons/navigation_icon.png")
            controller.click_by_image("Images/Navigation_Allow.png")
            controller.click_by_image("Images/Navigation_Search_Image.png")
            location = "Manchester"
            controller.enter_text(location)
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/textView_list_item_poi_title")

            controller.click_by_image("Icons/location_favourite_unselected.png")
            if controller.wait_for_text(f"{location} saved successfully as favorite"):
                log("Location saved as favourite")
            else:
                fail_log("Location not saved as favourite", "003", img_service)

            if controller.is_text_present("SEND TO CAR"):
                log("Location sent to car")
            else:
                fail_log("Send to car button not displayed", "003", img_service)

            if controller.wait_for_text(f"{location} sent successfully to {car}"):
                log("Location sent confirmation message received")
            else:
                fail_log("Location sent confirmation message not received", "003", img_service)

            # Check it is under fav and last destination
            controller.click_by_image("Images/Navigation_Search_Image.png")
            controller.click_text("NAVIGATION")
            if controller.is_text_present("Currently no favorites added. To add a favorites in your app destinations, use the search field in this view. The added app favorites could be synced to your vehicle."):
                log("Location deleted from favourites on app")
            else:
                manual_check(
                    instruction=f"Check whether the deleted location ({location}) is deleted from favourites section on the app",
                    test_id="003",
                    service=img_service,
                    take_screenshot=True
                )
                controller.small_swipe_up()
            if controller.is_text_present("Currently no destinations added. To add a destination use the search field."):
                log("Location deleted from sent destinations on app")
            else:
                manual_check(
                    instruction=f"Check whether the deleted location ({location}) is deleted from sent destination section on the app",
                    test_id="003",
                    service=img_service,
                    take_screenshot=True
                )

            controller.click_by_image("Icons/location_back.png")
            controller.click_by_image("Images/Navigation_Search_Image.png")
            controller.click_text("NAVIGATION")
            controller.delete_favourite_location() # Kind of broken
            controller.click_by_image("Icons/location_back.png")

            manual_check(
                instruction=f"Check whether the recently deleted location ({location}) is deleted from favourites section of the vehicle",
                test_id="003",
                service=img_service,
                take_screenshot = False
            )

    except Exception as e:
        error_log(e, "003", img_service)

def Nav_Companion_004():
    try:
        if app_login_setup():
            manual_check(
                instruction="1. In Vehicle, Launch Navigation and go to 'Navigation-Recent destination and tours' screen\n2. Select any of location info from the list and delete it from vehicle side",
                test_id="004",
                service=img_service
            )
            controller.click_by_image("Icons/navigation_icon.png")
            controller.click_by_image("Images/Navigation_Allow.png")
            controller.click_by_image("Images/Navigation_Search_Image.png")
            controller.swipe_down()

            while not compare_with_expected_crop("Images/no_sent_destinations.png"):
                controller.small_swipe_up()
                if controller.is_text_present("DEALERS"):
                    break

            if compare_with_expected_crop("Images/no_sent_destinations.png"):
                log("Recently deleted location not displayed under 'Sent destinations'")
            else:
                fail_log("Recently deleted location not displayed under 'Sent destinations'", "004", img_service)

            controller.click_by_image("Icons/location_back.png")

    except Exception as e:
        error_log(e, "004", img_service)

def Nav_Companion_005():
    try:
        if app_login_setup():
            # if manual
            controller.click_by_image("Icons/navigation_icon.png")
            controller.click_by_image("Images/Navigation_Allow.png")
            controller.click_by_image("Images/Navigation_Search_Image.png")
            location = "Crewe"
            controller.enter_text(location)
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/textView_list_item_poi_title")
            controller.click_by_image("Icons/location_favourite_unselected.png")
            if controller.wait_for_text(f"{location} saved successfully as favorite"):
                log("Location saved as favourite")
            else:
                fail_log("Location not saved as favourite", "005", img_service)
            controller.click_by_image("Icons/location_back.png")
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

            manual_check(
                instruction="1. In Vehicle, Launch Navigation and go to 'Navigation-Favourites' screen\n2. Select any of the favourite location info from the list and delete it from vehicle side",
                test_id="005",
                service=img_service
            )

            controller.click_by_image("Icons/navigation_icon.png")
            controller.click_by_image("Images/Navigation_Search_Image.png")
            controller.click_by_image("Images/Navigation_Allow.png")
            controller.click_text("NAVIGATION")

            if controller.is_text_present("Currently no favorites added. To add a favorites in your app destinations, use the search field in this view. The added app favorites could be synced to your vehicle."):
                log("Favourite location deleted from app")
            else:
                fail_log("Favourite location not deleted from app", "005", img_service)

            controller.click_by_image("Icons/location_back.png")
    except Exception as e:
        error_log(e, "005", img_service)

def Nav_Companion_006():
    try:
        if app_login_setup():
            controller.click_by_image("Icons/navigation_icon.png")
            controller.click_by_image("Images/Navigation_Allow.png")
            controller.click_by_image("Images/Navigation_Search_Image.png")
            location = "Crewe"
            controller.enter_text(location)
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/textView_list_item_poi_title")
            if controller.click_text("SEND TO CAR"):
                log("Location sent to car")
            else:
                fail_log("Send to car button not found", "006", img_service)
            controller.click_by_image("Icons/navigation_back.png")
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

            manual_check(
                instruction="",
                test_id="006",
                service=img_service
            )

            controller.click_by_image("Icons/navigation_icon.png")
            controller.click_by_image("Images/Navigation_Search_Image.png")
            controller.click_text("NAVIGATION")
            controller.delete_sent_location()
            if controller.wait_for_text("Currently no places found. To find a destination use the search field."):
                log("Sent location deleted from app")
            else:
                fail_log("Sent location not deleted from app", "006", img_service)
            controller.click_by_image("Icons/navigation_back.png")

            manual_check(
                instruction="",
                test_id="006",
                service=img_service
            )

    except Exception as e:
        error_log(e, "006", img_service)

def Nav_Companion_007():
    try:
        if app_login_setup():
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            car = identify_car()
            controller.click_by_image("Icons/navigation_icon.png")
            controller.click_by_image("Images/Navigation_Allow.png")
            controller.click_by_image("Images/Navigation_Search_Image.png")
            controller.click_text("NAVIGATION")
            controller.swipe_up()

            if controller.click_by_resource_id("uk.co.bentley.mybentley:id/textView_list_item_poi_title"):
                log("Dealer information opened")
            else:
                fail_log("A Bentley dealer could not be found", "007", img_service)

            dealer_title = controller.d(resourceId="uk.co.bentley.mybentley:id/textView_fragment_poi_detail_card_title").get_text()
            controller.click_text("SEND TO CAR")
            if controller.wait_for_text(f"{dealer_title} sent successfully to {car}"):
                log("Dealer sent to car")
            else:
                fail_log("Dealer failed to be sent to car", "007", img_service)
            controller.click_by_image("Icons/navigation_back.png")
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

            manual_check(
                instruction="",
                test_id="007",
                service=img_service
            )

            controller.click_by_image("Icons/navigation_icon.png")
            controller.click_by_image("Images/Navigation_Search_Image.png")
            controller.click_text("NAVIGATION")
            controller.delete_sent_location()
            if controller.wait_for_text("Currently no places found. To find a destination use the search field."):
                log("Sent dealer deleted from app")
            else:
                fail_log("Sent dealer not deleted from app", "007", img_service)
            controller.click_by_image("Icons/navigation_back.png")

            manual_check(
                instruction="",
                test_id="007",
                service=img_service
            )

    except Exception as e:
        error_log(e, "007", img_service)

def Nav_Companion_008():
    try:
        if app_login_setup():
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            car = identify_car()
            controller.click_by_image("Icons/navigation_icon.png")
            controller.click_by_image("Images/Navigation_Allow.png")
            controller.click_by_image("Images/Navigation_Search_Image.png")
            location = "Huddersfield"
            controller.enter_text(location)
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/textView_list_item_poi_title")
            if controller.click_by_image("Icons/location_favourite_unselected.png"):
                log("Location saved as favourite")
            else:
                fail_log("Location not saved as favourite", "008", img_service)
            controller.click_text("SEND TO CAR")
            if controller.wait_for_text(f"{location} sent successfully to {car}"):
                log("Location sent to car")
            controller.click_by_image("Icons/navigation_back.png")

            manual_check(
                instruction="",
                test_id="008",
                service=img_service
            )

    except Exception as e:
        error_log(e, "008", img_service)

def Nav_Companion_009():
    try:
        blocked_log("Test blocked - Not written due to issues")
    except Exception as e:
        error_log(e, "009", img_service)

def Nav_Companion_010():
    try:
        controller.click_by_image("Icons/navigation_icon.png")
        controller.click_by_image("Images/Navigation_Allow.png")
        controller.click_by_image("Images/Navigation_Search_Image.png")
        controller.click_text("NAVIGATION")
        controller.swipe_up()
        if not controller.is_text_present("CALENDAR"):
            controller.swipe_up()

        if controller.wait_for_text_that_contains("Currently no events found", 1):
            log("No contacts with saved addresses displayed in Calendar section")
        elif False:
            pass
            # What shows when there are calendar events??
        controller.click_by_image("Icons/navigation_back.png")
    except Exception as e:
        error_log(e, "010", img_service)

def Nav_Companion_011():
    try:
        controller.click_by_image("Icons/navigation_icon.png")
        controller.click_by_image("Images/Navigation_Allow.png")
        controller.click_by_image("Images/Navigation_Search_Image.png")
        controller.click_text("NAVIGATION")
        controller.swipe_up()
        if not controller.is_text_present("CONTACTS"):
            controller.swipe_up()

        if controller.wait_for_text_that_contains("Currently no contacts found", 1):
            log("No events with saved addresses displayed")
        elif False:
            pass
            # What shows when there are contacts??
        controller.click_by_image("Icons/navigation_back.png")

    except Exception as e:
        error_log(e, "011", img_service)

def Nav_Companion_012():
    try:
        blocked_log("Test blocked - Can't check style guide")
    except Exception as e:
        error_log(e, "012", img_service)
