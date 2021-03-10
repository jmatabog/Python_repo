import re
import sys
import json
import time
import shutil
import pickle
import os.path
import getpass
from io import StringIO
from datetime import datetime
from team32 import sys_encryp as sys_encrypt
from team32 import view_calednar as view_calednar
from team32 import make_booking as booking
from team32 import create_slots as createslots
from team32 import cancel_booking as cancel_b
from team32 import cancel_slots as cancel_slots
from termcolor import colored
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request



cmd_arg_dictionary = \
{
    'vc'    : ['View calendar       ', 'Displays user calendar.'],
    'vcc'   : ['View clinic calendar', 'Displays coding clinic calendar.'],
    'mb'    : ['Make booking        ', 'Book an appoinment in your name.'],
    'cs'    : ['Create Slot         ', 'Create a slot for appointments.'],
    'cb'    : ['Cancel Booking      ', 'Cancel a booking in your name.'],
    'csl'   : ['Cancel Slot         ', 'Cancel a slot for an appointment.'],
    'dp'    : ['Delete pickle       ', 'Delete the pickle assigned to you.'],
    'who'   : ['Logged in user      ', 'See who is logged in'],
    'login' : ['Log in              ', 'Creates you a ticket.'],
    'logout': ['Log out             ', 'Expires your ticket.'],
    'help'  : ['Help                ', 'List commands and their descriptions.']
}


global emailaddress

def return_creds(pickle_path):

    """
    Function called using the path to a pickle. 
    
    It opens the file in binary mode and creates a pickle object
    that can be used by the GOOGLE API services.

    Return: pickle object that can be used by the GOOGLE API services.
    """

    with open(pickle_path, 'rb') as token:
        creds = pickle.load(token)
    return creds


def function_init():
    """
    Function called using no parameters.

    It reads from the config file and access the username that is
    logged  in so that a credentials file for that user is obtained.

    Return: Function a function call to 'return_creds' using
    the pickle path.
    """

    config_string = read_from_config()
    
    username = config_string["users"]["logged_in"]

    pickle_path = sys_encrypt.get_pickle_dir(username)

    return return_creds(pickle_path)



def get_user_calendar():
    """
    Function called using no parameters.

    Intends to call the neccessary functions to display
    the primary calendar to user.

    Return: Function has no return value.
    """

    text = "\nPrimary Calendar\n"
    display = colored(text,'magenta', attrs=['bold'])
    print(display)  
    creds = function_init()

    view_calednar.view_calendar(creds, 'primary')


def get_clinic_calendar():
    """
    Function called using no parameters.

    Intends to call the neccessary functions to display
    the coding clinic calendar to user.

    Return: Function has no return value.
    """

    text = "\nClinic Calendar\n"
    display = colored(text,'cyan', attrs=['bold'])
    print(display)  

    creds = function_init()

    view_calednar.view_calendar(creds, 'coding.clinic32@gmail.com')


def make_booking():
    """
    Function called using no parameters.

    Intends to call the neccessary functions to make a booking 
    on the calendar.

    Return: Function has no return value.
    """

    text = "If at any point you wish to see the clinic calendar, enter 'y'."
    display = colored(text,'blue', attrs=['bold'])
    print(display)

    config_string = read_from_config()
    
    username = config_string["users"]["logged_in"]

    pickle_path = sys_encrypt.get_pickle_dir(username)

    creds = return_creds(pickle_path)
   
    booking.make_booking(creds, username)


def create_slot():
    """
    Function called using no parameters.

    Intends to call the neccessary functions to create a slot 
    on the calendar.

    Return: Function has no return value.
    """

    text = "If at any point you wish to see the clinic calendar, enter 'y'."
    display = colored(text,'blue', attrs=['bold'])
    print(display)

    creds = function_init()

    createslots.create_slot(creds)


