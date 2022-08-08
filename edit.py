def Edit(P, V):
    Pattern = list(P)
    Value = list(V)
    fill = Pattern[0]
    signif = 'off'
    p = v = 0

    while p < len(Pattern):

        if Pattern[p] == "▯" or Pattern[p] == "▮":

            if signif == 'off':
                if Pattern[p] != "▯" and Value[v] != "▮":

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
    
    return ''.join(Pattern)

data = [
    {'Pattern': "*▯▯,▯▯▯#",  'Value': "00000+" },
    {'Pattern': "*▯▯▯.▯▯#",  'Value': "00012-" },
    {'Pattern': "*▯▯▮.▯▯#",  'Value': "00012+" },
]
for d in data:
    print(d['Pattern'], d['Value'], Edit(d['Pattern'], d['Value']))


# 二次元配列
# data = [ 
#     ["*▯▯,▯▯▯#", "00000+"],
#     ["*▯▯▯.▯▯#", "00012-"],
#     ["*▯▯▮.▯▯#", "00012+"]
# ]
# for d in data:
    # print(d[0], d[1], Edit(d[0], d[1]))