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
        
		
	# Method to return value of a given index.
	def getblock(self, index1, index2):
		return self.matrix[index1][index2]
		
	
	# Method to create the tray as a matrix.
	def createMatrix(self,length,width):
		
		M = [[0 for i in range(width)] for j in range(length)]
		self.matrix = M
		return  self.matrix
		
		
	# Method to initialize the tray dictionary.	
	def init_matrix_dict(self):
		
		for entry1 in range(self.length):
			for entry2 in range(self.width):
				self.tray_dict[(entry1,entry2)] = 0
		return self.tray_dict	
	
		
			
	# Method to map block area to matrix
	def map_blocks_area(self):
	
		for blk in self.listOfBlks:
			upper_row = blk.position[0] + blk.size[0]
			upper_col = blk.position[1] + blk.size[1]
			for i in range(blk.position[0], upper_row):
				for j in range(blk.position[1], upper_col):
					self.matrix[i][j] = blk.size
				
		return self.matrix
		
	
	# Method to set a single block to an index in the matrix
	def set_block(self, block):
		
		self.matrix[block.position[0]][block.position[1]] = block.size
    
	
	# Method to update dictionary and matrix when the block moves.
	def tray_update(self, block):
		
		# to update the matrix
		self.matrix = self.createMatrix(self.length,self.width)
		self.matrix = self.map_blocks_area()
		
		# to update the dictionary
		for item in self.tray_dict:
			for block in self.listOfBlks:
				if ((item[0] == block.position[0])& (item[1] == block.position[1])):
					self.tray_dict[block.position[0],block.position[1]] = block
					
		return self.matrix

