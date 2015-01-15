#David Parrott
#CS 121
#Homework 9

class Board:

    def __init__( self, width, height ): 
        self.width = width
        self.height = height 
        self.data = []
        if self.width > 9:
            self.width = self.width % 9
                           # this will be the board
        for row in range( self.height ): 
            boardRow = []
            for col in range( self.width ): 
                boardRow += [' ']
            self.data += [boardRow]
        
    def __repr__(self):
        s = '' 
                           #the string to return 
        for row in range( self.height ): 
            s += '|'	
                           # add the spacer character 
            for col in range( self.width ):
                s += self.data[row][col] + '|' 
            s += '\n'
        else:
                           #if the board is not oversized
            sepLength = self.width
                           #scale the separator to the width of the board
                           
        separator = '--'*self.width+'-'
                           #generate the separator
        indicesLength = sepLength
                           #used to generate indices at the bottom of the board
        indices = ''
        for i in range(indicesLength):
            indices += ' '+str(i)
                           #populates the variable indices with a space and
                           #number that will correspond to the collumn immediately
                           #above it on the other side of the separator
        s = s+separator+'\n'+indices        
        return s	
                           # return it
    
    
    def setBoard(self, moveString):
                           #setBoard() is a function used to configure a preset
                           #board. This is used in debugging. moveString is 
                           #an input of the string type that represents a 
                           #sequence of collumns to place alternating checkers
                           #in. Essentially this function plays through the
                           #opening moves of a game automatically to let you
                           #test certain game functionalities.
        nextCh='X'
                           #nextCh sets the begining checker type to 'X'
        for colString in moveString:
                           #for every character in the moveString
            col = int(colString)
                           #convert each character to an int type
            if 0 <= col <= self.width:
                           #if col is a valid move on the board
                self.addMove(col,nextCh)
                           #call the addMove() function to place a checker
            if nextCh == 'X':
                nextCh = 'O'
                           #alternates checker types
            else:
                nextCh = 'X'
                
    def addMove(self, col, ox ):
                           #addMove() is a function to change the board data.
                           #it first calls allowsMove() to make certain the
                           #selected move is valid and, if so, it places a new
                           #checker
        if self.allowsMove(col):
                           #checks for a valid move
            for row in range( self.height ):
                if self.data[row][col] != ' ':
                    self.data[row-1][col] = ox
                           #if the row has an empty space, place the checker
                    return
            self.data[self.height-1][col] = ox
        return
        
    def allowsMove(self, col):
                           #allowsMove() is a function that checks for validity
                           #of a specified move.
        if 0 <= col < self.width: 
                           #if the move is on the board created
            return self.data[0][col] == ' ' 
                           #tell whatever called allowsMove() that you can move
        else:
            return False
                           #otherwise return move as invalid
        
    def delMove(self, col, ox ):
                           #delMove() removes the last checker placed.
        if self.allowsMove(col):
                           #checks for a valid move
            for row in range( self.height ):
                if self.data[row][col] == ox:
                    self.data[row][col] = ' '
                           #if the top checker in the row selected matches the 
                           #type of the checker selected, replace it with an
                           #empty space.
                    return
            self.data[self.height][col] = ' '

    def winsForHorizontal(self, ox):
        # check for horizontal wins
        for row in range(0,self.height):
            for col in range(0,self.width-3):
                           #we must limit the "width" we check for because of 
                           #method used to check. Skipping this step would
                           #return errors as python tried to check data that
                           #does not exist
                if self.data[row][col] == ox and \
                   self.data[row][col] != ' ' and \
                   self.data[row][col+1] == ox and \
                   self.data[row][col+2] == ox and \
                   self.data[row][col+3] == ox:
                           #if four in a row
                    return True
                           #True == WINNER!
        
    def winsForVertical(self, ox):
        # check for vertical wins
        for row in range(0,self.height-3):
                           #as with the winsForHorizontal() function we must
                           #limit a dimension of the board beacuse of the method
                           #used to check the data.
            for col in range(0,self.width):
                if self.data[row][col] == ox and \
                    self.data[row+1][col] == ox and \
                    self.data[row+2][col] == ox and \
                    self.data[row+3][col] == ox:
                           #if four in a row
                    return True
                           #True == WINNER!

    def winsForDiagonal(self, ox):
        # check for diagonal wins
        for row in range(0,self.height):
            for col in range(0,self.width-3):
                           #only the "width" must be limited here
                if self.data[row][col] == ox and \
                   self.data[row-1][col+1] == ox and \
                   self.data[row-2][col+2] == ox and \
                   self.data[row-3][col+3] == ox:
                    return True
        for row in range(0,self.height-3):
            for col in range(0,self.width-3):
                           #both "height" and "width" must be limited
                if self.data[row][col] == ox and \
                   self.data[row+1][col+1] == ox and \
                   self.data[row+2][col+2] == ox and \
                   self.data[row+3][col+3] == ox:
                    return True

    def winning(self):
                           #winning() is a helper function that calls each of
                           #the function designed to check for the various win
                           #combinations
        if self.winsForHorizontal('X') == True:
            print "X is the winner!"
            return True
        if self.winsForVertical('X') == True:
            print "X is the winner!"
            return True
        if self.winsForDiagonal('X') == True:
            print "X is the winner!"
            return True
        if self.winsForHorizontal('O') == True:
            print "O is the winner!"
            return True
        if self.winsForVertical('O') == True:
            print "O is the winner!"
            return True
        if self.winsForDiagonal('O') == True:
            print "O is the winner!"
            return True
        else:
            return False
        
    def isFull(self):
                           #isFull() checks for a full board
        fullness = 0
                           #this is a variable used to track the number of full
                           #collumns
        for col in range(self.width):
            if self.allowsMove(col) == False:
                fullness +=1
                           #calls allowsMove() to see if a row is full. If it is
                           #the tracking variable fullness is increased by one
        if fullness == self.width:
                           #if every collumn is full
            return True
                           #return True
        else:
            return False

    def hostGame(self):
                           #hostGame() is the framework for playing a game of
                           #connect 4. 
        nextCh = 'X'
        winner = False
                           #Sets the first player as 'X' and creates the winner
                           #variable to track if one of the players wins.
        while winner == False:
                           #while there is no winner yet
            print self
                           #print the board
            move = raw_input('It is '+nextCh+'s turn! :')
                           #asks for a move as raw_input assuming that the data
                           #entered will be a number
            col = int(move)
                           #converts the input in to an int type to simplify
            while col > self.width-1:
                           #if the move is outside of the board's dimensions
                move = raw_input('That is not a valid move! :')
                col = int(move)
                           #request a new move
            self.addMove(col,nextCh)
                           #add the requested move
            winner = self.winning()
                           #checks for a winner
            if self.isFull() == True:
                           #checks is the board is full
                print "The game resulted in a stalemate!"
                break
            
            if nextCh == 'X':
                nextCh = 'O'
            else:
                nextCh = 'X'
                           #alternates checker types
        print self
                           #displays the board

b= Board(6,7)
                           #preset for a standard board size