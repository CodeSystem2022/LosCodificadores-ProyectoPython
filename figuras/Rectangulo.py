from figuras.FigurasGeometricas import FigurasGeometricas


class Rectangulo(FigurasGeometricas):

    @classmethod
    def area(cls, base, altura):
        cls.cuerpoOperacion = f'{base} * {altura}'
        cls.resultado = base * altura
        return cls.resultado

    @classmethod
    def perimetro(cls, base, altura):
        cls.cuerpoOperacion = f'2 * {base} + 2 * {altura}'
        cls.resultado = (2 * base) + (2 * altura)
        return cls.resultado