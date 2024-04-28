import pygame
import random

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Первая игра от Ивана")
icon = pygame.image.load("jpg/Снимок12.JPG")
pygame.display.set_icon(icon)

target_img = pygame.image.load("jpg/target.png")
target_weight = 100
target_height = 100

target_x = random.randint(0, SCREEN_WIDTH - target_weight)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
color = (173, 216, 230)

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_weight and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_weight)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()

pygame.quit()