import subprocess
import platform
import time
import shutil

macos_packages_basic = ["fastfetch", "mactop"]
macos_packages_advanced = ["fastfetch"]
macos_packages_developer = ["mactop"]



os = platform.system()

if os == "Darwin":
    os = "MacOS"

def exec_on_os():
    if os in ("MacOS", "Linux"):
        print("Executing on " + os + "...")
        time.sleep(0.1)
    else:
        raise SystemExit("Unsupported OS")

def has_brew():
    return shutil.which("brew") is not None

def prepare_macos():
    print("Checking user permissions...")
    run("sudo echo 'User has adequete permissions'")
    if has_brew():
        print("Homebrew is installed:")
        print("Updating...")
        run("brew update && brew upgrade")
        print("System preparation is complete...")
    else:
        print("Homebrew is NOT installed:")
        print("Installing...")
        print("Checking user permissions...")
        run("sudo echo 'User has adequete permissions'")
        run('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')
        run("brew update && brew upgrade")

def install_on_macos1():
    print("Installing packages...")
    for i in range(len(macos_packages_basic)):
        run("brew install " + macos_packages_basic[i])

def install_on_macos2():
    print("Installing packages...")
    for i in range(len(macos_packages_advanced)):
        run("brew install " + macos_packages_advanced[i])

def install_on_macos3():
    print("Installing packages...")
    for i in range(len(macos_packages_developer)):
        run("brew install " + macos_packages_developer[i])

def macos_chest_select_install():
    print("Which chest (collection of packages) would you like to install?")
    print("Basic: 1")
    print("Advanced: 2")
    print("Developer: 3 (NOTE: may take a while)")
    selec = str(input("Enter choice: "))
    if selec in ("1", "2", "3"):
        if selec == "1":
            install_on_macos1()
        elif selec == "2":
            install_on_macos2()
        else:
            install_on_macos3()
    else:
        print("Invalid input, try again")
        macos_chest_select_install()

def get_linux_distro():
    distro = {}
    try:
        with open("/etc/os-release") as f:
            for line in f:
                line = line.strip()
                if not line or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                distro[k] = v.strip('"')
    except FileNotFoundError:
        return None

    return {
        "id": distro.get("ID"),
        "name": distro.get("NAME"),
        "like": distro.get("ID_LIKE"),
        "version": distro.get("VERSION_ID"),
    }


def run(cmd):
    subprocess.run(cmd, shell=True, check=True)

exec_on_os()

if os == "Linux":
    get_linux_distro()
else:
    prepare_macos()
    macos_chest_select_install()