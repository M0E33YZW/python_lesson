name1 = "rino"
age1 = 24

name2 = "master yoda"
age2 = 800

template = "名前:{0:<15}, 年齢:{1:>3}"

s = template.format(name1,age1)
print(s)

s = template.format(name2,age2)
print(s)