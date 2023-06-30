from figuras.FigurasGeometricas import FigurasGeometricas
import math

class Circulo(FigurasGeometricas):

    @classmethod
    def area(cls, radio):
        cls.cuerpoOperacion = f'{math.pi} * {radio} ^ 2'
        cls.resultado = math.pi * radio ** 2
        return cls.resultado

    @classmethod
    def perimetro(cls, radio):
        cls.cuerpoOperacion = f'2 * {math.pi} * {radio}'
        cls.resultado = 2 * math.pi * radio
        return cls.resultado

