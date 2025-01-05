import pygame
from OpenGL.GL import *

pygame.init()

class Mesh3D:
    def __init__(self) -> None:
        self.vertices:  list[tuple[float]]
        self.triangles: list[int]
        self.uvs:       list[tuple[float]]
        
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
        glEnable(GL_TEXTURE_2D)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
        glBindTexture(GL_TEXTURE_2D, self.texID)
        
        for t in range(0, len(self.triangles), 3):
            glBegin(self.drawType)
            
            glTexCoord2fv(self.uvs[self.triangles[  t  ]])
            glVertex3fv(self.vertices[self.triangles[  t  ]])
            glTexCoord2fv(self.uvs[self.triangles[t + 1]])
            glVertex3fv(self.vertices[self.triangles[t + 1]])
            glTexCoord2fv(self.uvs[self.triangles[t + 2]])
            glVertex3fv(self.vertices[self.triangles[t + 2]])
            
            glEnd()
            
class Cube(Mesh3D):
    def __init__(self, drawType, filename):
        Mesh3D.__init__(self)
        
        self.vertices = [
            ( 0.5, -0.5,  0.5),
            (-0.5, -0.5,  0.5),
            ( 0.5,  0.5,  0.5),
            (-0.5,  0.5,  0.5),
            ( 0.5,  0.5, -0.5),
            (-0.5,  0.5, -0.5),
            ( 0.5, -0.5, -0.5),
            (-0.5, -0.5, -0.5),
            ( 0.5,  0.5,  0.5),
            (-0.5,  0.5,  0.5),
            ( 0.5,  0.5, -0.5),
            (-0.5,  0.5, -0.5),
            ( 0.5, -0.5, -0.5),
            ( 0.5, -0.5,  0.5),
            (-0.5, -0.5,  0.5),
            (-0.5, -0.5, -0.5),
            (-0.5, -0.5,  0.5),
            (-0.5,  0.5,  0.5),
            (-0.5,  0.5, -0.5),
            (-0.5, -0.5, -0.5),
            ( 0.5, -0.5, -0.5),
            ( 0.5,  0.5, -0.5),
            ( 0.5,  0.5,  0.5),
            ( 0.5, -0.5,  0.5),
        ]
        self.triangles = [
            0,  2,  3,
            0,  3,  1,
            8,  4,  5,
            8,  5,  9,
            10, 6,  7,
            10, 7,  11,
            12, 13, 14,
            12, 14, 15,
            16, 17, 18,
            16, 18, 19,
            20, 21, 22,
            20, 22, 23,
        ]
        self.uvs = [
            (0.0, 0.0), (0.0, 1.0),
            (0.0, 1.0), (1.0, 1.0),
            (0.0, 1.0), (1.0, 1.0),
            (0.0, 1.0), (1.0, 1.0),
            (0.0, 0.0), (1.0, 0.0),
            (0.0, 0.0), (1.0, 0.0),
            (0.0, 0.0), (0.0, 1.0),
            (1.0, 1.0), (1.0, 0.0),
            (0.0, 0.0), (0.0, 1.0),
            (1.0, 1.0), (1.0, 0.0),
            (0.0, 0.0), (0.0, 1.0),
            (1.0, 1.0), (1.0, 0.0),
        ]
        
        self.texture = pygame.image.load(filename)
        self.drawType = drawType
        self.initTexture()