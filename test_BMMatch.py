import unittest
from BMMatch import BMMatch

class BMMatchTest():
    def __init__(self, Text, Pat, want):
        self.Text = Text
        self.Pat = Pat
        self.want = want

BMMatchTestCases = [
    BMMatchTest(['A','C','B','B','M','A','C','A','B','A','B','C'], ['A','C','A','B'], 6),
    BMMatchTest(['A','B','C','X','B','B','A','C','A','B','A','C','A','D','E','C'], ['A','C','A','B'], 9),
    BMMatchTest(['A','C','B','B','M','A','C','A','B','A','B','C'], ['T','W','I','C','E'], 0), # エラー
    BMMatchTest(['0','1','2','3','4','5','6','7','8','9'], ['7','8'], 8)
]

class BMMatchTestCase(unittest.TestCase):

    def test_BMMatch(self):
        for i, item in enumerate(BMMatchTestCases):

            have = BMMatch(item.Text, item.Pat)
            print('BMMatchTest[{}]'.format(i))
            self.assertEqual(have, item.want)


if __name__ == '__main__':
    unittest.main()