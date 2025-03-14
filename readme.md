# Monster Battle Game
This is a Monster Battle Game built using Python and the Pygame library. The player controls a hero who must defend themselves against waves of monsters. The goal is to kill as many monsters as possible before they reach the hero. The game features a scoreboard, sound effects, and a high-score system.

## Features
- Hero Movement- Move the hero using the arrow keys (left, right, up, down).
- Monster Spawning- Monsters spawn at the top of the screen and move toward the hero.
- Bullets- Shoot bullets using the space bar to kill monsters.
- Scoreboard-Displays the number of enemies killed, active enemies, and the high score.
- High Score System-The high score is saved to a SQLite database and displayed when the game starts.
- Restart and Quit Options- Restart the game or quit after the game ends.

## How to Play
1. Start the Game- Click the "Press to begin" button to start the game.
2. Move the Hero- Use the arrow keys to move the hero.
3. Shoot Bullets- Press the space bar to shoot bullets and kill monsters.
4. Avoid Monsters- If a monster reaches the hero, the game ends.
5. Restart or Quit- After the game ends, click "Restart" to play again or "Quit" to exit the game.

## Languages Used
-Python 3
-Pygame library
-SQLite (included with Python)

### File Structure.
pygame/
├── images/                  # Folder for game images (e.g., hero, monsters)
├── sounds/                  # Folder for game sounds (e.g., music, win/lose sounds)
├── game.py                  # Main game script
├── hero.py                  # Hero class
├── enemy.py                 # Enemy class
├── bullets.py               # Bullet class
├── settings.py              # Game settings
├── game_functions.py        # Game functions (e.g., event handling, screen updates)
├── start_button.py          # Start button class
├── quit_button.py           # Quit button class
├── restart_button.py        # Restart button class
├── scoreboard.py            # Scoreboard class
├── README.md                # Project documentation
└── requirements.txt         # List of dependencies

### Author:Edith Gatwiri Kobia
Feel free to reach out if you have any feedback or would like to connect . github:https://github.com/

Enjoy the battle! ⚔️🔥