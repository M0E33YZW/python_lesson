# ノードクラスオブジェクト
class Node:
    # コンストラクタ
    # 引数 self レシーバ
    # 戻値 なし
    def __init__(self, value): 
        self.value = value
        self.next = None

# 線形リスト
# リスト内のノードの値は昇順になるように整列される
class List:
    # コンストラクタ
    # 引数 self レシーバ
    # 戻値 なし
    def __init__(self):
        self.head = Node(None)

    # 線形リストにノードを挿入する
    # 引数 self レシーバ
    #     value 挿入するノードの値
    # 戻値 なし
    def insert(self, value): 
        previous = self.head
        current = previous.next
        while current and value > current.value: #valueを昇順で挿入
            previous = current
            current = current.next
        node = Node(value)
        node.next = current
        previous.next = node

    # 線形リストからノードを削除する
    # 削除対象ノードが存在しない場合は標準出力にエラーメッセージを出力する
    # 引数 self  レシーバ
    #      value 削除するノードの値
    # 戻値 なし
    def delete(self, value): 
        previous = self.head
        current = previous.next
        while current:
            if current.value == value:
                break
            previous = current
            current = current.next
        if not current: 
            print("[*] Data not found")
            return
        previous.next = current.next
        current = None

    

    # 線形リストの内容を標準出力へ出力する
    # 引数 self レシーバ
    # 戻値 なし
    def show(self): 
        tmp = self.head.next
        while tmp:
            print(tmp.value)
            tmp = tmp.next
    
    # 線形探索
    # 引数 self レシーバ
    #     index 探索に使う添字
    # 戻値 index 番目のvalueの値
    # リストの中に index 番目が存在しない場合はエラーメッセージを表示
    def get(self, index):
        tmp = self.head.next
        n = 0
        while tmp:
            if n == index:
              print(tmp.value)
              return tmp.value
            tmp = tmp.next
            n += 1
        print("[*] Data not found")

    # 線形探索
    # 引数 self レシーバ
    #     value 探索に使う値
    # 戻値 valueのあるindexの値、valueがない場合は-1を返す
    # リストの中に value が存在しない場合はエラーメッセージを表示
    def index_of(self, value):
        tmp = self.head.next
        n = 0
        while tmp:
            if tmp.value == value:
                print(n)
                return n
            tmp = tmp.next
            n += 1
        print("[*] Data not found")
        return -1

    # 線形リストの要素数を調べる
    # 引数 self レシーバ
    # 戻値 Listの要素数
    # リストが要素を持っていない場合はエラーメッセージを表示
    def len(self):
        tmp = self.head
        length = 0
        while tmp:
            if tmp.next == None:
                print(length)
                return length
            tmp = tmp.next
            length += 1
        print("[*] Data not found")

    # リストの値を配列として返す
    # 引数 self レシーバ
    # 戻値 リストの中身を持った配列 array
    def get_array(self):
        tmp = self.head.next
        array = []
        while tmp:
            array.append(tmp.value)
            tmp = tmp.next
        print(array)
        return array

    # リストの値をカンマ区切りの文字列として返す
    # 引数 self レシーバ
    # 戻値 リストの中身を持った文字列
    def get_str(self):
        tmp = self.head.next
        array = []
        while tmp:
            array.append(tmp.value)
            tmp = tmp.next
        print(','.join(map(str, array)))
        return ','.join(map(str, array))

def print_object_diagram(list):
   
    print('```plantuml')
    print('@startuml\n')

    print_node(list.head)
    
    print('map ' + str(id(list)) +' {')
    print('    class => List')
    print('    head *-> ' + str(id(list.head)))
    print('}\n')

    print('@enduml')
    print('```\n')

def print_node(node):
    # Noneだったら何もしない
    if node == None:
        return

    # 再帰呼び出し
    print_node(node.next)

    print('map ' + str(id(node)) +' {')
    print('    class => Node')
    print('    value => ' + str(node.value))

    if node.next == None:
        print('    next => None')
    else:
        print('    next *-> ' + str(id(node.next)))
    
    print('}\n')

print('# Object diagram')

list = List()
print('## LinkedList()')
print_object_diagram(list)

list.insert(3)
print('## insert(3)')
print_object_diagram(list)

list.insert(5)
print('## insert(5)')
print_object_diagram(list)

list.insert(1)
print('## insert(1)')
print_object_diagram(list)

list.delete(3)
print('## delete(3)')
print_object_diagram(list)



# l = List()
# print('insert 3, 5, 1...')
# l.insert(3)
# l.insert(5)
# l.insert(1)
# print_object_diagram(l)
# print('print data')
# l.show()
# print('delete 3...')
# l.delete(3)
# print('print data')
# l.show()
# print('get[0]')
# l.get(0)
# print('get[2]')
# l.get(2)
# print('--------------10月3日---------------')
# print('index of 3')
# l.index_of(3)
# print('index of 5')
# l.index_of(5)
# print('l_len')
# l.len()
# print('get_array')
# l.get_array()
# print('get_str')
# l.get_str()