def contador(inicio, fim, passo):
    '''
    Realiza uma contagem de números de acordo com os parâmetros fornecidos.
    Parâmetros:

    inicio (int): O número inicial da contagem.
    fim (int): O número final da contagem.
    passo (int): O intervalo entre os números na contagem. Se for 0, será ajustado para 1 ou -1 dependendo da direção da contagem.
    
    A função ajusta automaticamente o passo e o fim para garantir que a contagem seja realizada corretamente, seja ela crescente ou decrescente. 
    Exibe cada número da contagem com um intervalo de 0.5 segundos entre eles.
    '''
    
    # Exibe a contagem
    escreva(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(1)

    # Ajusta o passo se for 0
    if passo == 0:
        if inicio < fim:
            passo = 1
        else:
            passo = -1
    
    # Ajusta o passo e o fim para contagem crescente
    if inicio < fim:
        if passo < 0:
            passo = -passo
        fim += 1

    # Ajusta o passo e o fim para contagem decrescente
    elif inicio > fim:
        if passo > 0:
            passo = -passo
        fim -= 1
    
        
    # Realiza a contagem
    for i in range(inicio, fim, passo):
        print(i, end=' ')
        sleep(0.5)

help(contador)
