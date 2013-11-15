class Tray:
    def __init__(self, size, numOfBlks, listOfBlks ):
        #attributes of a Tray Object
                self.length = size[1] #getLength(), columns
                self.width = size[0]   #getWidth(), rows 
                self.numOfBlks = numOfBlks
                self.listOfBlks = listOfBlks  #new: getList of block objects
                self.matrix = self.createMatrix(size[1],size[0])
                
                
    def length(self):
                return self.length
    def width(self):
                return self.width
                
    def numOfBlks(self):
                return self.numOfBlks
            
    def __str__(self):
        size_string = str(self.length) +","+ str(self.width)
        numBlk_string = str(self.numOfBlks)   
        return 'Size:'+size_string+', NumberOfBlocks '+numBlk_string + str(self.matrix)
        
    def createMatrix(self,width,length):
        print 'In create Matrix'
        M = [[[i] for i in range(width)] for j in range(length)]
        print ('End of create Matrix')
        return  M
         
    def isFreeSpace(self,blk):
        
        directions = {"right" : 0 , "left" : 0, "up" : 0, "down" : 0}
        
        # returns direction dictionary that we can move
        return directions
    
A = Tray([3,3], 2, 2)
print A
#A.set_position(1,2)
#print A