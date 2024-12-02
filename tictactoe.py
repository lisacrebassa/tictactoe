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

