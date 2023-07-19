# Crie um programa que leia o ano de nascimento de sete pessoas
# No final, mostre quantas pessoas ainda não atingiram a maioridade
# e quantas já são maiores.

#Importo as bibliotecas a qual serão usadas
from datetime import date

#É criada as variáveis para a contagem de quantos são maiores de idade e quantos são menores de idade
maior = 0
menor = 0

#É criado o laço de repetição para perguntar o ano de nascimento das pessoas
for pess in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento da {pess} pessoa: '))
    idade = date.today().year - ano    # De acordo com o ano atual, é calculada a idade da pessoa
    if idade >= 21:                    # Se a idade da pessoa for maior ou igual a 21, ela é maior de idade
        maior += 1
    else:                              # Se não, ela é menor de idade
        menor += 1

#O programa exibe ao usuário o resultado de quantos são maiores e quantos são menores
print(f'Maiores de idade: {maior}')
print(f'Menores de idade: {menor}')
