import pygame
from game import PLAYER, AI  # Import PLAYER and AI, no need to import self.ROW_COUNT, self.COLUMN_COUNT

# Colors (R, G, B)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARK_BLUE = (30, 60, 90)  # Default button color
NAVY_BLUE = (10, 40, 70)  # Hover color
GREY = (220, 210, 190)  # Background color

# Board drawing constants
SQUARESIZE = 100
RADIUS = int(SQUARESIZE / 2 - 5)


class ConnectFourGUI:
    def __init__(self):
        pygame.init()
        self.switch_button_state = "6x6"  # Default to "6x6"
        self.update_board_size()  # Update board size based on the default state

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Connect Four")

        # Load custom fonts
        self.font = pygame.font.Font("MachineGunk.ttf", 50)
        self.button_font = pygame.font.Font("MachineGunk.ttf", 40)

        # Define button properties
        self.button_width = 450
        self.button_height = 80
        self.play_human_button_rect = pygame.Rect(0, 0, self.button_width, self.button_height)
        self.play_ai_button_rect = pygame.Rect(0, 0, self.button_width, self.button_height)
        self.ai_vs_ai_button_rect = pygame.Rect(0, 0, self.button_width, self.button_height)
        self.switch_button_rect = pygame.Rect(0, 0, self.button_width, self.button_height)

        # Track hover states
        self.button_colors = {
            "human": DARK_BLUE,
            "ai": DARK_BLUE,
            "ai_vs_ai": DARK_BLUE,
            "switch": DARK_BLUE
        }

        # Define restart and quit button properties for end page
        self.play_restart_button_rect = pygame.Rect(0, 0, self.button_width, self.button_height)
        self.play_quit_button_rect = pygame.Rect(0, 0, self.button_width, self.button_height)

        # Track hover states for the end page buttons
        self.button_colors_end = {
            "restart": DARK_BLUE,
            "quit": DARK_BLUE
        }

    def update_board_size(self):
        """Update the board size based on the current switch button state."""
        if self.switch_button_state == "6x6":
            self.ROW_COUNT = 6
            self.COLUMN_COUNT = 6
        elif self.switch_button_state == "9x9":
            self.ROW_COUNT = 9
            self.COLUMN_COUNT = 9

        self.width = self.COLUMN_COUNT * SQUARESIZE
        self.height = (self.ROW_COUNT + 1) * SQUARESIZE  # Extra row on top for piece drop
        self.size = (self.width, self.height)

        # Update the Pygame window size dynamically
        self.screen = pygame.display.set_mode((self.width, self.height))
    def get_board_size(self):
        """Return the current board size based on the switch button."""
        return self.ROW_COUNT, self.COLUMN_COUNT

    def draw_board(self, board):
        """Draw the game board and pieces on the screen."""
        for c in range(self.COLUMN_COUNT):
            for r in range(self.ROW_COUNT):
                pygame.draw.rect(
                    self.screen, DARK_BLUE,
                    (c * SQUARESIZE, (r + 1) * SQUARESIZE, SQUARESIZE, SQUARESIZE)
                )
                pygame.draw.circle(
                    self.screen, GREY,
                    (int(c * SQUARESIZE + SQUARESIZE / 2),
                     int((r + 1) * SQUARESIZE + SQUARESIZE / 2)),
                    RADIUS
                )

        for c in range(self.COLUMN_COUNT):
            for r in range(self.ROW_COUNT):
                if board[r][c] == PLAYER:
                    pygame.draw.circle(
                        self.screen, RED,
                        (int(c * SQUARESIZE + SQUARESIZE / 2),
                         self.height - int(r * SQUARESIZE + SQUARESIZE / 2)),
                        RADIUS
                    )
                elif board[r][c] == AI:
                    pygame.draw.circle(
                        self.screen, YELLOW,
                        (int(c * SQUARESIZE + SQUARESIZE / 2),
                         self.height - int(r * SQUARESIZE + SQUARESIZE / 2)),
                        RADIUS
                    )

        pygame.display.update()

    def draw_winner(self, winner):
        """Display the winner message on the screen."""
        if winner == "Player":
            label = self.font.render("Player1 wins!", True, RED)
        elif winner == "AI":
            label = self.font.render("AI wins!", True, YELLOW)
        elif winner == "Player2":
            label = self.font.render("Player2 wins!", True, YELLOW)
        elif winner == "Random":
            label = self.font.render("Random Agent wins!", True, RED)
        else:
            label = self.font.render("Draw!", True, WHITE)
        result_x = (self.width - label.get_width()) // 2
        self.screen.blit(label, (result_x, self.height // 4))
        pygame.display.update()

    def draw_menu(self):
        """Draw the menu screen with buttons and hover effects."""
        self.screen.fill(GREY)

        # Draw the title at the top center with bold font
        title = self.font.render("Connect Four", True, BLACK)
        title_x = (self.width - title.get_width()) // 2
        self.screen.blit(title, (title_x, 50))

        # Button positions centered and spaced
        button_y_start = (self.height - 3 * self.button_height) // 2  # Start Y position for buttons

        # Set button positions
        self.play_human_button_rect.topleft = ((self.width - self.button_width) // 2, button_y_start)
        self.play_ai_button_rect.topleft = ((self.width - self.button_width) // 2, button_y_start + self.button_height + 10)
        self.ai_vs_ai_button_rect.topleft = (
            (self.width - self.button_width) // 2, button_y_start + 2 * (self.button_height + 10))
        self.switch_button_rect.topleft = (
            (self.width - self.button_width) // 2, button_y_start + 3 * (self.button_height + 10))
        # Draw the buttons with rounded corners
        pygame.draw.rect(self.screen, self.button_colors["human"], self.play_human_button_rect, border_radius=40)
        pygame.draw.rect(self.screen, self.button_colors["ai"], self.play_ai_button_rect, border_radius=40)
        pygame.draw.rect(self.screen, self.button_colors["ai_vs_ai"], self.ai_vs_ai_button_rect, border_radius=40)
        pygame.draw.rect(self.screen, self.button_colors["switch"], self.switch_button_rect, border_radius=40)
        # Render button text
        human_text = self.button_font.render("Player vs Player", True, WHITE)
        ai_text = self.button_font.render("Player vs AI", True, WHITE)
        ai_vs_ai_text = self.button_font.render("AI vs AI", True, WHITE)
        switch_text = self.button_font.render(self.switch_button_state, True, WHITE)
        # Draw text centered inside buttons
        self.screen.blit(human_text, (self.play_human_button_rect.x + (self.button_width - human_text.get_width()) // 2,
                                      self.play_human_button_rect.y + (
                                                  self.button_height - human_text.get_height()) // 2))
        self.screen.blit(ai_text, (self.play_ai_button_rect.x + (self.button_width - ai_text.get_width()) // 2,
                                   self.play_ai_button_rect.y + (self.button_height - ai_text.get_height()) // 2))
        self.screen.blit(ai_vs_ai_text,
                         (self.ai_vs_ai_button_rect.x + (self.button_width - ai_vs_ai_text.get_width()) // 2,
                          self.ai_vs_ai_button_rect.y + (self.button_height - ai_vs_ai_text.get_height()) // 2))
        self.screen.blit(switch_text, (self.switch_button_rect.x + (self.button_width - switch_text.get_width()) // 2,
                                       self.switch_button_rect.y + (
                                                   self.button_height - switch_text.get_height()) // 2))
        pygame.display.update()

    def update_hover_effect(self, mouse_pos):
        """Smoothly transition button color when hovered."""
        buttons = {
            "human": self.play_human_button_rect,
            "ai": self.play_ai_button_rect,
            "ai_vs_ai": self.ai_vs_ai_button_rect,
            "switch": self.switch_button_rect
        }

        for key, button in buttons.items():
            if button.collidepoint(mouse_pos):
                self.button_colors[key] = self.lerp_color(self.button_colors[key], NAVY_BLUE, 0.1)  # Smooth transition
            else:
                self.button_colors[key] = self.lerp_color(self.button_colors[key], DARK_BLUE, 0.1)

    def lerp_color(self, current_color, target_color, speed):
        """Linearly interpolate between two colors."""
        return tuple(
            int(current + (target - current) * speed) for current, target in zip(current_color, target_color)
        )

    def draw_end_page(self, result):
        """Draw the end page with the result and buttons."""
        self.screen.fill(GREY)
        self.draw_winner(result)

        # Button Y positions
        button_y_start = (self.height - 2 * self.button_height) // 2  # Start Y position for buttons

        # Set button positions
        self.play_restart_button_rect.topleft = ((self.width - self.button_width) // 2, button_y_start)
        self.play_quit_button_rect.topleft = (
            (self.width - self.button_width) // 2, button_y_start + self.button_height + 10)

        # Draw buttons with their respective colors
        pygame.draw.rect(self.screen, self.button_colors_end["restart"], self.play_restart_button_rect,
                         border_radius=40)
        pygame.draw.rect(self.screen, self.button_colors_end["quit"], self.play_quit_button_rect, border_radius=40)

        # Render button text
        restart_text = self.button_font.render("Restart", True, WHITE)
        quit_text = self.button_font.render("Quit", True, WHITE)

        # Draw text centered inside buttons
        self.screen.blit(restart_text,
                         (self.play_restart_button_rect.x + (self.button_width - restart_text.get_width()) // 2,
                          self.play_restart_button_rect.y + (self.button_height - restart_text.get_height()) // 2))
        self.screen.blit(quit_text, (self.play_quit_button_rect.x + (self.button_width - quit_text.get_width()) // 2,
                                     self.play_quit_button_rect.y + (self.button_height - quit_text.get_height()) // 2))

        pygame.display.update()

    def end_page_loop(self, result):
        """End page event loop with hover detection and button click."""
        running = True
        selected_action = None
        self.draw_end_page(result)  # Show the result (you can customize this based on the winner)
        while running:
            mouse_pos = pygame.mouse.get_pos()
            self.update_hover_effect(mouse_pos)  # Smooth hover transition

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_restart_button_rect.collidepoint(mouse_pos):
                        selected_action = "restart"
                        running = False  # Exit the loop
                    elif self.play_quit_button_rect.collidepoint(mouse_pos):
                        selected_action = "quit"
                        running = False  # Exit the loop
            pygame.time.delay(20)  # Smooth animation delay

        return selected_action  # Return selected action ("restart" or "quit")

    def menu_loop(self):
        """Menu event loop with hover detection and button click."""
        running = True
        selected_mode = None

        while running:
            mouse_pos = pygame.mouse.get_pos()
            self.update_hover_effect(mouse_pos)  # Smooth hover transition
            self.draw_menu()  # Redraw menu with updated colors

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    selected_mode = self.get_menu_option(mouse_pos)
                    if selected_mode:
                        print(f"Selected: {selected_mode}")
                        running = False  # Exit the menu loop without quitting Pygame
                    if self.switch_button_rect.collidepoint(mouse_pos):
                        self.switch_button_state = "9x9" if self.switch_button_state == "6x6" else "6x6"
                        self.update_board_size()
                        print(f"Switching to {self.switch_button_state}")
            pygame.time.delay(20)  # Smooth animation delay

        return selected_mode  # Return selected mode instead of quitting

    def get_menu_option(self, pos):
        """Return selected game mode based on mouse position."""
        if self.play_human_button_rect.collidepoint(pos):
            return 'human'
        elif self.play_ai_button_rect.collidepoint(pos):
            return 'ai'
        elif self.ai_vs_ai_button_rect.collidepoint(pos):
            return 'ai_vs_ai'
        return None
