from figuras.ClaseFigurasGeometricas import FigurasGeometricas
import math


class Triangulo(FigurasGeometricas):
    def __init__(self, cateto_a=None, cateto_b=None, hipotenusa=None, angulo_A=None, angulo_B=None):

        self.cateto_a = cateto_a
        self.cateto_b = cateto_b
        self.hipotenusa = hipotenusa
        self.angulo_A = angulo_A
        self.angulo_B = angulo_B

    def calcular_hipotenusa(self):

        self.hipotenusa = math.sqrt(self.cateto_a ** 2 + self.cateto_b ** 2)
        return self.hipotenusa

    def calcular_con_catetoehipotenusa(self):

        if self.cateto_a is not None and self.hipotenusa is not None:
            self.cateto_b = (self.hipotenusa ** 2 - self.cateto_a ** 2) ** (1 / 2)
            return self.cateto_b
        elif self.cateto_b is not None and self.hipotenusa is not None:
            self.cateto_a = math.sqrt(self.hipotenusa ** 2 - self.cateto_b ** 2)
            return self.cateto_a
        else:
            return None

    def calcular_con_ladoyangulo(self):

        if self.cateto_a is not None and self.angulo_A is not None:
            self.cateto_b = self.cateto_a / math.tan(math.radians(self.angulo_A))
            self.hipotenusa = self.calcular_hipotenusa()
            self.angulo_B = 90 - self.angulo_A
            return f'cateto b = {self.cateto_b}\n hipotenusa = {self.hipotenusa}\n ángulo B = {self.angulo_B}'

        elif self.cateto_a is not None and self.angulo_B is not None:
            self.cateto_b = self.cateto_a * math.tan(self.angulo_B)
            self.hipotenusa = math.sqrt(self.cateto_a ** 2 + self.cateto_b ** 2)
            self.angulo_A = 90 - self.angulo_B
            return f'cateto b = {self.cateto_b}\n hipotenusa = {self.hipotenusa}\n ángulo B = {self.angulo_B}'

        elif self.cateto_b is not None and self.angulo_A is not None:
            self.cateto_a = self.cateto_b * math.tan(self.angulo_A)
            self.hipotenusa = math.sqrt(self.cateto_a ** 2 + self.cateto_b ** 2)
            self.angulo_B = 90 - self.angulo_A
            return f'cateto a = {self.cateto_a}\n hipotenusa = {self.hipotenusa}\n ángulo B = {self.angulo_B}'

        elif self.cateto_b is not None and self.angulo_B is not None:
            self.cateto_a = self.cateto_b / math.tan(self.angulo_B)
            self.hipotenusa = self.calcular_hipotenusa()
            self.angulo_A = 90 - self.angulo_B
            return f'cateto a = {self.cateto_a}\n hipotenusa = {self.hipotenusa}\n ángulo A = {self.angulo_A}'

        else:
            return None

    def calcular_area(self):

        if self.cateto_a is not None and self.cateto_b is not None:
            area = 0.5 * self.cateto_a * self.cateto_b
            return area
        elif self.cateto_a is not None and self.hipotenusa is not None:
            self.calcular_con_catetoehipotenusa()
            self.calcular_area()
            area = 0.5 * self.cateto_a * self.cateto_b
            return area
        elif self.cateto_a is not None and self.angulo_A is not None:
            self.calcular_con_ladoyangulo()
            self.calcular_area()
            return 0.5 * self.cateto_a * self.cateto_b
        elif self.cateto_a is not None and self.angulo_B is not None:
            self.calcular_con_ladoyangulo()
            self.calcular_area()
            return 0.5 * self.cateto_a * self.cateto_b
        elif self.cateto_b is not None and self.angulo_A is not None:
            self.calcular_con_ladoyangulo()
            self.calcular_area()
            return 0.5 * self.cateto_a * self.cateto_b
        elif self.cateto_b is not None and self.angulo_B is not None:
            self.calcular_con_ladoyangulo()
            self.calcular_area()
            return 0.5 * self.cateto_a * self.cateto_b
        else:
            return None

    def calcular_perimetro(self):

        if self.lado_a is not None and self.lado_b is not None and self.lado_c is not None:
            perimetro = self.lado_a + self.lado_b + self.lado_c()
            return "perimetro: ", perimetro
        else:
            return None

