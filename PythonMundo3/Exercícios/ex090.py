# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela

dados = {'Nome': '', 'Media': 0, 'Situação': ''}

dados['Nome'] = str(input('Nome: '))
dados['Media'] = float(input(f'Média de {dados["Nome"]}: '))

if dados['Media'] >= 7.0:
    dados['Situação'] = 'Aprovado'
elif 7.0 > dados['Media'] >= 5.0:
    dados['Situação'] = 'Recuperação'
elif dados['Media'] < 5.0:
    dados['Situação'] = 'Reprovado'

print(f'Nome é igual a {dados["Nome"]}')
print(f'Média é igual a {dados["Media"]}')
print(f'Situação é igual a {dados["Situação"]}')
