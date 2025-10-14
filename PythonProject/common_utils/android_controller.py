import uiautomator2 as u2
import time
import cv2
import os

class DeviceController:
    def __init__(self):
        self.d = u2.connect()

    def get_resource_path(self, filename):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(base_dir, ".."))
        return os.path.join(project_root, "resource", filename)

    def wake_up_unlock_screen(self):
        if not self.d.info.get("screenOn"):
            print("Device is sleeping. Waking up...")
            self.d.screen_on()
            time.sleep(1)
        else:
            # No action needed if already awake
            print("Device is already awake.")
            self.swipe_up()

    def click(self, x, y):
        """Click using screen coordinates."""
        self.d.click(x, y)
        time.sleep(0.5)

    def click_text(self, text):
        """Click on a UI element with specific text."""
        if self.d(text=text).exists:
            self.d(text=text).click()
            time.sleep(0.5)
            return True
        else:
            print(f"Text '{text}' not found.")
            return False

    def wait_for_text(self, text, timeout=10):
        """Wait until text appears on screen."""
        return self.d(text=text).wait(timeout=timeout)

    def wait_for_text_and_click(self, text, timeout=10):
        if self.wait_for_text(text, timeout=timeout):
            if self.d(text=text).exists:
                self.d(text=text).click()
                time.sleep(0.5)
                return True
            else:
                print(f"Text '{text}' not found.")
                return False
        else:
            return False

    def is_text_present(self, text):
        """Check if the given text is present on screen."""
        return self.d(text=text).exists

    def count_text(self,text):
        return len(self.d(text=text))

    def launch_app(self, package_name):
        self.d.app_start(package_name)
        time.sleep(1)

    def press_home(self):
        self.d.press("home")
        time.sleep(1)

    def take_screenshot(self, filename):
        os.makedirs("resource", exist_ok=True)
        full_path = self.get_resource_path(filename)
        self.d.screenshot(full_path)
        return full_path

    def take_fail_screenshot(self, filename):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(base_dir, ".."))
        fail_dir = os.path.join(project_root, "gui", "fail_images")
        os.makedirs(fail_dir, exist_ok=True)
        full_path = os.path.join(fail_dir, filename)
        self.d.screenshot(full_path)
        return full_path

    def swipe(self, start_x, start_y, end_x, end_y, duration=0.2):
        """Swipe from one point to another."""
        self.d.swipe(start_x, start_y, end_x, end_y, duration=duration)
        time.sleep(0.5)

    def swipe_up(self, duration=0.2):
        width, height = self.d.window_size()
        start_x = width // 2
        start_y = int(height * 0.8)
        end_y = int(height * 0.2)
        self.swipe(start_x, start_y, start_x, end_y, duration)

    def swipe_down(self, duration=0.2):
        width, height = self.d.window_size()
        start_x = width // 2
        start_y = int(height * 0.2)
        end_y = int(height * 0.8)
        self.swipe(start_x, start_y, start_x, end_y, duration)

    def swipe_left(self, duration=0.2):
        width, height = self.d.window_size()
        start_y = height // 2
        start_x = int(width * 0.8)
        end_x = int(width * 0.2)
        self.swipe(start_x, start_y, end_x, start_y, duration)

    def swipe_right(self, duration=0.2):
        width, height = self.d.window_size()
        start_y = height // 2
        start_x = int(width * 0.2)
        end_x = int(width * 0.8)
        self.swipe(start_x, start_y, end_x, start_y, duration)

    def click_by_image(self, image_path, threshold=0.8):
        """
        Click on the screen based on matching image.
        :param image_path: Relative path to the image you want to find and click.
        :param threshold: Confidence threshold (default 0.8).
        :return: True if image found and clicked, False otherwise.
        """
        template_path = self.get_resource_path(image_path)

        if not os.path.exists(template_path):
            print(f" Image file not found: {template_path}")
            return False

        screenshot_path = self.take_screenshot("temp.png")  # Make sure this returns the path
        screen = cv2.imread(screenshot_path)
        template = cv2.imread(template_path)

        if screen is None or template is None:
            print("Error reading screenshot or template image.")
            return False

        result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        print(f"Match confidence: {max_val}")

        if max_val >= threshold:
            h, w = template.shape[:2]
            center_x = max_loc[0] + w // 2
            center_y = max_loc[1] + h // 2
            print(f"Image found. Clicking at ({center_x}, {center_y})")
            self.click(center_x, center_y)

            # Optional: save debug image with match rectangle
            debug_img = screen.copy()
            cv2.rectangle(debug_img, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 255, 0), 2)
            cv2.imwrite("debug_match.png", debug_img)

            return True
        else:
            print("Image not found on screen (below threshold).")
            return False

    def click_by_resource_id(self, res_id):
        el = self.d(resourceId=res_id)
        if el.exists:
            el.click()
            return True
        return False

    def enter_pin(self, pin: str, press_enter: bool = True):
        if not isinstance(pin, str):
            raise ValueError("PIN must be a string")

        if not pin.isdigit():
            raise ValueError("PIN should only contain digits")

        os.system(f"adb shell input text {pin}")
        if press_enter:
            os.system("adb shell input keyevent 66")

    def enter_text(self, text: str, press_enter: bool = True):
        os.system(f"adb shell input text {text}")
        if press_enter:
            os.system("adb shell input keyevent 66")

    def clear_text(self, num_chars: int = 100):
        for _ in range(num_chars):
            os.system("adb shell input keyevent 67")  # KEYCODE_DEL


    def extract_dashboard_metrics(self):
        metrics = {}

        try:
            # Mileage
            if self.d(text="Mileage").exists:
                value = self.d(text="Mileage").sibling(className="android.widget.TextView", instance=1)
                if value.exists:
                    metrics["Mileage"] = value.get_text()

            # Lights
            if self.d(text="Lights").exists:
                value = self.d(text="Lights").sibling(className="android.widget.TextView", instance=1)
                if value.exists:
                    metrics["Lights"] = value.get_text()

            # Boot
            if self.d(text="Boot").exists:
                value = self.d(text="Boot").sibling(className="android.widget.TextView", instance=1)
                if value.exists:
                    metrics["Boot"] = value.get_text()

            # Bonnet
            if self.d(text="Bonnet").exists:
                value = self.d(text="Bonnet").sibling(className="android.widget.TextView", instance=1)
                if value.exists:
                    metrics["Bonnet"] = value.get_text()

            # Fuel Range
            if self.d(resourceId="uk.co.bentley.mybentley:id/textView_primary_range_title_vsr_combined_range").exists:
                value = self.d(resourceId="uk.co.bentley.mybentley:id/textView_primary_range_vsr_combined_range")
                if value.exists:
                    metrics["Fuel Range"] = value.get_text()

            # Doors
            if self.d(text="Doors").exists:
                value = self.d(text="Doors").sibling(className="android.widget.TextView", instance=1)
                if value.exists:
                    metrics["Doors"] = value.get_text()
            #Windows status
            if self.d(text="Windows").exists:
                value = self.d(text="Windows").sibling(className="android.widget.TextView", instance=1)
                if value.exists:
                    metrics["Windows"] = value.get_text()
            # Oil Level
            if self.d(text="Oil level").exists:
                value = self.d(text="Oil level").sibling(
                    resourceId="uk.co.bentley.mybentley:id/textView_value_vsr_metrics_item")
                if value.exists:
                    metrics["Oil Level"] = value.get_text()
            # Oil Change
            if self.d(text="Oil change").exists:
                value = self.d(text="Oil change").sibling(
                    resourceId="uk.co.bentley.mybentley:id/textView_value_vsr_metrics_item")
                if value.exists:
                    metrics["Oil Change"] = value.get_text()
            # Cluster Warnings
            if self.d(text="Cluster warnings").exists:
                value = self.d(text="Cluster warnings").sibling(
                    resourceId="uk.co.bentley.mybentley:id/textView_subtitle_dashboard_module_cluster_warnings")
                if value.exists:
                    metrics["Cluster Warnings"] = value.get_text()

            # Last Trip under MY CAR STATISTICS
            if self.d(resourceId="uk.co.bentley.mybentley:id/textView_title_car_remote_item",text="MY CAR STATISTICS").exists:
                last_trip = self.d(resourceId="uk.co.bentley.mybentley:id/textView_info_car_remote_item")
                if last_trip.exists:
                    metrics["Last Trip"] = last_trip.get_text()

            # MY BATTERY CHARGE
            battery_title = self.d(text="MY BATTERY CHARGE")
            if battery_title.exists:
                title_bounds = battery_title.info['bounds']
                status_nodes = self.d(resourceId="uk.co.bentley.mybentley:id/textView_status_car_remote_item")
                for node in status_nodes:
                    bounds = node.info['bounds']
                    if bounds['top'] > title_bounds['bottom']:
                        metrics["Battery Status"] = node.get_text()
                        break

            # MY CABIN COMFORT
            if self.d(text="MY CABIN COMFORT").exists:
                # Find the first status item appearing after this
                status_list = self.d(resourceId="uk.co.bentley.mybentley:id/textView_status_car_remote_item")
                for item in status_list:
                    if item.exists and item.info['bounds']['top'] > self.d(text="MY CABIN COMFORT").info['bounds'][
                        'bottom']:
                        metrics["Cabin Comfort"] = item.get_text()
                        break

            # Remote parking
            remote_title = self.d(text="REMOTE PARKING")
            if remote_title.exists:
                # Fetch the closest textView_status_car_remote_item *below* this title
                status_list = self.d(
                    resourceId="uk.co.bentley.mybentley:id/textView_status_car_remote_item")
                for item in status_list:
                    if item.exists and item.info["bounds"]["top"] > remote_title.info["bounds"]["bottom"]:
                        metrics["REMOTE PARKING"] = item.get_text()
                        break

            # THEFT ALARM
            remote_title = self.d(text="THEFT ALARM")
            if remote_title.exists:
                # Fetch the closest textView_status_car_remote_item *below* this title
                status_list = self.d(resourceId="uk.co.bentley.mybentley:id/textView_status_car_remote_item")
                for item in status_list:
                    if item.exists and item.info["bounds"]["top"] > remote_title.info["bounds"]["bottom"]:
                        metrics["THEFT ALARM"] = item.get_text()
                        break
            # ROADSIDE ASSISTANCE
            if self.d(text="ROADSIDE ASSISTANCE").exists:
                roadside_value = self.d(text="ROADSIDE ASSISTANCE").sibling(
                    resourceId="uk.co.bentley.mybentley:id/textView_info_car_remote_item")
                if roadside_value.exists:
                    metrics["Roadside Assistance"] = roadside_value.get_text()

            # DATA SERVICES
            if self.d(text="DATA SERVICES").exists:
                roadside_value = self.d(text="DATA SERVICES").sibling(
                    resourceId="uk.co.bentley.mybentley:id/textView_info_car_remote_item")
                if roadside_value.exists:
                    metrics["DATA SERVICES"] = roadside_value.get_text()

            # AUDIALS
            if self.d(text="AUDIALS").exists:
                roadside_value = self.d(text="AUDIALS").sibling(
                    resourceId="uk.co.bentley.mybentley:id/textView_info_car_remote_item")
                if roadside_value.exists:
                    metrics["AUDIALS"] = roadside_value.get_text()

            #Last Updated
            last_updated_node = self.d(textStartsWith="Last updated:")
            if last_updated_node.exists:
                last_updated_text = last_updated_node.get_text()
                metrics["Last Updated"] = last_updated_text

        except Exception as e:
            print(f"❌ Error while extracting 'Last updated': {e}")

            # Final Output
        if metrics:
            print("\n✅ Extracted Metrics:")
            for k, v in metrics.items():
                print(f"{k}: {v}")
        else:
            print("⚠️ No metrics found on screen.")

        return metrics

    def extract_all_license_dates(self):
        licenses = {}

        try:
            label = "Green traffic light prediction"
            license_value = self.d(text=label).sibling(className="android.widget.TextView", instance=1)
            if license_value.exists:
                licenses[label] = f"{license_value.get_text()}"

            label = "MyBentley in-car services"
            license_value = self.d(text=label).sibling(className="android.widget.TextView", instance=1)
            if license_value.exists:
                licenses[label] = f"{license_value.get_text()}"

            label = "MyBentley remote services"
            license_value = self.d(text=label).sibling(className="android.widget.TextView", instance=1)
            if license_value.exists:
                licenses[label] = f"{license_value.get_text()}"

            label = "Private e-Call"
            license_value = self.d(text=label).sibling(className="android.widget.TextView", instance=1)
            if license_value.exists:
                licenses[label] = f"{license_value.get_text()}"

            label = "Roadside assistance call"
            license_value = self.d(text=label).sibling(className="android.widget.TextView", instance=1)
            if license_value.exists:
                licenses[label] = f"{license_value.get_text()}"

        except Exception as e:
            print(f"❌ Error while extracting 'Last updated': {e}")

        if licenses:
            print("\n✅ Extracted Licenses:")
            for k, v in licenses.items():
                print(f"{k}: {v}")
        else:
            print("⚠️ No licenses found on screen.")

        return licenses

    def extract_license_date(self):
        try:
            label = "License is valid until"
            license_value = self.d(text=label).sibling(className="android.widget.TextView", instance=1)
            if license_value.exists:
                return license_value.get_text()

        except Exception as e:
            print(f"❌ Error while extracting license date: {e}")

    def extract_license_services(self):
        try:
            services = []
            # Find the scrollable container
            container = self.d(scrollable=True)
            if not container.exists:
                return []

            # Get only textviews inside that container
            nodes = container.child(className="android.widget.TextView")

            found_services_header = False
            for node in nodes:
                text = node.get_text().strip()
                if text == "SERVICES":
                    found_services_header = True
                    continue

                if found_services_header and text:
                    services.append(text)

            return services

        except Exception as e:
            print(f"❌ Error while extracting license services: {e}")
            return []

    def extract_status(self, status_id):
        try:
            status = self.d(resourceId=status_id)
            if status.exists and status.info.get("visibleToUser", False):
                return True
            else:
                return False

        except Exception as e:
            return False

    def extract_doors_status(self):
        door_status = {}
        try:
            if self.d(resourceId="uk.co.bentley.mybentley:id/textView_info_left_front_vsr_metrics_car_item").exists:
                left_front = self.d(resourceId="uk.co.bentley.mybentley:id/textView_info_left_front_vsr_metrics_car_item").get_text()
                door_status["front left"] = left_front

            if self.d(resourceId="uk.co.bentley.mybentley:id/textView_info_right_front_vsr_metrics_car_item").exists:
                right_front = self.d(resourceId="uk.co.bentley.mybentley:id/textView_info_right_front_vsr_metrics_car_item").get_text()
                door_status["front right"] = right_front

            if self.d(resourceId="uk.co.bentley.mybentley:id/textView_info_left_rear_vsr_metrics_car_item").exists:
                left_rear = self.d(resourceId="uk.co.bentley.mybentley:id/textView_info_left_rear_vsr_metrics_car_item").get_text()
                door_status["rear left"] = left_rear

            if self.d(resourceId="uk.co.bentley.mybentley:id/textView_info_right_rear_vsr_metrics_car_item").exists:
                right_rear = self.d(resourceId="uk.co.bentley.mybentley:id/textView_info_right_rear_vsr_metrics_car_item").get_text()
                door_status["rear right"] = right_rear

        except Exception as e:
            print(f"❌ Error while extracting fuel details: {e}")

        return door_status

    def extract_window_status(self):
        window_status = {}
        try:
            if self.d(resourceId="uk.co.bentley.mybentley:id/textView_info_left_front_vsr_metrics_car_item").exists:
                left_front = self.d(resourceId="uk.co.bentley.mybentley:id/textView_info_left_front_vsr_metrics_car_item").get_text()
                window_status["front left"] = left_front

            if self.d(resourceId="uk.co.bentley.mybentley:id/textView_info_right_front_vsr_metrics_car_item").exists:
                right_front = self.d(resourceId="uk.co.bentley.mybentley:id/textView_info_right_front_vsr_metrics_car_item").get_text()
                window_status["front right"] = right_front

            if self.d(resourceId="uk.co.bentley.mybentley:id/textView_info_left_rear_vsr_metrics_car_item").exists:
                left_rear = self.d(resourceId="uk.co.bentley.mybentley:id/textView_info_left_rear_vsr_metrics_car_item").get_text()
                window_status["rear left"] = left_rear

            if self.d(resourceId="uk.co.bentley.mybentley:id/textView_info_right_rear_vsr_metrics_car_item").exists:
                right_rear = self.d(resourceId="uk.co.bentley.mybentley:id/textView_info_right_rear_vsr_metrics_car_item").get_text()
                window_status["rear right"] = right_rear

            if self.d(resourceId="uk.co.bentley.mybentley:id/textView_roof_title_vsr_metrics_car_item").exists:
                sunroof = self.d(resourceId="uk.co.bentley.mybentley:id/textView_roof_title_vsr_metrics_car_item").get_text()
                window_status["sunroof"] = sunroof

        except Exception as e:
            print(f"❌ Error while extracting window details: {e}")

        return window_status

    def extract_boot_bonnet_status(self):
        boot_bonnet_status = {}
        try:
            if self.d(text="Boot").exists:
                value = self.d(text="Boot").sibling(className="android.widget.TextView", instance=1)
                if value.exists:
                    boot_bonnet_status["Boot"] = value.get_text()

            if self.d(text="Bonnet").exists:
                value = self.d(text="Bonnet").sibling(className="android.widget.TextView", instance=1)
                if value.exists:
                    boot_bonnet_status["Bonnet"] = value.get_text()

            return boot_bonnet_status

        except Exception as e:
            print(f"❌ Error while extracting boot/bonnet details: {e}")

    def extract_service_status(self):
        service_status = {}
        try:
            if self.d(text="Oil level").exists:
                value = self.d(text="Oil level").sibling(className="android.widget.TextView", instance=1)
                if value.exists:
                    service_status["Oil level"] = value.get_text()

            if self.d(text="Oil change").exists:
                value = self.d(text="Oil change").sibling(className="android.widget.TextView", instance=1)
                if value.exists:
                    service_status["Oil change"] = value.get_text()

            if self.d(text="Service").exists:
                value = self.d(text="Service").sibling(className="android.widget.TextView", instance=1)
                if value.exists:
                    service_status["Service"] = value.get_text()

            if self.d(text="Cluster warnings").exists:
                value = self.d(text="Cluster warnings").sibling(className="android.widget.TextView", instance=1)
                if value.exists:
                    service_status["Cluster warnings"] = value.get_text()

            return service_status

        except Exception as e:
            print(f"❌ Error while extracting service status: {e}")

    def dump_ui(self, filename="ui_dump.xml"):
        xml = self.d.dump_hierarchy()
        with open(filename, "w", encoding="utf-8") as f:
            f.write(xml)
        print(f"Dumped UI to {filename}")

    def extract_profile_details(self):
        details = {}
        try:
            # Last name
            if self.d(text="Last name").exists:
                value = self.d(text="Last name").sibling(className="android.widget.TextView", instance=1)
                if value.exists:
                    details["Last name"] = value.get_text()

            # First name
            if self.d(text="First name").exists:
                value = self.d(text="First name").sibling(className="android.widget.TextView", instance=1)
                if value.exists:
                    details["First name"] = value.get_text()

            # Email
            if self.d(text="Email address").exists:
                value = self.d(text="Email address").sibling(className="android.widget.TextView", instance=1)
                if value.exists:
                    details["Email address"] = value.get_text()

        except Exception as e:
            print(f"❌ Error while extracting profile details: {e}")

        # Print results
        if details:
            print("\n✅ Extracted Profile Details:")
            for k, v in details.items():
                print(f"{k}: {v}")
        else:
            print("⚠️ No profile details found.")

        return details

    def extract_fuel_range_and_level(self, phev=False):
        fuel_details = {}
        try:
            if self.d(resourceId="uk.co.bentley.mybentley:id/textView_level_vsr_fuel").exists:
                fuel_percentage = self.d(resourceId="uk.co.bentley.mybentley:id/textView_level_vsr_fuel").get_text()
                fuel_details["fuel level"] = fuel_percentage

            if self.d(resourceId="uk.co.bentley.mybentley:id/textView_primary_range_vsr_combined_range").exists:
                fuel_range = self.d(resourceId="uk.co.bentley.mybentley:id/textView_primary_range_vsr_combined_range").get_text()
                fuel_details["fuel range"] = fuel_range

            if self.d(resourceId="uk.co.bentley.mybentley:id/textView_value_vsr_metrics_item").exists:
                total_mileage = self.d(resourceId="uk.co.bentley.mybentley:id/textView_value_vsr_metrics_item").get_text()
                fuel_details["total mileage"] = total_mileage

            if phev:
                try:
                    fuel_type = self.d(resourceId="uk.co.bentley.mybentley:id/textView_level_vsr_fuel")
                    if fuel_type.count > 1:
                        elec_percentage = fuel_type[1].get_text()
                        fuel_details["elec level"] = elec_percentage

                    if self.d(resourceId="uk.co.bentley.mybentley:id/textView_secondary_range_vsr_combined_range").exists:
                        elec_range = self.d(resourceId="uk.co.bentley.mybentley:id/textView_secondary_range_vsr_combined_range").get_text()
                        fuel_details["elec range"] = elec_range

                    if self.d(resourceId="uk.co.bentley.mybentley:id/textView_combined_range_vsr_combined_range").exists:
                        fuel_range = self.d(resourceId="uk.co.bentley.mybentley:id/textView_combined_range_vsr_combined_range").get_text()
                        fuel_details["combined range"] = fuel_range
                except:
                    pass

        except Exception as e:
            print(f"❌ Error while extracting fuel details: {e}")

        return fuel_details

    def check_units(self, units):
        if self.d(resourceId="uk.co.bentley.mybentley:id/textView_combined_range_vsr_combined_range").exists:
            current_units = self.d(resourceId="uk.co.bentley.mybentley:id/textView_combined_range_vsr_combined_range").get_text()
            return current_units[-2:] == units
        return False

    def extract_service_management(self):
        service_management = []
        services = ['Theft alert', 'Lock my car', 'Find my car', 'Perimeter alert', 'Speed and curfew alert',
                    'Valet alert', 'My car status', 'My battery charge', 'My cabin comfort', 'My car statistics',
                    'Activate heating', 'Remote park assist']
        try:
            for _ in range(2):
                for service in services:
                    if self.d(text=service).exists and service not in service_management:
                        service_management.append(service)
                self.swipe_up()
        except Exception as e:
            print("❌ Error while extracting service management details: {e}")

        return service_management