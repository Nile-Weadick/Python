"""
The second program, randomread.py, is to read a set of 
random numbers from a file, 
counts how many were read, displays the random numbers, 
and displays the total count of random numbers.
"""

def main():
    # Open the file for reading.
    try:
        numFile = open('numFile.txt', 'r')
    except IOError:
        print("Could not open file")
        return

    # Initialize an accumulator to 0.0
    total = 0

    # Initialize a variable to keep count of the videos.
    count = 0

    print('Here are the random numbers generated')

    # Get the numbers from the file and total them.
    for line in numFile: 
        # Convert a line to a int
        num = int(line)

        # Add 1 to the count variable.
        count += 1

        # Display the time.
        print(count, ":", num)

        # Add the time to total.
        total += num #logic error

    # Close the file
    numFile.close()

    # Display the total
    print('The total is', total)

main()