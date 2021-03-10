import unittest
import mastermind
import sys
from unittest.mock import patch
from io import StringIO
class testing_mastermind(unittest.TestCase):

    def test_create_code(self):
        x = mastermind.create_code()
        for i in range(100):
            self.assertEqual(4, len(x))
            for i in range(4):
                self.assertIn(x[i], range(1,9))


    def test_check_correctness(self):
        self.assertEqual(True, mastermind.check_correctness(12, 4))
        self.assertEqual(False, mastermind.check_correctness(12, 3))


    @patch("sys.stdin", StringIO("12345\n1234\n"))
    def test_get_input(self):
        original = sys.stdout
        new_string = StringIO()
        j = mastermind.get_user_input()
        output = "Input 4 digit code: Please enter exactly 4 digits.\nInput 4 digits code: "
        sys.stdout = original
        self.assertEqual("Input 4 digit code: Please enter exactly 4 digits.\nInput 4 digits code: ", output)


    @patch("sys.stdin", StringIO("1235\n2468\n1234"))
    def test_take_turns(self):
        self.assertEqual(mastermind.take_turn([1,2,3,4]),(3,0))
        self.assertEqual(mastermind.take_turn([1,2,3,4]),(0,2))
        self.assertEqual(mastermind.take_turn([1,2,3,4]),(4,0))


if __name__ == "__main__":
    unittest.main()