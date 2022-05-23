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
    MemmanTest(
        Memman.init_for_unittest(
            1, # num
            [MIN_VAL, 0, 0, 0, 0], # spos
            [MAX_VAL, 0, 0, 0, 0], # epos
        ),
        1, # sp
        10, # ep
        Memman.init_for_unittest(
            2, # num
            [MIN_VAL, 11,      0, 0, 0], # spos
            [0,       MAX_VAL, 0, 0, 0], # epos
        ),
    ),
    MemmanTest(
        Memman.init_for_unittest(
            2, # num
            [MIN_VAL, 11,      0, 0, 0], # spos
            [0,       MAX_VAL, 0, 0, 0], # epos
        ),
        15, # sp
        17, # ep
        Memman.init_for_unittest(
            3, # num
            [MIN_VAL, 11, 18,      0, 0], # spos
            [0,       14, MAX_VAL, 0, 0], # epos
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
                self.assertEquals(m.before.spos[j], m.after.spos[j])
                self.assertEquals(m.before.epos[j], m.after.epos[j])



if __name__ == '__main__':
    unittest.main()