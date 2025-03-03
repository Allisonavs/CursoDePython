# Crie um programa que tenha a função leiaInt(), 
# que vai funcionar de forma semelhante à função input() do Python, 
# só que fazendo a validação para aceitar apenas um valor numérico.

# Função leiaInt que só aceita números inteiros
def leiaInt(num):

    # Loop infinito para pedir um número inteiro
    while True:
        n = str(input(num))
        if n.isnumeric(): # Se o número for um número inteiro, retorna o número
            return int(n)
        else: # Se o número não for um número inteiro, imprime uma mensagem de erro
            print('\033[91mERRO! Digite um número inteiro válido.\033[m')
             

# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
