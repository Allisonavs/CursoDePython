v = float(input('Qual é a velocidade do carro? '))
if v < 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    multa = ((v-80)*7)
    print('MULTADO! Você excedeu o limite de 80KM/h')
    print(F'Você deve pagar uma multa de R${multa:.2f}!')
