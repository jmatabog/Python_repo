import unittest

class tryingtest(unittest.TestCase):
    def test_date(self):
        vandag = datetime.date.today()
        weekdays = vandag.isoweek()
        self.assertTrue(vandag == datetime.date.today())


if __name__ == '__main__':
    unittest.main()