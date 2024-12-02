# Function to create an empty board
def create_board():
    return [" " for _ in range(9)]

# Function to display the board
def display_board(board):
    print("\n")  # Add space
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("-" * 9)
    print("\n")  # Add space 

# Function to place a symbol
def place_symbol(board, position, symbol):
    if board[position - 1] == " ":  # Check if the box is empty
        board[position - 1] = symbol
        return True
    else:
        print("This box is already occupied. Try another one.")
        return False
