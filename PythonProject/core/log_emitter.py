from PySide6.QtCore import QObject, Signal

class LogEmitter(QObject):
    log_signal = Signal(str)

log_emitter = LogEmitter()