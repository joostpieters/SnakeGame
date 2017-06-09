import Board

PrintBoard = """ """

MakeBoard(Board, Board_Height, Board_Length)

for y in range (Board_Height):
  for x in range(Board_Length):
    PrintBoard += Board[y][x]
  
  PrintBoard += "\n"
  
PrintBoard += 'end="\r"'
print(PrintBoard)