def cancel_booking():
    """
    Function called using no parameters.

    Intends to call the neccessary functions to cancel a booking for
    an event.

    Return: Function has no return value.
    """

    text = "If at any point you wish to see the clinic calendar, enter 'y'."
    display = colored(text,'blue', attrs=['bold'])
    print(display)

    config_string = read_from_config()
    
    username = config_string["users"]["logged_in"]

    pickle_path = sys_encrypt.get_pickle_dir(username)

    creds = return_creds(pickle_path)
   
    cancel_b.cancel_booking(creds, username)


def cancel_slot():
    """
    Function called using no parameters.

    Intends to call the neccessary functions to cancel a slot created
    on the calendar.

    Return: Function has no return value.
    """

    text = "If at any point you wish to see the clinic calendar, enter 'y'."
    display = colored(text,'blue', attrs=['bold'])
    print(display)

    config_string = read_from_config()
    
    username = config_string["users"]["logged_in"]

    pickle_path = sys_encrypt.get_pickle_dir(username)

    creds = return_creds(pickle_path)  

    cancel_slots.cancel_slot(creds, username)    


def delete_pickle():
    """
    Function is called with no parameters.

    It intends to delete an existing user pickle.

    Return: Function will return a True if the userame given 
    was not found in the cofig file.
    It will return False if the username given was found in 
    the config file.
    """

    user_name = input('Your username: ').strip().lower()

    user_true = validate_user()

    path = os.getcwd()+'/.config/users/'+user_name

<<<<<<< HEAD
=======
    ticket_dir = os.getcwd()+'/.config/sys/.ticket.txt'

>>>>>>> cf241b6cb422db7e0961459f488ab894a181f046
    while(user_true):
        shutil.rmtree(path)

        config_string = read_from_config()

        for key in config_string["users"]["user_dictionary"]:
            if(config_string["users"]["user_dictionary"][key][0] == user_name):
                
                print(f'Deleting credentials for: {user_name}.\n')
                
                config_string["users"]["user_dictionary"].pop(key)
                
<<<<<<< HEAD
                write_to_config_file(config_string)
                
                print('Pickle successfully deleted.\n')
=======
                config_string["users"]["logged_in"] = ""
                
                write_to_config_file(config_string)

                if(os.path.exists(ticket_dir)):

                    os.remove(ticket_dir)

                    print('Pickle successfully deleted.\n')
>>>>>>> cf241b6cb422db7e0961459f488ab894a181f046
                
                return False

        return True


def get_who():
    """
    Function is called using no paraneters.

    It intends to prompt the user with a scope of who is currently logged in.

    Function has no return value.
    """
    config_string = read_from_config()

    print(f'\n{time.strftime("%D",time.localtime())}\
    {time.strftime("%H:%M:%S",time.localtime())}\n')

    print(f'{config_string["users"]["logged_in"]} is currently logged in.\n')


def get_help():

    """
    Function cslled using no parameters.

    It is the default function invoked when an ivalid command is parsed.

    Return: Function has no return value.
    """

    print('Help', end='\n\n')

    for item in cmd_arg_dictionary:

        print(f'    {cmd_arg_dictionary[item][0]}     cmd arg:    {item}')

    print('\ni.e: clinic -help')


def log_out():
    """
    Function is called using no parameters.
    
    It intends to log the user out which in turn removes the ticket 
    file from a directory.

    Return: Function has no return value.
    """

    print('Logging you out...')

    ticket_dir = os.getcwd()+'/.config/sys/.ticket.txt'

    if(os.path.exists(ticket_dir)):

        config_string = read_from_config()
        config_string["users"]["logged_in"] = []
        write_to_config_file(config_string)
        
        os.remove(ticket_dir)


def log_in():
    """
    Function called with no parameters.

    It intends to log in the user through creating or refreshing a 
    the ticket file needed for every user.

    """
    ticket_dir = os.getcwd()+'/.config/sys/.ticket.txt'

    if(os.path.exists(ticket_dir)):

        print('\nLooks like you\'re logged in. Ticket will expire at: ', end='')

