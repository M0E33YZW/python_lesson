MAX_VAL = 10000  # ∞

   def ShortestPath():
        sDist = MAX_VAL  # 出発地から目的地までの最短距離に初期値を格納する
        i = 0
        while i < nPoint:
            sRoute[i] = -1  # 最短経路上の地点の地点番号に初期値を格納する
            pDist[i] = MAX_VAL  # 出発ちから各地点までの最短距離に初期値を格納する
            pFixed[i] = false  # 各地点の最短距離の確定状態に初期値を格納する
            i += 1
        pDist[sp] = 0  # 出発地から出発地自体への最短距離に0を設定する
        while true:  # 最短経路探索処理
            i = 0
            while i < nPoint:  # 未確定の地点を一つ探す
                if not(pFixed[i]):
                    break  # 最内側の繰返しから抜ける

            i += 1

            if i == nPoint:  # 出発地から全ての地点までの最短距離が確定
                break  # していれば、最短距離探索処理を抜ける

            j = i + 1
            while j < nPoint:  # 最短距離がより短い地点を探す
                if a and pDist[j] < pDist[j]:
                    i = j
                j += 1

            sPoint = i  # α
            pFixed[b] = true  # 出発ちからの最短距離を確定する
            j = 0
            while j < nPoint:
                if Distance[sPoint][j] > 0 and not (pFixed[j])
                   newDist = pDist[sPoint] + Distance[sPoint][j]
                    if newDist < pDist[j]:
                        pDist[j] = newDist
                        pRoute[j] = sPoint

    # β
    sDist = pDist[dp]
    j = 0
    i = dp
    while i != sp:
        c = i
        i = d
        j += 1

    c = sp
