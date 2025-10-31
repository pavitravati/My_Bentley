from common_utils.android_image_comparision import *
from core.log_emitter import log, fail_log, error_log, metric_log

img_service = "Nav Companion"

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

def Nav_Companion_001():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
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

        car_icon = False
        car_names = ['Bentayga', 'FlyingSpur', 'ContinentalGT', 'ContinentalGTC']
        for _ in range(4):
            if compare_with_expected_crop(f"Images/Navigation_{car_names[_]}_Image.png"):
                car_icon = True

        if controller.click_by_image("Images/Navigation_Car_Image.png"):
            if car_icon:
                log("Car Icon displayed and shows current location of vehicle")
            else:
                fail_log("Car Icon displayed but does not show current location of vehicle", "001", img_service)
        else:
            fail_log("Car Icon not displayed", "001", img_service)

        if controller.click_by_image("Images/Navigation_User_Image.png") and compare_with_expected_crop("Images/Navigation_User_Icon.png"):
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
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "001", img_service)

def Nav_Companion_002():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
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

        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "002", img_service)

def Nav_Companion_003():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        car = identify_car()
        controller.click_by_image("Icons/navigation_icon.png")
        controller.click_by_image("Images/Navigation_Allow.png")
        controller.click_by_image("Images/Navigation_Search_Image.png")
        controller.enter_text("London")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/textView_list_item_poi_title")

        if controller.click_text("SEND TO CAR"):
            log("Location sent to car")
        else:
            fail_log("Send to car button not displayed", "003", img_service)

        if controller.wait_for_text(f"London sent successfully to {car}"):
            log("Location sent confirmation message received")
        else:
            fail_log("Location sent confirmation message not received", "003", img_service)
        controller.click_by_image("Icons/location_back.png")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

        ##############
        # wait for checking in car
        ##############
    except Exception as e:
        error_log(e, "003", img_service)

def Nav_Companion_004():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/navigation_icon.png")
        controller.click_by_image("Images/Navigation_Allow.png")
        controller.click_by_image("Images/Navigation_Search_Image.png")
        controller.click_text("NAVIGATION")

        if controller.is_text_present("London"):
            controller.delete_sent_location()
            if controller.wait_for_text("Currently no places found. To find a destination use the search field."):
                log("Sent location deleted from app")
            else:
                fail_log("Sent location not deleted from app", "004", img_service)

        controller.click_by_image("Icons/location_back.png")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "004", img_service)

def Nav_Companion_005():
    try:
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
            fail_log("Location not saved as favourite", "005", img_service)

        if controller.is_text_present("SEND TO CAR"):
            log("Location sent to car")
        else:
            fail_log("Send to car button not displayed", "005", img_service)

        if controller.wait_for_text(f"{location} sent successfully to {car}"):
            log("Location sent confirmation message received")
        else:
            fail_log("Location sent confirmation message not received", "005", img_service)

        ##############
        # wait for checking in car
        ##############

        controller.click_by_image("Icons/location_back.png")
        controller.click_by_image("Images/Navigation_Search_Image.png")
        controller.click_text("NAVIGATION")
        controller.delete_favourite_location() # Kind of broken
        controller.click_by_image("Icons/location_back.png")

        ##############
        # wait for checking in car
        ##############

    except Exception as e:
        error_log(e, "005", img_service)

def Nav_Companion_006():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/navigation_icon.png")
        controller.click_by_image("Images/Navigation_Allow.png")
        controller.click_by_image("Images/Navigation_Search_Image.png")
        location = "London"
        controller.enter_text(location)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/textView_list_item_poi_title")
        controller.click_text("SEND TO CAR")
        controller.click_by_image("Icons/location_back.png")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

        ##########
        # Wait for in car stuff
        ##########

        controller.click_by_image("Icons/navigation_icon.png")
        controller.click_by_image("Images/Navigation_Search_Image.png")
        controller.click_text("NAVIGATION")

        if controller.is_text_present("Currently no places found. To find a destination use the search field."):
            log("Sent location deleted from app")
        else:
            fail_log("Sent location not deleted from app", "006", img_service)

        controller.click_by_image("Icons/location_back.png")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "006", img_service)

