# count total number of consonants in it. A consonant is an English alphabet character
#  that is not vowel (a, e, i, o and u)

def isConsonants(ch):
    ch = ch.upper()
    if ch not in ['A','E', 'I', 'O', 'U'] and (ord(ch) >= 65 and ord(ch) <= 90):
        return 1
    else:
        return 0

def recfunc(inp):
    if len(inp) == 1:
        return isConsonants(inp[0])
    else:
        return recfunc(inp[:-1]) + isConsonants(inp[-1])
        

print(recfunc('babc de'))