import core.globals as globals
from datetime import datetime
import os, glob
import io
import zipfile
from PySide6.QtGui import QDesktopServices
from PySide6.QtCore import QUrl

def download_kpm(service, row, manual=False):
    if manual:
        existing_files = []
        base_dir = os.path.dirname(os.path.abspath(__file__))
        project_dir = os.path.dirname(base_dir)
        image_dir = os.path.join(project_dir, "gui", "fail_images")
        for file_type in ['png', 'mp4']:
            for file in glob.glob(os.path.join(image_dir, f"*.{file_type}")):
                filename = os.path.basename(file)
                if service in filename:
                    existing_files.append(file)
    else:
        existing_files = []

    folder_name = f"KPM-{service}{row}"

    # --- create zip in memory ---
    zip_bytes = io.BytesIO()

    with zipfile.ZipFile(zip_bytes, 'w', zipfile.ZIP_DEFLATED) as z:

        # add existing files
        for f in existing_files:
            arcname = f"{folder_name}/{os.path.basename(f)}"
            z.write(f, arcname=arcname)

        # add a text file (created in memory)
        z.writestr(f"{folder_name}/KPM template.txt", create_kpm())

    # after writing you must seek to start
    zip_bytes.seek(0)

    # --- save only the ZIP file to user's Downloads folder ---
    downloads = os.path.join(os.path.expanduser("~"), "Downloads")
    os.makedirs(downloads, exist_ok=True)

    output_zip_path = os.path.join(downloads, f"{folder_name}.zip")

    with open(output_zip_path, "wb") as f:
        f.write(zip_bytes.read())

# Example button
# button = QPushButton("Download Folder")
# button.clicked.connect(download_zip)

def create_kpm():
    now = datetime.now()
    day = now.day
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][day % 10 - 1]
    current_date = now.strftime(f"%#d{suffix} %B %Y")
    current_time = now.strftime("%I:%M %p")

    return f"""Issue-1 : Smart Quality_[{globals.phone_type.title()}] -

Precondition :


Steps :


Actual :


Note : 

Expected :


Recovery : 

Reproducibility : 

At what level of PEP we are seeing this : 

Feature Owner : 

Proposed KPM Rating : 

Region : {globals.country.upper()}

Date : {current_date}
Place : []
Time : {current_time}

Account and VIN Info :
Username : {globals.current_email}
Password : {globals.current_password}
VIN : {globals.current_vin}

MIB SW : 

Asterix SW : 

App Info : ({globals.phone_type.upper()})
{globals.app_version}

Mobile Device Info :
Mobile : {globals.device}
Platform : {globals.phone_type.upper()}
S/W Version : {globals.phone_software}

Backend Information(Vehicle) : 

Note : 
"""