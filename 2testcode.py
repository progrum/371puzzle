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

print A

# Tray((A[0][0],A[0][2]), ListOfBlocks, numofblocks)
# Block class gets A[1:]; list of strings of input from file
# Tray class gets A[0]; tray size (row column)

	
	
#block_dictionary = create_dictionary(A)
#block_list = create_list(block_dictionary)
#print block_dictionary
#print block_list



# This code works, used to list the block instances.
#OBblock_list = [Block((1,1),[0,0]), Block((2,3),[11,3]), Block((4,2),[5,4])]
#for blk in OBblock_list:
#	print blk
#print 'ob: ', OBblock_list[0]
#print A[0][2]
#C = Tray((int(A[0][0]),int(A[0][2])), len(OBblock_list), OBblock_list)
#print C.size()

