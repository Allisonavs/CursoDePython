# Criando uma lista vazia chamada "valores"
valores = list()

# Solicitando ao usuário inserir 5 valores e adicionando-os à lista "valores"
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

# Iterando sobre a lista "valores" usando a função "enumerate" para obter a posição (pos) e o valor
for pos, valor in enumerate(valores):
    print(f'Na posição {pos} encontrei o valor {valor}')

# Exibindo uma mensagem para indicar o fim da lista
print('Cheguei ao final da lista')
