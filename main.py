from configobj import ConfigObj
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from os import getcwd

from mesh import *

pygame.init()

if __name__ == "__main__":

    path = getcwd()
    defaults = ConfigObj(f"{path}\\defaults.ini")
    
    screenWidth  = int(defaults['screen']['width'])
    screenHeight = int(defaults['screen']['height'])
    FPS          = int(defaults['screen']['FPS'])
    
    screen = pygame.display.set_mode((screenWidth, screenHeight), DOUBLEBUF | OPENGL)
    clock = pygame.time.Clock()
    pygame.display.set_caption("3D Graphics V2")
    
    FOV  = float(defaults['camera']['FOV'])
    NEAR = float(defaults['camera']['NEAR'])
    FAR  = float(defaults['camera']['FAR'])
    
    aspectRatio = screenWidth / screenHeight
    
    glMatrixMode(GL_PROJECTION)
    gluPerspective(FOV, aspectRatio, NEAR, FAR)
    
    glMatrixMode(GL_MODELVIEW)
    glTranslatef(0.0, 0.0, -3.0)
    
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    
    glLight(GL_LIGHT0, GL_POSITION, (5, -5, 0, 1))
    glLightfv(GL_LIGHT0, GL_AMBIENT,  (1.0, 1.0, 1.0, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE,  (1.0, 1.0, 1.0, 1.0))
    glLightfv(GL_LIGHT0, GL_SPECULAR, (1.0, 1.0, 0.0, 1.0))
    glEnable(GL_LIGHT0)
    
    mesh = Cube(GL_POLYGON, f"{path}\\Textures\\Pavement-Painted-Concrete.tif")
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        glRotatef(1, 1, 0, 1)
        mesh.draw()
        
        pygame.display.flip()
        clock.tick(FPS)
                
pygame.quit()
exit()