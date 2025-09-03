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

    def is_text_present(self, text):
        """Check if the given text is present on screen."""
        return self.d(text=text).exists

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
            #print(f" Image file not found: {template_path}")
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



