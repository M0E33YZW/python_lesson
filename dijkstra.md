# ダイクストラ法

----------------------------
## 変数
|変数|説明|
|:--|:--|
|pDist|出発地から各地点までの最短距離|
|pRoute|pDist を算出した経路の直前の地点|
|pFixed|pDist が確定したかどうか|
|sPoint|処理 [b] で確定した地点|
|newDist|処理 [c] において、確定地点を経由した出発地から隣接ノードまでの距離を一時的に格納| 
|i|処理 [b] において、未確定地点のうち pDist がより小さいノードを格納|
|j|処理 [b] において、未確定地点を順次参照するためのインデックス|
|j|処理 [c] において、隣接ノードを順次参照するためのインデックス|

----------------------------
## 処理の流れ

- [a] 初期化する
- [b] 未確定地点のうち pDist が一番小さいノードを確定地点とする
- [c] 確定地点（b で確定した地点）に隣接する未確定地点の pDist, pRoute を更新
- [d] 未確定地点が無くなるまで b, c を繰り返す
- [e] pDist[ep] の値を sDist とする
- [f] pRoute を辿って sRoute を生成する

sp=0, ep=6 のパターンで以下に詳細を記す。

----------------------------
### 1. [a] 初期化する

```plantuml
@startuml
!include skinparam.pu
map "0(sp)" as 0 {
    pFixed[0] => false
    pDist[0] => 0
    pRoute[0] => -1
}
map "1" as 1 {
    pFixed[1] => false
    pDist[1] => ∞ 
    pRoute[1] => -1
}
map "2" as 2 {
    pFixed[2] => false
    pDist[2] => ∞ 
    pRoute[2] => -1
}
map "3" as 3 {
    pFixed[3] => false
    pDist[3] => ∞ 
    pRoute[3] => -1
}
map "4" as 4 {
    pFixed[4] => false
    pDist[4] => ∞ 
    pRoute[4] => -1
}
map "5" as 5 {
    pFixed[5] => false
    pDist[5] => ∞ 
    pRoute[5] => -1
}
map "6(dp)" as 6 {
    pFixed[6] => false
    pDist[6] => ∞ 
    pRoute[6] => -1
}
1 -- 0: 2
0 - 2: 8
0 -- 3: 4
1 - 4: 3
2 - 4: 2
2 - 5: 3
3 - 5: 8
4 - 6: 9
5 - 6: 3
@enduml
```

----------------------------
### 2. [b] 未確定地点のうち pDist が一番小さいノードを確定地点とする

```plantuml
@startuml
!include skinparam.pu
map "0(sp)" as 0 #yellow {
    pFixed[0] => true ←
    pDist[0] => 0
    pRoute[0] => -1
}
map "1" as 1 {
    pFixed[1] => false
    pDist[1] => ∞ 
    pRoute[1] => -1
}
map "2" as 2 {
    pFixed[2] => false
    pDist[2] => ∞ 
    pRoute[2] => -1
}
map "3" as 3 {
    pFixed[3] => false
    pDist[3] => ∞ 
    pRoute[3] => -1
}
map "4" as 4 {
    pFixed[4] => false
    pDist[4] => ∞ 
    pRoute[4] => -1
}
map "5" as 5 {
    pFixed[5] => false
    pDist[5] => ∞ 
    pRoute[5] => -1
}
map "6(dp)" as 6 {
    pFixed[6] => false
    pDist[6] => ∞ 
    pRoute[6] => -1
}
1 -- 0: 2
0 - 2: 8
0 -- 3: 4
1 - 4: 3
2 - 4: 2
2 - 5: 3
3 - 5: 8
4 - 6: 9
5 - 6: 3
@enduml
```

----------------------------
### 3. [c] 確定地点に隣接する未確定地点の pDist, pRoute を更新

