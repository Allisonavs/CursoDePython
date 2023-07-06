d = float(input("Qual a distância da viagem? "))
print(f'Você está prestes a começar uma viagem de {d:.2f}KM')
if d <= 200:
    v = d * 0.5
else:
    v = d * 0.45
print(f"O valor da sua viagem será de R${v:.2f}")
