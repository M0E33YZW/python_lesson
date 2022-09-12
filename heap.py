def lchild(i: int):
    return 2 * i + 1


def rchild(i: int):
    return 2 * i + 2


def parent(i: int):
    return (i-1) // 2


# iで指定されたノードの子ノードのうち、大きい値を持つノードのindexを返却
# iで指定されたノードの子ノードが、配列の検索範囲外の場合は例外を送出する
# last：配列の検索範囲の最後のindex

def bigChild(i: int, last: int):
    left = lchild(i)
    if left > last:
        raise Exception('検索範囲外です')

    right = rchild(i)
    left_value = heap[left]
    if right > last:
        return left

    right_value = heap[right]
    if left_value <= right_value:
        return right
    else:
        return left


def swap(heap: list, i: int, j: int):
    tmp = heap[i]
    heap[i] = heap[j]
    heap[j] = tmp


def makeHeap(data: list, heap: list):
    hnum = len(data)

    i = 0
    while i < hnum:
        heap[i] = data[i]
        k = i

        while k > 0:
            if heap[k] > heap[parent(k)]:
                swap(heap, k, parent(k))
                k = parent(k)
            else:
                break
        i += 1

    print('整列後の配列：', heap)


def downHeap(heap: list, hlast: int):
    n = 0
    while lchild(n) <= hlast:
        bigger = bigChild(n, hlast)
        # bigger = lchild(n)
        # if rchild(n) <= hlast and heap[bigger] <= heap[rchild(n)]:
        #     bigger = rchild(n)

        if heap[bigger] > heap[n]:
            swap(heap, n, bigger)
        else:
            return

        n = bigger


def heapSort(data: list, heap: list):
    makeHeap(data, heap)
    hnum = len(data)

    last = hnum - 1
    while last > 0:
        swap(heap, 0, last)
        print('last=', last, ';downHeap開始前の配列 => ', heap)
        downHeap(heap, last-1)
        last -= 1

    print('heapSort実行後の配列 => ', heap)


data = [60, 15, 45, 30, 5, 10, 20]
heap = []
for _ in data:
    heap.append(0)
print('data：', data)
print('heap：', heap)

# makeHeap(data, heap)
heapSort(data, heap)
