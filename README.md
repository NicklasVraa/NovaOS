# NovaOS
Download the [ISO](https://drive.google.com/drive/folders/1PxN_xtd-8F6M6SU2Ia1yOs4M1Mpy6arj?usp=sharing) (31-5-2023 build). Confirmed to work in VirtualBox and on bare metal. If Windows won't let you boot into Linux after installation, install and run `boot-repair` from within the live session.

This is a remake of [Linux Mint](https://linuxmint.com). The intention with this ISO is to provide a very minimal and optimized version of Mint with sensible defaults and a coherent experience and muted look-and-feel. It's based on Mint 20.3, but with the newer 5.15 kernel. Also check out the standalone [theme](https://github.com/NicklasVraa/Nova-galactic-theme) and [icon-pack](https://github.com/NicklasVraa/Nova-galactic-icons).

Thank you to [penguins-eggs](https://github.com/pieroproietti/penguins-eggs) for making the process of building ISO's a little bit easier.

|                                   |                           |
|-----------------------------------|---------------------------|
| ![alt](meta/desktop.png)          | ![alt](meta/applet.png)   |
| ![alt](meta/files_settings.png)   | ![alt](meta/os_apps.png)  |
| ![alt](meta/code_term.png)        | ![alt](meta/obsidian.png) |
| ![alt](meta/browser_inkscape.png) | ![alt](meta/lock.png)     |

## Installation
![showcase](meta/showcase.JPG)
1. Download the [ISO](https://drive.google.com/drive/folders/1PxN_xtd-8F6M6SU2Ia1yOs4M1Mpy6arj?usp=sharing).
2. Create a bootable USB (e.g. using [Rufus](https://rufus.ie/en/)) and select the drive during boot. \
   The process of selecting a different boot-device depends on your hardware.
3. In the live-session, either use the graphical installer, or start a terminal and run `sudo eggs install`. Password: `nova`.
4. Run through the guided installation.

## Post-Install Suggestions
- Use the built-in update-manager or the terminal to update the system, which will also prompt you to remove packages, that are no longer needed. If the update-manager claims that apt is broken, simply refresh.
- Add additional [wallpapers](https://drive.google.com/drive/folders/1PxN_xtd-8F6M6SU2Ia1yOs4M1Mpy6arj?usp=sharing).

## Roadmap
- [ ] Post-install TUI for downloading and configuring recommended optional apps and explaining the UI.
- [ ] Global theme- and icon color changer, by editing svg- and css color code.
- [ ] Additional wallpapers.
- [ ] Color-matched Calamares installer.

---
**LEGAL NOTICE**: This repository, including any and all of its forks and derivatives, may NOT be used in the development or training of any machine learning model of any kind, without the explicit permission of the owner of the original repository.
