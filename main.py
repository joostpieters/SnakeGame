import time
import msvcrt
from Board import *

KeyStroke = b"a"

Snake = ""
Speed = 1

SnakeHeadY = 12
SnakeHeadX = 35

SnakeTailY = 12
SnakeTailX = 39


def SetUp(Board, PrintBoard, Snake) :

    Snake = ":0000"
    y = 12
    x = 35
    
    for i in Snake:
        UpdateBoard(Board, y, x, i)
        x +=1
    GetPrintBoard(Board, PrintBoard)

def SnakeMove(Board, PrintBoard, Snake, KeyStroke, SnakeHeadY, SnakeHeadX, SnakeTailY, SnakeTailX):
    while True :

        time.sleep(Speed)

        if msvcrt.kbhit():
            KeyStroke = msvcrt.getch()

        if KeyStroke == b"w" :
            UpdateBoard(Board, SnakeHeadY - 1, SnakeHeadX, '"')
            UpdateBoard(Board, SnakeHeadY, SnakeHeadX, "0")
            SnakeHeadY = SnakeHeadY - 1

            UpdateBoard(Board, SnakeTailY, SnakeTailX, " ")
            SnakeTailY = SnakeTailY - 1
   
        elif KeyStroke == b"a" :

            UpdateBoard(Board, SnakeHeadY, SnakeHeadX - 1, ":")
            UpdateBoard(Board, SnakeHeadY, SnakeHeadX, "0")
            SnakeHeadX = SnakeHeadX - 1

            UpdateBoard(Board, SnakeTailY, SnakeTailX, " ")
            SnakeTailX = SnakeTailX - 1

        elif KeyStroke == b"s" :
            pass

        elif KeyStroke == b"d" :
            pass    

        GetPrintBoard(Board, PrintBoard)
            
MakeBoard(Board, Board_Height, Board_Length)
SetUp(Board, PrintBoard, Snake)

SnakeMove(Board, PrintBoard, Snake, KeyStroke, SnakeHeadY, SnakeHeadX, SnakeTailY, SnakeTailX)

time.sleep(1000)
