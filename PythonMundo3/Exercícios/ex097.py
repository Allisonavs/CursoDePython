# Faça um programa que tenha uma função chamada escreva(), 
# que receba um texto qualquer como parâmetro e mostre uma mensagem 
# com tamanho adaptável.

# Função que escreve uma mensagem com tamanho adaptável
def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(msg.center(tam))
    print('~' * tam)

# Este trecho de código é executado apenas se este arquivo for executado diretamente
# e não se ele for importado por outro arquivo

# Escreve as mensagens
if __name__ == '__main__':
    escreva('Curso de Python no YouTube')
    escreva('Olá, Mundo!')
    escreva('CeV')
 