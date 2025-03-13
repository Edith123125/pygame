import pygame.font

class Scoreboard(object):
    def __init__(self, screen, scoreboard_text):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Scoreboard dimensions and properties
        self.width, self.height = 300, 50
        self.scoreboard_color = (0, 0, 0)  # Black background
        self.text_color = (255, 255, 255)  # White text
        self.font = pygame.font.Font(None, 40)  # Font and size

        # Build the scoreboard's rect object and position it at the top
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top + 10  # Position at the top of the screen

        # The scoreboard message needs to be prepped only once
        self.scoreboard_message(scoreboard_text)

    def scoreboard_message(self, scoreboard_text):
        """Render the scoreboard text."""
        self.image_message = self.font.render(scoreboard_text, True, self.text_color, self.scoreboard_color)
        self.image_message_rect = self.image_message.get_rect()
        self.image_message_rect.center = self.rect.center

    def draw_scoreboard(self):
        """Draw the scoreboard on the screen."""
        self.screen.fill(self.scoreboard_color, self.rect)
        self.screen.blit(self.image_message, self.image_message_rect)