class Tray:
    def __init__(self, size, numOfBlks, listOfBlks ):
        #attributes of a Tray Object
        self.length = size[1] #getLength(), columns
        self.width = size[0]   #getWidth(), rows 
        self.numOfBlks = numOfBlks
		self.listOfBlks = listOfBlks  #new: getList of block objects
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
    
    
    