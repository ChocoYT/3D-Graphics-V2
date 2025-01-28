import numpy as np

from graphicsData import GraphicsData
from mesh import *
from utils import compileShader, createProgram

class LoadMesh(Mesh3D):
    def __init__(self, vaoRef, material, drawType, modelFilename, textureFilename = "", backFaceCull = False) -> None:
        super().__init__()
        
        self.vertices, self.triangles = self.loadMesh(modelFilename)
        self.coordinates = self.formatVertices(self.vertices, self.triangles)
        
        self.drawType = drawType
        self.vaoRef = vaoRef
        
        position = GraphicsData("vec3", self.coordinates)
        position.createVar(material.programID, "position")
        
    def draw(self) -> None:
        glBindVertexArray(self.vaoRef)
        glDrawArrays(self.drawType, 0, len(self.coordinates))
        
    def loadMesh(self, filename) -> tuple[list[tuple[float] | int]]:
        vertices = []
        triangles = []
        
        with open(filename, "r") as f:
            line = f.readline()
            while line:
                if line[:2] == "v ":
                    vx, vy, vz = [float(value) for value in line[2:].split()]
                    
                    vertices.append((vx, vy, vz))
                if line[:2] == "f ":
                    t1, t2, t3 = [value for value in line[2:].split()]
                    
                    triangles.append([int(value) for value in t1.split("/")][0] - 1)
                    triangles.append([int(value) for value in t2.split("/")][0] - 1)
                    triangles.append([int(value) for value in t3.split("/")][0] - 1)
                    
                line = f.readline()
                
            return vertices, triangles

    def formatVertices(self, coordinates, triangles):
        allTriangles = []
        
        for t in range(0, len(triangles), 3):
            allTriangles.append(coordinates[triangles[  t  ]])
            allTriangles.append(coordinates[triangles[t + 1]])
            allTriangles.append(coordinates[triangles[t + 2]])
            
        return np.array(allTriangles, np.float32)