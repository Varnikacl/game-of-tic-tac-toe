import random

board = [' '] * 9

def print_board():
    for i in range(0, 9, 3):
        print(board[i], '|', board[i+1], '|', board[i+2])

def check_win(player):
    combos = [(0,1,2), (3,4,5), (6,7,8),
              (0,3,6), (1,4,7), (2,5,8),
              (0,4,8), (2,4,6)]
    return any(board[a]==board[b]==board[c]==player for a,b,c in combos)

def player_move():
    move = int(input("Enter position (1-9): ")) - 1
    if board[move] == ' ':
        board[move] = 'X'

def computer_move():
    choices = [i for i in range(9) if board[i] == ' ']
    move = random.choice(choices)
    board[move] = 'O'

while ' ' in board:
    print_board()
    player_move()
    if check_win('X'):
        print_board()
        print("You win!")
        break
    if ' ' not in board: break
    computer_move()
    if check_win('O'):
        print_board()
        print("Computer wins!")
        break
else:
    print("It's a draw!")