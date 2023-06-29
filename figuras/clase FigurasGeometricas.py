from Operacion import Operacion


class FigurasGeometricas(Operacion):
    def __init__(self, base=0, altura=0, radio=0, lado=0) -> None:
        self.tipoOperacion = 'figura'
        self._base = base
        self._altura = altura
        self._radio = radio
        self._lado = lado

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, base):
        self._base = base

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura):
        self._altura = altura

    @property
    def lado(self):
        return self._lado

    @lado.setter
    def lado(self, lado):
        self._lado = lado

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, radio):
        self._radio = radio

