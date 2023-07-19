# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
# daqueles que forem pares. Se o valor digitado for impar, desconsidere-o

#Crio a variavel de soma, contagem, e contagem total
s = 0
cont = 0
conttotal = 0

#O laço é criado
for c in range(1, 7):
    n = int(input(f'Digite o {c} valor: '))
    conttotal += 1
    if n % 2 == 0:
        s += n
        cont += 1
print(f'Somando apenas os {cont} números pares dos {conttotal} digitados, \no resultado é igual a {s}')
