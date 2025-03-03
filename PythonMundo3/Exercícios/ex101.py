# Crie um programa que tenha uma função chamada voto() 
# que vai receber como parâmetro o ano de nascimento de uma pessoa, 
# retornando um valor literal indicando se uma pessoa tem 
# voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições. 
# Para resolver esse exercício, pesquise sobre a função date da biblioteca datetime.


# Função voto que recebe o ano de nascimento e retorna se a pessoa pode votar ou não
def voto(ano):

    # Importa a biblioteca datetime
    from datetime import datetime
    
    # Calcula a idade da pessoa
    idade = datetime.now().year - ano

    # Condições para saber se a pessoa pode votar
    if idade < 16: # Se a pessoa tiver menos de 16 anos, não pode votar
        return f'Com {idade} anos: NÃO VOTA'
    
    elif 16 <= idade < 18 or idade > 65: # Se a pessoa tiver entre 16 e 18 anos ou mais de 65 anos, o voto é opcional
        return f'Com {idade} anos: VOTO OPCIONAL'
    
    else: # Se a pessoa tiver entre 18 e 65 anos, o voto é obrigatório
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


# Programa principal

# Pede o ano de nascimento da pessoa
ano = int(input('Digite o ano de nascimento: '))

# Chama a função voto e imprime o resultado
print(voto(ano))
