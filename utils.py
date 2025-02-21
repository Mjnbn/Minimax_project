import numpy as np
from game import PLAYER, AI

ROW_COUNT, COLUMN_COUNT = 6, 6

def evaluate_window(window, piece):
    """
    Evaluate a list of 4 board cells (window) and return a score.
    Positive scores favor the given piece; negative scores penalize.
    """

    #TODO



def score_position(board, piece):
    """
    Score the board based on the potential for the given piece to win.
    This function can be used by AI algorithms to evaluate board states.
    """
    # TODO


# Function to evaluate the utility of a given window of 4 cells
def score_window(window, piece):
    """Score a window of four cells."""
    # TODO


def evaluate_board(board, piece):
    """Evaluate the board and return a score based on potential winning moves and threats."""
    # TODO
