import unittest
from BMMatch import BMMatch

class BMMatchTest():
    def __init__(self, Text, Pat, want):
        self.Text = Text
        self.Pat = Pat
        self.want = want

BMMatchTestCases = [
    BMMatchTest('ACBBMACACBABC', 'ACAC', 5),
    BMMatchTest('ABCXBBACABACADEC', 'ACAB', 6),
    BMMatchTest('ACBBMACABABC', 'TWI', -1),
    BMMatchTest('', 'ABC', -1)
]

class BMMatchTestCase(unittest.TestCase):

    def test_BMMatch(self):
        for i, item in enumerate(BMMatchTestCases):

            have = BMMatch(item.Text, item.Pat)
            print('BMMatchTest[{}]'.format(i))
            self.assertEqual(have, item.want)


if __name__ == '__main__':
    unittest.main()