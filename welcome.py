import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Nova OS - Welcome")

        # Window setup.
        self.set_default_size(300, 200)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_border_width(10)

        # Container setup.
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)

        # Main header.
        welcome = Gtk.Label()
        welcome.set_markup("<b>Welcome to Nova OS</b>")
        box.pack_start(welcome, True, True, 0)

        # Introduction text.
        intro = Gtk.Label(label="This is a remake of Linux Mint. The intention with this ISO is to provide a very minimal and optimized version of Mint with sensible defaults and a coherent experience and muted look-and-feel.")
        intro.set_line_wrap(True)
        box.pack_start(intro, True, True, 0)

        # Bottom row of buttons.
        buttons = Gtk.Box(spacing=5)
        buttons.set_homogeneous(True)
        repo_button = Gtk.Button(label="Repository")
        buttons.pack_start(repo_button, True, True, 0)
        install_button = Gtk.Button(label="Install")
        buttons.pack_start(install_button, True, True, 0)
        settings_button = Gtk.Button(label="Settings")
        buttons.pack_start(settings_button, True, True, 0)
        box.pack_start(buttons, True, True, 0)

        self.add(box)

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
