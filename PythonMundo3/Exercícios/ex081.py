#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente
#C) Se o valor 5 foi digitado e está ou não na lista

num = []
cont = 0


while True:
    num.append(int(input('Digite um número: ')))
    cont += 1

    escolha = input('Deseja continuar? [S/N] ').upper().strip()[0]

    while escolha not in 'SN':
        escolha = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if escolha == 'N':
        break


print(f'Foram digitados {cont} números')
num.sort(reverse=True)
print(f'Lista em ordem descrescente: {num}')
if 5 in num:
    print('Foi digitado o número 5, ele está na lista')
else:
    print('Não, o número 5 não foi digitado, ele não está na lista')
