#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista

num = []

for c in range(5):
    num.append(int(input(f'Digite um número para a posição {c}: ')))

print(f'Você digitou os valores {num}')
print(f'O maior número digitado foi: {max(num)} na posição {num.index(max(num))}')
print(f'O menor número digitado foi: {min(num)} na posição {num.index(min(num))}')
