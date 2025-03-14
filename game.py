import pygame
import time
import sqlite3
from hero import Hero
from enemy import Enemy
from settings import Settings
import game_functions as gf
from pygame.sprite import Group
from start_button import Play_button
from quit_button import Quit_button
from restart_button import Restart_button
from scoreboard import Scoreboard

# this connects to the database 
conn = sqlite3.connect("game_data.db")
cursor = conn.cursor()

# this creates a table for high scores
cursor.execute("""
CREATE TABLE IF NOT EXISTS high_scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    score INTEGER NOT NULL
)
""")
conn.commit()

# a function that saves the high score
def save_high_score(score):
    cursor.execute("INSERT INTO high_scores (score) VALUES (?)", (score,))
    conn.commit()

# a function that loads the highest score
def load_high_score():
    cursor.execute("SELECT MAX(score) FROM high_scores")
    result = cursor.fetchone()
    return result[0] if result[0] is not None else 0

def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(game_settings.screen_size)
    pygame.display.set_caption("Monster Attack")
    hero = Hero(screen)

    # The Music
    pygame.mixer.music.load('sounds/music.wav')
    pygame.mixer.music.play(-1)

    # this creates a play button
    play_button = Play_button(screen, 'Press to begin')

    # this creates a quit button
    quit_button = Quit_button(screen, 'Quit')

    #  this creates a restart button
    restart_button = Restart_button(screen, 'Restart')

    # Loads now  the high score at the start of the game
    high_score = load_high_score()

    # this creates the groups for bullets and enemies 
    enemies = Group()
    bullets = Group()

    # This creates a scoreboard
    count = 0
    count_update = "Enemies Killed: %d | Active Enemies: %d | High Score: %d" % (count, len(enemies), high_score)
    scoreboard = Scoreboard(screen, count_update)

    tick = 0
    enemy_spawn_delay = 100  # Reduces the delay before first enemy spawns

    clock = pygame.time.Clock()  # Adds the  clock to control frame rates

    while True:
        clock.tick(60) 

        gf.check_events(hero, bullets, game_settings, screen, play_button, quit_button, restart_button, enemies)

        if game_settings.game_active:
            hero.update()
            enemies.update(hero, game_settings.enemy_speed)
            tick += 1

            # Spawns the enemies more frequently
            if tick > enemy_spawn_delay and tick % 50 == 0:  # Spawns the enemies after every 50 ticks
                enemies.add(Enemy(screen, game_settings))

            bullets.update()

            for enemy in enemies:
                for bullet in bullets:
                    if bullet.rect.bottom <= 0:
                        bullets.remove(bullet)
                    if len(bullets) >= 20:  
                        bullets.remove(bullet)
                    if enemy.rect.colliderect(bullet.rect):
                        count += 1
                        count_update = "Enemies Killed: %d | Active Enemies: %d | High Score: %d" % (count, len(enemies), high_score)
                        scoreboard.scoreboard_message(count_update)  # Updates the scoreboard text

                        enemies.remove(enemy)
                        bullets.remove(bullet)
                        pygame.mixer.music.load('sounds/win.wav')
                        pygame.mixer.music.play(0)

                if enemy.rect.colliderect(hero.rect):
                    print("The monster got you! You died!")
                    pygame.mixer.music.load('sounds/lose.wav')
                    pygame.mixer.music.play(0)
                    game_settings.game_active = False  # Ends the game

                    # this saves the high score when the current score is higher
                    if count > high_score:
                        high_score = count
                        save_high_score(high_score)

        # thi displays the score and active enemies 
        count_update = "Enemies Killed: %d | Active Enemies: %d | High Score: %d" % (count, len(enemies), high_score)
        scoreboard.scoreboard_message(count_update)

        # this draws everything on the screen
        gf.update_screen(game_settings, screen, hero, bullets, enemies, play_button, quit_button, restart_button, scoreboard)

    # Closes the database connection when now the game ends
    conn.close()

run_game()