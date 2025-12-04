import subprocess
import os
from time import sleep, time
from core import globals

class ScreenRecorder:
    def __init__(self, device_serial):
        self.device = device_serial
        base_dir = os.path.dirname(os.path.abspath(__file__))
        project_dir = os.path.dirname(base_dir)
        self.save_dir = os.path.join(project_dir, "gui", "fail_images")
        self.temp_path = "/sdcard/test_rec.mp4"
        self.process = None
        self.output_path = None
        self.start_time = 0

        os.makedirs(self.save_dir, exist_ok=True)

    def start(self, test_name):
        filename = f"{test_name}.mp4"
        self.output_path = os.path.join(self.save_dir, filename)

        adb = ["adb", "-s", self.device]
        cmd = adb + ["shell", "screenrecord", self.temp_path]

        self.process = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        sleep(0.5)
        self.start_time = time()
        return self.output_path

    def stop(self, save=True):
        run_time = time() - self.start_time
        if not self.process:
            return None

        self.process.terminate()
        self.process.wait(timeout=5)
        sleep(1)

        adb = ["adb", "-s", self.device]
        if save:
            subprocess.run(adb + ["pull", self.temp_path, self.output_path],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=30)

        adb = ["adb", "-s", self.device]
        subprocess.run(adb + ["shell", "rm", self.temp_path],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=5)

        return run_time