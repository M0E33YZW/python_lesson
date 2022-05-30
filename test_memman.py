import unittest
from memman import Memman
from memman import MIN_VAL
from memman import MAX_VAL


class MemmanTest():

    def __init__(self, before, sp, ep, after):
        self.sp = sp
        self.ep = ep
        self.before = before
        self.after = after

MemmanTests = [
    # ①(始点[I] == 始点P) かつ (終点P == 終点[I])
    MemmanTest(
        Memman.init_for_unittest(
            4, # num
            [MIN_VAL, 5, 13, 16,    ], # spos
            [1,       9, 14, MAX_VAL], # epos
        ),
        5, # sp
        9, # ep
        Memman.init_for_unittest(
            3, # num
            [MIN_VAL, 13, 16,    ], # spos
            [1,       14, MAX_VAL], # epos
        ),
    ),
    # ②(始点[I] == 始点P) かつ (終点P < 終点[I])
    MemmanTest(
        Memman.init_for_unittest(
            4, # num
            [MIN_VAL, 5, 13, 16,    ], # spos
            [1,       9, 14, MAX_VAL], # epos
        ),
        5, # sp
        7, # ep
        Memman.init_for_unittest(
            4, # num
            [MIN_VAL, 8, 13, 16,    ], # spos
            [1,       9, 14, MAX_VAL], # epos
        ),
    ),
    # # ③(始点[I] < 始点P) かつ (終点P == 終点[I])
    MemmanTest(
        Memman.init_for_unittest(
            4, # num
            [MIN_VAL, 5, 13, 16,    ], # spos
            [1,       9, 14, MAX_VAL], # epos
        ),
        8, # sp
        9, # ep
        Memman.init_for_unittest(
            4, # num
            [MIN_VAL, 5, 13, 16,    ], # spos
            [1,       7, 14, MAX_VAL], # epos
        ),
    ),
    # # ④(始点[I] < 始点P) かつ (終点P < 終点[I])
    MemmanTest(
        Memman.init_for_unittest(
            4, # num
            [MIN_VAL, 5, 13, 16,    ], # spos
            [1,       9, 14, MAX_VAL], # epos
        ),
        6, # sp
        7, # ep
        Memman.init_for_unittest(
            5, # num
            [MIN_VAL, 5, 8, 13, 16,    ], # spos
            [1,       5, 9, 14, MAX_VAL], # epos
        ),
    ),
]

class AllocTestCase(unittest.TestCase):

    def test_alloc(self):
        for i, m in enumerate(MemmanTests):
            m.before.Alloc(m.sp, m.ep)

            print('MemmanTests[{}]'.format(i))

            self.assertEqual(m.before.num, m.after.num)
            for j in range(m.after.num):
                self.assertEqual(m.before.spos[j], m.after.spos[j])
                self.assertEqual(m.before.epos[j], m.after.epos[j])


if __name__ == '__main__':
    unittest.main()