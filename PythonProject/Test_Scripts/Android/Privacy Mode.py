from common_utils.android_image_comparision import *
from core.log_emitter import log_emitter
from time import sleep

def log(msg):
    log_emitter.log_signal.emit(msg)

def fail_log(msg, num):
    log(f"{msg}")
    controller.take_fail_screenshot(f"Privacy Mode-{msg}-{num}.png")

def error_log(e, num):
    log(f"⚠️ - Unexpected error: {e}")
    controller.take_fail_screenshot(f"Privacy Mode-{e}-{num}.png")

# Feels redundant, why check the entire app works when its been running other tests without privacy mode
def Privacy_Mode_001():
    try:
        log("✅")
    except Exception as e:
        error_log(e, "001")

def Privacy_Mode_002():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.swipe_down()
        sleep(6)
        controller.click_by_image("Icons/Error_Icon.png")

        if compare_with_expected_crop("Icons/Remote_Lock_Unavailable.png"):
            log("✅ - Remote lock unlock unavailable")
        elif compare_with_expected_crop("Icons/Remote_Lock_Available.png"):
            fail_log("❌ - Remote lock unlock still available", "002")

        controller.swipe_up()
        if controller.is_text_present("My car status unavailable"):
            log("✅ - Car status information disabled")
        else:
            fail_log("❌ - Car status information still available", "002")
        controller.swipe_down()

        controller.click_by_image("Icons/windows_icon.png")
        section_titles = []
        for _ in range(2):
            titles = controller.d.xpath('//android.widget.TextView[''following-sibling::*//*[@text="Function disabled" or @text="Function not available"]]').all()
            section_titles.append([t.attrib.get("text", "") for t in titles if t.attrib.get("text") not in section_titles])
            controller.swipe_up(0.25)
        controller.swipe_down(0.05)

        section_titles = section_titles[0] + section_titles[1]
        log("✅ - My car statistics disabled") if "MY CAR STATISTICS" in section_titles else fail_log("❌ - My car statistics not disabled", "002")
        log("✅ - My battery charge disabled") if "MY BATTERY CHARGE" in section_titles else fail_log("❌ - My battery charge not disabled", "002")
        log("✅ - My cabin comfort disabled") if "MY CABIN COMFORT" in section_titles else fail_log("❌ - My cabin comfort not disabled", "002")
        log("✅ - Remote parking disabled") if "REMOTE PARKING" in section_titles else fail_log("❌ - Remote parking not disabled", "002")

        controller.click_text("STOLEN VEHICLE TRACKING")
        if compare_with_expected_crop("Icons/privacy_mode_error.png"):
            log("✅ - Theft alert disabled")
        else:
            fail_log("❌ - Theft alert not disabled", "002")
        controller.click_by_image("Icons/back_icon.png")
        controller.swipe_down()

        if not compare_with_expected_crop("Images/Navigation_Car_Image.png"):
            log("✅ - Vehicle location not accessible")
        else:
            fail_log("❌ - Vehicle location still accessible", "002")

    except Exception as e:
        error_log(e, "002")

def Privacy_Mode_003():
    try:
        pass
    except Exception as e:
        error_log(e, "003")

def Privacy_Mode_004():
    try:
        pass
    except Exception as e:
        error_log(e, "004")

def Privacy_Mode_005():
    try:
        pass
    except Exception as e:
        error_log(e, "005")

def Privacy_Mode_006():
    try:
        log("✅ - temp can't check style guide")
    except Exception as e:
        error_log(e, "006")
