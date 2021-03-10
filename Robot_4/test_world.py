import unittest
from world.text import world
from unittest.mock import patch
import sys
from io import StringIO
# from .. import obstacles

class test_world(unittest.TestCase):
    @patch("sys.stdin", StringIO())
    def test_show_position(self):
        with patch("sys.stdout", StringIO())as out:
            world.show_position("HAL")
        self.assertEqual("> HAL now at position (0,0).",out.getvalue().strip())

    def test_is_position_allowed(self):
        self.assertEqual(True, world.is_position_allowed(5,10))
        self.assertEqual(False, world.is_position_allowed(101,201))

    def test_update_positions(self):
        self.assertEqual(True,world.update_position(5))


if __name__ == "__main__":
    unittest.main()