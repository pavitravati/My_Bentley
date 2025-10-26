from common_utils.android_image_comparision import *
from core.log_emitter import log, fail_log, metric_log, error_log
import datetime
from dateutil.relativedelta import relativedelta

def Stolen_Vehicle_Tracking_001():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/info_btn.png")
        controller.click_text("Services and licenses")

        extracted = controller.extract_all_license_dates()
        current_date = datetime.date.today()
        date_limit = current_date + relativedelta(years=3)

        if extracted['Vehicle tracking system']:
            log("Licenses extracted")
            license_date = datetime.datetime.strptime(extracted['Vehicle tracking system'][-10:], "%d/%m/%Y").date()
            if license_date >= date_limit:
                log("Vehicle tracking system license has a valid date")
            else:
                fail_log("Vehicle tracking system license does not have a valid date", "001")
        else:
            fail_log("Failed to extract licenses", "001")

        controller.click_by_image("Icons/back_btn.png")
        controller.click_by_image("Icons/back_btn.png")

    except Exception as e:
        error_log(e, "001")

def Stolen_Vehicle_Tracking_002():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        controller.click_by_image("Icons/info_btn.png")
        controller.click_text("Services and licenses")
        extracted = controller.extract_all_license_dates()

        if extracted['Vehicle tracking system']:
            log("Licenses extracted")
            if extracted['Vehicle tracking system']:
                fail_log("Vehicle tracking system license is displayed", "002")
            else:
                log("Vehicle tracking system license is not displayed")
        else:
            fail_log("Failed to extract licenses", "002")

        controller.click_by_image("Icons/back_btn.png")
        controller.click_by_image("Icons/back_btn.png")

    except Exception as e:
        error_log(e, "002")

def Stolen_Vehicle_Tracking_003():
    try:
        pass
    except Exception as e:
        error_log(e, "003")

def Stolen_Vehicle_Tracking_004():
    try:
        pass
    except Exception as e:
        error_log(e, "004")

def Stolen_Vehicle_Tracking_005():
    try:
        pass
    except Exception as e:
        error_log(e, "005")

def Stolen_Vehicle_Tracking_006():
    try:
        pass
    except Exception as e:
        error_log(e, "006")

def Stolen_Vehicle_Tracking_007():
    try:
        pass
    except Exception as e:
        error_log(e, "007")

def Stolen_Vehicle_Tracking_008():
    try:
        pass
    except Exception as e:
        error_log(e, "008")

def Stolen_Vehicle_Tracking_009():
    try:
        pass
    except Exception as e:
        error_log(e, "009")

def Stolen_Vehicle_Tracking_010():
    try:
        pass
    except Exception as e:
        error_log(e, "010")

def Stolen_Vehicle_Tracking_011():
    try:
        pass
    except Exception as e:
        error_log(e, "011")

def Stolen_Vehicle_Tracking_012():
    try:
        pass
    except Exception as e:
        error_log(e, "012")

def Stolen_Vehicle_Tracking_013():
    try:
        pass
    except Exception as e:
        error_log(e, "013")

def Stolen_Vehicle_Tracking_014():
    try:
        pass
    except Exception as e:
        error_log(e, "014")

def Stolen_Vehicle_Tracking_015():
    try:
        pass
    except Exception as e:
        error_log(e, "015")

def Stolen_Vehicle_Tracking_016():
    try:
        pass
    except Exception as e:
        error_log(e, "016")

def Stolen_Vehicle_Tracking_017():
    try:
        pass
    except Exception as e:
        error_log(e, "017")

def Stolen_Vehicle_Tracking_018():
    try:
        pass
    except Exception as e:
        error_log(e, "018")

def Stolen_Vehicle_Tracking_019():
    try:
        pass
    except Exception as e:
        error_log(e, "019")

def Stolen_Vehicle_Tracking_020():
    try:
        pass
    except Exception as e:
        error_log(e, "020")

def Stolen_Vehicle_Tracking_021():
    try:
        pass
    except Exception as e:
        error_log(e, "021")

def Stolen_Vehicle_Tracking_022():
    try:
        pass
    except Exception as e:
        error_log(e, "022")

def Stolen_Vehicle_Tracking_023():
    try:
        pass
    except Exception as e:
        error_log(e, "023")

def Stolen_Vehicle_Tracking_024():
    try:
        pass
    except Exception as e:
        error_log(e, "024")

