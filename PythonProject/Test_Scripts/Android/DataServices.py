from time import sleep
from common_utils.android_image_comparision import *
from common_utils.android_controller import *
from core.log_emitter import log_emitter

def log(msg):
    log_emitter.log_signal.emit(msg)

def fail_log(msg, num):
    log(f"{msg}")
    controller.take_fail_screenshot(f"DataServices_{msg}_{num}.png")

def error_log(e, num):
    log(f"⚠️ - Unexpected error: {e}")
    controller.take_fail_screenshot(f"DataServices_{e}_{num}.png")

def DataServices_001():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")
        for _ in range(2):
            controller.swipe_up()
        controller.click_text("DATA SERVICES")
        if controller.click_text("VISIT STORE"):
            log("✅ - Bentley Support Centre web launched")
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

    except Exception as e:
        error_log(e, "001")

# Test is about style guide
def DataServices_002():
    try:
        pass
    except Exception as e:
        error_log(e, "002")