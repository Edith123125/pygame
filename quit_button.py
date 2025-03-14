import pygame.font

class Quit_button(object):
    def __init__(self, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # properties and dimensions of the button 
        self.width, self.height = 200, 50
        self.button_color = (255, 0, 0)  
        self.text_color = (255, 255, 255)  
        self.font = pygame.font.Font(None, 48)  

       
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.centery + 60  

        # The mesage of the button message should  be prepped only once
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)