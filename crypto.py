#!/usr/local/bin/python3.4

#------Variables------#

encrypt = True
text = "anyone can see... this"
alpha = "abcdefghijklmnopqrstuvwxyz"
TEXT = "CIPHERTEXT IS AN EXAMPLE OF A CIPHER"
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
preserveSpaces = True


#------Setting functions------#

def cryptDirection(direction):
    global encrypt
    if direction.lower() == "decrypt" or not direction:
        encrypt = False
    else:
        encrypt = True

def setCiphertext(NEW):
    global TEXT, preserveSpaces
    TEXT = NEW.upper()
    if not preserveSpaces:
        TEXT = TEXT.replace(" ","")


#------Analytic functions------#

def cribFind(crib):
    global TEXT
    crib = crib.lower()
    crib = crib.replace(" ","")
    result = []
    i = 0
    while i <= len(TEXT) - len(crib):
        match = True
        j = 0
        while j < len(crib) and match == True:
            k = j + 1
            while k < len(crib) and match == True:
                if crib[j] == crib[k]:
                    if TEXT[i + j] != TEXT[i + k]:
                        match = False
                else:
                    if TEXT[i + j] == TEXT[i + k]:
                        match = False
                k += 1
            j += 1
        if match == True:
            result.append(TEXT[i:i + len(crib)])
        i += 1
    return result

def stringFreq(length = 1, mincount = 1):
    global TEXT
    done = []
    result = []
    i = 0
    while i <= len(TEXT) - length:
        sub = TEXT[i:i + length]
        if not sub in done:
            if TEXT.count(sub) >= mincount:
                result.append([sub, TEXT.count(sub)])
            done.append(sub)
        i += 1
    result.sort(key=lambda seq: seq[0])
    result.sort(key=lambda seq: seq[1], reverse=True)
    return result


#------Cryptographic functions------#

def substitute(text, sourceAlpha, targetAlpha):
    text = TEXT
    for i in range(26):
        text = text.replace(sourceAlpha[i], targetAlpha[i])
    return text

def simpleMonoalphaSub():
    global encrypt, text, alphabet, TEXT, ALPHABET
    if encrypt:
        TEXT = substitute(text, alpha, ALPHA)
    else:
        text = substitute(TEXT, ALPHA, alpha)

