# create the board 
board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' ',}   
player = 'o'
computer = 'x'

def printBoard(board):
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("-+-+-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-+-+-")
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("\n")  

# helper to determine if a position is available or not
def spaceIsFree(position):
    if board[position] == ' ':
        return True 
    return False

#function to insert a letter x or o for the tic tac toe and its position
def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)
        if checkDraw():
            print("Draw!")
            exit()
        if checkWin():
            if letter == 'x':
                print("Bot wins!")
                exit()
            else:
                print("Player wins!")
                exit()
        return 
    else:
        print("Invalid position")
        position = int(input("please enter a new position: "))
        insertLetter(letter, position)
        return

# to check the winning conditions
def checkWin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '): 
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False
    
# to check the draw conditions
def checkDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True

def playerMove() :
    position = int(input("Enter a position for 'o': "))
    insertLetter(player, position)
    return

# computer/bot move
def compMove() :
    position = int(input("enter a position for 'x' : "))
    insertLetter(computer, position)
    return


# game loop
while not checkWin():
    compMove()
    playerMove()
