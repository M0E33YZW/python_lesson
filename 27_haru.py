# 引数 x 数値が格納されている一次元配列
# 引数 n 数値の個数
# 引数 k 選択する数値の小ささの順位を示す値

def Select(x, n, k):
    top = 0
    last = n

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

    return x[k]

print(Select([3,5,6,4,7,2,1], 6, 3))
print(Select([1,3,2,4,2,2,2], 6, 3))
