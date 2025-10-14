from common_utils.android_image_comparision import *
from common_utils.android_controller import *
from core.log_emitter import log_emitter
import datetime
from dateutil.relativedelta import relativedelta

def log(msg):
    log_emitter.log_signal.emit(msg)

def fail_log(msg, num):
    log(f"{msg}")
    controller.take_fail_screenshot(f"LicenseApp-{msg}-{num}.png")

def error_log(e, num):
    log(f"⚠️ - Unexpected error: {e}")
    controller.take_fail_screenshot(f"LicenseApp-{e}-{num}.png")

def backspace(num):
    for i in range(num):
        controller.click_by_image("Icons/Homescreen_Left_Arrow.png")

def early_setup(num):
    controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
    if controller.is_text_present("DASHBOARD"):
        log("✅ - Dashboard screen displayed")
    else:
        fail_log("❌ - Dashboard screen not displayed", num)

    controller.click_by_image("Icons/info_btn.png")

# First three test cases are not done on the app
###########
def LicenseApp_001():
    log("✅ - temp, not done in app")

def LicenseApp_002():
    log("✅ - temp, not done in app")

def License_003():
    log("✅ - temp, not done in app")
###########

def LicenseApp_004():
    try:
        early_setup("004")

        if controller.click_text("Services and licenses"):
            log("✅ - Services and licenses page opened")
        else:
            fail_log("❌ - Services and licenses page failed to open", "004")

        licenses = []
        extracted = controller.extract_all_license_dates()
        licenses.extend(extracted.items())
        current_date = datetime.date.today()
        date_limit = current_date + relativedelta(years=3)

        if licenses:
            log("✅ - Extracted Licenses:")
            for license, date in licenses:
                license_date = datetime.datetime.strptime(date[-10:], "%d/%m/%Y").date()
                if license_date >= date_limit:
                    log(f"{license}: {date}")
                else:
                    log(f"{license}: {date} - Less than 3 years ❌")
        else:
            fail_log("❌ - Metrics not extracted", "003")

        backspace(2)

    except Exception as e:
        error_log(e, "004")

LicenseApp_004()

def LicenseApp_005():
    try:
        early_setup("005")

        controller.click_text("Services and licenses")
        if controller.click_text("Green traffic light prediction"):
            log("✅ - Green traffic light prediction page opened")
        else:
            fail_log("❌ - Green traffic light prediction page failed to open", "005")

        if controller.is_text_present("GREEN TRAFFIC LIGHT PREDICTION"):
            log("✅ - Screen title displayed")
        else:
            fail_log("❌ - Screen title not displayed", "005")

        try:
            current_date = datetime.date.today()
            date_limit = current_date + relativedelta(years=3)
            license_date = datetime.datetime.strptime(controller.extract_license_date()[-10:], "%d/%m/%Y").date()
            if license_date >= date_limit:
                log("✅ - License is valid for at least 3 years")
            else:
                fail_log("❌ - License is not valid for at least 3 years", "005")

        except Exception as e:
            fail_log("❌ - License date not extracted", "005")

        if controller.is_text_present("Green traffic light prediction"):
            log("✅ - Service title displayed")
        else:
            fail_log("❌ - Service title not displayed", "005")

        backspace(3)

    except Exception as e:
        error_log(e, "005")

def LicenseApp_006():
    try:
        early_setup("006")

        controller.click_text("Services and licenses")
        if controller.click_text("My Bentley in-car services"):
            log("✅ - My Bentley in-car services page opened")
        else:
            fail_log("❌ - My Bentley in-car services page failed to open", "006")

        if controller.is_text_present("MY BENTLEY IN-CAR SERVICES"):
            log("✅ - Screen title displayed")
        else:
            fail_log("❌ - Screen title not displayed", "006")

        try:
            current_date = datetime.date.today()
            date_limit = current_date + relativedelta(years=3)
            license_date = datetime.datetime.strptime(controller.extract_license_date()[-10:], "%d/%m/%Y").date()
            if license_date >= date_limit:
                log("✅ - License is valid for at least 3 years")
            else:
                fail_log("❌ - License is not valid for at least 3 years", "006")
        except Exception as e:
            fail_log("❌ - License date not extracted", "006")

        service_titles = {
            "Local hazard information": False, "Map update": False, "Natural speech interaction": False, "News": False,
            "Online POI search": False, "Online radio": False, "Realtime traffic information": False,
            "Remote destination import": False, "Satellite Map": False, "Song recognition": False,
            "Traffic sign recognition": False, "Weather": False, "SiriusXM": False, "Personal Navigation Assistant": False
        }

        if controller.is_text_present("SERVICES"):
            log("✅ - Services are listed")
            for _ in range(4):
                for key, toggle in service_titles.items():
                    if _ == 3:
                        if service_titles[key]:
                            log(f"{key} is listed")
                        else:
                            fail_log(f"{key} is not listed - ❌", "006")
                    elif controller.is_text_present(key):
                        service_titles[key] = True
                controller.swipe_up()
        else:
            fail_log("❌ - Services are not listed", "006")

        backspace(3)

    except Exception as e:
        error_log(e, "006")

