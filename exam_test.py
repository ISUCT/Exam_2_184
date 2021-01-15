import unittest
import exam

class TestExam(unittest.TestCase):
    def test_1(self):
        res = exam.expand({'a': {'b': {'c': 12, 'd': 'Hello World'}, 'e': [1, 2, 3]}})
        ans = {'a/b/c': 12, 'a/b/d': 'Hello World', 'a/e': [1, 2, 3]}
        self.assertDictEqual(res, ans)

    def test_2(self):
        res = exam.expand({'a': {'b': {'c': {'d': 0}, 'e': 1}, 'f': 2}, 'g': 3})
        ans = {'a/b/c/d': 0, 'a/b/e': 1, 'a/f': 2, 'g': 3}
        self.assertDictEqual(res, ans)

if __name__ == '__main__':
    unittest.main()