import numpy as np
from OpenGL.GL import *

from graphicsData import GraphicsData
from mesh import Mesh3D
from texture import Texture
from uniform import Uniform
from utils import compileShader, createProgram

class LoadMesh(Mesh3D):
    def __init__(self, vaoRef, material, drawType, modelFilename, textureFilename = None, backFaceCull = False) -> None:
        super().__init__()
        
        self.vertices, self.uvs, self.uvsInd, self.normals, self.normalInd, self.triangles = self.loadMesh(modelFilename)
        
        self.coordinates = self.formatVertices(self.vertices, self.triangles)
        self.uvs = self.formatVertices(self.uvs, self.uvsInd)
        self.normals = self.formatVertices(self.normals, self.normalInd)
        
        self.material = material
        
        position = GraphicsData("vec3", self.coordinates)
        position.createVar(self.material.programID, "position")
        
        vertexNormals = GraphicsData("vec3", self.normals)
        vertexNormals.createVar(self.material.programID, "vertex_normal")
        
        vertexUvs = GraphicsData("vec2", self.uvs)
        vertexUvs.createVar(self.material.programID, "vertex_uv")
        
        self.texture = None
        if not textureFilename is None:
            self.image = Texture(textureFilename)
            self.texture = Uniform("sampler2D", [self.image.textureID, 1])
        
        self.drawType = drawType
        self.vaoRef = vaoRef
        
    def draw(self) -> None:
        if not self.texture is None:
            self.texture.findVar(self.material.programID, "tex")
            self.texture.load()
        
        glBindVertexArray(self.vaoRef)
        glDrawArrays(self.drawType, 0, len(self.coordinates))
        
    def loadMesh(self, filename) -> None:
        vertices = []
        uvs = []
        normals = []
        triangles = []

        uvsInd = []
        normalInd = []

        with open(filename, 'r') as file:
            line = file.readline()
            
            while line:
                if line[:2] == "v ":
                    vx, vy, vz = [float(value) for value in line[2:].split()]
                    
                    vertices.append((vx, vy, vz))
                    
                if line[:2] == "vn":
                    vx, vy, vz = [float(value) for value in line[3:].split()]
                    
                    normals.append((vx, vy, vz))
                    
                if line[:2] == "vt":
                    vx, vy, vz = [float(value) for value in line[3:].split()]
                    
                    uvs.append((vx, vy))
                    
                if line[:2] == "f ":
                    t1, t2, t3= [value for value in line[2:].split()]
                    
                    triangles.append([int(value) for value in t1.split("/")][0] - 1)
                    triangles.append([int(value) for value in t2.split("/")][0] - 1)
                    triangles.append([int(value) for value in t3.split("/")][0] - 1)
                    
                    uvsInd.append([int(value) for value in t1.split("/")][1] - 1)
                    uvsInd.append([int(value) for value in t2.split("/")][1] - 1)
                    uvsInd.append([int(value) for value in t3.split("/")][1] - 1)
                    
                    normalInd.append([int(value) for value in t1.split("/")][2] - 1)
                    normalInd.append([int(value) for value in t2.split("/")][2] - 1)
                    normalInd.append([int(value) for value in t3.split("/")][2] - 1)
                        
                line = file.readline()
            
        return vertices, uvs, uvsInd, normals, normalInd, triangles
        
    def formatVertices(self, coordinates, triangles):
        allTriangles = []
        
        for t in range(0, len(triangles), 3):
            allTriangles.append(coordinates[triangles[  t  ]])
            allTriangles.append(coordinates[triangles[t + 1]])
            allTriangles.append(coordinates[triangles[t + 2]])
            
        return np.array(allTriangles, np.float32)