# Author: Robert Banks Eugene Mammie


import sys                                  # to parse the input

# This function strips the newline char from each line in the file,
# and appends each line into a list.
def strip_file(f):
    
    c_list = []                             
    for line in f.readlines():
        line = line.rstrip('\n')
        c_list.append(line)
                         
    return (c_list)

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
	
	
class Puzzle:
    def __init__(self, tray_size, blocks):
        self.t_size = tray_size
        self.blk = blocks

    




#_______________________________________#    #space below used for testing above functions and class
print "Config. File:", str(sys.argv[2])      #to get config filename
confile = str(sys.argv[2])
print "Goal File:", str(sys.argv[3])
gofile = str(sys.argv[3])


A = op_file(confile)
B = op_file(gofile)

block_dictionary = create_dictionary(A)
print block_dictionary
 