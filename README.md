# JulesTest001
test repo for Jules

## Five App
A simple HTML application that asks a Python script for its output and displays the result.

## How to Run
1. Open PowerShell in this folder.
2. Run:
   ```powershell
   python server.py
   ```
3. Open this address in your browser:
   ```text
   http://localhost:8000
   ```

The page calls `/api/number`, the server runs `FiveApp001.py`, and the browser displays whatever the Python script prints.

To stop the server, press `Ctrl+C` in PowerShell.
