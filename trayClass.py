class Tray:
    def __init__(self,length,width,numOfBlks):
        #attributes of a Tray Object
        self.length = length #getLength()
        self.width = width   #getWidth() 
        self.numOfBlks = numOfBlks
        self.matrix = self.matrix()
        
    def length(self):
        return self.length
    def width(self):
        return self.width
    def numOfBlks(self):
        return self.numOfBlks
    def matrix(self):
        M = [self.width()][self.length()]
        for x in M:
            M[x] = 0
        return  M
    
    
    