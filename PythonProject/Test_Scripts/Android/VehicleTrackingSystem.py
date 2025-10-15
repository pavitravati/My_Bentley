from common_utils.android_image_comparision import *
from core.log_emitter import log_emitter
import datetime
from dateutil.relativedelta import relativedelta

def log(msg):
    log_emitter.log_signal.emit(msg)

def fail_log(msg, num):
    log(f"{msg}")
    controller.take_fail_screenshot(f"VehicleTrackingSystem-{msg}-{num}.png")

def error_log(e, num):
    log(f"⚠️ - Unexpected error: {e}")
    controller.take_fail_screenshot(f"VehicleTrackingSystem-{e}-{num}.png")

def VehicleTrackingSystem_001():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/info_btn.png")
        controller.click_text("Services and licenses")

        extracted = controller.extract_all_license_dates()
        current_date = datetime.date.today()
        date_limit = current_date + relativedelta(years=3)

        if extracted['Vehicle tracking system']:
            log("✅ - Licenses extracted")
            license_date = datetime.datetime.strptime(extracted['Vehicle tracking system'][-10:], "%d/%m/%Y").date()
            if license_date >= date_limit:
                log("✅ - Vehicle tracking system license has a valid date")
            else:
                fail_log("❌ - Vehicle tracking system license does not have a valid date", "001")
        else:
            fail_log("❌ - Failed to extract licenses", "001")

        controller.click_by_image("Icons/back_btn.png")
        controller.click_by_image("Icons/back_btn.png")

    except Exception as e:
        error_log(e, "001")

def VehicleTrackingSystem_002():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/info_btn.png")
        controller.click_text("Services and licenses")
        extracted = controller.extract_all_license_dates()

        if extracted['Vehicle tracking system']:
            log("✅ - Licenses extracted")
            if extracted['Vehicle tracking system']:
                fail_log("❌ - Vehicle tracking system license is displayed", "002")
            else:
                log("✅ - Vehicle tracking system license is not displayed")
        else:
            fail_log("❌ - Failed to extract licenses", "002")

        controller.click_by_image("Icons/back_btn.png")
        controller.click_by_image("Icons/back_btn.png")

    except Exception as e:
        error_log(e, "002")

# Cannot find the VTS under car remote
def VehicleTrackingSystem_003():
    try:
        pass
    except Exception as e:
        error_log(e, "003")

# Cannot find the VTS under car remote
def VehicleTrackingSystem_004():
    try:
        pass
    except Exception as e:
        error_log(e, "004")

def VehicleTrackingSystem_005():
    try:
        pass
    except Exception as e:
        error_log(e, "005")

def VehicleTrackingSystem_006():
    try:
        pass
    except Exception as e:
        error_log(e, "006")

def VehicleTrackingSystem_007():
    try:
        pass
    except Exception as e:
        error_log(e, "007")

def VehicleTrackingSystem_008():
    try:
        pass
    except Exception as e:
        error_log(e, "008")

def VehicleTrackingSystem_009():
    try:
        pass
    except Exception as e:
        error_log(e, "009")

def VehicleTrackingSystem_010():
    try:
        pass
    except Exception as e:
        error_log(e, "010")

def VehicleTrackingSystem_011():
    try:
        pass
    except Exception as e:
        error_log(e, "011")

def VehicleTrackingSystem_012():
    try:
        pass
    except Exception as e:
        error_log(e, "012")

def VehicleTrackingSystem_013():
    try:
        pass
    except Exception as e:
        error_log(e, "013")

def VehicleTrackingSystem_014():
    try:
        pass
    except Exception as e:
        error_log(e, "014")

def VehicleTrackingSystem_015():
    try:
        pass
    except Exception as e:
        error_log(e, "015")

def VehicleTrackingSystem_016():
    try:
        pass
    except Exception as e:
        error_log(e, "016")

def VehicleTrackingSystem_017():
    try:
        pass
    except Exception as e:
        error_log(e, "017")

def VehicleTrackingSystem_018():
    try:
        pass
    except Exception as e:
        error_log(e, "018")

def VehicleTrackingSystem_019():
    try:
        pass
    except Exception as e:
        error_log(e, "019")

def VehicleTrackingSystem_020():
    try:
        pass
    except Exception as e:
        error_log(e, "020")

def VehicleTrackingSystem_021():
    try:
        pass
    except Exception as e:
        error_log(e, "021")

