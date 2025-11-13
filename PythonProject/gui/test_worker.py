from PySide6.QtCore import QObject, Signal, Slot, QWaitCondition, QMutex
import importlib, sys, os
from excel import load_data
from core import globals
import traceback

testcase_map = load_data()

class TestRunnerWorker(QObject):
    finished = Signal()
    progress = Signal(int)
    current_row = Signal(int)
    row_finished = Signal(int)
    need_precondition = Signal(int)

    start_manual = Signal(int)

    def __init__(self, service, testcase_count, parent=None):
        super().__init__(parent)
        self.service = service
        self.testcase_count = testcase_count
        self._is_running = True

        self._wait_condition = QWaitCondition()
        self._mutex = QMutex()
        self._resume = False

        self.start_manual.connect(self.manual_run)

        # import test script module
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        test_scripts_path = os.path.join(project_root, "Test_Scripts", "Android")
        if test_scripts_path not in sys.path:
            sys.path.insert(0, test_scripts_path)
        try:
            self.module = importlib.import_module(self.service)
        except ModuleNotFoundError:
            print(f"⚠️ No module found for service {self.service}")
            self.module = None

    @Slot()
    def run(self):
        if not self.module:
            self.finished.emit()
            return

        for row in range(1, self.testcase_count + 1):
            # check early exit
            if not self._is_running:
                break

            self.current_row.emit(row)

            case = testcase_map[self.service][row-1]

            # If this row has preconditions, pause until UI confirms
            if case["Pre-Condition"]:
                self.need_precondition.emit(row)
                # wait but also break out if we are asked to stop
                self._mutex.lock()
                while not self._resume and self._is_running:
                    self._wait_condition.wait(self._mutex)
                self._resume = False
                self._mutex.unlock()
                if not self._is_running:
                    break

            # build function name
            fixed_function_name = self.service.replace(" ", "_").replace("-", "_").replace("& ", "")
            func_name = f"{fixed_function_name}_{row:03d}"
            func = getattr(self.module, func_name, None)

            if func:
                try:
                    func()
                except Exception as e:
                    # catch exceptions to avoid unpredictable thread state
                    print(f"Exception in test {func_name}: {e}")
                    traceback.print_exc()
            else:
                print(f"No function named {func_name}")

            self.progress.emit(row)
            self.row_finished.emit(row)

            if not self._is_running:
                break

        # ensure finished is always emitted once
        self.finished.emit()

    def stop(self):
        """
        Request the worker to stop. This must wake any wait_condition
        so the worker loop can exit promptly.
        """
        # mark for stop
        self._is_running = False
        # wake any waiting precondition
        self._mutex.lock()
        self._resume = True
        self._wait_condition.wakeAll()
        self._mutex.unlock()

    def resume(self):
        self._mutex.lock()
        self._resume = True
        self._wait_condition.wakeAll()
        self._mutex.unlock()

    @Slot(int)
    def manual_run(self, row_index):
        current_row = row_index + 1
        # Ensure logging entry exists BEFORE running test
        if self.service not in globals.log_history:
            globals.log_history[self.service] = {}
        if current_row not in globals.log_history[self.service]:
            globals.log_history[self.service][current_row] = []

        self.current_row.emit(current_row)

        if not self.module:
            self.finished.emit()
            return

        case = testcase_map[self.service][current_row - 1]

        if case["Pre-Condition"]:
            self.need_precondition.emit(current_row)
            self._mutex.lock()
            while not self._resume and self._is_running:
                self._wait_condition.wait(self._mutex)
            self._resume = False
            self._mutex.unlock()
            if not self._is_running:
                self.finished.emit()
                return

        fixed_function_name = self.service.replace(" ", "_").replace("-", "_").replace("& ", "")
        func_name = f"{fixed_function_name}_{current_row:03d}"
        func = getattr(self.module, func_name, None)
        if func:
            try:
                func()
            except Exception as e:
                print(f"Exception in manual test {func_name}: {e}")
                traceback.print_exc()
        else:
            print(f"No function named {func_name}")

        self.progress.emit(current_row)
        self.row_finished.emit(current_row)

        self.finished.emit()