import math

# Initialize the board
board = [" " for _ in range(9)]

# Function to print the current state of the board
def print_board():
    print("\n")
    for i in range(3):
        row = board[i*3:(i+1)*3]
        print("| " + " | ".join(row) + " |")
    print("\n")

# Check for a winner
def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] == player:
            return True
    return False

def is_full():
    return " " not in board

# Minimax algorithm
def minimax(is_maximizing):
    if check_winner("O"):
        return 1
    elif check_winner("X"):
        return -1
    elif is_full():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

# AI Move
def ai_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"

# Main game loop
def play_game():
    print("Welcome to AI Tic-Tac-Toe!")
    print_board()

    while True:
        # Player move
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] != " ":
                print("Invalid move! Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input! Enter a number between 1-9.")
            continue
        board[move] = "X"
        
        print_board()

        if check_winner("X"):
            print("You win!")
            break
        if is_full():
            print("It's a tie!")
            break

        # AI move
        ai_move()
        print("AI has made its move:")
        print_board()

        if check_winner("O"):
            print("AI wins!")
            break
        if is_full():
            print("It's a tie!")
            break

# Start Game
play_game()
