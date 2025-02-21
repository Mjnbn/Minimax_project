


# Connect Four AI Project

This project is an implementation of Connect Four using Python and Pygame. The project is organized into multiple files to separate the game logic, graphical interface, AI algorithms, and utility functions. Students are encouraged to experiment with and implement various AI algorithms (Minimax, Alpha-Beta Pruning, and Expectimax) in the `engine.py` file.

## Project Structure

```
connect_four/
├── engine.py         # AI algorithms (implement your AI functions here)
├── game.py           # Game rules and board logic
├── gui.py            # Pygame graphical rendering
├── main.py           # Main game loop and execution
├── utils.py          # Helper functions for board evaluation and move generation
├── README.md         # Project instructions and guidelines
└── requirements.txt  # Dependencies (pygame, numpy)
```

## Requirements

- Python 3.x
- Pygame
- Numpy

Install the required dependencies with:

```bash
pip install -r requirements.txt
```

## How to Run

Start the game by running:

```bash
python main.py
```

## Game Modes and Controls

- **Human vs. AI:** Click on a column in the game window to drop your piece.
- **AI vs. AI:** Modify the main loop in `main.py` to have both players controlled by the AI algorithms.
- **Restart:** Click on the "Restart" button (displayed in the upper-right corner) to reset the game.

## AI Implementation

In `engine.py`, you will find the following function stubs:

- `minimax(board, depth, maximizing_player)`
- `alpha_beta_pruning(board, depth, alpha, beta, maximizing_player)`
- `expectimax(board, depth, maximizing_player)`

These functions should be implemented to evaluate board states (using the heuristic functions provided in `utils.py`) and determine the best move. You can adjust the search depth in these functions to create different difficulty levels.

## Additional Notes

- **Board Representation:** The game board is a 6×6 numpy array defined in `game.py`.
- **Game Logic:** The game logic (e.g., placing pieces, checking for wins/draws) is encapsulated in the `ConnectFourGame` class.
- **Graphical Interface:** The `ConnectFourGUI` class in `gui.py` uses Pygame to render the game board, display pieces, highlight winning moves, and manage user inputs.
- **Utility Functions:** Functions for board evaluation and move generation are available in `utils.py` to help with AI development.

Happy coding and have fun building your AI for Connect Four!
```
