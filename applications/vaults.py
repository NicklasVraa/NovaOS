# Desc: Minimal Obsidian vault chooser that follows system theme.
# Auth: Nicklas Vraa

vaults = ["Academia", "Personal"] # Add new vaults here.

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import os

class vault_chooser(Gtk.Window):
    def __init__(self):
        super().__init__(title="Obsidian Vaults")

        # Window setup.
        self.set_default_size(160, 80)
        self.set_position(Gtk.WindowPosition.CENTER)

        # Setup Page.
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box.set_border_width(12)

        for vault in vaults:
            button = Gtk.Button(label=vault)
            button.connect("clicked", self.open_vault, vault)
            box.pack_start(button, False, False, 0)

        self.add(box)

    def open_vault(self, button, vault):
        cmd = "obsidian 'obsidian://open?vault=" + vault + "' &"
        os.system(cmd)
        Gtk.main_quit()

win = vault_chooser()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
