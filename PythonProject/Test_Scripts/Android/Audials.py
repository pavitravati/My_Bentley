from common_utils.android_image_comparision import *
from core.log_emitter import log_emitter

def log(msg):
    log_emitter.log_signal.emit(msg)

def fail_log(msg, num):
    log(f"{msg}")
    controller.take_fail_screenshot(f"Audials-{msg}-{num}.png")

def error_log(e, num):
    log(f"⚠️ - Unexpected error: {e}")
    controller.take_fail_screenshot(f"Audials-{e}-{num}.png")

def Audials_001():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/windows_icon.png")

        for _ in range(3):
            controller.swipe_up()

        if controller.click_text("AUDIALS"):
            log("✅ - Audials section clicked")
        else:
            fail_log("❌ - Audials section not clicked", "001")

        controller.click_text("OK")
        if controller.is_text_present("audials.com"):
            log("✅ - Redirected to Audials.com")
        else:
            fail_log("❌ - Failed to redirect to Audials.com", "001")

        controller.press_home()
        controller.launch_app("uk.co.bentley.mybentley")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "001")

# Font checking test
def Audials_002():
    try:
        log("✅ - Cannot check style")
    except Exception as e:
        error_log(e, "002")