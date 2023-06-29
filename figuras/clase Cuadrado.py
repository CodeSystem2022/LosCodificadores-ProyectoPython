from figuras.ClaseFigurasGeometricas import FigurasGeometricas


class Cuadrado(FigurasGeometricas):

    @classmethod
    def area(cls):
        return cls.lado ** 2

    @classmethod
    def perimetro(cls):
        return 4 * cls.lado

