#Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.

# Função que calcula a área de um terreno
def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno de {largura:.2f}m x {comprimento:.2f}m é de {a:.2f}m².')

# Main Program

# Pede ao usuário as dimensões do terreno
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))

# Chama a função area()
area(largura, comprimento)
