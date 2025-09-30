from PySide6.QtCore import QObject, Signal, Slot

class TestRunnerWorker(QObject):
    finished = Signal()
    progress = Signal(int)
    current_row = Signal(int)
    row_finished = Signal(int)

    def __init__(self, service, testcase_count, test_function_map, parent=None):
        super().__init__(parent)
        self.service = service
        self.testcase_count = testcase_count
        self.test_function_map = test_function_map
        self._is_running = True

    @Slot()
    def run(self):
        for row in range(1, self.testcase_count + 1):
            self.current_row.emit(row)
            if not self._is_running:
                break

            func_name = f"{self.service}_0{'0' + str(row) if row < 10 else str(row)}"
            func = self.test_function_map.get(func_name)

            if func:
                func()
            else:
                print(f"No function named {func_name}")

            self.progress.emit(row)

            self.row_finished.emit(row)

        self.finished.emit()

    def stop(self):
        self._is_running = False