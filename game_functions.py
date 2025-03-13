# we will put all main game functions here
import sys
import pygame
from bullets import Bullet  # we don't care about the update or draw functions. Just the class
from enemy import Enemy
from scoreboard import Scoreboard  # Import the Scoreboard class

def check_events(hero, bullets, game_settings, screen, play_button, quit_button, restart_button, enemies):
    for event in pygame.event.get():  # run through all pygame events
        if event.type == pygame.QUIT:  # if the event is the quit event...
            sys.exit()  # quit
        # handle button click
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if play_button.rect.collidepoint(mouse_x, mouse_y):
                game_settings.game_active = True
            elif quit_button.rect.collidepoint(mouse_x, mouse_y):  # Quit the game if quit button is clicked
                sys.exit()
            elif restart_button.rect.collidepoint(mouse_x, mouse_y):  # Restart the game if restart button is clicked
                reset_game(hero, bullets, game_settings, screen, enemies)  # Pass enemies to reset_game

        elif event.type == pygame.KEYDOWN:  # the user pushed a key and it's down
            if event.key == pygame.K_RIGHT:  # the user pressed right
                hero.moving_right = True  # set the flag

            elif event.key == pygame.K_LEFT:
                hero.moving_left = True  # set the flag

            elif event.key == pygame.K_SPACE:  # user pushed space bar
                new_bullet = Bullet(hero, game_settings, screen)
                bullets.add(new_bullet)

            elif event.key == pygame.K_UP:
                hero.moving_up = True

            elif event.key == pygame.K_DOWN:
                hero.moving_down = True

        elif event.type == pygame.KEYUP:  # user let go of a key
            if event.key == pygame.K_RIGHT:  # specifically the right arrow
                hero.moving_right = False

            elif event.key == pygame.K_LEFT:
                hero.moving_left = False

            elif event.key == pygame.K_UP:
                hero.moving_up = False

            elif event.key == pygame.K_DOWN:
                hero.moving_down = False

def reset_game(hero, bullets, game_settings, screen, enemies):
    # Reset the game state
    game_settings.game_active = True
    bullets.empty()  # Clear all bullets
    enemies.empty()  # Clear all enemies
    hero.rect.centerx = screen.get_rect().centerx  # Reposition the hero
    hero.rect.bottom = screen.get_rect().bottom
    count = 0  # Reset the score
    count_update = "Enemies Killed: %d" % count
    scoreboard = Scoreboard(screen, count_update)  # Update the scoreboard

def update_screen(settings, screen, hero, bullets, enemies, play_button, quit_button, restart_button, scoreboard):
    screen.fill(settings.bg_color)  # Fill the background with the specified color
    hero.draw_me()  # Draw the hero on the screen
    for enemy in enemies.sprites():
        enemy.draw_enemy()  # Draw each enemy
    for bullet in bullets.sprites():
        bullet.draw_bullet()  # Draw each bullet

    if not settings.game_active:  # If the game is not active, show buttons
        play_button.draw_button()  # Draw the play button
        quit_button.draw_button()  # Draw the quit button
        restart_button.draw_button()  # Draw the restart button

    scoreboard.draw_scoreboard()  # Draw the scoreboard

    pygame.display.flip()  # Update the full display surface to the screen