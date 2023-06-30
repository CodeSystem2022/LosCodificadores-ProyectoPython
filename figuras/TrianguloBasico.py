from figuras.FigurasGeometricas import FigurasGeometricas


class Rectangulo(FigurasGeometricas):

    @classmethod
    def area(cls):
        return (cls.base * cls.altura) / 2

