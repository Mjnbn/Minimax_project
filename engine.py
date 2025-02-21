"""
engine.py

AI Algorithms: Implement the following functions:

- minimax
- alpha_beta_pruning
- expectimax

Each function should evaluate board states using a heuristic (see utils.py)
and return the best column to play.
"""
from termios import TIOCPKT_DOSTOP

from utils import evaluate_board
from game import ConnectFourGame, PLAYER, AI
ROW_COUNT, COLUMN_COUNT = 6,6
def minimax(game, depth, maximizing_player):
    """
    Minimax algorithm to determine the best move.

    :param game: Current game object (contains board state and methods).
    :param depth: Depth limit for recursion.
    :param maximizing_player: Boolean indicating if AI is maximizing.
    :return: Best column to play.
    """
    # TODO


def alpha_beta_pruning(game, depth, alpha, beta, maximizing_player):
    """
    Alpha-Beta Pruning to optimize Minimax.

    :param game: Current game object (contains board state and methods).
    :param depth: Depth limit for recursion.
    :param alpha: Alpha value.
    :param beta: Beta value.
    :param maximizing_player: Boolean indicating if AI is maximizing.
    :return: Best column to play.
    """

    # TODO


def expectimax(game, depth, maximizing_player):
    """
    Expectimax algorithm for environments with randomness.

    :param game: Current game object (contains board state and methods).
    :param depth: Depth limit for recursion.
    :param maximizing_player: Boolean indicating if AI is maximizing.
    :return: Best column to play.
    """

    # TODO