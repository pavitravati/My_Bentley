from common_utils.android_image_comparision import *
from core.log_emitter import log, fail_log, error_log, metric_log, blocked_log, runtime_log
from core.app_functions import remote_swipe, service_reset
from time import sleep
from core.globals import manual_run
from core.screenrecord import ScreenRecorder

img_service = "Remote Park Assist"
recorder = ScreenRecorder(device_serial=controller.d.serial)

def Remote_Park_Assist_001():
    recorder.start(f"{img_service}-001")
    try:
        blocked_log("Test blocked - Can't be automated")
        # controller.click_by_image("Icons/remote_icon.png")
        # if remote_swipe("REMOTE PARKING"):
        #     if compare_with_expected_crop("Images/Remote_Parking.png") and (controller.is_text_present("Park in and out your vehicle remotely") or controller.is_text_present("Preconditions not fulfilled")):
        #         log("Remote Parking feature displayed correctly")
        #     # don't have image for this yet, get next time in privacy mode
        #     elif compare_with_expected_crop("Images/Remote_Parking_disabled.png") and controller.is_text_present("Function not available"):
        #         log("Remote Parking feature disabled in privacy mode")
        #     else:
        #         fail_log("Remote Parking feature displayed incorrectly", "001", img_service)
        #
        #     controller.swipe_down()
        #     controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "001", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_002():
    recorder.start(f"{img_service}-002")
    try:
        blocked_log("Test blocked - Can't be automated")
        # controller.click_by_image("Icons/remote_icon.png")
        # if remote_swipe("REMOTE PARKING"):
        #     controller.click_text("REMOTE PARKING")
        #     controller.click_text("AGREE & CONTINUE")
        #
        #     # Do at car
        #
        # controller.click_by_image("Icons/login_page_x.png")
        # controller.swipe_down(0.05)
        # controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "002", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

