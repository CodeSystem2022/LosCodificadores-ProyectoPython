from operacion.Operacion import Operacion


class ClaseConversor(Operacion):

    def __init__(self):
        self._valorAConvertir = 0
        self.tipoOperacion = "conversion"

    @property
    def valorAConvertir(self):
        return self._valorAConvertir

    @valorAConvertir.setter
    def valorAConvertir(self, valorAConvertir):
        self._valorAConvertir = valorAConvertir
