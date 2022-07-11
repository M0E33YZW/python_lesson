def upper(abc):
    return ord(abc) - ord('a')

def upperCase(Text):

    text = list(Text)
    print(text)

    upperText = ''
    
    for c in text:
        if  ord('a') <= ord(c) and ord(c) <= ord('z'):
            upperText += chr(65 + upper(c))
        else:
            upperText += c

    return upperText

print(upperCase('Azあb'))