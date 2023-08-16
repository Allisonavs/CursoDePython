# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.

#O programa pede o primeiro termo e a razão
pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))

#É criada as variaveis
termo = pt
c = 0
total = 0
mais = 10

#O laço é criado
while mais != 0:
    total += mais     # Soma o total de termos exibidos
    while c < total:  # Enquanto o contador for menor que total (gera {total} termos)
        print(termo, end=' -> ')
        termo += r  # Calcula o termo atual da sequência
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')
print('FIM')
