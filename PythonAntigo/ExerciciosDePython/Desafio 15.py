dias = int(input('Quantos dias você ficou com o carro? '))
km = float(input('Quantos Km foram rodados? '))
print(f'Você deverá pagar R${((dias*60) + (km*0.15)):.2f}')