import os
import numpy as np

maps = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]


win_combination = [[0, 1, 2],
                   [3, 4, 5],
                   [6, 7, 8],
                   [0, 3, 6],
                   [1, 4, 7],
                   [2, 5, 8],
                   [0, 4, 8],
                   [2, 4, 6]]



def print_maps():
    os.system('cls' if os.name == 'nt' else 'clear')        #Для запуска через файл или VSCode
    # print("\n" *100)                                      #Для запуска через IDE PyCharm
    print(maps[0], end="  ")
    print(maps[1], end="  ")
    print(maps[2])

    print(maps[3], end="  ")
    print(maps[4], end="  ")
    print(maps[5])

    print(maps[6], end="  ")
    print(maps[7], end="  ")
    print(maps[8])


def get_result(pl1, pl2):
    win = ""

    for i in win_combination:
        if maps[i[0]] == pl1 and maps[i[1]] == pl1 and maps[i[2]] == pl1:
            win = f"Игрок 1 {pl1}"
        if maps[i[0]] == pl2 and maps[i[1]] == pl2 and maps[i[2]] == pl2:
            win = f"Игрок 2 {pl2}"

    return win



game_over = False
player1 = True

while game_over == False:
                             
    print_maps()


    if player1 == True:
        symbol = chr(10008)
        step = int(input("Игрок 1, ваш ход: "))
    else:
        symbol = chr(11096)
        step = int(input("Игрок 2, ваш ход: "))

    maps[maps.index(step)] = symbol

    win = get_result(chr(10008), chr(11096))  
    
    if win:
        game_over = True
    else:
        game_over = False

    player1 = not (player1)



print_maps()
input(f"Победил {win}   ")