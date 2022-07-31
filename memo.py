class Memo:

    # コンストラクタ
    # 引数 self レシーバ
    # 戻値 なし
    def __init__(self):

        # int: 現在格納されているメモの件数
        self.MemoCnt = 0
        # int: 格納できるメモの最大件数(配列 Memo[] の要素数)
        self.MemoMax = 5
        # List[int]: メモごとの開始位置を保持する配列
        self.Memo = [0 for _ in range(self.MemoMax)]
        # int: 現在格納されている文字数
        self.DataLen = 0
        # int: 格納できる最大文字数(配列 Data[] の要素数)
        self.DataMax = 25
        # List[str]: メモを格納する配列
        self.Data = ['' for _ in range(self.DataMax)]
        self.temp = ['' for _ in range(self.DataMax)]

    # 全てのメモを消去する
    def restMemo(self):

        self.MemoCnt = 0
        self.DataLen = 0

    # 1件のメモを追加する
    def addMemo(self, textLen, text):
        self.Memo[self.MemoCnt] = self.DataLen
        self.MemoCnt = self.MemoCnt + 1
        self.Data[self.DataLen] = textLen
        self.DataLen = self.DataLen + 1

        i = 0
        while i < textLen:
            self.Data[self.DataLen + i] = text[i]
            i += 1

        self.DataLen = self.DataLen + textLen

    # 1件のメモを削除する
    def deleteMemo(self, pos):

        i = pos + 1
        while i < self.MemoCnt:
            self.Memo[i - 1] = self.Memo[i]
            i += 1
        self.MemoCnt -= 1

    # 1件のメモの内容を変更する
    def changeMemo(self, pos, textLen, text):

        self.Memo[pos] = self.DataLen
        self.Data[self.DataLen] = textLen
        self.DataLen += 1

        i = 0
        while i < textLen:
            self.Data[self.DataLen + i] = text[i]
            i += 1

        self.DataLen = self.DataLen + textLen

    # 1件のメモを移動する
    def moveMemo(self, fromPos, toPos):

        m = self.Memo[fromPos]
        if (fromPos < toPos):
            i = fromPos
            while i <= toPos - 1:
                self.Memo[i] = self.Memo[i + 1]

        elif (fromPos > toPos):
            i = fromPos
            while i >= toPos + 1:
                self.Memo[i] = self.Memo[i - 1]
                i -= 1

        self.Memo[toPos] = m

    # Data[] 中の参照されなくなったメモを取り除き，空き要素を増やす
    def clearGarbage(self):

        self.DataLen = 0

        if self.MemoCnt == 0:
            return

        m = 0
        while m < self.MemoCnt:
            d = self.Memo[m]
            self.Memo[m] = self.DataLen

            i = 0
            while i <= self.Data[d]:
                self.temp[self.DataLen] = self.Data[d + i]
                self.DataLen += 1
                i += 1

            m += 1

        d = 0
        while d < self.DataLen:
            self.Data[d] = self.temp[d]
            d += 1

    def print(self):
        print('Memo', self.Memo)
        print('MemoMax', self.MemoMax)
        print('MemoCnt', self.MemoCnt)
        print('Data', self.Data)
        print('DataMax', self.DataMax)
        print('DataLen', self.DataLen)

m = Memo()
m.restMemo()
m.print()
m.addMemo(4, "Aoki")
m.print()
m.addMemo(4, "Imai")
m.addMemo(3, "Uno")
m.addMemo(4, "Endo")
print('addMemo')
m.print()
m.deleteMemo(0)
print('deleteMemo')
m.print()
m.changeMemo(2, 3, "Abe")
print('changeMemo')
m.print()
m.moveMemo(2, 0)
print('moveMemo')
m.print()
print('clearGarbage')
m.clearGarbage()
m.print()