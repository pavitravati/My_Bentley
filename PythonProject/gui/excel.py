import pandas as pd
from openpyxl import load_workbook, Workbook
from openpyxl.utils import get_column_letter
import sys
import os

services = ['Demo Mode', 'Customer Enrollment', 'Add VIN', 'App Registration Pages', 'App Log in-Log out',
            'Nickname', 'Services and licenses', 'Vehicle Status Report', 'Remote Lock-Unlock', 'Remote Honk & Flash',
            'My Car Statistics', 'My Cabin Comfort', 'My Battery Charge', 'Service Management', 'Activate Heating',
            'Roadside Assistance', 'Data Services', 'My Alerts', 'Theft Alarm', 'Stolen Vehicle Locator', 'Audials',
            'Car Finder', 'Nav Companion', 'Notifications', 'Push Notifications', 'Profile', 'Localization', 'Privacy Mode',
            'Remote Park Assist', 'Stolen Vehicle Tracking']

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def load_data():
    # source_path = resource_path("gui/Android_MY26_BY636_SQ_Remote_Services_EUR_Full - test.xlsx")
    source_path = resource_path("gui/Remote_Services.xlsx")
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