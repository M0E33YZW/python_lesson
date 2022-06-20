class quickSort():

    @classmethod
    def init_for_unittest(cls):
        s = cls()
        return s

    # 引数 x 数値が格納されている一次元配列
    # 引数 n 数値の個数
    # 引数 k 選択する数値の小ささの順位を示す値
    def Select(x, n, k):
        top = 0
        last = n

        print('before x: ', x, 'top: ', top, 'last: ', last)

        while top < last:
            pivot = x[k]
            i = top
            j = last

            while x[i] < pivot:
                i += 1

            while pivot < x[j]:
                j -= j

            if i >= j:
                break

            work = x[i]
            x[i] = x[j]
            x[j] = work
            i += 1
            j -= 1

            if i <= k:
                top = j + 1

            if k <= j:
                last = i - 1

            print('after x:', x)

        return x[k]

q = quickSort
print(q.Select([3,5,6,4,7,2,1], 6, 2))
print(q.Select([1,3,2,4,2,2,2], 6, 2))
