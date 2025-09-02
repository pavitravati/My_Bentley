from datetime import datetime

class HTMLTestReport:
    def __init__(self, title, filename):
        self.title = title
        self.filename = filename
        self.test_results = []


    def add_test_result(self, name, status, description, duration, logs):
        self.test_results.append({
            "name": name,
            "status": status,
            "description": description,
            "duration": duration,
            "logs": logs
        })

    def generate_report(self):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.filename, "w", encoding="utf-8") as f:
            f.write(f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{self.title}</title>
    <style>
        body {{ font-family: Arial, sans-serif; background-color: #f7f7f7; padding: 20px; }}
        h1 {{ color: #333; }}
        table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
        th, td {{ border: 1px solid #ccc; padding: 8px; text-align: left; }}
        th {{ background-color: #333; color: white; }}
        .pass {{ background-color: #c8e6c9; }}
        .fail {{ background-color: #ffcdd2; }}
        .log-block {{ margin-top: 5px; font-family: monospace; background: #f1f1f1; padding: 10px; border: 1px solid #ccc; white-space: pre-wrap; }}
        .collapsible {{
            background-color: #eee;
            color: #444;
            cursor: pointer;
            padding: 10px;
            width: 100%;
            border: none;
            text-align: left;
            outline: none;
            font-size: 14px;
        }}
        .active, .collapsible:hover {{ background-color: #ccc; }}
        .content {{
            padding: 0 18px;
            display: none;
            overflow: hidden;
            background-color: #f9f9f9;
        }}
    </style>
</head>
<body>
    <h1>{self.title}</h1>
    <p>Generated on: {timestamp}</p>
    <table>
        <tr>
            <th>Test Case</th>
            <th>Status</th>
            <th>Description</th>
            <th>Duration</th>
            <th>Logs</th>
        </tr>
""")

            for result in self.test_results:
                row_class = "pass" if result['status'].lower() == "passed" else "fail"
                log_button_id = result["name"].replace(" ", "_")

                f.write(f"""
            <tr class="{row_class}">
                <td>{result["name"]}</td>
                <td>{result["status"]}</td>
                <td>{result["description"]}</td>
                <td>{result["duration"]}</td>
                <td>
                    <button class="collapsible">View Logs</button>
                    <div class="content"><div class="log-block">{result["logs"].replace("<", "&lt;").replace(">", "&gt;")}</div></div>
                </td>
            </tr>
            """)

            f.write("""
    </table>
    <script>
        const coll = document.getElementsByClassName("collapsible");
        for (let i = 0; i < coll.length; i++) {
            coll[i].addEventListener("click", function() {
                this.classList.toggle("active");
                const content = this.nextElementSibling;
                if (content.style.display === "block") {
                    content.style.display = "none";
                } else {
                    content.style.display = "block";
                }
            });
        }
    </script>
</body>
</html>
""")