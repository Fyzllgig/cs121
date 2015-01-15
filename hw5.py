#Assignmnet 5
#David Parrott
#28 September, 2011


#What data will your program need to keep track of?
#state of the board, possibly previous moves, if desirable. number of moves
#could be useful. user input
#What will your program need to do with the data?
#analyze board state VS user input. if previous moves are stored then knowing
#how to un-do would be useful. track number of moves.
#having a function that checks the state of each space on the board adjacent
#to the tile selected by the user would be useful. 
#

from csplot import * #so that 'show' is imported 
import time # provides time.sleep(0.5)
from random import * # provides choice( [0,1] ), etc.
import sys  # larger recursive stack
sys.setrecursionlimit(100000) # 100,000 deep
 
def runGenerations( L ):
    #runGenerations keeps running evolve...
    show(L)
    print L  # display the list, L
    time.sleep(0.5)   # pause a bit
    if allones(L): #checks if the list is all ones
        return 0
    newL = evolve( L )   # evolve L into newL
    return 1+runGenerations( newL )  # recurse and print number of generations


def evolve( L ):
    #evolve takes in a list of integers, L,
    #and returns a new list of integers
    #considered to be the "next generation"""
    N = len(L)  # N now holds the size of the list L
    return [ setNewElement( L, i ) for i in range(N) ]
 

def SetNewElement( L, i, x=0 ):
    #setNewElement returns the NEW list's ith element
    #input L: any list of integers
    #input i: the index of the new element to return
    #input x: an extra, optional input for future use
    return L[i] + 1 #adds 1 to the ith element of L

def SetNewElement( L, i, x=0 ):
    #setNewElement returns the NEW lists's ith element
    #input L: any list of integers
    #input i: the index of the new element to return
    #input x: an extra optional input for future use
    return L[i] * L[i] #squares the ith element of i

def SetNewElement( L, i, x=0 ):
    #setNewElement returns the NEW lists's ith element
    #input L: any list of integers
    #input i: the index of the new element to return
    #input x: an extra optional input for future use
    return L[i-1] #changes the order of L

def SetNewElement( L, i, x=0 ):
    #setNewElement returns the NEW lists's ith element
    #input L: any list of integers
    #input i: the index of the new element to return
    #input x: an extra optional input for future use
    return L[i-(len(L)-1)] #changes the order of L

def setNewElement( L, i, x=0 ):
    #setNewElement returns the NEW lists's ith element
    #input L: any list of integers
    #input i: the index of the new element to return
    #input x: an extra optional input for future use
    return choice( [0,1] ) #randomly returns a 1 or 0 for every i in L

def allones(L):
    #allones tests a NEW list after being processed by
    #setNewElement to test if all elements of the set
    #are now the number 1
    ones = [ e == 1 for e in L] #returns true if every element of L == 1
    return sum(ones) == len(L)

def evolve( L ):
    #evolve takes in a list of integers, L,
    #and returns a new list of integers
    #considered to be the "next generation"
    N = len(L)  # N now holds the size of the list L
    x = sqinput()  # Get mouse input from the user
    return [ setNewElement( L, i, x ) for i in range(N) ]
 
def setNewElement( L, i, x=0 ):
    #setNewElement returns the NEW list's ith element
    #input L: any list of integers
    #input i: the index of the new element to return
    #input x: an extra, optional input for future use
    if i == x:  # if it's the user's chosen column,
        return 1 - L[i] # toggles state of the tile selected
    if i == x + 1 and i <= len(L): # toggles state of tile to right
        return 1 - L[i]
    if i == x - 1 and i <= len(L): # toggles state of tile to left
        return 1 - L[i]
    else: 
        return L[i] # return the original
 
def randBL(N): 
    #used to randomize starting board
    seed = [choice([0,1]) for x in range(N)]
       #generates list of 1's and 0's
       #that is length N
    return seed

def runGenerations2D( L ):
    #runGenerations keeps running evolve...
    show(L)
    time.sleep(0.5)   # pause a bit
    if allones2D(L): #checks if the list is all ones
        print 'Victory!' #a little affirmation
        return 0
    newL = evolve2D( L )   # evolve L into newL
    return 1+runGenerations2D( newL )  # recurse

def evolve2D( L ): 
    # 2D version of evolve function
    N = len(L)  # N now holds the size of the list L
    x , y = sqinput2()  # Get mouse input from the user
    return [ [setNewElement2D( L, i, j, x, y ) for i in range(N) ] for j in range(N) ]

def randBL2D(N): 
    #calls initial randBL function to randomly populate the board
    seed = [randBL(N) for i in range(N)]
    return seed

def setNewElement2D( L, i, j, x=0, y=0 ):
    #setNewElement returns the NEW list's ith element
    #input L: any list of integers
    #input i: the index of the new element to return
    #input x: an extra, optional input for future use    
    if i == x and j == y:  #if it's the user's chosen column,
        return 1 - L[j][i] #toggles state of the tile selected
    elif i == x + 1 and j == y: #toggles state of tile to east
        return 1 - L[j][i]
    elif i == x - 1 and j == y: #toggles state of tile to west
        return 1 - L[j][i]
    elif i == x and j == y - 1: #toggles state of tile to north
        return 1 - L[j][i]
    elif i == x and j == y + 1: #toggles state of tile to south
        return 1 - L[j][i]
    else:
        return L[j][i] #return the original

def allones2D(L):
    #allones tests a NEW list after being processed by
    #setNewElement to test if all elements of the set
    #are now the number 1
    #ie have you won?
    ones = [ allones(e) == 1 for e in L] #returns True if every element of L == 1
    return sum(ones) == len(L)

def compEvolve2D( L ): 
    # 2D version of evolve function for computer play
    N = len(L)  # N now holds the size of the list L
    x = choice(range(N))
    y = choice(range(N)) 
    # randomly picks a tile
    return [ [setNewElement2D( L, i, j, x, y ) for i in range(N) ] for j in range(N) ]

def compRunGenerations2D( L ):
    #plays the game on auto-pilot
    show(L)
    time.sleep(0.5)   # pause a bit
    if allones2D(L): #checks if the list is all ones
        print 'Victory!' #a little affirmation
        return 0
    newL = compEvolve2D( L )   # evolve L into newL
    return 1+compRunGenerations2D( newL )  # recurse

runGenerations2D(randBL2D(3)) #sets the initial dimensions of the board
#compRunGenerations2D(randBL2D(3)) #sets up computer play