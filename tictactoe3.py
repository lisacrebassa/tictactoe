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
# Function to check if a player has won
def check_winner(board, symbol):
    winning_combinations = [
        [0, 1, 2],  # Rows
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],  # Columns
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],  # Diagonals
        [2, 4, 6]
    ]
    for combination in winning_combinations:
        if all(board[i] == symbol for i in combination):
            return True
    return False
# Function to check if the board is full
def is_full(board):
    return all(box != " " for box in board)
