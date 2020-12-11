#method that returns the cost of each seat psotion on plane
def get_cost_matrix():
    cost_matrix = [[500, 200, 500, 200, 500] for row in range(10)]
    return cost_matrix

def main():
    #Attempt to open reserved steas file and nootify user if fails
    try:
        seatsFile = open('reservations.txt', 'r+')
    except IOError:
        print("Could not open file")
        return

    # create 2d array of all seats on plane and assing them to empty
    seatsRows = 10
    seatsColums = 5
    seatsArray = [['O' for i in range(seatsColums)] for j in range(seatsRows)]

    #Determone what seats are iniatailly rserved using .txt file and assigned thos seats as reserved
    for line in seatsFile:
        data = line.split(",")
        row = int(data[1])
        seat = int(data[2])
        seatsArray[row][seat] = 'X'

    #delcare total cost and cost of each seat
    total = 0
    cost = get_cost_matrix()

    # detremine total cost of all reserved seats
    for i in range(seatsRows):
        for j in range(seatsColums):
            if seatsArray[i][j] == 'X':
                tempCost = int(cost[i][j])
                total += tempCost

    #print main menu and get user choice
    print("----------------------------------")
    print("1040 Airways Reservation System")
    print("----------------------------------")
    print("1. Admin Log-In")
    print("2. Reserve a seat")
    print("3. Exit")
    print("----------------------------------")
    choice = int(input("Choose an option: "))

    #only allow user to choose the 3 options to proceed
    while choice != 1 and choice != 2 and choice != 3:
        print("ERROR: Invalid Option! Select 1 or 2 or 3")
        print("----------------------------------")
        print("1040 Airways Reservation System")
        print("----------------------------------")
        print("1. Admin Log-In")
        print("2. Reserve a seat")
        print("3. Exit")
        print("----------------------------------")
        choice = int(input("Choose an option: "))

    #if user choose 1 go into admin login
    if choice == 1:
        print("----------------------------------")
        print("Admin Login")
        print("----------------------------------")
        #prompt user to enter username and password
        username = input("Enter Username:")
        password = input("Enter Password:")

        #open .txt file ocnating all valid usernames and passswords
        passwordFile = open('passcodes.txt', 'r')

        #create two empty list for username and password
        usernameList = []
        passwordList = []

        #split each line in passcodes file and append username and password to list
        for line in passwordFile:
            passwordData = line.split(", ")

            usernameList.append(passwordData[0])
            passwordList.append(passwordData[1].replace('\n', ''))
        
        #test each inputted username if machtes usersname in list
        for i in usernameList:
            if username == i:
                username = True

        #test each inputted password if machtes password in list
        for i in passwordList:
            if password == i:
                password = True

        # force useer to continoue to renter creds if they do not match whats in username and password list
        while username != True and password != True:
            print("Invalid username/password combination")
            print("----------------------------------")
            print("Admin Login")
            print("----------------------------------")
            username = input("Enter Username:")
            password = input("Enter Password:")

            #test creds again
            for i in usernameList:
                if username == i:
                    username = True

            for i in passwordList:
                if password == i:
                    password = True
        
        #if username and password are valid print the flight map and display total sales
        print("Printing the Flight Map...")
        for row in seatsArray:
                print(row)
        print("Total Sales:", total)

    #if user enters 2 display reveration menu
    if choice == 2:

        print("----------------------------------")
        print("Make a Reservation")
        print("----------------------------------")

        #prommpt user to enter frits and last name
        first = input("Enter First Name: ")
        last = input("Enter Last Name: ")

        #create a ticket using first and last name
        ticket = ""
        for letter in range(len(first)):
            ticket += first[letter] + last[letter]

        ticket += "1040"

        #prompt user to enter seat and row they want
        seatRow = input("Which seat row do you want?")
        seatColumn = input("Which seat column do you want?")

        #if seat and row and already reserved the user must re enter seat and row
        while seatsArray[int(seatRow)][int(seatColumn)] != 'O':
            print("Row:", seatRow, "Seat:", seatColumn, "is already assigned. Choose again.")
            seatRow = input("Which seat row do you want?")
            seatColumn = input("Which seat column do you want?")

        #if the user desired seat is avaialable then notify the user
        print("Your requested seat, Row:", seatRow, " Seat:", seatColumn, "has been assigned.")

        #write the user info to file so it can be used for update flight map 
        data = "%s, %s, %s, %s" % (first,seatRow,seatColumn,ticket)
        seatsFile.write(data)

        #file is closed and re opened so that the new data can be read while program is running
        seatsFile.close()
        seatsFile = open('reservations.txt', 'r')

        #Determone what seats are iniatailly rserved using .txt file and assigned thos seats as reserved
        for line in seatsFile:
            data = line.split(",")
            row = int(data[1])
            seat = int(data[2])
            seatsArray[row][seat] = 'X'

        #print updated flight map with user seat reserved
        print("Printing the Flight Map...")
        for row in seatsArray:
            print(row)

        #print the users ticket num
        print("Your e-ticket number is:", ticket)

    #close open files
    seatsFile.close()

    #if the user enters 3 tell them god buy and return program
    if choice == 3:
        print("Thank you for choosing 1040 Airways! Goodbye")

#call main method
main()