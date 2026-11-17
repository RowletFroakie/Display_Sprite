import sys
import pygame
import os



os.chdir(os.path.dirname(os.path.abspath(os.path.join(__file__, os.pardir))))

FPS = 72
animation_FPS_target = 24

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

pathway = f"pokemon/Animated_Pokemon_Sprites/Animated_Pokemon_Sprites/Graphics/Pokemon/{perspective}{style}/{pokemon.upper()}.png"
pokemon_sprite = pygame.image.load(pathway)

# Finds height and width of each pokemon sprite sheet
imh = pokemon_sprite.get_height()
iml = pokemon_sprite.get_width()

columns = iml/imh

x = 0
y = 0
pos1 = 0

frame_animation = 0

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

    if pos1 == iml:
        pos1 = 0


    source_area = pygame.Rect((pos1, 0), (imh, imh))
    screen.blit(pokemon_sprite, position, source_area)

    frame_animation += 1
    if frame_animation % (FPS/animation_FPS_target) == 0:
        pos1 +=imh

    clock.tick(FPS)
    pygame.display.flip()


pygame.quit()
sys.exit()