```plantuml
@startuml
!include skinparam.pu
map "0(sp)" as 0 #yellow {
    pFixed[0] => true
    pDist[0] => 0
    pRoute[0] => -1
}
map "1" as 1 #lightyellow {
    pFixed[1] => false
    pDist[1] => 2 ← 
    pRoute[1] => 0 ← 
}
map "2" as 2 #lightyellow {
    pFixed[2] => false
    pDist[2] => 8 ←
    pRoute[2] => 0 ←
}
map "3" as 3 #lightyellow {
    pFixed[3] => false
    pDist[3] => 4 ←
    pRoute[3] => 0 ←
}
map "4" as 4 {
    pFixed[4] => false
    pDist[4] => ∞ 
    pRoute[4] => -1
}
map "5" as 5 {
    pFixed[5] => false
    pDist[5] => ∞ 
    pRoute[5] => -1
}
map "6(dp)" as 6 {
    pFixed[6] => false
    pDist[6] => ∞ 
    pRoute[6] => -1
}
1 -- 0: 2
0 - 2: 8
0 -- 3: 4
1 - 4: 3
2 - 4: 2
2 - 5: 3
3 - 5: 8
4 - 6: 9
5 - 6: 3
@enduml
```

----------------------------
### 4. [b] 未確定地点のうち pDist が一番小さいノードを確定地点とする

```plantuml
@startuml
!include skinparam.pu
map "0(sp)" as 0 #eeeeee {
    pFixed[0] => true
    pDist[0] => 0
    pRoute[0] => -1
}
map "1" as 1 #yellow {
    pFixed[1] => true ←
    pDist[1] => 2 
    pRoute[1] => 0
}
map "2" as 2 { 
    pFixed[2] => false
    pDist[2] => 8
    pRoute[2] => 0
}
map "3" as 3 {
    pFixed[3] => false
    pDist[3] => 4 
    pRoute[3] => 0
}
map "4" as 4 {
    pFixed[4] => false
    pDist[4] => ∞ 
    pRoute[4] => -1
}
map "5" as 5 {
    pFixed[5] => false
    pDist[5] => ∞ 
    pRoute[5] => -1
}
map "6(dp)" as 6 {
    pFixed[6] => false
    pDist[6] => ∞ 
    pRoute[6] => -1
}
1 -- 0: 2
0 - 2: 8
0 -- 3: 4
1 - 4: 3
2 - 4: 2
2 - 5: 3
3 - 5: 8
4 - 6: 9
5 - 6: 3
@enduml
```

----------------------------
### 5. [c] 確定地点に隣接する未確定地点の pDist, pRoute を更新

```plantuml
@startuml
!include skinparam.pu
map "0(sp)" as 0 #eeeeee {
    pFixed[0] => true
    pDist[0] => 0
    pRoute[0] => -1
}
map "1" as 1 #yellow {
    pFixed[1] => true
    pDist[1] => 2 
    pRoute[1] => 0
}
map "2" as 2 { 
    pFixed[2] => false
    pDist[2] => 8
    pRoute[2] => 0
}
map "3" as 3 {
    pFixed[3] => false
    pDist[3] => 4 
    pRoute[3] => 0
}
map "4" as 4 #lightyellow {
    pFixed[4] => false
    pDist[4] => 5 ←
    pRoute[4] => 1 ←
}
map "5" as 5 {
    pFixed[5] => false
    pDist[5] => ∞ 
    pRoute[5] => -1
}
map "6(dp)" as 6 {
    pFixed[6] => false
    pDist[6] => ∞ 
    pRoute[6] => -1
}
1 -- 0: 2
0 - 2: 8
0 -- 3: 4
1 - 4: 3
2 - 4: 2
2 - 5: 3
3 - 5: 8
4 - 6: 9
5 - 6: 3
@enduml
```

----------------------------
### 6. [b] 未確定地点のうち pDist が一番小さいノードを確定地点とする

```plantuml
@startuml
!include skinparam.pu
map "0(sp)" as 0 #eeeeee {
    pFixed[0] => true
    pDist[0] => 0
    pRoute[0] => -1
}
map "1" as 1 #eeeeee {
    pFixed[1] => true
    pDist[1] => 2 
    pRoute[1] => 0
}
map "2" as 2 { 
    pFixed[2] => false
    pDist[2] => 8
    pRoute[2] => 0
}
map "3" as 3 #yellow {
    pFixed[3] => true ←
    pDist[3] => 4 
    pRoute[3] => 0
}
map "4" as 4 {
    pFixed[4] => false
    pDist[4] => 5
    pRoute[4] => 1
}
map "5" as 5 {
    pFixed[5] => false
    pDist[5] => ∞ 
    pRoute[5] => -1
}
map "6(dp)" as 6 {
    pFixed[6] => false
    pDist[6] => ∞ 
    pRoute[6] => -1
}
1 -- 0: 2
0 - 2: 8
0 -- 3: 4
1 - 4: 3
2 - 4: 2
2 - 5: 3
3 - 5: 8
4 - 6: 9
5 - 6: 3
@enduml
```

