import random

obs_list = []
# random.randint = lambda x,y : 1

def get_obstacles():
    """
    -generating random obstacles from 1 to 10 

    """
    global obs_list

    no_of_obs = random.randint(1,10)
    for i in range(no_of_obs):
        x_cord = random.randint(-100,100)
        y_cord = random.randint(-200,200)
        if x_cord == 0 and y_cord == 0:
            pass
        else:
            obs_list.append((x_cord, y_cord))

    return obs_list


def is_position_blocked(x,y):
    """
    checking the position of robot that it will land in the obstacles
    """
    for i in obs_list:
        if x in range(i[0],i[0]+5) and y in range(i[1],i[1]+5):
            return True
    return False


def is_path_blocked(x1,y1,x2,y2):
    """
    checking the path of the robot whether there is obstacles
    """
    if x1 == x2 and y2 > y1:
        for i in range(y1,y2+1):
            if is_position_blocked(x1,i) is True:
                return True
            continue
    elif x1 == x2 and y2 < y1:
        for i in range(y2,y1+1):
            if is_position_blocked(x1,i) is True:
                return True
            continue
    elif y1 == y2 and x2 > x1:
        for i in range(x1,x2+1):
            if is_position_blocked(i,y1):
                return True
            continue
    elif y1 == y2 and x2 < x1:
        for i in range(x2,x1+1):
            if is_position_blocked(i,y1):
                return True
            continue
    return False
   

def generate_obs():
    """
    calling of obstacles
    """

    return get_obstacles()


# if __name__ == "__main__":

#     print(get_obstacles())