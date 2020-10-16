"""
Description: Create a program called numstat.py that reads a series of integer numbers from a file and determines and displays the name of file, sum of numbers, count of numbers, average of numbers, maximum value, minimum value, and range of values.

Purpose: The purpose of this challenge is to provide experience working with numerical data in a file and generating summary information.

Requirements:

Create a program called numstat.py that reads a series of integer numbers from a file and determines and displays the following:

Name of the file.
Sum of the numbers.
Count of how many numbers are in the file.
Average of the numbers. The average is the sum of the numbers divided by how many there are.
Maximum value.
Minimum value.
Range of the values. The range is the maximum value minus the minimum value.
The program is to prompt the user for the name of the file that contains the numbers. If an exception occurs trying to open or read the file an error message is to be displayed. The program is not to crash if the file is not found or there is an error reading the file. Use try-except!

The output from the program is to display the information described above using the following strings preceding the values. There is to be a space between the colon and the value.
[5:20 PM]
File name:
Sum:
Count:
Average:
Maximum:
Minimum:
Range:

At the end of one attempt at reading, or a successful read, of a file the user it to be asked if they would like to evaluate another file of numbers. Use the prompt: Would you like to evaluate another file? (y/n) If the user answers y, then the program is to accept input for another file name. If the user answers with anything other than y, the program is to exit.

Testing
Resource: numbers.txt.zip (Links to an external site.)

Once you have written your program, you need to test it. A sample file called numbers.txt containing a list of integers is provided for testing. The file numbers.txt is contained in a file provided above called numbers.txt.zip. You must unzip numbers.txt.zip to get the numbers.txt file. You can also hand create files or use the random number writer from the earlier challenge to create files for testing.

The numbers.txt file, or any other test file containing numbers, needs to be in the same directory as the python program for it to be found.

For the provided numbers.txt file the following are the values your program should generate:

Sum: 56110
Count: 100
Average: 561.1
Maximum: 995
Minimum: 8
Range: 987

"""

def main():

        # Open the file for reading.
    fileName = 'numbers.txt'
    try:
        numFile = open(fileName, 'r')
        
    except IOError: #if file not found or no opened notify user
        print("Could not open file")
        return

    # declare and initinaize variables
    line = numFile.readline()
    sum = int(line)
    count = 1
    max = sum
    min = sum

    #loop though lines of .txt and calc variables
    for line in numFile:
        current = int(line)
        sum += current
        count = count + 1
        avg = sum / count

        #test for maxi int
        if(current > max):
            max = current

        #test for min int
        if(current < min):
            min = current

        range = max - min #find range

    numFile.close()#close open file

    #print results to the user
    print("File name:", fileName)
    print("Sum:", sum)
    print("Count:", count)
    print("Average:",avg)
    print("Max:", max)
    print("Min", min)
    print("Range:",range)

main()#call main function and exucute