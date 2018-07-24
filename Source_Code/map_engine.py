import pygame

class Tiles:

    size = 64

    def Load_Texture(file, size):

        surface = pygame.Surface((size, size), pygame.HWSURFACE|pygame.SRCALPHA)
        texture = pygame.image.load(file)
        surface.blit(texture, (0, 0))

        return surface

    isolated_grass = Load_Texture("/home/euler/Desktop/dungeons_v2/Assets/textures/isolated_grass.png", size)
    isolated_concrete = Load_Texture("/home/euler/Desktop/dungeons_v2/Assets/textures/concrete_isolated.png", size)
    Barrier = Load_Texture("/home/euler/Desktop/dungeons_v2/Assets/textures/barrier.png", size)

    Tiles_Dict = {1 : isolated_grass, 2 : isolated_concrete, 3 : Barrier}
    Blocked_Types = [3]


class Map:

    def __init__(self, File, Name):

        self.File = File
        self.Name = Name
        self.Map_Data = []
        self.Blocked_Tiles = []

    def Load_Map(self):

        Map_File = open(self.File, "r")
        Map_Data = Map_File.readline()
        Map_Data = Map_Data.split("|")
        del Map_Data[(len(Map_Data) - 1)]

        for i in range(0, len(Map_Data)):

            Map_Data[i] = Map_Data[i].split(",")

            for j in range(0, 3):

                Map_Data[i][j] = int(Map_Data[i][j])


        self.Map_Data = Map_Data


        pass

    def Render_Chunk(self, Chunk_Rect, Window, Camera_xy):

        for Tile in self.Map_Data:

            if Chunk_Rect.collidepoint((Tile[0] + Camera_xy[0], Tile[1] + Camera_xy[1])) == True:
                Window.blit(Tiles.Tiles_Dict[Tile[2]], (Tile[0] + Camera_xy[0], Tile[1] + Camera_xy[1]))
            else:
                continue

        return

    def Blocked_Calc(self):

        for Tile in self.Map_Data:

            if Tile[2] in Tiles.Blocked_Types:
                self.Blocked_Tiles.append([Tile[0] / 64, Tile[1] / 64, Tile[2]])
                continue
            else:
                continue

    def Default_Map(self, size):

        for i in range(0, 100):
            for j in range(0, 100):
                Cur_Tile = [size * j, size * i, 1]
                self.Map_Data.append(Cur_Tile)

    def Save_Map(self):

        Name = input("Choose a map_name: ")
        Path = "/home/euler/Desktop/dungeons_v2/Maps/"
        Map_Data = ""
        File_Path = Path + Name + ".txt"
        File = open(File_Path, "w")

        for Tile in self.Map_Data:
            Map_Data = Map_Data + str(Tile[0]) + "," + str(Tile[1]) + "," + str(Tile[2]) + "|"

        File.write(Map_Data)