import sys
import re

# テキストファイルを文字列リストへ変換する
# 引数 path: ファイルのパス名
# 戻値     : 文字列のリスト
def file_to_list(path):
    ss = []               # 空のリストを作成
    f = open(path, 'r')   # ファイルを開く
    while sn := f.readline(): # ファイルの全行を読み出し
        s = sn.rstrip()   # 取り出した行から改行文字を取り除く
        ss.append(s)      # 文字列をリストに追加
    f.close()             # ファイルを閉じる
    return ss             # リストを返却

# 文字列リストからkeywordを含む行を探し、
# その行に赤い=>をつけて標準出力へ出力する。
# 引数 ss     : 文字列リスト
# 引数 keyword: キーワード
# 戻値        : なし
def print_matching_lines(ss, keyword): 
    for s in ss: # 文字列リストから要素を取り出し
        if keyword in s:
            aft = match_color(keyword)
            s = re.sub(keyword, aft, s)
        print(s)

def match_color(key):
    template = "\033[45m{}\033[m"
    aft = template.format(key)
    return aft

# メイン関数
# 引数: なし
# 戻値: なし
def main():
    args = sys.argv         # コマンドラインの引数リスト
    path = args[1]          # 第1引数: 検索対象となるファイルのパス名
    keyword = args[2]       # 第2引数: 検索キーワード
    ss = file_to_list(path) # テキストファイルを文字列リストへ変換する
    print_matching_lines(ss, keyword) #文字列リストからkeywordを含む行を探して出力する

main()