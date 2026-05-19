import json
import subprocess
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SCRIPT = ROOT / "FiveApp001.py"


def run_number_script():
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


class FiveAppHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        if self.path == "/api/number":
            self.send_number()
            return

        super().do_GET()

    def send_number(self):
        try:
            payload = {"output": run_number_script()}
            status = 200
        except subprocess.CalledProcessError as error:
            payload = {"error": error.stderr.strip() or str(error)}
            status = 500

        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def main():
    server_address = ("localhost", 8000)
    print("Serving Five App at http://localhost:8000")
    ThreadingHTTPServer(server_address, FiveAppHandler).serve_forever()


if __name__ == "__main__":
    main()
