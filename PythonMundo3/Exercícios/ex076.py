#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos_precos = (
    "Camiseta", 29.99,
    "Calça Jeans", 59.90,
    "Tênis Esportivo", 99.50,
    "Bolsa de Couro", 79.99,
    "Relógio Analógico", 149.75,
    "Óculos de Sol", 39.99,
    "Chapéu de Palha", 19.50,
    "Sapato Social", 89.99,
    "Perfume Floral", 69.95,
    "Shorts Jeans", 34.75
)

print('-='*20)
print(f'{"Loja Super Tesoura de Cobre":^40}')
print('-='*20)

for pos, pro in enumerate(produtos_precos):
    if pos % 2 == 0:
        print(f'{produtos_precos[pos]:.<30}', end='')
    if pos % 2 == 1:
        print(f'R${produtos_precos[pos]:>.2f}')

print('-='*20)