from PythonProject.common_utils.ios_controller import IOSController
from PythonProject.common_utils.html_test_report import HTMLTestReport
from DemoMode import (
    Demo_Mode_001, Demo_Mode_002, Demo_Mode_003, Demo_Mode_004,
    Demo_Mode_005, Demo_Mode_006, Demo_Mode_007, Demo_Mode_008,
    Demo_Mode_009, Demo_Mode_010, Demo_Mode_011, Demo_Mode_012, Demo_Mode_013
)

# List of test cases
all_tests = [
    Demo_Mode_001, Demo_Mode_002, Demo_Mode_003, Demo_Mode_004,
    Demo_Mode_005, Demo_Mode_006, Demo_Mode_007, Demo_Mode_008,
    Demo_Mode_009, Demo_Mode_010, Demo_Mode_011, Demo_Mode_012, Demo_Mode_013
]

# iOS session details
ios = IOSController(
    mac_ip="192.168.1.5",
    port=8101,
    udid="00008130-0012513918A1401C",
    team_id="LDD46J9733",
    bundle_id="uk.co.bentley.MyBentley"
)

# Start single session
ios.start_session()

# Initialize HTML report
report = HTMLTestReport("My Bentley iOS Automation Report", "test_report.html")

# Run all tests
for idx, test in enumerate(all_tests, start=1):
    print(f"➡️ Running Test {idx}: {test.__name__}")
    result = test(ios)  # run test with shared session
    report.add_test_result(**result.to_result_dict())

# Generate HTML report
report.generate_report()

# Optional: close session after all tests
ios.quit()
