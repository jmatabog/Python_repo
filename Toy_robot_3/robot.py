"""
TODO: You can either work from this skeleton, or you can build on your solution for Toy Robot 2 exercise.
"""
history = []
locate = True

# list of valid command names
valid_commands = ['off', 'help', 'forward', 'back', 'right', 'left', 'sprint', 'replay', 'silent', 'reversed', 'reversed silent']

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100


def get_robot_name():
    """
    prompts the user to name the robot then converts the name to uppercase.
    """

    name = input("What do you want to name your robot? ").upper()
    while len(name) == 0:
        name = input("What do you want to name your robot? ")
    return name


def get_command(robot_name):
    """
    Asks the user for a command, and validate it as well
    Only return a valid command
    """

    prompt = ''+robot_name+': What must I do next? '
    command = input(prompt)
    while len(command) == 0 or not valid_command(command):
        output(robot_name, "Sorry, I did not understand '"+command+"'.")
        command = input(prompt)

    return command.lower()


def split_command_input(command):
    """
    Splits the string at the first space character, to get the actual command, as well as the argument(s) for the command
    :return: (command, argument)
    """

    args = command.split(' ', 1)
    if len(args) > 1:
        return args[0], args[1]
    return args[0], ''


def is_int(value):
    """
    Tests if the string value is an int or not
    :param value: a string value to test
    :return: True if it is an int
    """

    try:
        int(value)
        return True
    except ValueError:
        return False


def valid_command(command):
    """
    Returns a boolean indicating if the robot can understand the command or not
    Also checks if there is an argument to the command, and if it a valid int
    """

    valid_cmds = ["silent","reversed","reversed silent"]
    (command_name, arg1) = split_command_input(command)
    if command_name.lower() == "replay" and arg1.lower() in valid_cmds:
        return True
    return command_name.lower() in valid_commands and (len(arg1) == 0 or is_int(arg1)\
        or " " in arg1 and len(arg1.split()) == 3 and arg1.split()[2] in valid_cmds\
            or " " in arg1 and len(arg1.split()) == 2 and arg1.split()[1] in valid_cmds or arg1.count("-") == 1)


def output(name, message):
    """
    prints the name and the message.
    """

    print(''+name+": "+message)


def do_help():
    """
    Provides help information to the user
    :return: (True, help text) to indicate robot can continue after this command was handled
    """

    return True, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replay all the moves and commands made to the robot
"""



def show_position(robot_name):
    """
    Shows the position of the robot in co'ordinates.
    """

    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    if is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        return True
    return False


def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """

    if update_position(steps):
        if locate == False:
            return False, ""
        else:
            return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """

    if update_position(-steps):
        if locate == False:
            return False, ""
        else:
            return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """

    global current_direction_index

    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0
    if locate == False:
            return False, ""
    else:
        return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """

    global current_direction_index

    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3
    if locate == False:
        return False, ""
    else:
        return True, ' > '+robot_name+' turned left.'


def do_sprint(robot_name, steps):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :return: (True, forward output)
    """

    if steps == 1:
        return do_forward(robot_name, 1)
    else:
        (do_next, command_output) = do_forward(robot_name, steps)
        print(command_output)
        return do_sprint(robot_name, steps - 1)


def handle_command(robot_name, command):
    """
    Handles a command by asking different functions to handle each command.
    :param robot_name: the name given to robot
    :param command: the command entered by user
    :return: `True` if the robot must continue after the command, or else `False` if robot must shutdown
    """

    (command_name, arg) = split_command_input(command)

    if command_name == 'off':
        return False
    elif command_name == 'help':
        (do_next, command_output) = do_help()
    elif command_name == 'forward':
        (do_next, command_output) = do_forward(robot_name, int(arg))
    elif command_name == 'back':
        (do_next, command_output) = do_back(robot_name, int(arg))
    elif command_name == 'right':
        (do_next, command_output) = do_right_turn(robot_name)
    elif command_name == 'left':
        (do_next, command_output) = do_left_turn(robot_name)
    elif command_name == 'sprint':
        (do_next, command_output) = do_sprint(robot_name, int(arg))
    elif command_name == 'replay':
        (do_next, command_output) = replay_command(robot_name, arg)
   
    if do_next == False:
        if command_output == "":
            pass
        else:
            print(command_output)
            show_position(robot_name)
        do_next == True
    else:
        print(command_output)
        show_position(robot_name)
        return do_next


def show_history(command):
    """
    It gets you the history of the robot movements.
    """

    global history

    if command == "replay" or command == "replay silent" or command == "replay reversed" or command == "replay reversed silent" or command.split()[0] == "replay":
        pass
    else:
        history.append(command)
        #print (history)
    return (history)


def replay_command(robot_name, command_name):
    """
    replays the commands of the robot momements.
    """
    
    global locate
    locate = True
    count = 0
    replay_ = list(filter(lambda command: command.split()[0] in directions, history))

    if len(command_name) == 0:
        for i in replay_:
            count += 1 
            handle_command(robot_name, i)    
        return True,  ' > '+robot_name+' replayed '+str(count)+' commands.'

    if command_name == 'silent':
        locate = False
        for i in replay_:
            count += 1 
            handle_command(robot_name, i)    
        return True, ' > '+robot_name+' replayed '+str(count)+' commands silently.'
    
    elif command_name == 'reversed':
        replay_ = replay_[::-1]
        for i in replay_:
            count += 1 
            handle_command(robot_name, i)    
        return True, ' > '+robot_name+' replayed '+str(count)+' commands in reverse.'

    elif command_name == 'reversed silent':
        locate = False
        for i in replay_:
            count += 1 
            handle_command(robot_name, i)    
        return True, ' > '+robot_name+' replayed '+str(count)+' commands in reverse silently.'

    elif command_name.isdigit():
        replay_ = replay_[len(replay_)-int(command_name):]
        for i in replay_:
            handle_command(robot_name, i)    
        return True, ' > '+robot_name+' replayed '+str(command_name)+' commands.'

    elif command_name.split()[0].isdigit() and command_name.split()[1] == "silent":
        locate = False
        replay_ = replay_[len(replay_)-int(command_name.split()[0]):]
        count = 0
        for i in replay_:
            count += 1
            handle_command(robot_name, i)    
        return True, ' > '+robot_name+' replayed '+str(count)+' commands silently.'


    elif command_name.split()[0].isdigit() and command_name.split()[1] == "reversed":
    
        replay_ = replay_[::-1]
        count = 0
        arg = int(command_name.split()[0])
        replay_ = replay_[len(replay_)-arg:]
        for i in replay_:
            count += 1
            handle_command(robot_name, i)    
        return True, ' > '+robot_name+' replayed '+str(count)+' commands in reverse.'

    elif command_name.count("-") == 1:

        n = command_name.split("-")[0]
        m = command_name.split("-")[1]
        count = 0
        for i in range(int(n)-int(m)):
            count += 1
            command_name = replay_[i]
            handle_command(robot_name, command_name)
        return True, ' > '+robot_name+' replayed '+str(count)+' commands.'
    return True, ""


def robot_start():
    """This is the entry point for starting my robot"""

    global position_x, position_y, current_direction_index, history, locate

    robot_name = get_robot_name()
    output(robot_name, "Hello kiddo!")

    position_x = 0
    position_y = 0
    current_direction_index = 0
    history = []
    locate = True

    command = get_command(robot_name)
    show_history(command)
    while handle_command(robot_name, command):
        command = get_command(robot_name)
        show_history(command)
    output(robot_name, "Shutting down..")



if __name__ == "__main__":
    robot_start()
