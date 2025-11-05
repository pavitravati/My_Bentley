from PySide6.QtCore import QObject, Signal
from common_utils.android_image_comparision import *

class LogEmitter(QObject):
    log_signal = Signal(str)

log_emitter = LogEmitter()

def log(msg):
    print(f"✅ - {msg}")
    log_emitter.log_signal.emit(f"✅ - {msg}")

def metric_log(msg):
    print(msg)
    log_emitter.log_signal.emit(f"{msg}")

def fail_log(msg, num, service):
    print(f"❌ - {msg}")
    log_emitter.log_signal.emit(f"❌ - {msg}")
    controller.take_fail_screenshot(f"{service}-{msg}-{num}.png")

def error_log(e, num, service):
    print(f"⚠️ - {e}")
    log_emitter.log_signal.emit(f"⚠️ - Unexpected error: {e}")
    controller.take_fail_screenshot(f"{service}-{e}-{num}.png")