<<<<<<< HEAD
        print(time.strftime("%H:%M:%S",time.localtime(os.path.getctime(ticket_dir)+10000)), end='\n\n')
=======
        print(time.strftime("%H:%M:%S",time.localtime(os.path.getctime(\
ticket_dir)+10000)), end='\n\n')
>>>>>>> cf241b6cb422db7e0961459f488ab894a181f046

    else:
        user_true = validate_user()

        ticket_string = f'Ticket created for {user_true}.'

        with open(ticket_dir,'w+') as file:

            file.write(ticket_string)

        if(check_ticket()):

            config_string = read_from_config()

            config_string["users"]["logged_in"] = user_true

            write_to_config_file(config_string)

            print('Login successful. Ticket will expire at: ', end='')
            
<<<<<<< HEAD
            print(time.strftime("%H:%M:%S",time.localtime(os.path.getctime(ticket_dir)+10000)))
=======
            print(time.strftime("%H:%M:%S",time.localtime(os.path.getctime(\
ticket_dir)+10000)))
>>>>>>> cf241b6cb422db7e0961459f488ab894a181f046
  

def do_command(cmd_arg):
    """
        Function called using a string object 'cmd_arg'.
        The parameter is tested against allowed commands to
        call the appropriate function for the given command.

        Return: None object. Function call to the appropriate 
        function.
    """
    if(cmd_arg == 'vc'):
        return get_user_calendar()
    elif(cmd_arg == 'vcc'):
        return get_clinic_calendar()
    elif(cmd_arg == 'mb'):
        return make_booking()
    elif(cmd_arg == 'cs'):
        return create_slot()
    elif(cmd_arg == 'cb'):
        return cancel_booking()
    elif(cmd_arg == 'csl'):
        return cancel_slot()
    elif(cmd_arg  == 'dp'):
        return delete_pickle()
    elif(cmd_arg == 'who'):
        return get_who()
    elif(cmd_arg == 'help'):
        return get_help()
    elif(cmd_arg == 'login'):
        return log_in()
    elif(cmd_arg == 'logout'):
        return log_out()
    else:
        pass


def decrypt_credentials():
    """
        Function called to decrypt the encrypted values stored as 
        keys in the json file. It iterates through the dictionary obtained
        from 'read_from_config' and uses the decryption key for each 
        dictionary key to decrypt the password. It then updates 'system_users'
        dictionary to map the decerypted password to the correct username.

        Return: A dictionary object 'system_users' mapping passwords to 
        usernames.

    """

    system_users = dict()

    config_string = read_from_config()

    user_dictionary = config_string["users"]["user_dictionary"]

    for encry_passwd in user_dictionary:

        key_copy = encry_passwd

        user_name = user_dictionary[encry_passwd][0]

        a = encry_passwd[1:].strip('\'')

        encry_passwd = bytes(a,'utf-8')

        b = user_dictionary[key_copy][1][1:].strip('\'')

        decrypt_key = bytes(b,'utf-8')

<<<<<<< HEAD
        password = sys_encrypt.decrypt_user_password(decrypt_key, encry_passwd).decode()
=======
        password = sys_encrypt.decrypt_user_password(decrypt_key,\
 encry_passwd).decode()
>>>>>>> cf241b6cb422db7e0961459f488ab894a181f046

        system_users.update({password : user_name})
    
    return system_users


def validate_email_address(email_address):
    """
        Function called using string object 'email_address'
        to check if it is a valid wethinkcode email address or not.

        Return: A list object containing the username and the wethinkcode
        mailing domain. If the email given is invalid a boolean value 'False'
        is returned.
    """

    global emailaddress

    while('@' in email_address):

        email_split = email_address.split('@', 1)

        if(len(email_split) == 2 and \
email_split[1] =='wethinkcode.co.za' or\
email_split[1] == 'student.wethinkcode.co.za'):    
            emailaddress = '@'.join(email_split)    
            return email_split
        
        break

    return False


