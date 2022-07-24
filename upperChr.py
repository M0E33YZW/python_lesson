def upper(abc):
    return ord(abc) - ord('あ')

def upperCase(Text):

    text = list(Text)
    print(text)

    upperText = ''
    
    for c in text:
        if  ord('あ') <= ord(c) & ord(c) <= ord('ん'):
            upperText += chr(ord('ア') + upper(c))
        elif ord('a') <= ord(c) and ord(c) <= ord('z'):
            upperText += chr(ord('A') + upper(c))
        else:
            upperText += c

    return upperText

print(upperCase('Azあざわb'))
print(ord('あ'))