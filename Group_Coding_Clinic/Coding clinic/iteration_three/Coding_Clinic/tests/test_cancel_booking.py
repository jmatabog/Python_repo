import unittest
import sys
from io import StringIO
from unittest.mock import patch
from team32 import cancel_booking as cancel_booking

creds = 'coding.clinic32@gmail.com'
class MyTestCase(unittest.TestCase):
    def test_validate_time(self):
        self.assertTrue(cancel_booking.validate_time('09:30'))
        self.assertFalse(cancel_booking.validate_time('9:30am'))
        self.assertFalse(cancel_booking.validate_time('half past nine'))

    @patch("sys.stdin", StringIO("09:30\n9:30am\n9:30\nhalf past nine"))
    def test_validate_time_iter_two(self):
        with patch("sys.stdout", new=StringIO()) as out:
            cancel_booking.validate_time('time')
            output = out.getvalue().strip()
        self.assertEqual(output, """Incorrect time format, should be H:M""")
 
    
    def test_validate_date_time_iter_one(self):
        self.assertFalse(cancel_booking.validate_date_time('11-12-2020'))
    
    @patch("sys.stdin", StringIO("2020-12-15\n2020-11-03"))
    def test_validate_date_time_iter_two(self):
        with patch("sys.stdout", new=StringIO()) as out:
            cancel_booking.validate_date_time('time')
            output = out.getvalue().strip()
        self.assertEqual(output, """Incorrect data format, should be YYYY-MM-DD""")

    @patch("sys.stdin", StringIO("2020-01-----01 @ 14:00"))
    def test_date_query_iter_one(self):
        self.assertFalse(cancel_booking.date_query('14:00 @ 2020-01-01'))

    @patch("sys.stdin", StringIO("2020-01-01 @ 14:00"))
    def test_date_query_iter_two(self):
        with patch("sys.stdout", new=StringIO()) as out:
            return_result = cancel_booking.date_query('date and time')
            output = out.getvalue().strip()
        self.assertTrue(return_result)
            
    @patch("sys.stdin", StringIO("000obot"))
    def test_title_query_iter_one(self):
        self.assertFalse(cancel_booking.title_query(''))
    
    
    @patch("sys.stdin", StringIO('Toy Robot\n Toy Robot 5'))
    def test_title_query_two(self):
        with patch("sys.stdout", new=StringIO()) as out:
            return_result = cancel_booking.title_query('Event Title')
            output = out.getvalue().strip()
        self.assertFalse(return_result)


    def test_update_event(self):
        pass
    
if __name__ == "__main__":
    unittest.main()