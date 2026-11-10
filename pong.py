# Set correct login credentials
correct_username = "player1"
correct_password = "pong123"
# Allow the user 3 attempts to log in
attempts = 3

# Start login loop
while attempts > 0:
    # Ask the user for username and password
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if credentials are correct
    if username == correct_username and password == correct_password:
        print("Login successful! Launching Pong game...\n")
        break  # Exit the login loop
    else:
        attempts -= 1  # Decrease remaining attempts
        print(f"Incorrect login. You have {attempts} attempt(s) left.\n")

# If no attempts remain, exit the program
if attempts == 0:
    print("Too many failed attempts. Exiting system.")
    exit()


import pygame  # Main game library
import sys  # (Not used in the final code, can be removed)
import pandas as pd  # For saving scores in a data table
from datetime import datetime  # To record game time


pygame.init()  # Initialize all pygame modules

# Set screen dimensions and create the game window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")  # Set window title

# Define colors and font for text
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.SysFont(None, 36)



# Paddle class handles player paddles
class Paddle:
    def __init__(self, x, y, name):
        # Create a paddle as a rectangle
        self.rect = pygame.Rect(x, y, 10, 100)
        self.speed = 6  # Paddle movement speed
        self.score = 0  # Player's score
        self.name = name  # Player's name

    # Move the paddle based on keys pressed
    def move(self, up_key, down_key):
        keys = pygame.key.get_pressed()
        if keys[up_key] and self.rect.top > 0:
            self.rect.y -= self.speed  # Move up
        if keys[down_key] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed  # Move down

    # Draw the paddle on the screen
    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)

    # Increase the player's score by 1
    def add_point(self):
        self.score += 1

# Ball class handles the ball movement and behavior
class Ball:
    def __init__(self):
        # Create a ball as a rectangle
        self.rect = pygame.Rect(WIDTH//2 - 10, HEIGHT//2 - 10, 20, 20)
        self.speed_x = 5  # Horizontal speed
        self.speed_y = 5  # Vertical speed

    # Move the ball and bounce off top and bottom walls
    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Bounce the ball if it hits top or bottom
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed_y *= -1

    # Reset ball position and reverse direction
    def reset(self):
        self.rect.center = (WIDTH//2, HEIGHT//2)
        self.speed_x *= -1  # Change direction after a point

    # Draw the ball on the screen
    def draw(self):
        pygame.draw.ellipse(screen, WHITE, self.rect)



# Create player paddles and the ball
player1 = Paddle(50, HEIGHT//2 - 50, "Player 1")
player2 = Paddle(WIDTH - 60, HEIGHT//2 - 50, "Player 2")
ball = Ball()
clock = pygame.time.Clock()  # Clock to control game speed


game_active = True  # Game loop control variable
while game_active:
    screen.fill(BLACK)  # Clear screen every frame

    # Check for quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_active = False  # Exit game loop

    # Move paddles based on player input
    player1.move(pygame.K_w, pygame.K_s)  # Player 1: W/S keys
    player2.move(pygame.K_UP, pygame.K_DOWN)  # Player 2: Up/Down arrows

    # Move the ball
    ball.move()

    # Check for collisions between ball and paddles
    if ball.rect.colliderect(player1.rect) or ball.rect.colliderect(player2.rect):
        ball.speed_x *= -1  # Reverse ball direction

    # Score handling
    if ball.rect.left <= 0:
        player2.add_point()  # Player 2 scores
        ball.reset()  # Reset ball

    if ball.rect.right >= WIDTH:
        player1.add_point()  # Player 1 scores
        ball.reset()

    # Draw game objects
    player1.draw()
    player2.draw()
    ball.draw()
    pygame.draw.aaline(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))  # Center line

    # Draw scores on screen
    score_text_1 = FONT.render(str(player1.score), True, WHITE)
    score_text_2 = FONT.render(str(player2.score), True, WHITE)
    screen.blit(score_text_1, (WIDTH//4, 20))
    screen.blit(score_text_2, (WIDTH*3//4, 20))

    # Update the display and tick the clock
    pygame.display.flip()
    clock.tick(60)  # Limit to 60 frames per second



# Create a dictionary with game result data
result_data = {
    "Timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
    "Player 1 Score": [player1.score],
    "Player 2 Score": [player2.score],
    "Winner": ["Player 1" if player1.score > player2.score else "Player 2"]
}

# Convert data to a DataFrame and save to CSV
df = pd.DataFrame(result_data)
df.to_csv("pong_game_results.csv", index=False)
