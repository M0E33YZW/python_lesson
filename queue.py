# 待ち行列クラスオブジェクト
class WaitingList:
  # コンストラクタ
  # 引数 self レシーバ
  #     capacity(初期値 10)
  # 戻値 なし
  def __init__(self, capacity=10):
    # selfにNoneを挿入
    self.admission = [None for _ in range(capacity+1)]
    self.capacity = capacity+1
    #空の状態
    self.previous = self.behind = 0

  # 引数 self
  #      num データの順番
  # 戻値 num+1をself.capacityで割った時の余り == 次のデータの順番
  def next(self, num):
    return (num + 1) % self.capacity

  # 引数 self レシーバ
  #      num データの順番
  # 戻値 True or False
  def enqueue(self, num):
    if self.previous == self.next(self.behind):
      print("queue is full")
      return False
    self.admission[self.behind] = num
    self.behind = self.next(self.behind)
    return True

  # 引数 self レシーバ
  # 戻値 num か False
  def dequeue(self):
    if self.previous == self.behind:
      print("queue is empty")
      return False
    num = self.admission[self.previous]
    self.previous = self.next(self.previous)
    return num

def print_object_diagram(list):
   
  print('```plantuml')
  print('@startuml\n')
  
  print('map ' + str(id(list)) +' {')
  print('    0 => ' +str(q.admission[0]))
  print('    1 => ' +str(q.admission[1]))
  print('    2 => ' +str(q.admission[2]))
  print('    3 => ' +str(q.admission[3]))
  print('}\n')

  print_list(list)

  print('@enduml')
  print('```\n')

def print_list(list):

    print('map WaitingList {')
    print('    admission *-> ' + str(id(list)))
    print('    capacity => ' +str(q.capacity))
    print('    previous => ' +str(q.previous))
    print('    behind => ' +str(q.behind))
    print('}\n')

print('# Object diagram')

q = WaitingList(3)
print('## WaitingList()')
print_object_diagram(q)

q.enqueue("a")
print('## q.enqueue("a")')
print_object_diagram(q)

q.enqueue("b")
print('## q.enqueue("b")')
print_object_diagram(q)

q.enqueue("c")
print('## q.enqueue("c")')
print_object_diagram(q)

q.dequeue()
print('## q.dequeue()')
print_object_diagram(q)

q.dequeue()
print('## q.dequeue()')
print_object_diagram(q)

q.dequeue()
print('## q.dequeue()')
print_object_diagram(q)

# q = WaitingList(3)

# # ENQUEUE -------------------------
# r = q.enqueue("a")
# print(f'q.enqueue("a"), success:{r}')

# r = q.enqueue("b")
# print(f'q.enqueue("b"), success:{r}')

# r = q.enqueue("c")
# print(f'q.enqueue("c"), success:{r}')

# r = q.enqueue("d")
# print(f'q.enqueue("d"), success:{r}')

# # DEQUEUE -------------------------
# r = q.dequeue()
# print(f'q.dequeue(), success:{r}')

# r = q.dequeue()
# print(f'q.dequeue(), success:{r}')

# r = q.dequeue()
# print(f'q.dequeue(), success:{r}')

# r = q.dequeue()
# print(f'q.dequeue(), success:{r}')