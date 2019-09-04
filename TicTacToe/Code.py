import random
import sys


def display_board(board):
    print("    |   |   ")
    print("  " + board[7] + " | " + board[8] + " | " + board[9])
    print("    |   |   ")
    print("-------------")
    print("    |   |   ")
    print("  " + board[4] + " | " + board[5] + " | " + board[6])
    print("    |   |   ")
    print("-------------")
    print("    |   |   ")
    print("  " + board[1] + " | " + board[2] + " | " + board[3])
    print("    |   |   ")


def player_input():
    marker = " "

    while not (marker == 'X' or marker == 'O'):
        marker = input("Player 1: Do you want to be X or O?\n").upper()

    if marker == 'X':
        return('X', 'O')
    else:
        return('O', 'X')


def place_marker(board, marker, position):

    board[position] = marker


def win_check(board, mark):

    if(board[1] == mark and board[2] == mark and board[3] == mark):
        return True

    elif(board[4] == mark and board[5] == mark and board[6] == mark):
        return True

    elif(board[7] == mark and board[8] == mark and board[9] == mark):
        return True

    elif(board[1] == mark and board[4] == mark and board[7] == mark):
        return True

    elif(board[2] == mark and board[5] == mark and board[8] == mark):
        return True

    elif(board[3] == mark and board[6] == mark and board[9] == mark):
        return True

    elif(board[1] == mark and board[5] == mark and board[9] == mark):
        return True

    elif(board[3] == mark and board[5] == mark and board[7] == mark):
        return True

    else:
        return False


def choose_first():

    player = random.randint(1, 2)

    if player == 1:
        print("Player 1 will go first")
        return 1
    else:
        print("player 2 will go first")
        return 2


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):

    counter = 0

    for i in board:
        if i == 'X' or i == 'O':
            counter += 1

    if counter > 9:
        return True
    else:
        return False


def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input("Please select your next position: (1-9)\n"))
    return position


def replay():
    ans = ' '
    while(ans[0].lower() != 'y' and ans[0].lower() != 'n'):
        ans = input("Do you want to play again?(Y/N)\n")

    return ans[0].lower() == 'y'


print('Welcome to Tic Tac Toe!\n')

while True:
    inp = ' '
    board = [' ']*10
    game_on = True
    player1_marker, player2_marker = player_input()
    player = choose_first()
    while not (inp[0].lower() == 'y'):
        inp = input("Are you ready to play?(Yes/No):\n").lower()
        if inp[0].lower() == 'y':
            break
        elif inp[0].lower() == 'n':
            sys.exit()

    while game_on:
        if player == 1:
            position = player_choice(board)
            place_marker(board, player1_marker, position)
            print('\n'*100)
            display_board(board)
            player = 2
            if win_check(board, player1_marker):
                print("Player 1 won...!")
                game_on = False
            if full_board_check(board):
                print("Tie game...!")
                game_on = False
        else:
            position = player_choice(board)
            place_marker(board, player2_marker, position)
            print('\n'*100)
            display_board(board)
            player = 1
            if win_check(board, player2_marker):
                print("Player 1 won...!")
                game_on = False
            if full_board_check(board):
                print("Tie game...!")
                game_on = False
    if not replay():
        break
