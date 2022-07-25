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


class Skipper():

    def __init__(self, Pat):
        PatLen = len(Pat) - 1 # 検索文字列の長さ（1以上）
        self.skip = [PatLen for _ in range(26)]

        i = 0
        while i <= len(Pat) - 1:
            self.skip[Index(Pat[i])] = PatLen - i
            i += 1


    def getNum(self, chr):

        print(self.skip)
        print(chr)
        print(self.skip[Index(chr)])
        return self.skip[Index(chr)]


def BMMatch(Text, Pat):
    if Text == '' and Pat == '':
        return '文字列の入力がありません'

    Text = list(Text)
    Pat = list(Pat)
    print(Text, Pat)

    TextLen = len(Text) - 1 # 対象文字列の長さ（1以上）
    print('TextLen', TextLen)
    PatLen = len(Pat) - 1 # 検索文字列の長さ（1以上）
    print('PatLen', PatLen)

    # '''
    Skip = [0 for _ in range(26)] # 移動量を格納する要素数26の配列

    i = 0
    while i <= 25:
        Skip[i] = PatLen
        i += 1

    i = 0
    while i < PatLen:
        Skip[Index(Pat[i])] = PatLen - i
        i += 1
    # '''
    # skipper = Skipper(Pat)

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
        # PLast = PLast + skipper.getNum(Text[PLast])

    return -1

print(BMMatch('ACBBMACACBABC', 'ACAC'))
print(BMMatch('AABABCADCD', 'BCA'))