def Stolen_Vehicle_Tracking_025():
    try:
        pass
    except Exception as e:
        error_log(e, "025")

def Stolen_Vehicle_Tracking_026():
    try:
        pass
    except Exception as e:
        error_log(e, "026")

def Stolen_Vehicle_Tracking_027():
    try:
        pass
    except Exception as e:
        error_log(e, "027")

def Stolen_Vehicle_Tracking_028():
    try:
        pass
    except Exception as e:
        error_log(e, "028")

def Stolen_Vehicle_Tracking_029():
    try:
        pass
    except Exception as e:
        error_log(e, "029")

def Stolen_Vehicle_Tracking_030():
    try:
        pass
    except Exception as e:
        error_log(e, "030")

def Stolen_Vehicle_Tracking_031():
    try:
        pass
    except Exception as e:
        error_log(e, "031")

def Stolen_Vehicle_Tracking_032():
    try:
        pass
    except Exception as e:
        error_log(e, "032")

def Stolen_Vehicle_Tracking_033():
    try:
        pass
    except Exception as e:
        error_log(e, "033")

def Stolen_Vehicle_Tracking_034():
    try:
        pass
    except Exception as e:
        error_log(e, "034")

def Stolen_Vehicle_Tracking_035():
    try:
        pass
    except Exception as e:
        error_log(e, "035")

def Stolen_Vehicle_Tracking_036():
    try:
        pass
    except Exception as e:
        error_log(e, "036")

def Stolen_Vehicle_Tracking_037():
    try:
        pass
    except Exception as e:
        error_log(e, "037")

def Stolen_Vehicle_Tracking_038():
    try:
        pass
    except Exception as e:
        error_log(e, "038")

def Stolen_Vehicle_Tracking_039():
    try:
        pass
    except Exception as e:
        error_log(e, "039")

def Stolen_Vehicle_Tracking_040():
    try:
        pass
    except Exception as e:
        error_log(e, "040")

def Stolen_Vehicle_Tracking_041():
    try:
        pass
    except Exception as e:
        error_log(e, "041")

def Stolen_Vehicle_Tracking_042():
    try:
        pass
    except Exception as e:
        error_log(e, "042")

def Stolen_Vehicle_Tracking_043():
    try:
        pass
    except Exception as e:
        error_log(e, "043")

def Stolen_Vehicle_Tracking_044():
    try:
        pass
    except Exception as e:
        error_log(e, "044")

def Stolen_Vehicle_Tracking_045():
    try:
        pass
    except Exception as e:
        error_log(e, "045")

def Stolen_Vehicle_Tracking_046():
    try:
        pass
    except Exception as e:
        error_log(e, "046")

def Stolen_Vehicle_Tracking_047():
    try:
        pass
    except Exception as e:
        error_log(e, "047")

def Stolen_Vehicle_Tracking_048():
    try:
        pass
    except Exception as e:
        error_log(e, "048")

def Stolen_Vehicle_Tracking_049():
    try:
        pass
    except Exception as e:
        error_log(e, "049")

def Stolen_Vehicle_Tracking_050():
    try:
        pass
    except Exception as e:
        error_log(e, "050")

def Stolen_Vehicle_Tracking_051():
    try:
        pass
    except Exception as e:
        error_log(e, "051")

def Stolen_Vehicle_Tracking_052():
    try:
        pass
    except Exception as e:
        error_log(e, "052")

def Stolen_Vehicle_Tracking_053():
    try:
        pass
    except Exception as e:
        error_log(e, "053")

def Stolen_Vehicle_Tracking_054():
    try:
        pass
    except Exception as e:
        error_log(e, "054")

def Stolen_Vehicle_Tracking_055():
    try:
        pass
    except Exception as e:
        error_log(e, "055")

def Stolen_Vehicle_Tracking_056():
    try:
        pass
    except Exception as e:
        error_log(e, "056")

def Stolen_Vehicle_Tracking_057():
    try:
        pass
    except Exception as e:
        error_log(e, "057")

def Stolen_Vehicle_Tracking_058():
    try:
        pass
    except Exception as e:
        error_log(e, "058")

def Stolen_Vehicle_Tracking_059():
    try:
        pass
    except Exception as e:
        error_log(e, "059")

def Stolen_Vehicle_Tracking_060():
    try:
        pass
    except Exception as e:
        error_log(e, "060")