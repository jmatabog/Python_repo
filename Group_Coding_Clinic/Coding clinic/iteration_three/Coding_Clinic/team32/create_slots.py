import os
import json
import pickle
import datetime
from uuid import uuid4
from team32 import sys_encryp
from team32 import view_calednar as view_calednar
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


def view_available_slots(credentials):
    """
    CURRENTLY THIS CODE WAS JUST USED TO RETRIEVE THE LIST OF EVENTS 
    ON THE CALENDAR, HOWEVER UTIMATELY IT SHOULD BE USED TO MAKE THE BOOKING
    FOR A VOLUNTEER SLOT
    """
    print ("The coding clinic calendar currently looks as follows, \
please take note of the available slots \
and create a volunteer slot in one of them.")
    calendar_Id='coding.clinic32@gmail.com'
    view_calednar.view_calendar(credentials, calendar_Id)


def call_update_hour_minute(hour,hour_incre, minute, minute_incre):

    if 30<minute<59:

        return call_update_hour_minute(hour,hour_incre, 30, minute_incre)

    elif 00<minute<30:

        return call_update_hour_minute(hour,hour_incre, 00, minute_incre)

    new_hour = hour + hour_incre

    if minute == 30 and minute_incre == 30:
        new_hour += 1

        new_minute = 00 

    else:

       new_minute = minute + minute_incre

    return new_hour, new_minute


def verify_user():
    """
    Uses a while loop to get the user to input the correct email address with
    the WTC domain.

    /function has no return value
    """
    while(True):

        patient_email = input('Enter WTC email address: ').lower().strip()

        if(patient_email.split('@')[1] =='wethinkcode.co.za' or \
        patient_email.split('@')[1] == 'student.wethinkcode.co.za'):

            return patient_email


def check_for_conflicts(service, event_start_time, event_end_time):
    """
    Function checks user and coding clinic calendar to see if there are 
    any conflicts with booking times to prevent any double bookings

    Returns True bool if there are conflicts and false if not
    """
    global patient_email

    now = datetime.datetime.utcnow().isoformat()+ 'Z'
    tomorrow_delta = datetime.timedelta(days=6)
    tomorrow_ = (datetime.datetime.utcnow() + tomorrow_delta).isoformat() + 'Z'

    events_result = service.events().list(calendarId = patient_email,\
    timeMax = tomorrow_, timeMin = now, singleEvents=True,\
    orderBy = 'startTime').execute()
    events = events_result.get('items')

    event_start_time = event_start_time+'+02:00'
    event_end_time = event_end_time+'+02:00'

    for item in events:
<<<<<<< HEAD
<<<<<<< HEAD
        if event_start_time == item.get('start').get('dateTime') or\
    event_start_time < item.get('end').get('dateTime'):
=======
        if event_start_time == item.get('start').get('dateTime'):
>>>>>>> cf241b6cb422db7e0961459f488ab894a181f046
=======
        if event_start_time == item.get('start').get('dateTime'):
>>>>>>> 63f50c2bfba465cd2b7ce44be99384b80705e2cb
            print("Conflict: There is an event at the time you selected.")
            return True
    return False


