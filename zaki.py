from colorama import Fore, Style
import time
import random
import copy


rows = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

Board_size = 4

Yellow_start = Fore.YELLOW + Style.BRIGHT

Cyan_start = Fore.CYAN + Style.BRIGHT

green_start = Fore.GREEN + Style.BRIGHT

Purple_start = Fore.MAGENTA + Style.BRIGHT

Red_start = Fore.RED + Style.BRIGHT

Colour_end = Style.RESET_ALL


def tutorial():
    print(Cyan_start,"How to play:" , Colour_end, "\nUse ",Yellow_start, "WASD", Colour_end ," to merge identical blocks")
    time.sleep(1)
    print("Identical blocks will add together to form a larger block (eg 2→2 = 4)")
    time.sleep(1)
    print("Every movement will spawn either a 2 or a 4 on a random empty space")
    time.sleep(1)
    print("Keep playing until you create", Yellow_start, "2048", Colour_end," or run out of space!")
    print()

def display_board():
    largestValue = rows[0][0]
    for row in rows:
        for block in row:
            if block > largestValue:
                largestValue = block
    
    Spaces = len(str(largestValue))

    for row in rows:
        currentRow = "|"
        for block in row:
            if block == 0:
                currentRow += " " * Spaces + "|"
            else: 
                currentRow += (" " * (Spaces - len(str(block)))) + str(block) + "|"
        print(currentRow)

def MergeOneRowLeft(row):
    for x in range(Board_size - 1):
        for i in range(Board_size - 1, 0, -1):
            if row[i-1] == 0:
                row[i-1] = row[i]
                row[i] = 0
    
    for i in range(Board_size-1):
        if row[i] == row[i+1]:
            row[i] *= 2
            row[i+1] = 0

    for i in range(Board_size - 1, 0, -1):
        if row[i-1] == 0:
            row[i-1] = row[i]
            row[i] = 0

    return row
    
def MergeLeft(New_Board):
    for i in range(Board_size):
        New_Board[i] = MergeOneRowLeft(New_Board[i])
    return New_Board

def reverseOrders(row):
    ReversedBoard = []
    for i in range (Board_size -1, -1, -1):
        ReversedBoard.append(row[i])
    return ReversedBoard

def MergeRight(New_Board):
    for i in range(Board_size):
        New_Board[i] = reverseOrders(New_Board[i])
        New_Board[i] = MergeOneRowLeft(New_Board[i])
        New_Board[i] = reverseOrders(New_Board[i])
    return New_Board


def TransposeBoard(New_Board):
    for i in range(Board_size):
        for j in range (i, Board_size):
            if j != i:
                temporary = New_Board[i][j]
                New_Board[i][j] = New_Board[j][i]
                New_Board[j][i] = temporary

                
    return New_Board

def MergeDown(New_Board):
    
    New_Board = TransposeBoard(New_Board)
    
    New_Board = MergeRight(New_Board)
    
    New_Board = TransposeBoard(New_Board) 
    return New_Board

def MergeUp(New_Board):
    New_Board = TransposeBoard(New_Board)
    
    New_Board = MergeLeft(New_Board)
    
    New_Board = TransposeBoard(New_Board) 
    return New_Board

def NewNum():
    if random.randint(1,5) == 1:
        return 4
    else:
        return 2

def AddNew():
    RowNum = random.randint(0, Board_size - 1)
    ColumnNum = random.randint(0, Board_size - 1)

    while not rows[RowNum][ColumnNum] == 0:
        RowNum = random.randint(0, Board_size - 1)
        ColumnNum = random.randint(0, Board_size - 1)
    
    rows[RowNum][ColumnNum] = NewNum()

def Win():
    for row in rows:
        if 2048 in row:
            return True
    return False

def NoSpaceLeft():
    BoardCopy1 = copy.deepcopy(rows)
    BoardCopy2 = copy.deepcopy(rows)
    MergeDown(BoardCopy1)

    if BoardCopy1 == BoardCopy2:
        MergeUp(BoardCopy1)
        if BoardCopy1 == BoardCopy2:
            MergeLeft(BoardCopy1)
            if BoardCopy1 == BoardCopy2:
                MergeRight(BoardCopy1)
                if BoardCopy1 == BoardCopy2:
                    return True
                
    return False

rows = []

for i in range(Board_size):
    row = []
    for x in range (Board_size):
        row.append(0)
    rows.append(row)

Starting_Amount = 2
while Starting_Amount > 0:
    RowNum = random.randint(0, Board_size - 1)
    ColumnNum = random.randint(0, Board_size - 1)
    if rows[RowNum][ColumnNum] == 0:
        rows[RowNum][ColumnNum] = NewNum()
        Starting_Amount -= 1

def CountScore():
    score = sum(sum(num)for num in rows)
    print("Your score is")
    time.sleep(1)
    print(Yellow_start, score, Colour_end)

def Game():
    print(green_start,"Lets begin!", Colour_end)
    time.sleep(1.5)
    display_board()

    GameOver = False

    while not GameOver:
        movement =  input("Your move: ")
    
        movement = movement.lower()

        ValidMove = True

        BoardCopy = copy.deepcopy(rows)

        if movement == "a":
            MergeLeft(rows)
        elif movement == "s":
            MergeDown(rows)
        elif movement == "w":
            MergeUp(rows)
        elif movement == "d":
            MergeRight(rows)
        else:
            ValidMove = False
        
        if ValidMove == False:
            print(Red_start,"Thats not a move. ",Colour_end)

        else:
            if rows == BoardCopy:
                print(Red_start, "That doesn't change anything.", Colour_end)
            else:
                if Win():
                    display_board()
                    time.sleep(0.5)
                    print(Yellow_start,"YOU GOT 2048!", Colour_end)
                    time.sleep(0.5)
                    print(green_start,"YOU WON!!",Colour_end)
                    CountScore()
                    GameOver = True
                else: 
                    AddNew()
                    display_board()

                    if NoSpaceLeft():
                        print(Red_start,"Game Over!")
                        time.sleep(1)
                        print("You ran out of space!",Colour_end)
                        time.sleep(1)
                        print()
                        CountScore()
                        GameOver = True
            

def main_menu():
    print(Yellow_start,"Welcome to...")
    time.sleep(0.6)
    print("""
╔═══╦═══╦╗─╔╦═══╗
║╔═╗║╔═╗║║─║║╔═╗║
╚╝╔╝║║║║║╚═╝║╚═╝║
╔═╝╔╣║║║╠══╗║╔═╗║
║║╚═╣╚═╝║──║║╚═╝║
╚═══╩═══╝──╚╩═══╝""",Colour_end)
    time.sleep(0.6)
    print(green_start,"[Play]",Colour_end)
    time.sleep(0.5)
    print(Cyan_start,"[Tutorial]", Colour_end)
    time.sleep(0.5)
    choice = input("What would you like to do?\n")
    choice = choice.lower()

    while choice != "tutorial" and choice != "play":
        choice = input(Red_start + "Thats not an option, input again: " + Colour_end)
        choice = choice.lower()

    if choice == "tutorial":
        tutorial()
    Game()

main_menu()
# when milestone reached:
# git stage *
# git commit -m "blahblahlal"
# git push