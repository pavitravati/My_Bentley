from PySide6.QtCore import QObject, Signal
from common_utils.android_image_comparision import *
from core.kpm_creater import create_kpm
from core import globals

class LogEmitter(QObject):
    log_signal = Signal(str)

log_emitter = LogEmitter()

def log(msg):
    print(f"✅ - {msg}")
    log_emitter.log_signal.emit(f"✅ - {msg}")

def metric_log(msg):
    print(msg)
    log_emitter.log_signal.emit(f"{msg}")

def fail_log(msg, num, service, screenshot=True):
    print(f"❌ - {msg}")
    log_emitter.log_signal.emit(f"❌ - {msg}")
    if screenshot:
        controller.take_fail_screenshot(f"{service}-{msg}-{num}.png")
    existing_kpm = False
    for log in globals.log_history[service][int(num)]:
        if log[0] == "$":
            existing_kpm = True
    if not existing_kpm:
        log_emitter.log_signal.emit(f"${create_kpm()}")

def blocked_log(msg):
    print(f"🔒 - {msg}")
    log_emitter.log_signal.emit(f"🔒{msg}")

def error_log(e, num, service):
    print(f"⚠️ - {e}")
    log_emitter.log_signal.emit(f"⚠️ - Unexpected error: {e}")
    controller.take_fail_screenshot(f"{service}-{e}-{num}.png")