import random


def run_game():
    """
    TODO: implement Mastermind code here
    """
    code = []
    i = 0
    turns = 12
    corr = 0
    not_corr = 0
    while True:
        num = str(random.randint(1,8))
        if i == 4:
            break
        if num not in code:
            code.insert(i,num)
            i += 1

    print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.")
    while turns:
        guess = input("Input 4 digit code: ")
        if len(guess) < 4 or len(guess) > 4 or not guess.isdigit():
            print("Please enter exactly 4 digits.")
            continue

        i = 0
        guess = list(guess)
        while i in range(len(code)):
            if code[i] == guess[i]:
                corr = corr + 1
            elif (guess[i]) in code:
                not_corr = not_corr + 1
            i += 1
            
        print("Number of correct digits in correct place:     {}".format(corr))
        print("Number of correct digits not in correct place: {}".format(not_corr))
        x = ""
        if corr is 4:
            print("Congratulations! You are a codebreaker!")
            print("The code was: "+x.join(code))
            break
        else:
            turns = turns - 1
            print("Turns left: "+str(turns))
    
if __name__ == "__main__":
    run_game()
