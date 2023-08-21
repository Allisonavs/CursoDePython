# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário
# O programa será interrompido quando o número solicitado for negativo


#Inicia o laço de repetição
while True:
    print('-'*50)
    n = int(input('Digite um número para ver sua tabuada: '))
    print('-'*50)
    if n < 0:       # Se o número digitado for negativo, para o programa
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
print('Programa de tabuada ENCERRADO!')