# Authors: Robert Banks and Eugene Mammie

import networkx as nx
import sys                                  # to parse the input
from operator import itemgetter, attrgetter	# to sort the tuples
from block_class import *					# to test move block

G = nx.Graph()

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
	

# Function to create a list of the tray config.
def tray_list(config_file):

	Tray_list = [int(config_file[0][0]), int(config_file[0][2])]
	return (Tray_list)

	
# Function to test around a block
def move_generator(block):
	
	E.down_free_space(block)
	E.up_free_space(block)
	E.left_free_space(block)
	E.right_free_space(block)
	return block.moves
	
	
# Function to generate the graph, not complete
def Build_Graph(Tray):
	Tray.set_blocks()
	G.add_node(Tray)
	
	for block in Tray.listOfBlks:
		move_generator(block)
	for block in Tray.listOfBlks:
		block.legal_moves()