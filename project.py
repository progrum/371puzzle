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
			

def move_block(Tray, Block, Direction):
	# move the block
	if (Direction == 'left'):
		Block.
		
	if (Direction == 'right'):
		do
	
	if (Direction == 'up'):
		do
		
	if (Direction == 'down'):
		do
def free_space(Tray, Block):
	# check to make sure lies inside the boundary of the tray configuration
