# Block Class to create Block Instances.
class Block:

	# Constructor to initiate the block object.
	def __init__(self, size, position):
		self.size = size
		self.position = position
		self.log = [position]
		self.moves = {}
		self.legal = []
		
	# Method to return the position of the block.
	def block_position(self):
		return self.position
	
	# Method to return the size of the block.
	def block_size(self):
		return self.size
		
	# Str method for the block object.
	def __str__(self):
		size_string = str(self.size)
		position_string = str(self.position)
		return 'Size:'+size_string+', Position:'+position_string
		
	# eq method to see if blocks are equal.
	def __eq__(self,other):
		return (self.size == other) & (self.position == other)
	
	# neq method to see if blocks are not equal.
	def __ne__(self, other):
		return (self.size != other) or (self.position != other)

	# Method to move the block, x = rows, y = columns.
	def set_position(self, x, y):
		self.position = [self.position[0] + x, self.position[1] + y]


	# Method to move a block.
	def move_block(self, direction):
		if (direction == 'down'):
			self.set_position(1, 0)
			print self, 'moved one space down' 
			self.log_move(self.position)
			return True
			
		elif (direction == 'up'):
			self.set_position(-1, 0)
			print self, 'moved one space up' 
			self.log_move(self.position)
			return True
			
		elif (direction == 'left'):
			self.set_position(0, -1)
			print self, 'moved one space to the left' 
			self.log_move(self.position)
			return True
			
		elif (direction == 'right'):
			self.set_position(0, 1)
			print self, 'moved one space to the right' 
			self.log_move(self.position)
			return True
		else:
			print 'Invalid Direction!'
			return False
			
	# Method to log movements of block.
	def log_move(self, movement):
		self.log.append(movement)
		return self.log
	
		
	# Method to hold all moves, in a dictionary; key is direction, value is True or False.
	def all_moves(self, key, value):
		self.moves[key] = value
		return self.moves

	
	# Method to hold list of legal moves.
	def legal_moves(self):
		self.legal = []
		for move in self.moves:
			if (self.moves[move] == True):
				self.legal.append(move)
		return self.legal
