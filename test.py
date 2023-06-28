from menus.menuFigurasGeometricas import menuFigurasGeometricas
from menus.menuFunciones import menuFunciones
from menus.menuMatrices import menuMatrices
from menus.menuUnidades import menuUnidades
from operacion.OperacionDAO import OperacionDAO

def pantallaInicio():
    while (True):
        print('¡¡BIENVENIDO!!')
        print('CALCULADORA 2.0')
        print('1. Conversiones')
        print('2. Figuras Geometricas')
        print('3. Matrices')
        print('4. Funciones')
        print('5. Historial de operaciones')
        print('6. Salir')

        opcion = int(input('Escriba la opcion deseada: '))

        match (opcion):
            case 1:
                menuUnidades()
            case 2:
                menuFigurasGeometricas()
            case 3:
                menuMatrices()
            case 4:
                menuFunciones()
            case 5:
                try:
                    operaciones = OperacionDAO.obtenerDatos()
                    for operacion in operaciones:
                        print(operacion)
                except Exception as e:
                    print(f'Ocurrio un problema al intentar traer los datos desde la BD: {e}')
            case 6:
                print('Gracias por utilizar nuestra calculadora')
                print('Alumnos de la Tecnicatura en Programación')
                print('Cecilia Iribarren')
                print('Giuliana Gaffoglio')
                print('Guillermo Quinteros')
                print('Nicolas Aranibar')
                print('Agustin Vera')
                break
            case _:
                print('Ingrese una opción correcta')

pantallaInicio()