def creating_slot(command_line_input, credentials, date_and_time):
    """
    Function called using a string object containing the event title,
    a binary token file called credentials, and the list object 'date_and_time'.

    Uses a while loop to get the user to input the correct email address with
    the WTC domain.

    Creates three events to the coding_clinic  with a 30 minute gap.

    Return: Function has no return value.

    """
    global patient_email

    service = build('calendar', 'v3', credentials=credentials)

    year, month, day, hour, minute = \
        int(date_and_time[0][:4]), int(date_and_time[0][5:7]),\
        int(date_and_time[0][8:]), int(date_and_time[2][:2]), \
        int(date_and_time[2][3:5])

    
    while(True):

        patient_email = input('Enter WTC email address: ').lower().strip()

        if('@' in patient_email):
            if(len(patient_email.split()) and \
            patient_email.split('@')[1] =='wethinkcode.co.za' or \
            patient_email.split('@')[1] == 'student.wethinkcode.co.za'):

                break

    event_time_dict = dict()

    # cater for 30 minutes slot creation
    time = call_update_hour_minute(hour,0, minute, 0)

    event_start_time = datetime.datetime(year, month, day, time[0], time[1])

    isoformat_event_start_time = event_start_time.isoformat()

    time = call_update_hour_minute(hour,0, minute, 30)

    event_end_time = datetime.datetime(year, month, day, time[0], time[1])
    
    isoformat_event_end_time = event_end_time.isoformat()

    if not check_for_conflicts(service, isoformat_event_start_time,\
    isoformat_event_end_time):

        event_time_dict.update\
        ({isoformat_event_start_time:isoformat_event_end_time})

    elif check_for_conflicts(service, isoformat_event_start_time,\
    isoformat_event_end_time):
        return False


    event_start_time2 = datetime.datetime(year, month, day, time[0], time[1])

    isoformat_event_start_time2 = event_start_time2.isoformat()

    time = call_update_hour_minute(hour,1, minute, 0)

    event_end_time2 = datetime.datetime(year, month, day, time[0], time[1])
    
    isoformat_event_end_time2 = event_end_time2.isoformat()

    if not check_for_conflicts(service, isoformat_event_start_time2,\
    isoformat_event_end_time2):

        event_time_dict.update\
        ({isoformat_event_start_time2:isoformat_event_end_time2})

    elif check_for_conflicts(service, isoformat_event_start_time2,\
    isoformat_event_end_time2):
        return False

    
    event_start_time3 = datetime.datetime(year, month, day, time[0], time[1])

    isoformat_event_start_time3 = event_start_time3.isoformat()

    time = call_update_hour_minute(hour,1, minute, 30)

    event_end_time3 = datetime.datetime(year, month, day, time[0], time[1])
    
    isoformat_event_end_time3 = event_end_time3.isoformat()

    if not check_for_conflicts(service, isoformat_event_start_time2,\
    isoformat_event_end_time2):

        event_time_dict.update\
        ({isoformat_event_start_time3:isoformat_event_end_time3})

    elif check_for_conflicts(service, isoformat_event_start_time2,\
    isoformat_event_end_time2):
        return False

    for start_time in event_time_dict:

        event = {
                'summary': command_line_input,
                'location': 'Google meets.',
                'description': 'Doctor and patient confidentiality.',
                'start': {
                    'dateTime': start_time, 
                    'timeZone': 'Africa/Johannesburg',
                },
                'end': {
                    'dateTime': event_time_dict[start_time],
                    'timeZone': 'Africa/Johannesburg',
                    },
                'attendees': [
                    {'email': patient_email},
                    ],
                "conferenceData": {"createRequest": {"requestId": f"{uuid4().hex}",
                    "conferenceSolutionKey": {"type": "hangoutsMeet"}}},
                "reminders": {"useDefault": True}
                }
        event_result = service.events().\
        insert(calendarId='coding.clinic32@gmail.com', sendNotifications=True,\
        body=event, conferenceDataVersion=1).execute()
        
    print("Event created.")

    print('Please follow the link to if you want to use Google meets: %s' %\
    (event_result.get('htmlLink')))


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
        return False


def validate_date_time(start_date_time):
    """
    Function called using a list object 'start_date_time'.
    
    Uses ' datetime.datetime.strptime(start_date_time[0], '%Y-%m-%d')' to
    validate the date given.

    Return: Function returns False when 'Value Error' is raised. Should the
    that condition not be met, function returns a function call to 
    'validate_time'
    using the last index in the list.

    """

    try:
        datetime.datetime.strptime(start_date_time[0], '%Y-%m-%d')

        return validate_time(start_date_time[2])

    except ValueError:

        print("Incorrect data format, should be YYYY-MM-DD")

        return False


def date_query(creds):
    """
    Function called using no parameters.
    
    Uses a while loop to get the user to input the date and time as given in
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
    
    return False


def title_query(creds):
    """
    Function called using no parameters.
    
    Uses a while loop to get the user to inpute the title of the event 
    as given in the example. 

    Return: String object is returned onces it is of lenght two or more.

    """

    event_title = ''

    event_title = input('Enter title <username>: <problem topic>, e.g: coloots: toy robot five. ').lower().strip().split()

    if(''.join(event_title) == 'y'):
        view_calednar.view_calendar(creds, 'coding.clinic32@gmail.com')
        return title_query(creds)

    if(len(event_title)>=2 and len(event_title[0])>=4):

        return ' '.join(event_title)

    return False
    

def create_slot(creds):
    """
    Function called using the binary pickle object 'creds'. 
    
    Uses a while loop to get the user to enter the correct title.
    
    Uses another while loop to get the user to enter the correct date and time.

    Return: Function has no return value.
    """

    event_title, start_date_time = 1,1

    while event_title and start_date_time  :

        event_title = title_query(creds)

        start_date_time = date_query(creds)
    
        if(event_title and start_date_time ):

<<<<<<< HEAD
<<<<<<< HEAD
            if not creating_slot(event_title, creds, start_date_time):
=======
            if creating_slot(event_title, creds, start_date_time) == False:
>>>>>>> 63f50c2bfba465cd2b7ce44be99384b80705e2cb

                print('Could not create a slot. Please try again.')
                
            return 0

    # return creating_slot(event_title, creds, start_date_time)

=======
            if creating_slot(event_title, creds, start_date_time) == False:

                print('Could not create a slot. Please try again.')
                
            return 0
>>>>>>> cf241b6cb422db7e0961459f488ab894a181f046
