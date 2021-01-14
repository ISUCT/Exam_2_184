import unittest
import hello

class TestSum(unittest.TestCase):

    def test_correct_calc(self):
        res = hello.calc(2,4,3)
        self.assertAlmostEqual(res, 1.642, places=3, msg="Should be 1.641")

if __name__ == '__main__':
    unittest.main()