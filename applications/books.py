import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import subprocess

class Book(Gtk.Box):
    def __init__(self, title):
        super().__init__()
        self.pack_start(Gtk.Label(label=title), False, False, 0)
    pass

class Shelf(Gtk.Window):
    def __init__(self):
        super().__init__(title="Books")

        # Window setup.
        self.set_default_size(500, 500)
        self.set_position(Gtk.WindowPosition.CENTER)

        # Tips Page.
        padding = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        padding.set_border_width(10)
        self.add(padding)

        search = Gtk.SearchEntry()
        padding.pack_start(search, False, False, 0)

        scroller = Gtk.ScrolledWindow()
        padding.pack_start(scroller, True, True, 0)
        content = Gtk.FlowBox()
        scroller.add(content)

        content.add(Book("Book1"))

win = Shelf()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
