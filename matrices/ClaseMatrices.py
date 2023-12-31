import numpy as np
from operacion.Operacion import Operacion

class Matrices(Operacion):

    def __init__(self):
        self.matriz = None
        self.matriz2 = None
        self.tipoOperacion = 'matrices'

    def set_matriz(self, matriz):
        self.matriz = matriz

    def set_matriz2(self, matriz2):
        self.matriz2 = matriz2

    def get_matriz(self):
        return self.matriz

    def get_matriz2(self):
        return self.matriz2

    def llenar_matrices(self, operation_type):

        print(f'\n.:OPERACIÓN {operation_type.upper()} DE MATRICES:.\n')

        n_filas = int(input('Ingrese el número de FILAS: '))
        n_columnas = int(input('Ingrese el número de COLUMNAS: '))

        matriz = np.empty((n_filas, n_columnas))

        if operation_type != 'escalar' and operation_type != 'transpuesta':
            n_filas2 = int(input('Ingrese el número de FILAS de la segunda matriz: '))
            n_columnas2 = int(input('Ingrese el número de COLUMNAS de la segunda matriz: '))

            matriz2 = np.empty((n_filas2, n_columnas2))

            if operation_type == 'suma':
                while matriz.shape != matriz2.shape:
                    print("\nERROR: Las dimensiones de las matrices no son compatibles para la suma.\n")

                    n_filas = int(input('Ingrese el número de FILAS de la primer matriz: '))
                    n_columnas = int(input('Ingrese el número de COLUMNAS de la primer matriz: '))
                    matriz = np.empty((n_filas, n_columnas))

                    n_filas2 = int(input('Ingrese el número de FILAS de la segunda matriz: '))
                    n_columnas2 = int(input('Ingrese el número de COLUMNAS de la segunda matriz: '))
                    matriz2 = np.empty((n_filas2, n_columnas2))

            elif operation_type == 'producto':
                while n_columnas != n_filas2:
                    print("\nERROR: Las dimensiones de las matrices no son compatibles para el producto.\n")

                    n_filas = int(input('Ingrese el número de FILAS de la primer matriz: '))
                    n_columnas = int(input('Ingrese el número de COLUMNAS de la primer matriz: '))
                    matriz = np.empty((n_filas, n_columnas))

                    n_filas2 = int(input('Ingrese el número de FILAS de la segunda matriz: '))
                    n_columnas2 = int(input('Ingrese el número de COLUMNAS de la segunda matriz: '))
                    matriz2 = np.empty((n_filas2, n_columnas2))
        else:
            matriz2 = None

        print(f"\n----------MATRIZ N° 1----------\n-----INGRESAMOS LOS VALORES-----")
        for i in range(n_filas):
            for j in range(n_columnas):
                matriz[i, j] = float(input(f'Ingrese el valor para la posición[{i + 1}, {j + 1}]: '))

        if operation_type != 'escalar' and operation_type != 'transpuesta':
            print("\n----------MATRIZ N° 2----------\n-----INGRESAMOS LOS VALORES-----")
            for i in range(n_filas2):
                for j in range(n_columnas2):
                    matriz2[i, j] = float(input(f'Ingrese el valor para la posición[{i + 1}, {j + 1}]: '))

        self.set_matriz(matriz)
        self.set_matriz2(matriz2)

    def mostrar_matrices(self):
        print("\n ----------MATRIZ N°1---------- ")
        print(self.get_matriz())
        if self.get_matriz2() is not None:
            print("\n ----------MATRIZ N°2---------- ")
            print(self.get_matriz2())
            print("\n ----------MATRIZ RESULTADO----------")
            print(self.resultado)

    def transpuesta(self):
        if self.matriz is None:
            print("Error: La matriz no ha sido llenada. Por favor, llene la matriz primero.")
            return

        self.resultado = np.array_str(np.transpose(self.get_matriz()))
        self.cuerpoOperacion = f'Matriz transpuesta de: {self.get_matriz()}'
        return self.resultado

    def producto(self):
        if self.matriz is None or self.matriz2 is None:
            print("Error: Las matrices no han sido llenadas. Por favor, llene las matrices primero.")
            return
        self.resultado = np.array_str(np.dot(self.get_matriz(), self.get_matriz2()))
        self.cuerpoOperacion = f'{self.get_matriz()} * {self.get_matriz2()}'
        return self.resultado

    def suma(self):
        if self.matriz is None or self.matriz2 is None:
            print("Error: Las matrices no han sido llenadas. Por favor, llene las matrices primero.")
            return
        self.resultado = np.array_str(np.add(self.get_matriz(), self.get_matriz2()))
        self.cuerpoOperacion = f'{self.get_matriz()} + {self.get_matriz2()}'
        return self.resultado

    def producto_escalar(self):
        if self.matriz is None:
            print("Error: La matriz no ha sido llenada. Por favor, llene la matriz primero.")
            return

        escalar = int(input("\nIngrese el número por el que desea multiplicar la matriz: "))

        self.resultado = np.array_str(np.multiply(self.get_matriz(), escalar))
        self.cuerpoOperacion = f'{self.get_matriz()} * {escalar}'
        return self.resultado
