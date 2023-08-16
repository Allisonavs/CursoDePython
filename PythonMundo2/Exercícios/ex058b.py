from random import randint
from time import sleep

print('\033[4;31m=-=' * 20, '\033[m')
print(' \033[34mJOGO DA ADIVINHAÇÃO!\033[m')
print('\033[4;31m=-=' * 20, '\033[m')
r = '2'
while r == '2':
    modo_de_jogo = int(input('\033[1;36mEscolha o Modo de Jogo: \n[1] Fácil \n[2] Normal \n[3] Difícil \n-> \033[m'))
    r = '1'
    while r == '1':

        print('\033[4;31m=-=' * 20, '\033[m')
        print(' \033[34mVou \033[4mPensar em um \033[4mNúmero entre \033[4m0 a 10.\033[m')
        print(' \033[1;36mTente adivinhar...\033[m')
        print('\033[4;31m=-=' * 20, '\033[m')
        n = randint(0, 10)
        num = int(input('\033[1;34mEm que Número você acha que Eu Pensei? \n -> \033[m'))
        print('\033[1;31mProcessando...\033[m')
        sleep(2)
        tentativas = 1
        if modo_de_jogo == 1:
            if num != n:
                while num != n:
                    print(f'\033[1;32mHAHAHA VOCÊ ERROU!\033[m')
                    sleep(2)
                    if n > num:
                        print('\033[1;36mDica: é um Número Maior!\033[m')
                        sleep(2)
                    else:
                        print('\033[1;36mDica: é um Número Menor!\033[m')
                        sleep(2)
                    num = int(input('\033[1;34mEm que Número você acha que Eu Pensei? \n -> \033[m'))
                    tentativas += 1
                    print('\033[1;31mProcessando...\033[m')
                    sleep(2)
            else:
                print(f'\033[1; 33mVOCÊ ESTÁ COM SORTE! PARABÉNS, ACERTOU DE PRIMEIRA!\033[m')
        elif modo_de_jogo == 2:
            if num != n:
                while num != n:
                    print(f'\033[1;32mHAHAHA VOCÊ ERROU!\033[m')
                    sleep(2)
                    if n % 2 == 0:
                        print('\033[1;36mDica: é um Número PAR!\033[m')
                        sleep(2)
                    else:
                        print('\033[1;36mDica: é um Número ÍMPAR!\033[m')
                        sleep(2)
                    num = int(input('\033[1;34mEm que Número você acha que Eu Pensei? \n -> \033[m'))
                    tentativas += 1
                    print('\033[1;31mProcessando...\033[m')
                    sleep(2)
            else:
                print(f'\033[1; 33mVOCÊ ESTÁ COM SORTE! PARABÉNS, ACERTOU DE PRIMEIRA!\033[m')
        else:
            if num != n:
                while num != n:
                    print(f'\033[1;32mHAHAHA VOCÊ ERROU! \nTente Novamente!\033[m')
                    sleep(2)
                    num = int(input('\033[1;34mEm que Número você acha que Eu Pensei? \n -> \033[m'))
                    tentativas += 1
                    print('\033[1;31mProcessando...\033[m')
                    sleep(2)
            else:
                print(f'\033[1; 33mVOCÊ ESTÁ COM SORTE! PARABÉNS, ACERTOU DE PRIMEIRA!\033[m')
        print(f'\033[1;33mPARABÉNS, VOCÊ ACERTOU COM {tentativas} TENTATIVAS!\033[m')
        sleep(4)
        print('\033[4;31m========================\033[m')
        print('\033[1;32m [1] Jogar Novamente \n [2] Mudar Modo de Jogo \n [3] Fechar Jogo\033[m')
        r = str(input('\033[35m-> \033[m'))
    print('\033[4;30mFechando Jogo...\033[m')