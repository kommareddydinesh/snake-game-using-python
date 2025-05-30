# Enhanced Snake Game - Pygame

A classic Snake game built with Python and Pygame featuring:

- Multiple types of food with different scores and unique shapes
- Smooth animations and colorful graphics
- Background music and eating sound effects
- Pause and resume functionality
- Score tracking with high score saving
- Increasing difficulty levels as you progress

---

## Demo

![Snake Game Demo](demo.gif)  
*(Add a gif or screenshot of your game here for better presentation)*

---

## Features

- **Food Variety:** Apples, Grapes, Bananas, and Candy each with unique visuals and points.
- **Sound Effects:** Background music loops continuously; sound plays on eating food.
- **Pause/Resume:** Press `P` to pause or resume the game.
- **Score & Level:** Displays current score, level, and all-time high score.
- **Game Over:** Restart with `C` or quit with `Q` on game over screen.
- **Responsive Controls:** Arrow keys to control the snake.

---

## Installation

1. Make sure you have [Python 3.7+](https://www.python.org/downloads/) installed.
2. Install Pygame:
---bash:
pip install pygame

---
  
## Ensure your sound files are placed as follows (or update paths in snake.py):
**Background music:**
C:\Users\kdine\OneDrive\Documents\Desktop\instagram-clone\primitive-snake-charmer-melody-104216.mp3
**Eating sound:**
C:\Users\kdine\OneDrive\Documents\Desktop\instagram-clone\eating-crackers-sound-341911.mp3

## How to Play
-Run the game:python snake.py
-Control the snake using arrow keys.
-Eat food to grow and score points.
-Avoid hitting the walls or the snake’s own body.
-Press P to pause or resume.
-When the game ends, press C to play again or Q to quit.

## Notes
If the sound files are missing or paths are incorrect, the game will still run without sound.
For better eating sound effect support, convert .mp3 eating sound to .wav and update the path in the code.

## Acknowledgments
Pygame — Python game development library.
Sound clips from free sound libraries and music sources.
