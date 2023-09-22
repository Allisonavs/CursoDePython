# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um
# boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente

ficha = list()  # Inicializa uma lista vazia chamada 'ficha' para armazenar informações dos alunos.

while True:
    nome = str(input('Nome: '))  # Solicita o nome do aluno.
    nota1 = float(input('Nota 1: '))  # Solicita a primeira nota do aluno.
    nota2 = float(input('Nota 2: '))  # Solicita a segunda nota do aluno.

    media = (nota1 + nota2) / 2  # Calcula a média das duas notas.

    # Adiciona as informações do aluno como uma lista dentro da lista 'ficha'.
    ficha.append([nome, [nota1, nota2], media])

    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break  # Se a resposta for 'N' ou 'n', encerra o loop.

print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)

# Itera sobre a lista 'ficha' e exibe o número do aluno, nome e média.
for i, aluno in enumerate(ficha):
    print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))

    if opc == 999:
        print('FINALIZANDO...')
        break  # Se a opção for 999, encerra o loop.

    if opc <= len(ficha) - 1:
        # Exibe as notas do aluno escolhido com base na posição na lista 'ficha'.
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')

print('<<< VOLTE SEMPRE >>>')
