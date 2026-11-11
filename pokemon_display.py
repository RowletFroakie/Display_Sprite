import sys
import pygame


FPS = 60

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
pokemon_sprite = pygame.image.load(f"Animated_Pokemon_Sprites/Animated_Pokemon_Sprites/Graphics/Pokemon/{perspective}{style}/{pokemon.upper()}.png")

pathway = f"Animated_Pokemon_Sprites/Animated_Pokemon_Sprites/Graphics/Pokemon/{perspective}{style}/{pokemon.upper()}.png"

# Finds height and width of each pokemon sprite sheet
imh = pokemon_sprite.get_height()
iml = pokemon_sprite.get_width()

columns = iml//imh

x = 0
y = 0


while running:
    screen.fill("white")
    if pygame.event.get() == pygame.QUIT:
        running = False
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        running = False
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        x -= 5
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        x += 5
    if pygame.key.get_pressed()[pygame.K_UP]:
        y -= 5
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        y += 5
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        beam = pygame.draw.rect(screen, (255, 100, 150), (x, y, 70, 60))
        # while moving:
        #     move = pygame.Vector2(0,10)
        #     beam.move(move)
        #     moving = False
    position = (x, y)

    # origin2 = position[0] + imh + columns, position[1] (in case i want to print more than one from the same sprite sheet)

    source_area = pygame.Rect((0, 0), (imh, imh))
    screen.blit(pokemon_sprite, position, source_area)


    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()
sys.exit()
