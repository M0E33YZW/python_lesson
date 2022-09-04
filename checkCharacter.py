inspection_dict = {'␣': 0, '.': 1, ',': 2, '?': 3}

for i in range(26):
    inspection_dict[chr(97 + i)] = i + 4
# print(inspection_dict)


def getValue(key):
    value = inspection_dict[key]
    return value


def getChar(num):
    key = [k for k, v in inspection_dict.items() if v == num][0]
    return key


def calcCheckCharacter(input):  # 検査文字の生成
    N = 30
    sum = 0
    is_even = False

    i = len(input) - 1
    while i >= 0:
        value = getValue(input[i])
        if is_even == True:
            sum = sum + value
        else:
            sum = sum + (value*2) // N + (value*2) % N
        is_even = not is_even
        i -= 1

    check_value = (N - sum % N) % N
    print(getChar(check_value))
    return getChar(check_value)  # 検査文字


def validateCheckCharacter(input):  # 検査文字付文字列の検証
    N = 30
    sum = 0
    is_odd = True
    ret_value = True

    i = len(input) - 1
    while i >= 0:
        value = getValue(input[i])
        if is_odd == True:
            sum = sum + value
        else:
            sum = sum + (value*2) // N + (value*2) % N
        is_odd = not is_odd
        i -= 1

    if sum % N != 0:
        ret_value = False

    return ret_value


print(validateCheckCharacter('ipa␣␣' + str(calcCheckCharacter('ipa␣␣'))))
