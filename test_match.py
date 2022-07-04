import unittest
from match import Match

class MatchTest():
    def __init__(self, s, substr, want):
        self.s = s
        self.substr = substr
        self.want = want

MatchTestCases = [
    MatchTest('asdfjnjant', 'fjn', 3),
    MatchTest('aespatwice', 'aespa', 0),
    MatchTest('aespatwice', 'aespaa', -1),
    MatchTest('vivizstrayki', 'rayki', 7),
    MatchTest('vivizstrayki', 'raykia', -1),
    MatchTest('ACBBMACACBABC', 'ACAC', 5),
    MatchTest('ABCXBBACABACADEC', 'ACAB', 6),
    MatchTest('ACBBMACABABC', 'TWI', -1),
    MatchTest('0123456789', '78', 7),
    MatchTest('', '78', -1)
]

class MatchTestCase(unittest.TestCase):

    def test_Match(self):
        for i, item in enumerate(MatchTestCases):

            have = Match(item.s, item.substr)
            print('MatchTest[{}]'.format(i))
            self.assertEqual(have, item.want)

if __name__ == '__main__':
    unittest.main()