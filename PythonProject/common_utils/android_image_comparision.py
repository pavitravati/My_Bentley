import cv2
import os
from common_utils.android_controller import DeviceController
from skimage.metrics import structural_similarity as ssim
import numpy as np
controller = DeviceController()

def compare_images(expected, actual, threshold=0.99):
    img1_path = controller.get_resource_path(expected)
    img2_path = actual
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    # Convert to grayscale
    img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    score, diff = ssim(img1_gray, img2_gray, full=True)

    print(f"Similarity Score: {score}")

    if score >= threshold:
        print("Images are similar!")
    else:
        print("Images are different!")

def find_icon_in_screen(icon_filename, threshold=0.8):
    """
    Takes a screenshot and checks if the given icon image is present on the screen.
    :param icon_filename: Relative path to the icon image (e.g., 'Images/Close_Button.png')
    :param threshold: Matching threshold (default is 0.8)
    :return: True if icon is found on screen, False otherwise
    """
    # Ensure threshold is a float
    threshold = float(threshold)

    # Get icon image path
    icon_path = controller.get_resource_path(icon_filename)
    print("******", icon_path)

    # Capture current screen
    screenshot_path = controller.take_screenshot("temp.png")

    # Load images in grayscale
    icon = cv2.imread(icon_path, cv2.IMREAD_GRAYSCALE)
    screen = cv2.imread(screenshot_path, cv2.IMREAD_GRAYSCALE)

    # Error handling
    if icon is None:
        print("Could not read icon image: {icon_path}")
        return False
    if screen is None:
        print("Could not read screenshot: {screenshot_path}")
        return False

    # Template matching
    result = cv2.matchTemplate(screen, icon, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, _ = cv2.minMaxLoc(result)

    print("Match confidence: {max_val}")
    return max_val >= threshold

def compare_with_expected_crop(expected_image_path, threshold=0.95, output_folder="Images/output", greyscale=False):
    """
    Compare cropped expected image with current screen using template match + SSIM.
    Saves only the matched region bounding box if match fails.

    :param expected_image_path: Cropped expected image path (relative).
    :param threshold: SSIM threshold to pass.
    :param output_folder: Folder to save bounding box image.
    :return: True if match is above threshold, else False.
    """

    # Get full paths
    expected_image_path = controller.get_resource_path(expected_image_path)
    output_folder_path = controller.get_resource_path(output_folder)
    os.makedirs(output_folder_path, exist_ok=True)

    # Take screenshot
    screenshot_path = controller.take_screenshot("screen.png")
    #print("Screenshot taken: {screenshot_path}")

    # Load images in grayscale
    expected = cv2.imread(expected_image_path, cv2.IMREAD_GRAYSCALE)
    screen = cv2.imread(screenshot_path, cv2.IMREAD_GRAYSCALE)

    if expected is None:
        print("Could not load expected image: {expected_image_path}")
        return False
    if screen is None:
        print("Could not load screenshot: {screenshot_path}")
        return False

    # Apply Gaussian blur to reduce noise
    expected_blur = cv2.GaussianBlur(expected, (3, 3), 0)
    screen_blur = cv2.GaussianBlur(screen, (3, 3), 0)

    # Template matching
    result = cv2.matchTemplate(screen_blur, expected_blur, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    top_left = max_loc
    h, w = expected.shape
    bottom_right = (top_left[0] + w, top_left[1] + h)

    # Extract matched region
    matched_region = screen[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
    if matched_region.shape != expected.shape:
        print("Shape mismatch between expected and matched region")
        return False

    # SSIM check
    score, _ = ssim(expected, matched_region, full=True)
    #print("SSIM score: {score:.4f}")

    # Always save bounding box image for debug
    screen_color = cv2.imread(screenshot_path)
    cv2.rectangle(screen_color, top_left, bottom_right, (0, 255, 0), 2)
    match_box_path = os.path.join(output_folder_path, f"match_box_{os.path.basename(expected_image_path)}")
    cv2.imwrite(match_box_path, screen_color)
    #print(f"🟩 Match region saved: {match_box_path}")

    # Return result
    if score >= threshold:
        print(score)
        print("Match successful")
        return True
    else:
        print(score)
        print("Match failed")
        return False