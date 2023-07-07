# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status,
# de acordo com a tabela abaixo:
# -Abaixo de 18.5: Abaixo do Peso
# -Entre 18.5 e 25: Peso ideal
# -25 até 30: Sobrepeso
# -30 até 40: Obesidade
# -Acima de 40: Obesidade Mórbida

#O programa pede as informações corporeas do usuário

peso = float(input('Peso (Kg): '))
alt = float(input('Altura (m): '))

#O programa calcula o IMC desse usuário

IMC = peso / (alt**2)

#O programa indica ao usuário o IMC e o status

print(f'Com o IMC de {IMC:.1f} na tabela se encaixa em:')
if IMC <= 18.5:
    print('Abaixo do Peso')
elif 25 >= IMC > 18.5:
    print('Peso Ideal')
elif 30 >= IMC > 25:
    print('Sobrepeso')
elif 40 >= IMC > 30:
    print('Obesidade')
elif IMC > 40:
    print('Obesidade Mórbida')
