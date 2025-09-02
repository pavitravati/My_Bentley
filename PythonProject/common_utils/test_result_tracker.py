import time
import io
import sys

class TestCaseResult:
    def __init__(self, name):
        self.name = name
        self.status = "Passed"
        self.description = ""
        self.logs = ""
        self.start_time = None
        self.end_time = None
        self.log_stream = io.StringIO()

    def log(self, message: str):
        print(message)  # Print to console (redirected)
        self.log_stream.write(message + "\n")

    def log_step(self, message: str, success: bool):
        status = "✅" if success else "❌"
        self.log(f"{status} {message}")
        if not success:
            self.status = "Failed"

    def to_result_dict(self):
        duration = 0.0
        if self.start_time and self.end_time:
            duration = round(self.end_time - self.start_time, 2)

        return {
            "name": self.name,
            "status": self.status,
            "description": self.description,
            "duration": duration,
            "logs": self.logs.replace("\n", "<br>")
        }

    def set_status(self, status, description=""):
        self.status = status
        self.description = description

def run_test_with_logs(test_func):
    log_stream = io.StringIO()
    original_stdout = sys.stdout

    class DualLogger(io.TextIOBase):
        def write(self, message):
            original_stdout.write(message)   # Print to PyCharm console
            log_stream.write(message)        # Store for HTML report
            return len(message)

        def flush(self):
            original_stdout.flush()
            log_stream.flush()

    sys.stdout = DualLogger()  # Redirect to both

    try:
        result = test_func()
        if not isinstance(result, TestCaseResult):
            raise ValueError("Test function must return a TestCaseResult object")
    except Exception as e:
        result = TestCaseResult(test_func.__name__)
        result.set_status("Failed", f"Exception occurred: {e}")
        print(f"Exception: {e}")
    finally:
        sys.stdout = original_stdout  # Restore original stdout

    result.logs = log_stream.getvalue()
    return result