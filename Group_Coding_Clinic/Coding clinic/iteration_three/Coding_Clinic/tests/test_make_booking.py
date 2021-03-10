from team32 import make_booking as booking
import unittest
import sys
from io import StringIO
from unittest.mock import patch

<<<<<<< HEAD
=======

>>>>>>> cf241b6cb422db7e0961459f488ab894a181f046
class MyTestCase(unittest.TestCase):
    def test_validate_time_format(self):
        self.assertTrue(booking.validate_time('12:00'))
        self.assertTrue(booking.validate_time('00:00'))
        self.assertFalse(booking.validate_time('12am'))
        self.assertFalse(booking.validate_time('12'))
        self.assertFalse(booking.validate_time('twelve'))


    @patch("sys.stdin", StringIO("12:00\n00:00\n12am\n12\ntwelve"))
    def test_mock_input_for_validate_time_format_(self):
        with patch("sys.stdout", new=StringIO()) as out:
            booking.validate_time('time')
            output = out.getvalue().strip()
        self.assertEqual(output, """Incorrect time format, should be H:M""")


    def test_validate_date_time_format(self):
<<<<<<< HEAD
        # self.assertTrue(booking.validate_date_time('2020-01-01'))
        # self.assertTrue(booking.validate_date_time('2020-12-03'))
=======
        self.assertFalse(booking.validate_date_time('2020-01-01'))
        self.assertFalse(booking.validate_date_time('2020-12-03'))
>>>>>>> cf241b6cb422db7e0961459f488ab894a181f046
        pass


    @patch("sys.stdin", StringIO("2020-01-01\n"))
    def test_mock_input_for_validate_date_time_format_(self):
        with patch("sys.stdout", new=StringIO()) as out:
            booking.validate_date_time('time')
            output = out.getvalue().strip()
        print(output)
<<<<<<< HEAD
        # self.assertEqual(output, """Incorrect date format, should be YYYY-MM-DD""")




=======
        self.assertEqual(output, """Incorrect date format, should be YYYY-MM-DD\
""")
>>>>>>> cf241b6cb422db7e0961459f488ab894a181f046

if __name__ == "__main__":
    unittest.main()
