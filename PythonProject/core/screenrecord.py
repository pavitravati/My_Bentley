import subprocess
import os
from datetime import datetime
from time import sleep
from pathlib import Path


class ScreenRecorder:
    def __init__(self, device_serial):
        self.device = device_serial
        base_dir = os.path.dirname(os.path.abspath(__file__))
        project_dir = os.path.dirname(base_dir)
        self.save_dir = os.path.join(project_dir, "gui", "fail_images")
        self.temp_path = "/sdcard/test_rec.mp4"
        self.process = None
        self.output_path = None

        os.makedirs(self.save_dir, exist_ok=True)

    def start(self, test_name):
        filename = f"{test_name}.mp4"
        self.output_path = os.path.join(self.save_dir, filename)

        adb = ["adb", "-s", self.device]
        cmd = adb + ["shell", "screenrecord", self.temp_path]

        self.process = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        sleep(0.5)

        return self.output_path

    def stop(self, save=True):
        if not self.process:
            return None

        self.process.terminate()
        self.process.wait(timeout=5)
        sleep(1)

        if save:
            # Pull file from device
            adb = ["adb", "-s", self.device]
            subprocess.run(adb + ["pull", self.temp_path, self.output_path],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=30)

            subprocess.run(adb + ["shell", "rm", self.temp_path],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=5)

            return self.output_path
        else:
            adb = ["adb", "-s", self.device]
            subprocess.run(adb + ["shell", "rm", self.temp_path],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=5)
            return None