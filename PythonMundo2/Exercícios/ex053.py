# Crie um programa que leia uma frase qualquer e diga se ela é um
# palindromo, desconsiderando os espaços
# Ex: APOS A SOPA

#Peço ao usuário que digite uma frase
frase = str(input('Digite uma frase: ')).strip().upper()    # Já desconsidero espaços e já coloco toda a frase em maiuscula

#Fatio a frase por palavras
palavras = frase.split()

#Coloco as palavras todas juntas
junto = ''.join(palavras)

#Crio a váriavel do inverso da palavra
inverso = ''

'''#Crio o laço
for letra in range(len(junto) - 1, -1, -1):       # Inicio o range no último caractere da palavra, usando o len para contar quantos caracteres tem,
    inverso += junto[letra]                       # termino no primeiro caractere, e coloco -1 para indicar que é contagem regressiva'''

#Utilizando técnica de fatiamento
inverso = junto[::-1]                             # Junto começando do inicio e terminando no fim só que de trás para frente

print(f'O inverso de {junto} é {inverso}')
#Indico para o usuário se a palavra é ou não um palíndromo
if inverso == junto:                              # Para ser um palíndromo, a frase deve ser escrita da mesma forma de trás para frente
    print('Temos um PALÍNDROMO')
else:
    print('A frase digitada NÃO É um PALÍNDROMO')
