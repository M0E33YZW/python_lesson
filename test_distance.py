import unittest
from calcEditDistance import calcEditDistance

class EditDistanceTest():

    def __init__(self, str1, str2, want):
        self.str1 = str1
        self.str2 = str2
        self.want = want

EditTestCases = [
    EditDistanceTest('abcabba', 'cbabac', 5),
    EditDistanceTest('', '', 0),
    # EditDistanceTest('', '', 1), # エラー
    EditDistanceTest('a', '', 1)
]

class EditTestCase(unittest.TestCase):

    def test_editDistance(self):
        for i, item in enumerate(EditTestCases):
        
            have = calcEditDistance(item.str1, item.str2)
            print('EditTest[{}]'.format(i))
            self.assertEqual(have, item.want)


if __name__ == '__main__':
    unittest.main()
