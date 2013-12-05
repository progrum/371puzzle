# Code to test functions and classes
# Must group code together and organize

from block_class import *
from trayClass import *
from project import *


print "Config. File:", str(sys.argv[2])      #to get config filename
confile = str(sys.argv[2])
print "Goal File:", str(sys.argv[3])
gofile = str(sys.argv[3])


A = op_file(confile)
B = op_file(gofile)

# creating block objects and getting tray dimensions
C = block_list(A)
D = tray_list(A)

# tray initiation
E = Tray(D, len(C), C)
for x in E.get_list():
	print x


# maps the blocks according to size to the matrix
G = E.map_blocks_area()
for x in G:
	print x


# to move the block
for x in E.listOfBlks:
	print x

E.listOfBlks[2].move_right()
for x in E.listOfBlks:
	print x

T = E.getblock(1,1)
print T

# now need to update the tray
R = E.tray_update(E.listOfBlks[2])
for x in R:
	print x

	
print 'This is the goal file output.'
print B

