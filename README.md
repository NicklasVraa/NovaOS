# NovaOS <img src="meta/logo.svg" width="28"/>
Download the ISO (2023-11-26 build): [SourceForge](https://sourceforge.net/projects/novaos/files/) (recommended)| [Google Drive](https://drive.google.com/drive/folders/1f0jR0VEez13FHDwOYfysAfKcvFQYKSCm?usp=sharing) (backup)

sha256sum: `f89413450f0119c25b9d97b43bb3b191a871f5f324c4c11eaa8bd674dbc6d09e`


This is a remake of [Linux Mint](https://linuxmint.com). The intention with this ISO is to provide a very minimal and optimized version of Mint with sensible defaults and a coherent experience and muted look-and-feel. It's based on Mint 20.3, but with the newer 5.15 kernel. It will receive the same updates as normal Linux Mint. Also check out the standalone [theme](https://github.com/NicklasVraa/Nova-galactic-theme) and [icon-pack](https://github.com/NicklasVraa/Nova-galactic-icons), which were created using [Color_Manager](https://github.com/NicklasVraa/Color-manager). Additional [wallpapers](https://drive.google.com/drive/folders/1HjrJrt7eDFPl18DLkWYUCWC0cEZfyRGJ?usp=sharing) are available.

|                                   |                           |
|-----------------------------------|---------------------------|
| ![alt](meta/desktop.png)          | ![alt](meta/applet.png)   |
| ![alt](meta/files_settings.png)   | ![alt](meta/os_apps.png)  |
| ![alt](meta/code_term.png)        | ![alt](meta/obsidian.png) |
| ![alt](meta/drawio.png)           | ![alt](meta/nano.png)     |
| ![alt](meta/browser_inkscape.png) | ![alt](meta/lock.png)     |

Pre-installed software is kept to a minimum and has been appropriately themed and configured.
- Installed: Firefox, VSCode, Terminator, Obsidian, Drawio, LibreOffice7.5
- Recommended: TeXLive, Inkscape, GIMP, VirtualBox

If wanted, I can provide a version without any added pre-installed software.

## Installation
1. Download the [ISO](https://drive.google.com/drive/folders/1f0jR0VEez13FHDwOYfysAfKcvFQYKSCm?usp=sharing).
2. Create a bootable USB (e.g. using [Rufus](https://rufus.ie/en/)) and select the drive during boot. \
   The process of selecting a different boot-device depends on your hardware. You may need to disable secure-boot.
3. In the live-session, double-click the install icon on the desktop. An internet connection allows for automatic localization, but is not required.

## Post-Install
- If startup is slow, run `sudo rm /etc/initramfs-tools/conf.d/resume && sudo update-initramfs -u` in a terminal. This may take a second to complete.
- If Windows won't let you boot into Linux after installation, install and run `boot-repair` from within a terminal in the live session.
- Look for missing drivers using the driver-manager, and update the system using the update-manager. Start by refreshing.

## Roadmap
- [x] Finish Welcome GUI.
- [x] Finish [Color_Manager](https://github.com/NicklasVraa/Color-manager).
- [x] Add additional wallpapers to repository.
- [x] Host ISO on SourceForge.
- [x] Generate SHA256SUM for checking integrity of ISO.
- [ ] Integrate Welcome GUI into ISO.
- [ ] Integrate Color_Manager into ISO.
- [ ] Color-matched Calamares installer.

![showcase](meta/showcase.JPG)

---
**LEGAL NOTICE**: This repository, including any and all of its forks and derivatives, may NOT be used in the development or training of any machine learning model of any kind, without the explicit permission of the owner of the original repository.
