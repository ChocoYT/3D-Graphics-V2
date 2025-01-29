from OpenGL.GL import *

class Uniform:
    def __init__(self, dataType, data) -> None:
        self.dataType = dataType
        self.data = data
        
        self.varID = None
        
    def findVar(self, programID, varName) -> None:
        self.varID = glGetUniformLocation(programID, varName)
        
    def load(self) -> None:
        if self.dataType == "float":
            glUniform1f(self.varID, self.data)
        
        if self.dataType == "vec3":
            glUniform3f(self.varID, self.data[0], self.data[1], self.data[2])
            
        elif self.dataType == "mat4":
            glUniformMatrix4fv(self.varID, 1, GL_TRUE, self.data)
            
        elif self.dataType == "sampler2D":
            textureObj, textureUnit = self.data
            
            glActiveTexture(GL_TEXTURE0 + textureUnit)
            glBindTexture(GL_TEXTURE_2D, textureObj)
            glUniform1i(self.varID, textureUnit)
