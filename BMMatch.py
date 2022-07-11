'''
引数 List[str]
Text[]: 対象文字列が格納されている一次元配列
 Pat[]: 検索文字列が格納されている一次元配列
返却値 int
対象文字列中に検索文字列が見つかった場合は、1以上の値を返す。
検索文字列が見つからなかった場合は、-1を返す。
'''

def Index(abc):
    # import string
    # alphabets = string.ascii_uppercase
    # return alphabets.index(abc)

    # 文字コードで引算
    return ord(abc) - ord('A')


def BMMatch(Text, Pat):
    if Text == '' and Pat == '':
        return '文字列の入力がありません'

    Text = list(Text)
    Pat = list(Pat)
    print(Text, Pat)

    TextLen = len(Text) - 1 # 対象文字列の長さ（1以上）
    PatLen = len(Pat) - 1 # 検索文字列の長さ（1以上）

    Skip = [0 for _ in range(26)] # 移動量を格納する要素数26の配列

    i = 0
    while i <= 25:
        Skip[i] = PatLen 
        i += 1

    i = 0
    while i <= PatLen - 1:
        Skip[Index(Pat[i])] = PatLen - i
        i += 1

    PLast = PatLen

    while PLast <= TextLen:
        PText = PLast
        PPat = PatLen 

        while Text[PText] == Pat[PPat]:
            if PPat == 0:
                return PText

            PText = PText - 1
            PPat = PPat - 1

        PLast = PLast + Skip[Index(Text[PLast])]

    return -1

# print(BMMatch('ACBBMACACBABC', 'ACAC'))