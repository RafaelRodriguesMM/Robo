from numpy import full
from random import randint
import time
import os

inicio = time.time()

tamanho = 10
#gera a matriz tamanho x tamanho com as posicões vazias " "
matriz = full((tamanho, tamanho), " ")

#O robo comeca da primeira posição para o jogador poder ir movendo a partir dai
matriz[0][0] = "R"

#preenche a matriz como um numero de pacotes(#) em posições aleatorias
i = 0
while i < 5:
    Linha_aleatoria = randint(0,tamanho - 1)
    coluna_aleatoria = randint(0,tamanho - 1)
    # imperde que um pacote seja colocado na posição ocupada pelo robo ou por outro pacote
    if matriz[Linha_aleatoria][coluna_aleatoria] in "R#":
        ""
    else:
        matriz[Linha_aleatoria][coluna_aleatoria] = "#" 
        i = i + 1

print("AJUDE O ROBO A COLETAR OS PACOTES: ")


while True:
    print(matriz)

    #Acha a posição atual do robo
    for linha in range(0,tamanho):
        for coluna in range(0,tamanho):
            if matriz[linha][coluna] == "R":
                Linha_atual = linha
                coluna_atual = coluna
                break
        if matriz[linha][coluna] == "R":
                break
    
    #Verifica se ha pacotes restantes(o jogo continua, ou não há pacotes restantes(o jogador venceu))
    pacotes = 0
    for linha in range(0,tamanho):
        for coluna in range(0,tamanho):
            if matriz[linha][coluna] == '#':
                pacotes += 1
                
    if pacotes > 0:
        ''
    else:
        print("PARABENS, VOCÊ COLETOU TODOS OS PACOTES")
        fim = time.time()
        tempo = fim - inicio
        print(f"VOCE DEMOROU {tempo:.2f} SEGUNDOS PARA COLETAR TODOS OS PACOTES")
        print("FIM DE JOGO")
        
        
        break
        
    movimento = str(input("PARA ONDE DESEJA IR:\n[A]esquerda\n[D]direirta\n[W]frente\n[S]baixo\n[Q]sair do jogo\n: "))

    if movimento.lower() == "a":
        #Ir par a esquerda é mover para a coluna atual - 1, se o jogador tentar ir para a esquerda na coluna de indice 0 o robo não teria casa para ir.
        if (coluna_atual - 1 < 0):
            matriz[Linha_atual][coluna_atual] = ' '
            matriz[Linha_atual][9] = 'R'
        else:
            #A Posição atual do robo vai ficar vazia novamente e a posição a esquerda, neste movimento, vai ficar o robo
            matriz[Linha_atual][coluna_atual] = ' '
            matriz[Linha_atual][coluna_atual - 1] = 'R'

    elif movimento.lower() == "d":  
        if (coluna_atual + 1 > tamanho - 1):
            matriz[Linha_atual][coluna_atual] = ' '
            matriz[Linha_atual][0] = 'R'
        else:
            matriz[Linha_atual][coluna_atual] = ' '
            matriz[Linha_atual][coluna_atual + 1] = 'R'

    elif movimento.lower() == "w": 
        if (Linha_atual - 1 < 0):
            matriz[Linha_atual][coluna_atual] = ' '
            matriz[9][coluna_atual] = 'R'
        else:
            matriz[Linha_atual][coluna_atual] = ' '
            matriz[Linha_atual - 1][coluna_atual] = 'R'

    elif movimento.lower() == "s":  
        if (Linha_atual + 1 > tamanho - 1):
            matriz[Linha_atual][coluna_atual] = ' '
            matriz[0][coluna_atual] = 'R'

        else:
            matriz[Linha_atual][coluna_atual] = ' '
            matriz[Linha_atual + 1][coluna_atual] = 'R'

    elif movimento.lower() == "q":
        print("obrigado por jogar o jogo!")
        break
    else:
        print("digite um movimento valido")
    
    os.system("clear")
