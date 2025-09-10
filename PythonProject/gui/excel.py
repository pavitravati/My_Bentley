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