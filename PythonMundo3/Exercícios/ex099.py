# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

# Bibliotecas
from time import sleep

# Função que retorna o maior valor
def maior(*valores):
    print('Analisando os valores passados...')
    
    # Exibe os valores recebidos
    for valor in valores:
        print(valor, end=' ')
        sleep(0.5)
    
    # Exibe a quantidade de valores informados
    print(f'- Foram informados {len(valores)} valores ao todo.')
    
    # Caso nenhum valor seja informado, define '0' como padrão
    if len(valores) == 0:
        valores = '0'
    
    # Pausa para efeito visual
    if len(valores) > 1:
        sleep(2)
    
    # Exibe o maior valor informado
    print(f'O maior valor informado foi {max(valores)}.')
    print('-=' * 20)

# Programa Principal
print('-=' * 20)

# Testes da função maior
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
maior(
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20
    )
maior(10, 20, 30, 40, 50)
maior(100, 200, 300)
maior(5, 15, 25, 35, 45, 55, 65)