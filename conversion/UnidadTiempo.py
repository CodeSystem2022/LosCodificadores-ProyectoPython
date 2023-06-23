from conversion.ClaseConversor import ClaseConversor


class UnidadTiempo(ClaseConversor):

    @classmethod
    def segundoAMinuto(self, valor):
        self.valorAConvertir = valor
        self.cuerpoOperacion = f'{valor} / 60'
        self.resultado = valor / 60
        return f'{valor} segundos son {valor / 60} minutos'

    @classmethod
    def minutoAHora(self, valor):
        self.valorAConvertir = valor
        self.cuerpoOperacion = f'{valor} / 60'
        self.resultado = valor / 60
        return f'{valor} minutos son {valor / 60} horas'

    @classmethod
    def segundoAHora(self, valor):
        self.valorAConvertir = valor
        self.cuerpoOperacion = f'{valor} / 3600'
        self.resultado = valor / 3600
        return f'{valor} segundos son {valor / 3600} horas'

    @classmethod
    def minutoASegundo(self, valor):
        self.valorAConvertir = valor
        self.cuerpoOperacion = f'{valor} * 60'
        self.resultado = valor * 60
        return f'{valor} minutos son {valor * 60} segundos'

    @classmethod
    def horaAMinuto(self, valor):
        self.valorAConvertir = valor
        self.cuerpoOperacion = f'{valor} * 60'
        self.resultado = valor * 60
        return f'{valor} horas son {valor * 60} minutos'

    @classmethod
    def horaASegundos(self, valor):
        self.valorAConvertir = valor
        self.cuerpoOperacion = f'{valor} * 3600'
        self.resultado = valor * 3600
        return f'{valor} horas son {valor * 3600} segundos'
    