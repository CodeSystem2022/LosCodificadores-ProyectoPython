from operacion.Operacion import Operacion
import math

class FuncionesMatematicas(Operacion):
    def __init__(self):
        self.tipoOperacion = "funciones"

    @classmethod
    def pitagorasHipotenusa(self):
        catetoA = float(input('Ingrese el valor del cateto A: '))
        catetoB = float(input('Ingrese el valor del cateto B: '))

        self.cuerpoOperacion = f'sqrt({catetoA}^2 + {catetoB}^2)'
        self.resultado = math.sqrt((catetoA ** 2)+(catetoB ** 2))

        return math.sqrt((catetoA ** 2)+(catetoB ** 2))

    @classmethod
    def pitagorasCatetoA(self):
        hipotenusa = 0
        catetoB = 1
        while ((hipotenusa ** 2) < (catetoB ** 2)):
            print('Tener en cuenta que el valor de hipotenusa ^ 2 debe ser mayor a cateto b ^ 2, para que el radicando sea mayor a 0')
            hipotenusa = float(input('Ingrese el valor de la hipotenusa: '))
            catetoB = float(input('Ingrese el valor del cateto B: '))

        self.cuerpoOperacion = f'sqrt({hipotenusa}^2 - {catetoB}^2)'
        self.resultado = math.sqrt((hipotenusa ** 2) - (catetoB ** 2))

        return math.sqrt((hipotenusa ** 2) - (catetoB ** 2))

    @classmethod
    def pitagorasCatetoB(self):
        hipotenusa = 0
        catetoA = 1
        while ((hipotenusa ** 2) < (catetoA ** 2)):
            print('Tener en cuenta que el valor de hipotenusa ^ 2 debe ser mayor a cateto a ^ 2, para que el radicando sea mayor a 0')
            hipotenusa = float(input('Ingrese el valor de la hipotenusa: '))
            catetoA = float(input('Ingrese el valor del cateto A: '))

        self.cuerpoOperacion = f'sqrt({hipotenusa}^2 - {catetoA}^2)'
        self.resultado = math.sqrt((hipotenusa ** 2) - (catetoA ** 2))

        return math.sqrt((hipotenusa ** 2) - (catetoA ** 2))

    @classmethod
    def raicesCuadraticas(self):
        a = float(input('Ingrese el valor del coeficiente numérico de x^2: '))
        b = float(input('Ingrese el valor del coeficiente numérico de x: '))
        c = float(input('Ingrese el valor del termino independiente: '))

        if ((b ** 2 - 4*a*c) >= 0):
            raiz1 = (-b + math.sqrt(b ** 2 - 4*a*c)) / 2*a
            raiz2 = (-b - math.sqrt(b ** 2 - 4*a*c)) / 2*a

            self.cuerpoOperacion = f'{a}x^2 +({b}x) + ({c}) = x1: {raiz1}, x2: {raiz2}'
            self.resultado = {'x1': raiz1, 'x2': raiz2}
            return {'x1': raiz1, 'x2': raiz2}
        else:
            print(
                'Esta raiz no se puede resolver en el dominio de los números reales, intente con otra función')
            FuncionesMatematicas.raicesCuadraticas()

            
