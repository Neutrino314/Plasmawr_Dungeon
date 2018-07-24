import pygame, sys, math
from map_engine import *
from Globals import *

pygame.init()

Test_Map = Map("/home/euler/Desktop/dungeons_v2/Maps/blank.txt", "hi")
Map.Load_Map(Test_Map)

running = True
Mouse_Pos = [-64, -64]
Window_rect = pygame.Rect(0, 0, 800, 600)

Window = pygame.display.set_mode((Window_rect[2], Window_rect[3]), pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)
pygame.display.set_caption("Map Editor V3")

clock = pygame.time.Clock()

Brush = 1


while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_w:
                Globals.Camera_move = 1

            if event.key == pygame.K_s:
                Globals.Camera_move = 2

            if event.key == pygame.K_d:
                Globals.Camera_move = 3

            if event.key == pygame.K_a:
                Globals.Camera_move = 4

            if event.key == pygame.K_1:
                Map.Save_Map(Test_Map)

            if event.key == pygame.K_b:
                Brush = int(input("Choose a Brush: "))

        if event.type == pygame.KEYUP:
            Globals.Camera_move = 0

        if event.type == pygame.MOUSEMOTION:
            Mouse_Pos = [math.floor(pygame.mouse.get_pos()[0] / 64) * 64, math.floor(pygame.mouse.get_pos()[1] / 64) * 64]

        if event.type == pygame.VIDEORESIZE:
            pygame.display.set_mode(event.dict["size"], pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)
            Window_rect[2] = event.dict["size"][0]
            Window_rect[3] = event.dict["size"][1]

        if event.type == pygame.MOUSEBUTTONDOWN:

            for Tile in Test_Map.Map_Data:
                if [int(Mouse_Pos[0]), int(Mouse_Pos[1])] == [Tile[0], Tile[1]]:

                    if Tile[2] == Brush:
                        print("A tile is already placed There")
                    else:
                        Test_Map.Map_Data[Test_Map.Map_Data.index(Tile)][2] = Brush

        if event.type == pygame.MOUSEBUTTONUP:
            pass



    #Movement Logic:
    if Globals.Camera_move == 1:
        Globals.Camera_xy[1] += 64
    if Globals.Camera_move == 2:
        Globals.Camera_xy[1] -= 64
    if Globals.Camera_move == 3:
        Globals.Camera_xy[0] -= 64
    if Globals.Camera_move == 4:
        Globals.Camera_xy[0] += 64


    Window.fill((0, 0, 0))
    Map.Render_Chunk(Test_Map, Window_rect, Window, Globals.Camera_xy)
    pygame.draw.rect(Window,(255, 0, 0) , (Mouse_Pos[0], Mouse_Pos[1], Tiles.size, Tiles.size), 1)


    pygame.display.update()
    clock.tick(30)

pygame.quit()
sys.exit()
