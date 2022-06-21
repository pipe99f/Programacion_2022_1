import bashdata
import gi
import subprocess
import time
import os
import sys

#Default values
fPath = os.environ['HOME'] + "/Videos" #Carpeta ~/Videos
selectArea = ""
output = bashdata.screens[0]
audio = bashdata.defaultOutput
fName = bashdata.getDate()
delayTime = 0
audioDict={"Default input": bashdata.defaultInput, "Default output": bashdata.defaultOutput} #Diccionario para que en el app algunos valores de aparezcan bajo el alias "Default input" o "Default output"
for i in bashdata.sources:
    audioDict[i] = i

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class mainWindow(Gtk.Window):
    def __init__(self):
        global fileName, delayButton, audioCombo, outputsCombo

        super().__init__(title="Sway recorder")
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_border_width(8)
        self.set_default_size(300, 180)
        self.set_resizable(False)

        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title = "Sway recorder"
        self.set_titlebar(hb)


        boxAudio = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        audioLabel = Gtk.Label()
        audioLabel.set_markup("<big>Audio Source</big>")
        audioCombo=Gtk.ListStore(int,str)
        audioCombo.append([1, "Default output"])
        audioCombo.append([2, "Default input"])
        for i in range(3, len(bashdata.sources)+3):
            audioCombo.append([1, bashdata.sources[i-3]])
        audioCombo=Gtk.ComboBox.new_with_model_and_entry(audioCombo)
        audioCombo.set_entry_text_column(1)
        audioCombo.set_active(0)  # Valor predeterminado en el ComboBox
        boxAudio.pack_start(audioLabel, True, True, 0)
        boxAudio.pack_start(audioCombo, True, True, 0)


        boxOutput = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        outputLabel = Gtk.Label()
        outputLabel.set_markup("<big>Screen</big>")
        outputs=Gtk.ListStore(int,str)

        for i in range(1, len(bashdata.screens)+1):
            outputs.append([i,bashdata.screens[i-1]])

        outputsCombo=Gtk.ComboBox.new_with_model_and_entry(outputs)
        outputsCombo.set_entry_text_column(1)
        outputsCombo.set_active(0)
        boxOutput.pack_start(outputLabel, True, True, 0)
        boxOutput.pack_start(outputsCombo, True, True, 0)


        boxFile = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        fileLabel = Gtk.Label()
        fileLabel.set_markup("<big>File name</big>")
        fileName = Gtk.Entry()
        fileName.set_text(fName)
        boxFile.pack_start(fileLabel, True, True, 0)
        boxFile.pack_start(fileName, True, True, 0)


        boxPathChooser = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        pathLabel = Gtk.Label()
        pathLabel.set_markup("<big>Destination folder</big>")
        chooser = Gtk.Button(label=fPath)
        chooser.connect("clicked", self.selectPath)
        boxPathChooser.pack_start(pathLabel, True, True, 0)
        boxPathChooser.pack_start(chooser, True, True, 0)


        boxSelectArea = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        areaLabel = Gtk.Label()
        selectAreaButton = Gtk.Button(label="Select area")
        selectAreaButton.connect("clicked", self.selectAreaValue)
        boxSelectArea.pack_start(areaLabel, True, True, 0)
        boxSelectArea.pack_start(selectAreaButton, False, False, 0)


        boxDelayTime = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        delayLabel = Gtk.Label()
        delayLabel.set_markup("<big>Delay time</big>")
        delayIncrease = Gtk.Adjustment(upper=60, step_increment=1, page_increment=10)
        delayButton = Gtk.SpinButton()
        delayButton.set_adjustment(delayIncrease)
        boxDelayTime.pack_start(delayLabel, False, False, 0)
        boxDelayTime.pack_start(delayButton, False, False, 0)


        emptyLabel1 = Gtk.Label()
        emptyLabel2 = Gtk.Label()


        recordButton = Gtk.ToggleButton(label="Start recording")
        recordButton.connect("toggled", self.startRecording)


        grid = Gtk.Grid(column_spacing = 10, row_spacing = 10)
        grid.insert_column(1)
        grid.attach(boxAudio, 0, 0, 1, 1)
        # grid.attach(audioCombo, 0, 1, 1, 1)
        # grid.attach(asd, 3, 1, 1, 1)
        grid.attach(boxOutput, 1, 0, 1, 1)
        grid.attach(boxFile, 2, 0, 1, 1)
        grid.attach(boxPathChooser, 0, 1, 1, 1)
        grid.attach(boxDelayTime, 1, 1, 1, 1)
        grid.attach(boxSelectArea, 2, 1, 1, 1)
        grid.attach(emptyLabel1, 0, 2, 1, 1)
        grid.attach(emptyLabel2, 0, 3, 1, 1)
        grid.attach(boxSelectArea, 2, 1, 1, 1)
        grid.attach(recordButton, 1, 2, 1, 3)
        self.add(grid)




    def selectPath(self, widget):
        global fPath

        dialog = Gtk.FileChooserDialog(
            title="Choose destination folder",
            parent=self, #se usa para que también sea una ventana flotante
            action=Gtk.FileChooserAction.SELECT_FOLDER,
        )
        dialog.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, "Select", Gtk.ResponseType.OK
        )
        dialog.set_default_size(300, 300)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            fPath = dialog.get_filename()
            widget.set_label(fPath)
            print(widget.get_label())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()


    def selectAreaValue(self, button):
        global selectArea
        selectArea = subprocess.check_output('slurp').decode()[:-1]
        print(selectArea)

    def startRecording(self, widget):
        global wfProcess
        
        if widget.get_active():
            fName = fileName.get_text()
            delayTime = delayButton.get_text()
            audio = audioCombo.get_child()  # Se crea un nuevo instance para usar el método "get_text" que permite obtener el valor de los comboBoxes
            output = outputsCombo.get_child()

            time.sleep(int(delayTime))
            print("Recording has started")

            wf_recorder = ["wf-recorder", f"--audio={audioDict[audio.get_text()]}", f"-f {fName}.mp4", f"--output={output.get_text()}", "--bframes=4", "-g", f'"{selectArea}"']
            print(' '.join(wf_recorder))

            widget.set_label("Stop recording")
            # print(wf_recorder[-1])
            wfProcess = subprocess.Popen(wf_recorder, cwd=fPath)
        else:
            # wfProcess.kill()
            os.system("killall -s SIGINT wf-recorder")
            widget.set_label("Start recording")




win = mainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
