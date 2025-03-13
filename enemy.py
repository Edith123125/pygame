import math
from random import randint
import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
    def __init__(self, screen, game_settings):
        super(Enemy, self).__init__()
        self.screen = screen

        self.enemy_image = pygame.image.load('images/monster1.png')
        self.rect = self.enemy_image.get_rect()
        self.screen_rect = screen.get_rect()

        # Spawn enemies slightly off-screen and not directly on the hero
        self.rect.centerx = randint(self.screen_rect.left + 100, self.screen_rect.right - 100)
        self.rect.top = self.screen_rect.top - 50  # Spawn slightly above the screen

    def update(self, hero, speed=3):
        dx, dy = self.rect.x - hero.rect.x, self.rect.y - hero.rect.y
        dist = math.hypot(dx, dy)
        
        # Avoid division by zero
        if dist == 0:
            dist = 1  # Set a small distance to avoid division by zero

        dx, dy = dx / dist, dy / dist

        self.rect.x -= dx * speed
        self.rect.y -= dy * speed

    def draw_enemy(self):
        self.screen.blit(source=self.enemy_image, dest=self.rect)

    def __exit__(self, *err):
        self.remove(self)