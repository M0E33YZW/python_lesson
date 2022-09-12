def lchild(i: int):
    return 2*i+1


def rchild(i: int):
    return 2*i+2


def parent(i: int):
    return (i-1)//2


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
        tmp = lchild(n)
        if rchild(n) <= hlast and heap[tmp] <= heap[rchild(n)]:
            tmp = rchild(n)

        if heap[tmp] > heap[n]:
            swap(heap, n, tmp)
        else:
            return

        n = tmp


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


# data = [30, 60, 45, 15, 5, 10, 20]
data = [60, 15, 45, 30, 5, 10, 20]
heap = []
for _ in data:
    heap.append(0)
print('data：', data)
print('heap：', heap)

# makeHeap(data, heap)
heapSort(data, heap)
