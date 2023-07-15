import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import os, subprocess

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="My App")

        # Window setup.
        self.set_default_size(100, 70)
        self.set_position(Gtk.WindowPosition.CENTER)

        # Setup a content container.
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box.set_border_width(12)
        self.add(box) # Add box to window.

        # Add a label.
        my_label = Gtk.Label(label="Hello World")
        box.pack_start(my_label, False, False, 0)

        # Add a button.
        my_button = Gtk.Button(label="Say Hello")
        my_button.connect("clicked", self.on_clicked)
        box.pack_start(my_button, False, False, 0)

    # Define an event.
    def on_clicked(self, widget):
        cmd = "echo Hello World &"
        os.system(cmd)

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
