### IMPORTS ###
import trunkFileDir

### RANDOM CRAP ###

testKit = True


### CLASSES ###

class node:
    def __init__(self, nodeId, active, rootDir, rootDirFile):
        self.nodeId = nodeId
        self.active = active
        self.rootDir = rootDir
        self.rootDirFile = rootDirFile
        if testKit == True:
            print("Node ", self.nodeId, " created!")

    def ping(self):
        return(True)

    def nodeIdQuery(self):
        return self.nodeId

    def activeQuery(self):
        return self.active

    def rootDirQuery(self):
        return self.rootDir

    def rootDirFileQuery(self):
        return self.rootDirFile

    def fullDataQuery(self):
        return self.nodeId, self.active, self.rootDir, self.rootDirFile

### FUNCTIONS ###
