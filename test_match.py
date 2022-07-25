import unittest
from match import Match

class MatchTest():
    def __init__(self, s, substr, want):
        self.s = s
        self.substr = substr
        self.want = want

MatchTestCases = [
    MatchTest('引数に指定する複数の辞書', '複数', 7),
    MatchTest('引数に指定する複数の辞書', '三井', -1),
    MatchTest('引数に指定する複数の辞書', '辞書', 10),
    MatchTest('Stringの引数をURLに割り当てられませんというエラーです', 'エラー', 26),
    MatchTest('🐱🐶🐰🐯🐥🦊🐨🐹', '🐯🐥', 3),
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