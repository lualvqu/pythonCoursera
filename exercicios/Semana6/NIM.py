# Processa Escolha do Computador
def computador_escolhe_jogada(n, m):
    retirar = m
    for x in range(1, m):
        if (n - x) % (m+1) == 0:
            retirar = x
            break
    if retirar == 1:
        print('O computador tirou uma peça.')
    else:
        print('O computador tirou {0} peças.'.format(retirar))
    return retirar

# Processa Escolha do Jogador
def usuario_escolhe_jogada(n, m):
    retirar = -1
    while (retirar < 0 or retirar > m or retirar > n):
        retirar = int(input('Quantas peças você vai tirar? '))
        if (retirar < 0 or retirar > m or retirar > n):
            print('\nOops! Jogada inválida! Tente de novo.\n')
    if retirar == 1:
        print('Você tirou uma peça.')
    else:
        print('Você tirou {0} peças.'.format(retirar))
    return retirar

# Roda Partida
def partida ():
    startAUX = False
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))

    if (n % (m+1) == 0):
        print('\nVoce começa!\n')
    else:
        print('\nComputador começa!\n')
        startAUX = True

    while (n > 0):
        if(startAUX):
            n = n - computador_escolhe_jogada(n, m)
            if (n <= 0):
                print('Fim do jogo! O computador ganhou!\n')
                return 0
            else:
                if (n != 1):
                    print('Agora restam {0} peças no tabuleiro.\n'.format(n))
                else:
                    print('Agora resta apenas uma peça no tabuleiro.\n')
        n = n - usuario_escolhe_jogada(n, m)
        if (n <= 0):
            print('Fim do jogo! Voce ganhou!\n')
            return 1
        else:
            if (n != 1):
                print('Agora restam {0} peças no tabuleiro.\n'.format(n))
            else:
                print('Agora resta apenas uma peça no tabuleiro.\n')
        startAUX = True

def campeonato ():
    pontosUsuario = 0
    pontosPC = 0
    for x in range(3):
        print('**** Rodada {} ****\n'.format(x+1))
        ganhador = partida()
        if(ganhador == 0):
            pontosPC += 1
        else:
            pontosUsuario +=1
    print('**** Final do campeonato! ****\n')
    print('Placar: Você {0} X {1} Computador'.format(pontosUsuario, pontosPC))
# Inicia o progrma - Printando Menu inicial
def main ():
    print('\nBem-vindo ao jogo do NIM! Escolha:')
    escolha = int(input('\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato '))

    if (escolha == 1):
        print('\nVoce escolheu uma partida isolada!\n')
        partida()
    else:
        print('\nVoce escolheu um campeonato!\n')
        campeonato()

main()