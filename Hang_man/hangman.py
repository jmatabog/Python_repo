#TIP: use random.randint to get a random word from the list
import random


def read_file(file_name):
    """
    words = read_file(short_words.txt): Step 1 - open file and read lines as words
    """
    f = open(file_name,'r')
    line = f.readlines()
    return line


def select_random_word(words):
    """
    word = select_random_word(words): Step 2 - select random word from list of file
    """
    check = random.randint(0, len(words)-1)
    word = list(words[check])
    y = random.randint(0, len(word)-2)
    print("Guess the word: ",end="")
    for i in range (len(word)):
        word[y] = "_"
        print(word[i],end="")
    return words[check]

    """
    answer = get_user_input(): Step 3 - get user input for answer
    """
def get_user_input():
    user = input('\n'+'Guess the missing letter: ')
    return user


def run_game(file_name):
    """
    This is the main game code. You can leave it as is and only implement steps 1 to 3 as indicated above.
    """
    words = read_file(file_name)
    word = select_random_word(words)
    answer = get_user_input()
    print('The word was: '+word)


if __name__ == "__main__":
    run_game('short_words.txt')

