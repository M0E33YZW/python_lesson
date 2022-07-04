def Match(s, substr):

    s = list(s)
    substr = list(substr)

    print(s, substr)

    i = 0
    while i < len(s):
        j = 0

        while j < len(substr):
            if i + j >= len(s) or s[i + j] != substr[j]:
                break
            j += 1
        
        if j >= len(substr):
            return i

        i += 1

    return -1

# print(Match('asdfjnjant', 'fjn'))
# print(Match('aespatwice', 'aespa'))
# print(Match('vivizstrayki', 'rayki'))