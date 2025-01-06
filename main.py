from configobj import ConfigObj
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from os import getcwd

from object import *
from transform import *

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
    
    glLight(GL_LIGHT0, GL_POSITION, (5, 5, 5, 1))
    glLightfv(GL_LIGHT0, GL_AMBIENT,  (1.0, 1.0, 1.0, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE,  (1.0, 1.0, 1.0, 1.0))
    glLightfv(GL_LIGHT0, GL_SPECULAR, (1.0, 1.0, 1.0, 1.0))
    glEnable(GL_LIGHT0)
    
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (0.0, 1.0, 0.0, 1.0))
    
    objects: list[Object] = []
    
    cube = Object("Cube")
    cube.addComponent(Transform((0, 0, 0)))
    cube.addComponent(Cube(GL_POLYGON,
                           f"{path}\\Textures\\Pavement-Painted-Concrete.tif"
        ))
    objects.append(cube)
    
    moveSpeed = float(defaults['camera']['moveSpeed'])
    rotateSpeed = float(defaults['camera']['rotateSpeed'])
    
    mousePos = pygame.mouse.get_pos()
    mouseButtons = pygame.mouse.get_pressed()
    
    run = True
    while run:
        keys = pygame.key.get_pressed()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            elif event.type == MOUSEMOTION:
                mousePos = pygame.mouse.get_pos()
            elif event.type == MOUSEBUTTONDOWN:
                mouseButtons = pygame.mouse.get_pressed()
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        
        for o in objects:
            transform: Transform = o.getComponent(Transform)
            if not transform is None:
                transform.moveX((keys[K_a] - keys[K_d]) * moveSpeed)
                transform.moveY((keys[K_e] - keys[K_q]) * moveSpeed)
                transform.moveZ((keys[K_w] - keys[K_s]) * moveSpeed)

                transform.rotateX((keys[K_DOWN] - keys[K_UP]) * rotateSpeed)
                transform.rotateY((keys[K_RIGHT] - keys[K_LEFT]) * rotateSpeed)
                transform.rotateZ((keys[K_z] - keys[K_c]) * rotateSpeed)
            
            o.update()
        
        pygame.display.flip()
        clock.tick(FPS)
                
pygame.quit()
exit()