"""Random Number File Writer (randomwrite.py)
Create a program called randomwrite.py that writes a series of random integers to a file. 
The program is to request from the user how many random numbers to generate, the lower bound 
of the random numbers’ range, and the upper bound of the random numbers’ range. Each random 
integer value is to be on a separate line and is to be in the range of the inputted lower 
bound through the inputted upper bound. The file that the random numbers are written to is 
to be called randomnum.txt.
"""
from random import randint

def main():
    
    # Get quantity of random numbers to generate.
    numCount = int(input('How many random numbers do you want? ')) 
    while(numCount <= 0):
        print("The inputted number should be a positive integer.")
        numCount = int(input('How many random numbers do you want? ')) 

    # Get lower bound of the random numbers’ range.
    lowestNum = int(input('What is the lowest the random number should be? ')) 
    while(lowestNum <= 0):
        print("The inputted number should be a positive integer.")
        lowestNum = int(input('What is the lowest the random number should be? ')) 

    # Get upper bound of the random numbers’ range.
    largestNum = int(input('What is the highest the random number should be? ')) 
    while(largestNum <= 0):
        print("The inputted number should be a positive integer.")
        largestNum = int(input('What is the highest the random number should be?'))

    # Open the file
    numFile = open('numFile.txt', 'w')

    # Write Numbers to file
    for x in range(numCount):
        value = randint(lowestNum,largestNum)
        numFile.write(str(value) + '\n')

    print("Numbers have been writen to file") # Numbers have successfuly Witten
    numFile.close() # Close File

main()