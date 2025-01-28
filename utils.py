import numpy as np
from OpenGL.GL import *

def mapValue(currentMin, currentMax, newMin, newMax, value) -> float:
    currentRange = currentMax - currentMin
    newRange = newMax - newMin
    
    return newMin + newRange * ((value - currentMin) / currentRange)

def compileShader(shaderType, shaderSource):
    shaderID = glCreateShader(shaderType)
    glShaderSource(shaderID, shaderSource)
    glCompileShader(shaderID)
    
    compileSuccess = glGetShaderiv(shaderID, GL_COMPILE_STATUS)
    
    if not compileSuccess:
        error = glGetShaderInfoLog(shaderID)
        glDeleteShader(shaderID)
        
        error = f"\n{error.decode("utf-8")}"
        
        raise Exception(err)
    
    return shaderID

def createProgram(vertexShader, fragmentShader):
    vertexShaderID = compileShader(GL_VERTEX_SHADER, vertexShader)
    fragmentShaderID = compileShader(GL_FRAGMENT_SHADER, fragmentShader)
    
    programID = glCreateProgram()
    glAttachShader(programID, vertexShaderID)
    glAttachShader(programID, fragmentShaderID)
    
    glLinkProgram(programID)
    linkSuccess = glGetProgramiv(programID, GL_LINK_STATUS)
    
    if not linkSuccess:
        info = glGetProgramInfoLog(programID)
        raise RuntimeError(info)
    
    glDeleteShader(vertexShaderID)
    glDeleteShader(fragmentShaderID)
    
    return programID