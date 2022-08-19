import ImagenPulmon

"""
-Se ha evaluado este archivo con flake8
comando flake8 LungOpacy.py
"""


class LungOpacity(ImagenPulmon.ImagenPulmon):
    def __init__(self, nombre, raiz):
        super().__init__(nombre, raiz, "Lung_Opacity")
