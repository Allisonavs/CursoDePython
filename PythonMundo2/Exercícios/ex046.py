# Faça um programa que mostre na tela uma contagem regressiva para
# o estouro de fogos de artifício, inde de 10 até 0, com uma pausa de 1 segundo
# entre eles

from time import sleep
from emoji import emojize

#Crio o laço de repetição da contagem

for cr in range(10, -1, -1):
    print(cr)
    sleep(1)

#O programa escreve na tela a mensagem

print(emojize(':fireworks: HAPPY NEW YEAR! :fireworks:'))
