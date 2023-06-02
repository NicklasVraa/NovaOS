import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import subprocess

class NovaOS_welcome(Gtk.Window):
    def __init__(self):
        super().__init__(title="Nova OS")

        # Window setup.
        self.set_default_size(300, 220)
        self.set_position(Gtk.WindowPosition.CENTER)

        # Pages setup.
        pages = Gtk.Notebook()

        # Welcome Page.
        welcome = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        welcome.set_border_width(10)
        pages.append_page(welcome, Gtk.Label(label="Welcome"))
        intro = Gtk.Label(label="This is a remake of Linux Mint. The intention with this ISO is to provide a very minimal and optimized version of Mint with sensible defaults and a coherent experience and muted look-and-feel.\n\nFeel free to make it your own.")
        intro.set_line_wrap(True)
        welcome.pack_start(intro, False, True, 0)
        welcome.pack_start(Gtk.Box(), True, True, 0) # Spacer
        buttons = Gtk.Box(spacing=6)
        buttons.set_homogeneous(True)
        repo_button = Gtk.Button(label="Code Repository")
        repo_button.connect("clicked", self.on_repo_button_clicked)
        buttons.pack_start(repo_button, True, True, 0)
        settings_button = Gtk.Button(label="Adjust Settings")
        settings_button.connect("clicked", self.on_settings_button_clicked)
        buttons.pack_start(settings_button, True, True, 0)
        welcome.pack_start(buttons, False, False, 0)

        # Software Page.
        software = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        software.set_border_width(10)
        pages.append_page(software, Gtk.Label(label="Software"))
        desc = Gtk.Label(label="Mark any recommended software, you want on your system, then press install. They will automatically be set up and themed. Internet is required.")
        desc.set_line_wrap(True)
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
        software.pack_start(install_button, False, False, 0)

        # Tips Page.
        tips_padding = Gtk.Box()
        tips_padding.set_border_width(10)
        tips_scroller = Gtk.ScrolledWindow()
        tips_padding.pack_start(tips_scroller, True, True, 0)
        tips = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        tips_scroller.add(tips)
        pages.append_page(tips_padding, Gtk.Label(label="Tips"))
        tip_text = Gtk.Label(label="1. The [super] key opens the main menu in the top-left corner. With the menu open, simply start typing to search for an app, then hit enter.\n\n2. Right-click the [☰] icon, then configure/menu/menu-edtior to add application launchers and for customization options.\n\n3. The [▪ ▪ ▪] buttons in the top-right corners of all windows are in order from left to right: minimize, maximize, close.\n\n4. If the top menu (file, edit, view, ...) of an application is not visible, press [alt] while its window is focused. To hide it, press [alt] again.\n\n5. Check or set your own keyboard shortcuts in settings/keyboard/shortcuts.\n\n6. In a terminal, right-click to split it into several terminals - vertically or horizontally.\n\n7. To easily remove old logs, caches and empty all trash folders, open a terminal and run 'clean'.")
        tip_text.set_line_wrap(True)
        tips.pack_start(tip_text, False, True, 0)
        tips.pack_start(Gtk.Box(), True, True, 0) # Spacer

        # Credits Page.
        credit = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        credit.set_border_width(10)
        pages.append_page(credit, Gtk.Label(label="Credit"))
        about = Gtk.Label(label="Check out GitHub.com/NicklasVraa.\nStars are appreciated.")
        about.set_line_wrap(True)
        credit.pack_start(about, True, True, 0)
        git_button = Gtk.Button(label="GitHub")
        git_button.connect("clicked", self.on_git_button_clicked)
        credit.pack_start(git_button, False, False, 0)

        self.add(pages)

    def on_repo_button_clicked(self, widget):
        subprocess.run(["xdg-open", "https://github.com/NicklasVraa/NovaOS"])

    def on_settings_button_clicked(self, widget):
        subprocess.run(["cinnamon-settings"])

    def on_git_button_clicked(self, widget):
        subprocess.run(["xdg-open", "https://github.com/NicklasVraa"])

win = NovaOS_welcome()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
