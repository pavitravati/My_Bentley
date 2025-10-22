import os

# current_name = current_email = current_password = current_pin = vehicle_type = phone_type = None
current_name = None
current_email = 'testdrive@gqm.anonaddy.com'
current_password = 'Password1!'
current_pin = '1234'
vehicle_type = None
phone_type = None
selected_services = [None]

service_index = 0
log_history = {}

user_dir = os.environ.get("USERPROFILE")
base_path = os.path.join(user_dir, "Volkswagen AG", "BY GQM - Smart Quality - Documents", "7. Temp", "Automation-Harry")
sharedrive_path = base_path