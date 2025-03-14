import pygame
class Settings:
    def __init__(self):
        self.screen_size = (800, 600)  # Screen dimensions
        self.bg_color = (0, 0, 0)  # Background color 
        self.enemy_speed = 1  
        self.bullet_speed = 5  #  speed of the Bullet
        self.bullet_width = 3  # width of the Bullet 
        self.bullet_height = 15  # the height of the bullet 
        self.bullet_color = (255, 0, 0)  # Bullets color 
        self.game_active = False  # state of the game
		