def write_to_config_file(config_string):
    """
        Function called to write to the configuration file.
<<<<<<< HEAD
        Uses the json object attribute '.dump(dictionary_object,file)' to convert
        the python dictionary object into a json format.
=======
        Uses the json object attribute '.dump(dictionary_object,file)' to
        convert the python dictionary object into a json format.
>>>>>>> cf241b6cb422db7e0961459f488ab894a181f046

        Return: Function has no return value.       
    """

    path = os.getcwd()+'/.config/sys/.config.json'

    with open(path,'w') as config:
        
        json.dump(config_string,config,indent=4)


def read_from_config():
    """
        Function called to read from the configuration file.
        Uses the json object attribute '.load(file)' to convert
        the text string into a dictionary.

        Return: Dictionary object 'config_string'.
    """

    path = os.getcwd()+'/.config/sys/.config.json'

    with open(path,'r') as config:

        config_string = json.load(config)

    return config_string


def get_new_password():
    """
        Function called to prompt the user for their password.
        User will keep being prompt until they enter a password
        that is of characters that are longer than four.

        User is then asked to confirm their password.

        Return: String object of the password if the passwords entered match.
        A recursive function call to 'get_new_password' if the given passwords
        do not match.
    """

    password = getpass.getpass('Password: ').lower().strip()

    while('' or len(password) < 4):

        print('Stonger passwords only (length should be longer than four).')

        password = getpass.getpass('Password: ').lower().strip()

    passwrd_2 = getpass.getpass('Confirm password: ').lower().strip()
    
    if(password == passwrd_2):

        return passwrd_2

    print('Passwords do not match. Try again.')

    return get_new_password()


def add_clinic_calendar(username):

    """
    Adds new user to the coding clinic caledar.

    Funtion has no return value.
    """

    global emailaddress
    
    cc_path = os.getcwd()+'/.config/sys/'+'.codingclinic/codingclinic.pickle'

    with open(cc_path, 'rb') as token:
            creds = pickle.load(token)

    service = build('calendar', 'v3', credentials=creds)

    aclInfo = \
    {
        'kind': 'calendar#aclRule', 
        'id': 'user:'+emailaddress,
        'scope': {
            'type': 'user',
            'value': emailaddress
        },
        'role': 'writer'
    }

    created_rule = service.acl().insert(calendarId='coding.clinic32@gmail.com',\
         body=aclInfo).execute()

    if(created_rule):
        print(f"New user: {username} has been successfully added to the clinic\
 calendar.")
    else:
        print(f'Error: C32.\n   - Failled to add {username} to \
the clinic calendar.')


def update_json_first_time_use(username, password):
    """
        Function called using two string objects 'username'
        and 'password'. The password give is encrypted first
        then mapped to the 'username', decryption key value and
        the pickle directory path. THis is then stored in a the 
        json configuration file.

        Return: String object 'username' if a directory with the 
        same name as the username given. Recursive call to 
        'update_json_first_time_use' if file does not exist.
    """

    parent_dir = os.getcwd()+'/.config/users/'+username

    if(os.path.exists(parent_dir)):

        encryption_tuple = sys_encrypt.encrypt_user_password(password)

        pickle_path = sys_encrypt.get_pickle_dir(username)

        temp_list = [username, str(encryption_tuple[1]), pickle_path]

        config_string = read_from_config()  

        temp_dictionary = config_string["users"]["user_dictionary"]

        temp_dictionary.update({str(encryption_tuple[0]): temp_list})

        config_string["users"]["user_dictionary"] = temp_dictionary

        add_clinic_calendar(username)

        write_to_config_file(config_string)

        return username

    os.mkdir(parent_dir)

    return update_json_first_time_use(username, password)


