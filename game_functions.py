
import sys
import pygame
from bullets import Bullet  
from enemy import Enemy
from scoreboard import Scoreboard  

def check_events(hero, bullets, game_settings, screen, play_button, quit_button, restart_button, enemies):
    for event in pygame.event.get():  # runs through all the pygame events
        if event.type == pygame.QUIT: 
            sys.exit()  # quit
        # this handles the button click
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if play_button.rect.collidepoint(mouse_x, mouse_y):
                game_settings.game_active = True
            elif quit_button.rect.collidepoint(mouse_x, mouse_y):  # this quits the game if the quit button is clicked
                sys.exit()
            elif restart_button.rect.collidepoint(mouse_x, mouse_y):  # this restarts the game if restart button is clicked
                reset_game(hero, bullets, game_settings, screen, enemies)  

        elif event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_RIGHT:  # the user presses the right key 
                hero.moving_right = True  

            elif event.key == pygame.K_LEFT:
                hero.moving_left = True 

            elif event.key == pygame.K_SPACE:  # user pushes the space bar
                new_bullet = Bullet(hero, game_settings, screen)
                bullets.add(new_bullet)

            elif event.key == pygame.K_UP:
                hero.moving_up = True

            elif event.key == pygame.K_DOWN:
                hero.moving_down = True

        elif event.type == pygame.KEYUP:  
            if event.key == pygame.K_RIGHT: 
                hero.moving_right = False

            elif event.key == pygame.K_LEFT:
                hero.moving_left = False

            elif event.key == pygame.K_UP:
                hero.moving_up = False

            elif event.key == pygame.K_DOWN:
                hero.moving_down = False

def reset_game(hero, bullets, game_settings, screen, enemies):
    # Resets  game state
    game_settings.game_active = True
    bullets.empty()  # Clears all bullets
    enemies.empty()  # Clears all enemies
    hero.rect.centerx = screen.get_rect().centerx  # Repositions hero
    hero.rect.bottom = screen.get_rect().bottom
    count = 0  # Resets score
    count_update = "Enemies Killed: %d" % count
    scoreboard = Scoreboard(screen, count_update)  # Updates scoreboard

def update_screen(settings, screen, hero, bullets, enemies, play_button, quit_button, restart_button, scoreboard):
    screen.fill(settings.bg_color) 
    hero.draw_me()  # Draws the hero on the screen
    for enemy in enemies.sprites():
        enemy.draw_enemy()  
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    if not settings.game_active:  # when the game is not active, buttons should be displayed.
        play_button.draw_button()  # this draws the play button
        quit_button.draw_button()  # this draws the quit button
        restart_button.draw_button()  # this draws the restart button

    scoreboard.draw_scoreboard()  # this draws the scoreboard

    pygame.display.flip()  # Updates the full display surface to the screen