# had use to use images of text rather than checking directly as it would not work
def Remote_Park_Assist_003():
    recorder.start(f"{img_service}-003")
    try:
        blocked_log("Test blocked - Can't be automated")
        # controller.click_by_image("Icons/remote_icon.png")
        # if remote_swipe("REMOTE PARKING"):
        #     controller.click_text("REMOTE PARKING")
        #     controller.click_text("AGREE & CONTINUE")
        #     controller.click_by_image("Icons/parking_info_btn.png")
        #     if controller.is_text_present("HOW IT WORKS"):
        #         log("'HOW IT WORKS' page displayed")
        #     else:
        #         fail_log("'HOW IT WORKS' page not displayed", "003", img_service)
        #     controller.swipe_up()
        #     sleep(0.2)
        #     controller.click_text("Remote parking out")
        #     controller.swipe_up()
        #     sleep(0.2)
        #     if compare_with_expected_crop("Images/Remote_parking_in.png"):
        #         log("Remote parking out section displayed correctly")
        #     else:
        #         fail_log("Remote parking out section not displayed correctly", "003", img_service)
        #     controller.click_text("Remote parking in")
        #     controller.swipe_up()
        #     sleep(0.2)
        #     if controller.is_text_present(
        #             "To park in, initiate the parking process in the vehicle by pressing the parking button. In the next step the parking lots will be scanned."):
        #         log("Remote parking in section displayed correctly")
        #     else:
        #         fail_log("Remote parking in section not displayed correctly", "003", img_service)
        #     controller.click_by_image("Icons/login_page_x.png")
        # controller.click_by_image("Icons/login_page_x.png")
        # controller.swipe_down(0.05)
        # controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "003", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_004():
    recorder.start(f"{img_service}-004")
    try:
        blocked_log("Test blocked - Can't be automated")
        # controller.click_by_image("Icons/remote_icon.png")
        # if remote_swipe("REMOTE PARKING"):
        #     controller.click_text("REMOTE PARKING")
        #     controller.click_text("AGREE & CONTINUE")
        #
        #     # Do at car
        #
        # controller.click_by_image("Icons/login_page_x.png")
        # controller.swipe_down(0.05)
        # controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "004", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_005():
    recorder.start(f"{img_service}-005")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "005", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_006():
    recorder.start(f"{img_service}-006")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "006", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_007():
    recorder.start(f"{img_service}-007")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "007", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_008():
    recorder.start(f"{img_service}-008")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "008", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_009():
    recorder.start(f"{img_service}-009")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "009", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_010():
    recorder.start(f"{img_service}-010")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "010", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_011():
    recorder.start(f"{img_service}-011")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "011", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_012():
    recorder.start(f"{img_service}-012")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "012", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_013():
    recorder.start(f"{img_service}-013")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "013", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_014():
    recorder.start(f"{img_service}-014")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "014", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_015():
    recorder.start(f"{img_service}-015")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "015", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_016():
    recorder.start(f"{img_service}-016")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "016", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_017():
    recorder.start(f"{img_service}-017")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "017", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_018():
    recorder.start(f"{img_service}-018")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "018", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_019():
    recorder.start(f"{img_service}-019")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "019", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_020():
    recorder.start(f"{img_service}-020")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "020", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_021():
    recorder.start(f"{img_service}-021")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "021", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_022():
    recorder.start(f"{img_service}-022")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "022", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_023():
    recorder.start(f"{img_service}-023")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "023", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_024():
    recorder.start(f"{img_service}-024")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "024", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_025():
    recorder.start(f"{img_service}-025")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "025", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_026():
    recorder.start(f"{img_service}-026")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "026", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_027():
    recorder.start(f"{img_service}-027")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "027", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_028():
    recorder.start(f"{img_service}-028")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "028", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_029():
    recorder.start(f"{img_service}-029")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "029", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_030():
    recorder.start(f"{img_service}-030")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "030", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_031():
    recorder.start(f"{img_service}-031")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "031", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_032():
    recorder.start(f"{img_service}-032")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "032", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_033():
    recorder.start(f"{img_service}-033")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "033", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_034():
    recorder.start(f"{img_service}-034")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "034", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_035():
    recorder.start(f"{img_service}-035")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "035", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_036():
    recorder.start(f"{img_service}-036")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "036", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_037():
    recorder.start(f"{img_service}-037")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "037", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_038():
    recorder.start(f"{img_service}-038")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "038", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_039():
    recorder.start(f"{img_service}-039")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "039", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_040():
    recorder.start(f"{img_service}-040")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "040", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_041():
    recorder.start(f"{img_service}-041")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "041", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_042():
    recorder.start(f"{img_service}-042")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "042", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_043():
    recorder.start(f"{img_service}-043")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "043", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_044():
    recorder.start(f"{img_service}-044")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "044", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_045():
    recorder.start(f"{img_service}-045")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "045", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_046():
    recorder.start(f"{img_service}-046")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "046", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_047():
    recorder.start(f"{img_service}-047")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "047", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_048():
    recorder.start(f"{img_service}-048")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "048", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_049():
    recorder.start(f"{img_service}-049")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "049", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_050():
    recorder.start(f"{img_service}-050")
    try:
        blocked_log("Test blocked - Can't be automated")
        # controller.click_by_image("Icons/remote_icon.png")
        # if remote_swipe("REMOTE PARKING"):
        #     controller.click_text("REMOTE PARKING")
        #
        # controller.click_by_image("Icons/login_page_x.png")
        # controller.swipe_down(0.05)
        # controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    except Exception as e:
        error_log(e, "050", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_051():
    recorder.start(f"{img_service}-051")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "051", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_052():
    recorder.start(f"{img_service}-052")
    try:
        blocked_log("Test blocked - Can't be automated")
    except Exception as e:
        error_log(e, "052", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Remote_Park_Assist_053():
    recorder.start(f"{img_service}-053")
    try:
        blocked_log("Test blocked - Can't check style guide")
    except Exception as e:
        error_log(e, "053", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False