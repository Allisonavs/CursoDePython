s = float(input("Insira o salário do funcionário: R$"))
if s > 1250:
    ns = (s*0.10)+s
else:
    ns = (s*0.15)+s
print(f'O novo salário desse funcionário será de: R${ns:.2f}')
