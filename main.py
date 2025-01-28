from configobj import ConfigObj
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from os import getcwd

from button import Button
from camera import Camera
from loadMesh import LoadMesh
from material import Material
from mesh import Cube, Cursor
from object import Object
from transform import Transform

pygame.init()

def set2D() -> None:
    glMatrixMode(GL_PROJECTION)
    glLoadMatrixf(camera.getPPM())
    #glLoadIdentity()
    
    #gluOrtho2D(0, screenWidth, 0, screenHeight)
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    glViewport(0, 0, screenWidth, screenHeight)

def set3D() -> None:
    glMatrixMode(GL_PROJECTION)
    glLoadMatrixf(camera.getPPM())
    #glLoadIdentity()
    
    #gluPerspective(FOV, aspectRatio, NEAR, FAR)
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glViewport(0, 0, screenWidth, screenHeight)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_CULL_FACE)

if __name__ == "__main__":

    path = getcwd()
    defaults = ConfigObj(f"{path}\\defaults.ini")
    
    screenWidth  = int(defaults['screen']['width'])
    screenHeight = int(defaults['screen']['height'])
    FPS          = int(defaults['screen']['FPS'])
    
    screen = pygame.display.set_mode((screenWidth, screenHeight), DOUBLEBUF | OPENGL)
    clock = pygame.time.Clock()
    pygame.display.set_caption("3D Graphics V2")
    
    pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1)
    pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES, 4)
    pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)
    pygame.display.gl_set_attribute(pygame.GL_DEPTH_SIZE, 32)
    
    FOV  = float(defaults['camera']['FOV'])
    NEAR = float(defaults['camera']['NEAR'])
    FAR  = float(defaults['camera']['FAR'])
    
    aspectRatio = screenWidth / screenHeight
    camera = Camera(aspectRatio / FOV, aspectRatio, NEAR, FAR)
    
    set3D()
    
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glLight(GL_LIGHT0, GL_POSITION, (5, 5, 5, 0))
    glLightfv(GL_LIGHT0, GL_AMBIENT,  (1.0, 0.0, 1.0, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE,  (1.0, 1.0, 0.0, 1.0))
    glLightfv(GL_LIGHT0, GL_SPECULAR, (0.0, 1.0, 0.0, 1.0))
    glEnable(GL_LIGHT0)
    
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (0.0, 1.0, 0.0, 1.0))
    
    objects: list[Object] = []
    material = Material(f"{path}\\Shaders\\vertex.glsl", f"{path}\\Shaders\\fragment.glsl")
    
    mesh = Object("Teapot")
    mesh.addComponent(Transform())
    mesh.addComponent(LoadMesh(mesh.vaoRef, material, GL_LINE_LOOP, f"{path}\\Models\\teapot.obj"))
    mesh.addComponent(material)
    
    transform: Transform = mesh.getComponent(Transform)
    transform.rotateY(0)
    transform.updatePosition(pygame.Vector3(0, -2, -200))
    
    objects.append(mesh)
    
    moveSpeed = float(defaults['camera']['moveSpeed'])
    rotateSpeed = float(defaults['camera']['rotateSpeed'])
    
    mousePos = pygame.mouse.get_pos()
    mouseButtons = pygame.mouse.get_pressed()
    
    run = True
    while run:
        keys = pygame.key.get_pressed()
        
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                run = False
            elif event.type == MOUSEMOTION:
                mousePos = pygame.mouse.get_pos()
            elif event.type == MOUSEBUTTONDOWN:
                mouseButtons = pygame.mouse.get_pressed()
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        camera.update()
        set3D()
        
        print(f"Camera Position: {camera.transform.getPosition()}")
        
        for o in objects:
            o.update(camera, events)
            
        set2D()
        
        pygame.display.flip()
        clock.tick(FPS)
                
pygame.quit()
exit()