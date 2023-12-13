# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

#from logic import make_empty_board, get_winner, other_player
from logic import *


# Reminder to check all the tests

if __name__ == '__main__':
    game = TicTacTocGame()          #board = empty_board, winner = None, sign = 'X'

    game_mode = input("Choose game mode: \n 1. Single Player \n 2. Two Players \n")
    dic_game_mode = {"1": "Single Player", "2": "Two Players"}
    game.mode = dic_game_mode[str(game_mode)]
    if game_mode == "1":
        bot = BotPlayer()
        player = input("Choose your sign: X or O (X goes first)\n")
        game.print_board()
        if player == "X":
            while game.get_winner() == None:
                print('Take your turn(X)')
                pos_x, pos_y = input("Enter a position(x,y), split with space: ").split()
                game.board[int(pos_x)][int(pos_y)] = player

                #get first move
                if game.is_board_empty():
                    game.first_move["player"] = player
                    game.first_move["position"] = [int(pos_x), int(pos_y)]

                game.print_board()
                #print(game.get_winner())
                if game.get_winner() == None:
                    pos_x, pos_y = bot.make_move(game.board)
                    game.board[pos_x][pos_y] = "O"
                    print('Bot\'s turn(O)')
                    game.print_board()
            if game.get_winner() == None:
                game.player == "draw"
        elif player == "O":
            while game.get_winner() == None:
                pos_x, pos_y = bot.make_move(game.board)
                game.board[pos_x][pos_y] = "X"
                print('Bot\'s turn(X)')
                game.print_board()
                if game.get_winner() == None:
                    print('Take your turn(O)')
                    pos_x, pos_y = input("Enter a position(x,y), split with space: ").split()
                    game.board[int(pos_x)][int(pos_y)] = player
                    game.print_board()
            if game.get_winner() == None:
                game.player == "draw"
        game.save_to_log()
    if game_mode == "2":
        while game.get_winner() == None:
            game.print_board()
            print(f"take a turn!({game.player})")
            pos_x, pos_y = input("Enter a position(x,y), split with space: ").split()
            game.board[int(pos_x)][int(pos_y)] = game.player
            if game.get_winner() == None:
                game.other_player()
        if game.get_winner() == None:
            game.player == "draw"
        game.print_board()
        game.save_to_log()
    print(f"{game.get_winner()} wins!")