def LicenseApp_007():
    try:
        early_setup("007")
        controller.click_text("Services and licenses")

        if controller.click_text("My Bentley remote services"):
            log("✅ - Remote services page opened")
        else:
            fail_log("❌ - Remote services page failed to open", "007")

        if controller.is_text_present("MY BENTLEY REMOTE SERVICES"):
            log("✅ - Screen title displayed")
        else:
            fail_log("❌ - Screen title not displayed", "007")

        try:
            current_year = datetime.date.today().year
            license_date = int(controller.extract_license_date()[-4:])
            if license_date >= current_year+3:
                log("✅ - License is valid for at least 3 years")
            else:
                fail_log("❌ - License is not valid for at least 3 years", "007")
        except Exception as e:
            fail_log("❌ - License date not extracted", "007")

        service_titles = {
            "Activate heating": False, "Find my car": False, "Lock my car": False, "My car status": False,
            "My battery charge": False, "My cabin comfort": False, "My car statistics": False,
            "Remote departure time programming": False, "Theft alert": False, "Stolen Vehicle Locator/Finder": False,
            "Speed alert": False, "Valet alert": False, "Geofence": False, "Remote Honk & Flash": False
        }

        if controller.is_text_present("SERVICES"):
            log("✅ - Services are listed")
            for _ in range(3):
                for key, toggle in service_titles.items():
                    if _ == 2:
                        if service_titles[key]:
                            log(f"{key} is listed")
                        else:
                            fail_log(f"{key} is not listed - ❌", "007")
                    elif controller.is_text_present(key):
                        service_titles[key] = True
                controller.swipe_up()
        else:
            fail_log("❌ - Services are not listed", "007")

        backspace(3)

    except Exception as e:
        error_log(e, "007")

def LicenseApp_008():
    try:
        early_setup("008")
        controller.click_text("Services and licenses")
        if controller.click_text("Private e-Call"):
            log("✅ - Private e-Call page opened")
        else:
            fail_log("❌ - Private e-Call page not opened", "008")

        if controller.is_text_present("PRIVATE E-CALL"):
            log("✅ - Screen title displayed")
        else:
            fail_log("❌ - Screen title not displayed", "008")

        try:
            current_date = datetime.date.today()
            date_limit = current_date + relativedelta(years=3)
            license_date = datetime.datetime.strptime(controller.extract_license_date()[-10:], "%d/%m/%Y").date()
            if license_date >= date_limit:
                log("✅ - License is valid for at least 3 years")
            else:
                fail_log("❌ - License is not valid for at least 3 years", "008")
        except Exception as e:
            fail_log("❌ - License date not extracted", "008")

        if controller.is_text_present("Private e-Call"):
            log("✅ - Service title displayed")
        else:
            fail_log("❌ - Service title not displayed", "008")

        backspace(3)

    except Exception as e:
        error_log(e, "008")

def LicenseApp_009():
    try:
        early_setup("009")
        controller.click_text("Services and licenses")
        if controller.click_text("Roadside assistance call"):
            log("✅ - Roadside assistance call page opened")
        else:
            fail_log("❌ - Roadside assistance call page not opened", "009")

        if controller.is_text_present("ROADSIDE ASSISTANCE CALL"):
            log("✅ - Screen title displayed")
        else:
            fail_log("❌ - Screen title not displayed", "009")

        try:
            current_date = datetime.date.today()
            date_limit = current_date + relativedelta(years=3)
            license_date = datetime.datetime.strptime(controller.extract_license_date()[-10:], "%d/%m/%Y").date()
            if license_date >= date_limit:
                log("✅ - License is valid for at least 3 years")
            else:
                fail_log("❌ - License is not valid for at least 3 years", "009")
        except Exception as e:
            fail_log("❌ - License date not extracted", "009")

        if controller.is_text_present("Roadside assistance call"):
            log("✅ - Service title displayed")
        else:
            fail_log("❌ - Service title not displayed", "009")

        backspace(3)

    except Exception as e:
        error_log(e, "009")

# Service was not on my app so did this blind just copying from previous
def LicenseApp_010():
    try:
        early_setup("010")
        controller.click_text("Services and licenses")
        if controller.click_text("Vehicle tracking system"):
            log("✅ - Vehicle tracking system page opened")
        else:
            fail_log("❌ - Vehicle tracking system page not opened", "010")

        if controller.is_text_present("VEHICLE TRACKING SYSTEM"):
            log("✅ - Screen title displayed")
        else:
            fail_log("❌ - Screen title not displayed", "010")

        try:
            current_date = datetime.date.today()
            date_limit = current_date + relativedelta(years=3)
            license_date = datetime.datetime.strptime(controller.extract_license_date()[-10:], "%d/%m/%Y").date()
            if license_date >= date_limit:
                log("✅ - License is valid for at least 3 years")
            else:
                fail_log("❌ - License is not valid for at least 3 years", "010")
        except Exception as e:
            fail_log("❌ - License date not extracted", "010")

        if controller.is_text_present("Vehicle tracking system"):
            log("✅ - Service title displayed")
        else:
            fail_log("❌ - Service title not displayed", "010")

        backspace(3)
    except Exception as e:
        error_log(e, "010")

# Ask about these tests, how would i automate font checking etc...
def LicenseApp_011():
    try:
        log("✅ - Cannot check style")
    except Exception as e:
        error_log(e, "011")