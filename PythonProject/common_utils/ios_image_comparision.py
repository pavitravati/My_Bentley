from skimage.metrics import structural_similarity as ssim
import os
import cv2
import time
from PythonProject.common_utils.ios_controller import IOSController

def find_icon_in_screen_ios(controller: IOSController, icon_filename, threshold=0.9):
    """
    Checks if the specified icon is visible on the iOS screen by matching it with a screenshot.

    :param controller: Instance of IOSController
    :param icon_filename: Filename of the icon image (relative to 'resource' folder)
    :param threshold: Confidence threshold (default: 0.8)
    :return: True if icon is found, else False
    """
    # Ensure threshold is a float
    threshold = float(threshold)
    # Get full path of icon
    icon_path = controller.get_resource_path(icon_filename)

    # Capture current screen (in resource/temp_ios_screen.png)
    temp_screenshot = "temp_ios_screen.png"
    screenshot_path = controller.get_resource_path(temp_screenshot)
    controller.driver.save_screenshot(screenshot_path)

    # Load both images
    icon = cv2.imread(icon_path, cv2.IMREAD_GRAYSCALE)
    screen = cv2.imread(screenshot_path, cv2.IMREAD_GRAYSCALE)

    # Clean up temp screenshot
    import os
    if os.path.exists(screenshot_path):
        os.remove(screenshot_path)

    # Error handling
    if icon is None:
        print(f" Could not read icon image: {icon_path}")
        return False
    if screen is None:
        print(f" Could not read screenshot: {screenshot_path}")
        return False

    # Match template
    result = cv2.matchTemplate(screen, icon, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, _ = cv2.minMaxLoc(result)

    print(f" Match confidence: {max_val:.2f}")
    return max_val >= threshold

def compare_with_expected_crop_ios(controller: IOSController, expected_image_name, threshold=0.95, output_subfolder="ios_images/output"):
    """
    Compare expected cropped image with current screen (in memory), and save bounding box only on mismatch.

    :param controller: Instance of IOSController
    :param expected_image_name: Filename like 'ios_home.png' (must be in resource/ios_images/)
    :param threshold: SSIM threshold
    :param output_subfolder: Subfolder inside 'resource' where diff will be saved
    :return: True if match passed, False otherwise
    """

    # Step 1: Load expected image
    expected_image_path = controller.get_resource_path(os.path.join("ios_images", expected_image_name))
    expected = cv2.imread(expected_image_path, cv2.IMREAD_GRAYSCALE)
    if expected is None:
        print(f" Could not load expected image: {expected_image_path}")
        return False

    # Step 2: Capture current screenshot and keep temporarily
    screenshot_path = controller.get_resource_path("temp_ios_screen.png")
    controller.driver.save_screenshot(screenshot_path)

    # Load both grayscale and color version before removing file
    screen_gray = cv2.imread(screenshot_path, cv2.IMREAD_GRAYSCALE)
    screen_color = cv2.imread(screenshot_path)
    os.remove(screenshot_path)  # Safe to delete now

    if screen_gray is None or screen_color is None:
        print(f" Could not load screenshot from: {screenshot_path}")
        return False

    # Step 3: Apply Gaussian blur
    expected_blur = cv2.GaussianBlur(expected, (3, 3), 0)
    screen_blur = cv2.GaussianBlur(screen_gray, (3, 3), 0)

    # Step 4: Template match
    result = cv2.matchTemplate(screen_blur, expected_blur, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    top_left = max_loc
    h, w = expected.shape
    bottom_right = (top_left[0] + w, top_left[1] + h)

    matched_region = screen_gray[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
    if matched_region.shape != expected.shape:
        print(" Shape mismatch between expected and matched region.")
        return False

    # Step 5: SSIM check
    score, _ = ssim(expected, matched_region, full=True)
    print(f" SSIM Score: {score:.4f}")

    # Step 6: Save difference box if mismatch
    if score < threshold:
        cv2.rectangle(screen_color, top_left, bottom_right, (0, 255, 0), 2)
        diff_name = f"match_box_{expected_image_name}"
        diff_path = controller.get_resource_path(os.path.join(output_subfolder, diff_name))
        os.makedirs(os.path.dirname(diff_path), exist_ok=True)
        cv2.imwrite(diff_path, screen_color)
        print(f" Mismatch - diff saved at: {diff_path}")
        return False

    # Step 7: Success
    print(" Match successful")
    return True