# Faça um programa que calcule a soma entre todos os números impares
# que são múltiplos de três e que se encontram no intervalo de 1 até 500

#Crio a variavel de soma
s = 0

#Crio o laço de repetição usando o if para saber se ele é impar e multiplo de 3
for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:
        s = c + s

#Mostro para o usuário o resultado
print(f'A soma total é {s}')
