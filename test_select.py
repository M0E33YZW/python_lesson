import unittest
from quicksort27 import Select

class SelectTest():

    def __init__(self, x, k, want):
        self.x = x
        self.k = k
        self.want = want

SelectTestCases = [
    SelectTest([3, 5, 6, 4, 7, 2, 1], 2, 2),
    SelectTest([1, 3, 2, 4, 2, 2, 2], 2, 2),
    SelectTest([3, 5, 6, 4, 7, 2, 1], 2, 4),
]

class SelectTestCase(unittest.TestCase):

    def test_editDistance(self):
        for i, item in enumerate(SelectTestCases):
        
            have = Select(item.x, item.k)
            print('EditTest[{}]'.format(i))
            self.assertEqual(have, item.want)


if __name__ == '__main__':
    unittest.main()
