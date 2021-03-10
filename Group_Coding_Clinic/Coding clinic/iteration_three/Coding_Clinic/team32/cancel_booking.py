from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from team32 import view_calednar as view_calednar


SCOPES = ['https://www.googleapis.com/auth/calendar']


def validate_time(time):
    """
    Function called using a list object 'time'.
    
    Uses ' datetime.datetime.strptime(time, "%H:%M")' to
    validate the time given.

    Return: Function returns False when 'Value Error' is raised. Should the
    that condition not be met, function returns a boolean value of True.
    """

    try:
        datetime.datetime.strptime(time, "%H:%M")
        return True
        
    except ValueError:
        print("Incorrect time format, should be H:M")
        return 0


def validate_date_time(start_date_time):
    """
    Function called using a list object 'start_date_time'.
    
    Uses ' datetime.datetime.strptime(start_date_time[0], '%Y-%m-%d')' to
    validate the date given.

    Return: Function returns False when 'Value Error' is raised. Should the
    that condition not be met, function returns a function call to 'validate_time'
    using the last index in the list.
    """

    try:
        datetime.datetime.strptime(start_date_time[0], '%Y-%m-%d')

        return validate_time(start_date_time[2])

    except ValueError:

        print("Incorrect data format, should be YYYY-MM-DD")

        return 0


def date_query(creds):
    """
    Function called using no parameters.
    
    Uses a while loop to get the user to inpute the date and time as given in
    the example. 

    Return: List object is returned onces it is of lenght three and the function 
    call to 'validate_date_time' return True.

    """

    start_date_time = input('Enter appointment date i.e: 2020-01-01 @ 14:00. ').split()

    if(''.join(start_date_time) == 'y'):
        view_calednar.view_calendar(creds, 'coding.clinic32@gmail.com')
        return date_query(creds)

    if(len(start_date_time) == 3 and validate_date_time(start_date_time)):

        return start_date_time
    return 0


def title_query(creds):
    """
    Function called using no parameters.
    
    Uses a while loop to get the user to inpute the title of the event 
    as given in the example. 

    Return: String object is returned onces it is of lenght two or more.

    """

    event_title = ''

    event_title = input('Enter title <username>: <problem topic>, e.g: coloots:\
toy robot five. ').lower().strip().split()
    if(''.join(event_title) == 'y'):
        view_calednar.view_calendar(creds, 'coding.clinic32@gmail.com')
        return title_query(creds)

    if(len(event_title)>=2 and len(event_title[0])>=4):

        return ' '.join(event_title)

    return 0  
    

def get_event_id(creds, event_title, start_date_time):
    """
    Function called using three parameters; a binary pickle object
    called 'creds', string object 'event_title' and a list object 'start_date_time'. 
    
    Uses Google API calls to get a list of events on the calendar id: 
    coding.clinic32@gmail.com. Iterates through theat list and matches
    the given event title and start date time to retrieve the event id.

    Return: Function returns a function call to 'update_event' should an
    event id be found, user will be prompt and nothing will be returned.
    
    """

    service = build('calendar', 'v3', credentials=creds)

#     now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    
#     events_result = service.events().list(calendarId=\
# 'coding.clinic32@gmail.com', timeMin=now,
#                                         maxResults=10, singleEvents=True,
#                                         orderBy='startTime').execute()
    now = datetime.datetime.utcnow().isoformat()+ 'Z'

    next_week = datetime.timedelta(days=6)

    future = (datetime.datetime.utcnow() + next_week).isoformat() + 'Z'

    events_result = service.events().list(calendarId=\
<<<<<<< HEAD
'coding.clinic32@gmail.com', timeMin=now, singleEvents=True,
=======
                                        'coding.clinic32@gmail.com',\
                                        timeMax=future,
                                        timeMin=now, singleEvents=True,
>>>>>>> 63f50c2bfba465cd2b7ce44be99384b80705e2cb
                                        orderBy='startTime').execute()


    events = events_result.get('items', [])


    if not events:
        print('No upcoming events found.')

    for event in events:

        start = event['start'].get('dateTime', event['start'].get('date'))

        start = str(start)

        title = event['summary'].strip()

        if(title == event_title and start[:10] == start_date_time[0]\
        and start[11:16] == start_date_time[2]):

            event_id = event['id']

            print('Event ID found.')
            
            return event_id

    print('Event ID not found. Please consult the clinic calendar and try again.')
    return 0


def update_event(creds, username, event_title, start_date_time, event_id):
    """
    Function called using binary pickle file 'creds', string object 'event_title',
    list object 'start_date_time' and a unique id 'event_id'.

    Uses a while loop to get the user to inpute the correct email address with
    the WTC domain.

    Updates the attendees field event to the coding_clinic calendar.

    Return: Function has no return value
    """


    service = build('calendar', 'v3', credentials=creds)

    event = service.events().get(calendarId='coding.clinic32@gmail.com', eventId=event_id).execute()

    while(True):

        patient_email = input('Enter WTC email address: ').lower().strip()

        if('@' in patient_email):
            if(len(patient_email.split()) and \
            patient_email.split('@')[1] =='wethinkcode.co.za' or \
            patient_email.split('@')[1] == 'student.wethinkcode.co.za'):
                break
    
    email_to_del = ''
    
    for email in event['attendees']:

        if(email["email"] == patient_email):

            email_to_del = email

    if(email_to_del == ''):
        return 0

    event_title = event['summary'].replace(' with '+username,'')

    event['summary'] = event_title

    event["attendees"].remove(email_to_del)

    updated_event = \
service.events().update(calendarId='coding.clinic32@gmail.com', \
eventId=event['id'], body=event).execute()
    
    print('Booking removed.')

    return 0

   
def cancel_booking(creds, username):

    """
    Function called using a binary pickle object 'creds' and string object 
    'username'.

    This is the driver function in the module and intends to cancel bookings 
    on the coding clinic calendar.

    Return: Function has no return value.
    """
    event_title, start_date_time, event_id = 1,1,1
    while event_title and start_date_time and event_id:
        event_title = title_query(creds)

        start_date_time = date_query(creds)

        if(event_title and start_date_time):

            event_id = get_event_id(creds, event_title, start_date_time)

        if(event_title and start_date_time and event_id ):

            return update_event(creds, username, event_title, \
start_date_time, event_id)
    
    return 0
