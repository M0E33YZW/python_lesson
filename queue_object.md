# Object diagram

## WaitingList()

```plantuml
@startuml

map List {
  0 => None
  1 => None
  2 => None
  3 => None
}

map WaitingList {
  admission *-> List
  capacity => 4
  previous => 0
  behind => 0
}

@enduml
```

## q.enqueue("a")

```plantuml
@startuml

map List {
  0 => "a"
  1 => None
  2 => None
  3 => None
}

map WaitingList {
  admission *-> List
  capacity => 4
  previous => 0
  behind => 1
}

@enduml
```

## q.enqueue("b")

```plantuml
@startuml

map List {
  0 => "a"
  1 => "b"
  2 => None
  3 => None
}

map WaitingList {
  admission *-> List
  capacity => 4
  previous => 0
  behind => 2
}

@enduml
```

## q.enqueue("c")

```plantuml
@startuml

map List {
  0 => "a"
  1 => "b"
  2 => "c"
  3 => None
}

map WaitingList {
  admission *-> List
  capacity => 4
  previous => 0
  behind => 3
}

@enduml
```

## q.dequeue()

```plantuml
@startuml

map List {
  0 => "a"
  1 => "b"
  2 => "c"
  3 => None
}

map WaitingList {
  admission *-> List
  capacity => 4
  previous => 1
  behind => 3
}

@enduml
```

## q.dequeue()

```plantuml
@startuml

map List {
  0 => "a"
  1 => "b"
  2 => "c"
  3 => None
}

map WaitingList {
  admission *-> List
  capacity => 4
  previous => 2
  behind => 3
}

@enduml
```

## q.dequeue()

```plantuml
@startuml

map List {
  0 => "a"
  1 => "b"
  2 => "c"
  3 => None
}

map WaitingList {
  admission *-> List
  capacity => 4
  previous => 3
  behind => 3
}

@enduml
```