!pip install pygame
# (or)
pip install pygame


import pygame
import random
import os

# Initialize pygame and mixer
pygame.init()

# Sound file paths (update these if you move the files)
EAT_SOUND_PATH = r"C:\Users\kdine\OneDrive\Documents\Desktop\instagram-clone\eating-crackers-sound-341911.mp3"
MUSIC_PATH = r"C:\Users\kdine\OneDrive\Documents\Desktop\instagram-clone\primitive-snake-charmer-melody-104216.mp3"

# Load and play background music (loop indefinitely)
try:
    pygame.mixer.music.load(MUSIC_PATH)
    pygame.mixer.music.play(-1)
except pygame.error as e:
    print(f"Warning: Music file not found or failed to load: {MUSIC_PATH}\n{e}")

# Function to safely load short sounds (like eating)
def load_sound(path):
    try:
        return pygame.mixer.Sound(path)
    except (pygame.error, FileNotFoundError) as e:
        print(f"Warning: Sound file not found or failed to load: {path}\n{e}")
        return None

eat_sound = load_sound(EAT_SOUND_PATH)

# Colors
WHITE, DARK_GREEN, GREEN, BLACK = (250, 250, 250), (0, 100, 0), (0, 255, 0), (0, 0, 0)
RED, YELLOW, PURPLE, PINK, BLUE, SHADOW = (200, 30, 60), (255, 225, 0), (160, 32, 240), (255, 105, 180), (50, 153, 213), (30, 30, 30)

# Display settings
WIDTH, HEIGHT = 800, 600
BLOCK_SIZE = 20
FPS = 15

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🍎 Enhanced Snake Game")

# Fonts
font = pygame.font.SysFont("segoeuisemibold", 28)
score_font = pygame.font.SysFont("comicsansms", 36)

clock = pygame.time.Clock()

HIGHSCORE_FILE = "highscore.txt"

def load_highscore():
    if os.path.exists(HIGHSCORE_FILE):
        with open(HIGHSCORE_FILE, "r") as file:
            return int(file.read())
    return 0

def save_highscore(score):
    with open(HIGHSCORE_FILE, "w") as file:
        file.write(str(score))

# Food types
FOOD_TYPES = [
    {"name": "Apple", "color": RED, "score": 1},
    {"name": "Grape", "color": PURPLE, "score": 2},
    {"name": "Banana", "color": YELLOW, "score": 3},
    {"name": "Candy", "color": PINK, "score": 5},
]

def draw_text_center(text, color, y, shadow=False):
    render = font.render(text, True, SHADOW if shadow else color)
    rect = render.get_rect(center=(WIDTH // 2, y))
    if shadow:
        rect.x += 2
        rect.y += 2
    window.blit(render, rect)

def draw_score(score, level, high_score):
    value = score_font.render(f"Score: {score}  Level: {level}  High Score: {high_score}", True, BLUE)
    window.blit(value, [20, 20])

def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(window, DARK_GREEN, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE], border_radius=5)
        pygame.draw.rect(window, GREEN, [block[0]+4, block[1]+4, BLOCK_SIZE-8, BLOCK_SIZE-8], border_radius=3)

def draw_food(food):
    x, y = food["pos"]
    cx, cy = int(x + BLOCK_SIZE / 2), int(y + BLOCK_SIZE / 2)
    color = food["color"]
    shape = food["name"]

    if shape == "Apple":
        pygame.draw.circle(window, color, (cx, cy), BLOCK_SIZE // 2)
    elif shape == "Grape":
        pygame.draw.ellipse(window, color, [x, y + 3, BLOCK_SIZE, BLOCK_SIZE - 6])
    elif shape == "Banana":
        pygame.draw.polygon(window, color, [(cx, y), (x, y + BLOCK_SIZE), (x + BLOCK_SIZE, y + BLOCK_SIZE)])
    elif shape == "Candy":
        pygame.draw.polygon(window, color, [
            (cx, y), (cx + 4, y + 8), (x + BLOCK_SIZE, y + 8), (cx + 6, y + 14),
            (x + BLOCK_SIZE - 4, y + BLOCK_SIZE), (cx, y + 16),
            (x + 4, y + BLOCK_SIZE), (cx - 6, y + 14), (x, y + 8), (cx - 4, y + 8)
        ])

def generate_food():
    food_type = random.choice(FOOD_TYPES)
    x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0) * 20.0
    y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0) * 20.0
    return {"pos": [x, y], "color": food_type["color"], "score": food_type["score"], "name": food_type["name"]}

def show_message(msg, sub_msg):
    window.fill(PINK)
    draw_text_center(msg, WHITE, HEIGHT // 2 - 20)
    draw_text_center(sub_msg, WHITE, HEIGHT // 2 + 30)
    pygame.display.update()
    pygame.time.wait(1500)

def game_loop():
    x, y = WIDTH // 2, HEIGHT // 2
    dx, dy = 0, 0

    snake = []
    length = 1
    score = 0
    level = 1
    speed = FPS
    paused = False

    high_score = load_highscore()
    food = generate_food()
    running = True
    game_over = False

    while running:
        while game_over:
            show_message("You Lost!", "Press C to Play Again or Q to Quit")
            if score > high_score:
                save_highscore(score)
                high_score = score
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = False
                        game_over = False
                    elif event.key == pygame.K_c:
                        return game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if not paused:
                    if event.key == pygame.K_LEFT and dx == 0:
                        dx, dy = -BLOCK_SIZE, 0
                    elif event.key == pygame.K_RIGHT and dx == 0:
                        dx, dy = BLOCK_SIZE, 0
                    elif event.key == pygame.K_UP and dy == 0:
                        dx, dy = 0, -BLOCK_SIZE
                    elif event.key == pygame.K_DOWN and dy == 0:
                        dx, dy = 0, BLOCK_SIZE
                if event.key == pygame.K_p:
                    paused = not paused

        if paused:
            draw_text_center("Paused", BLUE, HEIGHT // 2)
            pygame.display.update()
            clock.tick(5)
            continue

        x += dx
        y += dy

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_over = True

        window.fill(WHITE)

        draw_food(food)
        head = [x, y]
        snake.append(head)
        if len(snake) > length:
            del snake[0]

        for segment in snake[:-1]:
            if segment == head:
                game_over = True

        draw_snake(snake)
        draw_score(score, level, high_score)
        pygame.display.update()

        # Eating food
        if x == food["pos"][0] and y == food["pos"][1]:
            score += food["score"]
            length += 1
            if eat_sound:
                eat_sound.play()
            food = generate_food()

            # Increase difficulty
            if score % 5 == 0:
                level += 1
                speed += 2

        clock.tick(speed)

    pygame.quit()
    quit()

# Start the game
game_loop()
