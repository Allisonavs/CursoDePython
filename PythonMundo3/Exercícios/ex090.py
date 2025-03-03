# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela

# Criando um dicionário para armazenar informações do aluno
aluno = dict()

# Solicitando e armazenando o nome do aluno
aluno['nome'] = str(input("Aluno: ")).title()

# Solicitando e armazenando a média do aluno
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))

# Determinando a situação do aluno com base na média
if aluno['média'] >= 7.0:
    aluno['situação'] = 'Aprovado'
elif aluno['média'] >= 5.0:
    aluno['situação'] = 'Recuperação'
elif aluno['média'] < 5.0:
    aluno['situação'] = 'Reprovado'

# Exibindo as informações do aluno
for k, v in aluno.items():
    print(f'  - {k.title()} é igual a {v}')

