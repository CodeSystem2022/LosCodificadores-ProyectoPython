from figuras.FigurasGeometricas import FigurasGeometricas


class Triangulo(FigurasGeometricas):

    @classmethod
    def area(cls, base, altura):
        cls.cuerpoOperacion = f'({base} * {altura}) / 2'
        cls.resultado = (base * altura) / 2
        return cls.resultado
    
    @classmethod
    def perimetro(cls, lado1, lado2, lado3):
        cls.cuerpoOperacion = f'({lado1} + {lado2} + {lado3})'
        cls.resultado = lado1 + lado2 + lado3
        return cls.resultado
