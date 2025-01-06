from mesh import *

class LoadMesh(Mesh3D):
    def __init__(self, drawType, modelFilename) -> None:
        super().__init__()
        
        self.vertices, self.triangles = self.loadMesh(modelFilename)
        self.drawType = drawType
        
    def draw(self) -> None:
        for t in range(0, len(self.triangles), 3):
            glBegin(self.drawType)
            
            glVertex3fv(self.vertices[self.triangles[  t  ]])
            glVertex3fv(self.vertices[self.triangles[t + 1]])
            glVertex3fv(self.vertices[self.triangles[t + 2]])
            
            glEnd()
        glDisable(GL_TEXTURE_2D)
        
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