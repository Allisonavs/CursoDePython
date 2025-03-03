def contador(* num):
    tam = len(num)
    print(f'Recebi os valores ', end='')
    for i, valor in enumerate(num):
        if i == tam - 1:
            print(f'{valor}', end=' ')
        else:
            print(f'{valor}', end=', ')
    print(f'e são ao todo {tam} números.')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)