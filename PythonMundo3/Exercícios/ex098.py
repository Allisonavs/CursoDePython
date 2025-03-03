# Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo e realize a contagem.
# Seu programa tem que realizar três contagens através da função criada:
# a) De 1 até 10, de 1 em 1
# b) De 10 até 0, de 2 em 2
# c) Uma contagem personalizada

# Bibliotecas
from time import sleep

# Função que conta de início até fim de passo em passo
def contador(inicio, fim, passo):
    '''
    Realiza uma contagem de números de acordo com os parâmetros fornecidos.
    Parâmetros:
    inicio (int): O número inicial da contagem.
    fim (int): O número final da contagem.
    passo (int): O intervalo entre os números na contagem. Se for 0, será ajustado para 1 ou -1 dependendo da direção da contagem.
    A função ajusta automaticamente o passo e o fim para garantir que a contagem seja realizada corretamente, seja ela crescente ou decrescente. 
    Exibe cada número da contagem com um intervalo de 0.5 segundos entre eles.
    '''
    
    # Exibe a contagem
    escreva(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(1)

    # Ajusta o passo se for 0
    if passo == 0:
        if inicio < fim:
            passo = 1
        else:
            passo = -1
    
    # Ajusta o passo e o fim para contagem crescente
    if inicio < fim:
        if passo < 0:
            passo = -passo
        fim += 1

    # Ajusta o passo e o fim para contagem decrescente
    elif inicio > fim:
        if passo > 0:
            passo = -passo
        fim -= 1
    
        
    # Realiza a contagem
    for i in range(inicio, fim, passo):
        print(i, end=' ')
        sleep(0.5)

# Função para escrever uma mensagem formatada
def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(msg.center(tam))
    print('~' * tam)

# Programa Principal

# Contagem de 1 até 10 de 1 em 1
sleep(1)
contador(1, 10, 1)
print()
sleep(1)

# Contagem de 10 até 0 de 2 em 2
sleep(1)
contador(10, 0, -2)
print()
sleep(1)

# Contagem personalizada
escreva('Contagem personalizada:')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

# Contagem personalizada de início até fim de passo em passo
contador(inicio, fim, passo)