def first_time_user():
    """
        Function called to prompt the user to enter their WeThinkCode
        email address. Their input is then validated and their username
        is retrieved from there. The cofiguration file is then updated
        to include their encrypted password value mapped to the username, 
        password decryption key and pickle directory path.

        Return: None object - Fuction call to 'update_json_first_time_use'
        upon valid e-mail address given and 'first_time_user' upon invalid 
        e-mail given.
    """

    email_address = input('WTC email: ').lower().strip()

    email_address = validate_email_address(email_address)

    while(email_address):
        
        username = email_address[0]

        password = get_new_password()

        return update_json_first_time_use(username, password)

    print('WTC users only.')
    
    return first_time_user()


def prompt_first_time():
    """
        Function called to prompt the user to indicate whether or 
        not it is their first time using the system.

        Return: valid user response. Either a 'y' or 'n'.
    """

    while(True):

        prompt = input('Is this your first time login? [n/Y] ').lower().strip()

        if(prompt == 'y' or prompt== 'n'):
            break
        
    return prompt


def validate_user():
    """
        Function called to validate a user logging in.
        First, credentials from the json file is decrypted and 
        stored in a dictionary that maps the user password to their 
        username, decryption key and picle directory path.

        This information is used to check whether user loggin is an existing
        or if a new pickle shpuld be created for them. This is all done by 
        checking whether or not the password entered exist in our records or not

        Return: A list containing username, decryption key and
        the pickle directory path.

    """

    system_users = decrypt_credentials() 

    password = getpass.getpass('WTC password: ')

    if(password in system_users):

        return system_users[password]

    if(password not in system_users):

        prompt = prompt_first_time()
        
        while(prompt == 'y'):

            return first_time_user()

        return validate_user()


def validate_cmd_arg(sys_argv):
    """
        Function called using a string object 'sys_argv'.
        The parameter passed is then checked if whether it is
        a valid command argument or not.

        Return: A boolean 'True' or 'False' is return depending on
        whether the 'sys_arg' is a valid command or not.
    """

    sys_argv = ''.join(re.split(r'\ |\-',sys_argv))
    
    sys.argv[1] = sys_argv

    if(sys_argv in cmd_arg_dictionary):

        return True

    return False


def check_ticket():
    """
        Function called to check if a ticket exist for 
        a user. If there is no ticket, or a ticket has expired
        a new one is created through validating the user.

        Return: function return a boolean 'True' to indicate 
        the success of the function call.
    """
    
    ticket_dir = os.getcwd()+'/.config/sys/.ticket.txt'

    if(not os.path.exists(ticket_dir)):
        print('First you log in.')
        return log_in()
      

<<<<<<< HEAD
    creation_time = os.path.getctime(ticket_dir) #get time file was created

    epoch = int(time.time()) #get unix epoch time

    two_45_later = creation_time+10000 #int value 2 hrs 45 mins later
   
    # print(time.strftime("%H:%M:%S",time.localtime(creation_time)))
=======
    creation_time = os.path.getctime(ticket_dir) 

    epoch = int(time.time())

    two_45_later = creation_time+10000 
   
>>>>>>> cf241b6cb422db7e0961459f488ab894a181f046

    if(epoch < two_45_later):
        
        return True

    else:
<<<<<<< HEAD

=======
>>>>>>> cf241b6cb422db7e0961459f488ab894a181f046
        os.remove(ticket_dir)

        return check_ticket()


def do_main():
    """ 
    Main function that outlines how the rest of the program 
    executes instructions. This function is dependend on system
    argument variables. If none is given, the 'get_help'
    functions is called.

    Only valid commands will be handled.

    The 'check_ticket' function is repsonsible for logging
    in the user and making sure a ticket exist for a each user.

    """

    global cmd_arg_dictionary

    if(len(sys.argv) == 2) and validate_cmd_arg(sys.argv[1]):

        cmd_arg = sys.argv[1].replace('-','').strip().lower()

        set_y = {'help','logout','login'}

        if(cmd_arg in set_y ):

            do_command(cmd_arg)
            
            return 0

        if(check_ticket()):

            do_command(cmd_arg)

    else:

        get_help()


if __name__ == "__main__":
    try:
        do_main()
    except KeyboardInterrupt:
        print()
        pass