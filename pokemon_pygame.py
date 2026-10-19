import sys
import pygame
import time


perspective = input("Front, Back, Footprints or Icon: ").lower()

if perspective == "front":
    perspective = "Front"
elif perspective == "back":
    perspective = "Back"
elif perspective == "icon":
    perspective = "Icons"
else:
    perspective = "Footprints"

if perspective == "Footprints":
    style = ""
else:
    style = input("Would you like shiny or normal: ").lower()
    if style == "shiny":
        style = "_Shiny"
    else:
        style = ""

pokemon = input("What pokemon would you like to render: ")
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
pokemon_render = pygame.image.load(f"Animated_Pokemon_Sprites/Animated_Pokemon_Sprites/Graphics/Pokemon/{perspective}{style}/{pokemon.capitalize()}.png")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        if perspective == "Footprint":
            screen.fill("white")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                screen.blit(pokemon_render, (0,0))

        pygame.display.update()

pygame.quit()
sys.exit()