import math

# Create Board
board = [' ' for _ in range(9)]

def print_board():
    for i in range(3):
        print('|'.join(board[i*3:(i+1)*3]))
        if i < 2:
            print('-'*5)

# Check Winner ke koi pattern banraha he yah nh in me se.
def check_winner(player):
    win_combos = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    return any(all(board[i] == player for i in combo) for combo in win_combos)

# Return karyga ke kon kon se moves bache he
def available_moves():
    return [i for i, val in enumerate(board) if val == ' ']

# Check koi jeeta yah nh
def is_terminal():
    return check_winner('X') or check_winner('O') or not available_moves()

# Master AI
def minimax(is_maximizing):
    if check_winner('O'):
        return {'score': 1}
    if check_winner('X'):
        return {'score': -1}
    if not available_moves():
        return {'score': 0}

    if is_maximizing:
        best = {'score': -math.inf}
        for move in available_moves():
            board[move] = 'O'
            sim = minimax(False)
            board[move] = ' '
            sim['move'] = move
            if sim['score'] > best['score']:
                best = sim
        return best
    else:
        best = {'score': math.inf}
        for move in available_moves():
            board[move] = 'X'
            sim = minimax(True)
            board[move] = ' '
            sim['move'] = move
            if sim['score'] < best['score']:
                best = sim
        return best

# Create best moves 
def ai_move():
    move = minimax(True)['move']
    board[move] = 'O'

# Game Loop
def play_game():
    print("You are X, Master AI is O. Let's play!")
    while not is_terminal():
        print_board()
        try:
            move = int(input("Enter your move (0-8): "))
            if board[move] != ' ':
                print("Invalid move. Try again.")
                continue
            board[move] = 'X'
        except:
            print("Invalid input.")
            continue

        if is_terminal():
            break

        ai_move()

    print_board()
    if check_winner('X'):
        print("You win! 🎉")
    elif check_winner('O'):
        print("AI wins! 🤖")
    else:
        print("It's a tie!")

play_game()
