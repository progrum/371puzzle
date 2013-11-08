# Author: Robert Banks
# Id #: 121-00-4826

import sys                                  # to parse the input

# This function strips the newline char from each line in the file,
# and appends each line into a list.
def strip_file(f):
    
    c_list = []                             
    for line in f.readlines():
        line = line.rstrip('\n')
        c_list.append(line)
                         
    return (c_list)

#function to open a file and strip the newline chars and close the file.
def op_file(a_file):
    
    file1 = open(a_file, 'r')
    str_file = strip_file(file1)
    file1.close()
    return (str_file)


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

L = []
print A
for x in A:
    tup = (int(x[0]),int(x[2]))
    L.append(tup)
print L

#p_type = Puzzle(A[0],A[1:])
#print p_type.t_size
#print p_type.blk    

