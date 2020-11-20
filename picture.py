import turtle 
t = turtle.Pen() #create turlte object
t.speed(100) #set objetc write speed

def shape(sides,length): # create a shape method so we can use recursion
    #create shape
    for i in range(0, sides):
        t.forward(length)
        t.left(360/sides)
    #move turtle
    t.forward(3)
    t.left(5)
    if(length<1):
        return false #stop when becomes negative
    shape(sides, length - 2) #call method for recursion

#call shape method
shape(5,123)