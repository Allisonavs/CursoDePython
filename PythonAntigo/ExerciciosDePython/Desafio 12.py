p = float(input('Qual o valor do produto? R$'))
print(f'Esse produto pago à vista fica com 5% de desconto e estará custando R${p - (p*5/100):.2f}')
print(f'Esse produto pago apartir de 10x no cartão de crédito, receberá 9.3% de aumento e passará a custar R${p+(p*9.3/100):.2f}')
