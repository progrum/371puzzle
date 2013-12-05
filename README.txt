371puzzle
=========

Authors:  Robert Banks and Eugene Mammie
email:    robert.banks@rutgers.edu
          eugene.mammie@rutgers.edu

Files: Project.py, block_class.py, trayClass.py, testbfs.py

Overview:
  This program was written using Python 2.7x, and using github to collaborate.
  This program was designed to solve the sliding block problem. 

Files:
  Project.py: contains functions to parse the input file, and create a list of
	Block objects from it. It also gets the tray configuration from a file. There
	is also a function to check if there are available moves a block can make
	from its current position. There is also an unfinished function that is 
	supposed to create a graph based on the tray configuration.
	
  block_class.py: contains the Block class, see Block class below.
  
  trayClass.py: contains the Tray class, see Tray class below.
  
  testbfs.py: contains some test code; NOTE: This section is not complete.

Objects:
  Two classes used were a Block class and a Tray class.
  Block:
    The Block class: creates block objects, allows user to retrieve block position and size,
      move block positions in a specified direction, and log the movement of the specific block.
      
  Tray:
    The Tray class: creates a tray object using a list of Block objects from the configuration file,
      the length of the list of Block objects, and the size of the tray configuration (read from the
      configuration file). The Tray class initializes a dictionary using the size provided 
      by the configuration file, and maps Block objects to an index in the dictionary. The Tray class 
      allows users to retrieve the length, width, number of blocks, and tests for free space around a 
	  given block.
      
Main:
		The program starts by taking in arguments from the command line such as, 
    python nameoffile.py placeholder init.config_file goal_file, where nameoffile.py is the file name,
    placeholder is just a placeholder because the -o option was not constructed, init.config_file is
    the initial configuration file, and goal_file is the goal file.
    
    The init.config_file is parsed and used to create the Block objects and Tray object.  The program is 
    supposed to then use a Depth-First Search approach to find a solution, the goal configuration file 
    should be checked after each iteration, to check to see if the problem was solved.
    
    The Tray object uses a dictionary to map indices inside the tray to a block object, therefore checking
    free space can be done in O(1) time, because the dictionary uses the index of the tray as its 
    key value and the value of a given index is the Block object if it contains a Block, and 0 if not. Therefore,
    only a check would need to be performed of adjacent indices in the dictionary (above,below,left,right), which 
	be done in a for loop. Thus methods to generate possible moves were based around this idea.
    
    The choice to initiate an entire dictionary containing every index of the 2D array should be done to 
    reduce the overall amount of work to be done to search for free space around a given block. We could
    have instead just initiated the dictionary using only the Block instances given by the file, however, 
	more work to calculate free space may have needed to be done.
	
	After the legal moves are generated for each block in the Tray, then the tree should be constructed, where
	the nodes of the tree are the current configurations of the Tray and the edges are the moves to reach
	one configuration to the next. I would have liked to use Breadth-First Search, however, the program is 
	not complete, so subsequent tests could not be performed. Too much time was spent trying to build the
	program bottom-up. This approach helped build helper-functions for the Block and Tray classes, but the 
	focus should have been on how to construct the information to best use for creating a graph in which 
	BFS could have been run.
    
    
    Although not complete, many lessons were learned during this coding assignment.
    (1) Map out the structure of the program on a high level first.
    (2) Build code piece-by-piece, ensuring correctness
    (3) Stay on task to build overall program
    (4) Don't underestimate the algorithm
