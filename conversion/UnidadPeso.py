from conversion.ClaseConversor import ClaseConversor


class UnidadPeso(ClaseConversor):

    @classmethod
    def kiloAGramo(self, valor):
        self.valorAConvertir = valor
        self.cuerpoOperacion = f'{valor} * 1000'
        self.resultado = valor * 1000
        return f'{valor} kilos son {valor * 1000} gramos'

    @classmethod
    def gramoAKilo(self, valor):
        self.valorAConvertir = valor
        self.cuerpoOperacion = f'{valor} / 1000'
        self.resultado = valor / 1000
        return f'{valor} gramos son {valor / 1000} kilos'

    @classmethod
    def kiloALibra(self, valor):
        self.valorAConvertir = valor
        self.cuerpoOperacion = f'{valor} * 2.205'
        self.resultado = valor * 2.205
        return f'{valor} kilos son {valor * 2.205} libras'

    @classmethod
    def libraAKilo(self, valor):
        self.valorAConvertir = valor
        self.cuerpoOperacion = f'{valor} / 2.205'
        self.resultado = valor / 2.205
        return f'{valor} libras son {valor / 2.205} kilos'
