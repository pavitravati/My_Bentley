import os

current_name = current_email = current_password = current_pin = vehicle_type = phone_type = country = current_VIN = second_email = second_password = ""
selected_services = []

service_index = 0
log_history = {}

user_dir = os.environ.get("USERPROFILE")
base_path = os.path.join(user_dir, "Volkswagen AG", "BY GQM - Smart Quality - Documents", "1. Workstreams", "1. Connected Car", "4. Testing", "Automated testing", "Automation app")
sharedrive_path = base_path

#temp
# current_email = "testdrive@gqm.anonaddy.com"
# current_password = "Password1!"
# current_VIN = "SJAAC14V6TC026906"
# current_name = "test gqm"
# second_email = "testdrive1@gqm.anonaddy.com"
# second_password = "Password1!"