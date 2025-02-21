import numpy as np
from game import PLAYER, AI

ROW_COUNT, COLUMN_COUNT = 6, 6

def evaluate_window(window, piece):
    """
    Evaluate a list of 4 board cells (window) and return a score.
    Positive scores favor the given piece; negative scores penalize.
    """
    score = 0
    opp_piece = PLAYER if piece == AI else AI

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(0) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(0) == 2:
        score += 2
    if window.count(opp_piece) == 3 and window.count(0) == 1:
        score -= 4

    return score


def score_position(board, piece):
    """
    Score the board based on the potential for the given piece to win.
    This function can be used by AI algorithms to evaluate board states.
    """
    score = 0

    # Score center column: encourage occupying the center
    center_array = [int(i) for i in list(board[:, COLUMN_COUNT // 2])]
    center_count = center_array.count(piece)
    score += center_count * 3

    # Score horizontal locations
    for r in range(ROW_COUNT):
        row_array = [int(i) for i in list(board[r, :])]
        for c in range(COLUMN_COUNT - 3):
            window = row_array[c:c + 4]
            score += evaluate_window(window, piece)

    # Score vertical locations
    for c in range(COLUMN_COUNT):
        col_array = [int(i) for i in list(board[:, c])]
        for r in range(ROW_COUNT - 3):
            window = col_array[r:r + 4]
            score += evaluate_window(window, piece)

    # Score positively sloped diagonals
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            window = [board[r + i][c + i] for i in range(4)]
            score += evaluate_window(window, piece)

    # Score negatively sloped diagonals
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            window = [board[r + 3 - i][c + i] for i in range(4)]
            score += evaluate_window(window, piece)

    return score


# Function to evaluate the utility of a given window of 4 cells
def score_window(window, piece):
    """Score a window of four cells."""
    score = 0
    opponent = PLAYER if piece == AI else AI

    # If the AI has four in a row, it's a winning move
    if window.count(piece) == 4:
        score += 100
    # If the AI has three pieces in a row and one empty space
    elif window.count(piece) == 3 and window.count(0) == 1:
        score += 5
    # If the AI has two pieces in a row and two empty spaces
    elif window.count(piece) == 2 and window.count(0) == 2:
        score += 2
    # If the opponent has three pieces in a row and one empty space, block it
    elif window.count(opponent) == 3 and window.count(0) == 1:
        score -= 50  # Heavy penalty for allowing opponent to win

    return score


def evaluate_board(board, piece):
    """Evaluate the board and return a score based on potential winning moves and threats."""
    score = 0
    ROW_COUNT, COLUMN_COUNT = board.shape
    # Evaluate horizontal windows
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT - 3):
            window = [board[r][c], board[r][c + 1], board[r][c + 2], board[r][c + 3]]
            score += score_window(window, piece)

    # Evaluate vertical windows
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            window = [board[r][c], board[r + 1][c], board[r + 2][c], board[r + 3][c]]
            score += score_window(window, piece)

    # Evaluate diagonal windows
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            window = [board[r][c], board[r + 1][c + 1], board[r + 2][c + 2], board[r + 3][c + 3]]
            score += score_window(window, piece)

    for r in range(3, ROW_COUNT):
        for c in range(COLUMN_COUNT - 3):
            window = [board[r][c], board[r - 1][c + 1], board[r - 2][c + 2], board[r - 3][c + 3]]
            score += score_window(window, piece)

    return score
