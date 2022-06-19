import gi
import sys

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class mainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Sway recorder")
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_border_width(8)
        self.set_default_size(600, 250)
        self.set_resizable(False)


        # self.box1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        # # self.add(self.box1)       
        #
        # self.box2 = Gtk.Box(spacing=6)
        # self.add(self.box2)       
        # self.box2.pack_start(self.box1, True, True, 0)

        audioLabel = Gtk.Label(label="Audio Source")
        audioLabel.set_hexpand(True)
        audioCombo=Gtk.ListStore(int,str)
        audioCombo.append([1,"alsa_output.pci-0000_0b_00.4.analog-stereo"])
        audioCombo.append([2, "proof"])
        audioCombo=Gtk.ComboBox.new_with_model_and_entry(audioCombo)
        audioCombo.set_entry_text_column(1)
        # self.box1.pack_start(audioCombo, True, True, 0)


        outputLabel = Gtk.Label(label="output")
        ouputs=Gtk.ListStore(int,str)
        ouputs.append([1,"uuh"])
        outputsCombo=Gtk.ComboBox.new_with_model_and_entry(ouputs)
        outputsCombo.set_entry_text_column(1)
        # self.box1.pack_start(outputsCombo, True, True, 0)

        recordButton = Gtk.Button(label="Start recording")
        recordButton.connect("clicked", self.on_button_clicked)
        # recordButton.set_hexpand(True) #Esta función hace que se centre el botón record.
        # self.box2.pack_start(self.button, True, True, 0)

        asd = Gtk.Button(label="HOLA!")
        asd.connect("clicked", self.on_button_clicked)

        grid = Gtk.Grid(column_spacing = 10, row_spacing = 10, column_homogeneous = True)
        grid.insert_column(1)
        grid.attach(audioLabel, 0, 0, 1, 1)
        grid.attach(audioCombo, 0, 1, 1, 1)
        # grid.attach_next_to(outputLabel, outputsCombo, Gtk.PositionType.TOP, 1, 1)
        grid.attach(asd, 3, 1, 1, 1)
        grid.attach(outputsCombo, 1, 1, 1, 1)
        grid.attach(recordButton, 2, 58, 1, 1)



        self.add(grid)


    def on_button_clicked(self, button):
        print("Recording has started")



win = mainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
