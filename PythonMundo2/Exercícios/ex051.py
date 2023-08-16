# Desenvolva um programa que leia o primeiro termo e a razão de uma PA
# No final, mostre os 10 primeiros termos dessa progressão

pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))

#Usando for:
for c in range(10):
    termo = pt + c * r
    print(termo, end=' -> ')
print('FIM')
