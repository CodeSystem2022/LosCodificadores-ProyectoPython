from figuras.FigurasGeometricas import FigurasGeometricas
import math


class Circulo(FigurasGeometricas):

    @classmethod
    def calcular_area(cls):
        return math.pi * cls.radio ** 2

    @classmethod
    def calcular_perimetro(cls):
        return 2 * math.pi * cls.radio

