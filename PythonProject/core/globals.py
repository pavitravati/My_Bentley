import os

current_name = current_email = current_password = current_pin = vehicle_type = phone_type = country = current_vin = second_email = second_password = fuel_pct = battery_pct = ""
manual_run = True
selected_services = []
rear_seat_heating = False

service_index = 0
log_history = {}

user_dir = os.environ.get("USERPROFILE")
base_path = os.path.join(user_dir, "Volkswagen AG", "BY GQM - Smart Quality - Documents", "1. Workstreams", "1. Connected Car", "4. Testing", "Automated testing", "Automation app")
sharedrive_path = base_path

#temp
current_email = "testdrive@gqm.anonaddy.com"
current_password = "Password1!"
# current_vin = "BBECEE4VZ25020601"
current_vin = "SJAAE14V3TC029739"
current_name = "Michael Scott"
# second_email = "testdrive1@gqm.anonaddy.com"
# second_password = "Password1!"