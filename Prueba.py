import os
while True:
    a = input('\tBienvenido, si desea continuar presione enter...\n\tsi desea salir presione E...\n')
    if a == "":
        b = '';
        b = input('\tIngrese el nombre de la persona: ')
        last = b[-1]
        if last == 'a' or last == 'A':
            print('\n\tEl nombre ingresado es Mujer\n');
            input('\n\tpresine enter par continuar...\n')
        else:
            print('\n\tEl nombre ingresado es Hombre\n');
            input('\n\tpresine enter par continuar...\n')
    elif a == 'E' or a == 'e':
        break
    else:
        print('\n\tError, seleccione Enter o E...\n')
        os.system('cls')
