pessoas = {'Nome': 'Allison', 'Sexo': 'M', 'Idade': 19}
pessoas['Nome'] = 'Leandro'
pessoas['Peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')
