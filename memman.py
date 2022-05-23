MIN_VAL = -10000 # -∞(最小)
MAX_VAL =  10000 #  ∞(最大)

class Memman:

    # コンストラクタ
    # 引数 self レシーバ
    # 戻値 なし
    def __init__(self):
    
        # 空リスト中の現在の組の数
        self.num = 1

        # 始点配列（要素数100）
        self.spos = [0] * 100
        self.spos[0] = MIN_VAL

        # 終点配列（要素数100）
        self.epos = [0] * 100
        self.epos[0] = MAX_VAL

    @classmethod
    def init_for_unittest(cls, num, spos, epos):
        m = cls()
        m.num = num
        m.spos = spos
        m.epos = epos
        return m


    # 引数 self レシーバ
    #     int: sp(始点P)
    #     int: ep(終点P)
    # 戻値 なし
    def Alloc(self, sp, ep):
        i = 0

        # print('終点P > 終点[I]')
        # print(ep, '>', self.epos[i])
        while ep > self.epos[i]:
            i += 1

        if self.spos[i] <= sp:
            # print('始点[I] <= 始点P')
            # print(self.spos[i], '<=', sp)

            if self.spos[i] == sp and ep == self.epos[i]:
                # print('①(始点[I] == 始点P) かつ (終点P == 終点[I])')
                # print(self.spos[i], '==', sp, 'and', ep, '==', self.epos[i])

                l = i + 1
                while (l <= self.num):
                    self.spos[l - 1] = self.spos[l]
                    self.epos[l - 1] = self.epos[l]
                    l += 1
                self.num = self.num - 1

            elif self.spos[i] == sp and ep < self.epos[i]:
                # print('②(始点[I] == 始点P) かつ (終点P < 終点[I])')
                # print(self.spos[i], '==', sp, 'and', ep, '<', self.epos[i])
                self.spos[i] = ep + 1

            elif self.spos[i] < sp and ep == self.epos[i]:
                # print('③(始点[I] < 始点P) かつ (終点P == 終点[I])')
                # print(self.spos[i], '<', sp, 'and', ep, '==', self.epos[i])
                self.epos[i] = sp - 1

            elif self.spos[i] < sp and ep < self.epos[i]:
                # print('④(始点[I] < 始点P) かつ (終点P < 終点[I])')
                # print(self.spos[i], '<', sp, 'and', ep, '<', self.epos[i])
                l = self.num
                while (l >= i + 1):
                    self.spos[l + 1] = self.spos[l]
                    self.epos[l + 1] = self.epos[l]
                    l -= 1

                self.spos[i + 1] = ep + 1
                self.epos[i + 1] = self.epos[i]
                self.epos[i] = sp - 1
                self.num += 1
            
        else:
            raise Exception("一部又は全体が割当済み")

    def print(self):
        print(self.spos)
        print(self.epos)
        print('空リスト中の組数', self.num)


# m = Memman()
# m.print()
# m.Alloc(1, 3)
# m.print()
# m.Alloc(5, 7)
# m.print()

# try:
#     m.Alloc(2, 4)
# except Exception as e:
#     print('例外を補足：', e)