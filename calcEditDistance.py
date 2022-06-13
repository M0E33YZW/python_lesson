class EditDistance:

    @classmethod
    def init_for_unittest(cls, str1, str2):
        e = cls()
        e.str1 = str1
        e.str2 = str2
        return e

    # 引数 str: str1 変換元の文字列が格納されている1次元配列
    #     str: str2 変換先の文字列が格納されている1次元配列
    # 戻値 int: 変換元と変換先の文字列間の編集距離
    def calcEditDistance(str1, str2):

        str1len = len(str1) # 変換元の文字列の長さ（1以上）
        str2len = len(str2) # 変換先の文字列の長さ（1以上）

        D = [0 for _ in range(str1len + 1)]

        for i, _ in enumerate(D):
            D[i] = [0 for _ in range(str2len + 1)]
        # print('二次元配列初期化：', D)

        x = 0
        while (x <= str1len):
            D[x][0] = x
            x += 1

        y = 0
        while (y <= str2len):
            D[0][y] = y
            y += 1

        x = 1
        while (x <= str1len):
            y = 1
            while (y <= str2len):
                if (str1[x-1] == str2[y-1]):
                    D[x][y] = min([D[x-1][y-1], D[x][y-1]+1, D[x-1][y]+1])
                else:
                    D[x][y] = min([D[x][y-1]+1, D[x-1][y]+1])                
                y += 1
            x += 1

        print('D :', D)
        return D[len(str1)][len(str2)]

e = EditDistance
print(e.calcEditDistance('abcabba', 'cbabac'))
# print('')
# print(calcEditDistance('abcabba', 'abcabba'))
# print('')
# print(calcEditDistance('abcabba', 'aabcabba'))
# print('')
# print(calcEditDistance('abcabba', 'acabba'))
# print('')
# print(calcEditDistance('abcabba', 'abcabbj'))
