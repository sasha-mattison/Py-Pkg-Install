import subprocess

linux_packages = [["fastfetch", "btop", "git", "firefox"], ["fastfetch", "btop", "git", "nvim", "zsh", "firefox", "waybar"], ["fastfetch", "btop", "git", "nvim", "zsh", "openjdk", "firefox", "waybar"]]

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
    user_input = str(input(">>> "))
    if user_input == "1":
        return "Arch"
    elif user_input == "2":
        return "Debian"
    elif user_input == "3":
        return "Fedora"
    else:
        print("Invalid input, try again")
        print("If you don't see your distro base it is currently not supported")
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

def linux_crate_select_install():
    global distro
    print("Select crate type:")
    print("Basic: 1")
    print("Advanced: 2")
    print("Developer: 3")
    print("Exit setup: 4")
    selec = str(input(">>>"))
    if selec in ("1", "2", "3", "4"):
        if selec == "1":
            install_on_linux(0)
        elif selec == "2":
            install_on_linux(1)
        elif selec == "3":
            install_on_linux(2)
        else:
            exit
    else:
        print("Invalid input, try again")
        linux_crate_select_install()


pack = package_manager()

def install_on_linux(selection):
    print("Installing packages...")
    for i in range(len(linux_packages[selection])):
        run(pack + linux_packages[selection][i])

linux_crate_select_install()