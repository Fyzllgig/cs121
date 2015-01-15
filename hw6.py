#Assignment 6
#David Parrott
#11239947
#submitted 10_19_2011

from math import *
from string import *
#import math for sqrt() function
#import string for lower() function

def encipher(S,n):
    #applies the Caesar cipher technique by calling rotate for every character
    #in the string S with a rotational value of n
    L = [rotate(i,n) for i in S] #applies rotate with rotational n
    return "".join(L) #prints the rotated characters

def rotate( let, num ):
    #shifts a character 'let' through the alphabet 'num' spaces
    if 'a' <= let <= 'z':
	#is let lowercase?
        return rotateL(let,num)
	#process let with lowercase shift function
	
    elif 'A' <= let <= 'Z':
	#is let uppercase?
        return rotateU(let,num)
	#process let with uppercase shift function
    
    else:
        return let
	#returns any non-letter characters unaltered
    
def rotateL(let,num):
    #function for lower case rotation
    neword = ord(let) + (num % 26)
	#shifts the character while accounting for large values in num
   
    if neword <= ord('z'): 
	#is the shifted character still in the lowercase alphabet?
        return chr(neword) 
    
    else:
	#'wraps' the shift around the alphabet

        modnew = ord(chr(neword))-ord('z')
        normalizedNum = modnew % 26
	#these lines adjust the shift so that we continue through the alphabet
	#after we ge to the end. modnew finds out how far past 'z' the shifted
	#character is and nomalizedNum turns that value in to how many spaces
	#in to the alphabet we need to go
	
        neword = ord('a') + normalizedNum-1
	#finalizes the adjusted shift

	#print normalizedNum
	#uncomment for testing
	#print neword
	#uncomment for testing
	
        return chr(neword)

def rotateU(let,num):
    neword = ord(let) + (num % 26)
	#shifts the character while accounting for large values in num
   
    if neword <= ord('Z'): 
	#is the shifted character still in the uppercase alphabet?
        return chr(neword) 

    else:
	#'wraps' the shift around the alphabet

        modnew = ord(chr(neword))-ord('Z')
        normalizedNum = modnew % 26
	#these lines adjust the shift so that we continue through the alphabet
	#after we ge to the end. modnew finds out how far past 'Z' the shifted
	#character is and nomalizedNum turns that value in to how many spaces
	#in to the alphabet we need to go
	
        neword = ord('A') + normalizedNum-1
	#finalizes the adjusted shift

	#print normalizedNum
	#uncomment for testing
	#print neword
	#uncomment for testing
	
        return chr(neword)

def decipher(S):
    #takes a string and attempts to guess what the most likely
    #original text was, assuming it was encrypted using the Caesar Cipher
    #decipher will compute all 26 possible combinations and test each of them
    #to compute a likely guess.
    #the tests are defined individually as letProb, vowelCount and qu.
    #totalProb calls them each as well as performing an additional test to
    #check if each word in the computed string has a vowel in it.
    #totalProb takes information from the various tests and uses that to
    #copmute a score for each string sent to it by decipher.
    #decipher keeps each computed string and the score computed for it in 
    #separate lists which it then zips together before checking which pair
    #has the highest score and returning that guess to the user.
    
    L = [encipher(S,i) for i in range(1,26)]
    #creates a list of all the possible Caesar permutations, excluding the
    #originally entered string
    #print L 
    #print statement used for testing

    LL = [totalProb(i) for i in L]
    #calls totalProb to create a list of the possible numeric probabilities
    #for each combination computed in L
    #print LL
    #print statement used for testing

    LLL = zip(LL,L)
    #combines the strings with their numerical probabilities
    #print LLL
    #print statement used for testing

    print "Your original message and the probable value assigned to it was ", max(LLL)
    print "......probably"
    
