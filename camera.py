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
        
        moveX = keys[K_d] - keys[K_a]
        moveY = keys[K_q] - keys[K_e]
        moveZ = keys[K_w] - keys[K_s]
        moveVector = pygame.Vector3(moveX, moveY, moveZ)
        if moveVector.length() > 0:
            moveVector.normalize_ip()
            moveVector *= self.moveSpeed
        
        self.transform.updatePosition(moveVector, False)

        rotateX = keys[K_UP]   - keys[K_DOWN]
        rotateY = keys[K_LEFT] - keys[K_RIGHT]
        rotateZ = keys[K_z]    - keys[K_x]
        rotateVector = pygame.Vector3(rotateX, rotateY, rotateZ)
        if rotateVector.length() > 0:
            rotateVector.normalize_ip()
            rotateVector *= self.rotateSpeed
            
        self.transform.updateRotation(rotateVector, True)
            
        self.VM = self.transform.getMVM()
