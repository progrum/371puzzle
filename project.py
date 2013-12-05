# Authors: Robert Banks and Eugene Mammie

import copy
import sys                                  # to parse the input
from operator import itemgetter, attrgetter	# to sort the tuples
from block_class import *					# to test move block
from trayClass import  *



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
	
# Function to parse the goal file contents, needs more work, but layout seems correct.
def goal_dict(goal_file):

	goal = {}
	goal[(int(goal_file[0][0]),int(goal_file[0][2]))] = [int(goal_file[0][4]), int(goal_file[0][6])]
	return goal

	
# Function to test around a block
def move_generator(Tray, block):
	
	Tray.down_free_space(block)
	Tray.up_free_space(block)
	Tray.left_free_space(block)
	Tray.right_free_space(block)
	return block.moves
	
	
# Function to setup the tray object
def setup(Tray):

	Tray.set_blocks()
	for block in Tray.listOfBlks:
		move_generator(Tray, block)
	
	for block in Tray.listOfBlks:
		block.legal_moves()

	Tray.legal_move_list()
	
	return Tray

	
# Modified Breadth-First to find solution to Sliding Block Puzzle.
def BFS(startTray):
	Q = []
	setup(startTray)
	add(Q,startTray)
	
	count = 0
	solution = 0
	
	while (solution == 0):
		
		u = rem(Q)
		

		if (u.getblock((u.tray_goal.values()[0][0],u.tray_goal.values()[0][1])) == 0)or (u.getblock((u.tray_goal.values()[0][0],u.tray_goal.values()[0][1])).size != u.tray_goal.keys()[0]):  # change to handle whether 0 or not equal to
			count = count + 1
			print 'LIVE MOVE COUNT:', count
			
			bound = len(u.legal_list)
			for x in range(bound):
			
				tray_copy = copy.deepcopy(u)
				tray_copy.legal_list[x][0].move_block(tray_copy.legal_list[x][1])
				tray_copy.init_dict()				# these two lines to reinitialize the dictionary
				tray_copy.set_blocks()
				tray_copy.legal_move_remove()		# clears copy tray objects legal moves, now to generate new list
				set_new_tray = setup(tray_copy)		# sets up tray_copy
				add(Q, set_new_tray)                    # to add the new tray copy to the Q
				# in above compare tray instance to other tray instances in overall dictionary, add new tray instance
				# if new instance is not already in overall dictionary
				
			

		else:
			solution = 1
			print '\n'
			print 'Solution found in %d moves!' % count
			print 'Goal block and position:', u.tray_goal
			return u

	
# global add, for stack
def add(Q,x):
	Q.append(x)
	
# global pop, for stack
def rem(Q):
	head = 0
	x = Q[head]
	Q.pop(head)
	return x
