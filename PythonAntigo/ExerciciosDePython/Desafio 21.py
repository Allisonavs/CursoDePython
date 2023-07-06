#Faça um programa em PythonAntigo que abra e reproduza o áudio de um arquivo MP3

"""pygame.init()
pygame.mixer.music.load('flamingo.mp3')
pygame.mixer.music.play()
pygame.event.wait()"""

#Mudou uns coiso no python e agora você tem que inciar o mixer
# e o pygame antes, então esse aqui pode funcionar:
'''from pygame import mixer
mixer.init()
mixer.music.load('flamingo.mp3')
mixer.music.play()
input('Agora você escuta?')'''

#Mas esse é o jeito certo ó:
import pygame
pygame.mixer.init()
pygame.init()

pygame.mixer.music.load('flamingo.mp3')
pygame.mixer.music.play()
pygame.event.wait()
