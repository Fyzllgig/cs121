#David Parrott
#XXXX
#CS 121
#Assignment 7

#computing the Mandelbrot sequence and visualizing it in both Black and White
#and color versions as a bitmap named Mandelbrot.bmp 
#mset() produces the B&W image
#msetColor() produces a color image
#Helper functions are used to handle some of the computational work.
#inMSet() is called by mset() to test if a partiuclar value is within the 
#Mandelbrot set.
#inMSetColor() is called by msetColor() to test if a particular value is within
#the Mandelbrot set as well as compute information about how quickly a value is
#'escaping' the Mandelbrot set. This is then used to determine what color each
#pixel outside of the set should be.
#scale() is a helper function used by mset() and msetColor()
#to create a set of real x and y values for coordinates in the imaginary plane.


#if you changed the line
#if col % 10 == 0 and row % 10 == 0:
#to the line
#if col % 10 == 0 or row % 10 == 0:
#you would print a grid.


from bmp import *
#for image()

from math import *
#for abs()

iterations = 25
#used when calling inMSet() to determine the maximum number of iterations to
#run before assuming the number being checked is outside of the Mandelbrot set


def inMSet(c,n):
    #used to determine whether a particular value is contained within the 
    #Mandelbrot set where c is the number being checked and n is the number
    #of iterations to run before assuming the number is not in the Mandelbrot
    #set

    mand = 0
    #creates variable that will contain the complex value throughout the
    #iteration process
    
    countIterations = 0
    #keeps track of the number of iterations

    while abs(mand) <= 2  and countIterations < n:
        #keeps iterating as long as mand is not greater or equal to 2. This
        #is a common value used when checking for numbers contained within the
        #Mandelbrot set
        
        mand = mand**2 + c
        #adds the comple value c to the square of mand

        countIterations += 1
        #one more iteration

    if countIterations >= n:
        #returns true if we make it through the entire number of iterations
        return True
    
    else:
        #returns false if abs(mand) > 2 and we did not make it through the
        #number of iterations specified by iterations
        return False

def scale(pix, pixNum, floatMin, floatMax):
    #scale is a helper function used by mset() to creates a set of real x and y
    #values for coordinates in the imaginary plane. This will be used by mset
    #to test if a point should be plotted
    
    pix = float(pix)
    pixNum = float(pixNum)
    #changes to float type to avoid rounding errors
    
    imaginaryDiff = abs(floatMin - floatMax)
    #difference in maximum and minimum point values
    
    realRatio = pix/pixNum
    #where is pix in relation to pixNum?
    
    imaginaryMove = floatMin + (realRatio * imaginaryDiff)
    #where in the plane is the point we are checking?
    
    return imaginaryMove
    
def mset(width, coordinateList):
    #mset() takes a dimension and a set of coordinates from the user and creates
    #a bitmap of the specified region of the Mandelbrot Set. 
    
    xMin = coordinateList[0]
    xMax = coordinateList[1]
    yMin = coordinateList[2]
    yMax = coordinateList[3]
    #reads through the list of coordinates and breaks up the values for use
    #individually
    
    height = width *(abs(yMin-yMax)/abs(xMin-xMax))
    #calculates image height as a functino of width

    image = BitMap(width, height)
    #used to store data about the image during computation
    
    for col in range(width):
        for row in range(int(height)):
            if inMSet(scale(col, width, xMin, xMax) + scale(row, height, yMin, yMax)*1j, iterations) == True:
                image.plotPoint(col, row)
                #systematically checks each value within the region specified by
                #the users to see if it contained within the Mandelbrot Set and,
                #if so, plots a point for each value
                
    image.saveFile( "Mandelbrot.bmp" )
    #saves data contained within image as test.bmp

    
def inMSetColor(c,n):
    #a version of inMSet that also passes information about how quickly a value
    #is determined to be outside of the Mandelbrot Set
    
    mand = 0
    countIterations = 0
    
    while abs(mand) <= 2  and countIterations < n:
        mand = mand**2 + c
        countIterations += 1
        clr = 765 * countIterations / n
        #clr is used to pass data about how quickly the number is 'escaping'
        
    if countIterations >= n:
        L = [ True, 0]
        #L is a list that contains information about the state of the number
        #ie True = within the Mandelbrot Set. 0 is used to display that pixel
        #as black when creating the image and can be altered if other colors
        #are desired.
        
        return L
    else:
        px = 0
        if clr > 510:
            px = [255, 255, clr % 255]
        elif clr > 255:
            px = [255, clr % 255, 0]
        else:
            px = [clr % 255, 0, 0]
        #this passes information about both the state of the number as well as
        #data that will be used by msetColor() to determine what color the 
        #pixel that corresponds to the tested values should be, based on how
        #quickly the number is 'escaping' the Mandelbrot set. px[0] will be used
        #to compute the 'red' component. px[1] will be used to compute the
        #'green' component and px[2] will be used to compute the 'blue'
        #component

        L = [ False, px]
        return L

def msetColor(width, coordinateList):
    #a version of mset() that will accept additional data used to alter the
    #the color of pixels outside the Mandelbrot set.

    xMin = coordinateList[0]
    xMax = coordinateList[1]
    yMin = coordinateList[2]
    yMax = coordinateList[3]
    height = width *(abs(yMin-yMax)/abs(xMin-xMax))

    image = BitMap(width, height)
    
    for col in range(width):
        for row in range(int(height)):
            if inMSetColor(scale(col, width, xMin, xMax) + scale(row, height, yMin, yMax)*1j, iterations)[0] == True:
                image.setPenColor(Color.BLACK)
                image.plotPoint(col, row)
            else:
                pixelC = inMSetColor(scale(col, width, xMin, xMax) + scale(row, height, yMin, yMax)*1j, iterations)[1]
                pixR = pixelC[0]
                pixG = pixelC[1]
                pixB = pixelC[2]
                #unpacks the information passed by inMSetColor() that will 
                #determine the color of each pixel outside the Mandelbrot set
                
                pixel3C = Color(pixR, pixG, pixB)
                #assigns the values as components in an RGB color
                
                image.setPenColor(pixel3C)
                image.plotPoint(col, row)
    
    image.saveFile( "Mandelbrot.bmp" )