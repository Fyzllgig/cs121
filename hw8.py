#David Parrott
#11239947
#CS 121
#HW8

#Calling the life() function will open a window allowing the user to set up
#a board that will then have the rules of John Conway's game of Life applied to
#to it. The life() function takes variables width and height ie life(20,20) and
#using csplot opens up an empty board. By holding 's' and selecting tiles on the
#board the state of the initial board can be set.

#While the game is running the user can pause by pressing 'p' resume by 
#pressing 'r' advance one generation by pressing '1' and quit by pressing 'q'

keys = 0
                                       #keys will be used to store values for user input
R = 0
                                       #R will be a place holder used to set up the board
B = []
                                       #B will hold information on the board
oldB = []
                                       #oldB will hold information on the board
                
import csplot
import random
import time


def createOneRow(n):
                                       #returns rows of n zeros...  You might use
                                       #this is the INNER loop in createBoard
    for col in range(n):
        R = 0
    return R

def createBoard(x,y):
                                       #sets up a 2D board by calling createOneRow 
                                       #vertically and horizontally
    B = [[0 for i in range(x)] for j in range(y)]
    return B
    
def update1( B ):
                                       #Takes an empty board as input and modifies that board
                                       #so that it has a diagonal strip of "on" cells
    width = len(B[0])
    height = len(B)
   
    for row in range(height):
        for col in range(width):
            if row == col:
                B[row][col] = 1
            else:
                B[row][col] = 0  
                                       # else not needed here,but OK

def update2(B):
                                       #takes an empty board as input and 
                                       #modifies that board so that it is all
                                       #'live' cells except for a border 1 cell 
                                       #wide around the perimeter
    width = len(B[0])
    height = len(B)
    for row in range(height):
        for col in range(width):
            if row == 0 or row == height-1:
                B[row][col] = 0
            elif col == 0 or col == width-1:
                B[row][col] = 0
            else:
                B[row][col] = 1

def updateRandom(B):
                                       #takes an empty board as input and 
                                       #modifies that board so that it is a random
                                       #set of 'live' cells except for a border 
                                       #1 cell wide around the perimeter
    width = len(B[0])
    height = len(B)
    for row in range(height):
        for col in range(width):
            if row == 0 or row == height-1:
                B[row][col] = 0
            elif col == 0 or col == width-1:
                B[row][col] = 0
            else:
                B[row][col] = random.choice([0,1])

                                            
def updateReversed(oldB, newB):
                                       #references oldB to store the opposite 
                                       #state for every cell as newB
                                       #leaves a 1 cell border around the primeter
    width = len(oldB[0])
    height = len(oldB)
    for row in range(height):
        for col in range(width):
            if row == 0 or row == height-1:
                newB[row][col] = 0
            elif col == 0 or col == width-1:
                newB[row][col] = 0
            elif oldB[row][col] == 0:
                newB[row][col] = 1
            elif oldB[row][col] == 1:
                newB[row][col] = 0
                
def updateNextLife(oldB,newB):
    width = len(oldB[0])
    height = len(oldB)
    x = height -1                
    for row in range(height):
        for col in range(width):
            ROW = x-row                #this is necessary because csplot and
                                       #python handle coordinate systems
                                       #differently WRT the Y-axis.
            state = countNeighbors(oldB,ROW,col)
                                       #state holds information about how many
                                       #neighbors a cell has
            if row == 0 or row == width-1:
                newB[ROW][col] = 0
            elif col == 0 or col == height-1:
                newB[ROW][col] = 0
            elif state > 3 and oldB[ROW][col] == 1:
                newB[ROW][col] = 0
            elif state == 3:
                if oldB[ROW][col] == 0:
                    newB[ROW][col] = 1
            elif state < 2:
                newB[ROW][col] = 0
            elif state == 2:
                newB[ROW][col] = oldB[ROW][col]
                                       #this is the actual application of the
                                       #rules contained in Conway's Life.
                                       #If a cell is on the perimeter then leave
                                       #it empty.
                                       #If a cell has more than 3 neighbors it
                                       #'dies'
                                       #If it is 'dead' and has exactly 3
                                       #neighbors it comes to life.
                                       #If it has less than 2 neighbors, it dies
                                       #If it has exactly 2 neighbors it is 
                                       #unaltered.

def countNeighbors(B,row,col):
                                       #this function is called by updateNextLife()
                                       #to count how many neighbors each cell has
    neighbors = 0
                                       #holds the count for the number of neighbors
    width = len(B[0])
    height = len(B)
    if row > 0 and col > 0:
        if row < height-1 and col < width-1:
            if B[row-1][col-1] == 1:
                neighbors += 1
            if B[row-1][col] == 1:
                neighbors += 1
            if B[row-1][col+1] == 1:
                neighbors += 1
            if B[row][col-1] == 1:
                neighbors += 1
            if B[row][col+1] == 1:
                neighbors += 1
            if B[row+1][col-1] == 1:
                neighbors += 1
            if B[row+1][col] == 1:
                neighbors += 1
            if B[row+1][col+1] == 1:
                neighbors += 1

            neighbors += B[row-1][col-1]
            neighbors += B[row-1][col]
            neighbors += B[row-1][col+1]
                                       #looks at each cell around the cell in
                                       #question and for each occupied cell
                                       #neighbors += 1
    return neighbors

 


def Life( width, height ):
                                       #will become John Conway's Game of Life..
                                       #This is the first version of the life()
                                       #function asked for in the assignment
    B = createBoard( width, height )
    updateRandom( B )
 
    while True:                      
                                       # run forever
        csplot.show(B)               
                                       # show current B
        time.sleep(0.25)              
                                       # pause a bit
        oldB = B       
                                       #  just a reminder for us humans
        B = createBoard(width, height)   
                                       #  creates a new board
        updateReversed( oldB, B )  
                                       #  sets the new board correctly
        
def LIfe( width, height ):
                                       #will become John Conway's Game of Life..
                                       #this is the second version of the life()
                                       #function asked for in the assignment
    B = createBoard( width, height )
    csplot.showAndClickInIdle(B)
    count = 0
                                       #ensures count is set properly 
    while True:                      
                                       # run forever
        while count <=15:
                                       #actually just run for awhile....
            csplot.show(B)               
                                       
                                       # show current B
            time.sleep(0.25)              
                                       # pause a bit
            oldB = B       
                                       #  just a reminder for us humans
            B = createBoard(width, height)   
                                       #creates a new board
            updateReversed( oldB, B )  #  sets the new board correctly
            count += 1
        break

        
def life( width, height ):
                                       #will become John Conway's Game of Life..
                                       #this is the final version of the life()
                                       #function assigned
    B = createBoard( width, height )
    csplot.showAndClickInIdle(B)
                                       #set the initial state of the board
    pause = False
    while True: 
                                       # run forever
        csplot.show(B)               
                                       # show current B
        time.sleep(0.25)              
                                       # pause a bit
        keys = csplot.getKeysDown()
                                       #checks for user input
        if 'p' in keys:
            pause = True
                                       #'p' is for pause!
        if pause == False:
            oldB = B
            B = createBoard(width, height)
            updateNextLife( oldB, B )
                                       #if we are not pausing then keep updating
        if 'r' in keys:
            pause = False
                                       #'r' is for resume!
        if 'q' in keys:
            break
                                       #'q' is for quit!
        if '1' in keys:
            oldB = B
            B = createBoard(width, height)
            updateNextLife(oldB, B)
            csplot.show(B)
            pause = True
                                       #'1' will advance a single generation and
                                       #pause. pressing '1' will run an 
                                       #additional generation, 'q' will quit and
                                       #'r' will resume normal functioning