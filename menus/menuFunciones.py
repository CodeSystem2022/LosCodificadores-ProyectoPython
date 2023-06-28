from operacion.OperacionDAO import OperacionDAO
from funciones.ClaseFuncionesMatematicas import FuncionesMatematicas

def menuFunciones():
    while (True):
        print('MENÚ DE FUNCIONES')
        print('1. Teorema de Pitagoras')
        print('2. Raices cuadráticas')
        print('3. Salir')

        opcion = int(input('Escriba la opcion que necesite: '))

        match(opcion):
            case 1:
                while (True):
                    print('MENU PITAGORAS')
                    print('1. hipotenusa')
                    print('2. cateto a')
                    print('3. cateto b')
                    print('4. salir')

                    opcionPitagoras = int(
                        input('¿Que valor desea encontrar?: '))
                    match(opcionPitagoras):
                        case 1:
                            operacion = FuncionesMatematicas()
                            print(operacion.pitagorasHipotenusa())
                            try:
                                OperacionDAO.agregarDato(operacion)
                                print(
                                    'La operación se guardo en el historial de operaciones')
                            except Exception as e:
                                print(
                                    f'Ocurrio un error al intentar guardar la operacion: {e}')
                        case 2:
                            operacion = FuncionesMatematicas()
                            print(operacion.pitagorasCatetoA())
                            try:
                                OperacionDAO.agregarDato(operacion)
                                print(
                                    'La operación se guardo en el historial de operaciones')
                            except Exception as e:
                                print(
                                    f'Ocurrio un error al intentar guardar la operacion: {e}')
                        case 3:
                            operacion = FuncionesMatematicas()
                            print(operacion.pitagorasCatetoB())
                            try:
                                OperacionDAO.agregarDato(operacion)
                                print(
                                    'La operación se guardo en el historial de operaciones')
                            except Exception as e:
                                print(
                                    f'Ocurrio un error al intentar guardar la operacion: {e}')
                        case 4:
                            break
                        case _:
                            print('Ingrese una opcion válida')
            case 2:
                operacion = FuncionesMatematicas()
                print(operacion.raicesCuadraticas())
                try:
                    OperacionDAO.agregarDato(operacion)
                    print('La operación se guardo en el historial de operaciones')
                except Exception as e:
                    print(
                        f'Ocurrio un error al intentar guardar la operacion: {e}')
            case 3:
                break
            case _:
                print('Ingrese una opcion válida')