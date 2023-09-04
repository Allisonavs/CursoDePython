# Criando uma lista "a" com alguns valores iniciais
a = [2, 3, 4, 7]

# Criando uma cópia da lista "a" usando a técnica de "slicing" (cópia por fatia)
b = a[:]

# Modificando o terceiro elemento da lista "b" para 8
b[2] = 8

# Imprimindo a lista "a" original
print(f'Lista A: {a}')

# Imprimindo a lista "b" modificada

print(f'Lista B: {b}')


# Fatiamento com Listas:

# Exemplo 1: Criando uma nova lista com elementos de índice 1 até 3 (exclusivo)
lista = [0, 1, 2, 3, 4, 5]
nova_lista = lista[1:3]
print(nova_lista)  # Resultado: [1, 2]

# Exemplo 2: Selecionando todos os elementos ímpares
lista = [0, 1, 2, 3, 4, 5]
impares = lista[1::2]
print(impares)  # Resultado: [1, 3, 5]

# Exemplo 3: Invertendo uma string
texto = "Python"
invertido = texto[::-1]
print(invertido)  # Resultado: "nohtyP"

