import subprocess
import shutil

#Package list goes like so: Basic, Advanced, Developer
macos_packages = [["fastfetch", "mactop", "git"], ["fastfetch", "mactop", "btop", "git", "nvim", "kitty", "zsh"], ["mactop", "fastfetch", "btop", "git", "nvim", "kitty", "nasm", "openjdk", "qemu", "vim", "zsh", "pipes-sh"]]

#macos_repositories = [[], ['sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"'], ['sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"', 'git clone https://github.com/LazyVim/starter ~/.config/nvim']]

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
        run("sudo echo 'User has adequate permissions'")
        run('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')
        run("brew update && brew upgrade")

def install_on_macos(selection):
    print("Installing packages...")
    for i in range(len(macos_packages[selection])):
        run("brew install " + macos_packages[selection][i])
    #for i in range(len(macos_repositories[selection])):
        #run(macos_repositories[selection][i])

def macos_crate_select_install():
    print("Which chest (collection of packages) would you like to install?")
    print("Basic: 1")
    print("Advanced: 2")
    print("Developer: 3 (NOTE: may take a while)")
    selec = str(input("Enter choice: "))
    if selec in ("1", "2", "3"):
        if selec == "1":
            install_on_macos(0)
        elif selec == "2":
            install_on_macos(1)
        else:
            install_on_macos(2)
            run("xcode-select --install")
    else:
        run("clear")
        print("Invalid input, try again")
        macos_crate_select_install()

def run(cmd):
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ignored non-critical error: {e}")

#Program execution below

prepare_macos()
macos_crate_select_install()