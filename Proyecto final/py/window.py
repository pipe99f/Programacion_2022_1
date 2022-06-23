import bashdata
import gi
import subprocess
import time
import os

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

#Default values
fPath = os.environ['HOME'] + "/Videos" #Carpeta ~/Videos
selectArea = ""
output = bashdata.screens[0]
audio = bashdata.defaultOutput
fName = bashdata.getDate()
delayTime = 0
audioDict={"Default input": bashdata.defaultInput, "Default output": bashdata.defaultOutput} #Diccionario para que en el app algunos valores de aparezcan bajo el alias "Default input" o "Default output"
for i in bashdata.sources:  # agrega al diccionario outputs que no son defaults
    audioDict[i] = i


class mainWindow(Gtk.Window):
    def __init__(self):
        global fileName, delayButton, audioCombo, outputsCombo

        super().__init__(title="Sway recorder")
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_border_width(8)  # espacio entre el borde de la ventana y los widgets
        self.set_default_size(300, 180) #tamaño de la ventana
        self.set_resizable(False) #Se obliga a la ventana a tener siempre el mismo tamaño, esto hace que siempre sea flotante

        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title = "Sway recorder" #agrega título a la barra arriba de la ventana #asigna variables el resultado de la función
        self.set_titlebar(hb)


        boxAudio = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2) #caja que ordena elementos de arriba hacia abajo
        audioLabel = Gtk.Label() #se crea un label ("widget que solo muestra un texto en la aplicación") vacío
        audioLabel.set_markup("<big>Audio Source</big>") #se le agrega texto de tamaño grande al label
        audioCombo=Gtk.ListStore(int,str) #crea lista de opciones del combobox. int = identificador.
        audioCombo.append([1, "Default output"]) #posición 1, valor "default output"
        audioCombo.append([2, "Default input"])
        for i in range(3, len(bashdata.sources)+3): #agrega el resto de fuentes de audio
            audioCombo.append([i, bashdata.sources[i-3]])
        audioCombo=Gtk.ComboBox.new_with_model_and_entry(audioCombo) #crea combobox y añade la lista anterior
        audioCombo.set_entry_text_column(1)
        audioCombo.set_active(0)  # Valor predeterminado en el ComboBox
        boxAudio.pack_start(audioLabel, True, True, 0) #añade el label a la caja
        boxAudio.pack_start(audioCombo, True, True, 0) #1er True para expandir, 2do True para rellenar y el 0 hace referencia al padding

        #ocurre prácticamente lo mismo que con el combobox del audio
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


        boxFile = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2) #caja que ordena los elementos de arriba hacia abajo 
        fileLabel = Gtk.Label()
        fileLabel.set_markup("<big>File name</big>")
        fileName = Gtk.Entry() # casilla que recibe el input del usuario, en este caso, el nombre con el que se quiere que se guarde el video
        fileName.set_text(fName) #asigna fName como valor predeterminado de la casilla
        boxFile.pack_start(fileLabel, True, True, 0) # se agrega el label a la caja
        boxFile.pack_start(fileName, True, True, 0)  # se agrega la casilla de entrada de texto a la caja


        boxPathChooser = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2) #caja que va de arriba hacia abajo
        pathLabel = Gtk.Label()
        pathLabel.set_markup("<big>Destination folder</big>")
        chooser = Gtk.Button(label=fPath) #crea botón con el path default
        chooser.connect("clicked", self.selectPath) #si se da click al botón, se activa la función selectPath()
        boxPathChooser.pack_start(pathLabel, True, True, 0)
        boxPathChooser.pack_start(chooser, True, True, 0)


        boxSelectArea = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        areaLabel = Gtk.Label()
        selectAreaButton = Gtk.Button(label="Select area") #botón que permite ajustar el área de la pantalla que se quiere grabar
        selectAreaButton.connect("clicked", self.selectAreaValue)  # si se da click al botón, se activa la función selectAreaVaule()
        boxSelectArea.pack_start(areaLabel, True, True, 0)
        boxSelectArea.pack_start(selectAreaButton, False, False, 0)


        boxDelayTime = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        delayLabel = Gtk.Label()
        delayLabel.set_markup("<big>Delay time</big>")
        delayButton = Gtk.SpinButton() #crea casilla de entrada de texto con botones para aumentar o disminuir el valor del texto
        delayIncrease = Gtk.Adjustment(upper=60, step_increment=1) # determina la razón de cambio dichos botones 
        delayButton.set_adjustment(delayIncrease) #enlaza el objeto Gtk.Adjustment a los botones
        boxDelayTime.pack_start(delayLabel, False, False, 0)
        boxDelayTime.pack_start(delayButton, False, False, 0)


        emptyLabel1 = Gtk.Label() #se crean labels sin texto para dejar un espacio invisible que añade "grosor" a las dos últimas filas. De este modo, el siguiente widget, que es un botón y ajusta su tamaño dinámicamente, sería tan grueso como las dos filas correspondientes a los empty labels que se acabaron de crear
        emptyLabel2 = Gtk.Label()


        recordButton = Gtk.ToggleButton(label="Start recording") #botón que inicia o detiene la grabación
        recordButton.connect("toggled", self.startRecording)


        grid = Gtk.Grid(column_spacing = 10, row_spacing = 10) #se crea una cuadrícula invisible que permite organizar los widgets anteriormente creados
        #.....................0, 0, 1, 1) los argumentos indican, en el siguiente orden: columna, fila, ancho, largo 
        grid.attach(boxAudio, 0, 0, 1, 1) # se añade boxAudio a la primera casilla de la cuadrícula
        grid.attach(boxOutput, 1, 0, 1, 1)
        grid.attach(boxFile, 2, 0, 1, 1)
        grid.attach(boxPathChooser, 0, 1, 1, 1)
        grid.attach(boxDelayTime, 1, 1, 1, 1)
        grid.attach(boxSelectArea, 2, 1, 1, 1)
        grid.attach(emptyLabel1, 0, 2, 1, 1)
        grid.attach(emptyLabel2, 0, 3, 1, 1)
        grid.attach(boxSelectArea, 2, 1, 1, 1)
        grid.attach(recordButton, 1, 2, 1, 3)
        self.add(grid) #la cuadrícula ya con todos los widgets es añadida a la ventana principal




    def selectPath(self, widget):
        global fPath

        dialog = Gtk.FileChooserDialog( #se crea una ventana que permite escoger la carpeta donde se quiere guardar el video
            title="Choose destination folder",
            parent=self, #se usa para que también sea una ventana flotante
            action=Gtk.FileChooserAction.SELECT_FOLDER,
        )
        dialog.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, "Select", Gtk.ResponseType.OK #Añade botones a la ventana del buscador de archivos
        )
        dialog.set_default_size(300, 300)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            fPath = dialog.get_filename()
            widget.set_label(fPath)  # si selecciono una carpeta, el nombre y su "path" van a aparecer en el botón "Destination Folder"
            print(widget.get_label())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()


    def selectAreaValue(self, button):
        global selectArea #es global para que después startRecording() tome el valor del área seleccionada
        selectArea = subprocess.check_output('slurp').decode()[:-1] #se ejecuta slurp, un programa que permite seleccionar un área de la pantalla y que retorna las coordenadas del área seleccionada
        print(selectArea)

    def startRecording(self, widget):
        
        if widget.get_active(): #si el botón se activa, inicia la grabación
            fName = fileName.get_text() #se asigna el valor de texto de la casilla de entrada "fileName" a la variable fName
            delayTime = delayButton.get_text() 
            audio = audioCombo.get_child()  # Se crea un nuevo instance para usar el método "get_text" que permite obtener el valor de los comboBoxes, de lo contrario "audio Combo" al ser un objeto de la clase Gtk.ComboBox no puede utilizar este método
            output = outputsCombo.get_child()

            time.sleep(int(delayTime)) #retrasa la grabación en la cantidad de segundos determinada por la variable delayTime
            print("Recording has started")

            wf_recorder = ["wf-recorder", f"--audio={audioDict[audio.get_text()]}", f"-f {fName}.mp4", f"--output={output.get_text()}", "--bframes=4", "-g", f'"{selectArea}"'] #lista con los argumentos del comando wf-recorder ajustados según las interacciones que el usuario ha tenido con la interfaz gráfica
            print(' '.join(wf_recorder))

            widget.set_label("Stop recording") #el nombre del botón "Start recording" pasa a ser "Stop recording"
            # print(wf_recorder[-1])
            subprocess.Popen(wf_recorder, cwd=fPath) #se ejecuta "wf-recorder" en la carpeta "fPath" que es donde se guardaría el video. En esta línea es donde exactamente inicia la grabación
        else: #si el botón se desactiva, se detiene la grabación
            os.system("killall -s SIGINT wf-recorder") #se detiene "wf-recorder" y por tanto se acaba la grabación
            widget.set_label("Start recording") #el nombre del botón "Stop recording" pasa a ser "Start recording"




win = mainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
