import unittest
import super_algos

class test_super_algos(unittest.TestCase):
    def test_find_min(self):
        self.assertEqual(-1, super_algos.find_min([1,2,3,4,5,"a"]))
        self.assertEqual(-1, super_algos.find_min([]))
        self.assertEqual(min([1,2,3,4,5]), super_algos.find_min([1,2,3,4,5]))


    def test_sum_all(self):
        self.assertEqual(-1, super_algos.sum_all([1,2,3,4,5,"a"]))
        self.assertEqual(-1, super_algos.sum_all([]))
        self.assertEqual(sum([1,2,3,4,5]), super_algos.sum_all([1,2,3,4,5]))


    def test_find_possible_strings(self):
        self.assertEqual(["aa","ab","ba","bb"], super_algos.find_possible_strings(["a","b"], 2))
        self.assertEqual([], super_algos.find_possible_strings(["a","b",9], 3))


if __name__ == "__main__":
    unittest.main()