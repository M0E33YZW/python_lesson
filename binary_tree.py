# 木構造の部品（節）クラス
class Part:
    # コンストラクタ
    # 引数 self レシーバ
    # 引数 name 要素名
    # 戻値 なし
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

## 3つの深さ優先探索
def pre_order(part):
    # 引数 part 確認する要素
    # 戻値 なし
    # 行きがけ順（先行順）
    # 左側のpartから探索
    # 左側に進めないときは1つ前のpartに戻って探索
    if part == None:
        return
    print(part.name)
    # print('左')
    pre_order(part.left)
    # print('右')
    pre_order(part.right)

def in_order(part):
    # 引数 part 確認する要素
    # 戻値 なし
    # 通りがけ順（中間順）
    # 左端を優先的に探索
    # 左側に進めないときは1つ前のpartに戻って探索
    if part == None:
        return
    # print('左')
    in_order(part.left)
    print(part.name)
    # print('右')
    in_order(part.right)

def post_order(part):
    # 引数 part 確認する要素
    # 戻値 なし
    # 帰りがけ順（後行順）
    # 左に進めるだけ進んだ後、右に進めるだけ進み探索
    # 左右進めない時は1つ前のpartに戻る
    if part == None:
        return
    # print('左')
    post_order(part.left)
    # print('右')
    post_order(part.right)
    print(part.name)

def print_object_diagram(part):

    print('## binary_tree')
    print('```plantuml')
    print('@startuml\n')
    print_order(part)
    print('@enduml')
    print('```\n')

def print_order(part):
    if part == None:
        return

    print_order(part.left)
    print_order(part.right)
   
    print('map ' + str(id(part)) +' {')
    print('    name => ' + str(part.name))
    if part.left == None:
        print('    left => None')
    else:
        print('    left *-> ' + str(id(part.left)))
    if part.right == None:
        print('    right => None')
    else:
        print('    right *-> ' + str(id(part.right)))
    print('}\n')

def main():
    top = Part('A')
    top.left = Part('B')
    top.right = Part('H')
    top.left.left = Part('C')
    top.left.right = Part('D')
    top.left.right.left = Part('E')
    top.left.right.right = Part('F')
    top.left.right.left.left = Part('G')
    print('pre_order...')
    pre_order(top)
    print()
    print('in_order...')
    in_order(top)
    print()
    print('post_order...')
    post_order(top)
    print_object_diagram(top)

main()