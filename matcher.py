# 事前課題プログラム matcher.py

import sys

# テキストファイルを文字列リストへ変換する
# 引数 path: ファイルのパス名
# 戻値     : 文字列のリスト
def file_to_list(path):
    ss = []                   # 空のリストを作成
    f = open(path, 'r')       # ファイルを開く
    while sn := f.readline(): # 1行づつ読出し（ファイルの終端まで）
        s = sn.rstrip()       # 取り出した行から改行文字を取り除く
        ss.append(s)          # 文字列をリストに追加
    f.close()                 # ファイルをクローズ
    return ss                 # リストを返却

# 文字列リストから keyword を含む行を探し、
# その行を標準出力へ出力する。
# 引数 ss     : 文字列リスト
# 引数 keyword: キーワード
# 戻値        : なし
def print_matching_lines(ss, keyword):
    for (i, s) in enumerate(ss):           # 文字列リストから要素取り出し（リストの終端まで）
        if keyword in s:                   # 文字列要素にキーワードが含まれていたら
            print("{0}: {1}".format(i, s)) # 標準出力へ "<行番号>: <行の内容>" の 形式で出力

# メイン関数
# 引数: なし
# 戻値: なし
def main():
    args    = sys.argv                 # コマンドライン引数のリスト
    path    = args[1]                  # 第1引数: 検索対象となるファイルのパス名
    keyword = args[2]                  # 第2引数: 検索キーワード
    ss      = file_to_list(path)       # テキストファイルを文字列リストへ変換する
    print_matching_lines(ss, keyword)  # 文字列リストから keyword を含む行を探して出力

# メイン関数の実行
main()