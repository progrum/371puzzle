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
print A[0][0]
print A[0][2]
# Tray((A[0][0],A[0][2]), ListOfBlocks, numofblocks)
# Block class gets A[1:]; list of strings of input from file
# Tray class gets A[0]; tray size (row column)




block_dictionary = create_dictionary(A)
block_list = create_list(block_dictionary)
print block_dictionary
print block_list
