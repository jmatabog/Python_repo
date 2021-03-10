import unittest
import robot
from unittest.mock import patch
from contextlib import redirect_stdout
from test_base import captured_io
from io import StringIO

class MyRobotTestCases(unittest.TestCase):
    @patch("sys.stdin", StringIO("HAL\n"))
    def test_get_name_robot(self):
        output = "HAL"
        self.assertEqual(robot.get_robot_name(), output)
    
    
    @patch("sys.stdin", StringIO("HAL\njump up\noff\n"))
    def test_off(self):
        f = StringIO()
        with redirect_stdout(f):
            robot.robot_start()
        output = f.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next? HAL: Sorry, I did not understand 'jump up'.
HAL: What must I do next? HAL: Shutting down..""", output)
    
    
    @patch("sys.stdin", StringIO("HAL\nhelp\noff\n"))
    def test_help(self):
        f = StringIO()
        with redirect_stdout(f):
            robot.robot_start()
        output = f.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next? I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replay all the moves and commands made to the robot

 > HAL now at position (0,0).
HAL: What must I do next? HAL: Shutting down..""", output)


    @patch("sys.stdin", StringIO("HAL\nforward 10\noff\n"))
    def test_forward(self):
        f = StringIO()
        with redirect_stdout(f):
            robot.robot_start()
        output = f.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next? HAL: Shutting down..""", output)

    
    @patch("sys.stdin", StringIO("HAL\nforward 10\nforward 5\noff\n"))
    def test_forward_update(self):
        f = StringIO()
        with redirect_stdout(f):
            robot.robot_start()
        output = f.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,15).
HAL: What must I do next? HAL: Shutting down..""", output)


    @patch("sys.stdin", StringIO("HAL\nright\noff\n"))
    def test_right(self):
        f = StringIO()
        with redirect_stdout(f):
            robot.robot_start()
        output = f.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (0,0).
HAL: What must I do next? HAL: Shutting down..""", output)

    @patch("sys.stdin", StringIO("HAL\nright\noff\n"))
    def test_turn_right(self):
        f = StringIO()
        with redirect_stdout(f):
            robot.robot_start()
        output = f.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (0,0).
HAL: What must I do next? HAL: Shutting down..""", output.strip())


    @patch("sys.stdin", StringIO("HAL\nleft\noff\n"))
    def test_turn_left(self):
        f = StringIO()
        with redirect_stdout(f):
            robot.robot_start()
        output = f.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL turned left.
 > HAL now at position (0,0).
HAL: What must I do next? HAL: Shutting down..""", output)


    @patch("sys.stdin", StringIO("HAL\nforward 10\noff\n"))
    def test_turn_left_forward(self):
        f = StringIO()
        with redirect_stdout(f):
            robot.robot_start()
        output = f.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next? HAL: Shutting down..""", output)


    @patch("sys.stdin", StringIO("HAL\nback 10\noff\n"))
    def test_back(self):
        f = StringIO()
        with redirect_stdout(f):
            robot.robot_start()
        output = f.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved back by 10 steps.
 > HAL now at position (0,-10).
HAL: What must I do next? HAL: Shutting down..""", output)


    @patch("sys.stdin", StringIO("HAL\nback 10\nback 5\noff\n"))
    def test_back_update(self):
        f = StringIO()
        with redirect_stdout(f):
            robot.robot_start()
        output = f.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved back by 10 steps.
 > HAL now at position (0,-10).
HAL: What must I do next?  > HAL moved back by 5 steps.
 > HAL now at position (0,-15).
HAL: What must I do next? HAL: Shutting down..""", output)


    @patch("sys.stdin", StringIO("HAL\nright\nback 10\noff\n"))
    def test_turn_right_back(self):
        f = StringIO()
        with redirect_stdout(f):
            robot.robot_start()
        output = f.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (0,0).
HAL: What must I do next?  > HAL moved back by 10 steps.
 > HAL now at position (-10,0).
HAL: What must I do next? HAL: Shutting down..""", output)


    @patch("sys.stdin", StringIO("HAL\nleft\nback 10\noff\n"))
    def test_turn_left_forward(self):
        f = StringIO()
        with redirect_stdout(f):
            robot.robot_start()
        output = f.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL turned left.
 > HAL now at position (0,0).
HAL: What must I do next?  > HAL moved back by 10 steps.
 > HAL now at position (10,0).
HAL: What must I do next? HAL: Shutting down..""", output)


    @patch("sys.stdin", StringIO("HAL\nforward 210\noff\n"))
    def test_limit(self):
        f = StringIO()
        with redirect_stdout(f):
            robot.robot_start()
        output = f.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next? HAL: Sorry, I cannot go outside my safe zone.
 > HAL now at position (0,0).
HAL: What must I do next? HAL: Shutting down..""", output)


    @patch("sys.stdin", StringIO("HAL\nback 210\noff\n"))
    def test_limit_back(self):
        f = StringIO()
        with redirect_stdout(f):
            robot.robot_start()
        output = f.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next? HAL: Sorry, I cannot go outside my safe zone.
 > HAL now at position (0,0).
HAL: What must I do next? HAL: Shutting down..""", output)


    @patch("sys.stdin", StringIO("HAL\nforward 10\nforward 5\nreplay\noff\n"))
    def test_replay(self):
        f = StringIO()
        with redirect_stdout(f):
            robot.robot_start()
        output = f.getvalue().strip()
        self.assertTrue("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,15).
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,25).
 > HAL moved forward by 5 steps.
 > HAL now at position (0,30).
 > HAL replayed 2 commands.
 > HAL now at position (0,30).
HAL: What must I do next? HAL: Shutting down..""", output)
    

    @patch("sys.stdin", StringIO("HAL\nforward 10\nforward 5\nreplay silent\noff\n"))
    def test_replay_silent(self):
        f = StringIO()
        with redirect_stdout(f):
            robot.robot_start()
        output = f.getvalue().strip()
        self.assertTrue("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,15).
HAL: What must I do next?  > HAL replayed 2 commands silently.
 > HAL now at position (0,30).
HAL: What must I do next? HAL: Shutting down..""", output)


    @patch("sys.stdin", StringIO("HAl\nforward 10\nforward 5\nreplay reversed silent\noff\n"))
    def test_replay_reversed_silent(self):
        with patch("sys.stdout", StringIO())as out:
            robot.robot_start()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,15).
HAL: What must I do next?  > HAL replayed 2 commands in reverse silently.
 > HAL now at position (0,30).
HAL: What must I do next? HAL: Shutting down..""", out.getvalue().strip())
    

    @patch("sys.stdin", StringIO("HAL\nforward 10\nforward 5\nreplay 1\noff\n"))
    def test_replay_1(self):
        f = StringIO()
        with redirect_stdout(f):
            robot.robot_start()
        output = f.getvalue().strip()
        self.assertTrue("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,15).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,20).
 > HAL replayed 1 commands.
 > HAL now at position (0,20).
HAL: What must I do next? HAL: Shutting down..""", output)
     

    @patch("sys.stdin", StringIO("HAL\nforward 3\nforward 2\nforward 1\nreplay 3-1\noff\n"))
    def test_replay_n_m(self):
        f = StringIO()
        with redirect_stdout(f):
            robot.robot_start()
        output = f.getvalue().strip()
        self.assertTrue("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 3 steps.
 > HAL now at position (0,3).
HAL: What must I do next?  > HAL moved forward by 2 steps.
 > HAL now at position (0,5).
HAL: What must I do next?  > HAL moved forward by 1 steps.
 > HAL moved forward by 3 steps.
 > HAL now at position (0,9).
 > HAL moved forward by 2 steps.
 > HAL now at position (0,11)
 > HAL replayed 2 commands.
 > HAL now at position (0,11).
HAL: What must I do next? HAL: Shutting down..""", output)
if __name__ == "__main__":
    unittest.main()