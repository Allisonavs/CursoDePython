#Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#Depois dissos você deve mostrar, para cada palavras, quais são as suas vogais

palavras_aleatorias = (
    "guitarra", "sorvete", "computador", "livro", "janela",
    "bicicleta", "telefone", "cachorro", "elefante", "abacaxi",
    "caneta", "avião", "piano", "papel", "relógio",
    "água", "página", "ônibus", "árvores", "céu"
)

for palavra in palavras_aleatorias:
    print(f'\nNa palavra {palavra.upper()} temos as vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aáàãeéêiíõu':
            print(letra, end=' ')
