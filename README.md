# NovaOS
**Attention**: Had to remove ISO, because I need the space in Google Drive for Colab. Will update and reupload in the future.

**Attention**: ISO fixed. If you cannot login, username:`user` and password:`nova` works.

My personal respin of the [Linux Mint](https://linuxmint.com) operating system, where "bloat" has been removed and the UI cleaned up and given a new coat of paint using my [theme](https://github.com/NicklasVraa/Nova-galactic-theme) and [icon-pack](https://github.com/NicklasVraa/Nova-galactic-icons).
It's based on Mint 20.3, but with the 5.15 kernel.

Thank you to [penguins-eggs](https://github.com/pieroproietti/penguins-eggs) for making the process of distributing ISO's easy.

|                                   |                           |
|-----------------------------------|---------------------------|
| ![alt](meta/desktop.png)          | ![alt](meta/applet.png)   |
| ![alt](meta/files_settings.png)   | ![alt](meta/os_apps.png)  |
| ![alt](meta/code_term.png)        | ![alt](meta/obsidian.png) |
| ![alt](meta/browser_inkscape.png) | ![alt](meta/lock.png)     |

## Installation
![showcase](meta/showcase.JPG)
1. Download the [ISO](https://drive.google.com/drive/folders/1djzd2mm6oHLx1MuvaAjNLqDi0mUxStYA?usp=share_link).
2. Create a bootable USB (e.g. using [Rufus](https://rufus.ie/en/)) and select the drive during boot. \
   The process of selecting a different boot-device depends on your hardware.
3. In the live-session, start a terminal and run `sudo eggs install`. Password: `nova`.
4. Run through the guided installation.

## Post-Install Suggestions
- Use the built-in updater or the terminal to update the system, which will also prompt you to remove packages, that are no longer needed.

---
**LEGAL NOTICE**: This repository, including any and all of its forks and derivatives, may NOT be used in the development or training of any machine learning model of any kind, without the explicit permission of the owner of the original repository.
