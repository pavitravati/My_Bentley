from time import sleep
from common_utils.android_image_comparision import *
from core.app_functions import app_login_setup, service_reset, primary_user_check
from core.globals import vehicle_type, country, current_name, current_email
from core.log_emitter import log, fail_log, metric_log, error_log, blocked_log, runtime_log
import datetime
from dateutil.relativedelta import relativedelta
from core.screenrecord import ScreenRecorder
from core import globals
from gui.manual_check import manual_check

img_service = "Services and licenses"
recorder = ScreenRecorder(device_serial=controller.d.serial)

def backspace(num):
    for i in range(num):
        controller.click_by_image("Icons/Homescreen_Left_Arrow.png")

# Finish
def activate_vts(num):
    controller.swipe_up()
    if controller.click_text("ACTIVATE"):
        controller.wait_for_text_and_click("Accept Terms & Conditions")
        controller.wait_for_text_and_click("CONFIRM")
        if controller.click_text("First Name"):
            controller.enter_text(current_name.split()[0])
        if controller.click_text("Last Name"):
            controller.enter_text(current_name.split()[1])
        controller.swipe(500, 500, 500, 100)
        if controller.click_text("Email address"):
            controller.enter_text(current_email)
    controller.wait_for_text_and_click("CONTINUE")
    if controller.click_text("Address"):
        controller.enter_text("25%sPyms%sLane", False)
    controller.swipe(500, 500, 500, 100)
    if controller.click_text("City"):
        controller.enter_text("Crewe")
    controller.swipe(500, 500, 500, 100)
    if controller.click_text("Postcode"):
        controller.enter_text("CW1%s3PL")
    sleep(0.5)
    controller.wait_for_text_and_click("CONTINUE")
    sleep(1)
    controller.click(500, 500)
    if not controller.is_text_present("Mobile number"):
        log("Mobile number successfully auto filled when activating SVT")
    else:
        fail_log("Mobile number not auto filled when activating SVT", "005", img_service)
        # Look into automating this when the phone used to verify is the phone used in the testing
        manual_check(
            instruction="Enter the a phone number to continue the SVT activation",
            test_id=num,
            service=img_service,
            take_screenshot=False
        )
    controller.wait_for_text_and_click("CONTINUE")
    controller.wait_for_text_and_click("Confirm")
    manual_check(
        instruction="Enter the code sent to the mobile number to activate VTS",
        test_id=num,
        service=img_service,
        take_screenshot=False
    )
    ### What happens now
    controller.swipe_down()

