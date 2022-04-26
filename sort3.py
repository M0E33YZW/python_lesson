first_column_s  = lambda array: array[0]
second_column_s = lambda array: array[1]
second_column_i = lambda array: int(array[1])
third_column_s  = lambda array: array[2]

a = [
    ["apple" , "3", "1,000"],
    ["cherry", "10", "1,000"],
    ["banana", "10", "300"],
    ["banana", "2", "2,000"],
    ["apple" , "2", "1,000"],
]

print("origin         : ", end="")
print(a)

b = sorted(a, key = first_column_s)
print("first_column_s : ", end="")
print(b)

c = sorted(a, key = second_column_s)
print("second_column_s: ", end="")
print(c)

d = sorted(a, key = second_column_i)
print("second_column_i: ", end="")
print(d)

e = sorted(a, key = third_column_s)
print("third_column_s : ", end="")
print(e)