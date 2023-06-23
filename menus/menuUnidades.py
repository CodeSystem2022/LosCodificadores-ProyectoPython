from OperacionDAO import OperacionDAO
from UnidadLongitud import UnidadLongitud
from conversion.UnidadPeso import UnidadPeso
from conversion.UnidadTiempo import UnidadTiempo

def menuUnidades():
    while(True):
        print('MENÚ DE PASAJE DE UNIDADES')
        print('1. metro a centrimetros')
        print('2. centimetro a metro')
        print('3. metro a kilometro')
        print('4. kilometro a metro')
        print('5. kilogramo a gramo')
        print('6. gramo a kilogramo')
        print('7. kilogramo a libra')
        print('8. libra a kilogramo')
        print('9. segundo a minuto')
        print('10. minuto a hora')
        print('11. segundo a hora')
        print('12. minuto a segundo')
        print('13. hora a minuto')
        print('14. hora a segundo')
        print('15. Salir')
        
        opcion = int(input('Escriba la opcion deseada: '))

        match(opcion):
            case 1:
                valor = int(input('Ingrese los metros: '))
                operacion = UnidadLongitud()
                print(operacion.metroACentimetro(valor))
                try:
                    OperacionDAO.agregarDato(operacion)
                    print('La operación se guardo en el historial de operaciones')
                except Exception as e:
                    print(f'Ocurrio un error al intentar guardar la operacion: {e}')
            case 2:
                valor = int(input('Ingrese los centimetros: '))
                operacion = UnidadLongitud()
                print(operacion.centimetrosAMetro(valor))
                try:
                    OperacionDAO.agregarDato(operacion)
                    print('La operación se guardo en el historial de operaciones')
                except Exception as e:
                    print(f'Ocurrio un error al intentar guardar la operacion: {e}')
            case 3:
                valor = int(input('Ingrese los metros: '))
                operacion = UnidadLongitud()
                print(operacion.metrosAKilometro(valor))
                try:
                    OperacionDAO.agregarDato(operacion)
                    print('La operación se guardo en el historial de operaciones')
                except Exception as e:
                    print(f'Ocurrio un error al intentar guardar la operacion: {e}')
            case 4:
                valor = int(input('Ingrese los kilometros: '))
                operacion = UnidadLongitud()
                print(operacion.kilometrosAMetros(valor))
                try:
                    OperacionDAO.agregarDato(operacion)
                    print('La operación se guardo en el historial de operaciones')
                except Exception as e:
                    print(f'Ocurrio un error al intentar guardar la operacion: {e}')
            case 5:
                valor = int(input('Ingrese los kilogramos: '))
                operacion = UnidadPeso()
                print(operacion.kiloAGramo(valor))
                try:
                    OperacionDAO.agregarDato(operacion)
                    print('La operación se guardo en el historial de operaciones')
                except Exception as e:
                    print(f'Ocurrio un error al intentar guardar la operacion: {e}')
            case 6:
                valor = int(input('Ingrese los gramos: '))
                operacion = UnidadPeso()
                print(operacion.gramoAKilo(valor))
                try:
                    OperacionDAO.agregarDato(operacion)
                    print('La operación se guardo en el historial de operaciones')
                except Exception as e:
                    print(f'Ocurrio un error al intentar guardar la operacion: {e}')
            case 7:
                valor = int(input('Ingrese los kilogramos: '))
                operacion = UnidadPeso()
                print(operacion.kiloALibra(valor))
                try:
                    OperacionDAO.agregarDato(operacion)
                    print('La operación se guardo en el historial de operaciones')
                except Exception as e:
                    print(f'Ocurrio un error al intentar guardar la operacion: {e}')
            case 8:
                valor = int(input('Ingrese las libras: '))
                operacion = UnidadPeso()
                print(operacion.libraAKilo(valor))
                try:
                    OperacionDAO.agregarDato(operacion)
                    print('La operación se guardo en el historial de operaciones')
                except Exception as e:
                    print(f'Ocurrio un error al intentar guardar la operacion: {e}')
            case 9:
                valor = int(input('Ingrese los segundos: '))
                operacion = UnidadTiempo()
                print(operacion.segundoAMinuto(valor))
                try:
                    OperacionDAO.agregarDato(operacion)
                    print('La operación se guardo en el historial de operaciones')
                except Exception as e:
                    print(f'Ocurrio un error al intentar guardar la operacion: {e}')
            case 10:
                valor = int(input('Ingrese los minutos: '))
                operacion = UnidadTiempo()
                print(operacion.minutoAHora(valor))
                try:
                    OperacionDAO.agregarDato(operacion)
                    print('La operación se guardo en el historial de operaciones')
                except Exception as e:
                    print(f'Ocurrio un error al intentar guardar la operacion: {e}')
            case 11:
                valor = int(input('Ingrese los segundos: '))
                operacion = UnidadTiempo()
                print(operacion.segundoAHora(valor))
                try:
                    OperacionDAO.agregarDato(operacion)
                    print('La operación se guardo en el historial de operaciones')
                except Exception as e:
                    print(f'Ocurrio un error al intentar guardar la operacion: {e}')
            case 12:
                valor = int(input('Ingrese los minutos: '))
                operacion = UnidadTiempo()
                print(operacion.minutoASegundo(valor))
                try:
                    OperacionDAO.agregarDato(operacion)
                    print('La operación se guardo en el historial de operaciones')
                except Exception as e:
                    print(f'Ocurrio un error al intentar guardar la operacion: {e}')
            case 13:
                valor = int(input('Ingrese las horas: '))
                operacion = UnidadTiempo()
                print(operacion.horaAMinuto(valor))
                try:
                    OperacionDAO.agregarDato(operacion)
                    print('La operación se guardo en el historial de operaciones')
                except Exception as e:
                    print(f'Ocurrio un error al intentar guardar la operacion: {e}')
            case 14:
                valor = int(input('Ingrese las horas: '))
                operacion = UnidadTiempo()
                print(operacion.horaASegundos(valor))
                try:
                    OperacionDAO.agregarDato(operacion)
                    print('La operación se guardo en el historial de operaciones')
                except Exception as e:
                    print(f'Ocurrio un error al intentar guardar la operacion: {e}')
            case 15:
                print('Muchas gracias por usar la calculadora')
                break
            case _:
                print('Valor ingresado incorrecto')
