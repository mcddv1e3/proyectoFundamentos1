import Covid
import LungOpacity
import Normal
import ViralPneumonia
from tkinter import Tk, Button, StringVar, messagebox
from tkinter import filedialog
import os

"""Módulo que sirve para poder mostrar la ventana que realiza la eliminación de imágenes
See also
--------
-Se ha evaluado este archivo con flake8
comando flake8 eliminacion.py
se ha dejado sin errores
con excepción de E501 line too long (82 > 79 characters)
puesto de que las ventanas actuales aceptan mas caracteres
"""

root = Tk()
root.geometry("900x300")
imagenElegida = StringVar()
imagenElegidaMascara = StringVar()
global imagenElegida1
imagenElegida1 = ""
directorioR = "C:/Users/LicHernandoSanabria/MODULOII/PROYECTO"


def select_file():
    """Esta funcion selecciona una imagen para poder eliminar con filedialog
    Returns
    ----------
    imagenElegida2 : str
                    Es la imagen elegida que va ha ser eliminada con toda su ruta
    """

    filetypes = (
        ('png files', '*.png'),
        ('jpg files', '*.jpg'),
        ('All files', '*.*')
    )
    imagenElegida2 = filedialog.askopenfilename(
        title='Open a file',
        initialdir=directorioR+"/DATOS",
        filetypes=filetypes)
    imagenElegida.set(imagenElegida2)


def refrescar(value1):
    """Esta función sirve para poder realizar la eliminacion de las imágenes llamando al método eliminar de cada clase
    Parameters
    ----------
    value1 : str
            es la imagen con toda su ruta que va ha ser eliminada
    Returns
    ----------
    messagebox : messagebox
                Un mensaje que indica si se ha realizado la eliminacion y otro si hubo algun error
    """
    vresul = 1
    if not os.path.exists(value1):
        vresul = 0
    if vresul == 1:
        imagen1 = value1.split('/')
        imagen2 = imagen1[len(imagen1)-1]
        value = imagen1[len(imagen1)-3]
        if value == "COVID":
            covid2 = Covid.Covid('NombreProvisional.png', directorioR)
            vresul = covid2.eliminar(
                                        imagen2,
                                        imagen2,
                                        'DATOS'
                                     )
        if value == "Lung_Opacity":
            LungOpacity1 = LungOpacity.LungOpacity('NombreProvisional.png',
                                                   directorioR)
            vresul = LungOpacity1.eliminar(
                                            imagen2,
                                            imagen2,
                                            'DATOS'
                                            )
        if value == "Normal":
            Normal1 = Normal.Normal('NombreProvisional.png', directorioR)
            vresul = Normal1.eliminar(
                                        imagen2,
                                        imagen2,
                                        'DATOS'
                                      )
        if value == "Viral Pneumonia":
            ViralPneumonia1 = ViralPneumonia.ViralPneumonia(
                            'NombreProvisional.png', directorioR)
            vresul = ViralPneumonia1.eliminar(
                                                imagen2,
                                                imagen2,
                                                'DATOS'
                                             )
    if vresul == 1:
        messagebox.showinfo(message="Se guardaron los cambios satisfactoriamente")
    else:
        messagebox.showinfo(message="Ocurrio algun error")


i = 0
btnEnv = Button(root, text="Escoja Imagen Principal",
                command=select_file).grid(row=i)
i = i+1

btnEnv = Button(root,
                text="Eliminar",
                command=lambda: refrescar(
                                            imagenElegida.get()
                                         )
                ).grid(row=i)
root.mainloop()
