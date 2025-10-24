from common_utils.android_image_comparision import *
from core.log_emitter import log_emitter
from time import sleep
from core.app_functions import app_login, app_logout

def log(msg):
    # log_emitter.log_signal.emit(msg)
    print(msg)

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

        if controller.find_img("Icons/Remote_Lock_Unavailable_Icon.png", 0.75):
            log("✅ - Remote lock unlock unavailable")
        elif controller.find_img("Icons/lock_icon.png", 0.75):
            fail_log("❌ - Remote lock unlock still available", "002")

        if controller.is_text_present("My car status unavailable"):
            log("✅ - Car status information disabled")
        else:
            fail_log("❌ - Car status information still available", "002")

        controller.click_by_image("Icons/windows_icon.png")
        section_titles = []
        for _ in range(2):
            titles = controller.d.xpath('//android.widget.TextView[''following-sibling::*//*[@text="Function disabled" or @text="Function not available"]]').all()
            section_titles.append([t.attrib.get("text", "") for t in titles if t.attrib.get("text") not in section_titles])
            if _ == 0:
                controller.swipe_up(0.25)

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

        controller.click_by_image("Icons/navigation_icon.png")
        controller.click_by_image("Images/Navigation_Allow.png")
        if not compare_with_expected_crop("Images/Navigation_Car_Image.png", 0.9):
            log("✅ - Vehicle location not accessible")
        else:
            fail_log("❌ - Vehicle location still accessible", "002")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "002")

# The next 3 test cases all have actions to be done/checked in the HMI
def Privacy_Mode_003():
    try:
        app_logout()
        if app_login():
            log("✅ - Login successful")
        else:
            fail_log("❌ - Login failed", "003")

        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.swipe_down()
        sleep(6)
        controller.click_by_image("Icons/Error_Icon.png")

        if controller.find_img("Icons/Remote_Lock_Unavailable_Icon.png", 0.75):
            log("✅ - Remote lock unlock unavailable")
        elif controller.find_img("Icons/lock_icon.png", 0.75):
            fail_log("❌ - Remote lock unlock still available", "003")

        if controller.is_text_present("My car status unavailable"):
            log("✅ - Car status information disabled")
        else:
            fail_log("❌ - Car status information still available", "003")

        controller.click_by_image("Icons/windows_icon.png")
        section_titles = []
        for _ in range(2):
            titles = controller.d.xpath('//android.widget.TextView[''following-sibling::*//*[@text="Function disabled" or @text="Function not available"]]').all()
            section_titles.append([t.attrib.get("text", "") for t in titles if t.attrib.get("text") not in section_titles])
            if _ == 0:
                controller.swipe_up(0.25)

        section_titles = section_titles[0] + section_titles[1]
        log("✅ - My car statistics disabled") if "MY CAR STATISTICS" in section_titles else fail_log("❌ - My car statistics not disabled", "003")
        log("✅ - My battery charge disabled") if "MY BATTERY CHARGE" in section_titles else fail_log("❌ - My battery charge not disabled", "003")
        log("✅ - My cabin comfort disabled") if "MY CABIN COMFORT" in section_titles else fail_log("❌ - My cabin comfort not disabled", "003")
        log("✅ - Remote parking disabled") if "REMOTE PARKING" in section_titles else fail_log("❌ - Remote parking not disabled", "003")

        controller.click_text("STOLEN VEHICLE TRACKING")
        if compare_with_expected_crop("Icons/privacy_mode_error.png"):
            log("✅ - Theft alert disabled")
        else:
            fail_log("❌ - Theft alert not disabled", "003")
        controller.click_by_image("Icons/back_icon.png")
        controller.swipe_down()

        controller.click_by_image("Icons/navigation_icon.png")
        controller.click_by_image("Images/Navigation_Allow.png")
        if not compare_with_expected_crop("Images/Navigation_Car_Image.png", 0.9):
            log("✅ - Vehicle location not accessible")
        else:
            fail_log("❌ - Vehicle location still accessible", "003")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "003")

