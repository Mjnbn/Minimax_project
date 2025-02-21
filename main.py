import random
import sys
import pygame
from game import ConnectFourGame, PLAYER, AI
from gui import ConnectFourGUI, RADIUS, SQUARESIZE
import engine

def main():
    # Initialize the game and GUI
    gui = ConnectFourGUI()
    # Get the updated board size after menu selection
    # Show the menu and wait for a selection
    mode = gui.menu_loop()
    ROW_COUNT, COLUMN_COUNT = gui.get_board_size()  # Retrieve the updated board size from GUI
    game = ConnectFourGame(ROW_COUNT, COLUMN_COUNT)  # Pass these values to the game initialization
    # Start the selected game mode
    if mode == 'human':
        run_human_vs_human(game, gui)
    elif mode == 'ai':
        run_player_vs_ai(game, gui)
    elif mode == 'ai_vs_ai':
        run_ai_vs_ai(game, gui)


def run_human_vs_human(game, gui):
    """
    Handles the logic for two human players (Red vs Yellow).
    """
    turn = 0  # 0 => Player 1 (Red), 1 => Player 2 (Yellow)
    game_over = False
    game.reset()
    gui.draw_board(game.board)
    pygame.display.update()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Mouse motion for piece preview on the top row
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(gui.screen, (0, 0, 0), (0, 0, gui.screen.get_width(), SQUARESIZE))
                posx = event.pos[0]
                if turn == 0:
                    # Player 1 (Red)
                    pygame.draw.circle(gui.screen, (255, 0, 0), (posx, SQUARESIZE // 2), RADIUS)
                else:
                    # Player 2 (Yellow)
                    pygame.draw.circle(gui.screen, (255, 255, 0), (posx, SQUARESIZE // 2), RADIUS)
                pygame.display.update()

            # Mouse click events
            if event.type == pygame.MOUSEBUTTONDOWN:
                posx = event.pos[0]
                col = posx // SQUARESIZE  # Determine column based on x-position

                if game.is_valid_location(col):
                    row = game.get_next_open_row(col)

                    if turn == 0:
                        # Player 1 (Red)
                        game.drop_piece(row, col, PLAYER)
                        if game.winning_move(PLAYER):
                            game.game_over = True
                            game.winner = "Player"
                            #gui.draw_winner("Player")  # or just #gui.draw_winner(PLAYER)
                        else:
                            # Check if it's a draw after Player 1's move
                            if game.is_draw():
                                game.game_over = True
                                game.winner = "Draw"
                                #gui.draw_winner("Draw")

                        turn = 1
                    else:
                        # Player 2 (Yellow)
                        game.drop_piece(row, col, AI)
                        if game.winning_move(AI):
                            game.game_over = True
                            game.winner = "Player2"
                            # Optional: label for "Player 2"
                            #gui.draw_winner("Player2")
                        else:
                            # Check if it's a draw after Player 2's move
                            if game.is_draw():
                                game.game_over = True
                                game.winner = "Draw"
                                #gui.draw_winner("Draw")

                        turn = 0

                    # Redraw board after the move
                    gui.draw_board(game.board)

        # Check if game ended this frame
        if game.game_over:
            pygame.time.wait(1000)  # Display the result for 3 seconds
            action = gui.end_page_loop(game.winner)  # Show the end page with options
            if action == "restart":
                game.reset()
                gui.draw_board(game.board)
                turn = 0
                game.game_over = False
            elif action == "quit":
                pygame.quit()
                sys.exit()


def run_player_vs_ai(game, gui):
    """
    Handles the logic for Player (Red) vs. AI (Yellow).
    """
    turn = 0  # Player goes first
    game_over = False
    game.reset()
    gui.draw_board(game.board)
    pygame.display.update()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Mouse motion for piece preview on the top row
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(gui.screen, (0, 0, 0), (0, 0, gui.screen.get_width(), SQUARESIZE))
                posx = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(gui.screen, (255, 0, 0), (posx, SQUARESIZE // 2), RADIUS)
                else:
                    pygame.draw.circle(gui.screen, (255, 255, 0), (posx, SQUARESIZE // 2), RADIUS)
                pygame.display.update()

            # Mouse click events (for player)
            if event.type == pygame.MOUSEBUTTONDOWN and turn == 0:
                posx = event.pos[0]
                col = posx // SQUARESIZE  # Determine column based on x-position

                if game.is_valid_location(col):
                    row = game.get_next_open_row(col)
                    game.drop_piece(row, col, PLAYER)

                    if game.winning_move(PLAYER):
                        game.game_over = True
                        game.winner = "Player"
                        #gui.draw_winner("Player")
                    else:
                        # Check draw
                        if game.is_draw():
                            game.game_over = True
                            game.winner = "Draw"
                            #gui.draw_winner("Draw")

                    gui.draw_board(game.board)
                    turn = 1  # Switch to AI

        # AI Turn (using Expectimax algorithm)
        if turn == 1 and not game.game_over:
            # You can switch to alpha_beta or minimax if you prefer:
            # col, _ = engine.alpha_beta_pruning(game, depth=4, alpha=-float('inf'), beta=float('inf'), maximizing_player=True)
            col, _ = engine.expectimax(game, depth=4, maximizing_player=True)
            row = game.get_next_open_row(col)
            game.drop_piece(row, col, AI)

            if game.winning_move(AI):
                game.game_over = True
                game.winner = "AI"
                #gui.draw_winner("AI")
            else:
                # Check draw
                if game.is_draw():
                    game.game_over = True
                    game.winner = "Draw"
                    #gui.draw_winner("Draw")

            gui.draw_board(game.board)
            turn = 0

        if game.game_over:
            pygame.time.wait(1000)
            action = gui.end_page_loop(game.winner)  # Show the end page with options
            if action == "restart":
                game.reset()
                gui.draw_board(game.board)
                turn = 0
                game.game_over = False
            elif action == "quit":
                pygame.quit()
                sys.exit()


def run_ai_vs_ai(game, gui):
    """
    Handles the logic for AI (Red) vs. AI (Yellow).
    """
    turn = 0  # AI 1 (Red) goes first
    game_over = False
    game.reset()
    gui.draw_board(game.board)
    pygame.display.update()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # AI 1's Turn (Maximizing Player using Expectimax)
        if turn == 0 and not game.game_over:

            # col, _ = engine.expectimax(game, depth=4, maximizing_player=True)
            # row = game.get_next_open_row(col)

            col = random.choice(game.get_valid_locations())
            row = game.get_next_open_row(col)
            game.drop_piece(row, col, PLAYER)  # AI 1 uses Red pieces
            pygame.time.wait(100)

            if game.winning_move(PLAYER):
                game.game_over = True
                game.winner = "Random"
                #gui.draw_winner("Player1")
            else:
                # Check draw
                if game.is_draw():
                    game.game_over = True
                    game.winner = "Draw"
                    #gui.draw_winner("Draw")

            gui.draw_board(game.board)
            turn = 1  # Switch to AI 2

        # AI 2's Turn (Minimizing Player using Alpha-Beta)
        if turn == 1 and not game.game_over:
            col, _ = engine.alpha_beta_pruning(game, depth=1, alpha=-float('inf'), beta=float('inf'), maximizing_player=False)
            row = game.get_next_open_row(col)
            game.drop_piece(row, col, AI)  # AI 2 uses Yellow pieces

            if game.winning_move(AI):
                game.game_over = True
                game.winner = "AI"
                #gui.draw_winner("Player2")
            else:
                # Check draw
                if game.is_draw():
                    game.game_over = True
                    game.winner = "Draw"
                    #gui.draw_winner("Draw")

            gui.draw_board(game.board)
            turn = 0  # Switch back to AI 1

        # After both AI turns, check if the game is over
        if game.game_over:
            pygame.time.wait(1000)
            action = gui.end_page_loop(game.winner)  # Show the end page with options
            if action == "restart":
                game.reset()
                gui.draw_board(game.board)
                turn = 0
                game.game_over = False
            elif action == "quit":
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()