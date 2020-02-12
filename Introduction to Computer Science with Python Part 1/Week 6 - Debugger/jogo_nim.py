def computador_escolhe_jogada(n,m):
    jogada = 1

    while (jogada != m):
        if ((n - jogada) % (m + 1) == 0):
            return jogada
        else:
            jogada = jogada + 1
    return jogada

def usuario_escolhe_jogada(n,m):
    jogadaValida = False

    while (not jogadaValida):
        jogada = int(input("Quantas peças você vai tirar? "))
        if (jogada > m or jogada < 1 or jogada > n):
            print("\nOops! Jogada inválida! Tente de novo.\n")
        else:
            jogadaValida = True
    return jogada

def campeonato():
    placarUsuario = 0
    placarComputador = 0
    rodada = 1

    while (rodada <= 3):
        print("\n**** Rodada", rodada, "****\n")
        rodada = rodada + 1
        vencedor = partida()
        if vencedor == 1:
            placarUsuario = placarUsuario + 1
        else:
            placarComputador = placarComputador + 1

    print("\n**** Final do campeonato! ****\nPlacar: Você", placarUsuario, "X", placarComputador ,"Computador")

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    turnoComputador = False

    if (n % (m+1) == 0):
        print("\nVocê começa!")
    else:
        print("\nComputador começa!")
        turnoComputador = True

    while (n > 0):
        if (turnoComputador):
            jogada = computador_escolhe_jogada(n,m)
            if (jogada == 1):
                print("\nO computador tirou uma peça")
            else:
                print("O computador tirou", jogada, "peças")
            turnoComputador = False
        else:
            jogada = usuario_escolhe_jogada(n,m)
            if (jogada == 1):
                print("\nVocê tirou uma peça")
            else:
                print("Você tirou", jogada, "peças")
            turnoComputador = True
        n = n - jogada

        if (n == 1):
            print("Agora resta apenas uma peça no tabuleiro.\n")
        else:
            if (n != 0):
                print("Agora restam", n, "peças no tabuleiro.\n")

    if (turnoComputador):
        print("\nFim do jogo! Você ganhou!")
    else:
        print("\nFim do jogo! O computador ganhou!")

tipoJogo = int(input("Bem-vindo ao jogo do NIM! Escolha: \n\n1 - para jogar uma partida isolada \n2 - para jogar um campeonato "))
if tipoJogo == 1:
    partida()
if tipoJogo == 2:
    print("\nVoce escolheu um campeonato!\n")
    campeonato()
else:
    print("\nOpção inválida!\n")
