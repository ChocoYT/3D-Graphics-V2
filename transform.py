import pygame
import math
import numpy as np

class Transform:
    def __init__(self) -> None:
        self.MVM = np.identity(4)
        
    def getMVM(self):
        return self.MVM
    
    def updatePosition(self, position, local=True) -> None:
        matrix = np.matrix([
            [1, 0, 0, position.x],
            [0, 1, 0, position.y],
            [0, 0, 1, position.z],
            [0, 0, 0, 1         ],
        ])
        
        if local:
            self.MVM = self.MVM @ matrix
        else:
            self.MVM = matrix @ self.MVM
        
    def getPosition(self):
        position = pygame.Vector3(
            self.MVM[0, 3],
            self.MVM[1, 3],
            self.MVM[2, 3],
        )
        
        return position
        
    def updateScale(self, scale, local = True) -> None:
        matrix = np.matrix([
            [scale.x, 0,       0,       0],
            [0,       scale.y, 0,       0],
            [0,       0,       scale.z, 0],
            [0,       0,       0,       1],
        ])
        
        if local:
            self.MVM = self.MVM @ matrix
        else:
            self.MVM = matrix @ self.MVM
        
    def getScale(self):
        scaleX = pygame.Vector3(
            self.MVM[0, 0],
            self.MVM[1, 0],
            self.MVM[2, 0],
        )
        scaleY = pygame.Vector3(
            self.MVM[0, 1],
            self.MVM[1, 1],
            self.MVM[2, 1],
        )
        scaleZ = pygame.Vector3(
            self.MVM[0, 2],
            self.MVM[1, 2],
            self.MVM[2, 2],
        )
        
        return pygame.Vector3(scaleX.magnitude(), scaleY.magnitude(), scaleZ.magnitude())
        
    def rotateX(self, n, local = True) -> None:
        n = math.radians(n)
        matrix = np.matrix([
            [1,  0,           0,           0],
            [0,  math.cos(n), math.sin(n), 0],
            [0, -math.sin(n), math.cos(n), 0],
            [0,  0,           0,           1],
        ])
        
        if local:
            self.MVM = self.MVM @ matrix
        else:
            self.MVM = matrix @ self.MVM
        
    def rotateY(self, n, local = True) -> None:
        n = math.radians(n)
        matrix = np.matrix([
            [math.cos(n), 0, -math.sin(n), 0],
            [0,           1,  0,           0],
            [math.sin(n), 0,  math.cos(n), 0],
            [0,           0,  0,           1],
        ])
        
        if local:
            self.MVM = self.MVM @ matrix
        else:
            self.MVM = matrix @ self.MVM
        
    def rotateZ(self, n, local = True) -> None:
        n = math.radians(n)
        matrix = np.matrix([
            [ math.cos(n), math.sin(n), 0, 0],
            [-math.sin(n), math.cos(n), 0, 0],
            [ 0,           0,           1, 0],
            [ 0,           0,           0, 1],
        ])
        
        if local:
            self.MVM = self.MVM @ matrix
        else:
            self.MVM = matrix @ self.MVM
            
    def updateRotation(self, rotation, local = True) -> None:
        x, y, z = rotation
        self.rotateX(x, local)
        self.rotateY(y, local)
        self.rotateZ(z, local)
        
    def getRotation(self):
        xDir = math.atan2( self.MVM[2, 1], self.MVM[2, 2])
        yDir = math.atan2(-self.MVM[2, 0], math.sqrt((self.MVM[2, 1] ** 2) + (self.MVM[2, 2] ** 2)))
        ZDir = math.atan2( self.MVM[1, 0], self.MVM[0, 0])

        return pygame.Vector3(xDir, yDir, ZDir)
