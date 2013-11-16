# Import to test code with block class
from block_class import *                 

class Tray:

	#Constructor to initialize the Tray object.
	def __init__(self, size, numOfBlks, listOfBlks ):
	#attributes of a Tray Object
		self.width = size[1] #getLength(), columns
		self.length = size[0]   #getWidth(), rows 
		self.numOfBlks = numOfBlks
		self.listOfBlks = listOfBlks  #new: getList of block objects
		self.matrix = self.createMatrix(size[0],size[1])
		self.tray_dict = {}
		
	# Method to return the length of the Tray.
	def length(self):
		return self.length
		
	# Method to return the width of the Tray.
	def width(self):
		return self.width
		
	# Method to return the number of blocks.
	def numOfBlks(self):
		return self.numOfBlks
		
	# Method to print out the Tray object.
	def __str__(self):
		size_string = str(self.length) +","+ str(self.width)
		numBlk_string = str(self.numOfBlks)   
		return 'Size:'+size_string+', NumberOfBlocks '+numBlk_string + str(self.matrix)
        
		
	# Method to create the tray as a matrix.
	def createMatrix(self,length,width):
		
		M = [[0 for i in range(width)] for j in range(length)]
		self.matrix = M
		return  M
			
	# Method to determine...
	def isFreeSpace(self,blk):
		upper_row = blk.position[0] + blk.size[0]
		upper_col = blk.position[1] + blk.size[1]
		for i in range(blk.position[0], upper_row):
			for j in range(blk.position[1], upper_col):
				self.matrix[i][j] = 2
				
		return self.matrix
        """
		directions = {"right" : 0 , "left" : 0, "up" : 0, "down" : 0}
        # returns direction dictionary that we can move
		return directions
		"""
		
	# Method to 0 out an index in the matrix.
	def zero_index(self, index1, index2):
	
		self.matrix[index1][index2] = 0
	
	
	# Method to set a single block to an index in the matrix
	def set_block(self, block):
		
		self.matrix[block.position[0]][block.position[1]] = block.size
	
	
	# Method to set all the blocks within the matrix.
	def set_blocks(self):

		for block in self.listOfBlks:
			self.matrix[block.position[0]][block.position[1]] = block.size

		return self.matrix
	
	# Method to map the blocks to a dictionary	
	def map_blocks(self):
		
		for blk in self.listOfBlks:
			self.tray_dict[blk.position[0],blk.position[1]] = blk
			
		return self.tray_dict
    
	
# To test code
A = [Block((4,5), [0,0]), Block((5,3), [1,2]), Block((1,1), [2,0])]
#print A[0]
#A[0].set_position(1,2)
#print A[0]
B = Tray([5,10], len(A), A)
for x in B.matrix:
	print x
	
print '\n'
B.set_blocks()
for x in B.matrix:
	print x
	
B.isFreeSpace(A[0])

for x in B.matrix:
	print x
