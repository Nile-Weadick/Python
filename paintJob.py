'''
A painting company has determined that for every 350 square feet of wall space, 
one gallon of paint and six hours of labor are required.  
The company charges $62.25 per hour for labor. 
Write a program called paintjobestimator.py that asks the user to enter the square feet 
of wall space to be painted and the price of the paint per gallon. 
The program is to display the following information.

The number of gallons of paint required rounded up to whole gallons.
The hours of labor required.
The cost of the paint based on the rounded up whole gallons.
The labor charges.
The total cost of the paint job.

At the end of one estimate the user it to be asked if they would like to perform another estimate. 
Use the prompt: Would you like to do another estimate? (y/n) 
If the user answers y, then the program is to accept input for another estimate.
If the user answers with anything other than y, the program is to exit.
'''

def main():

    bad_input = True

    #while bad_input is True the loop will continue to execute
    while bad_input:   
        try: 
            #ask user for input: 
            squareFeet = float(input("Enter the square feet of wall space to be painted:"))

            #if the user enters a negative number go back to the beginning of the loop
            while squareFeet <= 0:
                print("Square feet must greater than 0")
                print("Please enter input again\n")
                squareFeet = float(input("Enter the square feet of wall space to be painted:"))
            
            #ask user for input:
            gallonPrice = float(input("Enter price per gallon of paint: "))

            #if the user enters a negative number go back to the beginning of the loop
            while gallonPrice <= 0:
                print("Value for time must be 0 or greater.")
                print("Please enter input again\n")
                gallonPrice = float(input("Enter price per gallon of paint: "))
                
            #calculate
            gallons = squareFeet / 350

            if((gallons) > int(round(gallons, 2))):

                gallons = int(round(gallons, 2)) + 1

            else:
                gallons = int(round(gallons, 2))

            laborHours = squareFeet / 58.33
            costOfPaint = squareFeet / 350 * gallonPrice
            laborCharges = laborHours * 62.25
            totalCost = (laborHours * 62.25) + (gallons * gallonPrice)

            #print 
            print("Gallons required:", gallons)
            print("Labor hours required:", round(laborHours,1))
            print("Cost of paint:$", round(costOfPaint,2))
            print("Labor charges:$", round(laborCharges,2))
            print("Total Cost:$", round(totalCost, 2))

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