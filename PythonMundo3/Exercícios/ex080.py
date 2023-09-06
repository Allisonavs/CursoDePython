#Crie um programa onde o usuário possa digitar cinco valores númericos e cadastre-os em um alista,
#já na posição correta de inserção (sem usar o sort())
#No final, mostre a lista ordenada na tela

# Inicializa uma lista vazia.
lista = []

# Loop para receber 5 valores do usuário.
for c in range(5):
    # Solicita ao usuário que digite um valor e o converte para inteiro.
    n = int(input('Digite um valor: '))

    # Verifica se é o primeiro valor inserido ou se o valor atual é maior do que o último valor na lista.
    if c == 0 or n > lista[-1]:
        # Adiciona o valor no final da lista.
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        # Inicializa a posição como 0.
        pos = 0

        # Enquanto a posição for menor do que o comprimento da lista.
        while pos < len(lista):
            # Verifica se o valor é menor ou igual ao valor na posição atual da lista.
            if n <= lista[pos]:
                # Insere o valor na posição atual da lista.
                lista.insert(pos, n)
                # Exibe a mensagem informando a posição onde o valor foi inserido.
                print(f'Adicionado na posição {pos} da lista')
                # Sai do loop while.
                break
            pos += 1

# Exibe a lista completa após o loop.
print(f'Os valores digitados em ordem foram {lista}')
