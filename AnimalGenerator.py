""""
The value of mood is to be set randomly. Generate a random number between 1 and 3. Then:

If the number is 1, the mood attribute is to be set to a value of happy.
If the number is 2, the mood attribute is to be set to a value of hungry.
If the number is 3, the mood attribute is to be set to a value of sleepy.

get_animal_type should return the value of the animal_type field.

get_name should return the value of the name field.

check_mood should return the value of the mood field.

Animal Generator Program
Once you have created the Animal class, create another Python file called animalGenerator.py. This program is to use Animal.py as a module.

In animalGenerator.py, prompt the user to enter the name and type of an animal. Create a new Animal object instance to store this data. 
Then, ask the user if they would like to repeat the process. They should be able to create as many Animal object instances as they would like.

After the user is done creating animals, the program is to use the object’s accessor methods (get_animal_type, get_name, and check_mood) 
to retrieve the name, type, and mood of each animal. This information is to be formatted and displayed as shown in the sample program output below.
"""

from Animal import Animal #import Animal Class from Animal.py
import random #import for randm int generator
list = []
choice = 'y'
while(choice == "y"):
    #get user input
    s = input("What type of animal would you like to create? ")
    n = input("What is the animal’s name? ")
    #great rand int
    m = random.randint(1,3)

    #determine mood from rand int
    if(m == 1):
        m = "Happy"
    elif(m == 2):
        m = "Hungry"
    else: 
        m = "Sleepy"

    #create Animal object
    myAnimal = Animal()

    # set variables to object attributes
    myAnimal.set_spec(s)    
    myAnimal.set_name(n)
    myAnimal.set_mood(m)

    #print(myAnimal.get_name(),"the",myAnimal.get_spec(),"is",myAnimal.get_mood())

    myString = myAnimal.get_name(), "the", myAnimal.get_spec(),"is", myAnimal.get_mood()
    list.append(myString)

    # get user input if more animals are to be created
    choice = input("Would you like to add more animals (y/n)?")

#iterate through list and print elements
for i in list:
    print(*i, sep= " ")#seperate list string by spaces instead of commas and remove brackets