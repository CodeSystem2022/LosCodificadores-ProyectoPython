from operacion.OperacionDAO import OperacionDAO
# from figuras.Rectangulo import Rectangulo

def menuFigurasGeometricas():
    while(True):
        print('MENÚ DE FIGURA GEOMETRICAS')
        print('1. rectangulo')
        print('2. cuadrado')
        print('3. circulo')
        print('4. Salir')
        
        opcion = int(input('Escriba la opcion correspondiente a la figura a trabajar: '))

        match(opcion):
            case 1:
                base = int(input('Ingrese la base del rectangulo: '))
                altura = int(input('Ingrese la alura del rectangulo: '))
                while(True):
                    print('MENU RECTANGULO')
                    print('1. area')
                    print('2. perimetro')
                    print('3. salir')
                    opcionRectangulo = int(input('Escriba que operación desea realizar: '))
                    match(opcionRectangulo):
                        case 1:
                            operacion = Rectangulo(base, altura)
                            print(operacion.area())
                            try:
                                OperacionDAO.agregarDato(operacion)
                                print('La operación se guardo en el historial de operaciones')
                            except Exception as e:
                                print(f'Ocurrio un error al intentar guardar la operacion: {e}')
                        case 2:
                            operacion = Rectangulo(base, altura)
                            print(operacion.perimetro())
                            try:
                                OperacionDAO.agregarDato(operacion)
                                print('La operación se guardo en el historial de operaciones')
                            except Exception as e:
                                print(f'Ocurrio un error al intentar guardar la operacion: {e}')
                        case 3: 
                            break
                        case _:
                            print('Ingrese una opcion válida')
            case 2:
                    lado = int(input('Ingrese el lado del cuadrado: '))
                    while(True):
                        print('MENU CUADRADO')
                        print('1. area')
                        print('2. perimetro')
                        print('3. salir')
                        opcionCuadrado = int(input('Escriba que operación desea realizar: '))
                        match(opcionCuadrado):
                            case 1:
                                operacion = Cuadrado(base, altura)
                                print(operacion.area())
                                try:
                                    OperacionDAO.agregarDato(operacion)
                                    print('La operación se guardo en el historial de operaciones')
                                except Exception as e:
                                    print(f'Ocurrio un error al intentar guardar la operacion: {e}')
                            case 2:
                                operacion = Rectangulo(base, altura)
                                print(operacion.perimetro())
                                try:
                                    OperacionDAO.agregarDato(operacion)
                                    print('La operación se guardo en el historial de operaciones')
                                except Exception as e:
                                    print(f'Ocurrio un error al intentar guardar la operacion: {e}')
                            case 3: 
                                break
                            case _:
                                print('Ingrese una opcion válida')
            case 3:
                lado = int(input('Ingrese el radio del circulo: '))
                while(True):
                        print('MENU CIRCULO')
                        print('1. area')
                        print('2. perimetro')
                        print('3. salir')
                        opcionCuadrado = int(input('Escriba que operación desea realizar: '))
                        match(opcionCuadrado):
                            case 1:
                                operacion = Circulo(base, altura)
                                print(operacion.area())
                                try:
                                    OperacionDAO.agregarDato(operacion)
                                    print('La operación se guardo en el historial de operaciones')
                                except Exception as e:
                                    print(f'Ocurrio un error al intentar guardar la operacion: {e}')
                            case 2:
                                operacion = Rectangulo(base, altura)
                                print(operacion.perimetro())
                                try:
                                    OperacionDAO.agregarDato(operacion)
                                    print('La operación se guardo en el historial de operaciones')
                                except Exception as e:
                                    print(f'Ocurrio un error al intentar guardar la operacion: {e}')
                            case 3: 
                                break
                            case _:
                                print('Ingrese una opcion válida')      
            case 4:
                print('Muchas gracias por usar la calculadora')
                break
            case _:
                print('Valor ingresado incorrecto')