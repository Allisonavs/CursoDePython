# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
# digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados
# e qual foi a soma entre eles (desconsiderando o flag).

#Inicio as variáveis
cont = soma = 0

#Crio um laço de repetição infinito
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:        # Se n for igual a 999, o programa para
        break
    soma += n
    cont += 1
print(f'Foram digitados {cont} números')
print(f'A soma total desses números é {soma}')
