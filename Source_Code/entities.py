import pygame, math
from Globals import *

class Entity:

    def __init__(self, Name, Pos, Sprite_Sheet, xy, Friendly, Inventory):

        self.Name = Name
        self.Pos = Pos
        self.Max_Health = 10
        self.Health = 10
        self.Sprite_Sheet = pygame.image.load(Sprite_Sheet)
        self.sprite_dict = {}
        self.xy = xy
        self.Friendly = Friendly
        self.Inventory = Inventory
        self.Interacting = False
        return

class Player(Entity):

    def __init__(self, Name, Pos, Sprite_Sheet, Class, xy, Inventory):

        Entity.__init__(self, Name, Pos, Sprite_Sheet, xy, True, Inventory)
        self.Class = Class
        self.X_Pos_Colliding = False
        self.X_Neg_Colliding = False
        self.Y_Pos_Colliding = False
        self.Y_Neg_Colliding = False


        return

    def Pos_Calc(self, xy):

        self.Pos = [(self.xy[0] - xy[0]) / 64, (self.xy[1] - xy[1]) / 64]
        return

    def Environment_Collide(self, Blocked_Tiles):


        #This section detects whether THe player is colliding with the map boundaries
        if self.Pos[0] < 0.125:
            self.X_Neg_Colliding = True
        elif self.Pos[0] > 98.875:
            self.X_Pos_Colliding = True
        elif self.Pos[1] < 0.125:
            self.Y_Pos_Colliding = True
        elif self.Pos[1] > 98.875:
            self.Y_Neg_Colliding = True
        else:
            self.X_Pos_Colliding = False
            self.X_Neg_Colliding = False
            self.Y_Pos_Colliding = False
            self.Y_Neg_Colliding = False

        #This for loop tests whether the player occupies the same tile as an NPC
        for i in range(0, len(Blocked_Tiles)):

            #Handles collision with barrier textures on the x axis
            if (self.Pos[0] > Blocked_Tiles[i][0] - 1.125 and self.Pos[0] < Blocked_Tiles[i][0]) and (self.Pos[1] > Blocked_Tiles[i][1] - 1 and self.Pos[1] < Blocked_Tiles[i][1] + 1):
                self.X_Pos_Colliding = True
            elif (self.Pos[0] < Blocked_Tiles[i][0] + 1.125 and self.Pos[0] > Blocked_Tiles[i][0]) and (self.Pos[1] > Blocked_Tiles[i][1] - 1 and self.Pos[1] < Blocked_Tiles[i][1] + 1):
                self.X_Neg_Colliding = True

            elif (self.Pos[1] < Blocked_Tiles[i][1] + 1.125 and self.Pos[1] > Blocked_Tiles[i][1]) and (self.Pos[0] < Blocked_Tiles[i][0] + 1 and self.Pos[0] > Blocked_Tiles[i][0] - 1):
                self.Y_Pos_Colliding = True
            elif (self.Pos[1] > Blocked_Tiles[i][1] - 1.125 and self.Pos[1] < Blocked_Tiles[i][1]) and (self.Pos[0] < Blocked_Tiles[i][0] + 1 and self.Pos[0] > Blocked_Tiles[i][0] - 1):
                self.Y_Neg_Colliding = True

        return

    def Player_Move(self):

        if not self.Y_Pos_Colliding:
            if Globals.Camera_move == 1:
                Globals.Camera_xy[1] += 8
        if not self.Y_Neg_Colliding:
            if Globals.Camera_move == 2:
                Globals.Camera_xy[1] -= 8
        if not self.X_Pos_Colliding:
            if Globals.Camera_move == 3:
                Globals.Camera_xy[0] -= 8
        if not self.X_Neg_Colliding:
            if Globals.Camera_move == 4:
                Globals.Camera_xy[0] += 8

class NPC(Entity):

    def __init__(self, Name, Pos, Sprite_Sheet, xy, Friendly, Inventory):

        Entity.__init__(self, Name, Pos, Sprite_Sheet, xy, Friendly, Inventory)
        return

class Container(Entity):

    def __init__(self, Name, Pos, Sprite_Sheet, xy, Friendly, Inventory):

        Entity.__init__(self, Name, Pos, Sprite_Sheet, xy, Friendly, Inventory)
        return

