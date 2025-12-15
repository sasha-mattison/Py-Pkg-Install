import subprocess

packages = ["fastfetch"]

distro = None
def run(cmd):
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ignored non-critical error: {e}")

def find_distro():
    print("Which Linux distro are you using?")
    print("Arch based: 1")
    print("Debian based: 2")
    print("Fedora based: 3")
    user_input = int(input(">>> "))
    if user_input == 1:
        return "Arch"
    elif user_input == 2:
        return "Debian"
    elif user_input == 3:
        return "Fedora"
    else:
        print("Invalid input, try again")
        return find_distro()
    
distro = find_distro()

def package_manager():
    global distro 
    if distro == "Arch":
        return "sudo pacman -Syu "
    elif distro == "Debian":
        return "sudo apt install "
    else:
        return "sudo dnf install "


pack = package_manager()

def installer():
    print("Installing packages...")
    for i in range(len(packages)):
        run(pack + packages[i])

installer()