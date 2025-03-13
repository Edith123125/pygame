import pygame
import time
from hero import Hero
from enemy import Enemy
from settings import Settings
import game_functions as gf
from pygame.sprite import Group
from start_button import Play_button
from quit_button import Quit_button
from restart_button import Restart_button  # Import the new Restart_button class
from scoreboard import Scoreboard

def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(game_settings.screen_size)
    pygame.display.set_caption("Monster Attack")
    hero = Hero(screen)

    # Music
    pygame.mixer.music.load('sounds/music.wav')
    pygame.mixer.music.play(-1)

    # Create a play button
    play_button = Play_button(screen, 'Press to begin')

    # Create a quit button
    quit_button = Quit_button(screen, 'Quit')

    # Create a restart button
    restart_button = Restart_button(screen, 'Restart')

    # Create a scoreboard
    count = 0
    count_update = "Enemies Killed: %d" % count
    scoreboard = Scoreboard(screen, count_update)

    enemies = Group()
    bullets = Group()

    tick = 0
    enemy_spawn_delay = 400  # Increased delay before first enemy spawns

    clock = pygame.time.Clock()  # Add a clock to control frame rate

    while True:
        clock.tick(60)  # Limit the frame rate to 60 FPS

        gf.check_events(hero, bullets, game_settings, screen, play_button, quit_button, restart_button, enemies)

        if game_settings.game_active:
            hero.update()
            enemies.update(hero, game_settings.enemy_speed)
            tick += 1

            # Delay enemy spawn and slow down frequency
            if tick > enemy_spawn_delay and tick % 200 == 0:  # Spawn enemies less frequently
                enemies.add(Enemy(screen, game_settings))

            bullets.update()

            for enemy in enemies:
                for bullet in bullets:
                    if bullet.rect.bottom <= 0:
                        bullets.remove(bullet)
                    if len(bullets) >= 20:  # Increased bullet limit
                        bullets.remove(bullet)
                    if enemy.rect.colliderect(bullet.rect):
                        count += 1
                        count_update = "Enemies Killed: %d" % count
                        scoreboard = Scoreboard(screen, count_update)

                        enemies.remove(enemy)
                        bullets.remove(bullet)
                        pygame.mixer.music.load('sounds/win.wav')
                        pygame.mixer.music.play(0)

                if enemy.rect.colliderect(hero.rect):
                    print("The monster got you! You died!")
                    pygame.mixer.music.load('sounds/lose.wav')
                    pygame.mixer.music.play(0)
                    game_settings.game_active = False  # End the game

        # Display active enemies and score
        count_update = "Enemies Killed: %d" % count
        scoreboard = Scoreboard(screen, count_update)

        gf.update_screen(game_settings, screen, hero, bullets, enemies, play_button, quit_button, restart_button, scoreboard)

run_game()