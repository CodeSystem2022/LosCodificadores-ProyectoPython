from operacion.OperacionDAO import OperacionDAO
from matrices.ClaseMatrices import Matrices


def menuMatrices():
    while (True):
        print('MENÚ DE MATRICES')
        print('1. Matriz traspuesta')
        print('2. Matriz escalar')
        print('3. Suma de matrices')
        print('4. Producto de una matriz')
        print('5. Salir')

        opcion = int(
            input('Escriba la opcion correspondiente a la figura a trabajar: '))
        match(opcion):
            case 1:
                operacion = Matrices()
                operacion.llenar_matrices('transpuesta')
                print(operacion.transpuesta())
                try:
                    OperacionDAO.agregarDato(operacion)
                    print('La operación se guardo en el historial de operaciones')
                except Exception as e:
                    print(f'Ocurrio un error al intentar guardar la operacion: {e}')
            case 2:
                operacion = Matrices()
                operacion.llenar_matrices('escalar')
                print(operacion.producto_escalar())
                try:
                    OperacionDAO.agregarDato(operacion)
                    print('La operación se guardo en el historial de operaciones')
                except Exception as e:
                    print(f'Ocurrio un error al intentar guardar la operacion: {e}')
            case 3:
                operacion = Matrices()
                operacion.llenar_matrices('suma')
                print(operacion.suma())
                try:
                    OperacionDAO.agregarDato(operacion)
                    print('La operación se guardo en el historial de operaciones')
                except Exception as e:
                    print(f'Ocurrio un error al intentar guardar la operacion: {e}')
            case 4:
                operacion = Matrices()
                operacion.llenar_matrices('producto')
                print(operacion.producto())
                try:
                    OperacionDAO.agregarDato(operacion)
                    print('La operación se guardo en el historial de operaciones')
                except Exception as e:
                    print(f'Ocurrio un error al intentar guardar la operacion: {e}')
            case 5:
                break
            case _:
                print('Ingrese una opción válida')