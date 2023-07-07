# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# -Equilátero: todos os lados iguais
# -Isósceles: dois lado iguais
# -Escaleno: todos os lados diferentes

# Primeiro menu do programa
print('-='*20)
print('Analisador de Triângulos')
print('-='*20)

# Pede o valor dos segmentos
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

# Analisa se pode ou não forma um triângulo, de acordo com o teorema de desigualdade triangular
# E caso seja possível formar, indicará o tipo do triângulo formado, Equilátero, Isósceles ou Escaleno
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('É POSSÍVEL formar um triângulo!')
    if s1 == s2 and s1 == s3 and s2 == s3:
        print('O triângulo formado será equilátero')
    elif s1 == s2 or s1 == s3 or s2 == s3:
        print('O triângulo formado será isósceles')
    elif s1 != s2 and s1 != s3 and s2 != s3:
        print('O triângulo formado será escaleno')
else:
    print('NÃO É POSSÍVEL formar um triângulo')
