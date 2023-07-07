# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
# preço normal e condição de pagamento:
# -À vista dinheiro/cheque: 10% de desconto
# -À vista no cartão: 5% de desconto
# -Em até 2x no cartão: preço normal
# -3x ou mais no cartão: 20% de juros

#Menu inicial da loja

print('--------------LOJAS ALLISON--------------')

#O programa pergunta o valor dos produtos

pc = float(input('Preço das compras: R$'))

#Pergunta ao usuário qual será a forma de pagamento

print('Qual vai ser a forma de pagamento?')
print(' [1] - À vista no dinheiro ou cheque\n'
      ' [2] - À vista no cartão\n'
      ' [3] - Parcelado no cartão')
op = input()

#De acordo com a opção escolhida pelo cliente, indica o valor que sairá as compras, caso parcele, o programa pergunta
#em quantas parcelas será paga as compras

if op == '1':
    cd = pc - (pc * 0.10)
    print(f'As compras sairão por R${cd:.2f}')
elif op == '2':
    cd = pc - (pc * 0.05)
    print(f'As compras sairão por R${cd:.2f}')
elif op == '3':
    np = int(input('Deseja parcelar em quantas vezes? '))
    if np <= 2:
        print(f'As compras sairão por R${pc:.2f}')
    elif np > 2:
        cd = pc + (pc * 0.20)
        cdp = cd / np
        print(f'COM JUROS as compras sairão por R${cd:.2f} com parcelas de R${cdp:.2f}')
else:
    print('Você não escolheu uma opção válida!')
