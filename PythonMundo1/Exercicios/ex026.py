f = str(input("Digite uma frase: ")).strip().upper()
print(f"A letra A aparece {f.count('A')} vezes na sua frase")
print(f"Ela aparece pela primeira vez na posição {f.find('A')+1}")
print(f"E aparece pela última vez na posição {f.rfind('A')+1}")
