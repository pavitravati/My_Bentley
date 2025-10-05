from time import sleep
from common_utils.android_image_comparision import *
from common_utils.android_controller import *
from core.log_emitter import log_emitter

def log(msg):
    log_emitter.log_signal.emit(msg)

def fail_log(msg, num):
    log(f"{msg}")
    controller.take_fail_screenshot(f"Nickname_{msg}_{num}.png")

def error_log(e, num):
    log(f"⚠️ - Unexpected error: {e}")
    controller.take_fail_screenshot(f"Nickname_{e}_{num}.png")

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

def VehicleStatusReport_001():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        if controller.is_text_present("DASHBOARD"):
            log("✅ - Dashboard page opened")
        else:
            fail_log("❌ - Dashboard page not opened", "001")

        controller.swipe_up()
        if controller.is_text_present("Fuel range"):
            log("✅ - Status report is displayed, VehicleStatusReport_001 Passed")
        else:
            fail_log("❌ - Status report is not displayed, VehicleStatusReport_001 Failed", "001")
        controller.swipe_down()

    except Exception as e:
        error_log(e, "001")

def VehicleStatusReport_002():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        if controller.is_text_present("DASHBOARD"):
            log("✅ - Dashboard page opened")
            log("✅ - Status information can be checked")
        else:
            fail_log("❌ - Dashboard page not opened", "002")
            log("❌ - Status information can't be checked")

        log("✅ - Screen title displayed") if controller.is_text_present("DASHBOARD") else fail_log("❌ - Screen title not displayed", "002")
        log("✅ - Vehicle image displayed") if identify_car() != '' else fail_log("❌ - Vehicle image not displayed", "002")
        log("✅ - Info icon displayed") if compare_with_expected_crop("Icons/info_btn.png") else fail_log("❌ - Info icon not displayed", "002")
        # Greeting message and date check if it is always "Good"...
        log("✅ - Vehicle image displayed") if identify_car() != '' else fail_log("❌ - Vehicle image not displayed", "002")

    except Exception as e:
        error_log(e, "002")

def VehicleStatusReport_003():
    try:
        pass
    except Exception as e:
        error_log(e, "003")

def VehicleStatusReport_004():
    try:
        pass
    except Exception as e:
        error_log(e, "004")

def VehicleStatusReport_005():
    try:
        pass
    except Exception as e:
        error_log(e, "005")

def VehicleStatusReport_006():
    try:
        pass
    except Exception as e:
        error_log(e, "006")

def VehicleStatusReport_007():
    try:
        pass
    except Exception as e:
        error_log(e, "007")

def VehicleStatusReport_008():
    try:
        pass
    except Exception as e:
        error_log(e, "008")

def VehicleStatusReport_009():
    try:
        pass
    except Exception as e:
        error_log(e, "009")

def VehicleStatusReport_010():
    try:
        pass
    except Exception as e:
        error_log(e, "010")

def VehicleStatusReport_011():
    try:
        pass
    except Exception as e:
        error_log(e, "011")

def VehicleStatusReport_012():
    try:
        pass
    except Exception as e:
        error_log(e, "012")

def VehicleStatusReport_013():
    try:
        pass
    except Exception as e:
        error_log(e, "013")

def VehicleStatusReport_014():
    try:
        pass
    except Exception as e:
        error_log(e, "014")

def VehicleStatusReport_015():
    try:
        pass
    except Exception as e:
        error_log(e, "015")

def VehicleStatusReport_016():
    try:
        pass
    except Exception as e:
        error_log(e, "016")

def VehicleStatusReport_017():
    try:
        pass
    except Exception as e:
        error_log(e, "017")

def VehicleStatusReport_018():
    try:
        pass
    except Exception as e:
        error_log(e, "018")

def VehicleStatusReport_019():
    try:
        pass
    except Exception as e:
        error_log(e, "019")

def VehicleStatusReport_020():
    try:
        pass
    except Exception as e:
        error_log(e, "020")

def VehicleStatusReport_021():
    try:
        pass
    except Exception as e:
        error_log(e, "021")

def VehicleStatusReport_022():
    try:
        pass
    except Exception as e:
        error_log(e, "022")

def VehicleStatusReport_023():
    try:
        pass
    except Exception as e:
        error_log(e, "023")

def VehicleStatusReport_024():
    try:
        pass
    except Exception as e:
        error_log(e, "024")

def VehicleStatusReport_025():
    try:
        pass
    except Exception as e:
        error_log(e, "025")

def VehicleStatusReport_026():
    try:
        pass
    except Exception as e:
        error_log(e, "026")

def VehicleStatusReport_027():
    try:
        pass
    except Exception as e:
        error_log(e, "027")

def VehicleStatusReport_028():
    try:
        pass
    except Exception as e:
        error_log(e, "028")

def VehicleStatusReport_029():
    try:
        pass
    except Exception as e:
        error_log(e, "029")

def VehicleStatusReport_030():
    try:
        pass
    except Exception as e:
        error_log(e, "030")

def VehicleStatusReport_031():
    try:
        pass
    except Exception as e:
        error_log(e, "031")

def VehicleStatusReport_032():
    try:
        pass
    except Exception as e:
        error_log(e, "032")

def VehicleStatusReport_033():
    try:
        pass
    except Exception as e:
        error_log(e, "033")
