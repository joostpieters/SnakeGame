import time
import msvcrt
from Board import *

KeyStroke = b"a"
Suggested_KeyStroke = ""

Snake = ""
Speed = 0.2

MakeBoard(Board, Board_Height, Board_Length)

GetFruitSpaces(Board, FruitSpaces)
FruitY = FruitSpaces.index(random.choice(FruitSpaces))
FruitX = FruitSpaces[FruitY][random.randint(0, (len(FruitSpaces[FruitY])- 1))]

SnakeHeadY = 11
SnakeHeadX = 36

SnakeTailY = 11
SnakeTailX = 40

def SetUp(Board, PrintBoard, Snake) :

    Snake = ":0000"
    y = 11
    x = 36
    
    for i in Snake:
        UpdateBoard(Board, y, x, i)
        x +=1

    UpdateBoard(Board, FruitY, FruitX, "F")
    GetPrintBoard(Board, PrintBoard)

def Grow(SnakeHeadY, SnakeHeadX, FruitY, FruitX) :
    
    if SnakeHeadY == FruitY :
        if SnakeHeadX == FruitX :

            return True

def SnakeMove(Board, PrintBoard, Snake, KeyStroke, Suggested_KeyStroke, SnakeHeadY, SnakeHeadX, SnakeTailY, SnakeTailX, FruitY, FruitX):
    while True :

        time.sleep(Speed)
        

        if msvcrt.kbhit():
            Suggested_KeyStroke = msvcrt.getch()
        
        if Suggested_KeyStroke == b"w" :
            if KeyStroke == b"s" :
                Suggested_KeyStroke = b"s"

            if not Board[SnakeHeadY - 1][SnakeHeadX] == "X" :
                KeyStroke = Suggested_KeyStroke
            
        elif Suggested_KeyStroke == b"a" :
            if KeyStroke == b"d" :
                Suggested_KeyStroke = b"d"

            if not Board[SnakeHeadY][SnakeHeadX - 1] == "X" :
                KeyStroke = Suggested_KeyStroke

        elif Suggested_KeyStroke == b"s" :
            if KeyStroke == b"w" :
                Suggested_KeyStroke = b"w"

            if not Board[SnakeHeadY + 1][SnakeHeadX] == "X" :
                KeyStroke = Suggested_KeyStroke

        elif Suggested_KeyStroke == b"d" :
            if KeyStroke == b"a" :
                Suggested_KeyStroke = b"a"

            if not Board[SnakeHeadY][SnakeHeadX + 1] == "X" :
                KeyStroke = Suggested_KeyStroke


        if KeyStroke == b"w" :

            UpdateBoard(Board, SnakeHeadY - 1, SnakeHeadX, '"')
            UpdateBoard(Board, SnakeHeadY, SnakeHeadX, "0")
            SnakeHeadY = SnakeHeadY - 1
   
        elif KeyStroke == b"a" :

            UpdateBoard(Board, SnakeHeadY, SnakeHeadX - 1, ":")
            UpdateBoard(Board, SnakeHeadY, SnakeHeadX, "0")
            SnakeHeadX = SnakeHeadX - 1

        elif KeyStroke == b"s" :

            UpdateBoard(Board, SnakeHeadY + 1, SnakeHeadX, '"')
            UpdateBoard(Board, SnakeHeadY, SnakeHeadX, "0")
            SnakeHeadY = SnakeHeadY + 1

        elif KeyStroke == b"d" :

            UpdateBoard(Board, SnakeHeadY, SnakeHeadX + 1, ":")
            UpdateBoard(Board, SnakeHeadY, SnakeHeadX, "0")
            SnakeHeadX = SnakeHeadX + 1

        UpdateBoard(Board, SnakeTailY, SnakeTailX, " ")

        if Board[SnakeTailY - 1][SnakeTailX] == "0":

            if Grow(SnakeHeadY, SnakeHeadX, FruitY, FruitX) :
                print("Grow")
                FruitY = FruitSpaces.index(random.choice(FruitSpaces))
                FruitX = FruitSpaces[FruitY][random.randint(0, (len(FruitSpaces[FruitY])- 1))]
                UpdateBoard(Board, FruitY, FruitX, "F")
            else:
                SnakeTailY = SnakeTailY - 1

        elif Board[SnakeTailY + 1][SnakeTailX] == "0":

            if Grow(SnakeHeadY, SnakeHeadX, FruitY, FruitX) :
                print("Grow")
                FruitY = FruitSpaces.index(random.choice(FruitSpaces))
                FruitX = FruitSpaces[FruitY][random.randint(0, (len(FruitSpaces[FruitY])- 1))]
                UpdateBoard(Board, FruitY, FruitX, "F")
            else:
                SnakeTailY = SnakeTailY + 1

        elif Board[SnakeTailY][SnakeTailX - 1] == "0":

            if Grow(SnakeHeadY, SnakeHeadX, FruitY, FruitX) :
                print("Grow")
                FruitY = FruitSpaces.index(random.choice(FruitSpaces))
                FruitX = FruitSpaces[FruitY][random.randint(0, (len(FruitSpaces[FruitY])- 1))]
                UpdateBoard(Board, FruitY, FruitX, "F")
            else:
                SnakeTailX = SnakeTailX - 1

        elif Board[SnakeTailY][SnakeTailX + 1] == "0":

            if Grow(SnakeHeadY, SnakeHeadX, FruitY, FruitX) :
                print("Grow")
                FruitY = FruitSpaces.index(random.choice(FruitSpaces))
                FruitX = FruitSpaces[FruitY][random.randint(0, (len(FruitSpaces[FruitY])- 1))]
                UpdateBoard(Board, FruitY, FruitX, "F")
            else:
                SnakeTailX = SnakeTailX + 1
            
        GetPrintBoard(Board, PrintBoard)
        
    
SetUp(Board, PrintBoard, Snake)

SnakeMove(Board, PrintBoard, Snake, KeyStroke, Suggested_KeyStroke, SnakeHeadY, SnakeHeadX, SnakeTailY, SnakeTailX, FruitY, FruitX)

time.sleep(1000)
