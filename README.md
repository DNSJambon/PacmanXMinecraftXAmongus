# Pacamn X Minecraft X Amongus - Python Maze Game

## Overview

A small maze game developed using Python's `Tkinter` library. The game features a character that must navigate through a grid, collect all the gold pieces, and avoid enemies to win the game. The game also includes different difficulty levels and tracks the best scores.

## Features

- **Multiple Difficulty Levels**: Choose from three difficulty levels - Easy, Medium, and Hard.
- **Enemy AI**: The game includes two enemies with different behaviors. One follows a random path, while the other chases the player.
- **Score Tracking**: The game tracks and displays the highest score based on the difficulty level and time taken to complete the game.
- **Keyboard Controls**: Use the keyboard to move the character around the maze.

## How to Play

1. **Run the Game**: Start the game by running the `jeu.py` script:
   ```bash
   python jeu.py
   ```

2. **Control the Character**:
   - `q` - Move left
   - `d` - Move right
   - `z` - Move up
   - `s` - Move down

3. **Objective**: Collect all the gold pieces and avoid the enemies to win the game. If you collect all the pieces, you win. If an enemy catches you, you lose.

4. **Restart**: If you lose or win, you can restart the game from the menu.

## Files

- `jeu.py`: Main game logic.
- `map/mur.txt`: Defines the maze structure.
- `images/`: Contains the images used in the game.
- `score/score.txt`: Stores the best score.

## Customization

- **Map Editing**: You can modify the `map/mur.txt` file to change the layout of the maze. (x is a wall, p is a lingot)
- **Images**: Replace the images in the `images/` folder to change the game's appearance.

## Dependencies

- `Tkinter`: GUI library for Python.
- `Pillow`: Python Imaging Library to handle images.

## License

free to use or edit

## Credits

me
  
