# 引数 x 数値が格納されている一次元配列
# 引数 n 数値の個数
# 引数 k 選択する数値の小ささの順位を示す値
# 戻値　　k番目に小さい値
def Select(x, n, k):
    top = 0
    last = n

    while top < last:
        print('x: ', x, 'top: ', top + 1, 'last: ', last + 1)
        pivot = x[k]
        print('pivot', x[k])
        i = top
        j = last
        print('xi', x[i])
        while x[i] < pivot:
            i += 1
        print('25i', i, 'xi', x[i])


        print('xj', x[j])
        while pivot < x[j]:
            j -= j
        print('30j', j, 'xj', x[j])

        if i > j:
            break

        work = x[i]
        x[i] = x[j]
        x[j] = work
        i += 1
        j -= 1
        print('ij', i, j)

        if i <= k:
            top = j + 1
        print('39', j + 1, top)

        if k <= j:
            last = i - 1
        print('43', i - 1, last)

    print('after x:', x)
    return str(k) + '番目に小さい値', x[k]

# q = quickSort # x, n, k
# print(q.Select([3, 5, 6, 4, 7, 2, 1], 6, 2))
# print(q.Select([1,3,2,4,2,2,2], 6, 2))
