# File to test code
import networkx as nx
G = nx.Graph()

from block_class import *
from trayClass import *
from project import *


print "Config. File:", str(sys.argv[2])      #to get config filename
confile = str(sys.argv[2])
print "Goal File:", str(sys.argv[3])
gofile = str(sys.argv[3])


A = op_file(confile)
B = op_file(gofile)
B = goal_dict(B)

# creating block objects and getting tray dimensions
C = block_list(A)
D = tray_list(A)

# tray initiation
E = Tray(D, len(C), C, B)
L = Tray(D, len(C), C, B)

# viewing the dictionary
print E

# Function sets up the Tray object
print setup(E)
print setup(L)
for x in E.listOfBlks:
	print x
	
# To test eq and ne operators in block class
#print E.listOfBlks[0] == E.listOfBlks[1]
#print E.listOfBlks[0] != E.listOfBlks[1]

# To test eq operator in tray class
print E == L

	
#for x in E.legal_list:
#	print x[0],x[1]


# to view how size is expressed
#print E.listOfBlks[1].size
#print E.tray_goal.keys()[0]		# size of goal block
#print 'this is ...'
#print E.getblock((E.tray_goal.values()[0][0],E.tray_goal.values()[0][1]))

#print (E.tray_goal.values()[0][0],E.tray_goal.values()[0][1])

#for x in E.legal_list:
	#print x[0], x[1] 		


#s = BFS(E)
#for x in s.listOfBlks:
#	print x


# creates a dictionary of Tray objects
#traydict = {}
#traydict[E]={'adj_moves': E.legal_list, 'color': 'grey', 'pre': None 'goalblock': E.tray_goal}
#print traydict


# global stack, should get first tray instance as first entry
#global stack = []
#stack = [E]
#for tup in E.legal_list:
#	stack.append(tup)
#print stack











