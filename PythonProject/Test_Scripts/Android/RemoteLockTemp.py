from time import sleep
from PythonProject.common_utils.android_image_comparision import *
from PythonProject.common_utils.test_result_tracker import TestCaseResult
from PythonProject.common_utils.android_controller import *
from PySide6.QtCore import QObject, Signal
from PythonProject.core.log_emitter import log_emitter

controller = DeviceController()
d = u2.connect()

def log(msg):
    log_emitter.log_signal.emit(msg)

def Remote_Lock_Unlock001():
    try:
        controller.click_by_resource_id("uk.co.bentley.mybentley:id/tab_vehicle_dashboard")
        if (compare_with_expected_crop("Icons/Remote_Lock.png")) and (compare_with_expected_crop("Icons/Remote_Unlock.png")):
            log("✅ Success: Lock and Unlock button are visible with respect to current lock status of the vehicle.")
            log("✅ Remote_Lock_Unlock_001 passed")
        else:
            log("❌ Failed: Lock and Unlock button are visible with respect to current lock status of the vehicle.")
            log("❌ Remote_Lock_Unlock_001 failed")

    except Exception as e:
        log(f"Unexpected error: {e}")