# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
# e quantas mulheres têm menos de 20 anos.

#Crio as variáveis
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

#Crio o laço de repetição para cadastrar o nome, idade e sexo das pessoas, para depois analisar
for p in range (1,5):
    print(f'----- {p}ª Pessoa -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade                                # É somada todas as idades
    if p == 1 and sexo in 'Mm':                       # Se for o primeiro laço e for do sexo masculino, esse será o mais velho
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:      # Se não, serão substituidos os que já estão inseridos
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:                   # Se for mulher e tiver menos que 20 anos, aumenta 1 no contador
        totmulher20 += 1

#O programa calcula a média de idade do grupo de pessoas
mediaidade = somaidade / 4

#O programa mostra ao usuário a analise dos dados
print(f'A idade média é de {mediaidade} anos')
print(f'O homem mais velho tem {maioridadehomem} e se chama {nomevelho}')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos')
