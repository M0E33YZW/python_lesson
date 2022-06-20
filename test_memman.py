import unittest
from memman import Memman
from memman import MIN_VAL
from memman import MAX_VAL


class MemmanTest():

    def __init__(self, before, sp, ep, after, err):
        self.before = before
        self.sp = sp
        self.ep = ep
        self.after = after
        self.err = err

AllocTestCases = [
    # エラーが出ないことを期待するデータ①〜④（正常系）
    # ① 始点[I] == 始点P かつ 終点P == 終点[I]
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
        '', # err
    ),
    # ② 始点[I] == 始点P かつ 終点P < 終点[I]
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
        '', # err
    ),
    # ③ 始点[I] < 始点P かつ 終点P == 終点[I]
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
        '', # err
    ),
    # ④ 始点[I] < 始点P かつ 終点P < 終点[I]
    MemmanTest(
        Memman.init_for_unittest(
            4, # num
            [MIN_VAL, 5, 13, 16,      0], # spos
            [1,       9, 14, MAX_VAL, 0], # epos
        ),
        6, # sp
        7, # ep
        Memman.init_for_unittest(
            5, # num
            [MIN_VAL, 5, 8, 13, 16,    ], # spos
            [1,       5, 9, 14, MAX_VAL], # epos
        ),
        '', # err
    ),
    # ⑤raise エラーが出ることを期待するテストデータ（異常系）
    MemmanTest(
        Memman.init_for_unittest(
            4, # num
            [MIN_VAL, 5, 13, 16,      0], # spos
            [1,       9, 14, MAX_VAL, 0], # epos
        ),
        5, # sp
        10, # ep
        # Memman.init_for_unittest( # after
        #     3, # num
        #     [MIN_VAL, 13, 16,    ], # spos
        #     [1,       14, MAX_VAL], # epos
        # ),
        None, # after
        # '', # err
        '一部又は全体が割当済み', # err
    ),
]

FreeTestCases = [
    # エラーが出ないことを期待するデータ①〜④（正常系）
    # ① 終点[I] == 始点P-1 かつ 終点P+1 == 始点[I+1]
    MemmanTest(
        Memman.init_for_unittest(
            3, # num
            [1, 9,  14,      0, 0], # spos
            [4, 10, MAX_VAL, 0, 0], # epos
        ),
        5, # sp
        8, # ep
        Memman.init_for_unittest(
            2, # num
            [1,  14,      0, 0, 0], # spos
            [10, MAX_VAL, 0, 0, 0], # epos
        ),
        '', # err
    ),
    # ② 終点[I] == 始点P-1 かつ 終点P+1 < 始点[I+1]
    MemmanTest(
        Memman.init_for_unittest(
            3, # num
            [1, 9,  14,      0, 0], # spos
            [4, 10, MAX_VAL, 0, 0], # epos
        ),
        5, # sp
        7, # ep
        Memman.init_for_unittest(
            3, # num
            [1, 9,  14,      0, 0], # spos
            [7, 10, MAX_VAL, 0, 0], # epos
        ),
        '', # err
    ),
    # ③ 終点[I] < 始点P-1 かつ 終点P+1 == 始点[I+1]
    MemmanTest(
        Memman.init_for_unittest(
            3, # num
            [1, 9,  14,      0, 0], # spos
            [4, 10, MAX_VAL, 0, 0], # epos
        ),
        6, # sp
        8, # ep
        Memman.init_for_unittest(
            3, # num
            [1, 6,  14,      0, 0], # spos
            [4, 10, MAX_VAL, 0, 0], # epos
        ),
        '', # err
    ),
    # ④ 終点[I] < 始点P-1 かつ 終点P+1 < 始点[I+1]
    MemmanTest(
        Memman.init_for_unittest(
            3, # num
            [1, 9,  14,      0, 0], # spos
            [4, 10, MAX_VAL, 0, 0], # epos
        ),
        6, # sp
        7, # ep
        Memman.init_for_unittest(
            4, # num
            [1, 6, 9,  14,      0], # spos
            [4, 7, 10, MAX_VAL, 0], # epos
        ),
        '', # err
    ),
    # ⑤raise エラーが出ることを期待するテストデータ（異常系）
    MemmanTest(
        Memman.init_for_unittest(
            1, # num
            [MIN_VAL, 0, 0, 0, 0], # spos
            [MAX_VAL, 0, 0, 0, 0], # epos
        ),
        4, # sp
        6, # ep
        Memman.init_for_unittest(
            1, # num
            [0, 0, 0, 0, 0], # spos
            [0, 0, 0, 0, 0], # epos
        ),
        '一部又は全体が割当済みでない', # err
    ),
    # ⑥割り当て間違い
]


class MemmanTestCase(unittest.TestCase):

    def test_alloc(self):
        for i, m in enumerate(AllocTestCases):
            try:
                m.before.Alloc(m.sp, m.ep)
                print('MemmanTests[{}]'.format(i))

                # 実際にエラーが起きなかったとき、期待したエラー値になったか
                self.assertEqual(m.err, '')

                # エラーが起きなかったとき、期待したafterの値になったか
                self.assertEqual(m.before.num, m.after.num)
                for j in range(m.after.num):
                    self.assertEqual(m.before.spos[j], m.after.spos[j])
                    self.assertEqual(m.before.epos[j], m.after.epos[j])

            except Exception as e:
                # 実際にエラーが起きたとき、期待したエラー値になったか
                # '' はエラーではない
                self.assertEqual(m.err, str(e))

    def test_free(self):
        for i, m in enumerate(FreeTestCases):
            try:
                m.before.Free(m.sp, m.ep)
                print('MemmanTests[{}]'.format(i))

                # 実際にエラーが起きなかったとき、期待したエラー値になったか
                self.assertEqual(m.err, '')

                # エラーが起きなかったとき、期待したafterの値になったか
                self.assertEqual(m.before.num, m.after.num)
                for j in range(m.after.num):
                    self.assertEqual(m.before.spos[j], m.after.spos[j])
                    self.assertEqual(m.before.epos[j], m.after.epos[j])

            except Exception as e:
                # 実際にエラーが起きたとき、期待したエラー値になったか
                # '' はエラーではない
                self.assertEqual(m.err, str(e))


if __name__ == '__main__':
    unittest.main()