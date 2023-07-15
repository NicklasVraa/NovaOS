import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import os, subprocess

class NovaOS_welcome(Gtk.Window):
    def __init__(self):
        super().__init__(title="Nova OS - Welcome")

        # Window setup.
        self.set_default_size(300, 220)
        self.set_position(Gtk.WindowPosition.CENTER)

        # Pages setup.
        pages = Gtk.Notebook()

        # Welcome Page.
        welcome = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        welcome.set_border_width(12)
        pages.append_page(welcome, Gtk.Label(label="Welcome"))
        intro = Gtk.Label(label="This is a remake of Linux Mint. The intention with this ISO is to provide a very minimal and optimized version of Mint with sensible defaults and a coherent experience and muted look-and-feel. Nothing more, nothing less.\n\nFeel free to make it your own.")
        intro.set_line_wrap(True)
        intro.set_alignment(0,0)
        welcome.pack_start(intro, False, True, 0)
        welcome.pack_start(Gtk.Box(), True, True, 0) # Spacer
        buttons = Gtk.Box(spacing=6)
        buttons.set_homogeneous(True)
        repo_button = Gtk.Button(label="Repository")
        repo_button.connect("clicked", self.on_repo_button_clicked)
        buttons.pack_start(repo_button, True, True, 0)
        settings_button = Gtk.Button(label="Settings")
        settings_button.connect("clicked", self.on_settings_button_clicked)
        buttons.pack_start(settings_button, True, True, 0)
        system_button = Gtk.Button(label="System")
        system_button.connect("clicked", self.on_system_button_clicked)
        buttons.pack_start(system_button, True, True, 0)
        welcome.pack_start(buttons, False, False, 0)

        # Setup Page.
        setup = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        setup.set_border_width(12)
        pages.append_page(setup, Gtk.Label(label="Setup"))
        desc = Gtk.Label(label="If your screen shows the OS logo for more than a couple of seconds after startup, press this.")
        desc.set_line_wrap(True)
        desc.set_alignment(0,0)
        setup.pack_start(desc, False, True, 0)
        bootfix_button = Gtk.Button(label="Fix slow boot")
        bootfix_button.connect("clicked", self.on_bootfix_button_clicked)
        setup.pack_start(bootfix_button, False, False, 0)
        desc = Gtk.Label(label="Perform a full update of your system using the update-manager. Access from the main menu [☰].")
        desc.set_line_wrap(True)
        desc.set_alignment(0,0)
        setup.pack_start(desc, False, True, 0)
        update_button = Gtk.Button(label="Update system")
        update_button.connect("clicked", self.on_update_button_clicked)
        setup.pack_start(update_button, False, False, 0)

        # Software Page.
        software = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        software.set_border_width(12)
        pages.append_page(software, Gtk.Label(label="Software"))
        desc = Gtk.Label(label="Mark any recommended software, you want on your system, then press install. They will automatically be set up and themed. Internet is required.")
        desc.set_line_wrap(True)
        desc.set_alignment(0,0)
        software.pack_start(desc, False, True, 0)
        checks = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        checks.set_border_width(5)
        buttons.set_homogeneous(True)
        obsidian = Gtk.CheckButton(label="Obsidian (Notes)")
        checks.pack_start(obsidian, True, True, 0)
        vscode = Gtk.CheckButton(label="VS Code (Text Editing)")
        checks.pack_start(vscode, True, True, 0)
        inkscape = Gtk.CheckButton(label="Inkscape (Illustration)")
        checks.pack_start(inkscape, True, True, 0)
        gimp = Gtk.CheckButton(label="GIMP (Photo Editing)")
        checks.pack_start(gimp, True, True, 0)
        software.pack_start(checks, False, False, 0)
        software.pack_start(Gtk.Box(), True, True, 0) # Spacer
        install_button = Gtk.Button(label="Install")
        install_button.connect("clicked", self.on_install_button_clicked)
        software.pack_start(install_button, False, False, 0)

        # Tips Page.
        tips_padding = Gtk.Box()
        tips_padding.set_border_width(12)
        tips_scroller = Gtk.ScrolledWindow()
        tips_padding.pack_start(tips_scroller, True, True, 0)
        tips = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        tips_scroller.add(tips)
        pages.append_page(tips_padding, Gtk.Label(label="Tips"))
        tip_text = Gtk.Label(label="For Linux beginners:\n\n1. The [super/win/⌘] key opens the main menu [☰] in the top-left corner. With the menu open, simply start typing to search for an app, or navigate with the arrow keys, then hit enter.\n\n2. Right-click the [☰] icon, then configure/menu/menu-edtior to add application launchers and for customization options.\n\n3. The [▪▪▪] buttons in the top-right corners of all windows are in order from left to right: minimize, maximize, close.\n\n4. When searching for software online, look for '.deb' packages or alternatively 'appimages'. 'flatpaks' are also okay.\n\n5. If the top menu (file, edit, view, ...) of an application is not visible, press [alt] while its window is focused. To hide it, press [alt] again.\n\n6. Right-click the top bar to move or customize it. Install applets for more functionality.\n\n7. For a quick summary of your system, open a terminal and type 'fetch', then hit enter.\n\nFor intermediates:\n\n8. Check or set your own keyboard shortcuts in settings/keyboard/shortcuts.\n\n9. In a terminal, right-click to split it into several terminals - vertically or horizontally.\n\n10. To easily remove old logs, caches and empty all trash folders, open a terminal and run 'clean'.\n\n11. Type 'kernels' in a terminal to check what kernel components are currently installed.\n\n12. The default color scheme for the desktop and all installed apps is called 'Nord', if you wish to theme non-gtk-based apps.")
        tip_text.set_line_wrap(True)
        tip_text.set_alignment(0,0)
        tips.pack_start(tip_text, False, True, 0)
        tips.pack_start(Gtk.Box(), True, True, 0) # Spacer

        # Credits Page.
        credit = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        credit.set_border_width(12)
        pages.append_page(credit, Gtk.Label(label="Credit"))
        about = Gtk.Label(label="Check out GitHub.com/NicklasVraa.\nStars are appreciated.\n\nLinux branch:\nDebian → Ubuntu → Mint (cinnamon) → Nova")
        about.set_line_wrap(True)
        credit.pack_start(about, True, True, 0)
        git_button = Gtk.Button(label="GitHub")
        git_button.connect("clicked", self.on_git_button_clicked)
        credit.pack_start(git_button, False, False, 0)

        self.add(pages)

    # Welcome page buttons.
    def on_repo_button_clicked(self, widget):
        subprocess.run(["xdg-open", "https://github.com/NicklasVraa/NovaOS"])

    def on_settings_button_clicked(self, widget):
        subprocess.run(["cinnamon-settings"])

    def on_system_button_clicked(self, widget):
        os.system("terminator -e 'neofetch; exec bash' --geometry=600x340")

    # Setup page buttons.
    def on_bootfix_button_clicked(self, widget):
        os.system("terminator -e 'sudo rm /etc/initramfs-tools/conf.d/resume && echo This may take a moment... && sudo update-initramfs -u; echo Success! You may close this window.; exec bash'")

    def on_update_button_clicked(self, widget):
        subprocess.run(["mintupdate"])

    # Software page buttons.
    def on_install_button_clicked(self, widget):
        pass

    # Credit page buttons.
    def on_git_button_clicked(self, widget):
        subprocess.run(["xdg-open", "https://github.com/NicklasVraa"])

win = NovaOS_welcome()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
