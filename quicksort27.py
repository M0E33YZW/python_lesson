# 引数 x 数値が格納されている一次元配列
# 引数 k 選択する数値の小ささの順位を示す値
# 戻値   k番目に小さい値
def Select(x, k):
    top = 0
    last = len(x) - 1
    k -= 1

    while top < last:
        # print('x: ', x, 'top: ', top + 1, 'last: ', last + 1)
        pivot = x[k]

        i = top
        j = last

        while True:
            print('x: ', x, 'pivot: ', pivot, 'i: ', i, 'j: ', j)
            while x[i] < pivot:
                i += 1

            while pivot < x[j]:
                j -= 1

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

    return x[k]

k = 4
# sel = Select([3, 5, 6, 4, 7, 2, 1], k)
# print('2番目に小さい値', sel)

# sel = Select([1, 3, 2, 4, 2, 2, 2], k)
# print('2番目に小さい値', sel)

# sel = Select([3, 5, 1, 4, 2, 7, 6], k)
# print('2番目に小さい値', sel)

# sel = Select([8, 2, 7, 6, 5, 1, 4, 3, 9], k)
# print('2番目に小さい値', sel)

sel = Select([2, 7, 6, 5, 1, 4, 3], k)
print('4番目に小さい値', sel)
