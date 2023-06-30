from figuras.FigurasGeometricas import FigurasGeometricas


class Rectangulo(FigurasGeometricas):

    @classmethod
    def area(cls):
        return cls.base * cls.altura

    @classmethod
    def perimetro(cls):
        return (2 * cls.base) + (2 * cls.altura)

