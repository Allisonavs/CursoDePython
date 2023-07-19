# Faça um programa que calcule a soma entre todos os números impares
# que são múltiplos de três e que se encontram no intervalo de 1 até 500

#Crio a variavel de soma e contador
soma = 0
cont = 0

#Crio o laço de repetição usando o if para saber se ele é impar e multiplo de 3
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1   # Cont = ele mesmo + 1
        soma += c   # Soma = ele mesmo + c

#Mostro para o usuário o resultado
print(f'A soma total de todos os {cont} valores solicitados é {soma}')
