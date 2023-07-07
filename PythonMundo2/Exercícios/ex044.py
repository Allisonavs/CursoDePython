# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
# preço normal e condição de pagamento:
# -À vista dinheiro/cheque: 10% de desconto
# -À vista no cartão: 5% de desconto
# -Em até 2x no cartão: preço normal
# -3x ou mais no cartão: 20% de juros

#O programa anuncia o valor do produto

print('Geladeira Abluble por apenas R$2.450!!!')

#Pergunta ao usuário qual será a forma de pagamento

print('Qual vai ser a forma de pagamento?')
print(' 1 - À vista no dinheiro ou cheque\n'
      ' 2 - À vista no cartão\n'
      ' 3 - Parcelado no cartão')
op = input()

if op == '1':
    cd = 2450 - (2450 * 0.10)
    print(f'A geladeira sairá por R${cd:.2f}')
elif op == '2':
    cd = 2450 - (2450 * 0.05)
    print(f'A geladeira sairá por R${cd:.2f}')
elif op == '3':
    np = int(input('Deseja parcelar em quantas vezes? '))
    if np <= 2:
        print('A geladeira sairá por R$2450.00')
    elif np > 2:
        cd = 2450 + (2450 * 0.20)
        cdp = cd / np
        print(f'A geladeira sairá por R${cd:.2f} com parcelas de R${cdp:.2f}')
else:
    print('Você não escolheu uma opção válida!')
