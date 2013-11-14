class Block:
	def __init__(self, size, position):
		self.size = size
		self.position = position
		
	def block_position(self):
		return self.position
		
	def block_size(self):
		return self.size
		
	def __str__(self):
		size_string = str(self.size)
		position_string = str(self.position)
		return 'Size:'+size_string+', Position:'+position_string

	# to move the block
	def set_position(self, x, y):
		self.position = [self.position[0] + x, self.position[1] + y]		# x = rows, y = columns
		
	#def move_right(self):
	#	set_position(1, 0)
		
		
		
		
		
print 'hi'
A = Block((4,5), [0,0])
print A
A.set_position(1,2)
#A.move_right()
print A