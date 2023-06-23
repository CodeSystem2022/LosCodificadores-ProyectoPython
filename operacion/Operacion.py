class Operacion():
    def __init__(self, tipoOperacion = None, cuerpoOperacion = None, resultado = None) -> None:
        self._cuerpoOperacion = cuerpoOperacion
        self._tipoOperacion = tipoOperacion
        self._resultado = resultado
    
    @property
    def tipoOperacion(self):
        return self._tipoOperacion

    @tipoOperacion.setter
    def tipoOperacion(self, tipoOperacion):
        self._tipoOperacion = tipoOperacion

    @property
    def cuerpoOperacion(self):
        return self._cuerpoOperacion

    @cuerpoOperacion.setter
    def cuerpoOperacion(self, cuerpoOperacion):
        self._cuerpoOperacion = cuerpoOperacion

    @property
    def resultado(self):
        return self._resultado

    @resultado.setter
    def resultado(self, resultado):
        self._resultado = resultado

    def __str__(self) -> str:
        return f'Operacion: [tipoOperacion:{self.tipoOperacion}, cuerpoOperacion:{self.cuerpoOperacion}, resultado: {self.resultado}]'