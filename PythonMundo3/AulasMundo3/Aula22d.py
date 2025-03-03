def parOuImpar(n=0):
    if n % 2 == 0:
        return 'Par'
    else:
        return 'Impar'
    
num = int(input('Digite um número: '))
print(f'O número {num} é {parOuImpar(num)}')
