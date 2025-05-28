"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """

    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    player_x_count = sum(row.count(X) for row in board)
    player_o_count = sum(row.count(O) for row in board)
    if player_x_count > player_o_count:
        return O
    elif player_x_count < player_o_count:
        return X
    else:
        return X  # X starts first, so if counts are equal, it's X's turn


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                actions_set.add((i, j))

    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    # Check if action is within bounds
    if not (0 <= i < 3 and 0 <= j < 3):
        raise ValueError("Invalid action: Move is out of bounds.")
    if board[i][j] is not EMPTY:
        raise ValueError("Invalid action: Cell is already occupied.")

    new_board = [row.copy() for row in board]  # Create a copy of the board
    current_player = player(board)
    new_board[i][j] = current_player  # Place the current player's mark
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None  # No winner yet


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check if there's a winner or if the board is full
    if winner(board) is not None:
        return True

    # Check if the board is full
    if all(cell is not EMPTY for row in board for cell in row):
        return True

    return False  # Game is not over


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1

    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    turn = player(board)

    # X’s (maximizing) turn
    if turn == X:
        best_score = -math.inf
        best_action = None

        for action in actions(board):
            score = min_value(result(board, action))  # calls O’s turn
            if score > best_score:
                best_score, best_action = score, action  # fix order!

        return best_action

    # O’s (minimizing) turn
    else:
        best_score = math.inf
        best_action = None

        for action in actions(board):
            score = max_value(result(board, action))  # call X’s turn helper
            if score < best_score:
                best_score, best_action = score, action  # fix order!

        return best_action


def max_value(board):
    if terminal(board):
        return utility(board)
    value = -math.inf
    for action in actions(board):
        value = max(value, min_value(result(board, action)))
    return value


def min_value(board):
    if terminal(board):
        return utility(board)
    value = math.inf
    for action in actions(board):
        value = min(value, max_value(result(board, action)))
    return value
