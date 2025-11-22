from common_utils.android_image_comparision import *
from time import sleep
from core.app_functions import remote_swipe, app_login_setup
import core.globals as globals

def get_details():
    controller.d.press("recent")
    sleep(0.5)
    controller.click_text("Close all")
    controller.launch_app("uk.co.bentley.mybentley")
    while not controller.is_text_present("DASHBOARD") and not controller.is_text_present("LOGIN OR REGISTER"):
        sleep(0.2)
    if app_login_setup():
        controller.swipe_up()
        veh_range = controller.d.xpath('//*[@resource-id="uk.co.bentley.mybentley:id/textView_level_vsr_fuel"]').all()
        if len(veh_range) > 1:
            globals.vehicle_type = "phev"
            globals.battery_pct = veh_range[1].text[:-1]
        else:
            globals.vehicle_type = "ice"
        globals.fuel_pct = veh_range[0].text[:-1]
        controller.swipe_down(0.2)
        if not controller.click_by_image("Icons/info_btn.png"):
            controller.small_swipe_down()
        globals.current_vin = controller.d.xpath('//android.widget.TextView[@text="VIN"]/following-sibling::android.widget.TextView[1]').get_text()
        globals.current_car = controller.d.xpath('//android.widget.TextView[@text="Model"]/following-sibling::android.widget.TextView[1]').get_text()
        controller.click_by_image("Icons/back_icon.png")
        if globals.vehicle_type == 'phev':
            controller.click_by_image("Icons/remote_icon.png")
            remote_swipe("MY CABIN COMFORT")
            controller.click_text("MY CABIN COMFORT")
            controller.click_by_image("Icons/timer_toggle_off.png")
            if controller.is_text_present("Rear left"):
                globals.rear_seat_heating = True
            controller.click_by_image("Icons/back_icon.png")
            controller.swipe_down()
        controller.click_by_image("Icons/Profile_Icon.png")
        controller.click_text("My Details")
        globals.current_name = controller.d(resourceId="uk.co.bentley.mybentley:id/textView_user_name_profile").get_text()
        if globals.current_email != "":
            globals.current_email = controller.d.xpath('//android.widget.TextView[@text="Email address"]/following-sibling::android.widget.TextView[1]').get_text()
        controller.click_text("Account")
        controller.swipe_up()
        controller.click_text("Copyright")
        globals.app_version = controller.d.xpath('//*[contains(@text, "(Build: ")]').get_text()[11:-1].replace(" (Build: ", "_")
        controller.click_by_image("Icons/back_icon.png")

def service_reset():
    controller.d.press("recent")
    sleep(0.5)
    controller.click_text("Close all")
    controller.launch_app("uk.co.bentley.mybentley")
    while not controller.is_text_present("DASHBOARD") and not controller.is_text_present("LOGIN OR REGISTER"):
        sleep(0.2)

def get_device_details():
    controller.launch_app("com.android.settings")
    if controller.click_by_image("Icons/settings_search.png"):
        controller.enter_text("Software information")
        controller.click_text("Software information")
        globals.device = controller.d.xpath('//*[contains(@content-desc, "Product name")]').get_text()
        controller.click_text("Software information")
        globals.phone_software = controller.d.xpath('//android.widget.TextView[@text="Android version"]/following-sibling::android.widget.TextView[1]').get_text()
