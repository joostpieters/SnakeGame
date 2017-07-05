import os

Board = []
Board_Height = 23 ## Must be an odd number
Board_Length = 79 ## Must be an odd number
PrintBoard = ""

## Lower ==> Higher
##   ||
##   ||
##   \/
## Higher

def MakeBoard(Board, Board_Height, Board_Length): ## Do not use more than once
    
    for y in range(Board_Height) : ## Creates dictionary ## List of lists
        Board.append([])           ## Will be y coord

        for x in range(Board_Length) : ## x coord

            if x == 0 and y == 0 :           ## checks for position and
                Board[y].append("+")         ## sets value for board
            elif x == Board_Length - 1 and y == 0 :
                Board[y].append("+")
            elif x == 0 and y == Board_Height - 1 :
                Board[y].append("+")
            elif x == Board_Length - 1 and y == Board_Height - 1 :
                Board[y].append("+")

            elif x == 0 :
                Board[y].append("|")
            elif x == Board_Length - 1 :
                Board[y].append("|")

            elif y == 0 :
                Board[y].append("-")
            elif y == Board_Height - 1 :
                Board[y].append("-")
            
            elif y % 2 == 0 and x % 2 == 0 :
                print("True")
                Board[y].append("X")
            
            else:
                Board[y].append(" ")


def UpdateBoard(Board, Update_y, Update_x, Update): ## Updates board with new value
                                                    ## with Update_y and _x being the coords
    if Update_y != 0 and Update_y != Board_Height - 1 :

        if Update_x != 0 and Update_x != Board_Length - 1:
            
            if Board[Update_y][Update_x] != "X" :

                Board[Update_y][Update_x] = Update

def GetPrintBoard(Board, PrintBoard):

    PrintBoard = ""

    for y in range(Board_Height):
        for x in range(Board_Length):
            PrintBoard += Board[y][x]

        if y < Board_Height - 1:
            PrintBoard += "\n"


    os.system("cls")
    print(PrintBoard)
