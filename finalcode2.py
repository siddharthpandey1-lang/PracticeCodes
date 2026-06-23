import pygame
import sys

# Initialize Pygame
pygame.init()

# Window settings
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Function Tester")

# FPS
clock = pygame.time.Clock()

# Fonts
title_font = pygame.font.SysFont("Arial", 50)
input_font = pygame.font.SysFont("Arial", 40)
result_font = pygame.font.SysFont("Arial", 45)

# Colors
WHITE = (255, 255, 255)
BLACK = (20, 20, 20)
BLUE = (0, 120, 255)
GREEN = (0, 255, 100)

# Variables
user_input = ""
result_text = "Enter a number and press ENTER"

running = True

while running:
    clock.tick(120)

    # Background animation
    t = pygame.time.get_ticks() / 10
    bg_color = (
        int((t % 255)),
        int((t * 0.5) % 255),
        int((t * 0.2) % 255)
    )

    screen.fill(bg_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False

            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]

            elif event.key == pygame.K_RETURN:

                if user_input.isdigit():
                    number = int(user_input)
                    result = number * 2
                    result_text = f"The result of doubling {number} is {result}"
                else:
                    result_text = "Please enter a valid number."

                user_input = ""

            else:
                if event.unicode.isprintable():
                    user_input += event.unicode

    # Draw title
    title = title_font.render("FUNCTION TESTER", True, WHITE)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 60))

    # Draw input box
    pygame.draw.rect(screen, BLACK, (290, 220, 700, 70), border_radius=15)
    pygame.draw.rect(screen, BLUE, (290, 220, 700, 70), 4, border_radius=15)

    input_surface = input_font.render(user_input, True, WHITE)
    screen.blit(input_surface, (310, 235))

    # Instructions
    instruction = input_font.render(
        "Type a number and press ENTER",
        True,
        WHITE
    )
    screen.blit(instruction, (350, 150))

    # Result
    result_surface = result_font.render(result_text, True, GREEN)
    screen.blit(result_surface, (100, 400))

    # FPS Counter
    fps_text = input_font.render(
        f"FPS: {int(clock.get_fps())}",
        True,
        WHITE
    )
    screen.blit(fps_text, (20, 20))

    pygame.display.flip()

pygame.quit()
sys.exit()