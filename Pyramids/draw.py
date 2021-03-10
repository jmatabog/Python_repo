

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    shape = input("Shape?: ").lower()
    if shape == 'pyramid' or shape == 'square' or shape == 'triangle' or shape == 'diamond':
        return shape
    else:
        return get_shape()


# TODO: Step 1 - get height (it must be int!)
def get_height():
    i = input("Height?: ")
    try:
        if int(i) <= 80:
            return int(i)
    except ValueError:
        return get_height()

# TODO: Step 2
def draw_pyramid(height, outline):
    if outline == False:
        for i in range(height):
            if i == 0:
                print(" " * (height-i-1)+ "*",end="")
            elif i == height-1:
                print("*" * (height*2-1),end="")
            else :
                print(" " * (height-i-1)+ "*" + "*" * (i*2-1) + "*",end="")
            print()

    else:
        for i in range(height):
            if i == 0:
                print(" " * (height-i-1)+ "*",end="")
            elif i == height-1:
                print("*" * (height*2-1),end="")
            else :
                print(" " * (height-i-1)+ "*" + " " * (i*2-1) + "*",end="")
            print()


# TODO: Step 3
def draw_square(height, outline):
    if outline == False:
        i = 1
        for i in range(height):
            for o in range(height):
                if o == 0 or  i == 0:
                    print("*",end="")
                else:
                    print("*",end="")
            print()

    else:
        for i in range(height):
            for j in range(height):
                if j == 0 or i == 0 or j == (height-1) or i ==(height-1):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()


# TODO: Step 4
def draw_triangle(height, outline):
    if outline == False:
        i = 1
        while i <= height:
            print("*" * i)
            i += 1

    else:
        i = 1
        while i <= height:
            if i == 1 or i == height:
                print("*" * i)
                i += 1
            else:
                print("*" + " " * (i - 2) + "*")
                i +=  1
                
def draw_diamond(height, outline):
    x = 0
    y = 1
    j = -1
    while outline == False and x in range(height):
        if x < 1:
            print(" " * (height - 1) + "*")
        if x == 1 or x > 1 and x < (height - 1):
            print(" " * (height - y) + "*" * (y + x))
        if x == (height - 1):
            print ("*" * (y + x))
        x +=1
        y +=1
        a = x - 1
        b = y
    while outline == False and a in range(height):
        if a == 1 or a > 1 and a < (height - 1):
            print (" " * (height - b + 1) + "*" * (b + a -1))
        if a < 1:
            print(" " * (height - 1) + "*")
        a -=1
        b -=1
#---Outline--diamond----
    while outline == True and x in range(height):
        if x < 1:
            print(" " * (height - 1) + "*")
        if x == 1 or x > 1 and x < (height - 1):
            print(" " * (height - y) + "*" + " " * (x + j) + "*")
        x +=1
        y +=1
        j +=1
        a = x - 1
        b = y
    while outline == True and a in range(height):
        if a == 1 or a > 1 and a < (height - 1):
            print(" " * (height - b) + "*" + " " * (a + b - 1) + "*")
        if a < 1:
            print(" " * (height - 1) + "*")
        a -=1
        b -=1

# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if shape == 'pyramid':
        draw_pyramid(height,outline)
    elif shape == 'square':
        draw_square(height,outline)
    elif shape == 'triangle':
        draw_triangle(height,outline)
    elif shape == 'diamond':
        draw_diamond(height,outline)

# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    o = input('Outline only? (y/n): ')
    if o == 'y' or o == 'Y':
        return True
    elif o == 'n' or o == 'N':
        return False
    else:
        return get_outline()


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

