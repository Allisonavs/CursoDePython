# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os
# 10 primeiros temos da progressão sando a estrutura while

#O programa pede o primeiro termo e a razão
pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))

#É criada as variaveis
termo = pt
c = 0

#O laço é criado
while c < 10:  # Enquanto o contador for menor que 10 (gera 10 termos)
    print(termo, end=' -> ')
    termo += r  # Calcula o termo atual da sequência
    c += 1
print('Fim')
