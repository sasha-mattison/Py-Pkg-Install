import subprocess
import platform
import macos
import linux

os = platform.system()

if os == "Darwin":
    os = "MacOS"

def exec_on_os():
    if os in ("MacOS", "Linux"):
        print("Executing on " + os + "...")
    else:
        raise SystemExit("Unsupported OS")


#Program execution below

exec_on_os()

if os == "Linux":
    subprocess.run(linux.py)
else:
    subprocess.run(macos.py)