---
lang: es
---
# Easy Sway Recorder

Este proyecto responde a la necesidad de tener una interfaz gráfica fácil de usar para hacer capturas de video de la pantalla en sistemas operativos linux que utilicen compositors de Wayland basados en Wlroots, particularmente [Sway](https://swaywm.org/) que es uno de los más populares. Easy Sway Recorder sería un wrapper de [Wf-recorder](https://github.com/ammen99/wf-recorder), software que se encarga bastante bien de hacer las capturas de video pero que por ser de uso desde la línea de comandos resulta siendo poco intuitivo para el usuario final. 

## Características mínimas
- Ser una ["aplicación GTK"](https://gtk.org/).
- Hacer que "~/Videos" sea la carpeta predeterminada de exportación de las capturas de pantalla.
- Menú que permita escoger entre los distintos codecs disponibles en Wf-recorder.
- Menú que permita escoger alguno de los distintos servidores de sonido de Pulse Audio.
- Recuadro que permita ingresar la carpeta destino y el nombre de la captura de pantalla.
- Checkbox que permita activar o desactivar el audio en la grabación.
- Script que funcione como trigger de Easy Sway Recorder bien sea para iniciar la aplicación o para detener una grabación en curso. Esto, con el fin de que se pueda anclar el script a un keybinding y hacer la experiencia de una grabación de pantalla similar a la de un screenshot.


## Características deseables
- Detección automática del server de salida de audio del computador ya que por defecto Wf-recorder no lo reconoce. 
- Menú que permita seleccionar la ventana o workspace específico a grabar.
- Casilla para ingresar el lapso de tiempo que debe transcurrir desde que se da clic en el botón "Iniciar grabación" hasta que se empieza a grabar.





Easy Sway Recorder será probado inicialmente en la distribución Arch linux con Easy Effects y Pipewire como controladores de audio y Sway como comopositor de Wayland. No obstante, se
espera que también funcione correctamente con otras distribuciones, servidores de audio y compositors. Como detalle final, una vez sea estable Easy Sway Recorder, sería ideal que se empaquete y se suba al repositorio AUR, para que se pueda descargar e instalar fácilmente en las distribuciones basadas en Arch. No se descarta incluírlo en otros repositorios como el de Debian o incluso Flatpak.

Inicialmente, el código estará en esta carpeta pero cuando sea estable se trabajará sobre este [repositorio](https://github.com/pipe99g/Easy-Sway-Recorder).
