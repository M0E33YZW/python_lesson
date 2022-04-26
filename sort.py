############################################
# リスト型のメソッド sort() のパラメータ key
# を理解するために、使い方が似ている組込関数
# sorted() で key の使い方を検証する。
############################################

#-----------------------------------------
# 組込関数 sorted の パラメータ key の検証
#-----------------------------------------
def lucy7(n):
    if n == 7:
        return -1
    else:
        return n

a = [5, 1, 30, 7, 9]
b = sorted(a)            # key 指定なし
c = sorted(a, key=str)   # 組込関数 str() を指定
d = sorted(a, key=lucy7) # 独自関数 lucy7() を指定

print("-----------------------")

print("a                     : ", end="")
print(a)

print("b=sorted(a)           : ", end="")
print(b)

print("c=sorted(a, key=str)  : ", end="")
print(c)

print("d=sorted(a, key=lucy7): ", end="")
print(d)

#-----------------------------------------
# 組込関数 sorted の パラメータ key の検証
# 文字列中の「曜日を示す文字」順に並び替え
#-----------------------------------------
def day_of_week(s):
    dow=['日', '月', '火', '水', '木', '金', '土']
    for i, d in enumerate(dow):
        if d in s:
            return i
    return len(dow)

a = ["海王星", "水没", "金メダル", "日本", "粘土", "満月", "六本木", "発火", ]
b = sorted(a, key=day_of_week)

print("-----------------------------")

print("a                           : ", end="")
print(a)

print("b=sorted(a, key=day_of_week): ", end="")
print(b)