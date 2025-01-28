from OpenGL.GL import *

from utils import compileShader, createProgram

class Material:
    def __init__(self, vertexShader, fragmentShader) -> None:
        self.programID = createProgram(
            open(vertexShader).read(),
            open(fragmentShader).read(),
        )
        
    def use(self) -> None:
        glUseProgram(self.programID)