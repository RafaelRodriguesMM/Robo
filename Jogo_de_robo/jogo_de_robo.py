import numpy as np
from random import randint
import time
import os


inicio = time.time()

tamanho = 10
#gera a matriz tamanho posicao_linha tamanho com as posicões vazias " "
matriz = np.full((tamanho, tamanho), " ")

#O robo comeca da primeira posição para o jogador poder ir movendo a partir dai

robo = np.array([0, 0])
posicao_linha = robo[0]
posicao_coluna = robo[1]
matriz[posicao_linha][posicao_coluna] = "R"

#preenche a matriz como um numero de pacotes(#) em posições aleatorias(as posições são gravadas na lista)
i = 0

pacote = []
lista_pacotes = []
while i < 5:
    Linha_aleatoria = randint(0,tamanho - 1)
    coluna_aleatoria = randint(0,tamanho - 1)
    lista_pacotes.append([Linha_aleatoria, coluna_aleatoria])
    # imperde que um pacote seja colocado na posição ocupada pelo robo ou por outro pacote
    if matriz[Linha_aleatoria][coluna_aleatoria] in "R#":
        ""
    else:
        matriz[Linha_aleatoria][coluna_aleatoria] = "#" 
        i = i + 1
        


print("AJUDE O ROBO A COLETAR OS PACOTES: ")


while True:
    print(matriz)

    #Mostra a posição atual do robo na matriz

    print(f"Posições atuais do robo na matriz x = {posicao_linha} y = {posicao_coluna}")

   
    
    #Verifica se ha pacotes restantes(o jogo continua, ou não há pacotes restantes(o jogador venceu))
    pacotes = 0
    for p in lista_pacotes:
        if matriz[p[0]][p[1]] == "#":
            pacotes = pacotes + 1            
    if pacotes == 0:
        print("PARABENS, VOCÊ COLETOU TODOS OS PACOTES")
        fim = time.time()
        tempo = fim - inicio
        print(f"VOCE DEMOROU {tempo:.2f} SEGUNDOS PARA COLETAR TODOS OS PACOTES")
        print("FIM DE JOGO")
        
        
        break
        
    movimento = str(input("PARA ONDE DESEJA IR:\n[A]esquerda\n[D]direirta\n[W]frente\n[S]baixo\n[Q]sair do jogo\n: "))

    if movimento.lower() == "a":
        #Ir par a esquerda é mover para a coluna atual - 1, se o jogador tentar ir para a esquerda na coluna de inlistae 0 o robo não teria casa para ir.
        posicao_coluna = posicao_coluna - 1
        if (posicao_coluna < 0):
            matriz[posicao_linha][posicao_coluna + 1] = ' '
            matriz[posicao_linha][posicao_coluna + tamanho] = 'R'
            posicao_coluna = posicao_coluna + tamanho
        else:
            #A Posição atual do robo vai ficar vazia novamente e a posição a esquerda, neste movimento, vai ficar o robo
            matriz[posicao_linha][posicao_coluna + 1] = ' '
            matriz[posicao_linha][posicao_coluna] = 'R'

    elif movimento.lower() == "d":  
        posicao_coluna = posicao_coluna + 1
        if (posicao_coluna > tamanho - 1):
            matriz[posicao_linha][posicao_coluna - 1] = ' '
            matriz[posicao_linha][posicao_coluna - tamanho] = 'R'
            posicao_coluna = posicao_coluna - tamanho
        else:
            matriz[posicao_linha][posicao_coluna - 1] = ' '
            matriz[posicao_linha][posicao_coluna] = 'R'

    elif movimento.lower() == "w":
        posicao_linha = posicao_linha - 1
        if (posicao_linha < 0):
            matriz[posicao_linha + 1][posicao_coluna] = ' '
            matriz[posicao_linha + tamanho][posicao_coluna] = 'R'
            posicao_linha = posicao_linha + tamanho
        else:
            matriz[posicao_linha + 1][posicao_coluna] = ' '
            matriz[posicao_linha][posicao_coluna] = 'R'

    elif movimento.lower() == "s":
        posicao_linha = posicao_linha + 1
        if (posicao_linha > tamanho - 1):
            matriz[posicao_linha - 1][posicao_coluna] = ' '
            matriz[posicao_linha - tamanho][posicao_coluna] = 'R'
            posicao_linha = posicao_linha - tamanho

        else:
            matriz[posicao_linha - 1][posicao_coluna] = ' '
            matriz[posicao_linha][posicao_coluna] = 'R'

    elif movimento.lower() == "q":
        print("obrigado por jogar o jogo!")
        break
    else:
        print("digite um movimento valido")
    
    
    if os.name == 'posix':#se for linux/Unixa/macOS
        os.system("clear")
    elif os.name == 'nt':#se for windows
        os.system("cls")