def Nav_Companion_007():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
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
            fail_log("Location not saved as favourite", "007", img_service)
        controller.click_by_image("Icons/location_back.png")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

        ##########
        # Wait for in car stuff
        ##########

        controller.click_by_image("Icons/navigation_icon.png")
        controller.click_by_image("Images/Navigation_Search_Image.png")
        controller.click_text("NAVIGATION")

        if controller.is_text_present("Currently no favorites added. To add a favorites in your app destinations, use the search field in this view. The added app favorites could be synced to your vehicle."):
            log("Favourite location deleted from app")
        else:
            fail_log("Favourite location not deleted from app", "007", img_service)

        controller.click_by_image("Icons/location_back.png")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "007", img_service)

def Nav_Companion_008():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/navigation_icon.png")
        controller.click_by_image("Images/Navigation_Allow.png")
        controller.click_by_image("Images/Navigation_Search_Image.png")
        location = "Crewe"
        controller.enter_text(location)
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/textView_list_item_poi_title")
        if controller.click_text("SEND TO CAR"):
            log("Location sent to car")
        else:
            fail_log("Send to car button not found", "008", img_service)
        controller.click_by_image("Icons/navigation_back.png")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

        ##########
        # Wait for in car stuff
        ##########

        controller.click_by_image("Icons/navigation_icon.png")
        controller.click_by_image("Images/Navigation_Search_Image.png")
        controller.click_text("NAVIGATION")
        controller.delete_sent_location()
        if controller.wait_for_text("Currently no places found. To find a destination use the search field."):
            log("Sent location deleted from app")
        else:
            fail_log("Sent location not deleted from app", "004", img_service)
        controller.click_by_image("Icons/navigation_back.png")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

        ##########
        # Check in car stuff
        ##########

    except Exception as e:
        error_log(e, "008", img_service)

def Nav_Companion_009():
    try:
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
            fail_log("A Bentley dealer could not be found", "009", img_service)

        dealer_title = controller.d(resourceId="uk.co.bentley.mybentley:id/textView_fragment_poi_detail_card_title").get_text()
        controller.click_text("SEND TO CAR")
        if controller.wait_for_text(f"{dealer_title} sent successfully to {car}"):
            log("Dealer sent to car")
        else:
            fail_log("Dealer failed to be sent to car", "009", img_service)
        controller.click_by_image("Icons/navigation_back.png")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

        ##########
        # Wait for in car stuff
        ##########

        controller.click_by_image("Icons/navigation_icon.png")
        controller.click_by_image("Images/Navigation_Search_Image.png")
        controller.click_text("NAVIGATION")
        controller.delete_sent_location()
        if controller.wait_for_text("Currently no places found. To find a destination use the search field."):
            log("Sent dealer deleted from app")
        else:
            fail_log("Sent dealer not deleted from app", "009", img_service)
        controller.click_by_image("Icons/navigation_back.png")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

        ##########
        # Check in car stuff
        ##########

    except Exception as e:
        error_log(e, "009", img_service)

def Nav_Companion_010():
    try:
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
            fail_log("Location not saved as favourite", "010", img_service)
        controller.click_text("SEND TO CAR")
        if controller.wait_for_text(f"{location} sent successfully to {car}"):
            log("Location sent to car")
        controller.click_by_image("Icons/navigation_back.png")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

        ##########
        # Check in car stuff
        ##########
    except Exception as e:
        error_log(e, "010", img_service)

def Nav_Companion_011():
    try:
        pass
    except Exception as e:
        error_log(e, "011", img_service)

def Nav_Companion_012():
    try:
        pass
    except Exception as e:
        error_log(e, "012", img_service)

def Nav_Companion_013():
    try:
        pass
    except Exception as e:
        error_log(e, "013", img_service)

def Nav_Companion_014():
    try:
        log("Cannot complete style guide testcases (temporary)")
    except Exception as e:
        error_log(e, "014", img_service)
