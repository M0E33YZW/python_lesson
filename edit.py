
def Edit(Pattern, Value):
    print('変更前')
    print(Value)
    print(Pattern)
    fill = Pattern[0]
    signif = 'off'
    p = v = 0

    while p < len(Pattern):

        if Pattern[p] == "□" or Pattern[p] == "■":

            if signif == 'off':
                if Pattern[p] != "□" and Value[v] != "■":

                    if Value[v + 1] != "+":
                        signif = 'on'

                if Value[v] == "0":
                    Pattern[p] = fill
                else:
                    Pattern[p] = Value[v]

            else:
                if Value[v + 1] == "+":
                    signif = 'off'

                Pattern[p] = Value[v]

            v += 1
        else:
            if signif == 'off':
                Pattern[p] = fill

        p += 1
    
    print('変更後')
    print(Pattern)

Edit(["*","□","□",",","□","□","□","#"], ["0","0","0","0","0","+"])
Edit(["*","□","□","□",".","□","□","#"], ["0","0","0","1","2","-"])
Edit(["*","□","□","■",".","□","□","#"], ["0","0","0","1","2","+"])

