from time import sleep
from common_utils.android_image_comparision import *
from common_utils.android_controller import *
from core.app_functions import app_login_setup, service_reset
from core.log_emitter import log, fail_log, error_log, metric_log, blocked_log, runtime_log
from core.globals import country
from core.globals import manual_run
from core.screenrecord import ScreenRecorder

img_service = "Remote Honk Flash"
recorder = ScreenRecorder(device_serial=controller.d.serial)

# Cannot test without china app
def Remote_Honk_Flash_001():
    recorder.start(f"{img_service}-001")
    try:
        if country == "chn":
            if app_login_setup():
                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
                if compare_with_expected_crop("Icons/remote_honk.png"):
                    log("Remote Honk button displayed")
                else:
                    fail_log("Remote Honk button not displayed", "001", img_service)

                if compare_with_expected_crop("Icons/remote_flash.png"):
                    log("Remote Flash button displayed")
                else:
                    fail_log("Remote Flash button not displayed", "001", img_service)
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "001", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Honk_Flash_002():
    recorder.start(f"{img_service}-002")
    try:
        if country == "chn":
            if app_login_setup():
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
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "002", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Honk_Flash_003():
    recorder.start(f"{img_service}-003")
    try:
        if country == "chn":
            if app_login_setup():
                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
                controller.click_by_image("Icons/remote_honk.png")
                controller.click_text("USE OF HORN IS PERMITTED")
                if controller.wait_for_text("Horn activated successfully"):
                    log("Horn activated in the app")
                else:
                    fail_log("Horn failed to be activated in app", "003", img_service)
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "003", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Honk_Flash_004():
    recorder.start(f"{img_service}-004")
    try:
        if country == "chn":
            if app_login_setup():
                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
                controller.click_by_image("Icons/remote_honk.png")
                controller.click_text("USE OF HORN IS PERMITTED")
                if controller.wait_for_text("Horn activated successfully"):
                    log("Horn activated in the app")
                else:
                    fail_log("Horn failed to be activated in app", "004", img_service)
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "004", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Honk_Flash_005():
    recorder.start(f"{img_service}-005")
    try:
        if country == "chn":
            if app_login_setup():
                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
                controller.click_by_image("Icons/remote_honk.png")
                controller.click_text("USE OF HORN IS PERMITTED")
                if controller.wait_for_text("Horn activated successfully"):
                    log("Horn activated in the app")
                else:
                    fail_log("Horn failed to be activated in app", "005", img_service)
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "005", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Honk_Flash_006():
    recorder.start(f"{img_service}-006")
    try:
        if country == "chn":
            if app_login_setup():
                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
                controller.click_by_image("Icons/remote_honk.png")
                controller.click_text("USE OF HORN IS PERMITTED")
                if controller.wait_for_text("Horn activated successfully"):
                    log("Horn activated in the app")
                else:
                    fail_log("Horn failed to be activated in app", "006", img_service)
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "006", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Honk_Flash_007():
    recorder.start(f"{img_service}-007")
    try:
        if country == "chn":
            if app_login_setup():
                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
                controller.click_by_image("Icons/remote_honk.png")
                controller.click_text("USE OF HORN IS PERMITTED")
                if controller.wait_for_text("Horn activated successfully"):
                    log("Horn activated in the app")
                else:
                    fail_log("Horn failed to be activated in app", "007", img_service)
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "007", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Honk_Flash_008():
    recorder.start(f"{img_service}-008")
    try:
        if country == "chn":
            if app_login_setup():
                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
                controller.click_by_image("Icons/remote_honk.png")
                controller.click_text("USE OF HORN IS PERMITTED")
                # What is shown in the app when hazards are on
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "008", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Honk_Flash_009():
    recorder.start(f"{img_service}-009")
    try:
        if country == "chn":
            if app_login_setup():
                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
                controller.click_by_image("Icons/remote_honk.png")
                controller.click_text("USE OF HORN IS PERMITTED")
                # What is shown in the app when far away from vehicle
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "009", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Honk_Flash_010():
    recorder.start(f"{img_service}-010")
    try:
        if country == "chn":
            if app_login_setup():
                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
                controller.click_by_image("Icons/remote_flash.png")
                controller.click_text("USE OF LIGHTS IS PERMITTED")

                if controller.wait_for_text("Lights activated successfully"):
                    log("Lights activated in the app")
                else:
                    fail_log("Lights failed to be activated in app", "010", img_service)
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "010", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Honk_Flash_011():
    recorder.start(f"{img_service}-011")
    try:
        if country == "chn":
            if app_login_setup():
                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
                controller.click_by_image("Icons/remote_flash.png")
                controller.click_text("USE OF LIGHTS IS PERMITTED")

                if controller.wait_for_text("Lights activated successfully"):
                    log("Lights activated in the app")
                else:
                    fail_log("Lights failed to be activated in app", "011", img_service)
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "011", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Honk_Flash_012():
    recorder.start(f"{img_service}-012")
    try:
        if country == "chn":
            if app_login_setup():
                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
                controller.click_by_image("Icons/remote_flash.png")
                controller.click_text("USE OF LIGHTS IS PERMITTED")

                if controller.wait_for_text("Lights activated successfully"):
                    log("Lights activated in the app")
                else:
                    fail_log("Lights failed to be activated in app", "012", img_service)
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "012", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Honk_Flash_013():
    recorder.start(f"{img_service}-013")
    try:
        if country == "chn":
            if app_login_setup():
                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
                controller.click_by_image("Icons/remote_flash.png")
                controller.click_text("USE OF LIGHTS IS PERMITTED")

                if controller.wait_for_text("Lights activated successfully"):
                    log("Lights activated in the app")
                else:
                    fail_log("Lights failed to be activated in app", "013", img_service)
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "013", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Honk_Flash_014():
    recorder.start(f"{img_service}-014")
    try:
        if country == "chn":
            if app_login_setup():
                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
                controller.click_by_image("Icons/remote_flash.png")
                controller.click_text("USE OF LIGHTS IS PERMITTED")

                if controller.wait_for_text("Lights activated successfully"):
                    log("Lights activated in the app")
                else:
                    fail_log("Lights failed to be activated in app", "014", img_service)
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "014", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Honk_Flash_015():
    recorder.start(f"{img_service}-015")
    try:
        if country == "chn":
            if app_login_setup():
                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
                controller.click_by_image("Icons/remote_flash.png")
                controller.click_text("USE OF LIGHTS IS PERMITTED")

                if controller.wait_for_text("Lights activated successfully"):
                    log("Lights activated in the app")
                else:
                    fail_log("Lights failed to be activated in app", "013", img_service)
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "015", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Honk_Flash_016():
    recorder.start(f"{img_service}-016")
    try:
        if country == "chn":
            if app_login_setup():
                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
                controller.click_by_image("Icons/remote_flash.png")
                controller.click_text("USE OF LIGHTS IS PERMITTED")
                # What is shown in the app when hazards are on
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "016", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Honk_Flash_017():
    recorder.start(f"{img_service}-017")
    try:
        if country == "chn":
            if app_login_setup():
                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
                controller.click_by_image("Icons/remote_flash.png")
                controller.click_text("USE OF LIGHTS IS PERMITTED")
                # What is shown in the app when far away from vehicle
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "017", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Honk_Flash_018():
    recorder.start(f"{img_service}-018")
    try:
        if country == "chn":
            blocked_log("Test blocked - Can't check style guide")
        else:
            blocked_log("Test blocked - Region locked (CHN)")
    except Exception as e:
        error_log(e, "018", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False