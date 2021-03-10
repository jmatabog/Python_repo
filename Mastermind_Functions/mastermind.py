
import random

code = [0, 0, 0, 0]
correct_digits_and_position = 0
correct_digits_only = 0
correct = False

# TODO: Decompose into functions

def generate_code():
    """Function that creates the 4 digit code, using random digits from 1 to 8 and cannot repeart"""

    global code
    code = [0, 0, 0, 0]

    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value

    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')


def display_digits():
    """function show's the correctness of the code and print, the output of their places"""

    print('Number of correct digits in correct place:     ' + str(correct_digits_and_position))
    print('Number of correct digits not in correct place: ' + str(correct_digits_only))


def compare_code():
    """ compare the code with user input"""

    global correct_digits_and_position
    global correct_digits_only

    answer = input("Input 4 digit code: ")
    while len(answer) < 4 or len(answer) > 4:
        print("Please enter exactly 4 digits.")
        answer = input("Input 4 digit code: ")

    correct_digits_and_position = 0
    correct_digits_only = 0
    for i in range(len(answer)):
        if code[i] == int(answer[i]):
            correct_digits_and_position += 1
        elif int(answer[i]) in code:
            correct_digits_only += 1

    display_digits()


def print_code():
    """Print the random generated code"""

    print('The code was: '+str(code))


def check_code(turns):
    """Checks the correctness of the code and displa's the remaining turns"""

    global correct

    if correct_digits_and_position == 4:
        correct = True
        print('Congratulations! You are a codebreaker!')
    else:
        print('Turns left: ' + str(12 - turns))


def run_game():
    """Main function for running game"""

    global correct
    correct = False

    generate_code()

    turns = 0
    while not correct and turns < 12:
        compare_code()
        turns += 1
        check_code(turns)

    print_code()

if __name__ == "__main__":
    run_game()