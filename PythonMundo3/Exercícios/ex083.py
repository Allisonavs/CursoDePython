#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
#Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta


# Solicita ao usuário que digite uma expressão
expr = str(input('Digite uma expressão: '))
# Inicializa uma pilha vazia para verificar o equilíbrio dos parênteses
pilha = []

# Itera sobre cada caractere na expressão
for simb in expr:
    # Se o caractere for um parêntese de abertura, adiciona-o à pilha
    if simb == '(':
        pilha.append('(')
    # Se o caractere for um parêntese de fechamento
    elif simb == ')':
        # Verifica se a pilha não está vazia (há um parêntese de abertura correspondente)
        if len(pilha) > 0:
            # Remove o parêntese de abertura correspondente da pilha
            pilha.pop()
        else:
            # Se a pilha estiver vazia e encontrarmos um parêntese de fechamento, a expressão está desequilibrada,
            # então saímos do loop
            pilha.append(')')
            break

# Após percorrer toda a expressão, verifica se a pilha está vazia
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    # Se a pilha não estiver vazia, significa que há parênteses de abertura não correspondidos
    print('Sua expressão está errada!')
