#Faça um programa que leia um ângulo qualquer e mosre na tela o valor do
#seno, cosseno e tangente desse ângulo

from math import sin, cos, tan, radians
ang = float(input('Digite o ângulo que você deseja: '))
print(f'O seu SENO é {(sin(radians(ang))):.2f} \nO seu COSSENO É {(cos(radians(ang))):.2f} \nA sua TANGENTE é {(tan(radians(ang))):.2f}')
