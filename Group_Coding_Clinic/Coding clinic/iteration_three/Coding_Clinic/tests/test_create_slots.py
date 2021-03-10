from team32 import create_slots as create
import unittest
import sys
import datetime
import calendar
import coding_clinic 
from io import StringIO
from unittest.mock import patch
from googleapiclient.discovery import build

now = datetime.datetime.utcnow().isoformat()+ 'Z'
next_week = datetime.timedelta(days=6)
future = (datetime.datetime.utcnow() + next_week).isoformat() + 'Z'

creds = 'coding.clinic32@gmail.com'

class MyTestCase(unittest.TestCase):

    def test_validate_time(self):

        temp_out = StringIO()
        sys.stdout = temp_out

        self.assertTrue(create.validate_time('09:30'))
      
    def test_validate_time_false(self):

        temp_out = StringIO()
        sys.stdout = temp_out

        self.assertFalse(create.validate_time('99:30'))

    def test_validate_date_time_false(self):

        temp_out = StringIO()
        sys.stdout = temp_out

        self.assertFalse(create.validate_date_time('11-12-2020'))
    
    @patch("sys.stdin", StringIO("2020-12-15\n2020-11-03"))
    def test_validate_date_time(self):

        with patch("sys.stdout", new=StringIO()) as out:
            create.validate_date_time('time')
            output = out.getvalue().strip()

        self.assertEqual(output, """Incorrect data format, should be YYYY-MM-DD""")

    @patch("sys.stdin", StringIO('14:00 @ 2020-01-01'))
    def test_date_query_false(self):

        temp_out = StringIO()
        sys.stdout = temp_out

        self.assertFalse(create.date_query('14:00 @ 2020-01-01'))

    @patch("sys.stdin", StringIO("2020-01-01 @ 14:00"))
    def test_date_query(self):

        with patch("sys.stdout", new=StringIO()) as out:
            create.date_query('date and time')
            output = out.getvalue().strip()
        self.assertFalse(0)

    @patch("sys.stdin", StringIO('Toy Robot'))
    def test_title_query(self):

        temp_out = StringIO()
        sys.stdout = temp_out

        self.assertFalse(create.title_query('Toy Robot'))


    @patch("sys.stdin", StringIO('Toy Robot'))
    def test_title_query_(self):

        with patch("sys.stdout", new=StringIO()) as out:
            create.title_query('Event Title')
            output = out.getvalue().strip()
        self.assertFalse(0)

    @patch('sys.stdin', StringIO("""
coloots: toy robot nine\n2020-12-17 @ 14:00\n\
coloots@student.wethinkcode.co.za\n"""))
    def test_volunteer_create_slot(self):
        coding_clinic.create_slot()
        validate_date_time = '2020-12-17 @ 14:00'
        creds = coding_clinic.function_init()
        service = build('calendar', 'v3', credentials=creds)
        now = datetime.datetime.utcnow().isoformat()+ 'Z'
        events_list = service.events().list(calendarId =\
                                        'coding.clinic32@gmail.com',\
                                        timeMax = future, \
                                        timeMin = now, singleEvents=True,\
                                        orderBy = 'startTime').execute()
        for item in events_list.get('items'):
            if item.get('summary') == 'coloots: toy robot nine'\
                and item.get('start').get('dateTime').get('date') == '2020-12-17':
                self.assertEqual(item.get('summary'), 'coloots: toy robot nine')
