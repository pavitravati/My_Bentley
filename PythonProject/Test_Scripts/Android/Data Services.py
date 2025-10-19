from time import sleep
from common_utils.android_image_comparision import *
from core.log_emitter import log_emitter

def log(msg):
    log_emitter.log_signal.emit(msg)

def fail_log(msg, num):
    log(f"{msg}")
    controller.take_fail_screenshot(f"Data Services-{msg}-{num}.png")

def error_log(e, num):
    log(f"⚠️ - Unexpected error: {e}")
    controller.take_fail_screenshot(f"Data Services-{e}-{num}.png")

# Make sure this works using better wifi as it struggles on bad wifi
def Data_Services_001():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        for _ in range(2):
            controller.swipe_up()
        controller.click_text("DATA SERVICES")
        if controller.click_text("VISIT STORE"):
            log("✅ - Bentley Support Centre web launched")
            controller.wait_for_text_and_click("AGREE TO ALL")
        else:
            fail_log("❌ - Bentley Support Centre web not launched", "001")
        sleep(5)

        controller.swipe_up()
        controller.click_text("BUY DATA")
        sleep(5)
        if controller.is_text_present("Connect Now"):
            log("✅ - Data Service Provider web launched")
        else:
            fail_log("❌ - Data Service Provider web not launched", "001")

        controller.press_home()
        controller.launch_app("uk.co.bentley.mybentley")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "001")

def Data_Services_002():
    try:
        pass
    except Exception as e:
        error_log(e, "002")

def Data_Services_003():
    try:
        pass
    except Exception as e:
        error_log(e, "003")

def Data_Services_004():
    try:
        pass
    except Exception as e:
        error_log(e, "004")

def Data_Services_005():
    try:
        pass
    except Exception as e:
        error_log(e, "005")