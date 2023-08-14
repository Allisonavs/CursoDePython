# Faça um programa que leio o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor corretor

sexo = str(input('Qual o seu sexo? [M/F]: '))
while sexo != 'M' and sexo != 'F':
    print('Opção inválida, tente novamente')
    sexo = str(input('Qual o seu sexo? [M/F]: '))

if sexo == 'M':
    print('Você é do sexo masculino')
elif sexo == 'F':
    print('Você é do sexo feminino')