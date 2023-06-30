from figuras.FigurasGeometricas import FigurasGeometricas


class Cuadrado(FigurasGeometricas):

    @classmethod
    def area(cls, lado):
        cls.cuerpoOperacion = f'{lado} ^ 2'
        cls.resultado = lado ** 2
        return cls.resultado

    @classmethod
    def perimetro(cls, lado):
        cls.cuerpoOperacion = f'4 * {lado}'
        cls.resultado = 4 * lado
        return cls.resultado

