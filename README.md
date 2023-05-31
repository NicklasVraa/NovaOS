# NovaOS
**Attention**: Reuploaded an updated [ISO](https://drive.google.com/drive/folders/1PxN_xtd-8F6M6SU2Ia1yOs4M1Mpy6arj?usp=sharing), but have not had a chance to test it. If prompted for username or password, type `nova`. If the icons did not install correctly, download the [icon-pack](https://github.com/NicklasVraa/Nova-galactic-icons) and add it to `~/.icons/`, then select in settings/theme. When I have time, I will add a welcome app.

This is a remake of [Linux Mint](https://linuxmint.com). The intention with this ISO is to provide a very minimal and optimized version of Mint with sensible defaults and a coherent experience and muted look-and-feel. Also check out the standalone [theme](https://github.com/NicklasVraa/Nova-galactic-theme) and [icon-pack](https://github.com/NicklasVraa/Nova-galactic-icons).

It's based on Mint 20.3, but with the newer 5.15 kernel.

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
- Use the built-in updater or the terminal to update the system, which will also prompt you to remove packages, that are no longer needed.

- Add additional [wallpapers](https://drive.google.com/drive/folders/1PxN_xtd-8F6M6SU2Ia1yOs4M1Mpy6arj?usp=sharing).

---
**LEGAL NOTICE**: This repository, including any and all of its forks and derivatives, may NOT be used in the development or training of any machine learning model of any kind, without the explicit permission of the owner of the original repository.
