import pygame

class Transform:
    def __init__(self, position = pygame.Vector3(0, 0, 0), rotation = pygame.Vector3(0, 0, 0), scale = pygame.Vector3(1, 1, 1)) -> None:
        self.setPosition(position)
        self.setRotation(rotation)
        self.setScale(scale)
        
    def moveX(self, n) -> None:
        self.position = pygame.Vector3(self.position.x + n, self.position.y, self.position.z)
        
    def moveY(self, n) -> None:
        self.position = pygame.Vector3(self.position.x, self.position.y + n, self.position.z)
    
    def moveZ(self, n) -> None:
        self.position = pygame.Vector3(self.position.x, self.position.y, self.position.z + n)
        
    def rotateX(self, n) -> None:
        self.rotation = pygame.Vector3(self.rotation.x + n, self.rotation.y, self.rotation.z)
        
    def rotateY(self, n) -> None:
        self.rotation = pygame.Vector3(self.rotation.x, self.rotation.y + n, self.rotation.z)
    
    def rotateZ(self, n) -> None:
        self.rotation = pygame.Vector3(self.rotation.x, self.rotation.y, self.rotation.z + n)
        
    def scaleX(self, n) -> None:
        self.scale = pygame.Vector3(self.scale.x + n, self.scale.y, self.scale.z)
        
    def scaleY(self, n) -> None:
        self.scale = pygame.Vector3(self.scale.x, self.scale.y + n, self.scale.z)
    
    def scaleZ(self, n) -> None:
        self.scale = pygame.Vector3(self.scale.x, self.scale.y, self.scale.z + n)
    
    def getPosition(self) -> pygame.Vector3:
        return self.position
    
    def setPosition(self, position) -> None:
        self.position = pygame.Vector3(position)
        
    def getRotation(self) -> pygame.Vector3:
        return self.rotation
    
    def setRotation(self, rotation) -> None:
        self.rotation = pygame.Vector3(rotation)
        
    def getScale(self) -> pygame.Vector3:
        return self.scale
    
    def setScale(self, scale) -> None:
        self.scale = pygame.Vector3(scale)
