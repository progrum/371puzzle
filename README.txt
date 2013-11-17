371puzzle
=========

Authors:  Robert Banks and Eugene Mammie
email:    robert.banks@rutgers.edu
          eugene.mammie@rutgers.edu

Files: Project.py, block_class.py, trayClass.py

Overview:
  This program was written using Python 2.7x, and using github to collaborate.
  This program was designed to solve the sliding block problem. 
  
Objects:
  Two classes used were a Block class and a Tray class.
  Block:
    The Block class: creates block objects, allows user to retrieve block position and size,
      move block positions in a specified direction, and log the movement of the specific block.
      
  Tray:
    The Tray class: creates a tray object using a list of Block objects from the configuration file,
      the length of the list of Block objects, and the size of the tray configuration (read from the
      configuration file). The Tray class initializes a matrix and dictionary using the size provided 
      by the configuration file, and maps Block objects to an index in the matrix. The Tray class 
      allows users to retrieve the length, width, number of blocks, map blocks area in the matrix 
      (2D array), and supposed to test for free space around a given block.
      
Main:
  The program starts by taking in arguments from the command line such as, 
    python nameoffile.py placeholder init.config_file goal_file, where nameoffile.py is the file name,
    placeholder is just a placeholder because the -o option was not constructed, init.config_file is
    the initial configuration file, and goal_file is the goal file.
    
    The init.config_file is parsed and used to create the Block objects and Tray object.  The program is 
    supposed to then use a Depth-First Search approach to find a solution, the goal configuration file 
    should be checked after each iteration, to check to see if the problem was solved.
    
    The Tray object uses a dictionary to map indices inside the matrix to a block object, therefore checking
    free space can be done in O(1) time, because the dictionary uses the index of the matrix as its 
    key value and the value of a given index is the Block size if it contains a Block, and 0 if not. Therefore,
    only a check would need to be performed of adjacent indices in the dictionary (above,below,left,right).
    
    The choice to initiate an entire dictionary containing every index of the 2D array should be done to 
    reduce the overall amount of work to be done to search for free space around a given block. We could
    have instead just iniated the dictionary using only the Block instances given by the file, however, the
    time to check free space takes more time and the code is more complex.
    
    By sorting the list of dictionary keys (indices in matrix), we can perform binary search on the block 
    instances, and be able to find the closest block to a specific area of the matrix in O(lg n) time.
    
    
    
    Eugene--See the guidlines, and add what you see fit (Don't forget to delete this line.)
    
    Although not complete, many lessons were learned during this coding assignment.
    (1) Map out the structure of the program on a high level first.
    (2) Build code piece-by-piece, ensuring correctness
    (3) Stay on task to build overall program
    (4) Don't underestimate the algorithm
