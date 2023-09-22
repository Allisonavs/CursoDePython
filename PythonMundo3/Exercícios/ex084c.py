#PROGRAMA CORRIGIDO NA VIDEO AULA

# Inicialização de variáveis
temp = []  # Lista temporária para armazenar informações de uma pessoa
princ = []  # Lista principal para armazenar informações de todas as pessoas
mai = men = 0  # Inicialização das variáveis para peso mais alto e mais baixo

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))

    # Verificando se é a primeira pessoa cadastrada
    if len(princ) == 0:
        mai = men = temp[1]  # Se for a primeira, ambos mai e men serão definidos com o peso desta pessoa
    else:
        # Verificando se o peso da pessoa atual é maior que o peso mais alto (mai)
        if temp[1] > mai:
            mai = temp[1]
        # Verificando se o peso da pessoa atual é menor que o peso mais baixo (men)
        if temp[1] < men:
            men = temp[1]

    princ.append(temp[:])  # Adicionando uma cópia dos dados da pessoa atual à lista principal
    temp.clear()  # Limpando a lista temporária para a próxima pessoa

    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break

print('-=' * 30)  # Linha de separação para melhorar a apresentação

print(f'Ao todo você cadastrou {len(princ)} pessoas.')

# Encontrando pessoas com o maior peso
print(f'O maior peso foi {mai}kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')

# Encontrando pessoas com o menor peso
print(f'\nO menor peso foi {men}kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]', end='')
