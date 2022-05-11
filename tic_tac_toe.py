"""
Created on Tue May  3 15:54:53 2022

@author: jcinv
"""


GAME_OVER = False
KEEP_PLAYING = True
jogador = 0
score_1 = 0
score_2 = 0
valor_1 = 0
valor_2 = 0
jogo = 0
jogador_1 = []
jogador_2 = [] 
usados = []

JOGO = """ 
      |     |     
   1  |  2  |  3  
 _____|_____|_____
      |     |     
   4  |  5  |  6 
 _____|_____|_____
      |     |     
   7  |  8  |  9  
      |     |      
"""

ganhar =  [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [1,4,7],
    [2,5,8],
    [3,6,9],
    [1,5,9],
    [3,5,7]]



nome_1 = input("Name player 1: ")
nome_2 = input("name player 2: ")


def game(jogador_1):
    games = False
    for lista in ganhar:
        valor = []
        for e in range(len(jogador_1)):
            for z in range(3):
                if jogador_1[e] == lista[z]:
                    valor.append(jogador_1[e])
                    if len(valor) == 3:
                        games = True
    return games



def aceitar_valor(nome_1, usados):
    VALOR_CERTO = False
    while VALOR_CERTO == False:
        jogada = input(f"Jogador {nome_1}: ")
        try:
            if int(jogada) <10:
                if int(jogada) not in usados:
                    VALOR_CERTO = True
                    usados.append(int(jogada))
                else:
                    print(f"{jogada} was alredy used. Choose another number.")
                    VALOR_CERTO = False
            else:
                VALOR_CERTO = False 
                print(f"{jogada} it's not available. Choose another number.")
        
        except ValueError:
            print(f"{jogada} can't be used. Choose another number.")
            VALOR_CERTO = False
            
    return jogada



def new_game(JOGO, ganhar, score_1, score_2):
    
    jogador = 0
    GAME_OVER = False
    usados = []
    
    while GAME_OVER == False:
        
        if jogador % 2 == 0:
            jogada = aceitar_valor(nome_1, usados)
            play = 'o'
            jogador_1.append(int(jogada))
            GAME_OVER = game(jogador_1)
            if GAME_OVER == True:
                print(f"{nome_1} wins!")
                score_1 += 1
        else:
            jogada = aceitar_valor(nome_2, usados)
            play = '*'
            jogador_2.append(int(jogada))
            GAME_OVER = game(jogador_2)
            if GAME_OVER == True:
                print(f"{nome_2} wins!")
                score_2 += 1
        if jogador == 8 and GAME_OVER == False:
            GAME_OVER = True
            print("It's a tie 👔")
        usados.append(int(jogada))
        JOGO = JOGO.replace(jogada, play)
        print(JOGO)
        jogador += 1
    return [score_1, score_2]


while KEEP_PLAYING == True: 

    if jogo == 0:    
        print(JOGO)
        score = new_game(JOGO, ganhar, valor_1, valor_2)
        valor_1 += score[0]
        valor_2 += score[1]
        jogo +=1
    else:
        keep = input("One more game? (Y/N): ").upper()
        if keep == 'Y':
            print(JOGO)
            KEEP_PLAYING = True
            jogador = 0
            jogador_1 = []
            jogador_2 = [] 
            GAME_OVER == False        
            score = new_game(JOGO, ganhar, score_1, score_2)
            valor_1 += score[0]
            valor_2 += score[1]
            jogo +=1
        else:
            KEEP_PLAYING = False
            print(f"{nome_1} - {nome_2}")
            print(f"{valor_1} - {valor_2}")
            if valor_1 > valor_2:
                print(f'WINNER: {nome_1}!!')
            elif valor_1 < valor_2:
                print(f"WINNER: {nome_2}!!")
            else:
                print("It's a tie")
    
    
    
    
        