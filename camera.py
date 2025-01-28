from configobj import ConfigObj
import pygame
from pygame.locals import *
import math
import numpy as np
from os import getcwd

from transform import Transform

path = getcwd()

defaults = ConfigObj(f"{path}\\defaults.ini")

class Camera:
    def __init__(self, FOVy, aspectRatio, near, far) -> None:
        f = 1 / math.tan(math.radians(FOVy / 2))
        a = f / aspectRatio
        b = f
        c = (near + far) / (near - far)
        d = 2 * near * far / (near - far)
        
        self.PPM = np.matrix([
            [a, 0,  0, 0],
            [0, b,  0, 0],
            [0, 0,  c, d],
            [0, 0, -1, 0],
        ])
        self.VM = np.identity(4)
        
        self.transform = Transform()
        self.transform.rotateY(90)
        
        self.moveSpeed   = float(defaults['camera']['moveSpeed'])
        self.rotateSpeed = float(defaults['camera']['rotateSpeed'])
        self.mouseSensitivityX = float(defaults['camera']['mouseSensitivityX'])
        self.mouseSensitivityY = float(defaults['camera']['mouseSensitivityY'])
        
    def getVM(self):
        return self.VM
    
    def getPPM(self):
        return self.PPM
    
    def getPosition(self) -> pygame.Vector3:
        position = pygame.Vector3(
            self.VM[0, 3],
            self.VM[1, 3],
            self.VM[2, 3],
        )
        
        return position
        
    def update(self) -> None:
        keys = pygame.key.get_pressed()
        
        if keys[K_w]:
            self.transform.updatePosition(self.transform.getPosition() + pygame.Vector3(0, 0,  self.moveSpeed))
        if keys[K_s]:
            self.transform.updatePosition(self.transform.getPosition() + pygame.Vector3(0, 0, -self.moveSpeed))
        if keys[K_q]:
            self.transform.updatePosition(self.transform.getPosition() + pygame.Vector3(0,  self.moveSpeed, 0))
        if keys[K_e]:
            self.transform.updatePosition(self.transform.getPosition() + pygame.Vector3(0, -self.moveSpeed, 0))
        if keys[K_d]:
            self.transform.updatePosition(self.transform.getPosition() + pygame.Vector3(-self.moveSpeed, 0, 0))
        if keys[K_a]:
            self.transform.updatePosition(self.transform.getPosition() + pygame.Vector3( self.moveSpeed, 0, 0))
            
        if keys[K_RIGHT]:
            self.transform.rotateX(-self.rotateSpeed)
        if keys[K_LEFT]:
            self.transform.rotateX( self.rotateSpeed)
        if keys[K_UP]:
            self.transform.rotateY( self.rotateSpeed)
        if keys[K_DOWN]:
            self.transform.rotateX(-self.rotateSpeed)
