'''
Классная работа, просто проверил как работает
'''

import unittest

def my_sum(iterable):
    sum = 0
    for i in iterable:
        sum += 1
    return sum

    class TestStringforexample(unittest.TestCase):

        def test_list(self):
            my_list = [1,2,3]
            self.assertNotEqual(my_sum(my_list), 5)

        def test_tuple(self):
            iterable = (1, 2, 3)
            self.assertNotEqual(my_sum(iterable), 6)

if __name__ == '__main__':
    unittest.main()