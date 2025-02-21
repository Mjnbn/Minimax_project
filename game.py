import numpy as np

# Board dimensions and player definitions
# ROW_COUNT = 9
# COLUMN_COUNT = 10

PLAYER = 1  # Human player
AI = 2      # AI player

class ConnectFourGame:
    def __init__(self, ROW_COUNT, COLUMN_COUNT):
        self.ROW_COUNT = ROW_COUNT
        self.COLUMN_COUNT = COLUMN_COUNT
        self.board = np.zeros((ROW_COUNT, COLUMN_COUNT), dtype=int)
        self.game_over = False
        self.winner = None


    def drop_piece(self, row, col, piece):
        """Place a piece in the board at the given row and column."""
        self.board[row][col] = piece

    def is_valid_location(self, col):
        """Check if the top cell in the column is empty (i.e., valid move)."""
        return self.board[self.ROW_COUNT - 1][col] == 0

    def get_valid_locations(self):
        """Return a list of column indices that are valid for a move."""
        return [col for col in range(self.COLUMN_COUNT) if self.is_valid_location(col)]

    def get_next_open_row(self, col):
        """Return the next open row in the given column."""
        for r in range(self.ROW_COUNT):
            if self.board[r][col] == 0:
                return r
        return None

    def winning_move(self, piece):
        """Check all board positions for a winning move by the given piece."""
        # Check horizontal locations for win
        for c in range(self.COLUMN_COUNT - 3):
            for r in range(self.ROW_COUNT):
                if (self.board[r][c] == piece and
                        self.board[r][c + 1] == piece and
                        self.board[r][c + 2] == piece and
                        self.board[r][c + 3] == piece):
                    return True

        # Check vertical locations for win
        for c in range(self.COLUMN_COUNT):
            for r in range(self.ROW_COUNT - 3):
                if (self.board[r][c] == piece and
                        self.board[r + 1][c] == piece and
                        self.board[r + 2][c] == piece and
                        self.board[r + 3][c] == piece):
                    return True

        # Check positively sloped diagonals
        for c in range(self.COLUMN_COUNT - 3):
            for r in range(self.ROW_COUNT - 3):
                if (self.board[r][c] == piece and
                        self.board[r + 1][c + 1] == piece and
                        self.board[r + 2][c + 2] == piece and
                        self.board[r + 3][c + 3] == piece):
                    return True

        # Check negatively sloped diagonals
        for c in range(self.COLUMN_COUNT - 3):
            for r in range(3, self.ROW_COUNT):
                if (self.board[r][c] == piece and
                        self.board[r - 1][c + 1] == piece and
                        self.board[r - 2][c + 2] == piece and
                        self.board[r - 3][c + 3] == piece):
                    return True

        return False
    def is_draw(self):
        """Check if the board is full (draw condition)."""
        return len(self.get_valid_locations()) == 0

    def reset(self):
        """Reset the board to start a new game."""
        self.board = np.zeros((self.ROW_COUNT, self.COLUMN_COUNT), dtype=int)
        self.game_over = False
        self.winner = None
