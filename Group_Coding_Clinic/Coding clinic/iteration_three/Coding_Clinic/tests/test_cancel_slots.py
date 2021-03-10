import sys
import unittest
import datetime
import calendar
import datetime
import coding_clinic
from io import StringIO
from unittest.mock import patch
from team32 import make_booking as booking
from googleapiclient.discovery import build
from team32 import create_slots as create_slots
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow


now = datetime.datetime.utcnow().isoformat()+ 'Z'
next_week = datetime.timedelta(days=6)
future = (datetime.datetime.utcnow() + next_week).isoformat() + 'Z'

class MyTestCase(unittest.TestCase):

    @patch('sys.stdin', StringIO("""
 cskosana: testing cancel slots\n2020-12-16 @ 10:00\n\
 cskosana@student.wethinkcode.co.za\ncskosana: testing cancel slots\n\
 2020-12-16 @ 10:30\ncskosana@student.wethinkcode.co.za\n"""))
    def test_cancel_middle_slots(self):
        coding_clinic.create_slot()
        coding_clinic.cancel_slot()
        creds = coding_clinic.function_init()
        service = build('calendar', 'v3', credentials=creds)
        now = datetime.datetime.utcnow().isoformat()+ 'Z'
        events_list = service.events().list(calendarId =\
                                        'coding.clinic32@gmail.com',\
                                        timeMax = future, \
                                        timeMin = now, singleEvents=True,\
                                        orderBy = 'startTime').execute()
        for item in events_list.get('items'):
<<<<<<< HEAD
            self.assertNotEqual(item.get('summary'),'cskosana: testing cancel\
 slots')
=======
            self.assertNotEqual(item.get('summary'),'cskosana: testing cancel slots')
>>>>>>> 63f50c2bfba465cd2b7ce44be99384b80705e2cb
    

    @patch('sys.stdin', StringIO("""cskosana: toy robot fifty\n\
 2020-12-16 @ 12:00\ncskosana@student.wethinkcode.co.za\n"""))
    def test_cancel_slot_with_same_time_as_other(self):
        page_token = None
        # coding_clinic.create_slot()
        coding_clinic.cancel_slot()
        creds = coding_clinic.function_init()
        service = build('calendar', 'v3', credentials=creds)
        now = datetime.datetime.utcnow().isoformat()+ 'Z'
        events_list = service.events().list(calendarId =\
                                        'coding.clinic32@gmail.com',\
                                        timeMax = future, \
                                        timeMin = now, singleEvents=True,\
                                        orderBy = 'startTime').execute()
        for item in events_list.get('items'):
            if item.get('start').get('dateTime') == '2020-12-16T12:00:00+02:00':
                self.assertNotEqual(item.get('summary'),\
                                'cskosana: toy robot fifty')
            

    @patch('sys.stdin', StringIO("""cskosana: toy robot fifty\n\
        2020-12-16 @ 12:00\ncskosana@student.wethinkcode.co.za\n"""))        
    def test_cancel_slot_with_same_name_as_other(self):
        coding_clinic.cancel_slot()
        creds = coding_clinic.function_init()
        service = build('calendar', 'v3', credentials=creds)
        now = datetime.datetime.utcnow().isoformat()+ 'Z'
        events_list = service.events().list(calendarId =\
                                        'coding.clinic32@gmail.com',\
                                        timeMax = future, \
                                        timeMin = now, singleEvents=True,\
                                        orderBy = 'startTime').execute()
        for item in events_list.get('items'):
            if item.get('summary') == 'cskosana: testing cancel slots':
                self.assertNotEqual(item.get('start').get('dateTime'),\
<<<<<<< HEAD
                                    '2020-12-16T12:00:00+02:00')
=======
                                    '2020-12-16T12:00:00+02:00')
>>>>>>> 63f50c2bfba465cd2b7ce44be99384b80705e2cb
