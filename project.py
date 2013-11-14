# Authors: Robert Banks and Eugene Mammie


import sys                                  # to parse the input
from operator import itemgetter, attrgetter	# to sort the tuples

# This function strips the newline char from each line in the file,
# and appends each line into a list.
def strip_file(f):
    
    line_list = []                             
    for line in f.readlines():
        line = line.rstrip('\n')
        line_list.append(line)
                         
    return (line_list)

# function to open a file and strip the newline chars and close the file.
def op_file(a_file):
    
    file1 = open(a_file, 'r')
    str_file = strip_file(file1)
    file1.close()
    return (str_file)


# function to create a dictionary to store blocks; 
# keys are the size and unique id; values are the current positions.
def create_dictionary(input_list):

	dct = {}
	i = 0
	id = 0
	for item in input_list:
		if i != 0:
			tup = (int(item[0]), int(item[2]), id)
			val = (int(item[4]), int(item[6]))
			dct[tup] = val
			id = id + 1
	
		else:
			i = i + 1
	return (dct)
	
	
# Function to sort the list of tuples, by position.
def create_list(input_dict):

	dict_list = sorted([(value,key) for (key,value) in input_dict.items()])
	dict_list = [key for (value, key) in dict_list]	
	return (dict_list)
	

# Function to perform binary search on sorted list of dictionary keys; sorted by position.
# NOTE: Augment for finding in dictionary...
def binary_search(dict_list, key, imin, imax):

	# test if array is empty
	if (imax < imin):
		# set is empty, so return value showing not found
		return (False)
	else:
		# calculate midpoint to cut set in half
		imid = (imin + imax) / 2;
 
		# three-way comparison
		if (A[imid] > key):
			# key is in lower subset
			return binary_search(A, key, imin, imid-1);
		elif (A[imid] < key):
			# key is in upper subset
			return binary_search(A, key, imid+1, imax);
		else:
			# key has been found
			return imid;	
	
	
	
# Note: Extend Puzzle class to handle block dictionary and block list.
class Puzzle:
    def __init__(self, blocks):
        self.block_list = blocks
	
	def __str__(self):
		puzstring = str(self.block_list)
		return 'List of Blocks: '+puzstring
	
	
# Prototype Class Tray; used for testing main
#class Tray:
#    def __init__(self, t_size, blk_list, blk_dict):
#        self.size = t_size
#        self.blk_list = blk_list
#        self.blk_dict = blk_dict
#
#   def __str__(self):
#        string = self.size
#        return 'Tray is size'+' '+str(string)

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




#_______________________________________#    #space below used for testing above functions and class
print "Config. File:", str(sys.argv[2])      #to get config filename
confile = str(sys.argv[2])
print "Goal File:", str(sys.argv[3])
gofile = str(sys.argv[3])


A = op_file(confile)
B = op_file(gofile)

block_dictionary = create_dictionary(A)
block_list = create_list(block_dictionary)
print block_dictionary
print block_list


#print A[0][2]
#C = Tray((int(A[0][0]),int(A[0][2])), block_list, block_dictionary)
#print C

# Input size as a tuple, to avoid accidental changes.
#D = [Block((1,2), [0,0]), Block((2,3), [3,5])]
#E = Puzzle(D)
#print 'Puzzle class: ', E