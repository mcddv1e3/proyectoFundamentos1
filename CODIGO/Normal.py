import ImagenPulmon

"""
-Se ha evaluado este archivo con flake8
comando flake8 Normal.py
"""


class Normal(ImagenPulmon.ImagenPulmon):
    def __init__(self, nombre, raiz):
        super().__init__(nombre, raiz, "Normal")
