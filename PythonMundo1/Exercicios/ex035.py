# Primeiro menu do programa
print('\033[0;30;43m-='*20)
print('Analisador de Triângulos')
print('-='*20)
print('\033[m')
# Pede o valor dos segmentos
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

# Analisa se pode ou não forma um triângulo, de acordo com o teorema de desigualdade triangular
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('É POSSÍVEL formar um triângulo!')
else:
    print('NÃO É POSSÍVEL formar um triângulo')
