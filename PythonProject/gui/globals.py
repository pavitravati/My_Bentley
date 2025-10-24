import os

current_name = current_email = current_password = current_pin = vehicle_type = phone_type = None
selected_services = [None]

service_index = 0
log_history = {}

tests_run = tests_passed = tests_failed = 0
for service, tests in log_history.items():
    for test in tests:
        failed_test = False
        for log in range(len(log_history[service][test])):
            tests_run += 1
            if '❌' in log_history[service][test][log]:
                tests_failed += 1
            else:
                tests_passed += 1

user_dir = os.environ.get("USERPROFILE")
base_path = os.path.join(user_dir, "Volkswagen AG", "BY GQM - Smart Quality - Documents", "1. Workstreams", "1. Connected Car", "4. Testing", "Automated testing", "Automation app")
sharedrive_path = base_path