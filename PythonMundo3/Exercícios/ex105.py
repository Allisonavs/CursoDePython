# Faça um programa que tenha uma função notas() 
# que pode receber várias notas de alunos e vai retornar 
# um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# Adicione também as docstrings da função.


# Função notas com vários parâmetros e um parâmetro opcional
def notas(*n, sit=False):
    
    """
    -> Função para analisar notas e situação de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita várias)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação
    :return: Dicionário com várias informações sobre a situação da turma.
    """

    # Dicionário com as informações
    info = dict()

    # Quantidade de notas
    info['Total'] = len(n)

    # Maior nota
    info['Maior'] = max(n)

    # Menor nota
    info['Menor'] = min(n)

    # Média da turma
    info['Média'] = round(sum(n) / info['Total'], 2)

    # Se sit for True, verifica a situação da turma
    if sit:
        if info['Média'] >= 7:
            info['Situação'] = 'BOA'
        elif 5 <= info['Média'] < 7:
            info['Situação'] = 'RAZOÁVEL'
        else:
            info['Situação'] = 'RUIM'

    return info

# Programa principal
resp = notas(5.5, 2.5, 9, 8.5, 3, 2, 1, 1, sit=True)
print(resp)
print()

for k, v in resp.items():
    print(f'{k}: {v}')

print()
help(notas)
