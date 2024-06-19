# Higher-Lower-Game


## Overview

Higher Lower Game is a fun and engaging game where you compare the follower counts of two different celebrities, brands, or entities. The goal is to guess which one has more followers and try to achieve the highest score possible.

## Table of Contents

- [Game Overview](#overview)
- [Features](#features)
- [How to Play](#how-to-play)


## Features

- Randomly selects two entities from a predefined list.
- Compares the follower counts of the selected entities.
- Tracks the player's score.
- Prompts the player to continue or restart the game upon a wrong guess.


## How to Play

1. Run the game:
   ```bash
   python main.py
   ```

2. The game will display two entities with their descriptions and countries.
3. You will be prompted to guess which entity has more followers by typing 'A' or 'B'.
4. If you guess correctly, your score increases, and you continue to the next round with a new entity to compare.
5. If you guess incorrectly, the game ends and displays your final score. You will be prompted to play again.

## Code Structure

- `main.py`: Contains the main game logic.
- `game_data.py`: Contains the data for the entities used in the game.
- `art.py`: Contains the ASCII art for the game logo and the 'vs' symbol.


