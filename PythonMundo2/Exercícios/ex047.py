# Crie um programa que mostre na tela todos os números pares
# que estão no intervalo entre 1 e 50


#Crio o laço de repetição, usando apenas o for
'''for c in range(2, 51, 2):
    print(c)'''

#Crio o laço de repetição, porém, verificando se o número realmente é par
for c in range(1, 51):
    if c % 2 == 0:  # Verifica se o número é par
        print(c)
