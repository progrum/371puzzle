# Import to test code with block class
from block_class import *                 

class Tray:
	def __init__(self, size, numOfBlks, listOfBlks ):
	#attributes of a Tray Object
		self.width = size[1] #getLength(), columns
		self.length = size[0]   #getWidth(), rows 
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
        
	def createMatrix(self,length,width):
		print 'In create Matrix'
		# Update: initiated matrix to zero, and rearranged the loop.
		M = [[0 for i in range(width)] for j in range(length)]
		print ('End of create Matrix')
		return  M
			
	# Function to determine.
	def isFreeSpace(self,blk):
        
		directions = {"right" : 0 , "left" : 0, "up" : 0, "down" : 0}
        # returns direction dictionary that we can move
		return directions
		
	# Function to map the blocks to a dictionary	
	def map_blocks(self):
		
		tray_dict = {}
		print 'in map blocks'
		for blk in self.listOfBlks:
			tray_dict[(blk.position[0],blk.position[1])] = blk
		print 'out map blocks'
		return tray_dict
    
	
# To test code
A = [Block((4,5), [0,0]), Block((5,3), [6,7]), Block((1,1), [9,4])]
print A[0]
A[0].set_position(1,2)
print A[0]
B = Tray([5,10], len(A), A)
print B

C = B.isFreeSpace(A[0])
print C
# Below to print a formatted 3x4 matrix
D = B.createMatrix(3,4)
for x in D:
	print x

print B.listOfBlks[0].position
F = B.map_blocks()
print F
"""
tray_dict = {}
for blk in B.listOfBlks:
	tray_dict[(blk.position[0],blk.position[1])] = blk
print tray_dict
"""
"""
A = Tray([5,5], 1, [(4,5),[1,1]])
print A
print A.isFreeSpace(((4,3),[0,0]))
A.map_blocks()
"""