# Import to test code with block class
from block_class import *   
from operator import itemgetter, attrgetter              

class Tray:

	#Constructor to initialize the Tray object.
	def __init__(self, size, numOfBlks, listOfBlks, goal):
		self.tray_dict = {}
	#attributes of a Tray Object
		self.width = size[1] #getLength(), columns
		self.length = size[0]   #getWidth(), rows 
		self.numOfBlks = numOfBlks
		self.listOfBlks = listOfBlks  # getList of block objects
		self.tray_dict = self.init_dict()
		self.tray_goal = goal			#new: to keep goal inside of tray instance
		self.legal_list = []			#new: keeps a list of all possible moves; priority queue goes here i think
		
		
	# Method to return the length of the Tray.
	def length(self):
		return self.length
		
	# Method to return the width of the Tray.
	def width(self):
		return self.width
		
	# Method to return the number of blocks.
	def numOfBlks(self):
		return self.numOfBlks
		
	# Method to return the goal configuration
	def goal_config(self):
		return self.tray_goal
		
	# Method to print out the Tray object.
	def __str__(self):
		size_string = str(self.length) +","+ str(self.width)
		numBlk_string = str(self.numOfBlks)   
		return 'Size:'+size_string+'\nNumberOfBlocks: '+numBlk_string +'\n'+ str(self.tray_dict)
        
		
	# Method to return value of a given index.
	def getblock(self, key):
		return self.tray_dict[key]
		
	
	# Method to return sorted list of Dictionary keys.
	def get_list(self):
		return sorted(self.tray_dict.keys(), key = itemgetter(0,1))
	
	# Method to initialize the tray dictionary.	
	def init_dict(self):
		
		for entry1 in range(self.length):
			for entry2 in range(self.width):
				self.tray_dict[(entry1,entry2)] = 0
		return self.tray_dict	

	
	# Method to set blocks to proper coordinates. 
	def	set_blocks(self):
		
		for block in self.listOfBlks:
			self.tray_dict[block.position[0],block.position[1]] = block


	# Method to determine if there is a left free space.
	def left_free_space(self, block):

		left_col = block.position[1] - 1
		blk_range = block.position[0] + block.size[0]
		
		if (blk_range > self.width):
			block.all_moves('left', False)
			return False


		if (left_col < 0):
			block.all_moves('left', False)
			return False

		i = block.position[0]
		for index in range(block.position[0],blk_range):
			if (self.tray_dict[(i,left_col)] == 0):
				i = i + 1
				
			else:
				block.all_moves('left', False)
				return False
		block.all_moves('left', True)
		return True
	
		
	# Method to determine if there is a left free space.
	def right_free_space(self, block):

		right_col = block.position[1] + 1
		blk_range = block.position[0] + block.size[0]
		
		if (blk_range > self.width):
			block.all_moves('right', False)
			return False
		
		if (right_col > (self.width - 1)):
			block.all_moves('right', False)
			return False
			
		i = block.position[0]
		for index in range(block.position[0],blk_range):
			if (self.tray_dict[(i,right_col)] == 0):
				i = i + 1
			else:
				block.all_moves('right', False)
				return False
		block.all_moves('right', True)
		return True		
		
		
	# Method to determine if there is a upward free space.
	def up_free_space(self, block):

		up_row = block.position[0] - 1
		blk_range = block.position[1] + block.size[1]
		
		
		if (blk_range > self.length):
			block.all_moves('up', False)
			return False
		
		if (up_row < 0):
			block.all_moves('up', False)
			return False
			
		i = block.position[1]
		for index in range(block.position[1],blk_range):
			if (self.tray_dict[(up_row,i)] == 0):
				i = i + 1
			else:
				block.all_moves('up', False)
				return False
		block.all_moves('up', True)
		return True	
		
		
	# Method to determine if there is a downward free space.
	def down_free_space(self, block):

		down_row = block.position[0] + 1
		blk_range = block.position[1] + block.size[1]
		
		if (blk_range > self.length):
			block.all_moves('down', False)
			return False
		
		if (down_row > (self.length - 1)):
			block.all_moves('down', False)
			return False
			
		i = block.position[1]
		for index in range(block.position[1],blk_range):
			if (self.tray_dict[(down_row,i)] == 0):
				i = i + 1
			else:
				block.all_moves('down', False)
				return False
		block.all_moves('down', True)
		return True	
		
	# Method to get a list of all possible moves from every block.
	def legal_move_list(self):
		
		for block in self.listOfBlks:
			if (len(block.legal_moves()) != 0):
				step = block.legal_moves()
				count = len(step)
				for i in range(count):
					self.legal_list.append((block,step[i]))
		return self.legal_list	

    # Method to clear the current legal_list of the tray instance.
	def legal_move_remove(self):
                
		self.legal_list = []
		return self.legal_list
		
	# Method to see if tray objects are equal; implies blocks sizes and positions are equal, can detect by the dictionary.	
	def	__eq__(self,other):
		return self.tray_dict == other
			 
	
	"""	
	# Function to pop the self.legal_list	
	def Dequeue(self):
                
		head = 0
		x = self.legal_list[head]
		self.legal_list.pop(head)
		return x
		
	# Function to put key value on the queue.
	def Enqueue(self,x):
                
		self.legal_list.append(x)
	"""	
