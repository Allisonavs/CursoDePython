# Solicita 3 números
a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))
# Verificando quem é menor:
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
# Verificando o maior:
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
# Mostra qual o menor e o maior valor
print(f'O menor valor digitado é: {menor}')
print(f'O maior valor digitado é: {maior}')
