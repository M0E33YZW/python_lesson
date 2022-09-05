# modulus30
N = 30
inspection_dict = {'␣': 0, '.': 1, ',': 2, '?': 3}

for i in range(26):
    inspection_dict[chr(97 + i)] = i + 4
# print(inspection_dict)


def getValue(key):
    return inspection_dict[key]


def getChar(num):
    return [k for k, v in inspection_dict.items() if v == num][0]


def calcCheckCharacter(input):  # 検査文字の生成
    sum = 0
    is_even = False

    i = len(input) - 1
    while i >= 0:
        value = getValue(input[i])
        if is_even:
            sum += value
        else:
            sum += sum + (value*2) // N + (value*2) % N
        is_even = not is_even
        i -= 1

    check_value = (N - sum % N) % N
    return getChar(check_value)  # 検査文字


def validateCheckCharacter(input):  # 検査文字付文字列の検証
    sum = 0
    is_odd = True

    i = len(input) - 1
    while i >= 0:
        value = getValue(input[i])
        if is_odd:
            sum += value
        else:
            sum += sum + (value*2) // N + (value*2) % N
        is_odd = not is_odd
        i -= 1

    ret_value = sum % N != 0
    return ret_value


print(validateCheckCharacter('ipa␣␣' + str(calcCheckCharacter('ipa␣␣'))))
