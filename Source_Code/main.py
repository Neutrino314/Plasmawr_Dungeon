import pygame, math, sys
from map_engine import *
from entities import *
from Rendering import *
from Script_Engine import *


pygame.init()

#Declaring the Entities used in the game
player1 = Player("Alex", [0, 0], "/home/euler/Desktop/dungeons_v2/Assets/Player/blank_south.png", "Nerd", [384, 256], [])
Player.Pos_Calc(player1, Globals.Camera_xy)

#Creating an instance of the 'Map' class and declaring all of its variables
Terrain = Map("/home/euler/Desktop/dungeons_v2/Maps/barrier_test.txt", "World")
Map.Load_Map(Terrain)
Map.Blocked_Calc(Terrain)

#Seting up the variables needed for the display and the game loop
size = [800, 600]

display = pygame.display.set_mode(size, pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)
pygame.display.set_caption("The Dungeons of Plasmawr")
Chunk = pygame.Rect(-64, -64, size[0] + 128, size[1] + 128)
clock = pygame.time.Clock()
running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.VIDEORESIZE:

            display = pygame.display.set_mode(event.dict["size"], pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)
            resize = Render.resize(event, player1, [], display)
            size = resize[0]
            Chunk = resize[1]

        if event.type == pygame.KEYDOWN:
            
            Key_Pressed = event.key

            if Key_Pressed == pygame.K_w:
                Globals.Camera_move = 1
            if Key_Pressed == pygame.K_s:
                Globals.Camera_move = 2
            if Key_Pressed == pygame.K_d:
                Globals.Camera_move = 3
            if Key_Pressed == pygame.K_a:
                Globals.Camera_move = 4

        if event.type == pygame.KEYUP:
            Globals.Camera_move = 0

    Player.Environment_Collide(player1, Terrain.Blocked_Tiles)
    Player.Player_Move(player1)
    Player.Pos_Calc(player1, Globals.Camera_xy)

    display.fill((175, 175, 255))
    Render.Render(display, [], player1, Chunk, Terrain)
    pygame.display.update()
    clock.tick(30)

pygame.quit()
sys.exit
