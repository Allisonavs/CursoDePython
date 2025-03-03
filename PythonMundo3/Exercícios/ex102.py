# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e o outro chamado show,
# que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.


# Função fatorial que calcula o fatorial de um número
def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número num.
    
    
    O fatorial de um número n é o produto de todos os números inteiros positivos menores ou iguais a n.
    Por exemplo, o fatorial de 5 (escrito como 5!) é 5 x 4 x 3 x 2 x 1 = 120.
    """

    # Calcula o fatorial
    
    f = 1
    for c in range(num, 0, -1):
        f = f * c
    

        # Mostra o cálculo
        if show: # Se show for True, imprime o cálculo
            print(f'{c}' , end='')
            if c > 1: # Se c for maior que 1, imprime o x
                print(' x ', end='')
            else: # Se c for igual a 1, imprime o resultado
                print(' = ', end='')
    return f


# Programa principal

print('Mostrando o fatorial de 5:')
print(fatorial(5), end='\n\n')

print('Mostrando o fatorial de 5 com o show=True:')
print(fatorial(5, show=True), end='\n\n')

print('O que é fatorial?')
help(fatorial)
