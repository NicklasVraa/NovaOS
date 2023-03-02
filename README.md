# NovaOS
My personal respin of the [Linux Mint](https://linuxmint.com) operating system, where "bloat" has been removed and the UI cleaned up and given a new coat of paint using my [theme](https://github.com/NicklasVraa/Nova-galactic-theme) and [icon-pack](https://github.com/NicklasVraa/Nova-galactic-icons).

Thank you to [penguins-eggs](https://github.com/pieroproietti/penguins-eggs) for making the process of distributing ISO's easy.

|   |   |
|---|---|
| ![alt](meta/desktop.png) | ![alt](meta/applet.png) |
| ![alt](meta/files_settings.png) | ![alt](meta/os_apps.png) |
| ![alt](meta/code_term.png) | ![alt](meta/obsidian.png) |
| ![alt](meta/browser_inkscape.png) | ![alt](meta/lock.png) |

## Installation
1. Download the [ISO](https://drive.google.com/drive/folders/1djzd2mm6oHLx1MuvaAjNLqDi0mUxStYA?usp=share_link).
2. Create a bootable USB and select it during boot. \
   This process depends on your hardware or current OS.
3. In the live-session, start a terminal and run `sudo eggs install`. \
   Password: `nova`, which will also be the root password.
4. Run through the guided installation.

## Post-Install Suggestions
Launch a terminal and run:
- `sudo rm /etc/xdg/autostart/penguins-links-add.desktop` to remove the script that creates shortcuts on the desktop.
- `rm Desktop/*` to remove the shortcuts on the desktop.
- `sudo apt remove eggs` to remove penguins-eggs, if you don't plan on sharing your system.
- `clean` to clean up caches.
- `sudo apt update` to check for updates.
