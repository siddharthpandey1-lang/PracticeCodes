import pygame
import sys

pygame.init()

# 4K Resolution
WIDTH, HEIGHT = 3840, 2160
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Function Tester")

clock = pygame.time.Clock()

font = pygame.font.SysFont("comic", 80)

input_text = ""
result_text = ""
active = True

while True:
    clock.tick(120)  # 120 FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if input_text.isdigit():
                    number = int(input_text)
                    result = number * 2
                    result_text = f"Result: {result}"
                else:
                    result_text = "Please enter a valid number."

                input_text = ""

            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

    # Animated background
    t = pygame.time.get_ticks() / 1000
    r = int((pygame.math.Vector2(1, 0).rotate(t * 50).x + 1) * 127)
    b = int((pygame.math.Vector2(1, 0).rotate(t * 50).y + 1) * 127)

    screen.fill((r, 50, b))

    title = font.render("Enter a Number:", True, (255, 255, 255))
    screen.blit(title, (100, 100))

    user_surface = font.render(input_text, True, (255, 255, 0))
    screen.blit(user_surface, (100, 250))

    result_surface = font.render(result_text, True, (0, 255, 0))
    screen.blit(result_surface, (100, 400))

    pygame.display.flip()