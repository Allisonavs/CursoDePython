# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

#O programa pede que o usuário digite as duas notas do aluno

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))

#O programa calcula a média do aluno e mostra para o usuário

m = (n1 + n2) / 2
print(f'A média do aluno foi de {m:.1f}')

#O programa indica se o aluno se encontra REPROVADO, em RECUPERAÇÃO ou se ele está APROVADO

if m < 5.0:
    print('O aluno está REPROVADO')
elif 6.9 >= m >= 5.0:
    print('O aluno está de RECUPERAÇÃO')
elif m >= 7.0:
    print('O aluno está APROVADO')
