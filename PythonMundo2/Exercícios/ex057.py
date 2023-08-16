# Faça um programa que leio o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor corretor

#O programa pergunta qual o sexo do usuário
sexo = str(input('Qual o seu sexo? [M/F]: ')).strip().upper()[0]

#É criado o laço de repetição para continuar perguntando caso a resposta seja inválida
while sexo not in 'MmFf':
    print('Opção inválida, tente novamente')
    sexo = str(input('Qual o seu sexo? [M/F]: ')).strip().upper()[0]

#Se a resposta for válida, ira analisar a resposta do usuário e indicar qual o sexo dele
if sexo == 'M':
    print('Você é do sexo masculino')
elif sexo == 'F':
    print('Você é do sexo feminino')
