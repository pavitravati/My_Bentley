from time import sleep
from common_utils.android_image_comparision import *
from common_utils.android_controller import *
from core.log_emitter import log, fail_log, error_log, metric_log

img_service = "Remote Honk Flash"
controller.take_screenshot()

# Cannot test without china app
def Remote_Honk_Flash_001():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        if compare_with_expected_crop("Icons/remote_honk.png"):
            log("Remote Honk button displayed")
        else:
            fail_log("Remote Honk button not displayed", "001", img_service)

        if compare_with_expected_crop("Icons/remote_flash.png"):
            log("Remote Flash button displayed")
        else:
            fail_log("Remote Flash button not displayed", "001", img_service)
    except Exception as e:
        error_log(e, "001", img_service)

def Remote_Honk_Flash_002():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        if controller.click_by_image("Icons/remote_honk.png"):
            log("Remote Honk button pressed")
        else:
            fail_log("Remote Honk button not pressed", "002", img_service)

        controller.click_text("USE OF HORN IS PERMITTED")
        if controller.wait_for_text("Horn activated successfully"):
            log("Horn activated in the app")
        else:
            fail_log("Horn failed to be activated in app", "002", img_service)

    except Exception as e:
        error_log(e, "002", img_service)

def Remote_Honk_Flash_003():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/remote_honk.png")
        controller.click_text("USE OF HORN IS PERMITTED")
        if controller.wait_for_text("Horn activated successfully"):
            log("Horn activated in the app")
        else:
            fail_log("Horn failed to be activated in app", "003", img_service)
    except Exception as e:
        error_log(e, "003", img_service)

def Remote_Honk_Flash_004():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/remote_honk.png")
        controller.click_text("USE OF HORN IS PERMITTED")
        if controller.wait_for_text("Horn activated successfully"):
            log("Horn activated in the app")
        else:
            fail_log("Horn failed to be activated in app", "004", img_service)
    except Exception as e:
        error_log(e, "004", img_service)

def Remote_Honk_Flash_005():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/remote_honk.png")
        controller.click_text("USE OF HORN IS PERMITTED")
        if controller.wait_for_text("Horn activated successfully"):
            log("Horn activated in the app")
        else:
            fail_log("Horn failed to be activated in app", "005", img_service)
    except Exception as e:
        error_log(e, "005", img_service)

def Remote_Honk_Flash_006():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/remote_honk.png")
        controller.click_text("USE OF HORN IS PERMITTED")
        if controller.wait_for_text("Horn activated successfully"):
            log("Horn activated in the app")
        else:
            fail_log("Horn failed to be activated in app", "006", img_service)
    except Exception as e:
        error_log(e, "006", img_service)

def Remote_Honk_Flash_007():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/remote_honk.png")
        controller.click_text("USE OF HORN IS PERMITTED")
        if controller.wait_for_text("Horn activated successfully"):
            log("Horn activated in the app")
        else:
            fail_log("Horn failed to be activated in app", "007", img_service)
    except Exception as e:
        error_log(e, "007", img_service)

def Remote_Honk_Flash_008():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/remote_honk.png")
        controller.click_text("USE OF HORN IS PERMITTED")
        # What is shown in the app when hazards are on
    except Exception as e:
        error_log(e, "008", img_service)

def Remote_Honk_Flash_009():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/remote_honk.png")
        controller.click_text("USE OF HORN IS PERMITTED")
        # What is shown in the app when far away from vehicle
    except Exception as e:
        error_log(e, "009", img_service)

def Remote_Honk_Flash_010():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/remote_flash.png")
        controller.click_text("USE OF LIGHTS IS PERMITTED")

        if controller.wait_for_text("Lights activated successfully"):
            log("Lights activated in the app")
        else:
            fail_log("Lights failed to be activated in app", "010", img_service)

    except Exception as e:
        error_log(e, "010", img_service)

def Remote_Honk_Flash_011():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/remote_flash.png")
        controller.click_text("USE OF LIGHTS IS PERMITTED")

        if controller.wait_for_text("Lights activated successfully"):
            log("Lights activated in the app")
        else:
            fail_log("Lights failed to be activated in app", "011", img_service)
    except Exception as e:
        error_log(e, "011", img_service)

def Remote_Honk_Flash_012():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/remote_flash.png")
        controller.click_text("USE OF LIGHTS IS PERMITTED")

        if controller.wait_for_text("Lights activated successfully"):
            log("Lights activated in the app")
        else:
            fail_log("Lights failed to be activated in app", "012", img_service)
    except Exception as e:
        error_log(e, "012", img_service)

def Remote_Honk_Flash_013():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/remote_flash.png")
        controller.click_text("USE OF LIGHTS IS PERMITTED")

        if controller.wait_for_text("Lights activated successfully"):
            log("Lights activated in the app")
        else:
            fail_log("Lights failed to be activated in app", "013", img_service)
    except Exception as e:
        error_log(e, "013", img_service)

def Remote_Honk_Flash_014():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/remote_flash.png")
        controller.click_text("USE OF LIGHTS IS PERMITTED")

        if controller.wait_for_text("Lights activated successfully"):
            log("Lights activated in the app")
        else:
            fail_log("Lights failed to be activated in app", "014", img_service)
    except Exception as e:
        error_log(e, "014", img_service)

def Remote_Honk_Flash_015():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/remote_flash.png")
        controller.click_text("USE OF LIGHTS IS PERMITTED")

        if controller.wait_for_text("Lights activated successfully"):
            log("Lights activated in the app")
        else:
            fail_log("Lights failed to be activated in app", "013", img_service)
    except Exception as e:
        error_log(e, "015", img_service)

def Remote_Honk_Flash_016():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/remote_flash.png")
        controller.click_text("USE OF LIGHTS IS PERMITTED")
        # What is shown in the app when hazards are on

    except Exception as e:
        error_log(e, "016", img_service)

def Remote_Honk_Flash_017():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/remote_flash.png")
        controller.click_text("USE OF LIGHTS IS PERMITTED")
        # What is shown in the app when far away from vehicle

    except Exception as e:
        error_log(e, "017", img_service)

def Remote_Honk_Flash_018():
    try:
        log("✅ - temp, can't check style guide")
    except Exception as e:
        error_log(e, "018", img_service)