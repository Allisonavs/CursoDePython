# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os
# 10 primeiros temos da progressão sando a estrutura while

pt = int(input('Primeiro termo: '))  # Solicita o primeiro termo da sequência ao usuário
r = int(input('Razão: '))  # Solicita a razão da sequência ao usuário

c = 0  # Inicializa o contador de termos
while c < 10:  # Enquanto o contador for menor que 10 (gera 10 termos)
    termo = pt + c * r  # Calcula o termo atual da sequência
    print(termo, end=' -> ')  # Imprime o termo atual seguido por ' -> '
    c += 1  # Incrementa o contador em 1 para passar para o próximo termo
print('Fim')  # Imprime 'Fim' quando o loop terminar
