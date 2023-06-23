from ClaseConversor import ClaseConversor


class UnidadLongitud(ClaseConversor):

    @classmethod
    def metroACentimetro(self, valor):
        self.valorAConvertir = valor
        self.cuerpoOperacion = f'{valor} * 100'
        self.resultado = valor * 100
        return f'{valor} metros son {valor * 100} centimetros'

    @classmethod
    def centimetrosAMetro(self, valor):
        self.valorAConvertir = valor
        self.cuerpoOperacion = f'{valor} / 100'
        self.resultado = valor / 100
        return f'{valor} centimetros son {self.resultado} metros'

    @classmethod
    def metrosAKilometro(self, valor):
        self.valorAConvertir = valor
        self.cuerpoOperacion = f'{valor} / 1000'
        self.resultado = valor / 1000
        return f'{valor} metros son {self.resultado} kilometros'

    @classmethod
    def kilometrosAMetros(self, valor):
        self.valorAConvertir = valor
        self.cuerpoOperacion = f'{valor} * 1000'
        self.resultado = valor * 1000
        return f'{valor} kilometros son {self.resultado} metros'