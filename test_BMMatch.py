import unittest
from BMMatch import BMMatch

class BMMatchTest():
    def __init__(self, Text, Pat, want):
        self.Text = Text
        self.Pat = Pat
        self.want = want

BMMatchTestCases = [
    BMMatchTest('asdfjnjant', 'fjn', 3),
    BMMatchTest('aespatwice', 'aespa', 0),
    BMMatchTest('aespatwice', 'aespaa', -1),
    BMMatchTest('vivizstrayki', 'rayki', 7),
    BMMatchTest('vivizstrayki', 'raykia', -1),
    BMMatchTest('ACBBMACACBABC', 'ACAC', 5),
    BMMatchTest('ABCXBBACABACADEC', 'ACAB', 6),
    BMMatchTest('ACBBMACABABC', 'TWI', -1),
    BMMatchTest('0123456789', '78', 7),
    BMMatchTest('', '78', -1)
]

class BMMatchTestCase(unittest.TestCase):

    def test_BMMatch(self):
        for i, item in enumerate(BMMatchTestCases):

            have = BMMatch(item.Text, item.Pat)
            print('BMMatchTest[{}]'.format(i))
            self.assertEqual(have, item.want)


if __name__ == '__main__':
    unittest.main()