import os
import time
from Board import *
#from ReadKeyStrokes import KeyStroke

#os.startfile('ReadKeyStrokes.py')
Snake = ":0000"
def SetUp(Board, PrintBoard, Snake) :

    KeyStroke = "A"
    Snake = ":0000"
    y = 3
    x = 1

    
    for i in Snake:
        UpdateBoard(Board, PrintBoard, y, x, i)
        x +=1

MakeBoard(Board, Board_Height, Board_Length)
SetUp(Board, PrintBoard, Snake)
time.sleep(1000)
