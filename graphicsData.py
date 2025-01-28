import numpy as np
from OpenGL.GL import *

class GraphicsData:
    def __init__(self, dataType, data) -> None:
        self.dataType = dataType
        self.data = data
        
        self.bufferRef = glGenBuffers(1)
        self.load()
        
    def load(self) -> None:
        data = np.array(self.data, np.float32)
        
        glBindBuffer(GL_ARRAY_BUFFER, self.bufferRef)
        glBufferData(GL_ARRAY_BUFFER, data.ravel(), GL_STATIC_DRAW)
        
    def createVar(self, programID, varName) -> None:
        varID = glGetAttribLocation(programID, varName)
        glBindBuffer(GL_ARRAY_BUFFER, self.bufferRef)
        
        if self.dataType == "vec3":
            glVertexAttribPointer(varID, 3, GL_FLOAT, False, 0, None)
            
        elif self.dataType == "vec2":
            glVertexAttribPointer(varID, 2, GL_FLOAT, False, 0, None)
        
        glEnableVertexAttribArray(varID)
