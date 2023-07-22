import tkinter as tk

# Função para calcular os resultados e exibi-los em uma nova janela
def exibir_resultados():
    # Código para calcular os resultados
    somaidade = 0
    mediaidade = 0
    maioridadehomem = 0
    nomevelho = ''
    totmulher20 = 0

    for p in range(1, 5):
        nome = nome_entries[p-1].get()
        idade = int(idade_entries[p-1].get())
        sexo = sexo_entries[p-1].get()
        somaidade += idade

        if p == 1 and sexo in 'Mm':
            maioridadehomem = idade
            nomevelho = nome

        if sexo in 'Mm' and idade > maioridadehomem:
            maioridadehomem = idade
            nomevelho = nome

        if sexo in 'Ff' and idade < 20:
            totmulher20 += 1

    mediaidade = somaidade / 4

    # Criação da janela para exibir os resultados
    resultado_window = tk.Toplevel(root)
    resultado_window.title("Resultados")

    # Labels para exibir os resultados
    label_media = tk.Label(resultado_window, text=f'A idade média é de {mediaidade:.2f} anos', padx=10, pady=5)
    label_media.pack()

    label_homem_mais_velho = tk.Label(resultado_window, text=f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}', padx=10, pady=5)
    label_homem_mais_velho.pack()

    label_mulheres_menos_20 = tk.Label(resultado_window, text=f'Ao todo são {totmulher20} mulheres com menos de 20 anos', padx=10, pady=5)
    label_mulheres_menos_20.pack()

# Função para passar o foco para a próxima caixa de entrada
def passar_proxima_caixa(event):
    event.widget.tk_focusNext().focus()

# Criação da janela principal
root = tk.Tk()
root.title("Cadastro de Pessoas")

# Listas para armazenar as caixas de entrada para nome, idade e sexo
nome_entries = []
idade_entries = []
sexo_entries = []

# Widgets para o cadastro de pessoas
for p in range(1, 5):
    frame = tk.Frame(root)
    frame.pack(pady=10)

    tk.Label(frame, text=f'----- {p}ª Pessoa -----').pack()

    tk.Label(frame, text="Nome:").pack(side=tk.LEFT)
    nome_entry = tk.Entry(frame)
    nome_entry.pack(side=tk.LEFT, padx=5)
    nome_entries.append(nome_entry)
    nome_entry.bind("<Return>", passar_proxima_caixa)

    tk.Label(frame, text="Idade:").pack(side=tk.LEFT)
    idade_entry = tk.Entry(frame)
    idade_entry.pack(side=tk.LEFT, padx=5)
    idade_entries.append(idade_entry)
    idade_entry.bind("<Return>", passar_proxima_caixa)

    tk.Label(frame, text="Sexo [M/F]:").pack(side=tk.LEFT)
    sexo_entry = tk.Entry(frame)
    sexo_entry.pack(side=tk.LEFT, padx=5)
    sexo_entries.append(sexo_entry)
    sexo_entry.bind("<Return>", passar_proxima_caixa)

# Botão para exibir os resultados
btn_resultados = tk.Button(root, text="Exibir Resultados", command=exibir_resultados)
btn_resultados.pack(pady=10)

# Iniciar a janela principal
root.mainloop()
