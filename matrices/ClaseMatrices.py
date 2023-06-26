from Operacion import Operacion

class Matrices(Operacion):

    def __init__(self):
        self.matriz = None
        self.matriz2 = None

    def set_matriz(self, matriz):
        self.matriz = matriz

    def set_matriz2(self, matriz2):
        self.matriz2 = matriz2

    def get_matriz(self):
        return self.matriz

    def get_matriz2(self):
        return self.matriz2
