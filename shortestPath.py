MAX_VAL = 10000  # ∞(最大値を表す定数)


class Shortest:

    # コンストラクタ
    # 引数 self レシーバ
    # 戻値 なし
    def __init__(self):
        self.sRoute = []  # 出発地から目的地までの最短経路上の地点の地点番号を目的地から出発地までの順に設定する1次元配列
        self.sDist = MAX_VAL  # 出発地から目的地までの最短距離を設定する配列
        self.pFixed = []
        self.pDist = []
        self.pRoute = []


    # 出発地から目的地に至る最短経路とその距離を求める
    def ShortestPath(self: __init__, Distance: list[list[int]], sp: int, dp: int):
        nPoint = len(Distance[0])

        i = 0
        while i < nPoint:
            self.sRoute.append(-1)      # 最短経路上の地点の地点番号に初期値を格納する
            self.pDist.append(MAX_VAL)  # 出発地から各地点までの最短距離に初期値を格納する
            self.pFixed.append(False)   # 各地点の最短距離の確定状態に初期値を格納する
            self.pRoute.append(0)
            i += 1
        # print('sRoute', self.sRoute)
        # print('pDist', self.pDist)
        # print('pFixed', self.pFixed)
        self.pDist[sp] = 0  # 出発地から出発地自体への最短距離に0を設定する
        while True:  # 最短経路探索処理
            i = 0
            while i < nPoint:  # 未確定の地点を一つ探す
                if not(self.pFixed[i]):
                    break  # 最内側の繰返しから抜ける
                i += 1

            if i == nPoint:  # 出発地から全ての地点までの最短距離が確定
                break        # していれば、最短距離探索処理を抜ける

            j = i + 1
            while j < nPoint:  # 最短距離がより短い地点を探す
                if not(self.pFixed[j]) and self.pDist[j] < self.pDist[i]:
                    i = j
                j += 1

            sPoint = i  # α
            self.pFixed[sPoint] = True  # 出発地からの最短距離を確定する
            j = 0
            while j < nPoint:
                if Distance[sPoint][j] > 0 and not (self.pFixed[j]):
                    newDist = self.pDist[sPoint] + Distance[sPoint][j]
                    if newDist < self.pDist[j]:
                        self.pDist[j] = newDist
                        self.pRoute[j] = sPoint
                j += 1

        # β
        # 出発地から目的地までの最短距離を sDist に，最短経路上の地点の地点番号を目的地から出発地までの順に配列 sRoute に設定する。
        self.sDist = self.pDist[dp]
        j = 0
        i = dp
        while i != sp:
            self.sRoute[j] = i
            i = self.pRoute[i]
            j += 1

        self.sRoute[j] = sp

        return self.sDist, self.sRoute
        # 配列と最短距離の2つのフィールドを持ったクラスを返す

D0 = [
    [0, 2, 8, 4, -1, -1, -1],
    [2, 0, -1, -1, 3, -1, -1],
    [8, -1, 0, -1, 2, 3, -1],
    [4, -1, -1, 0, -1, 8, -1],
    [-1, 3, 2, -1, 0, -1, 9],
    [-1, -1, 3, 8, -1, 0, 3],
    [-1, -1, -1, -1, 9, 3, 0]
]
D1 = [
    [0, 1, 5, -1, -1, -1],
    [1, 0, 3, 3, -1, -1],
    [5, 3, 0, -1, 4, -1],
    [-1, 3, -1, 0, -1, 4],
    [-1, -1, 4, -1, 0, 5],
    [-1, -1, -1, 4, 5, 0],
]

s = Shortest()
print(s.ShortestPath(D0, 0, 6))  # 最短 13日
s = Shortest()
print(s.ShortestPath(D0, 2, 3))  # 最短 11日
s = Shortest()
print(s.ShortestPath(D0, 1, 5))  # 最短 8日
# s = Shortest()
# print(s.ShortestPath(D1, 0, 5))  # 最短 8日
