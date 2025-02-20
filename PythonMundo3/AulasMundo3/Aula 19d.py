estado = dict()  # Cria um dicionário vazio para armazenar os estados
brasil = list()  # Cria uma lista vazia para armazenar os dicionários de estados

for c in range(3):
    estado['uf'] = str(input('Unidade Federativa: '))  # Solicita a unidade federativa e armazena no dicionário
    estado['sigla'] = str(input('Sigla do Estado: '))  # Solicita a sigla do estado e armazena no dicionário
    brasil.append(estado.copy())  # Adiciona uma cópia do dicionário à lista

for e in brasil:
    print(f"{e['uf']} - {e['sigla']}")  # Imprime a unidade federativa e a sigla de cada estado na lista