# Criando uma lista chamada "num" com valores iniciais
num = [2, 5, 9, 1]

# Modificando o terceiro elemento da lista para 3
num[2] = 3

# Adicionando o número 7 ao final da lista
num.append(7)

# Classificando a lista em ordem decrescente
num.sort(reverse=True)

# Inserindo o número 2 na posição 2 da lista
num.insert(2, 2)

# Verificando se o número 5 está na lista
if 5 in num:
    num.remove(5)  # Se estiver, removendo-o da lista
else:
    print('Não achei o número 5')  # Se não estiver, exibindo uma mensagem

# Imprimindo a lista atualizada
print(num)

# Exibindo a quantidade de elementos na lista
print(f'Essa lista tem {len(num)} elementos')
