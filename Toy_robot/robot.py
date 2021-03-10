

# TODO: Decompose into functions

#Description of how a square of size 10 should be
def move_square():
    size = 10
    print("Moving in a square of size "+str(size))
    for i in range(4):
        degrees = 90
        print("* Move Forward "+str(size))
        print("* Turn Right "+str(degrees)+" degrees")

#Description of a rectangle of length 20 & width 10
def move_rectangle():
    length = 20
    width = 10
    print("Moving in a rectangle of "+str(length)+" by "+str(width))
    for i in range(2):
        degrees = 90
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")
        print("* Move Forward "+str(width))
        print("* Turn Right "+str(degrees)+" degrees")

#Description of how you draw a circle 
def move_circle():
    print("Moving in a circle")
    degrees = 1
    for i in range(360):
        length = 1
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")

#Description of 3 square's of size 20
def dancing_square():
    size = 20
    degrees = 90
    print("Square dancing - 3 squares of size 20")
    for i in range(3):
        length = 20
        print("* Move Forward "+str(length))
        print("Moving in a square of size 20")
        for j in range(4):
            print("* Move Forward " + str(size))
            print("* Turn Right " + str(degrees) + " degrees")     

#Description of a 4 circle's of the same size
def cropping_circles():
    degrees = 1
    print("Crop circles - 4 circles")
    for i in range(4):
        length = 20
        print("* Move Forward "+str(length))
        print("Moving in a circle")
        for k in range(360):
            length = 1
            print("* Move Forward " + str(length))
            print("* Turn Right " + str(degrees) + " degrees")

#def control- Because this is where you control/call your functions
def move():
    move_square()
    move_rectangle()
    move_circle()
    dancing_square()
    cropping_circles()


def robot_start():
    move()


if __name__ == "__main__":
    robot_start()
