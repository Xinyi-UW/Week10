def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""
    #check rows
    for row in board:
        if row[0]==row[1]==row[2]:
            output = row[0]
        else:
            output = None
    #check columns
    for i in range(3):
        if board[0][i]==board[1][i]==board[2][i]:
            output = board[0][i]
        #check diagonals
        if board[0][0]==board[1][1]==board[2][2] or board[2][0]==board[1][1]==board[2][0]:
            output = board[1][1]
    return output  # FIXME


def other_player(player):
    """Given the character for a player, returns the other player."""
    if player == "X":
        player = "O"
        #return "O"
    elif player == "O":
        player = "X"
        #return "X"

def is_board_full(board):
    return all(all(cell is not None for cell in row) for row in board)

def is_valid_move(board, row, col):
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] is None