----------------------------
### 7. [c] 確定地点に隣接する未確定地点の pDist, pRoute を更新

```plantuml
@startuml
!include skinparam.pu
map "0(sp)" as 0 #eeeeee {
    pFixed[0] => true
    pDist[0] => 0
    pRoute[0] => -1
}
map "1" as 1 #eeeeee {
    pFixed[1] => true
    pDist[1] => 2 
    pRoute[1] => 0
}
map "2" as 2 { 
    pFixed[2] => false
    pDist[2] => 8
    pRoute[2] => 0
}
map "3" as 3 #yellow {
    pFixed[3] => true
    pDist[3] => 4 
    pRoute[3] => 0
}
map "4" as 4 {
    pFixed[4] => false
    pDist[4] => 5
    pRoute[4] => 1
}
map "5" as 5 #lightyellow {
    pFixed[5] => false
    pDist[5] => 12 ←
    pRoute[5] => 3 ←
}
map "6(dp)" as 6 {
    pFixed[6] => false
    pDist[6] => ∞ 
    pRoute[6] => -1
}
1 -- 0: 2
0 - 2: 8
0 -- 3: 4
1 - 4: 3
2 - 4: 2
2 - 5: 3
3 - 5: 8
4 - 6: 9
5 - 6: 3
@enduml
```

----------------------------
### 8. [b] 未確定地点のうち pDist が一番小さいノードを確定地点とする

```plantuml
@startuml
!include skinparam.pu
map "0(sp)" as 0 #eeeeee {
    pFixed[0] => true
    pDist[0] => 0
    pRoute[0] => -1
}
map "1" as 1 #eeeeee {
    pFixed[1] => true
    pDist[1] => 2 
    pRoute[1] => 0
}
map "2" as 2 { 
    pFixed[2] => false
    pDist[2] => 8
    pRoute[2] => 0
}
map "3" as 3 #eeeeee {
    pFixed[3] => true
    pDist[3] => 4 
    pRoute[3] => 0
}
map "4" as 4 #yellow {
    pFixed[4] => true ←
    pDist[4] => 5
    pRoute[4] => 1
}
map "5" as 5 {
    pFixed[5] => false
    pDist[5] => 12
    pRoute[5] => 3
}
map "6(dp)" as 6 {
    pFixed[6] => false
    pDist[6] => ∞ 
    pRoute[6] => -1
}
1 -- 0: 2
0 - 2: 8
0 -- 3: 4
1 - 4: 3
2 - 4: 2
2 - 5: 3
3 - 5: 8
4 - 6: 9
5 - 6: 3
@enduml
```

----------------------------
### 9. [c] 確定地点に隣接する未確定地点の pDist, pRoute を更新

```plantuml
@startuml
!include skinparam.pu
map "0(sp)" as 0 #eeeeee {
    pFixed[0] => true
    pDist[0] => 0
    pRoute[0] => -1
}
map "1" as 1 #eeeeee {
    pFixed[1] => true
    pDist[1] => 2 
    pRoute[1] => 0
}
map "2" as 2 #lightyellow { 
    pFixed[2] => false
    pDist[2] => 7 ←
    pRoute[2] => 4 ←
}
map "3" as 3 #eeeeee {
    pFixed[3] => true
    pDist[3] => 4 
    pRoute[3] => 0
}
map "4" as 4 #yellow {
    pFixed[4] => true
    pDist[4] => 5
    pRoute[4] => 1
}
map "5" as 5 {
    pFixed[5] => false
    pDist[5] => 12
    pRoute[5] => 3
}
map "6(dp)" as 6 #lightyellow {
    pFixed[6] => false
    pDist[6] => 14 ←
    pRoute[6] => 4 ←
}
1 -- 0: 2
0 - 2: 8
0 -- 3: 4
1 - 4: 3
2 - 4: 2
2 - 5: 3
3 - 5: 8
4 - 6: 9
5 - 6: 3
@enduml
```

