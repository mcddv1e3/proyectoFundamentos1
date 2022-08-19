import Covid
import LungOpacity
import Normal
import ViralPneumonia
from tkinter import Tk, Button, Label, Radiobutton, Entry, StringVar
from tkinter import filedialog

"""
-Módulo que sirve para poder mostrar la ventana
que realiza la adición de imágenes
-Se ha evaluado este archivo con flake8
comando flake8 .\adicion.py
se ha dejado sin errores
"""

root = Tk()
root.geometry("900x300")
imagenElegida = StringVar()
imagenElegidaMascara = StringVar()
global imagenElegida1
imagenElegida1 = ""
directorioR = "C:/Users/LicHernandoSanabria/MODULOII/PROYECTO"


def select_file():
    filetypes = (
        ('png files', '*.png'),
        ('jpg files', '*.jpg'),
        ('All files', '*.*')
    )
    imagenElegida2 = filedialog.askopenfilename(
        title='Open a file',
        initialdir=directorioR+"/IMAGENESADICION/imagenes",
        filetypes=filetypes)
    imagenElegida.set(imagenElegida2)


def select_file1():
    filetypes = (
        ('png files', '*.png'),
        ('jpg files', '*.jpg'),
        ('All files', '*.*')
    )
    imagenElegidaMascara1 = filedialog.askopenfilename(
        title='Open a file',
        initialdir=directorioR + "/IMAGENESADICION/mascaras",
        filetypes=filetypes)
    imagenElegidaMascara.set(imagenElegidaMascara1)


def refrescar(value, value1, vurl1, imagen_mascara):
    """
    Esta función sirve para poder realizar la adición de las imágenes
    """
    imagen1 = value1.split('/')
    imagen2 = imagen1[len(imagen1)-1]
    imagenm1 = imagen_mascara.split('/')
    imagenm2 = imagenm1[len(imagenm1)-1]
    if value == "COVID":
        covid2 = Covid.Covid('NombreProvisional.png', directorioR)
        covid2.adicionar(imagen2, imagenm2,
                         vurl1, 'IMAGENESADICION/imagenes',
                         'IMAGENESADICION/mascaras', 'DATOS')
    if value == "Lung_Opacity":
        LungOpacity1 = LungOpacity.LungOpacity('NombreProvisional.png',
                                               directorioR)
        LungOpacity1.adicionar(imagen2, imagenm2,
                               vurl1, 'IMAGENESADICION/imagenes',
                               'IMAGENESADICION/mascaras', 'DATOS')
    if value == "Normal":
        Normal1 = Normal.Normal('NombreProvisional.png', directorioR)
        Normal1.adicionar(imagen2, imagenm2,
                          vurl1, 'IMAGENESADICION/imagenes',
                          'IMAGENESADICION/mascaras', 'DATOS')
    if value == "Viral Pneumonia":
        ViralPneumonia1 = ViralPneumonia.ViralPneumonia(
                        'NombreProvisional.png', directorioR)
        ViralPneumonia1.adicionar(imagen2, imagenm2,
                                  vurl1, 'IMAGENESADICION/imagenes',
                                  'IMAGENESADICION/mascaras', 'DATOS')


i = 0
btnEnv = Button(root, text="Escoja Imagen Principal",
                command=select_file).grid(row=i)
i = i+1
btnEnv = Button(root, text="Escoja Imagen Mascara",
                command=select_file1).grid(row=i)
i = i+1
titulo = Label(
               root,
               text="Elija a cual categoria corresponden las imagenes:"
              ).grid(row=i)
elegir = ["COVID", "Lung_Opacity", "Normal", "Viral Pneumonia"]
carpetas = StringVar()
carpetas.set("COVID")
i = i+1
for elige in elegir:
    Radiobutton(root, text=elige,
                value=elige, variable=carpetas).grid(row=i)
    i = i+1
titulo1 = Label(root, text="Introduzca url").grid(row=i, column=0)
vurl1 = StringVar()
vurl1.set("")
vurl = Entry(root, textvar=vurl1, width=100).grid(row=i, column=1)
i = i+1

btnEnv = Button(root,
                text="Guardar",
                command=lambda: refrescar(
                                            carpetas.get(),
                                            imagenElegida.get(),
                                            vurl1.get(),
                                            imagenElegidaMascara.get()
                                         )
                ).grid(row=i)
root.mainloop()
