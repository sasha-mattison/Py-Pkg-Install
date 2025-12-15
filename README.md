# Py-Pkg-Install v0.0.6
This is a homemade tool that is meant to make installing packages on MacOS and Linux easy. 

# To-Do List
- Add support for curl commands (other than homebrew)
- Further Linux support
- Bug check on each supported OS (currently known working on MacOS only)
- Fix possible package install errors (e.g. if a package is unavialable, skip it)

# Support
MacOS support - 70%
Linux support - 50%
Windows support - No plans to support
Other OSes (FreeBSD etc.) - No plans to support

# Commit History
Commit 1
- Laid down basic framework for MacOS installation

Commit 2
- Fixed some errors and bugs that could arise with running program on a non-darwin operating system

Commit 3
- Added `xcode-select --install` command to developer chest

Commit 4
- Cleaned code
- Refactored some functions
- Made two new files called `macos.py` and `linux.py` that execute on their respective operating systems

Commit 5
- Added full package lists for MacOS
- Fixed bugs for MacOS installer

Commit 6
- Added framework for the following Linux distros: Arch, Fedora, Debian
