# Authors: Robert Banks and Eugene Mammie


import sys                                  # to parse the input
from operator import itemgetter, attrgetter	# to sort the tuples

from block_class import *					# to test move block

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


# Function to create a list of Block instances from the configuration file.
def block_list(config_file):

	Block_list = []
	i = 0
	for item in config_file:
		if (i == 0):
			#Tray_list.append((int(A[i][0]), int(A[i][2])))
			i = i + 1

		else:
			Block_list.append(Block((int(config_file[i][0]), int(config_file[i][2])), [int(config_file[i][4]), int(config_file[i][6])]))
			i = i + 1
	return (Block_list)
	
# Function to sort the block list by position
"""def sort_blocks(listOfBlocks):
	sorted(listOfBlocks, k=itemgetter(
"""
# Function to create a list of the tray config.
def tray_list(config_file):

	Tray_list = [int(config_file[0][0]), int(config_file[0][2])]
	return (Tray_list)
"""	
# To test the tray_list function
A = ['3 4 0 0']
blklist = block_list(A)
trlist = tray_list(A)
# to check contents of Block_list.
for blk in blklist:
	print blk
print trlist
"""


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
		
# Function to perform algorithm on blocks
#def algorithm():
# Need to perform DFS, categorize possible moves, choose move based on goal position.
	
		
		
		

# Code to test the move_block function.	
"""A = Block((1,2), [3,2])
print A
placeholder = 0
move_block(placeholder, A, 'up')
print A
move_block(placeholder, A, 'left')
print A
		
#def free_space(Tray, Block):
	# check to make sure lies inside the boundary of the tray configuration
"""