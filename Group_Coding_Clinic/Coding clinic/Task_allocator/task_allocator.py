import sys
from io import StringIO
import random
import json
import smtplib
import getpass
import os
from datetime import datetime
from email.message import EmailMessage


#Edited: Sunday, 15 November 2020 by Isaac.

iteration_dictionary = {'iteration one':['Step one - Configure the system', 'Step two - View Calendars', 'Testing' ],
               'iteration two':['Step three - Make a booking', 'Step four - Volunteer slots', 'Testing'],
               'iteration three':['Step five - Cancel a booking', 'Step six - Cancel volunteering', 'Testing'],
               'iteration bonus': ['Step seven', 'Step eight', 'Testing']}



def get_names(available_names):

    chosen_names = []

    while len(chosen_names)<=1:

        rand_index = random.randint(0, len(available_names)-1)

        chosen_name = available_names[rand_index]

        chosen_names.append(chosen_name)

        available_names.remove(chosen_name)

    return chosen_names, available_names


def get_iteration_key_input(remainin_iterations):

    if(len(remainin_iterations)<1):
        print("Project iterations done. Please refresh config file")
        return False

    key = ''
    while(key not in remainin_iterations):
        print('Sorry, did not find iteration in the remaining iterations. Try again.')
        key = input('Please enter iteration i.e: iteration one ').lower().strip()
    print()
    return key


def get_iteration_key(remainin_iterations):
    '''
    Gets iteration key from the user through command line arguments or user prompt.
    '''

    if(len(sys.argv)>1 and sys.argv[1].lower() in remainin_iterations):  

        key = sys.argv[1].lower().strip()        

    if(len(sys.argv) == 1):   

       return get_iteration_key_input(remainin_iterations)
    

def who_is():
    email_one = input('Sender email please: ').strip().split('@')

    while(email_one[1] == 'student.wethinkcode.co.za'):

        passwd_one = getpass.getpass('Password please: ')
        passwd_two = getpass.getpass('Confirm password: ')

        if(passwd_one == passwd_two):
            return '@'.join(email_one), passwd_two
            
        print("User provided incorrect password.")
       
        break

    return who_is()

    
def send_email(user_names, key, contents):

    fromaddr, passwd = who_is()

    msg = EmailMessage()
    msg['Subject'] = f'Tasks allocated [{key.upper()}!]'
    msg['From'] = fromaddr
    msg['To'] = user_names
    
    email_content = contents

    msg.set_content(email_content)

    # Send the message via our own SMTP server.
    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()
  
    server.login(fromaddr, passwd)

    server.send_message(msg)

    server.quit()


def get_allocate_testers(names, tdd_done):

    if(len(tdd_done)==6):
        print('No more testers. Congratulations!')
        return False, False

    filtered_list = [i for i in names if i not in tdd_done]

    chosen_names, new_available_list = get_names(filtered_list)

    none = [new_available_list.append(i) for i in tdd_done]

    return chosen_names, new_available_list


def write_to_file(key, task_dictionary):
    date_and_time = datetime.now()

    f = StringIO()

    current_date_and_time = date_and_time.strftime("%H:%M:%S %B %d, %Y")

    f.write('TIME STAMP: '+current_date_and_time+'.\n\n')

    f.write(str(key.upper())+'\n\n')

    for key in task_dictionary:

        f.write(str(key).upper() + '\n')

        for items in task_dictionary[key]:

            f.write('--'+str(items) + '\n')

        f.write('\n')

    f.write('\nRegards\n - Team 32 ;)')

    contents = f.getvalue()

    print(contents)

    f.close()

    return contents


def get_task_dictionary(key, tester_names, available_names, iteration_dictionary):
    
    task_dictionary = dict()

    for item in range(0,3):

        if(item == 2):

            task_dictionary.update({iteration_dictionary[key.lower()][item]: tester_names})

            break

        new_chosen_names, available_names = get_names(available_names)

        task_dictionary.update({iteration_dictionary[key.lower()][item]: new_chosen_names})
    
    return task_dictionary


def write_to_config_file(config_string):

    path = os.getcwd()+'/email_cred.json'

    with open(path,'w') as config:
        json.dump(config_string,config)


def read_from_config():

    path = os.getcwd()+'/email_cred.json'

    with open(path,'r') as config:
        config_string = json.load(config)
    return config_string


def main():

    chosen_names = []

    config_string = read_from_config()

    names = config_string["user"]["names"]

    user_names = config_string["user"]["user_names"]
    
    tdd_done = config_string["user"]["tdd_done"]

    iteration_dictionary = config_string["user"]["iteration_dictionary"]

    remainin_iterations = config_string["user"]["remainig_iterations"]

    key = get_iteration_key(remainin_iterations)

    if(not key):
        return 0

    key_copy = key

    tester_names, available_names = get_allocate_testers(names, tdd_done)

    if(not tester_names and not available_names):
        return 0

    [tdd_done.append(i) for i in tester_names]

    remainin_iterations.remove(key_copy)

    config_string["user"]["remainig_iterations"] = remainin_iterations
    
    config_string["user"]["tdd_done"] = tdd_done

    write_to_config_file(config_string)

    task_dictionary = get_task_dictionary(key, tester_names, available_names, iteration_dictionary)
    
    contents = write_to_file(key, task_dictionary)

    send_email(user_names, key_copy, contents)

    print('Goodluck, team32 :0!')


if __name__ == "__main__":
    main()