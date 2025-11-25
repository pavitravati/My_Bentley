from common_utils.android_image_comparision import *
from core.app_functions import app_login_setup
from core.log_emitter import log, fail_log, error_log, metric_log, blocked_log
from datetime import datetime, timedelta
from time import sleep
from core.globals import country, manual_run

img_service = "Notifications"

def Notifications_001():
    try:
        if app_login_setup():
            if controller.click_by_image("Icons/New_Notification_icon.png") or controller.click_by_image("Icons/Notification_icon.png"):
                log("Notification page launched")
            else:
                fail_log("Notification page not launched", "001", img_service)

            if controller.is_text_present("NOTIFICATIONS"):
                log("Notification title displayed")
            else:
                fail_log("Notification title not displayed", "001", img_service)

            if controller.is_text_present("Actions") and controller.is_text_present("Alerts"):
                log("Actions & Alerts tab displayed")
            else:
                fail_log("Actions & Alerts tab not displayed", "001", img_service)

            if controller.d.xpath('//*[contains(@text, "Last updated")]').exists:
                log("Last updated status displayed")
            else:
                fail_log("Last updated status not displayed", "001", img_service)

    except Exception as e:
        error_log(e, "001", img_service)

def Notifications_002():
    try:
        if app_login_setup():
            controller.click_by_image("Icons/New_Notification_icon.png")
            controller.click_by_image("Icons/Notification_icon.png")

            controller.settings_swipe_down()
            now = datetime.now()
            one_minute_ago = now - timedelta(minutes=1)
            if controller.wait_for_text(f"Last updated: {now.strftime('%A')[:3]}, {str(int(now.strftime('%d')))} {now.strftime('%b')} at {now.strftime('%H:%M')}"):
                controller.click_by_image("Icons/Error_Icon.png")
                log("Last updated status displayed and up to date")
            elif controller.is_text_present(f"Last updated: {one_minute_ago.strftime('%A')[:3]}, {str(int(one_minute_ago.strftime('%d')))} {one_minute_ago.strftime('%b')} at {one_minute_ago.strftime('%H:%M')}"):

                log("Last updated status displayed and up to date")
            else:
                fail_log("Last updated status not displayed or up to date", "002", img_service)
            sleep(1)
            controller.click_by_image("Icons/Error_Icon.png")

            notifications = controller.d.xpath('//android.widget.TextView').all()
            events = []

            if len(notifications[0].attrib.get("text")) == 5:
                notifications.pop(0)
            chronological_order = True
            for i in range(2, 12, 3):
                try:
                    title = notifications[i].attrib.get("text", "")
                    time = notifications[i + 1].attrib.get("text", "")
                    desc = notifications[i + 2].attrib.get("text", "")
                    events.append({
                        "title": title,
                        "time": time,
                        "description": desc
                    })

                    if i != 2:
                        current_notif_time = datetime.strptime(time[-4:], '%H:%M')
                        last_notif_time = datetime.strptime(notifications[i - 2].attrib.get("text", "")[-4:], '%H:%M')

                        if not current_notif_time < last_notif_time:
                            chronological_order = False
                except IndexError:
                    break

            if len(events) > 0:
                log("Notifications displayed and details extracted")
            # Check what is shown when there are no notifications, below may be incorrect
            elif controller.is_text_present("There are no new notifications to display"):
                log("No notifications to displayed")
            else:
                fail_log("Notifications displayed but details not extracted", "002", img_service)
            for event in events:
                metric_log(f"{event['title']} - {event['description']} ({event['time']})")

            if chronological_order:
                log("Notifications displayed from newest to oldest")
            else:
                fail_log("Notifications not displayed from oldest to newest", "002", img_service)
    except Exception as e:
        error_log(e, "002", img_service)

# All checked in 2, can't really check max of 10, unless very important
def Notifications_003():
    try:
        blocked_log("Test blocked - Not written due to repetition")
    except Exception as e:
        error_log(e, "003", img_service)

# Checked in 2
def Notifications_004():
    try:
        blocked_log("Test blocked - Not written due to repetition")
    except Exception as e:
        error_log(e, "004", img_service)

# Check if this can be skipped
def Notifications_005():
    try:
        blocked_log("Test blocked - Not written due to repetition")
    except Exception as e:
        error_log(e, "005", img_service)

def Notifications_006():
    try:
        if country == "NAR":
            blocked_log("Test blocked - Not written")
        else:
            blocked_log("Test blocked - Region locked (NAR)")
    except Exception as e:
        error_log(e, "006", img_service)

# Can't really be automated, but check alerts screen when alerts are there to see if it can be just verified they exist and metric log what they say
def Notifications_007():
    try:
        if country == "NAR":
            blocked_log("Test blocked - Not written")
        else:
            blocked_log("Test blocked - Region locked (NAR)")
    except Exception as e:
        error_log(e, "007", img_service)

def Notifications_008():
    try:
        blocked_log("Test blocked - Can't check style guide")
    except Exception as e:
        error_log(e, "008", img_service)