def vowelCount(S):
    #counts the number of vowels in a string
    #while the input should not be more than a single character for the
    #purposes of this assignment it seemed like a good idea to build the helper
    #function with the ability to handle strings of any size
    
    count = 0
    #creates tracking variable
    
    for v in S:
        #print v
        if v in "aeiouAEIOU":
	    #is the letter a vowel?
            count += 1
    return count #return 0 if not a vowel

    
def qu(S):
#checks if q's are followed by u's

    noQ = 0
    #creates variable for tracking

    S = lower(S)
    #changes to all lowercase to simplify testing for qu combination

    for i in range(len(S)-1):
	if S[i] == 'q' and S[i+1] != 'u':
	    noQ += 1 
    #if u does not follow q then tracking variable increase
	    
    if S[len(S)-1] == 'q':
	noQ += 1
    #if q is at the end of the string tracking variable increase
    
    if noQ > 0:
	return False
    #return False if an q's without u's
    
    else:
	return True
    #return True if all q's have u's
    
def totalProb(S):
    #copmutes a numerical value to use when guessing the original message

    prob = 1.0
    #creates prob variable
    
    for i in S:
	prob = prob * letProb(i)
    #increases the prob variable by the value passed from the letProb function
	
    if ('q' in S or 'Q' in S) and not qu(S):
	prob = prob - sqrt(2)
    #decreases prob if qu returns False
    
    vow = vowelCount(S)
    #computes total number of vowels
    
    placer = True
    #creates a boolean to be used in testing that each word has at least
    #one vowel

    pieces = S.split()
    #splits user string in to pieces to test for vowels in each word

    for i in pieces:
	if vowelCount(i) >= 1:
	    placer = True
	    #preserves the True value so long as there is at least one vowel
	    #in each element in pieces
	else:
	    placer = False
	    #passes a False value if any element of pieces does not contain
	    #at least one vowel
    
    probTracker = prob + sqrt(vow)
    #creates agregate probablity value
    
    if placer == False:
	probTracker = probTracker - 1
	#decreases the likelihood that a string that has words containing no
	#vowels will be selected by decreasing the weight of that particular
	#computed strings probability
    
    return probTracker #sends the computed agregate probability


# table of probabilities for each letter...
def letProb( c ):
    #if c is the space character or an alphabetic 
    #character,
    #we return its monogram probability (for english),
    #otherwise we return 1.0 We ignore capitalization.
    #Adapted from
    #http://www.cs.chalmers.se/Cs/Grundutb/Kurser/krypto/en
    #_stat.html
    
    if c == ' ': return 0.1904
    if c == 'e' or c == 'E': return 0.1017
    if c == 't' or c == 'T': return 0.0737
    if c == 'a' or c == 'A': return 0.0661
    if c == 'o' or c == 'O': return 0.0610
    if c == 'i' or c == 'I': return 0.0562
    if c == 'n' or c == 'N': return 0.0557
    if c == 'h' or c == 'H': return 0.0542
    if c == 's' or c == 'S': return 0.0508
    if c == 'r' or c == 'R': return 0.0458
    if c == 'd' or c == 'D': return 0.0369
    if c == 'l' or c == 'L': return 0.0325
    if c == 'u' or c == 'U': return 0.0228
    if c == 'm' or c == 'M': return 0.0205
    if c == 'c' or c == 'C': return 0.0192
    if c == 'w' or c == 'W': return 0.0190
    if c == 'f' or c == 'F': return 0.0175
    if c == 'y' or c == 'Y': return 0.0165
    if c == 'g' or c == 'G': return 0.0161
    if c == 'p' or c == 'P': return 0.0131
    if c == 'b' or c == 'B': return 0.0115
    if c == 'v' or c == 'V': return 0.0088
    if c == 'k' or c == 'K': return 0.0066
    if c == 'x' or c == 'X': return 0.0014
    if c == 'j' or c == 'J': return 0.0008
    if c == 'q' or c == 'Q': return 0.0008
    if c == 'z' or c == 'Z': return 0.0005
    return 1