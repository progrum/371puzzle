# Authors: Robert Banks and Eugene Mammie


import sys                                  # to parse the input
from operator import itemgetter, attrgetter	# to sort the tuples
from block_class import *					# to test move block
from trayClass import  *
import copy



# This function strips the newline char from each line in the file,
# and appends each line into a list.
def strip_file(f):
    #exact_list = []
	line_list = []                             
	for line in f.readlines():
		line = line.rstrip('\n')
		line_list.append(line)
	print line_list
	
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
			i = i + 1

		else:
			Block_list.append(Block((int(config_file[i][0]), int(config_file[i][2])), [int(config_file[i][4]), int(config_file[i][6])]))
			i = i + 1
	return Block_list
	

# Function to create a list of the tray config.
def tray_list(config_file):

	Tray_list = [int(config_file[0][0]), int(config_file[0][2])]
	return Tray_list
	
# Function to parse the goal file contents into a list, to create a Tray instance of this data.
def goal_list(goal_file):

	goal = []
	i = 0
	for item in goal_file:
		#(int(goal_file[i][0]),int(goal_file[i][2])), [int(goal_file[i][4]), int(goal_file[i][6])]
		goal.append(Block((int(goal_file[i][0]),int(goal_file[i][2])), [int(goal_file[i][4]), int(goal_file[i][6])]))
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
def BFS(startTray, goalTray):
	Q = []
	#container_tray_dict = {}
	setup(startTray)
	#setup(goalTray)
	add(Q,startTray)

	count = 0
	solution = CompareAll(goalTray, startTray)
	
	while (solution == False):
		
		u = rem(Q)
		count = count + 1
		print 'LIVE MOVE COUNT:', count
		
		bound = len(u.legal_list)
		if (bound == 0):
			print 'Impossible Puzzle!'
			return u
		
		else:	
			for x in range(bound):
		
				tray_copy = copy.deepcopy(u)
			
				tray_copy.legal_list[x][0].move_block(tray_copy.legal_list[x][1])
				tray_copy.init_dict()				# these two lines to reinitialize the dictionary
				tray_copy.set_blocks()
				tray_copy.legal_move_remove()		# clears copy tray objects legal moves, now to generate new list
				setup(tray_copy)					# sets up tray_copy

				solution = CompareAll(goalTray, tray_copy)
				if (solution == True):
					print 'found in %d moves!' % count
					return tray_copy	
					
				else:
					add(Q, tray_copy)				# to add the new tray copy to the Q
				#print Q

	print '\n'
	print 'Solution found in %d moves!' % count
	return tray_copy

	
# global add, for stack
def add(Q,x):
	Q.append(x)
	
# global pop, for stack
def rem(Q):
	head = 0
	x = Q[head]
	Q.pop(head)
	return x
	
	
	
# Function to compare current tray to final tray.
def CompareAll(goalTray, trayInstance):
	for block in goalTray.listOfBlks:
		if (goalTray.tray_dict[(block.position[0],block.position[1])] == trayInstance.tray_dict[(block.position[0],block.position[1])]):
			continue
			
		else:
			return False
	return True
	
	
	
	
	
	
	
	
	
	
	
	
	#container_tray_dict[str(startTray)] = {'adj_moves': startTray.legal_list, 'color': 'grey', 'goal_block': startTray.tray_goal}
	#print startTray
	#print container_tray_dict	
	
	
# function to create dictionary of tray objects as keys and certain other attributes
# creates a dictionary of Tray objects
#traydict = {}		# probably should be somewhere else
# function should take in newly setup tray object
#traydict[E]={'adj_moves': E.legal_list, 'color': 'grey', 'pre': None 'goalblock': E.tray_goal}
#print traydict
