import ImagenPulmon

"""
-Se ha evaluado este archivo con flake8
comando flake8 ViralPneumonia.py
"""


class ViralPneumonia(ImagenPulmon.ImagenPulmon):
    def __init__(self, nombre, raiz):
        super().__init__(nombre, raiz, "Viral Pneumonia")