def VehicleTrackingSystem_022():
    try:
        pass
    except Exception as e:
        error_log(e, "022")

def VehicleTrackingSystem_023():
    try:
        pass
    except Exception as e:
        error_log(e, "023")

def VehicleTrackingSystem_024():
    try:
        pass
    except Exception as e:
        error_log(e, "024")

def VehicleTrackingSystem_025():
    try:
        pass
    except Exception as e:
        error_log(e, "025")

def VehicleTrackingSystem_026():
    try:
        pass
    except Exception as e:
        error_log(e, "026")

def VehicleTrackingSystem_027():
    try:
        pass
    except Exception as e:
        error_log(e, "027")

def VehicleTrackingSystem_028():
    try:
        pass
    except Exception as e:
        error_log(e, "028")

def VehicleTrackingSystem_029():
    try:
        pass
    except Exception as e:
        error_log(e, "029")

def VehicleTrackingSystem_030():
    try:
        pass
    except Exception as e:
        error_log(e, "030")

def VehicleTrackingSystem_031():
    try:
        pass
    except Exception as e:
        error_log(e, "031")

def VehicleTrackingSystem_032():
    try:
        pass
    except Exception as e:
        error_log(e, "032")

def VehicleTrackingSystem_033():
    try:
        pass
    except Exception as e:
        error_log(e, "033")

def VehicleTrackingSystem_034():
    try:
        pass
    except Exception as e:
        error_log(e, "034")

def VehicleTrackingSystem_035():
    try:
        pass
    except Exception as e:
        error_log(e, "035")

def VehicleTrackingSystem_036():
    try:
        pass
    except Exception as e:
        error_log(e, "036")

def VehicleTrackingSystem_037():
    try:
        pass
    except Exception as e:
        error_log(e, "037")

def VehicleTrackingSystem_038():
    try:
        pass
    except Exception as e:
        error_log(e, "038")

def VehicleTrackingSystem_039():
    try:
        pass
    except Exception as e:
        error_log(e, "039")

def VehicleTrackingSystem_040():
    try:
        pass
    except Exception as e:
        error_log(e, "040")

def VehicleTrackingSystem_041():
    try:
        pass
    except Exception as e:
        error_log(e, "041")

def VehicleTrackingSystem_042():
    try:
        pass
    except Exception as e:
        error_log(e, "042")

def VehicleTrackingSystem_043():
    try:
        pass
    except Exception as e:
        error_log(e, "043")

def VehicleTrackingSystem_044():
    try:
        pass
    except Exception as e:
        error_log(e, "044")

def VehicleTrackingSystem_045():
    try:
        pass
    except Exception as e:
        error_log(e, "045")

def VehicleTrackingSystem_046():
    try:
        pass
    except Exception as e:
        error_log(e, "046")

def VehicleTrackingSystem_047():
    try:
        pass
    except Exception as e:
        error_log(e, "047")

def VehicleTrackingSystem_048():
    try:
        pass
    except Exception as e:
        error_log(e, "048")

def VehicleTrackingSystem_049():
    try:
        pass
    except Exception as e:
        error_log(e, "049")

def VehicleTrackingSystem_050():
    try:
        pass
    except Exception as e:
        error_log(e, "050")

def VehicleTrackingSystem_051():
    try:
        pass
    except Exception as e:
        error_log(e, "051")

def VehicleTrackingSystem_052():
    try:
        pass
    except Exception as e:
        error_log(e, "052")

def VehicleTrackingSystem_053():
    try:
        pass
    except Exception as e:
        error_log(e, "053")

def VehicleTrackingSystem_054():
    try:
        pass
    except Exception as e:
        error_log(e, "054")

def VehicleTrackingSystem_055():
    try:
        pass
    except Exception as e:
        error_log(e, "055")

def VehicleTrackingSystem_056():
    try:
        pass
    except Exception as e:
        error_log(e, "056")

def VehicleTrackingSystem_057():
    try:
        pass
    except Exception as e:
        error_log(e, "057")

def VehicleTrackingSystem_058():
    try:
        pass
    except Exception as e:
        error_log(e, "058")

def VehicleTrackingSystem_059():
    try:
        pass
    except Exception as e:
        error_log(e, "059")

def VehicleTrackingSystem_060():
    try:
        pass
    except Exception as e:
        error_log(e, "060")

def VehicleTrackingSystem_061():
    try:
        pass
    except Exception as e:
        error_log(e, "061")
