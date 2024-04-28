import pygame
import random
pygame.init()

SCREEN_WEIDHT = 1600
SCREEN_HEIGHT = 900

screen = pygame.display.set_mode((SCREEN_WEIDHT, SCREEN_HEIGHT))

pygame.display.set_caption("Первая игра от Ивана", "Поехали")
icon = pygame.image.load("jpg/Снимок12.JPG")
pygame.display.set_icon(icon)

target_img = pygame.image.load("jpg/target.png")
target_weight = 50
target_height = 50

target_x = random.randint(0, SCREEN_WEIDHT- target_weight)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

running = True
while running:
    pass


pygame.quit()