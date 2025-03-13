import pygame.font

class Quit_button(object):
    def __init__(self, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Button dimensions and properties
        self.width, self.height = 200, 50
        self.button_color = (255, 0, 0)  # Red color
        self.text_color = (255, 255, 255)  # White text
        self.font = pygame.font.Font(None, 48)  # Larger font size

        # Build the button's rect object and position it below the start button
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.centery + 60  # Position below the start button

        # The button message needs to be prepped only once
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw the button and then draw the message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)