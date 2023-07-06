#Faça um programa que leia o conprimento do cateto oposto e do cateto adjacente
#de um triâmgulo, calcule e mostre o comprimento da hipotenusa

from math import hypot
co = float(input('De o comprimento do cateto oposto: '))
ca = float(input('De o comprimento do cateto adjacente: '))
print(f'A hipotenusa é igual a: {(hypot(co, ca)):.2f}')
