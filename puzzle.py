# Note: Extend Puzzle class to handle block dictionary and block list.
class Puzzle:
    def __init__(self, blocks):
        self.block_list = blocks
	
	def __str__(self):
		puzstring = str(self.block_list)
		return 'List of Blocks: '+puzstring
