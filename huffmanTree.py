from functools import cmp_to_key
'AAAABBCDCDDACCAAAAA'
Max = 7
# 葉である節の個数
size = 4
# 同じ要素番号に対応する要素の組みによって，1つの節を表す4つの1次元配列
# 親
parent = [-1 for _ in range(Max)]
# 左側の子
left = [-1 for _ in range(Max)]
# 右側の子
right = [-1 for _ in range(Max)]
# 出現回数
freq = [-1 for _ in range(Max)]
freq[0] = 10
freq[1] = 2
freq[2] = 4
freq[3] = 3
print('freq初期状態', freq)


'''
ハフマン木を表現する配列を作成する
'''
def Huffman(size: int, parent: list[int], left: list[int], right: list[int], freq: list[int]):
    node = [0 for _ in range(Max)]
    nsize = SortNode(size, parent, freq, node)
    while nsize >= 2:
        i = node[0]  # 最も小さい値を持つ要素組の要素番号
        j = node[1]  # 2番目に小さい値を持つ要素組の要素番号
        left[size] = i
        right[size] = j
        freq[size] = freq[i] + freq[j]  # 子の値の合計
        parent[i] = size  # 子に親の節の要素番号を格納
        parent[j] = size  # 子に親の節の要素番号を格納
        size += 1
        nsize = SortNode(size, parent, freq, node)

    print('parent:', parent)
    print('freq  :', freq)
    print('left  :', left)
    print('right :', right)
    print('node  :', node)


'''
親が作成されていない節を抽出し，出現回数の昇順に整列し，
節を表す要素組の要素番号を順に配列 node に格納し，
その個数を変数 nsize に格納する。
親が作成されていない節を表す要素組の要素番号を抽出し，節の値の昇順に整列する。
'''
def SortNode(size: int, parent: list[int], freq: list[int], node: list[int]):
    nsize = 0
    i = 0
    while i < size:
        if parent[i] < 0:
            node[nsize] = i
            nsize += 1
        i += 1
    Sort(freq, node)
    return nsize


'''
節を表す要素組の要素番号の配列 node を受け取り，
要素番号に対応する要素組が表す節の値が昇順となるように整列する。
節の値が同じときの順序は並べ替える直前の順序に従う。
安定性補償のためにsorted()を使用。
https://docs.python.org/3/library/functions.html#sorted
'''
def Sort(freq: list[int], node: list[int]):

    def cmpFreq(a, b):
        return freq[a] - freq[b]

    print(sorted(node, key=cmp_to_key(cmpFreq)))


def Encode(k: int, parent: list[int], left: list[int]):
    if parent[k] >= 0:
        Encode(parent[k], parent, left)

        result = ''
        if left[parent[k]] == k:
            result += '0'
        else:
            result += '1'
        print(result)


Huffman(size, parent, left, right, freq)
Encode(0, parent, left)
