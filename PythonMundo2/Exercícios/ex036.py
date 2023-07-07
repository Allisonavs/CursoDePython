# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa
# O programa vai perguntar o *valor da casa*, o *salário* do comprador e em *quantos anos*
# ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder
# 30% do salário ou então o empréstimo será negado

# Definindo as variáveis
vc = float(input('Valor da casa: R$'))
s = float(input('Salário: R$'))
a = int(input('Em quantos anos deseja pagar? '))

# Calculando a prestação mensal
pm = vc / (a*12)

# Calculando se o valor das parcelas excedem 30% do salário
tps = s * 0.30
if pm > tps:
    print('Não será possível efetuar o empréstimo, pois o valor das parcelas excedem o valor de 30% do salário')
else:
    print(f'O valor das parcelas serão de R${pm:.2f}')
