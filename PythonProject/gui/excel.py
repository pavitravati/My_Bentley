import pandas as pd

excel_file = "Android_MY26_BY634_SQ_Remote_Services_EUR_Full.xlsm"
sheet_names = pd.ExcelFile(excel_file).sheet_names

Services = {}

ignore_sheets = ["Dashboard", "ChartBox", "Change_History"]
ignore_columns = ["TC ID", "Test Priority", "Overall Effort (in Mins)", "Effort in mins", "Actual Result", "No Of Observations", "Defect IDs/Comments", "Test Result"]
for sheet in sheet_names:
    if sheet not in ignore_sheets:
        row = 3
        Services[sheet] = {}
        df = pd.read_excel(excel_file, sheet_name=sheet)
        current_service = []
        while True:
            column = 1
            if row == df.shape[0]:
                break
            current_row = {}
            for i in range(8):
                column += 1
                header = df.iat[2,column]
                if header not in ignore_columns and not pd.isna(header):
                    if header == "Test Case Title":
                        header = "Test Case Description"
                    current_row[header] = df.iat[row, column]
            current_service.append(current_row)
            row += 1
        Services[sheet] = current_service


print(Services)

testCases = [
    { "Region" : "EUR, NAR, CHN", "Test Case Description" : "Access Remote Lock & Unlock service Mobile App", "Pre-Condition" : [], "Action" : ["Scroll up/down and search for Lock and Unlock button"], "Expected Result" : ["Lock and Unlock button are visible with respect to current lock status of the vehicle"] },
    { "Region" : "EUR, NAR, CHN", "Test Case Description" : "Verify Remote Unlock", "Pre-Condition" : [], "Action" : ["Tap on Unlock button", "Enter PIN"], "Expected Result" : ["The action should perform and Door disarming alarm should be played", "App should be notified with an appropriate message", "The status of the lock should be updated", "Push notification received in app"] },
    { "Region" : "EUR, NAR, CHN", "Test Case Description" : "Verify Remote Lock", "Pre-Condition" : ["All Doors are closed", "Vehicle is unlocked"], "Action" : ["Tap on Lock button", "Enter SPIN"], "Expected Result" : ["The action should perform and Door arming alarm should be played", "App should be notified with an appropriate message", "The status of the lock should be updated", "Push notification received in app"] }
]

services = ['DemoMode', 'Customer_Enrollment', 'App_registration_Pages-IDK', 'Add_VIN', 'MyBentleyLogin',
            'Nickname', 'License(App)', 'VehicleStatusReport', 'RemoteLockUnlock', 'SingleServiceActivation',
            'PHEV-MyCarStatistics', 'PHEV-MyCabinComfort', 'PHEV_MyBatteryCharge', 'RoadsideAssistanceCall(App)',
            'DataServices', 'TheftAlarm', 'Audials(App)', 'CarFinder', 'NavComparison', 'Notifications',
            'Profiles', 'TextStrings', 'PrivacyMode(App)', 'RemoteParkAssist', 'VehicleTrackingSystem']