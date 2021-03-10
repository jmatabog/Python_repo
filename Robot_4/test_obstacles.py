import unittest
from world import obstacles
import random

class Test_obstacles(unittest.TestCase):
    
    def test_is_position_blocked(self):
        obstacles.obs_list = [(1,1)]
        self.assertEqual(False, obstacles.is_position_blocked(6,8))
        self.assertEqual(True, obstacles.is_position_blocked(2,2))


    def test_is_path_blocked(self):
        obstacles.obs_list = [(1,1)]
        self.assertEqual(False ,obstacles.is_path_blocked(6,9,6,7))
        self.assertEqual(True ,obstacles.is_path_blocked(1,2,1,3))


    def test_get_obstacles(self):
        random.randint = lambda x,y : 1
        self.assertEqual([(1,1)],obstacles.get_obstacles())
        self.assertEqual(1, len(obstacles.obs_list))


    # def test_generate_obs(self):
    #     random.randint = lambda x,y : 1
    #     obstacles.obs_list = [(1,1)]
    #     self.assertEqual([(1,1)],obstacles.generate_obs())
    #     print(obstacles.generate_obs())
    #     self.assertEqual(1, len(obstacles.obs_list))


if __name__ == "__main__":
    unittest.main()