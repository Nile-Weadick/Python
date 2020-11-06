from document import Document #get Document class 

#init local variables
list = []
choice = 'y'

while(choice == "y"): #allow user to compute as much data as they like
    title = input("Enter Title:")
    body = input("Enter Body:")
    author = input('Enter Author:')

    myDocument = Document() # create a new document object

    myDocument._init_(title,body,author) #give new object data

    #print page
    page = "TITLE\n", "-------------\n", myDocument.get_title(), "\n", "BODY\n", "-------------\n", myDocument.get_body(), "\n", "AUTHOR\n", "-------------\n", myDocument.get_author()

    list.append(page)# add page to list

    choice = input("Would you like to add more documents (y/n)?")#ask user if they wan to compute more data

for i in list:
    print(*i, sep= " ")#seperate list string by spaces instead of commas and remove brackets