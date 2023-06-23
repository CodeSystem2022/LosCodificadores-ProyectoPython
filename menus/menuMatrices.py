def menuMatrices():
    while(True):
        print('MENÚ DE MATRICES')
        print('1. Matriz traspuesta')
        print('2. Matriz escalar')
        print('3. Suma de matrices')
        print('4. Producto de una matriz')
        print('5. Salir')
        
        opcion = int(input('Escriba la opcion correspondiente a la figura a trabajar: '))
        match(opcion):
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                break
            case _:
                print('Ingrese una opción válida')