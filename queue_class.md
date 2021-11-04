# WaitingList クラス図

```plantuml
@startuml

class WaitingList {
  admission : List
  capacity : Node
  previous : 0
  behind : 0
  __init__()
  next()
  enqueue()
  dequeue()
}

@enduml
```