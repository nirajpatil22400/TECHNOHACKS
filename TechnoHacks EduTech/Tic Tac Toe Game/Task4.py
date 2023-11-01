# Initialize the game board
board = [[' ' for _ in range(3)] for _ in range(3)]

# Function to display the game board


def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def get_player_move(player):
    while True:
        try:
            move = input(f"Player {player}, enter your move (row, column): ")
            row, col = map(int, move.split(','))
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                return row, col
            else:
                print("Invalid move. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid move.")

# Example usage:
# row, col = get_player_move(1)


def check_win(player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def play_tic_tac_toe():
    player = 'X'
    moves = 0
    while True:
        display_board(board)
        row, col = get_player_move(player)
        board[row][col] = player
        moves += 1

        if check_win(player):
            display_board(board)
            print(f"Player {player} wins!")
            break
        if moves == 9:
            display_board(board)
            print("It's a draw!")
            break

        player = 'O' if player == 'X' else 'X'


# Start the game:
play_tic_tac_toe()
