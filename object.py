from OpenGL.GL import *

from camera import Camera
from loadMesh import LoadMesh
from material import Material
from transform import Transform
from uniform import Uniform

class Object:
    def __init__(self, objName) -> None:
        self.name = objName
        self.components = []
        self.material = None
        
        self.vaoRef = glGenVertexArrays(1)
        glBindVertexArray(self.vaoRef)
        
        self.time = 0
        
    def addComponent(self, component) -> None:
        if isinstance(component, Transform):
            self.components.insert(0, component)
            return
        elif isinstance(component, Material):
            self.material = component
            
        self.components.append(component)
        
    def getComponent(self, classType):
        for c in self.components:
            if type(c) is classType:
                return c
            else:
                return None
        
    def update(self, camera: Camera, dt, events = None) -> None:
        self.material.use()
        
        for c in self.components:
            if isinstance(c, Transform):
                projection = Uniform("mat4", camera.getPPM())
                projection.findVar(self.material.programID, "projection_mat")
                projection.load()
                
                lookat = Uniform("mat4", camera.getVM())
                lookat.findVar(self.material.programID, "view_mat")
                lookat.load()
                
                transformation = Uniform("mat4", c.getMVM())
                transformation.findVar(self.material.programID, "model_mat")
                transformation.load()
                
                time = Uniform("float", self.time)
                time.findVar(self.material.programID, "time")
                time.load()
                
            elif isinstance(c, LoadMesh):
                c.draw()
                
        if not dt is None:
            self.time += dt