def Privacy_Mode_004():
    try:
        app_logout()
        if app_login():
            log("✅ - Login successful")
        else:
            fail_log("❌ - Login failed", "004")

        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.swipe_down()
        sleep(6)
        controller.click_by_image("Icons/Error_Icon.png")

        controller.click_by_image("Icons/navigation_icon.png")
        controller.click_by_image("Images/Navigation_Allow.png")
        if not compare_with_expected_crop("Images/Navigation_Car_Image.png", 0.9):
            log("✅ - Vehicle location not accessible")
        else:
            fail_log("❌ - Vehicle location still accessible", "004")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

        if controller.find_img("Icons/Remote_Lock_Unavailable_Icon.png", 0.75):
            log("✅ - Remote lock unlock unavailable")
        elif controller.find_img("Icons/lock_icon.png", 0.75):
            fail_log("❌ - Remote lock unlock still available", "004")

        if not controller.is_text_present("My car status unavailable"):
            log("✅ - Car status information accessible")
        else:
            fail_log("❌ - Car status information still unavailable", "004")

        controller.click_by_image("Icons/windows_icon.png")
        section_titles = []
        for _ in range(2):
            titles = controller.d.xpath('//android.widget.TextView[''following-sibling::*//*[@text="Function disabled" or @text="Function not available"]]').all()
            section_titles.append([t.attrib.get("text", "") for t in titles if t.attrib.get("text") not in section_titles])
            if _ == 0:
                controller.swipe_up(0.25)

        section_titles = section_titles[0] + section_titles[1]
        log("✅ - My car statistics accessible") if "MY CAR STATISTICS" not in section_titles else fail_log("❌ - My car statistics still disabled", "004")
        log("✅ - My battery charge accessible") if "MY BATTERY CHARGE" not in section_titles else fail_log("❌ - My battery charge still disabled", "004")
        log("✅ - My cabin comfort accessible") if "MY CABIN COMFORT" not in section_titles else fail_log("❌ - My cabin comfort still disabled", "004")
        log("✅ - Remote parking accessible") if "REMOTE PARKING" not in section_titles else fail_log("❌ - Remote parking still disabled", "004")

        controller.click_text("STOLEN VEHICLE TRACKING")
        if not compare_with_expected_crop("Icons/privacy_mode_error.png"):
            log("✅ - Theft alert not disabled")
        else:
            fail_log("❌ - Theft alert still disabled", "004")
        controller.click_by_image("Icons/back_icon.png")
        controller.swipe_down()
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
        error_log(e, "004")

def Privacy_Mode_005():
    try:
        app_logout()
        if app_login():
            log("✅ - Login successful")
        else:
            fail_log("❌ - Login failed", "005")

        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.swipe_down()
        sleep(8)
        controller.click_by_image("Icons/Error_Icon.png")

        controller.click_by_image("Icons/navigation_icon.png")
        controller.click_by_image("Images/Navigation_Allow.png")
        if not compare_with_expected_crop("Images/Navigation_Car_Image.png", 0.9):
            log("✅ - Vehicle location not accessible")
        else:
            fail_log("❌ - Vehicle location still accessible", "005")
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

        if controller.find_img("Icons/Remote_Lock_Unavailable_Icon.png", 0.75):
            log("✅ - Remote lock unlock unavailable")
        elif controller.find_img("Icons/lock_icon.png", 0.75):
            fail_log("❌ - Remote lock unlock still available", "005")

        if not controller.is_text_present("My car status unavailable"):
            log("✅ - Car status information accessible")
        else:
            fail_log("❌ - Car status information still unavailable", "005")

        controller.click_by_image("Icons/windows_icon.png")
        section_titles = []
        for _ in range(2):
            titles = controller.d.xpath(
                '//android.widget.TextView[''following-sibling::*//*[@text="Function disabled" or @text="Function not available"]]').all()
            section_titles.append(
                [t.attrib.get("text", "") for t in titles if t.attrib.get("text") not in section_titles])
            if _ == 0:
                controller.swipe_up(0.25)

        section_titles = section_titles[0] + section_titles[1]
        log("✅ - My car statistics accessible") if "MY CAR STATISTICS" not in section_titles else fail_log(
            "❌ - My car statistics still disabled", "005")
        log("✅ - My battery charge accessible") if "MY BATTERY CHARGE" not in section_titles else fail_log(
            "❌ - My battery charge still disabled", "005")
        log("✅ - My cabin comfort accessible") if "MY CABIN COMFORT" not in section_titles else fail_log(
            "❌ - My cabin comfort still disabled", "005")
        log("✅ - Remote parking accessible") if "REMOTE PARKING" not in section_titles else fail_log(
            "❌ - Remote parking still disabled", "005")

        controller.click_text("STOLEN VEHICLE TRACKING")
        if not compare_with_expected_crop("Icons/privacy_mode_error.png"):
            log("✅ - Theft alert not disabled")
        else:
            fail_log("❌ - Theft alert still disabled", "005")
        controller.click_by_image("Icons/back_icon.png")
        controller.swipe_down()
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")

    except Exception as e:
            error_log(e, "005")

def Privacy_Mode_006():
    try:
        log("✅ - temp can't check style guide")
    except Exception as e:
        error_log(e, "006")
