# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.

class TicTacTocGame():
    LOG_FILE_PATH = 'logs/tictactoe_log.csv'

    def __init__(self):
        self.board = self.make_empty_board()
        self.player = "X"
        self.winner = None
        self.mode = None
        self.first_move = {"player": None, "position": None}


    def get_winner(self):
        """Determines the winner of the given board.
        Returns 'X', 'O', or None."""
        #check rows
        for row in self.board:
            if row[0]==row[1]==row[2] and row[0] is not None and row[1] is not None and row[2] is not None:
                output = row[0]
                self.winner = output
            else:
                output = None
        #check columns
        for i in range(3):
            if self.board[0][i]==self.board[1][i]==self.board[2][i] and self.board[0][i] is not None and self.board[1][i] is not None and self.board[2][i] is not None:
                output = self.board[0][i]
                self.winner = output
            #check diagonals
            if self.board[0][0]==self.board[1][1]==self.board[2][2] or self.board[2][0]==self.board[1][1]==self.board[2][0] and self.board[1][1] is not None:
                output = self.board[1][1]
                self.winner = output
        return output  # FIXME
    
    def save_to_log(self):
        import csv
        import os
        if self.winner is not None:
            with open(self.LOG_FILE_PATH, 'a') as f:
                writer = csv.writer(f)
                if not os.path.isfile(self.LOG_FILE_PATH):
                    writer.writerow(['Mode', 'Winner'])
                writer.writerow([self.mode, self.winner])
        print("Game saved to log!")


    def other_player(self):
        """Given the character for a player, returns the other player."""
        if self.player == "X":
            self.player = "O"
            #return "O"
        elif self.player == "O":
            self.player = "X"
            #return "X"
        
        '''
    def print_board(self):
        """Prints the board."""
        for row in self.board:
            print(row)
        #print('\n')
        '''

    def print_board(self):
        max_width = max(len(str(cell)) for row in self.board for cell in row)

        for row in self.board:
            for cell in row:
                cell_str = str(cell) if cell is not None else " "
                print(cell_str.ljust(max_width), end=" | ")
            print("\n" + "- " * max_width * 3)
    
    def is_board_empty(self):
        """Returns True if the board is empty."""
        for row in self.board:
            for cell in row:
                if cell is not None:
                    return False
        return True


class BotPlayer():
    def __init__(self):
        pass

    def make_move(self, board):
        """Given a board, returns a move."""
        #find empty space (x,y)
        empty_space = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == None:
                    empty_space.append((i,j))
        #randomly pick one
        import random
        return random.choice(empty_space)
