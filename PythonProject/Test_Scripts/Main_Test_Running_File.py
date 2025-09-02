from common_utils.html_test_report import *
from Test_Scripts.Android_TestCase import *
from common_utils.test_result_tracker import run_test_with_logs

all_tests = [
    Demo_Mode_001,
    Demo_Mode_002,
    Demo_Mode_003,
    Demo_Mode_004,
    Demo_Mode_005,
    Demo_Mode_006,
    Demo_Mode_007,
    Demo_Mode_008,
    Demo_Mode_009,
    Demo_Mode_010,
    Demo_Mode_011,
    Demo_Mode_012,
    Demo_Mode_013
]

report = HTMLTestReport("My Test Report", "test_report.html")

for idx, test_func in enumerate(all_tests, start=1):
    print(f"➡️ Running Test {idx}: {test_func.__name__}")
    result = run_test_with_logs(test_func)
    report.add_test_result(**result.to_result_dict())

report.generate_report()
