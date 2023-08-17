# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

#Defino as variaveis que serão usadas
total = 0
flag = ''
cont = 0

#É criado o laço de repetição
while flag != 'end':
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:        # Se for diferente de 999, o programa somará o número no total e adiciona 1 no contador
        total += n
        cont += 1
    else:               # Se não, o flag receberá o sinal de parada
        flag = 'end'

#O programa mostra quantos números foram digitados e a soma de todos eles, desconsiderando o flag
print(f'A soma entre os {cont} números digitados é igual a {total}')
