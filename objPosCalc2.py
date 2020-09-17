
def main():

    bad_input = True

    #while bad_input is True the loop will continue to execute
    while bad_input:   
        try: 
            #ask user for input: 
            position = float(input("Enter the initial position "))
            velocity = float(input("Enter the initial velocity "))
            acceleration = float(input("Enter the acceleration "))
            time = float(input("Enter the time "))

            #if the user enters a negative number go back to the beginning of the loop
            if time < 0:
                print("Value for time must be 0 or greater.")
                print("Please enter input again\n")
                continue

            #calculate
            finalPosition = position + velocity * time + 0.5 * acceleration * time * time
            print("The final position is", finalPosition)

            #Set bad_input to False if all previous code in the try block executes successfully
            #Setting bad_input to False will cause the while loop to end
            bad_input = False
        except Exception as error:
            print("The following error occured:", error)
            print("Please enter input again\n")

#call main to begin the program
main()
userInput = input("Would you like to preform another calculation? (y/n) ")
while userInput == "y":
    main()
    userInput = input("Would you like to preform another calculation? (y/n) ")