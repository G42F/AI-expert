import random
from colorama import init, Fore,Style

init(autoreset=True)




# Initialize the Tic Tac Toe boardboard = [' ' for _ in range(9)]board = [' ' for _ in range(9)]
# Initialize the Tic Tac Toe board
def display_board(board):
    print()
    def colored_cell(cell):
        if cell == 'X':
            return Fore.RED + cell + style.RESET_ALL
        elif cell == 'O':
            return Fore.BLUE + cell + style.RESET_ALL
        else:
            return cell
    print(Fore.CYAN + f" {board[0]} | {board[1]} | {board[2]} ")
    print(Fore.CYAN + "---|---|---")
    print(Fore.CYAN + f" {board[3]} | {board[4]} | {board[5]} ")
    print(Fore.CYAN + "---|---|---")
    print(Fore.CYAN + f" {board[6]} | {board[7]} | {board[8]} ")

def player_choice(board):
    symbol=''

    while symbol not in ['X', 'O']:
        symbol = input(Fore.YELLOW + "Choose your symbol (X/O): ").upper()
    if symbol == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def player_move(board, symbol):
    move = -1
    while move not in range(1, 10) or board[move - 1] != ' ':
        try:
            move = int(input(Fore.YELLOW + f"Enter your move (1-9) for {symbol}: "))
        except ValueError:
            continue
    board[move - 1] = symbol

def ai_move(board, ai_symbol, player_symbol):
    # Simple AI: choose a random available spot
    available_moves = [i for i, spot in enumerate(board) if spot == ' ']
    move = random.choice(available_moves)
    board[move] = ai_symbol

def check_winner(board, symbol):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == symbol for i in condition):
            return True
    return False
def check_full(board):
    return all(spot != ' ' for spot in board)

def tic_tac_toe():
    board = [' ' for _ in range(9)]
    player_symbol, ai_symbol = player_choice(board)
    current_turn = 'Player' if player_symbol == 'X' else 'AI'

    while True:
        display_board(board)
        if current_turn == 'Player':
            player_move(board, player_symbol)
            if check_winner(board, player_symbol):
                display_board(board)
                print(Fore.GREEN + "Congratulations! You win!")
                break
            current_turn = 'AI'
        else:
            ai_move(board, ai_symbol, player_symbol)
            if check_winner(board, ai_symbol):
                display_board(board)
                print(Fore.RED + "AI wins! Better luck next time.")
                break
            current_turn = 'Player'
        
        if check_full(board):
            display_board(board)
            print(Fore.YELLOW + "It's a tie!")
            break
    play_again = input(Fore.YELLOW + "Play again? (yes/no): ").lower()
    if play_again != 'yes':
        print(Fore.CYAN + "Thanks for playing Tic Tac Toe!")
        print(Fore.CYAN + "")
        return
    
if __name__ == "__main__":
    tic_tac_toe()
        