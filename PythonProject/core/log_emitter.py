from PySide6.QtCore import QObject, Signal
from common_utils.android_image_comparision import *

class LogEmitter(QObject):
    log_signal = Signal(str)

log_emitter = LogEmitter()

def log(msg):
    log_emitter.log_signal.emit(f"✅ - {msg}")

def metric_log(msg):
    log_emitter.log_signal.emit(f"{msg}")

def fail_log(msg, num):
    log_emitter.log_signal.emit(f"❌ - {msg}")
    controller.take_fail_screenshot(f"Vehicle Status Report-{msg}-{num}.png")

def error_log(e, num):
    log_emitter.log_signal.emit(f"⚠️ - Unexpected error: {e}")
    controller.take_fail_screenshot(f"Vehicle Status Report-{e}-{num}.png")