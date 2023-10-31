"""tic-tac-toe game"""
import sys


# function for displaying the playing field
def print_board(board):
    print("---------")
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(cell, end=" ")
        print("|")
    print("---------")


# function to check the status of the game
def check_game_state(board):
    # check rows, columns, and diagonals for a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return board[i][0] + " wins"
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return board[0][i] + " wins"
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0] + " wins"
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2] + " wins"

    # check for a draw
    if all(cell != " " for row in board for cell in row):
        return "Draw"

    # the game is still on
    return "Game not finished"


# function for displaying a message informing about the impossible state of the game
def print_impossible():
    print("Impossible")


# function to update the playing field after a user's move
def make_user_move(board, move, player):
    row, col = move
    if board[row - 1][col - 1] == " ":
        board[row - 1][col - 1] = player
    else:
        print("This cell is occupied! Choose another one!")


# basic code for the game
def play_game():
    game_board = [[" " for _ in range(3)] for _ in range(3)]
    print_board(game_board)

    # The starting player is "X"
    current_player = "X"

    # until the game is over, we move between players step by step
    while check_game_state(game_board) == "Game not finished":
        while True:
            move_input = input("Enter the coordinates for {}: ".format(current_player))
            if move_input.count(" ") != 1:
                print("You should enter two numbers separated by a single space.")
                continue

            try:
                user_move = tuple(map(int, move_input.split()))
            except ValueError:
                print("You should enter numbers!")
                continue

            if not (1 <= user_move[0] <= 3) or not (1 <= user_move[1] <= 3):
                print("Coordinates should be from 1 to 3!")
                continue

            if game_board[user_move[0] - 1][user_move[1] - 1] != " ":
                print("This cell is occupied! Choose another one!")
            else:
                make_user_move(game_board, user_move, current_player)
                print_board(game_board)
                break

        # changing the player
        current_player = "X" if current_player == "0" else "0"

    # after the game is over, print the result
    print(check_game_state(game_board))
    print('')


# game menu
def main_menu():
    print("""
█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█
▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█""")
    print("""
████████╗██╗██╗░░██╗  ████████╗░█████╗░██╗░░██╗  ████████╗░█████╗░███████╗
╚══██╔══╝██║██║░██╔╝  ╚══██╔══╝██╔══██╗██║░██╔╝  ╚══██╔══╝██╔══██╗██╔════╝
░░░██║░░░██║█████═╝░  ░░░██║░░░███████║█████═╝░  ░░░██║░░░██║░░██║█████╗░░
░░░██║░░░██║██╔═██╗░  ░░░██║░░░██╔══██║██╔═██╗░  ░░░██║░░░██║░░██║██╔══╝░░
░░░██║░░░██║██║░╚██╗  ░░░██║░░░██║░░██║██║░╚██╗  ░░░██║░░░╚█████╔╝███████╗
░░░╚═╝░░░╚═╝╚═╝░░╚═╝  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝  ░░░╚═╝░░░░╚════╝░╚══════╝""")

    # if the player enters "play", the game starts, and if "exit", the program ends
    while True:
        print('Type "play" to play the game, "exit" to quit: ')
        choice = input('> ').lower()
        if choice == 'play':
            play_game()
        elif choice == 'exit':
            print("Goodbye!")
            sys.exit()
        else:
            print("Incorrect selection. Enter 'play' or 'exit'.")


if __name__ == "__main__":
    main_menu()
