# Import to test code with block class
from block_class import *                 

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
		# Update: initiated matrix to zero, and rearranged the loop.
        M = [[0 for i in range(length)] for j in range(width)]
        print ('End of create Matrix')
        return  M
         
    def isFreeSpace(self,blk):
        
        directions = {"right" : 0 , "left" : 0, "up" : 0, "down" : 0}
        
        # returns direction dictionary that we can move
        return directions
    
A = [Block((4,5), [0,0]), Block((5,3), [6,7]), Block((1,1), [9,4])]
print A[0]
A[0].set_position(1,2)
print A[0]
B = Tray([5,10], len(A), A)
print B
C = B.isFreeSpace(A[0])
print C

