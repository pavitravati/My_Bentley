import pandas as pd
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
import re
import os

services = ['DemoMode', 'Customer_Enrollment', 'App_Registration_Pages-IDK', 'Add_VIN', 'MyBentleyAppLogin',
            'Nickname', 'License(App)', 'VehicleStatusReport', 'RemoteLockUnlock', 'SingleServiceActivation',
            'PHEV-MyCarStatistics', 'PHEV-MyCabinComfort', 'PHEV-MyBatteryCharge', 'RoadsideAssistanceCall(App)',
            'DataServices', 'TheftAlarm', 'Audials(App)', 'CarFinder', 'NavCompanion', 'Notifications',
            'Profiles', 'TextStrings', 'PrivacyMode(App)', 'RemoteParkAssist', 'VehicleTrackingSystem']

def load_data():
    # Cleans the data so it can be easily added
    source_path = os.path.join(os.getcwd(), "Android_MY26_BY636_SQ_Remote_Services_EUR_Full - test.xlsx")
    workbook = load_workbook(source_path)

    skip_columns = ["A", "B", "D", "E", "G"]

    # Corrects the headers, swaps " for ' to avoid errors, replaces numeric list prefixes, removes sublists, removes empty lines,
    correct_headers = ['', 'TC ID', 'Region', 'Test Priority', 'Overall Effort (in Mins)', 'Test Case Title', 'Pre-Condition', 'Pre-Condition (Vehicle)', 'Action', 'Expected Result']
    for service in services:
        sheet = workbook[service]

        for col in sheet.iter_cols():
            col_letter = get_column_letter(col[0].column)
            if col_letter == "K":
                break
            if col_letter not in skip_columns:
                for cell in col:
                    if isinstance(cell.value, str):
                        cell.value = cell.value.replace("\"", "'")
                        cell.value = re.sub(r'(^|\n)\d+\. ', r'\1', cell.value)
                        cell.value = re.sub(r'(\n)[a-zA-Z]\.', ',', cell.value)
                        cell.value = re.sub('• ', '', cell.value)
                        while "\n\n" in cell.value:
                            cell.value = cell.value.replace("\n\n", "\n")

        col_num = 0
        for col in sheet.iter_cols():
            col_letter = get_column_letter(col[0].column)
            if col_letter == "K":
                break
            cell = sheet[f"{col_letter}4"]
            cell.value = correct_headers[col_num]

            col_num += 1

    workbook.save(source_path)

    TestCases = {}

    excel_file = pd.ExcelFile(source_path)
    sheet_names = excel_file.sheet_names
    for sheet in sheet_names:
        df = pd.read_excel(excel_file, sheet_name=sheet, skiprows=3, usecols="B:J")
        test_case_list = []

        for _, row in df.iterrows():
            precon, action, expected = [], [], []
            unsplit_precon = row.get("Pre-Condition (Vehicle)")
            try:
                split_precon = unsplit_precon.split('\n')
                for txt in split_precon:
                    precon.append(txt)
            except:
                pass
            unsplit_action = row.get("Action")
            try:
                split_action = unsplit_action.split('\n')
                for txt in split_action:
                    action.append(txt)
            except:
                pass
            unsplit_expected = row.get("Expected Result")
            try:
                split_expected = unsplit_expected.split('\n')
                for txt in split_expected:
                    expected.append(txt)
            except:
                pass
            test_case = {
                "Region": row.get("Region", "").strip(),
                "Test Case Description": row.get("Test Case Title", "").strip(),
                "Pre-Condition": precon,
                "Action": action,
                "Expected Result": expected
            }
            test_case_list.append(test_case)

        TestCases[sheet] = test_case_list


    return TestCases

    # # Remote Lock Unlock test cases while waiting on bringing them all in from the sheets
    # RemoteLockUnlock_testCases = [
    #     {"Region": "EUR, NAR, CHN", "Test Case Description": "Access Remote Lock & Unlock service Mobile App", "Pre-Condition": [], "Action": ["Scroll up/down and search for Lock and Unlock button"], "Expected Result": ["Lock and Unlock button are visible with respect to current lock status of the vehicle"]},
    #     {"Region": "EUR, NAR, CHN", "Test Case Description": "Verify Remote Unlock", "Pre-Condition": ["All Doors are closed", "Vehicle is locked"], "Action": ["Tap on Unlock button", "Enter PIN"], "Expected Result": ["The action should perform and Door disarming alarm should be played", "App should be notified with an appropriate message", "The status of the lock should be updated", "Push notification received in app"]},
    #     {"Region": "EUR, NAR, CHN", "Test Case Description": "Verify Remote Lock", "Pre-Condition": ["All Doors are closed", "Vehicle is unlocked"], "Action": ["Tap on Lock button", "Enter SPIN"], "Expected Result": ["The action should perform and Door arming alarm should be played", "App should be notified with an appropriate message", "The status of the lock should be updated", "Push notification received in app"]},
    #     {"Region": "EUR, NAR, CHN", "Test Case Description": "Verify the Remote Lock functionality when Ignition is ON", "Pre-Condition": ["All Doors are closed", "Vehicle is unlocked", "Ignition is ON"], "Action": ["Tap on 'Lock' button --> Enter SPIN"], "Expected Result": ["The action should performed and rejected by vehicle", "App should be notified with an appropriate  message (e.g. response as 'Unable to Lock Vehicle, Please switch Off the Ignition' [relevant message])", "Lock status should not be changed in app", "Push notification should be received in the app"]},
    #     {"Region": "EUR, NAR, CHN", "Test Case Description": "Verify the Remote Unlock functionality when Ignition is ON", "Pre-Condition": ["All Doors are closed", "Vehicle is locked", "Ignition is ON"], "Action": ["Tap on 'Unlock' button --> Enter SPIN "], "Expected Result": ["The action should performed and rejected by vehicle", "App should be notified with an appropriate  message (e.g. response as 'Unable to Lock Vehicle, Please switch Off the Ignition' [relevant message])", "Lock status should not be changed in app", "Push notification should be received in the app"]},
    #     {"Region": "EUR, NAR, CHN", "Test Case Description": "Verify the Remote Lock functionality when Driver Door is opened", "Pre-Condition": ["Driver door open but other doors closed", "Vehicle is unlocked", "Ignition is OFF"], "Action": ["Tap on 'Lock' button --> Enter SPIN"], "Expected Result": ["The action should performed and rejected by vehicle", "App should be notified with an appropriate  message (e.g. response as 'Unable to Lock Vehicle, Driver's door is opened'  [relevant message])", "Lock status should not be changed in app", "Push notification should be received in the app"]},
    #     {"Region": "EUR, NAR, CHN", "Test Case Description": "Verify the Remote Lock functionality when Any door or trunk is opened", "Pre-Condition": ["A door/bonnet is open other than the driver door", "Vehicle is unlocked", "Ignition is OFF"], "Action": ["Tap on 'Lock' button --> Enter SPIN "], "Expected Result": ["The action should performed and Door arming alarm should be played", "App should be notified with an appropriate  message (e.g. response as 'Vehicle is partially locked'  [relevant message])", "The status of the lock should be updated simultaneously", "Push notification should be received in the app"]},
    #     {"Region": "EUR, NAR, CHN", "Test Case Description": "Access to Remote Lock/unlock history  ", "Pre-Condition": [], "Action": ["Go to Notifications"], "Expected Result": ["Lock/unlock history should be visible with correct timestamps"]},
    #     {"Region": "EUR, NAR, CHN", "Test Case Description": "Verify the Remote Lock/Unlock latency time (Service Round Trip Time)", "Pre-Condition": ["All Doors are closed", "Vehicle is unlocked", "Ignition is OFF"], "Action": ["Tap on 'Lock' button --> Enter SPIN"], "Expected Result": ["The action should performed successfully and complete in 40 seconds."]},
    #     {"Region": "EUR, NAR, CHN", "Test Case Description": "Verify the Remote Lock functionality when vehicle is already locked", "Pre-Condition": ["All Doors are closed", "Vehicle is locked", "Ignition is OFF"], "Action": ["Tap on 'Lock' button --> Enter SPIN"], "Expected Result": ["The action should performed and get response with an appropriate  message (e.g. response as 'Vehicle is already locked / Vehicle locked'  [relevant message])", "Push notification should be received in the app"]},
    #     {"Region": "EUR, NAR, CHN", "Test Case Description": "Verify the Remote Unlock functionality when vehicle is already unlocked", "Pre-Condition": ["All Doors are closed", "Vehicle is unlocked", "Ignition is OFF"], "Action": ["Tap on 'Unlock' button --> Enter SPIN"], "Expected Result": ["The action should performed and get response with an appropriate  message (e.g. response as 'Vehicle is already unlocked / Vehicle unlocked'  [relevant message])", "Push notification should be received in the app"]},
    #     {"Region": "EUR, NAR, CHN", "Test Case Description": "Verify the Remote Lock functionality timeout when vehicle is not connected to network", "Pre-Condition": ["All Doors are closed", "Disconnect the vehicle from network or Activate flight mode on mobile", "Vehicle is locked", "Ignition is OFF"], "Action": ["Tap on 'Lock' button --> Enter SPIN"], "Expected Result": ["The action should be terminated (timeout) after 2 minutes", "App should be notified with an appropriate  message (e.g. response as 'Vehicle unreachable'  [relevant message])", "Push notification should be received in the app"]},
    #     {"Region": "EUR, NAR, CHN", "Test Case Description": "Verify Remote Lock functionality when Fob Keys are left inside the vehicle ", "Pre-Condition": ["Keep the Fob Key inside the vehicle", "Vehicle is unlocked", "Ignition is OFF"], "Action": ["Tap on 'Lock' button --> Enter SPIN"], "Expected Result": ["The action should performed and Door arming alarm should be played", "App should be notified with an appropriate  message (e.g. response as 'Vehicle is successfully locked'  [relevant message])", "The status of the lock should be updated simultaneously", "Push notification should be received in the app"]},
    #     {"Region": "EUR, NAR, CHN", "Test Case Description": "Verify Remote Unlock functionality when Fob Keys are left inside the vehicle ", "Pre-Condition": ["Keep the Fob Key inside the vehicle", "Vehicle is locked", "Ignition is OFF"], "Action": ["Tap on 'Unlock' button --> Enter SPIN"], "Expected Result": ["The action should performed and Door disarming alarm should be played", "App should be notified with an appropriate  message (e.g. response as 'Vehicle is successfully unlocked'  [relevant message])", "The status of the lock should be updated simultaneously"]},
    #     {"Region": "EUR, NAR, CHN", "Test Case Description": "Verify Remote Lock functionality when Vehicle is locked by Fob Keys ", "Pre-Condition": ["Vehicle is unlocked", "Ignition is OFF"], "Action": ["Tap on 'Lock' button --> Enter SPIN"], "Expected Result": ["The action should performed and Door arming alarm should be played", "App should be notified with an appropriate  message (e.g. response as 'Vehicle is successfully locked'  [relevant message])", "The status of the lock should be updated simultaneously", "Push notification should be received in the app"]},
    #     {"Region": "EUR, NAR, CHN", "Test Case Description": "Access to Remote Lock/unlock functionalities when Privacy mode is ON", "Pre-Condition": ["Privacy Mode is ON in HMI"], "Action": ["Scroll up/down and check the status of the Lock and Unlock services."], "Expected Result": ["The Remote locking service should be disabled(Greyed out)", "Lock and Unlock button should not be accessible."]},
    #     {"Region": "EUR, NAR, CHN", "Test Case Description": "Access to Remote Lock/unlock functionalities when Privacy mode is Off ", "Pre-Condition": ["Privacy Mode is OFF in HMI"], "Action": ["Scroll up/down and check the status of the Lock and Unlock services."], "Expected Result": ["The Remote locking service should be enabled", "Lock and Unlock button should be accessible."]},
    # ]
    #
    # DemoMode_testCases = [
    #     {"Region": "EUR, NAR, CHN", "Test Case Description": "Accessing Demo mode", "Pre-Condition": [], "Action": ["Click on 'Demo mode' link"], "Expected Result": ["The Dashboard should be launched successfully."]},
    #     {"Region": "EUR, NAR, CHN", "Test Case Description": "Verify 'Demo Mode' content", "Pre-Condition": [], "Action": ["Observe the Demo mode indication."], "Expected Result": ["The user must be indicated that it is a demo mode screen."]},
    #     {"Region": "EUR, NAR, CHN", "Test Case Description": "Verify 'Dashboard' content", "Pre-Condition": [], "Action": ["Observe the dashboard screen's text, icon & buttons."], "Expected Result": ["The screen should display like the actual logged account dashboard screen.", "All  the below information  must be clear to the user: Vehicle image, Greetings, Day & Date, Vehicle name, Vehicle Last contact details, Door lock & Unlock  buttons, Fuel range, Mileage details, Lights status, Door status, Bonnet & Boot status, Windows status, Oil details, Cluster warning navigation"]},
    #     {"Region": "EUR, NAR, CHN", "Test Case Description": "Verify 'Car Remote' screen", "Pre-Condition": [], "Action": ["Observe the Car Remote screen's text, images & modules."], "Expected Result": ["The screen should display like the actual logged account Car Remote screen.", "All the below information must be clear to the use:, My Car Statistics (PHEV Only), My Battery Charge (PHEV Only), My Cabin Comfort (PHEV Only), My Alerts (NAR region Only), Theft Alarm (EU region Only), Roadside assistance, Data services, Audials(EU & NAR Only), Activate Heating (Optional)"]},
    #     {"Region": "EUR, NAR, CHN", "Test Case Description": "Verify a 'module/feature'", "Pre-Condition": [], "Action": ["Click on a module.", "Observe the screen's text, icon & buttons."], "Expected Result": ["The screen should display like the actual logged account screen.", "The information, screen flow must be clear to the user"]},
    #     {"Region": "EUR, NAR, CHN", "Test Case Description": "Verify 'Navigation' screen", "Pre-Condition": [], "Action": ["Observe the navigation screen's text, icon & buttons."], "Expected Result": ["The screen should display like the actual logged account screen.", "All  the below information  must be clear to the user, Car icon, User icon, Search icon, Satellite map enable disable option, Traffic data enable disable option"]},
    #     {"Region": "EUR, NAR, CHN", "Test Case Description": "Verify 'Notification' screen", "Pre-Condition": [], "Action": ["Observe the notification screen's text & image."], "Expected Result": ["The screen should display like the actual logged account screen.", "All  the below information  must be clear to the user: Screen Title : Notifications, Last Updated Date & Time Information, Vehicle Specific Lock / Unlock - Successfull / Unsuccessfull Information along with date & time information"]},
    #     {"Region": "EUR, NAR, CHN", "Test Case Description": "Verify 'Profile' screen", "Pre-Condition": [], "Action": ["Observe the Profile screen's text, image & tabs."], "Expected Result": ["The screen should display like the actual logged account screen.", "All  the below information  must be clear to the user: Screen Title : PROFILE, User icon, User name, My Detail tab, Account tab, General tab, Gear/Setting icon"]},
    #     {"Region": "EUR, NAR, CHN", "Test Case Description": "Verify 'Setting' screen", "Pre-Condition": [], "Action": ["Click on Gear icon.", "Observe the setting screen's text & tabs."], "Expected Result": ["The screen should display like the actual logged account screen.", "All  the below information  must be clear to the user: Units tab, Access tab, Last mile notification enable/disable."]},
    #     {"Region": "EUR, NAR, CHN", "Test Case Description": "Verify 'Add vehicle' screen", "Pre-Condition": [], "Action": ["Observe the screen's text, icon & buttons."], "Expected Result": ["The screen should display like the actual logged account screen.", "All  the below information  must be clear to the user: The necessary detail required to add VIN, Add A Vehicle button"]},
    #     {"Region": "EUR, NAR, CHN", "Test Case Description": "Verify all the screen with Bentley style guide.", "Pre-Condition": [], "Action": ["Observe all the screen's icon, font, colour"], "Expected Result": ["All the icon, font, colour should be followed as per Bentley style guide."]},
    #     {"Region": "EUR, NAR, CHN", "Test Case Description": "Verification of 'Log out'", "Pre-Condition": [], "Action": ["Click on 'Log out' text."], "Expected Result": ["The Demo mode exit successfully.", "The screen should back to Sign in/Signup page."]},
    #     {"Region": "EUR, NAR, CHN", "Test Case Description": "Closing the 'Demo mode'", "Pre-Condition": [], "Action": ["Click on 'Demo mode' pop up X mark."], "Expected Result": ["The Demo mode exit successfully.", "The screen should back to Sign in/Signup page."]}
    # ]