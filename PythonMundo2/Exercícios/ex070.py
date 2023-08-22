# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar
# No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000
# C) Qual é o nome do produto mais barato


# Início das variáveis
total_gasto = 0         # Armazena o total gasto pelo usuário
produtos_acima_1000 = 0 # Contador de produtos com preço maior que R$1000
produto_mais_barato_nome = ''  # Nome do produto mais barato encontrado
preco_mais_barato = float('inf')  # Inicializa o preço do produto mais barato com um valor infinitamente grande

#Telá inicial
print('-'*30)
print(f'{"LOJA SUPER BARATÃO":^30}')
print('-'*30)

# Inicia o laço de repetição infinito
while True:
    nome_produto = input('Produto: ')
    preco_produto = float(input('Preço: R$'))
    total_gasto += preco_produto  # Adiciona o preço do produto ao total gasto
    print('-='*15)

    if preco_produto > 1000:
        produtos_acima_1000 += 1

    if preco_produto < preco_mais_barato:
        produto_mais_barato_nome = nome_produto
        preco_mais_barato = preco_produto

    escolha = input('Deseja continuar? [S/N] ').upper().strip()[0]
    while escolha not in 'SN':
        print('Resposta Inválida. Tente novamente')
        escolha = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print('-' * 30)
    if escolha == 'N':
        break

# Exibe os resultados ao usuário
print(f'Total gasto: \033[32mR${total_gasto:.2f}\033[m')
print(f'Produtos que custam mais de R$1000: \033[32m{produtos_acima_1000}\033[m')
print(f'Produto mais barato: \033[32m{produto_mais_barato_nome}\033[m que custou \033[32mR${preco_mais_barato:.2f}\033[m')
