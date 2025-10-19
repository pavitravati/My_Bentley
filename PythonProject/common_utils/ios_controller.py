
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from appium.options.ios import XCUITestOptions
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
import time
import os
import cv2


class IOSController:
    def __init__(self, mac_ip, port, udid, team_id, bundle_id):
        self.mac_ip = mac_ip
        self.port = port
        self.udid = udid
        self.team_id = team_id
        self.bundle_id = bundle_id  # Required to launch app at session start
        self.driver = None

    def start_session(self):
        options = XCUITestOptions()
        options.set_capability("platformName", "iOS")
        options.set_capability("automationName", "XCUITest")
        options.set_capability("deviceName", "iPhone")
        options.set_capability("platformVersion", "18.2")
        options.set_capability("udid", self.udid)
        options.set_capability("bundleId", self.bundle_id)
        options.set_capability("xcodeOrgId", self.team_id)
        options.set_capability("xcodeSigningId", "iPhone Developer")
        options.set_capability("noReset", True)

        self.driver = webdriver.Remote(f"http://{self.mac_ip}:{self.port}", options=options)
        time.sleep(3)
        print("iOS session started and app launched")

    def launch_app(self, bundle_id):
        if not self.driver:
            raise RuntimeError("Driver not initialized. Call start_session() first.")

        try:
            self.driver.execute_script("mobile: launchApp", {"bundleId": bundle_id})
            print(f"App launched: {bundle_id}")
        except Exception as e:
            print(f"Failed to launch app {bundle_id}: {e}")

    def click_element(self, accessibility_id=None, xpath=None):
        """
        Clicks an iOS element if visible.

        Args:
            accessibility_id: Accessibility id of the element (preferred)
            xpath: XPath of the element (fallback)

        Returns:
            True if clicked, False if not found
        """
        try:
            if accessibility_id:
                elem = self.driver.find_element("accessibility id", accessibility_id)
                if elem.is_displayed():
                    elem.click()
                    print(f"✅ Clicked element via accessibility id: {accessibility_id}")
                    return True
        except NoSuchElementException:
            pass

        try:
            if xpath:
                elem = self.driver.find_element("xpath", xpath)
                if elem.is_displayed():
                    elem.click()
                    print(f"✅ Clicked element via XPath: {xpath}")
                    return True
        except NoSuchElementException:
            pass

        print("❌ Element not found")
        return False

    def get_resource_path(self, filename):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(base_dir, ".."))
        return os.path.join(project_root, "resource", filename)

    def tap(self, x, y):
        if not self.driver:
            raise RuntimeError("Driver not initialized. Call start_session() first.")

        actions = ActionBuilder(self.driver)
        finger = actions.add_pointer_input("touch", "finger1")

        finger.create_pointer_move(duration=0, x=x, y=y)
        finger.create_pointer_down(button=0)
        finger.create_pointer_up(button=0)

        actions.perform()

        print(f" Tap at ({x}, {y})")

    def swipe(self, direction="up"):
        if not self.driver:
            raise RuntimeError("Driver not initialized. Call start_session() first.")

        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']

        start_x = width // 2
        start_y = int(height * 0.8)
        end_y = int(height * 0.2)
        end_x = start_x

        if direction == "down":
            start_y, end_y = end_y, start_y
        elif direction == "left":
            start_x = int(width * 0.8)
            end_x = int(width * 0.2)
            start_y = end_y = height // 2
        elif direction == "right":
            start_x = int(width * 0.2)
            end_x = int(width * 0.8)
            start_y = end_y = height // 2

        actions = ActionBuilder(self.driver)
        finger = actions.add_pointer_input("touch", "finger1")

        finger.create_pointer_move(duration=0, x=start_x, y=start_y)
        finger.create_pointer_down(button=0)
        finger.create_pointer_move(duration=800, x=end_x, y=end_y)
        finger.create_pointer_up(button=0)

        actions.perform()
        print(f" Swipe {direction} completed")

    def take_screenshot(self, filename="ios_screenshot.png"):
        if not self.driver:
            raise RuntimeError(" Driver not initialized. Call start_session() first.")

        path = self.get_resource_path(filename)  # Save directly inside 'resource' folder
        self.driver.save_screenshot(path)
        print(f"📸 Screenshot saved at {path}")
        return path  # Important: return the path for further use

    def click_by_text(self, text):
        """Click on element by visible text (label)."""
        if not self.driver:
            raise RuntimeError("Driver not initialized. Call start_session() first.")
        try:
            element = self.driver.find_element("accessibility id", text)
            element.click()
            print(f"Clicked element with text: {text}")
        except Exception as e:
            raise RuntimeError(f" Could not find or click element with text '{text}': {e}")

    def click_by_image(self, image_filename, threshold=0.8):
        """Click on the screen by matching an image using OpenCV and return True/False."""

        if not self.driver:
            raise RuntimeError("Driver not initialized. Call start_session() first.")

        try:
            # Save screenshot in resource folder
            screenshot_filename = "ios_screen.png"
            self.take_screenshot(screenshot_filename)
            screenshot_path = self.get_resource_path(screenshot_filename)
            template_path = self.get_resource_path(image_filename)

            # Load images
            screen = cv2.imread(screenshot_path)
            template = cv2.imread(template_path)

            if screen is None or template is None:
                raise RuntimeError("Failed to load screenshot or template image.")

            # Template matching
            result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv2.minMaxLoc(result)

            print(f"🔎 Match Confidence: {max_val:.2f}")

            if max_val < threshold:
                print(f"❌ Image match failed. Confidence {max_val:.2f} < threshold {threshold}")
                return False  # ❗ Return False instead of raising

            # Center of matched region
            h, w = template.shape[:2]
            match_x = max_loc[0] + w // 2
            match_y = max_loc[1] + h // 2

            # Get actual device size
            device_size = self.driver.get_window_size()
            device_width = device_size["width"]
            device_height = device_size["height"]

            # Get screenshot size
            screen_height, screen_width = screen.shape[:2]

            # Scale to actual device coordinates
            scale_x = device_width / screen_width
            scale_y = device_height / screen_height
            tap_x = int(match_x * scale_x)
            tap_y = int(match_y * scale_y)

            print(f"✅ Found image at: ({match_x}, {match_y}), tapping at center: ({tap_x}, {tap_y})")
            self.tap(tap_x, tap_y)

            return True  # ✅ Success case

        except Exception as e:
            print(f"⚠️ Error in click_by_image: {e}")
            return False  # ✅ Always return False on any failure

    def extract_dashboard_metrics_Overview(self):
        metrics = {}
        try:
            # Dictionary with primary & fallback XPaths for each label
            label_value_xpaths = {
                "Mileage": [
                    ("//XCUIElementTypeStaticText[@label='Mileage']",
                     "(//XCUIElementTypeStaticText[@label='Mileage']/following-sibling::XCUIElementTypeStaticText)[1]"),
                    ("//XCUIElementTypeStaticText[@name='Mileage']",
                     "(//XCUIElementTypeStaticText[@name='Mileage']/following-sibling::XCUIElementTypeStaticText)[1]")
                ],
                "Lights": [
                    ("//XCUIElementTypeStaticText[@label='Lights']",
                     "(//XCUIElementTypeStaticText[@label='Lights']/following-sibling::XCUIElementTypeStaticText)[1]"),
                    ("//XCUIElementTypeStaticText[@name='Lights']",
                     "(//XCUIElementTypeStaticText[@name='Lights']/following-sibling::XCUIElementTypeStaticText)[1]")
                ],
                "Fuel": [
                    ("//XCUIElementTypeStaticText[@label='Fuel range']",
                     "(//XCUIElementTypeStaticText[@label='Fuel range']/following-sibling::XCUIElementTypeStaticText)[1]"),
                    ("//XCUIElementTypeStaticText[contains(@label,'Fuel')]",
                     "(//XCUIElementTypeStaticText[contains(@label,'Fuel')]/following-sibling::XCUIElementTypeStaticText)[1]")
                ],
                "Boot": [
                    ("//XCUIElementTypeStaticText[@label='Boot']",
                     "(//XCUIElementTypeStaticText[@label='Boot']/following-sibling::XCUIElementTypeStaticText)[1]"),
                    ("//XCUIElementTypeStaticText[@name='Boot']",
                     "(//XCUIElementTypeStaticText[@name='Boot']/following-sibling::XCUIElementTypeStaticText)[1]")
                ],
                "Bonnet": [
                    ("//XCUIElementTypeStaticText[@label='Bonnet']",
                     "(//XCUIElementTypeStaticText[@label='Bonnet']/following-sibling::XCUIElementTypeStaticText)[1]"),
                    ("//XCUIElementTypeStaticText[@name='Bonnet']",
                     "(//XCUIElementTypeStaticText[@name='Bonnet']/following-sibling::XCUIElementTypeStaticText)[1]")
                ],
                "Doors": [
                    ("//XCUIElementTypeStaticText[@label='Doors']",
                     "(//XCUIElementTypeStaticText[@label='Doors']/ancestor::XCUIElementTypeOther/following-sibling::XCUIElementTypeOther//XCUIElementTypeStaticText)[1]"),
                    ("//XCUIElementTypeStaticText[contains(@label,'Door')]",
                     "(//XCUIElementTypeStaticText[contains(@label,'Door')]/ancestor::XCUIElementTypeOther/following-sibling::XCUIElementTypeOther//XCUIElementTypeStaticText)[1]")
                ],
                "Windows": [
                    ("//XCUIElementTypeStaticText[@label='Windows']",
                     "(//XCUIElementTypeStaticText[@label='Windows']/ancestor::XCUIElementTypeOther/following-sibling::XCUIElementTypeOther//XCUIElementTypeStaticText)[1]"),
                    ("//XCUIElementTypeStaticText[contains(@label,'Window')]",
                     "(//XCUIElementTypeStaticText[contains(@label,'Window')]/ancestor::XCUIElementTypeOther/following-sibling::XCUIElementTypeOther//XCUIElementTypeStaticText)[1]")
                ],
                "Oil Level": [
                    ("//XCUIElementTypeStaticText[@label='Oil level']",
                     "(//XCUIElementTypeStaticText[@label='Oil level']/following-sibling::XCUIElementTypeStaticText)[1]"),
                    ("//XCUIElementTypeStaticText[contains(@label,'Oil level')]",
                     "(//XCUIElementTypeStaticText[contains(@label,'Oil level')]/following-sibling::XCUIElementTypeStaticText)[1]")
                ],
                "Oil Change": [
                    ("//XCUIElementTypeStaticText[@label='Oil change']",
                     "(//XCUIElementTypeStaticText[@label='Oil change']/following-sibling::XCUIElementTypeStaticText)[1]"),
                    ("//XCUIElementTypeStaticText[contains(@label,'Oil change')]",
                     "(//XCUIElementTypeStaticText[contains(@label,'Oil change')]/following-sibling::XCUIElementTypeStaticText)[1]")
                ],
                "Cluster Warnings": [
                    ("//XCUIElementTypeStaticText[@label='Cluster warnings']",
                     "(//XCUIElementTypeStaticText[@label='Cluster warnings']/following-sibling::XCUIElementTypeStaticText)[1]"),
                    ("//XCUIElementTypeStaticText[contains(@label,'Cluster')]",
                     "(//XCUIElementTypeStaticText[contains(@label,'Cluster')]/following-sibling::XCUIElementTypeStaticText)[1]")
                ]
            }

            # Loop through metrics and try primary → fallback
            for label, xpaths in label_value_xpaths.items():
                extracted = False
                for (label_xpath, value_xpath) in xpaths:
                    try:
                        label_elem = self.driver.find_element("xpath", label_xpath)
                        value_elem = self.driver.find_element("xpath", value_xpath)
                        value = value_elem.get_attribute("label") or value_elem.get_attribute("value")
                        metrics[label] = value
                        #print(f"✅ Extracted '{label}' using locator: {label_xpath}")
                        extracted = True
                        break  # stop trying other fallbacks
                    except Exception:
                        continue
                if not extracted:
                    print(f"⚠️ Could not extract '{label}' using any locator.")

        except Exception as e:
            print(f"❌ Error while extracting metrics: {e}")


            # Print output
        if metrics:
            print("\n✅ Extracted Metrics:")
            for k, v in metrics.items():
                print(f"{k}: {v}")
        else:
            print("⚠️ No metrics found.")

        return metrics

    def extract_car_statistics(self):
        metrics = {}
        try:
            value_xpath =  "(//XCUIElementTypeStaticText[@label='MY CAR STATISTICS']/following::XCUIElementTypeStaticText)[1]"
            value_elem = self.driver.find_element("xpath", value_xpath)
            metrics["Last Trip"] = value_elem.get_attribute("label") or value_elem.get_attribute("value")
        except Exception as e:
            print(f"⚠️ Could not extract 'MY CAR STATISTICS': {e}")

        # ✅ Print directly here
        if metrics:
            print("\n✅ Extracted Car Statistics:")
            for k, v in metrics.items():
                print(f"{k}: {v}")
        else:
            print("⚠️ No Car Statistics found.")

        return metrics

        # ------------------ Battery Charge ------------------

    def extract_battery_charge(self):
        metrics = {}
        try:
            value_xpath = "(//XCUIElementTypeStaticText[@label='MY BATTERY CHARGE']/following::XCUIElementTypeStaticText)[1]"
            value_elem = self.driver.find_element("xpath", value_xpath)
            metrics["Battery Status"] = value_elem.get_attribute("label") or value_elem.get_attribute("value")
        except Exception as e:
            print(f"⚠️ Could not extract 'MY BATTERY CHARGE': {e}")
        if metrics:
            print("\n✅ Extracted Battery Charge:")
            for k, v in metrics.items():
                print(f"{k}: {v}")
        else:
            print("⚠️ No Battery Charge info found.")

        return metrics

        # ------------------ Cabin Comfort ------------------

    def extract_cabin_comfort(self):
        metrics = {}
        try:
            value_xpath =  "(//XCUIElementTypeStaticText[@label='MY CABIN COMFORT']/following::XCUIElementTypeStaticText)[1]"
            value_elem = self.driver.find_element("xpath", value_xpath)
            metrics["Cabin Comfort"] = value_elem.get_attribute("label") or value_elem.get_attribute("value")
        except Exception as e:
            print(f"⚠️ Could not extract 'MY CABIN COMFORT': {e}")
        if metrics:
            print("\n✅ Extracted Cabin Comfort:")
            for k, v in metrics.items():
                print(f"{k}: {v}")
        else:
            print("⚠️ No Cabin Comfort info found.")

        return metrics
        # ------------------ Remote Parking ------------------

    def extract_remote_parking(self):
        metrics = {}
        try:
            value_xpath = "(//XCUIElementTypeStaticText[@label='REMOTE PARKING']/following-sibling::XCUIElementTypeOther//XCUIElementTypeStaticText)[1]"
            value_elem = self.driver.find_element("xpath", value_xpath)
            metrics["Remote Parking"] = value_elem.get_attribute("label") or value_elem.get_attribute("value")
        except Exception as e:
            print(f"⚠️ Could not extract 'REMOTE PARKING': {e}")
        if metrics:
            print("\n✅ Extracted Remote Parking:")
            for k, v in metrics.items():
                print(f"{k}: {v}")
        else:
            print("⚠️ No Remote Parking info found.")

        return metrics

        # ------------------ Theft Alarm ------------------

    def extract_theft_alarm(self):
        metrics = {}
        try:
            value_xpath =  "(//XCUIElementTypeStaticText[@label='THEFT ALARM']/following-sibling::XCUIElementTypeOther//XCUIElementTypeStaticText)[1]"
            value_elem = self.driver.find_element("xpath", value_xpath)
            metrics["Theft Alarm"] = value_elem.get_attribute("label") or value_elem.get_attribute("value")
        except Exception as e:
            print(f"⚠️ Could not extract 'THEFT ALARM': {e}")
        if metrics:
            print("\n✅ Extracted Theft Alarm:")
            for k, v in metrics.items():
                print(f"{k}: {v}")
        else:
            print("⚠️ No Theft Alarm info found.")

        return metrics

        # ------------------ Roadside Assistance ------------------

    def extract_roadside_assistance(self):
        metrics = {}
        try:
            value_xpath =  "(//XCUIElementTypeStaticText[@label='ROADSIDE ASSISTANCE']/following-sibling::XCUIElementTypeOther//XCUIElementTypeStaticText)[1]"
            value_elem = self.driver.find_element("xpath", value_xpath)
            metrics["Roadside Assistance"] = value_elem.get_attribute("label") or value_elem.get_attribute("value")
        except Exception as e:
            print(f"⚠️ Could not extract 'ROADSIDE ASSISTANCE': {e}")
        if metrics:
            print("\n✅ Extracted Roadside Assistance:")
            for k, v in metrics.items():
                print(f"{k}: {v}")
        else:
            print("⚠️ No Roadside Assistance info found.")

        return metrics

        # ------------------ Data Services ------------------

    def extract_data_services(self):
        metrics = {}
        try:
            value_xpath = "(//XCUIElementTypeStaticText[@label='DATA SERVICES']/following-sibling::XCUIElementTypeOther//XCUIElementTypeStaticText)[1]"
            value_elem = self.driver.find_element("xpath", value_xpath)
            metrics["Data Services"] = value_elem.get_attribute("label") or value_elem.get_attribute("value")
        except Exception as e:
            print(f"⚠️ Could not extract 'DATA SERVICES': {e}")
        if metrics:
            print("\n✅ Extracted Data Services:")
            for k, v in metrics.items():
                print(f"{k}: {v}")
        else:
            print("⚠️ No Data Services info found.")

        return metrics

    def extract_last_updated(self):
        details = {}
        try:
            xml_source = self.driver.page_source

            import xml.etree.ElementTree as ET
            root = ET.fromstring(xml_source)

            for elem in root.iter("XCUIElementTypeStaticText"):
                # Get all relevant attributes
                value = elem.attrib.get("value", "")
                name = elem.attrib.get("name", "")
                label = elem.attrib.get("label", "")

                # Normalize spaces and lowercase for comparison
                combined = " ".join([value, name, label]).replace("\u202F", " ").lower()

                if "last updated" in combined:
                    # Pick whichever attribute is non-empty
                    details["Last updated"] = value or label or name
                    break

        except Exception as e:
            print(f"⚠️ Could not extract 'Last updated': {e}")

        if details:
            print("\n✅ Extracted Last Updated:")
            for k, v in details.items():
                print(f"{k}: {v}")
        else:
            print("⚠️ No 'Last updated' info found.")

        return details

    def click_element_generic(self, locator_type, locator_value, timeout=10):
        """
        Generic function to click an element on iOS.

        Args:
            locator_type: 'accessibility_id' or 'xpath'
            locator_value: the value of the locator
            timeout: max wait time in seconds

        Returns:
            True if clicked successfully, False otherwise
        """
        if not self.driver:
            raise RuntimeError("Driver not initialized. Call start_session() first.")

        try:
            if locator_type.lower() == "accessibility_id":
                element = WebDriverWait(self.driver, timeout).until(
                    EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, locator_value))
                )
            elif locator_type.lower() == "xpath":
                element = WebDriverWait(self.driver, timeout).until(
                    EC.element_to_be_clickable((AppiumBy.XPATH, locator_value))
                )
            else:
                raise ValueError(f"Unsupported locator type: {locator_type}")

            element.click()
            print(f"✅ Clicked element using {locator_type}: {locator_value}")
            return True

        except Exception as e:
            print(f"❌ Failed to click element using {locator_type}: {locator_value}. Error: {e}")
            return False

    def quit(self):
        if self.driver:
            self.driver.quit()
            print(" Session ended")
