#Crio as váriaveis
galera = list()     #Lista de toda a galera
dado = list()       #Lista dos dados coletados a cada laço
totmai = totmen = 0 #Variáveis de total de maiores e menores de idade

#Laço de repetição para coletar os dados, nome e idade
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])      #Adiciona uma copia da lista dado em galera
    dado.clear()                #Limpa a lista dado

#Laço de repetição para mostrar se fulano é maior ou menor de idade
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade')