import unittest
import robot
import sys
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import patch
import random
from world import obstacles

class Test_robot(unittest.TestCase):
    @patch("sys.stdin", StringIO("hal\noff\n"))
    def test_off_(self):
        random.randint = lambda x,y: 0
        with patch("sys.stdout", StringIO())as out:
            robot.robot_start()
        self.assertEqual("""What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next? hal: Shutting down..""", out.getvalue().strip())

    
    @patch("sys.stdin", StringIO("hal\nOFF\n"))
    def test_OFF(self):
        random.randint = lambda x,y: 0
        with patch("sys.stdout", StringIO())as out:
            robot.robot_start()
        self.assertEqual("""What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next? hal: Shutting down..""", out.getvalue().strip())


    @patch("sys.stdin", StringIO("hal\nhelp\noff\n"))
    def test_help_off(self):
        random.randint = lambda x,y: 0
        with patch("sys.stdout", StringIO())as out:
            robot.robot_start()
        self.assertEqual("""What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next? I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replays all movement commands from history [FORWARD, BACK, RIGHT, LEFT, SPRINT]

 > hal now at position (0,0).
hal: What must I do next? hal: Shutting down..""", out.getvalue().strip())


    @patch("sys.stdin", StringIO("hal\nasd sd\noff\n"))
    def test_wrong_off(self):
        random.randint = lambda x,y: 0
        with patch("sys.stdout", StringIO())as out:
            robot.robot_start()    
        self.assertEqual("""What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next? hal: Sorry, I did not understand 'asd sd'.
hal: What must I do next? hal: Shutting down..""", out.getvalue().strip())


    @patch("sys.stdin", StringIO("hal\nforward 10\noff\n"))
    def test_forward_off(self):
        random.randint = lambda x,y: 0
        with patch("sys.stdout", StringIO())as out:
            robot.robot_start()
        self.assertEqual("""What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal moved forward by 10 steps.
 > hal now at position (0,10).
hal: What must I do next? hal: Shutting down..""", out.getvalue().strip())


    @patch("sys.stdin", StringIO("hal\nforward 10\nback 5\noff\n"))
    def test_forward_back_off(self):
        random.randint = lambda x,y: 0
        with patch("sys.stdout", StringIO())as out:
            robot.robot_start()
        self.assertEqual("""What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal moved forward by 10 steps.
 > hal now at position (0,10).
hal: What must I do next?  > hal moved back by 5 steps.
 > hal now at position (0,5).
hal: What must I do next? hal: Shutting down..""", out.getvalue().strip())


    @patch("sys.stdin", StringIO("hal\nright\noff\n"))
    def test_right_off(self):
        random.randint = lambda x,y: 0
        with patch("sys.stdout", StringIO())as out:
            robot.robot_start()
        self.assertEqual("""What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal turned right.
 > hal now at position (0,0).
hal: What must I do next? hal: Shutting down..""", out.getvalue().strip())


    @patch("sys.stdin", StringIO("hal\nright\nforward 10\noff\n"))
    def test_right_forward_off(self):
        random.randint = lambda x,y: 0
        with patch("sys.stdout", StringIO())as out:
            robot.robot_start()
        self.assertEqual("""What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal turned right.
 > hal now at position (0,0).
hal: What must I do next?  > hal moved forward by 10 steps.
 > hal now at position (10,0).
hal: What must I do next? hal: Shutting down..""", out.getvalue().strip())


    @patch("sys.stdin", StringIO("hal\nright\nforward 10\nback 5\noff\n"))
    def test_right_forward_back_off(self):
        random.randint = lambda x,y: 0
        with patch("sys.stdout", StringIO())as out:
            robot.robot_start()
        self.assertEqual("""What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal turned right.
 > hal now at position (0,0).
hal: What must I do next?  > hal moved forward by 10 steps.
 > hal now at position (10,0).
hal: What must I do next?  > hal moved back by 5 steps.
 > hal now at position (5,0).
hal: What must I do next? hal: Shutting down..""", out.getvalue().strip())


    @patch("sys.stdin", StringIO("hal\nleft\noff\n"))
    def test_left_off(self):
        random.randint = lambda x,y: 0
        with patch("sys.stdout", StringIO())as out:
            robot.robot_start()
        self.assertEqual("""What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal turned left.
 > hal now at position (0,0).
hal: What must I do next? hal: Shutting down..""", out.getvalue().strip())


    @patch("sys.stdin", StringIO("hal\nleft\nforward 10\noff\n"))
    def test_left_forward_off(self):
        random.randint = lambda x,y: 0
        with patch("sys.stdout", StringIO())as out:
            robot.robot_start()
        self.assertEqual("""What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal turned left.
 > hal now at position (0,0).
hal: What must I do next?  > hal moved forward by 10 steps.
 > hal now at position (-10,0).
hal: What must I do next? hal: Shutting down..""", out.getvalue().strip())


    @patch("sys.stdin", StringIO("hal\nleft\nforward 10\nbakc 5\noff\n"))
    def test_left_forward_bakc_off(self):
        random.randint = lambda x,y: 0
        with patch("sys.stdout", StringIO())as out:
            robot.robot_start()
        self.assertEqual("""What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal turned left.
 > hal now at position (0,0).
hal: What must I do next?  > hal moved forward by 10 steps.
 > hal now at position (-10,0).
hal: What must I do next? hal: Sorry, I did not understand 'bakc 5'.
hal: What must I do next? hal: Shutting down..""", out.getvalue().strip())


    @patch("sys.stdin", StringIO("hal\nleft\nforward 10\nback 5\noff\n"))
    def test_left_forward_back_off(self):
        random.randint = lambda x,y: 0
        with patch("sys.stdout", StringIO())as out:
            robot.robot_start()
        self.assertEqual("""What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal turned left.
 > hal now at position (0,0).
hal: What must I do next?  > hal moved forward by 10 steps.
 > hal now at position (-10,0).
hal: What must I do next?  > hal moved back by 5 steps.
 > hal now at position (-5,0).
hal: What must I do next? hal: Shutting down..""", out.getvalue().strip())


    @patch("sys.stdin", StringIO("hal\nforward 10\nback 5\nreplay\noff\n"))
    def test_forward_back_replay_off(self):
        random.randint = lambda x,y: 0
        with patch("sys.stdout", StringIO())as out:
            robot.robot_start()
        self.assertEqual("""What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal moved forward by 10 steps.
 > hal now at position (0,10).
hal: What must I do next?  > hal moved back by 5 steps.
 > hal now at position (0,5).
hal: What must I do next?  > hal moved forward by 10 steps.
 > hal now at position (0,15).
 > hal moved back by 5 steps.
 > hal now at position (0,10).
 > hal replayed 2 commands.
 > hal now at position (0,10).
hal: What must I do next? hal: Shutting down..""", out.getvalue().strip())


    @patch("sys.stdin", StringIO("hal\nforward 10\nback 5\nreplay sd\noff\n"))
    def test_forward_back_replay_wrong_off(self):
        random.randint = lambda x,y: 0
        with patch("sys.stdout", StringIO())as out:
            robot.robot_start()
        self.assertEqual("""What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal moved forward by 10 steps.
 > hal now at position (0,10).
hal: What must I do next?  > hal moved back by 5 steps.
 > hal now at position (0,5).
hal: What must I do next? hal: Sorry, I did not understand 'replay sd'.
hal: What must I do next? hal: Shutting down..""", out.getvalue().strip())


    @patch("sys.stdin", StringIO("hal\nforward 1\nforward 2\nreplay silent\noff"))
    def test_forward_replay_silent_off(self):
        random.randint = lambda x,y: 0
        with patch("sys.stdout", StringIO())as out:
            robot.robot_start()
        self.assertEqual("""What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal moved forward by 1 steps.
 > hal now at position (0,1).
hal: What must I do next?  > hal moved forward by 2 steps.
 > hal now at position (0,3).
hal: What must I do next?  > hal replayed 2 commands silently.
 > hal now at position (0,6).
hal: What must I do next? hal: Shutting down..""", out.getvalue().strip())


    @patch("sys.stdin", StringIO("hal\nforward 1\nforward 2\nreplay silent asd\noff"))
    def test_forward_replay_silent_wrong_off(self):
        random.randint = lambda x,y: 0
        with patch("sys.stdout", StringIO())as out:
            robot.robot_start()
        self.assertEqual("""What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal moved forward by 1 steps.
 > hal now at position (0,1).
hal: What must I do next?  > hal moved forward by 2 steps.
 > hal now at position (0,3).
hal: What must I do next? hal: Sorry, I did not understand 'replay silent asd'.
hal: What must I do next? hal: Shutting down..""", out.getvalue().strip())


    @patch("sys.stdin", StringIO("hal\nforward 1\nforward 2\nreplay reversed\noff\n"))
    def test_forward_replay_reversed_off(self):
        random.randint = lambda x,y: 0
        with patch("sys.stdout", StringIO())as out:
            robot.robot_start()
        self.assertEqual("""What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal moved forward by 1 steps.
 > hal now at position (0,1).
hal: What must I do next?  > hal moved forward by 2 steps.
 > hal now at position (0,3).
hal: What must I do next?  > hal moved forward by 2 steps.
 > hal now at position (0,5).
 > hal moved forward by 1 steps.
 > hal now at position (0,6).
 > hal replayed 2 commands in reverse.
 > hal now at position (0,6).
hal: What must I do next? hal: Shutting down..""", out.getvalue().strip())


    @patch("sys.stdin", StringIO("hal\nforward 1\nforward 2\nreplay reversed asd\noff\n"))
    def test_forward_replay_reversed_wwrong_off(self):
        random.randint = lambda x,y: 0
        with patch("sys.stdout", StringIO())as out:
            robot.robot_start()
        self.assertEqual("""What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal moved forward by 1 steps.
 > hal now at position (0,1).
hal: What must I do next?  > hal moved forward by 2 steps.
 > hal now at position (0,3).
hal: What must I do next? hal: Sorry, I did not understand 'replay reversed asd'.
hal: What must I do next? hal: Shutting down..""", out.getvalue().strip())

    
    @patch("sys.stdin", StringIO("hal\nforward 2\nforward 1\nreplay reversed silent\noff\n"))
    def test_forward_replay_reversed_silent_off(self):
        random.randint = lambda x,y: 0
        with patch("sys.stdout", StringIO())as out:
            robot.robot_start()
        self.assertEqual("""What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal moved forward by 2 steps.
 > hal now at position (0,2).
hal: What must I do next?  > hal moved forward by 1 steps.
 > hal now at position (0,3).
hal: What must I do next?  > hal replayed 2 commands in reverse silently.
 > hal now at position (0,6).
hal: What must I do next? hal: Shutting down..""", out.getvalue().strip())


    @patch("sys.stdin", StringIO("hal\nforward 2\nforward 1\nreplay reversed silent asd\noff\n"))
    def test_forward_replay_reversed_silent_wrong_off(self):
        random.randint = lambda x,y: 0
        with patch("sys.stdout", StringIO())as out:
            robot.robot_start()
        self.assertEqual("""What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal moved forward by 2 steps.
 > hal now at position (0,2).
hal: What must I do next?  > hal moved forward by 1 steps.
 > hal now at position (0,3).
hal: What must I do next? hal: Sorry, I did not understand 'replay reversed silent asd'.
hal: What must I do next? hal: Shutting down..""", out.getvalue().strip())


    @patch("sys.stdin", StringIO("hal\nforward 1\nforward 2\nforward 3\nreplay 2\noff\n"))
    def test_forward_replay_n_off(self):
        random.randint = lambda x,y: 0
        with patch("sys.stdout", StringIO())as out:
            robot.robot_start()
        self.assertEqual("""What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal moved forward by 1 steps.
 > hal now at position (0,1).
hal: What must I do next?  > hal moved forward by 2 steps.
 > hal now at position (0,3).
hal: What must I do next?  > hal moved forward by 3 steps.
 > hal now at position (0,6).
hal: What must I do next?  > hal moved forward by 2 steps.
 > hal now at position (0,8).
 > hal moved forward by 3 steps.
 > hal now at position (0,11).
 > hal replayed 2 commands.
 > hal now at position (0,11).
hal: What must I do next? hal: Shutting down..""", out.getvalue().strip())


    @patch("sys.stdin", StringIO("hal\nforward 1\nforward 2\nforward 3\nreplay asd\noff\n"))
    def test_forward_replay_wrong_off(self):
        random.randint = lambda x,y: 0
        with patch("sys.stdout", StringIO())as out:
            robot.robot_start()
        self.assertEqual("""What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal moved forward by 1 steps.
 > hal now at position (0,1).
hal: What must I do next?  > hal moved forward by 2 steps.
 > hal now at position (0,3).
hal: What must I do next?  > hal moved forward by 3 steps.
 > hal now at position (0,6).
hal: What must I do next? hal: Sorry, I did not understand 'replay asd'.
hal: What must I do next? hal: Shutting down..""", out.getvalue().strip())

    
    @patch("sys.stdin", StringIO("hal\nforward 3\nforward 2\nforward 1\nreplay 3-1\noff\n"))
    def test_forward_replay_limit(self):
        random.randint = lambda x,y: 0
        with patch("sys.stdout", StringIO())as out:
            robot.robot_start()
        self.assertEqual("""What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal moved forward by 3 steps.
 > hal now at position (0,3).
hal: What must I do next?  > hal moved forward by 2 steps.
 > hal now at position (0,5).
hal: What must I do next?  > hal moved forward by 1 steps.
 > hal now at position (0,6).
hal: What must I do next?  > hal moved forward by 3 steps.
 > hal now at position (0,9).
 > hal moved forward by 2 steps.
 > hal now at position (0,11).
 > hal replayed 2 commands.
 > hal now at position (0,11).
hal: What must I do next? hal: Shutting down..""", out.getvalue().strip())


    @patch("sys.stdin", StringIO("hal\nforward 3\nforward 2\nforward 1\nreplay 3--1\noff\n"))
    def test_forward_replay_limit_wrong(self):
        random.randint = lambda x,y: 0
        f = StringIO()
        with redirect_stdout(f):
            robot.robot_start()
        output = f.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal moved forward by 3 steps.
 > hal now at position (0,3).
hal: What must I do next?  > hal moved forward by 2 steps.
 > hal now at position (0,5).
hal: What must I do next?  > hal moved forward by 1 steps.
 > hal now at position (0,6).
hal: What must I do next? hal: Sorry, I did not understand 'replay 3--1'.
hal: What must I do next? hal: Shutting down..""", output)


if __name__ == "__main__":
    unittest.main()