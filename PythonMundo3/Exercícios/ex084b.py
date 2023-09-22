# PROGRAMA COM DECLARAÇÕES DEMAIS NO INICIO

# Inicializando listas vazias para armazenar informações das pessoas.
pessoas = list()         # Lista para todas as pessoas cadastradas.
dado = list()            # Lista temporária para armazenar dados de uma pessoa.
pessoas_pesadas = list() # Lista para pessoas com peso igual ou superior a 100.
pessoas_leves = list()   # Lista para pessoas com peso menor ou igual a 70.
contador = 0             # Contador para acompanhar o número de pessoas cadastradas.
peso_mais_leve = float('inf')  # Peso mais leve inicializado com infinito.
pessoa_peso_mais_leve = list()     # Lista para armazenar pessoas com o peso mais leve.
peso_mais_pesado = float('-inf')  # Peso mais pesado inicializado com negativo infinito.
pessoa_peso_mais_pesado = list()     # Lista para armazenar pessoas com o peso mais pesado.

# Loop infinito para cadastrar pessoas até que o usuário decida parar.
while True:
    # Solicita o nome e peso da pessoa.
    dado.append(str(input('Nome: ')))
    peso = float(input('Peso: '))
    dado.append(peso)

    # Verifica se o peso é o mais leve ou o mais pesado até agora.
    if peso <= 70:
        pessoas_leves.append(dado[:])   # Adiciona informações de pessoa leve à lista.
        if peso == peso_mais_leve:
            pessoa_peso_mais_leve.append(dado[0])
        elif peso < peso_mais_leve:
            peso_mais_leve = peso
            pessoa_peso_mais_leve = [dado[0]]
    elif peso >= 100:
        pessoas_pesadas.append(dado[:]) # Adiciona informações de pessoa pesada à lista.
        if peso == peso_mais_pesado:
            pessoa_peso_mais_pesado.append(dado[0])
        elif peso > peso_mais_pesado:
            peso_mais_pesado = peso
            pessoa_peso_mais_pesado = [dado[0]]

    pessoas.append(dado[:]) # Adiciona informações de pessoa à lista principal.
    dado.clear()            # Limpa a lista temporária para a próxima entrada.
    contador += 1           # Incrementa o contador de pessoas cadastradas.

    # Pergunta ao usuário se deseja continuar cadastrando pessoas.
    escolha = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if escolha == 'N':
        break

# Exibe o número total de pessoas cadastradas e as listas de pessoas pesadas e leves.
print(f'Foram cadastradas {contador} pessoas')

if pessoas_leves:
    print(f'O peso mais leve encontrado foi {peso_mais_leve} kg, e as pessoas com esse peso são: {", ".join(pessoa_peso_mais_leve)}')

if pessoas_pesadas:
    print(f'O peso mais pesado encontrado foi {peso_mais_pesado} kg, e as pessoas com esse peso são: {", ".join(pessoa_peso_mais_pesado)}')
