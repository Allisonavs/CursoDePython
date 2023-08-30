#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
#na ordem de colocação. Depois mostre:
#A) Apenas os 5 primeiros colocados.
#B) Os últimos 4 colocados da tabela.
#C) Uma lista com os times em ordem alfabética.
#D) Em que posição na tabela está o time da Chapecoense.

from time import sleep

times = (
    "Botafogo", "Palmeiras", "Grêmio", "Flamengo", "Fluminense", "Bragantino",
    "Athletico-PR", "Fortaleza", "Atlético-MG", "Cuiabá", "São Paulo", "Cruzeiro",
    "Corinthians", "Internacional", "Goiás", "Bahia", "Santos", "Vasco",
    "Coritiba", "América-MG")

print("="*50)
print("{:^50}".format("DADOS DO BRASILEIRÃO 2019"))
print("="*50)
opcao = 0

while opcao != 8:
    sleep(2)
    opcao = int(input('''[1] O Campeão do campeonato
[2] Classificados para fase de grupos da Libertadores 
[3] Classificados para Pré - Libertadores 
[4] Classificados para fase de grupos da Copa Sul-Americana
[5] Rebaixados para serie B
[6] Posição e situação de determinado time
[7] Tabela completa
[8] Sair do programa do brasileirão
Digite: '''))

    print("="*50)
    if opcao == 1:
        print("O campeão foi o {}".format(times[0]))
    elif opcao == 2:
        print(f"Classificados para Libertadores 2020:")
        for t in times[:6]:
            print(t)
    elif opcao == 3:
        print(f"Classificados para Pré - Libertadores 2020:")
        for t in times[6:8]:
            print(t)
    elif opcao == 4:
        print(f"Classificados para Sul-Americana 2020:")
        for t in times[8:14]:
            print(t)
    elif opcao == 5:
        print(f"Rebaixados para Segunda Divisão:")
        for t in times[-4:]:
            print(t)
    elif opcao == 6:
        time = str(input("Escreva o nome do seu time: ")).strip().title()
        if time in times:
            print(f"O {time} ficou na {times.index(time)+1}º Posição")
            print("Situação: ",end="")
            if times.index(time) == 0:
                print("Campeão brasileiro e está na Libertadores")
            elif times.index(time) >= 1 and times.index(time) <= 5:
                print("Está na Libertadores")
            elif times.index(time) >= 6 and times.index(time) < 8:
                print("Está na Pré - Libertadores")
            elif times.index(time) >= 8 and times.index(time) <= 13:
                print("Está na Copa Sul-Americana")
            elif times.index(time) >= 16:
                print("Está Rebaixado para a Serie B")
            else:
                print("Ficou na Serie A, porém não se classificou para nenhuma outra competição")
        else:
            print("O {} não participou do Brasileirão 2019".format(time))
    elif opcao == 7:
        cont = 0
        print("="*50)
        print("{:^50}".format("TABELA DO BRASILEIRÃO 2019"))
        print("="*50)
        for tabela in times:
            print(f"{cont + 1}º {tabela}")
            cont += 1
    else:
        print('Opção Inválida, tente novamente!')

    print("=" * 50)
print("Fim do programa do campeonato brasileiro")
