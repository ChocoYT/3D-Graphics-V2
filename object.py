from mesh import *
from transform import *

class Object:
    def __init__(self, objName) -> None:
        self.name = objName
        self.components = []
        
    def addComponent(self, component) -> None:
        if isinstance(component, Transform):
            self.components.insert(0, component)
            return
            
        self.components.append(component)
        
    def getComponent(self, classType):
        for c in self.components:
            if type(c) is classType:
                return c
            else:
                return None
        
    def update(self) -> None:
        glPushMatrix()
        
        for c in self.components:
            if isinstance(c, Transform):
                position = c.getPosition()
                rotation = c.getRotation()
                scale    = c.getScale()

                glTranslatef(position.x, position.y, position.z)
                glScalef(scale.x, scale.y, scale.z)
                glRotatef(rotation.x, 1, 0, 0)
                glRotatef(rotation.y, 0, 1, 0)
                glRotatef(rotation.z, 0, 0, 1)
            
            elif isinstance(c, Mesh3D):
                c.draw()
                
        glPopMatrix()
