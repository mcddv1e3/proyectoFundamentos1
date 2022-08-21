import pandas as pd
import cv2  # instalarlo pip install opencv-python
import shutil
import os
from PIL import Image
"""
-Se ha evaluado este archivo con flake8
comando flake8 ImagenPulmon
se ha dejado sin errores
con excepción de E501 line too long (82 > 79 characters)
puesto de que las ventanas actuales aceptan mas caracteres
"""


class ImagenPulmon:
    """Clase que tiene los métodos que hacen la adición, modificación y eliminación de imagenes y sus metadatos
    Parameters
    ----------
    nombre  : str
            El nombre de la clase al crear una instancia

    raiz    : str
            El directorio donde se esta corriendo el programa por defecto

    directorio : str
            La categoria a la que pertenece la clase por ejemplo: COVID, Normal, etc... que
            luego se usa como directorio pues tiene el mismo nombre
    """
    def __init__(self, nombre, raiz, directorio):
        self.nombre = nombre  # el nombre de la imagen
        self.raiz = raiz  # el directorio raiz donde se trabajara por ejemplo c:/PROYECTOFINAL
        self.directorio = directorio  # el directorio donde pertenece la imagen ejm. COVID, Lung_Opacity

    def adicionar(
                    self, nombre_imagen,
                    nombre_mascara, url,
                    dir_imagenes, dir_mascaras,
                    dir_datos
                 ):
        """Método que sirve para adicionar una imágen tanto en images como masks y actualizar su excel correspondiente
        -se obtiene la extension del archivo de imagen para obtener su tipo
        -determinamos el nombre que nos corresponde para grabar:obtenemos el ultimo nombre (FILE NAME )
        del registro del excel donde vamos a grabar para poder determinar el nombre que me toca
        sumar en 1 en el nombre, usamos un data frame para esto (df)
        -obteniendo los datos de la imágen:se obtiene el ancho, alto de la imagen a ser copiada
        -se agrega al excel el registro correspondiente.

        Parameters
        ----------
        nombre_imagen : str
                      nombre de la imagen a adicionar a la carpeta images ejm. mimagen.jpg

        nombre_mascara : str
                      nombre de la imagen a adicionar para la carpeta masks ejm imagen1.jpg

        url : str
                la direccion url que se guardara en el excel

        dir_imagenes : str
                la direccion de las imagenes que podemos adicionar a la carpeta imagenes

        dir_mascaras : str
                la direccion de las imagenes que podemos adicionar a la carpeta mascaras

        dir_datos : str
                la carpeta donde esta el dataset

        Returns
        -------
        vtodo_bien : int
                Si no ha ocurrido ningun error devuelve 1 y si hay algun error devuelve 0.
        """
        vtodo_bien = 1
        if not os.path.exists(self.raiz):
            vtodo_bien = 0
        if not os.path.exists(self.raiz+"/"+dir_datos+"/"+self.directorio+".metadata.xlsx"):
            vtodo_bien = 0
        if not os.path.exists(self.raiz+"/"+dir_imagenes+"/"+nombre_imagen):
            vtodo_bien = 0
        if not os.path.exists(self.raiz+"/"+dir_mascaras+"/"+nombre_mascara):
            vtodo_bien = 0
        if vtodo_bien == 1:
            try:
                # obteniendo la extension del archivo de imagen para obtener su tipo
                extension1 = nombre_imagen.split(".")
                extension2 = extension1[-1]
                # determinamos el nombre que nos corresponde para grabar
                df = pd.read_excel(self.raiz+"/"+dir_datos+"/"+self.directorio+".metadata.xlsx")
                ultimo = df.loc[df.index[-1], "FILE NAME"]
                ultimo1 = ultimo.split("-")
                ultimo2 = ultimo1[-1]
                ultimo_numero = int(ultimo2)
                ultimo_mas1 = ultimo_numero+1
                ultimo_file_name_nextension = self.directorio+"-"+str(ultimo_mas1)
                ultimo_file_name = self.directorio+"-"+str(ultimo_mas1)+"."+extension2
                # obteniendo el nombre de la mascara con su extension
                extensionm1 = nombre_mascara.split(".")
                extensionm2 = extensionm1[-1]
                ultimo_file_mname = self.directorio+"-"+str(ultimo_mas1)+"."+extensionm2
                # obteniendo los datos de la imágen ancho alto
                imagen_copiar = self.raiz+"/"+dir_imagenes+"/"+nombre_imagen
                img = cv2.imread(imagen_copiar, cv2.IMREAD_UNCHANGED)
                ancho = img.shape[0]
                alto = img.shape[1]
                csize = str(ancho)+"*"+str(alto)
                shutil.copy(imagen_copiar, self.raiz+"/"+dir_datos+"/"+self.directorio+"/images/"+ultimo_file_name)
                # copiando mascara
                imagen_mascara_copiar = self.raiz+"/"+dir_mascaras+"/"+nombre_mascara
                shutil.copy(imagen_mascara_copiar, self.raiz+"/"+dir_datos+"/"+self.directorio+"/masks/"+ultimo_file_mname)
                # agregando al excel el registro correspondiente
                nuevo_registro = {"FILE NAME": ultimo_file_name_nextension, "FORMAT": extension2, "SIZE": csize, "URL": url}
                df = df.append(nuevo_registro, ignore_index=True)
                df.to_excel(self.raiz+"/"+dir_datos+"/"+self.directorio+".metadata.xlsx", index=False)
            except FileNotFoundError:
                vtodo_bien = 0
        return vtodo_bien

    def eliminar(
                    self, nombre_imagen,
                    nombre_mascara,
                    dir_datos
                 ):
        """Este método elimina una imagen de la carpeta images y mask y del excel
        Parameters
        ----------
        nombre_imagen : str
                      nombre de la imagen a eliminar de la carpeta images ejm. COVID-112.png
        nombre_mascara : str
                      nombre de la imagen a eliminar de la carpeta de masks ejm COVID-112.png
        dir_datos : str
                    la carpeta donde esta el dataset
        Returns
        -------
        vtodo_bien : int
                Si no ha ocurrido ningun error devuelve 1 y si hay algun error devuelve 0.
        """
        vtodo_bien = 1
        if not os.path.exists(self.raiz):
            vtodo_bien = 0
        if not os.path.exists(self.raiz+"/"+dir_datos+"/"+self.directorio+".metadata.xlsx"):
            vtodo_bien = 0
        if vtodo_bien == 1:
            try:
                nombre_imagen1 = nombre_imagen.split(".")
                nombre = nombre_imagen1[0]
                nom_imagen = self.raiz+"/"+dir_datos+"/"+self.directorio+"/images/"+nombre_imagen
                nom_mascara = self.raiz+"/"+dir_datos+"/"+self.directorio+"/masks/"+nombre_mascara
                os.remove(nom_imagen)
                os.remove(nom_mascara)
                df = pd.read_excel(self.raiz+"/"+dir_datos+"/"+self.directorio+".metadata.xlsx")
                df1 = df.drop(df[df['FILE NAME'] == nombre].index)
                df1.to_excel(self.raiz+"/"+dir_datos+"/"+self.directorio+".metadata.xlsx", index=False)
            except FileNotFoundError:
                vtodo_bien = 0
        return vtodo_bien

    def modificar(
                self, nombre_imagen,
                nombre_mascara,
                dir_datos
                ):
        """Este método modifica una imagen de la carpeta images y mask y el excel
        La modificación consiste en cambiar la extension de las imagenes a png y el tamaño
        a 256 x 256 pixeles que es el formato que todas las imagenes tienen
        Parameters
        ----------
        nombre_imagen : str
                      nombre de la imagen a modificar de la carpeta images ejm. COVID-112.png
        nombre_mascara : str
                      nombre de la imagen a modificar de la carpeta de masks ejm COVID-112.png
        dir_datos : str
                    la carpeta donde esta el dataset
        Returns
        -------
        vtodo_bien : int
                Si no ha ocurrido ningun error devuelve 1 y si hay algun error devuelve 0.
        """
        vtodo_bien = 1
        try:
            # Redimensionar imágenes

            img = cv2.imread(f'{self.raiz}/{dir_datos}/{self.directorio}/images/{nombre_imagen}', cv2.IMREAD_UNCHANGED)
            alto = 256
            ancho = 256
            dimension = (alto, ancho)

            redimensionado = cv2.resize(img, dimension, interpolation=cv2.INTER_AREA)
            cv2.imwrite(f'{self.raiz}/{dir_datos}/{self.directorio}/images/{nombre_imagen}', redimensionado)

            # Redimensionar máscaras

            msk = cv2.imread(f'{self.raiz}/{dir_datos}/{self.directorio}/masks/{nombre_mascara}', cv2.IMREAD_UNCHANGED)
            alto = 256
            ancho = 256
            dimension = (alto, ancho)

            redimensionado = cv2.resize(msk, dimension, interpolation=cv2.INTER_AREA)
            cv2.imwrite(f'{self.raiz}/{dir_datos}/{self.directorio}/masks/{nombre_mascara}', redimensionado)

            imagen_png = Image.open(f'{self.raiz}/{dir_datos}/{self.directorio}/images/{nombre_imagen}')
            imagen_png = imagen_png.save(f'{self.raiz}/{dir_datos}/{self.directorio}/images/{str(nombre_imagen.split(".")[0])}.png')
            os.remove(f'{self.raiz}/{dir_datos}/{self.directorio}/images/{nombre_imagen}')

            mascara_png = Image.open(f'{self.raiz}/{dir_datos}/{self.directorio}/masks/{nombre_mascara}')
            mascara_png = mascara_png.save(f'{self.raiz}/{dir_datos}/{self.directorio}/masks/{str(nombre_mascara.split(".")[0])}.png')
            os.remove(f'{self.raiz}/{dir_datos}/{self.directorio}/masks/{nombre_mascara}')

            # Editar dataset

            df = pd.read_excel(f'{self.raiz}/{dir_datos}/{self.directorio}.metadata.xlsx')
            indice = df[df['FILE NAME'] == nombre_imagen.split('.')[0]].index[0]

        except IndexError as e:
            vtodo_bien = 0
        except :
            vtodo_bien = 0
        if vtodo_bien == 1:
            df.iloc[indice]['FORMAT'] = 'PNG'
            df.iloc[indice]['SIZE'] = '256*256'

            # Descargar base de datos .xlsx
            df.to_excel(f'{self.raiz}/{dir_datos}/{self.directorio}.metadata.xlsx', index=False)
        return vtodo_bien