----------------------------
### 10. [b] 未確定地点のうち pDist が一番小さいノードを確定地点とする

```plantuml
@startuml
!include skinparam.pu
map "0(sp)" as 0 #eeeeee {
    pFixed[0] => true
    pDist[0] => 0
    pRoute[0] => -1
}
map "1" as 1 #eeeeee {
    pFixed[1] => true
    pDist[1] => 2 
    pRoute[1] => 0
}
map "2" as 2 #yellow { 
    pFixed[2] => true ←
    pDist[2] => 7
    pRoute[2] => 4
}
map "3" as 3 #eeeeee {
    pFixed[3] => true
    pDist[3] => 4 
    pRoute[3] => 0
}
map "4" as 4 #eeeeee {
    pFixed[4] => true
    pDist[4] => 5
    pRoute[4] => 1
}
map "5" as 5 {
    pFixed[5] => false
    pDist[5] => 12
    pRoute[5] => 3
}
map "6(dp)" as 6 {
    pFixed[6] => false
    pDist[6] => 14
    pRoute[6] => 4
}
1 -- 0: 2
0 - 2: 8
0 -- 3: 4
1 - 4: 3
2 - 4: 2
2 - 5: 3
3 - 5: 8
4 - 6: 9
5 - 6: 3
@enduml
```

----------------------------
### 11. [c] 確定地点に隣接する未確定地点の pDist, pRoute を更新

```plantuml
@startuml
!include skinparam.pu
map "0(sp)" as 0 #eeeeee {
    pFixed[0] => true
    pDist[0] => 0
    pRoute[0] => -1
}
map "1" as 1 #eeeeee {
    pFixed[1] => true
    pDist[1] => 2 
    pRoute[1] => 0
}
map "2" as 2 #yellow { 
    pFixed[2] => true
    pDist[2] => 7
    pRoute[2] => 4
}
map "3" as 3 #eeeeee {
    pFixed[3] => true
    pDist[3] => 4 
    pRoute[3] => 0
}
map "4" as 4 #eeeeee {
    pFixed[4] => true
    pDist[4] => 5
    pRoute[4] => 1
}
map "5" as 5 #lightyellow {
    pFixed[5] => false
    pDist[5] => 10 ←
    pRoute[5] => 2 ←
}
map "6(dp)" as 6 {
    pFixed[6] => false
    pDist[6] => 14
    pRoute[6] => 4
}
1 -- 0: 2
0 - 2: 8
0 -- 3: 4
1 - 4: 3
2 - 4: 2
2 - 5: 3
3 - 5: 8
4 - 6: 9
5 - 6: 3
@enduml
```

----------------------------
### 12. [b] 未確定地点のうち pDist が一番小さいノードを確定地点とする

```plantuml
@startuml
!include skinparam.pu
map "0(sp)" as 0 #eeeeee {
    pFixed[0] => true
    pDist[0] => 0
    pRoute[0] => -1
}
map "1" as 1 #eeeeee {
    pFixed[1] => true
    pDist[1] => 2 
    pRoute[1] => 0
}
map "2" as 2 #eeeeee { 
    pFixed[2] => true
    pDist[2] => 7
    pRoute[2] => 4
}
map "3" as 3 #eeeeee {
    pFixed[3] => true
    pDist[3] => 4 
    pRoute[3] => 0
}
map "4" as 4 #eeeeee {
    pFixed[4] => true
    pDist[4] => 5
    pRoute[4] => 1
}
map "5" as 5 #yellow {
    pFixed[5] => true ←
    pDist[5] => 10
    pRoute[5] => 2
}
map "6(dp)" as 6 {
    pFixed[6] => false
    pDist[6] => 14
    pRoute[6] => 4
}
1 -- 0: 2
0 - 2: 8
0 -- 3: 4
1 - 4: 3
2 - 4: 2
2 - 5: 3
3 - 5: 8
4 - 6: 9
5 - 6: 3
@enduml
```