def Services_and_licenses_001():
    recorder.start(f"{img_service}-001")
    try:
        # blocked_log("Test blocked - All done in vehicle")
        manual_check(
            instruction="""Validate remote services license screen' in HMI(Home Screen->General->Settings->License Periods->My Bentley remote services), it should display:
                            \n1. Screen title as 'My Bentley remote services'\n2. List of My Bentley Remote Services license should be displayed:\n
                            a. Activate heating (NAR/CHN)\nb. Find my car\nc. Lock my car\nd. My battery charge(PHEV)\n
                            e. My cabin comfort (PHEV)\nf.) My car statistics (PHEV)\ng. My car status\nh. Remote departure time programming
                            \ni. Theft alert (NAR/CHN)\nj.) Perimeter alert(NAR)\nk. Speed alert(NAR)
                            \nl. Valet alert(NAR)\nm. Activate lights and horn(CHN)""",
            test_id="001",
            service=img_service,
            take_screenshot=False
        )
    except Exception as e:
        error_log(e, "001", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Services_and_licenses_002():
    recorder.start(f"{img_service}-002")
    try:
        # blocked_log("Test blocked - All done in vehicle")
        manual_check(
            instruction="""Verify 'My Bentley remote services' license validity in HMI(Home Screen->General->Settings->License Periods->My Bentley remote services)\n
                            'My Bentley remote services' license screen should display a 3-Year license\n
                            Note: Any license that is longer than 3 years just displays the validity status as “Active”""",
            test_id="002",
            service=img_service,
            take_screenshot=False
        )
    except Exception as e:
        error_log(e, "002", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Services_and_licenses_003():
    recorder.start(f"{img_service}-003")
    try:
        # blocked_log("Test blocked - All done in vehicle")
        manual_check(
            instruction="""Verify 'Roadside Assistance' license validity in HMI(Home Screen->General->Settings->License Periods->Roadside assistance call)\n
                            'Roadside assistance call' license screen should display a 3-Year license\n
                            Note: Any license that is longer than 3 years just displays the validity status as “Active”""",
            test_id="003",
            service=img_service,
            take_screenshot=False
        )
    except Exception as e:
        error_log(e, "003", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Services_and_licenses_004():
    recorder.start(f"{img_service}-004")
    try:
        if app_login_setup():
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            primary_user_check("004", img_service, True)
            ######
            # activate_vts("004")
            ######

            controller.click_by_image("Icons/info_btn.png")

            if controller.click_text("Services and licenses"):
                log("Services and licenses page opened")
            else:
                fail_log("Services and licenses page failed to open", "004", img_service)

            licenses = []
            extracted = controller.extract_all_license_dates()
            licenses.extend(extracted.items())
            current_date = datetime.date.today()
            date_limit = current_date + relativedelta(years=3)

            if licenses:
                log("Extracted Licenses:")
                print(licenses)
                for license, date in licenses:
                    license_date = datetime.datetime.strptime(date[-10:], "%d/%m/%Y").date()
                    if license_date >= date_limit:
                        log(f"{license}: {date}")
                    else:
                        fail_log(f"{license.replace("-", "")} expire in less than 3 years", "004", img_service)
            else:
                fail_log("Metrics not extracted", "004", img_service)
            backspace(2)

    except Exception as e:
        error_log(e, "004", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Services_and_licenses_005():
    recorder.start(f"{img_service}-005")
    try:
        if app_login_setup():
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            primary_user_check("005", img_service)
            controller.click_by_image("Icons/info_btn.png")

            controller.click_text("Services and licenses")
            if controller.click_text("Green traffic light prediction"):
                log("Green traffic light prediction page opened")
            else:
                fail_log("Green traffic light prediction page failed to open", "005", img_service)

            if controller.is_text_present("GREEN TRAFFIC LIGHT PREDICTION"):
                log("Screen title displayed")
            else:
                fail_log("Screen title not displayed", "005", img_service)

            try:
                current_date = datetime.date.today()
                date_limit = current_date + relativedelta(years=3)
                license_date = datetime.datetime.strptime(controller.extract_license_date()[-10:], "%d/%m/%Y").date()
                if license_date >= date_limit:
                    log("License is valid for at least 3 years")
                else:
                    fail_log("License is not valid for at least 3 years", "005", img_service)

            except Exception as e:
                fail_log("License date not extracted", "005", img_service)

            if controller.is_text_present("Green traffic light prediction"):
                log("Service title displayed")
            else:
                fail_log("Service title not displayed", "005", img_service)

            backspace(3)

    except Exception as e:
        error_log(e, "005", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

# One service uncheckable at bottom due to samsung ui
def Services_and_licenses_006():
    recorder.start(f"{img_service}-006")
    try:
        if app_login_setup():
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            primary_user_check("006", img_service)
            controller.click_by_image("Icons/info_btn.png")

            controller.click_text("Services and licenses")
            if controller.click_text("My Bentley in-car services"):
                log("My Bentley in-car services page opened")
            else:
                fail_log("My Bentley in-car services page failed to open", "006", img_service)

            if controller.is_text_present("MY BENTLEY IN-CAR SERVICES"):
                log("Screen title displayed")
            else:
                fail_log("Screen title not displayed", "006", img_service)

            try:
                current_date = datetime.date.today()
                date_limit = current_date + relativedelta(years=3)
                license_date = datetime.datetime.strptime(controller.extract_license_date()[-10:], "%d/%m/%Y").date()
                if license_date >= date_limit:
                    log("License is valid for at least 3 years")
                else:
                    fail_log("License is not valid for at least 3 years", "006", img_service)
            except Exception as e:
                fail_log("License date not extracted", "006", img_service)

            service_titles = {
                "Local hazard information": False, "Map update": False, "Natural speech interaction": False, "News": False,
                "Online POI search": False, "Online radio": False, "Realtime traffic information": False,
                "Remote destination import": False, "Satellite Map": False, "Song recognition": False, "Weather": False
            }
            if country == "chn":
                service_titles['Personal Navigation Assistant'] = False
            elif country == "nar":
                service_titles['SiriusXM'] = False
            elif country == "germany":
                service_titles['Traffic sign recognition'] = False

            if controller.is_text_present("SERVICES"):
                log("Services are listed")
                for _ in range(4):
                    for key, toggle in service_titles.items():
                        if _ == 3:
                            if service_titles[key]:
                                log(f"{key} is listed")
                            else:
                                fail_log(f"{key} is not listed", "006", img_service)
                        elif controller.is_text_present(key):
                            service_titles[key] = True
                    controller.swipe_up()
            else:
                fail_log("Services are not listed", "006", img_service)

            backspace(3)

    except Exception as e:
        error_log(e, "006", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Services_and_licenses_007():
    recorder.start(f"{img_service}-007")
    try:
        if app_login_setup():
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            primary_user_check("007", img_service)
            controller.click_by_image("Icons/info_btn.png")
            controller.click_text("Services and licenses")

            if controller.click_text("My Bentley remote services"):
                log("Remote services page opened")
            else:
                fail_log("Remote services page failed to open", "007", img_service)

            if controller.is_text_present("MY BENTLEY REMOTE SERVICES"):
                log("Screen title displayed")
            else:
                fail_log("Screen title not displayed", "007", img_service)

            try:
                current_year = datetime.date.today().year
                license_date = int(controller.extract_license_date()[-4:])
                if license_date >= current_year+3:
                    log("License is valid for at least 3 years")
                else:
                    fail_log("License is not valid for at least 3 years", "007", img_service)
            except Exception as e:
                fail_log("License date not extracted", "007", img_service)

            if vehicle_type == "phev":
                service_titles = {
                    "Find my car": False, "Lock my car": False, "My car status": False,
                    "My battery charge": False, "My cabin comfort": False, "My car statistics": False,
                    "Remote departure time programming": False, "Theft alert": False
                }

                if controller.is_text_present("SERVICES"):
                    log("Services are listed")
                    for _ in range(3):
                        for key, toggle in service_titles.items():
                            if _ == 2:
                                if service_titles[key]:
                                    log(f"{key} is listed")
                                else:
                                    fail_log(f"{key.replace("/", " ")} is not listed", "007", img_service)
                            elif controller.is_text_present(key):
                                service_titles[key] = True
                        controller.swipe_up()
                else:
                    fail_log("Services are not listed", "007", img_service)
            elif vehicle_type == "ice":
                service_titles = {
                    "Activate heating": False, "Find my car": False, "Lock my car": False, "My car status": False, "Theft alert": False
                }

                if controller.is_text_present("SERVICES"):
                    log("Services are listed")
                    for _ in range(2):
                        for key, toggle in service_titles.items():
                            if _ == 1:
                                if service_titles[key]:
                                    log(f"{key} is listed")
                                else:
                                    fail_log(f"{key.replace("/", " ")} is not listed", "007", img_service)
                            elif controller.is_text_present(key):
                                service_titles[key] = True
                else:
                    fail_log("Services are not listed", "007", img_service)
            backspace(3)

    except Exception as e:
        error_log(e, "007", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Services_and_licenses_008():
    recorder.start(f"{img_service}-008")
    try:
        if app_login_setup():
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            primary_user_check("008", img_service)
            controller.click_by_image("Icons/info_btn.png")
            controller.click_text("Services and licenses")
            if controller.click_text("Private e-Call"):
                log("Private e-Call page opened")
            else:
                fail_log("Private e-Call page not opened", "008", img_service)

            if controller.is_text_present("PRIVATE E-CALL"):
                log("Screen title displayed")
            else:
                fail_log("Screen title not displayed", "008", img_service)

            try:
                current_date = datetime.date.today()
                date_limit = current_date + relativedelta(years=3)
                license_date = datetime.datetime.strptime(controller.extract_license_date()[-10:], "%d/%m/%Y").date()
                if license_date >= date_limit:
                    log("License is valid for at least 3 years")
                else:
                    fail_log("License is not valid for at least 3 years", "008", img_service)
            except Exception as e:
                fail_log("License date not extracted", "008", img_service)

            if controller.is_text_present("Private e-Call"):
                log("Service title displayed")
            else:
                fail_log("Service title not displayed", "008", img_service)

            backspace(3)

    except Exception as e:
        error_log(e, "008", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Services_and_licenses_009():
    recorder.start(f"{img_service}-009")
    try:
        if app_login_setup():
            controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
            primary_user_check("009", img_service)
            controller.click_by_image("Icons/info_btn.png")
            controller.click_text("Services and licenses")
            if controller.click_text("Roadside assistance call"):
                log("Roadside assistance call page opened")
            else:
                fail_log("Roadside assistance call page not opened", "009", img_service)

            if controller.is_text_present("ROADSIDE ASSISTANCE CALL"):
                log("Screen title displayed")
            else:
                fail_log("Screen title not displayed", "009", img_service)

            try:
                current_date = datetime.date.today()
                date_limit = current_date + relativedelta(years=3)
                license_date = datetime.datetime.strptime(controller.extract_license_date()[-10:], "%d/%m/%Y").date()
                if license_date >= date_limit:
                    log("License is valid for at least 3 years")
                else:
                    fail_log("License is not valid for at least 3 years", "009", img_service)
            except Exception as e:
                fail_log("License date not extracted", "009", img_service)

            if controller.is_text_present("Roadside assistance call"):
                log("Service title displayed")
            else:
                fail_log("Service title not displayed", "009", img_service)

            backspace(3)

    except Exception as e:
        error_log(e, "009", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Services_and_licenses_010():
    recorder.start(f"{img_service}-010")
    try:
        if country == "eur":
            if app_login_setup():
                controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
                primary_user_check("010", img_service, True)
                ######
                # activate_vts("010")
                ######
                controller.click_by_image("Icons/info_btn.png")
                controller.click_text("Services and licenses")
                if controller.click_text("Vehicle tracking system"):
                    log("Vehicle tracking system page opened")
                else:
                    fail_log("Vehicle tracking system page not opened", "010", img_service)

                if controller.is_text_present("VEHICLE TRACKING SYSTEM"):
                    log("Screen title displayed")
                else:
                    fail_log("Screen title not displayed", "010", img_service)

                try:
                    current_date = datetime.date.today()
                    date_limit = current_date + relativedelta(years=3)
                    license_date = datetime.datetime.strptime(controller.extract_license_date()[-10:], "%d/%m/%Y").date()
                    if license_date >= date_limit:
                        log("License is valid for at least 3 years")
                    else:
                        fail_log("License is not valid for at least 3 years", "010", img_service)
                except Exception as e:
                    fail_log("License date not extracted", "010", img_service)

                if controller.is_text_present("Vehicle tracking system"):
                    log("Service title displayed")
                else:
                    fail_log("Service title not displayed", "010", img_service)

                backspace(3)
        else:
            blocked_log("Test blocked - Region locked (EUR)")
    except Exception as e:
        error_log(e, "010", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False

def Services_and_licenses_011():
    recorder.start(f"{img_service}-011")
    try:
        blocked_log("Test blocked - Can't check style guide")
    except Exception as e:
        error_log(e, "011", img_service)
    finally:
        runtime_log(recorder.stop(globals.test_failed))
        if globals.test_failed:
            service_reset()
            globals.test_failed = False