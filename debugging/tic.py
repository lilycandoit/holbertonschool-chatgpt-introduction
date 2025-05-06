#!/usr/bin/python3

# Function to print the current state of the game board
def print_board(board):
    for row in board:
        print(" | ".join(row))  # Join cells with vertical bars
        print("-" * 5)          # Print a horizontal line after each row

# Function to check if there's a winner
def check_winner(board):
    # Check rows for a win
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":  # All 3 cells match and are not empty
            return True

    # Check columns for a win
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    # Check top-left to bottom-right diagonal
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True

    # Check top-right to bottom-left diagonal
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False  # No winner yet

# Function to check if the board is completely filled (a draw)
def is_full(board):
    for row in board:
        if " " in row:  # If any cell is still empty, return False
            return False
    return True  # All cells are filled

# Main game loop
def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]  # Create 3x3 grid filled with spaces
    player = "X"  # Player "X" starts the game

    while True:
        print_board(board)  # Show current board state

        try:
            # Get player move
            row = int(input(f"Enter row (0, 1, 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, 2) for player {player}: "))
        except ValueError:
            print("⚠️ Invalid input. Please enter numbers.")  # Handles non-number input
            continue  # Go back to the start of the loop

        # Check if row and col are within valid range
        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("⚠️ Coordinates must be between 0 and 2.")
            continue

        # Check if the cell is already taken
        if board[row][col] != " ":
            print("⚠️ That spot is already taken!")
            continue

        # Place the player's mark on the board
        board[row][col] = player

        # Check for a win after the move
        if check_winner(board):
            print_board(board)
            print(f"🎉 Player {player} wins!")
            break  # End the game

        # Check for draw
        if is_full(board):
            print_board(board)
            print("🤝 It's a draw!")
            break  # End the game

        # Switch to the other player
        player = "O" if player == "X" else "X"

# Start the game
tic_tac_toe()