----------------------------
### 13. [c] 確定地点に隣接する未確定地点の pDist, pRoute を更新

```plantuml
@startuml
!include skinparam.pu
map "0(sp)" as 0 #eeeeee {
    pFixed[0] => true
    pDist[0] => 0
    pRoute[0] => -1
}
map "1" as 1 #eeeeee {
    pFixed[1] => true
    pDist[1] => 2 
    pRoute[1] => 0
}
map "2" as 2 #eeeeee { 
    pFixed[2] => true
    pDist[2] => 7
    pRoute[2] => 4
}
map "3" as 3 #eeeeee {
    pFixed[3] => true
    pDist[3] => 4 
    pRoute[3] => 0
}
map "4" as 4 #eeeeee {
    pFixed[4] => true
    pDist[4] => 5
    pRoute[4] => 1
}
map "5" as 5 #yellow {
    pFixed[5] => true
    pDist[5] => 10
    pRoute[5] => 2
}
map "6(dp)" as 6 #lightyellow {
    pFixed[6] => false
    pDist[6] => 13 ←
    pRoute[6] => 5 ←
}
1 -- 0: 2
0 - 2: 8
0 -- 3: 4
1 - 4: 3
2 - 4: 2
2 - 5: 3
3 - 5: 8
4 - 6: 9
5 - 6: 3
@enduml
```

----------------------------
### 14. [b] 未確定地点のうち pDist が一番小さいノードを確定地点とする

```plantuml
@startuml
!include skinparam.pu
map "0(sp)" as 0 #eeeeee {
    pFixed[0] => true
    pDist[0] => 0
    pRoute[0] => -1
}
map "1" as 1 #eeeeee {
    pFixed[1] => true
    pDist[1] => 2 
    pRoute[1] => 0
}
map "2" as 2 #eeeeee { 
    pFixed[2] => true
    pDist[2] => 7
    pRoute[2] => 4
}
map "3" as 3 #eeeeee {
    pFixed[3] => true
    pDist[3] => 4 
    pRoute[3] => 0
}
map "4" as 4 #eeeeee {
    pFixed[4] => true
    pDist[4] => 5
    pRoute[4] => 1
}
map "5" as 5 #eeeeee {
    pFixed[5] => true
    pDist[5] => 10
    pRoute[5] => 2
}
map "6(dp)" as 6 #yellow {
    pFixed[6] => true ←
    pDist[6] => 13
    pRoute[6] => 5
}
1 -- 0: 2
0 - 2: 8
0 -- 3: 4
1 - 4: 3
2 - 4: 2
2 - 5: 3
3 - 5: 8
4 - 6: 9
5 - 6: 3
@enduml
```

----------------------------
### 15. [f] sRoute（出発地から目的地への逆順経路）を求める

```plantuml
@startuml
!include skinparam.pu
map "0(sp)" as 0 #eeeeee {
    pFixed[0] => true
    pDist[0] => 0
    pRoute[0] => -1
}
map "1" as 1 #eeeeee {
    pFixed[1] => true
    pDist[1] => 2 
    pRoute[1] => 0
}
map "2" as 2 #eeeeee { 
    pFixed[2] => true
    pDist[2] => 7
    pRoute[2] => 4
}
map "3" as 3 #eeeeee {
    pFixed[3] => true
    pDist[3] => 4 
    pRoute[3] => 0
}
map "4" as 4 #eeeeee {
    pFixed[4] => true
    pDist[4] => 5
    pRoute[4] => 1
}
map "5" as 5 #eeeeee {
    pFixed[5] => true
    pDist[5] => 10
    pRoute[5] => 2
}
map "6(dp)" as 6 #eeeeee {
    pFixed[6] => true
    pDist[6] => 13
    pRoute[6] => 5
}
1 -[#black]-> 0: 2
0 - 2: 8
0 -- 3: 4
1 <-[#black] 4: 3
2 -[#black]> 4: 2
2 <-[#black] 5: 3
3 - 5: 8
4 - 6: 9
5 <-[#black] 6: 3
@enduml
```
