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


#print A[0][2]
#C = Tray((int(A[0][0]),int(A[0][2])), block_list, block_dictionary)
#print C

# Input size as a tuple, to avoid accidental changes.
#D = [Block((1,2), [0,0]), Block((2,3), [3,5])]
#E = Puzzle(D)
#print 'Puzzle class: ', E
