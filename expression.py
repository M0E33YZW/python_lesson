Operator = ['' for _ in range(100)]
Priority = [0 for _ in range(100)]
Value = [0 for _ in range(100)]


def compute(Expression: list):
    ExpLen = len(Expression)

    # 解析処理
    OpCnt = 0
    nest = 0
    i = 0
    while i < ExpLen:
        chr = Expression[i]
        if '0' <= chr and chr <= '9':  # 数字0~9か?
            Value[OpCnt] = 10 * Value[OpCnt] + int(chr)

        if chr == '+' or chr == '-' or chr == '×' or chr == '÷':
            Operator[OpCnt] = chr
            if chr == '+' or chr == '-':
                Priority[OpCnt] = nest + 1
            else:
                Priority[OpCnt] = nest + 2

            OpCnt += 1
            Value[OpCnt] = 0

        elif chr == '(':
            nest += 10
        elif chr == ')':
            nest -= 10

        i += 1

    # 計算処理
    while OpCnt > 0:
        ip = 0
        i = 1
        while i < OpCnt:
            if Priority[ip] < Priority[i]:
                ip = i
            i += 1

        chr = Operator[ip]
        if chr == '+':
            Value[ip] = Value[ip] + Value[ip+1]
        elif chr == '-':
            Value[ip] = Value[ip] - Value[ip+1]
        elif chr == '×':
            Value[ip] = Value[ip] * Value[ip+1]
        elif chr == '÷':
            Value[ip] = Value[ip] // Value[ip+1]

        i = ip + 1
        while i < OpCnt:
            Value[i] = Value[i+1]
            Operator[i-1] = Operator[i]
            Priority[i-1] = Priority[i]
            i += 1

        OpCnt -= 1

    return Value[0]


# print(compute('2×(34-(5+67)÷8)'))  # answer: 50
# print(compute('2×(-1)'))  # answer: -2
print(compute('(+2)×((-3)+(-4))'))  # answer: -14
# print(compute('+2×(-3+(-4))'))  # answer: -14
