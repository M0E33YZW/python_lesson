'''
1. クレジットカード番号の後ろから数えて、奇数桁だけを合計する。
2. クレジットカード番号の後ろから数えて、偶数桁を2倍して合計する。
   2倍した数が10以上になる時は合計する前に9を引く。
3. 1と2の数字を合計する。
4. 正しいカード番号ならこの合計が10で割り切れる。
'''

def validateCreditNumber(s):
    is_odd = True
    num = 0

    i = len(s) - 1
    while i >= 0:
        # if not s[i].isdecimal():
        #     return False
        try:
            value = int(s[i])
        except Exception as e:
            return False

        if is_odd:
            num += value
        else:
            num += value * 2 - 9 if value * 2 >= 10 else value * 2

        is_odd = not is_odd
        i -= 1

    return num % 10 == 0