import Covid
import LungOpacity
import Normal
import ViralPneumonia
import unittest


class TestAdicion(unittest.TestCase):
    def test_prueba_humo(self):
        """
        Mandamos valores validos para realizar la adicion
        deberia de devolvernos un 1 muestra que esta todo funcionando bien
        no deberia de fallar (no sale humo)
        """
        covid2 = Covid.Covid('NombreProvisional.png', 'C:/Users/LicHernandoSanabria/MODULOII/PROYECTO')
        vresul = covid2.adicionar(
                                    '95878.jpg',
                                    'estudios-de-imagen-covid-19.jpg',
                                    'pruebaHumo1.com',
                                    'IMAGENESADICION/imagenes',
                                    'IMAGENESADICION/mascaras',
                                    'DATOS'
                                )
        print("prueba humo")
        print(vresul)

    def test_prueba_humo1(self):
        """
        Mandamos valores validos para realizar la adicion
        deberia de devolvernos un 1 muestra que esta todo funcionando bien
        no deberia de fallar (no sale humo)
        """
        lung1 = LungOpacity.LungOpacity('NombreProvisional.png', 'C:/Users/LicHernandoSanabria/MODULOII/PROYECTO')
        vresul = lung1.adicionar(
                                    '95878.jpg',
                                    'estudios-de-imagen-covid-19.jpg',
                                    'pruebaHumo1.com',
                                    'IMAGENESADICION/imagenes',
                                    'IMAGENESADICION/mascaras',
                                    'DATOS'
                                )
        print("prueba humo")
        print(vresul)
    
    def test_prueba_golpe(self):
        """
        Mandamos un directorio raiz que no existe deberia devolvernos un 0
        (prueba de golpe sabemos que resultado debe darnos)
        indica que hubo un error
        """
        covid2 = Covid.Covid('NombreProvisional.png', 'C:/Users/LicHernandoSanabria/')
        vresul = covid2.adicionar(
                                    '95878.jpg',
                                    'estudios-de-imagen-covid-19.jpg',
                                    'pruebaHumo1.com',
                                    'IMAGENESADICION/imagenes',
                                    'IMAGENESADICION/mascaras',
                                    'DATOS'
                                )
        print("prueba golpe")
        print(vresul)

    def test_prueba_golpe1(self):
        """
        Mandamos un directorio raiz que no existe deberia devolvernos un 0
        (prueba de golpe sabemos que resultado debe darnos)
        indica que hubo un error
        """
        normal1 = Normal.Normal('NombreProvisional.png', 'C:/Users/LicHernandoSanabria/')
        vresul = normal1.adicionar(
                                    '95878.jpg',
                                    'estudios-de-imagen-covid-19.jpg',
                                    'pruebaHumo1.com',
                                    'IMAGENESADICION/imagenes',
                                    'IMAGENESADICION/mascaras',
                                    'DATOS'
                                )
        print("prueba golpe")
        print(vresul)

    def test_prueba_borde(self):
        """
        Mandamos una imagen que no existe para guardar deberia de lanzar la excepcion FileNotFoundError
        """
        covid2 = Covid.Covid('NombreProvisional.png', 'C:/Users/LicHernandoSanabria/')
        vresul = covid2.adicionar(
                                    '123234.jpg',
                                    'estudios-de-imagen-covid-19.jpg',
                                    'pruebaHumo1.com',
                                    'IMAGENESADICION/imagenes',
                                    'IMAGENESADICION/mascaras',
                                    'DATOS'
                                )
        print("prueba borde")
        print(vresul)

    def test_prueba_borde1(self):
        """
        Mandamos una imagen que no existe para guardar deberia de lanzar la excepcion FileNotFoundError
        """
        viralPneumonia1 = ViralPneumonia.ViralPneumonia('NombreProvisional.png', 'C:/Users/LicHernandoSanabria/')
        vresul = viralPneumonia1.adicionar(
                                    '123234.jpg',
                                    'estudios-de-imagen-covid-19.jpg',
                                    'pruebaHumo1.com',
                                    'IMAGENESADICION/imagenes',
                                    'IMAGENESADICION/mascaras',
                                    'DATOS'
                                )
        print("prueba borde")
        print(vresul)


suite = unittest.TestLoader().loadTestsFromTestCase(TestAdicion)
_ = unittest.TextTestRunner().run(suite)
