import pygame
from OpenGL.GL import *

pygame.init()

class Mesh3D:
    def __init__(self) -> None:
        self.vertices:  list[tuple[float]]
        self.triangles: list[int]
        
        self.texture: pygame.Surface
        self.drawType = GL_LINE_LOOP
        self.texID: int
        
    def initTexture(self) -> None:
        self.texID = glGenTextures(1)
        textureData = pygame.image.tostring(self.texture, "RGB", True)
        
        width, height = self.texture.get_size()
        glBindTexture(GL_TEXTURE_2D, self.texID)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, 3, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, textureData)
        
    def draw(self) -> None:
        for t in range(0, len(self.triangles), 3):
            glBegin(GL_POLYGON)
            
            glVertex3fv(self.vertices[self.triangles[  t  ]])
            glVertex3fv(self.vertices[self.triangles[t + 1]])
            glVertex3fv(self.vertices[self.triangles[t + 2]])
            
            glEnd()
            
class Cube(Mesh3D):
    def __init__(self, drawType, filename):
        Mesh3D.__init__(self)
        
        self.texture = pygame.image.load(filename)
        self.drawType = drawType
        self.initTexture()
        
        self.vertices = [
            ( 0.5,  0.5,  0.5),
            (-0.5,  0.5,  0.5),
            ( 0.5,  0.5, -0.5),
            (-0.5,  0.5, -0.5),
            ( 0.5, -0.5,  0.5),
            (-0.5, -0.5,  0.5),
            ( 0.5, -0.5, -0.5),
            (-0.5, -0.5, -0.5),
        ]
        self.triangles = [
            0, 1, 2,  # Top
            3, 1, 2,
            4, 5, 6,  # Bottom
            7, 5, 6,
            0, 1, 4,  # Front
            1, 4, 5,
            2, 3, 6,  # Back
            3, 6, 7,
            0, 2, 6,  # Right
            0, 4, 6,
            1, 3, 7,  # Left
            1, 5, 7,
        ]