import pygame, math
from map_engine import *
from Globals import * 
from entities import *

class Render:

    def Render(Window, Entity_list, player, Chunk, map):

        Map.Render_Chunk(map, Chunk, Window, Globals.Camera_xy)
        for Entity in Entity_list:
            Window.blit(Entity, (Entity.xy[0], Entity.xy[1]))
        Window.blit(player.Sprite_Sheet, (player.xy[0], player.xy[1]))

        return

    def resize(event, player, Entity_List, Window):

        size = event.dict["size"]
        Window = pygame.display.set_mode(size, pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)
        Chunk = pygame.Rect(-64, -64, size[0] + 128, size[1] + 128)

        Resizing_x = True
        Resizing_y = True

        x, y = 0, 0
        Prev_xy = [player.xy[0], player.xy[1]]

        while Resizing_x:
            
            if x < size[0] / 2:
                x += 64
                continue
            elif x > size[0] / 2:
                x -= 64
                player.xy[0] = x
                Resizing_x = False

        while Resizing_y:

            if y < size[1] / 2:
                y += 64
                continue
            elif y > size[1] / 2:
                y -= 64
                player.xy[1] = y
                Resizing_y = False

        Globals.Camera_xy[0] += x - Prev_xy[0]
        Globals.Camera_xy[1] += y - Prev_xy[1]

        Player.Pos_Calc(player, Globals.Camera_xy)

        return size, Chunk
        
            