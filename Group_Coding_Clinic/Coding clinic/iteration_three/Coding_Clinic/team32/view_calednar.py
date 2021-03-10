from terminaltables import SingleTable, AsciiTable, DoubleTable
import datetime
import calendar
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from termcolor import colored

event_dict = {"Date": [], "Time":[],"Event":[], "Color": []}

def get_calendar_service(creds, calendar_Id):

    """
    This is to get all the evnts details of the Google calendar,
    which would use for dispalying.
    This is used to retreive all the information from the 
    module that calls all the google events.
    It does this through the imports, where a dictionary is returned.
    """

    service = build('calendar', 'v3', credentials=creds)

    now = datetime.datetime.utcnow().isoformat()+ 'Z'

    next_week = datetime.timedelta(days=6)

    future = (datetime.datetime.utcnow() + next_week).isoformat() + 'Z'

    events_result = service.events().list(calendarId=calendar_Id,timeMax=future,
                                        timeMin=now, singleEvents=True,
                                        orderBy='startTime').execute()

    events = events_result.get('items', [])
    
    if not events:
        print('No upcoming events found.')
        
    for event in events:
        
        if 'attendees' in event:
        
            limit = event['start'].get('dateTime',\
                event['start'].get('date'))[11:16]

            if (limit >= '08:00' and limit < '18:00') :
            
                day = event['start'].get('dateTime',\
                    event['start'].get('date'))[:19] + 'Z'
            
                day_name = datetime.datetime.strptime(day, '%Y-%m-%dT%H:%M:%SZ')

                start = event['start'].get('dateTime',\
                    event['start'].get('date'))[:16] +'-'

                start = start.replace('T', " Time ")
            

                end = event['end'].get('dateTime',\
                    event['start'].get('date'))[11:16]
            
                event_dict["Date"].append(start[:10])

                event_dict["Time"].append((start+end)[16:27])

                event_dict["Event"].append(event['summary'])
                if len(event["attendees"]) < 2 and len(event["attendees"]) > 0:
                    """Event available """
                    event_dict["Color"].append('green')
                elif len(event["attendees"]) >= 2  :
                    """Not avail"""
                    event_dict["Color"].append('red')
                elif len(event["attendees"])==0:
                    event_dict['Color'].append('blank')
        else:

            limit = event['start'].get('dateTime', \
            event['start'].get('date'))[11:16]

            if (limit >= '08:00' and limit < '18:00') :
            
                day = event['start'].get('dateTime',\
                    event['start'].get('date'))[:19] + 'Z'
            
                day_name = datetime.datetime.strptime(day, '%Y-%m-%dT%H:%M:%SZ')

                start = event['start'].get('dateTime',\
                 event['start'].get('date'))[:16] +'-'

                start = start.replace('T', " Time ")
            

                end = event['end'].get('dateTime',\
                 event['start'].get('date'))[11:16]
            
                event_dict["Date"].append(start[:10])

                event_dict["Time"].append((start+end)[16:27])

                event_dict["Event"].append(event['summary'])

                event_dict['Color'].append('blank')


    return(event_dict)


def date():

    """
    This is used to display the specific date of that day and display it 
    on the calendar.
    """

    theday = datetime.date.today()

    weekday = theday.isoweekday()

    start = theday 

    dates = [start + datetime.timedelta(days=d) for d in range(7)]

    dates = [str(d) for d in dates]

    return dates


def date_seven(start_date, end_date):

    """
    This functions is used to set a limit to the days to be used.
    """

    seven_days = (end_date-start_date).days

    for i in range(seven_days):
        yield start_date + datetime.timedelta(days= i)


def week_day(i):

    """
    This specifies the days of the week to be shown in the calendar.
    """

    current_week_day = []

    for j in i:

        date = j.date()

        day = calendar.day_name[date.weekday()]

        current_week_day.append(day)

    return current_week_day


def print_cal(current_week_day, dates, event):

    """
    This is used for printing of the calendar, where it would show 
    from that specific day.
    """

    list_cal =[
        [colored("Time", 'white', attrs=['bold']),\
colored(current_week_day[0]+" " +dates[0], 'white', attrs=['bold']),\
colored(current_week_day[1]+" "+dates[1], 'white', attrs=['bold']),\
colored(current_week_day[2]+" "+dates[2], 'white', attrs=['bold']),\
colored(current_week_day[3]+ " "+dates[3], 'white', attrs=['bold']),\
colored(current_week_day[4]+" "+dates[4], 'white', attrs=['bold']),\
colored(current_week_day[5]+" "+dates[5], 'white', attrs=['bold']),\
colored(current_week_day[6]+ " " +dates[6], 'white', attrs=['bold'])],
        ["08:00", "", "", "", "", "", "",""],
        ["08:30", "", "", "", "", "", "",""],
        ["09:00",  "", "", "", "", "","",""],
        ["09:30", "", "", "", "", "","",""],
        ["10:00", "", "", "", "", "","",""],
        ["10:30", "", "", "", "", "","",""],
        ["11:00", "", "", "", "", "","",""],
        ["11:30", "", "", "", "", "","",""],
        ["12:00", "", "", "", "", "","",""],
        ["12:30", "", "", "", "", "","",""],
        ["13:00", "", "", "", "", "","",""],
        ["13:30", "", "", "", "", "","",""],
        ["14:00", "", "", "", "", "","",""],
        ["14:30", "", "", "", "", "","",""],
        ["15:00", "", "", "", "", "","",""],
        ["15:30", "", "", "", "", "","",""],  
        ["16:00", "", "", "", "", "","",""],
        ["16:30", "", "", "", "", "","",""],
        ["17:00", "", "", "", "", "","",""],
        ["17:30", "", "", "", "", "","",""],
        ["18:00", "", "", "", "", "","",""]
    ]

    x_list = [i for key, value in event.items() for date in value \
for i in range(len(list_cal[0])) if date in list_cal[0][i] if key == 'Date']
        
    y_list = [i for key, value in event.items() for time in value  \
for i in range(21) if time[:5] >= list_cal[i][0] and\
     time[:5] < list_cal[i+1][0] if key == 'Time']
   
    events = [event for key, value in event.items() for event in value \
if key == 'Event']

    for cal_app in (x_list):
        for i in range(len(events)):
            if event["Color"][i] == 'red':
                list_cal[y_list[i]][x_list[i]] = colored((events[i] +' '+\
                     event['Time'][i]), 'red', attrs=['bold'])
            elif event["Color"][i] == 'green':
                list_cal[y_list[i]][x_list[i]] = colored((events[i] +' '+\
                     event['Time'][i]), 'green',attrs=['bold'])
            elif event["Color"][i] == 'blank':
                list_cal[y_list[i]][x_list[i]] = colored((events[i] +' '+\
                     event['Time'][i]), 'green',attrs=['bold'])
            
    cal = AsciiTable(list_cal)

    cal.inner_row_border = True

    print(cal.table)


def view_calendar(creds, calendar_Id):

    """
    All the information needed in this module to be imported in 
    coding_clinic.py.
    """

    event = get_calendar_service(creds,calendar_Id)

    today = datetime.datetime.today()

    end  = today + datetime.timedelta(days= 7)

    i = list(date_seven(today, end))

    current_week_day = week_day(i)

    dates = date()
    
    print_cal(current_week_day, dates, event)

