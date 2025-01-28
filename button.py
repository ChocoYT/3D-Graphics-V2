import pygame
from OpenGL.GL import *

from utils import *

class Button:
    def __init__(self, screen: pygame.Surface, position: tuple[int], dimensions: tuple[int], color: tuple[int], oColor: tuple[int], pColor: tuple[int]) -> None:
        self.screen = screen
        self.position = position
        self.width, self.height = dimensions
        
        self.normalColor = color
        self.overColor = oColor
        self.pressedColor = pColor
        
    def draw(self, events) -> None:
        mousePos = pygame.mouse.get_pos()
        mx = mapValue(0, 800, 0, 1600, mousePos[0])
        my = mapValue(0, 600, 1200, 0, mousePos[1])
        
        glPushMatrix()
        glLoadIdentity()
        
        # If Mouse over Button
        if self.position[0] < mx < (self.position[0] + self.width) and self.position[1] < my < (self.position[1] + self.height):
            glColor3f(self.overColor[0], self.overColor[1], self.overColor[2])
        else:
            glColor3f(self.normalColor[0], self.normalColor[1], self.normalColor[2])
        
        glBegin(GL_POLYGON)
        
        glVertex2f(self.position[0], self.position[1])
        glVertex2f(self.position[0] + self.width, self.position[1])
        glVertex2f(self.position[0] + self.width, self.position[1] + self.height)
        glVertex2f(self.position[0], self.position[1] + self.height)
        
        glEnd()
        glPopMatrix()
        