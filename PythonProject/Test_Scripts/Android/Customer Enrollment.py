from common_utils.android_image_comparision import *
from core.log_emitter import log, fail_log, error_log
from core.app_functions import app_login
from core.globals import *
from time import sleep

img_service = "Customer Enrollment"

def Customer_Enrollment_001():
    try:
        pass
    except Exception as e:
        error_log(e, "001", img_service)

def Customer_Enrollment_002():
    try:
        pass
    except Exception as e:
        error_log(e, "002", img_service)

def Customer_Enrollment_003():
    try:
        pass
    except Exception as e:
        error_log(e, "003", img_service)

def Customer_Enrollment_004():
    try:
        pass
    except Exception as e:
        error_log(e, "004", img_service)

def Customer_Enrollment_005():
    try:
        pass
    except Exception as e:
        error_log(e, "005", img_service)

def Customer_Enrollment_006():
    try:
        pass
    except Exception as e:
        error_log(e, "006", img_service)

def Customer_Enrollment_007():
    try:
        pass
    except Exception as e:
        error_log(e, "007", img_service)

def Customer_Enrollment_008():
    try:
        pass
    except Exception as e:
        error_log(e, "008", img_service)

def Customer_Enrollment_009():
    try:
        pass
    except Exception as e:
        error_log(e, "009", img_service)

def Customer_Enrollment_010():
    try:
        pass
    except Exception as e:
        error_log(e, "010", img_service)

def Customer_Enrollment_011():
    try:
        pass
    except Exception as e:
        error_log(e, "011", img_service)

def Customer_Enrollment_012():
    try:
        pass
    except Exception as e:
        error_log(e, "012", img_service)

def Customer_Enrollment_013():
    try:
        pass
    except Exception as e:
        error_log(e, "013", img_service)

def Customer_Enrollment_014():
    try:
        pass
    except Exception as e:
        error_log(e, "014", img_service)

def Customer_Enrollment_015():
    try:
        pass
    except Exception as e:
        error_log(e, "015", img_service)

def Customer_Enrollment_016():
    try:
        pass
    except Exception as e:
        error_log(e, "016", img_service)

def Customer_Enrollment_017():
    try:
        pass
    except Exception as e:
        error_log(e, "017", img_service)

def Customer_Enrollment_018():
    try:
        pass
    except Exception as e:
        error_log(e, "018", img_service)

def Customer_Enrollment_019():
    try:
        pass
    except Exception as e:
        error_log(e, "019", img_service)

def Customer_Enrollment_020():
    try:
        pass
    except Exception as e:
        error_log(e, "020", img_service)

def Customer_Enrollment_021():
    try:
        pass
    except Exception as e:
        error_log(e, "021", img_service)

def Customer_Enrollment_022():
    try:
        pass
    except Exception as e:
        error_log(e, "022", img_service)

def Customer_Enrollment_023():
    try:
        pass
    except Exception as e:
        error_log(e, "023", img_service)

def Customer_Enrollment_022():
    try:
        pass
    except Exception as e:
        error_log(e, "022", img_service)

def Customer_Enrollment_023():
    try:
        pass
    except Exception as e:
        error_log(e, "023", img_service)

def Customer_Enrollment_024():
    try:
        pass
    except Exception as e:
        error_log(e, "024", img_service)

def Customer_Enrollment_025():
    try:
        pass
    except Exception as e:
        error_log(e, "025", img_service)

def Customer_Enrollment_026():
    try:
        pass
    except Exception as e:
        error_log(e, "026", img_service)

def Customer_Enrollment_027():
    try:
        pass
    except Exception as e:
        error_log(e, "027", img_service)

def Customer_Enrollment_028():
    try:
        pass
    except Exception as e:
        error_log(e, "028", img_service)

def Customer_Enrollment_029():
    try:
        pass
    except Exception as e:
        error_log(e, "029", img_service)

def Customer_Enrollment_030():
    try:
        pass
    except Exception as e:
        error_log(e, "030", img_service)

def Customer_Enrollment_031():
    try:
        pass
    except Exception as e:
        error_log(e, "031", img_service)

def Customer_Enrollment_032():
    try:
        pass
    except Exception as e:
        error_log(e, "032", img_service)

def Customer_Enrollment_033():
    try:
        pass
    except Exception as e:
        error_log(e, "033", img_service)

def Customer_Enrollment_034():
    try:
        pass
    except Exception as e:
        error_log(e, "034", img_service)

def Customer_Enrollment_035():
    try:
        pass
    except Exception as e:
        error_log(e, "035", img_service)

def Customer_Enrollment_036():
    try:
        pass
        # Delete vehicle function

        ############
        # Tester check HMI
        ############
    except Exception as e:
        error_log(e, "036", img_service)

def Customer_Enrollment_037():
    try:
        # Delete vehicle function

        while not controller.is_text_present("ADD A VEHICLE"):
            controller.click_by_image("Icons/Homescreen_Right_Arrow.png")
            sleep(0.05)
        controller.small_swipe_up()
        controller.click_text("ADD A VEHICLE")
        controller.small_swipe_up()
        controller.click_text("Enter VIN manually")
        controller.enter_text(current_VIN)
        if controller.click_text("CONFIRM"):
            log("VIN entered manually")
        else:
            fail_log("VIN failed to be entered manually", "037", img_service)
        controller.click_by_image("Icons/Homescreen_Right_Arrow.png")
        controller.wait_for_text_and_click("Search by retailer name or location")
        controller.enter_text("Manchester")
        controller.click_text("Bentley Manchester")
        controller.wait_for_text_and_click("CONFIRM")

        # Check how to automate adding VIN and then check
    except Exception as e:
        error_log(e, "037", img_service)

def Customer_Enrollment_038():
    try:
        app_login(second_email, second_password)
        if controller.wait_for_text("ADD A VEHICLE"):
            log("No VIN on second account")
        else:
            fail_log("No VIN on second account check failed", "038", img_service)
        controller.small_swipe_up()
        controller.click_text("ADD A VEHICLE")
        controller.small_swipe_up()
        controller.click_text("Enter VIN manually")
        controller.enter_text(current_VIN)
        if controller.click_text("CONFIRM"):
            log("VIN entered manually")
        else:
            fail_log("VIN failed to be entered manually", "038", img_service)
        controller.click_by_image("Icons/Homescreen_Right_Arrow.png")
        controller.wait_for_text_and_click("Search by retailer name or location")
        controller.enter_text("Manchester")
        controller.click_text("Bentley Manchester")
        controller.wait_for_text_and_click("CONFIRM")

        # Check how to automate adding VIN and then check
    except Exception as e:
        error_log(e, "038", img_service)

# Can't be automated
def Customer_Enrollment_039():
    try:
        pass
    except Exception as e:
        error_log(e, "039", img_service)

def Customer_Enrollment_040():
    try:
        log("Cannot check style guide")
    except Exception as e:
        error_log(e, "040", img_service)