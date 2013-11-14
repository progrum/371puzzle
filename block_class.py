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
