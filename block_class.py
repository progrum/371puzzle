# Block Class to create Block Instances.
class Block:

	# Constructor to initiate the block object.
	def __init__(self, size, position):
		self.size = size
		self.position = position
		self.log = []
		
	# Method to return the position of the block.
	def block_position(self):
		return self.position
	
	# Method to return the size of the block.
	def block_size(self):
		return self.size
		
	# Str method  for the block object.
	def __str__(self):
		size_string = str(self.size)
		position_string = str(self.position)
		return 'Size:'+size_string+', Position:'+position_string

	# Method to move the block, x = rows, y = columns.
	def set_position(self, x, y):
		self.position = [self.position[0] + x, self.position[1] + y]
	
	# Method to move block to the right.
	def move_right(self):
		self.set_position(1, 0)
		print 'moved one space to the right' 
		
	# Method to log movements of block.
	def log_move(self, movement):
		log.append(movement)
		return log
		
		
# Code to test the block class.
A = Block((4,5), [0,0])
print A
A.set_position(1,2)
print A
A.move_right()
print A
#print A.size