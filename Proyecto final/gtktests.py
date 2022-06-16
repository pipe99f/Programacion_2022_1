import sys
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw

import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

def on_activate(app):
    win = Gtk.ApplicationWindow(application=app)
    win.present()

app = Gtk.Application()
app.connect('activate', on_activate)

app.run(None)
#  class MainWindow(Gtk.ApplicationWindow):
#      def __init__(self, *args, **kwargs):
#          super().__init__(*args, **kwargs)
#          self.box1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
#          self.set_child(self.box1)
#
#          self.button = Gtk.Button(label="Hello")
#          self.box1.append(self.button)
#          self.button.connect('clicked', self.hello)
#          self.set_default_size(600, 250)
#          self.set_title("MyApp")
#          self.box1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
#          self.box2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
#          self.box3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
#
#          self.button = Gtk.Button(label="Hello")
#          self.button.connect('clicked', self.hello)
#
#          self.set_child(self.box1)  # Horizontal box to window
#          self.box1.append(self.box2)  # Put vert box in that box
#          self.box1.append(self.box3)  # And another one, empty for now
#
#          self.box2.append(self.button) # Put button in the first of the two vertial boxes
#          self.check = Gtk.CheckButton(label="And goodbye?")
#          self.box2.append(self.check)
#
#      def hello(self, button):
#          print("Hello world")
#          if self.check.get_active():
#              print("Goodbye world!")
#              self.close()
#
#  class MyApp(Adw.Application):
#      def __init__(self, **kwargs):
#          super().__init__(**kwargs)
#          self.connect('activate', self.on_activate)
#
#      def on_activate(self, app):
#          self.win = MainWindow(application=app)
#          self.win.present()
#
#  app = MyApp(application_id="com.example.GtkApplication")
#  app.run(sys.argv)

#segmento genérico del website de gtk

#  def on_activate(app):
#      # … create a new window…
#      win = Gtk.ApplicationWindow(application=app)
#      # … with a button in it…
#      btn = Gtk.Button(label='Hello, World!')
#      # … which closes the window when clicked
#      btn.connect('clicked', lambda x: win.close())
#      win.set_child(btn)
#      win.present()
#
#  # Create a new application
#  app = Gtk.Application(application_id='com.example.GtkApplication')
#  app.connect('activate', on_activate)
#
#  # Run the application
#  app.run(None)

