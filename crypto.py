#!/usr/local/bin/python3.4

#------Variables------#

alphabet = "abcdefghijklmnopqrstuvwxyz"

text = "anyone can see... this"
alpha = alphabet.lower()
TEXT = "CIPHERTEXT IS AN EXAMPLE OF A CIPHER CIP"
ALPHA = alphabet.upper()
encrypt = True
canon_alpha = True
ignore = " ,.!-_'?/><~][;:="
remove = ""
strict = " ,.!-_'?/><~][;:="

#------Setting functions------#

def set_crypt_dir(direction):
    global encrypt
    if direction.lower() == "decrypt" or not direction:
        encrypt = False
    else:
        encrypt = True

def set_canon_alpha(canon):
    global canon_alpha
    if canon == "ALPHA" or canon.lower() == "decrypt" or not canon:
        canon_alpha = False
    else:
        canon_alpha = True

def process_remove(string, taboo = remove):
    for c in taboo:
        string = string.replace(c, "")
    return string

def set_text(new):
    global text
    text = new.lower()
    text = process_remove(text)

def set_TEXT(NEW):
    global TEXT
    TEXT = NEW.upper()
    TEXT = process_remove(TEXT)


#------Analytic functions------#

def ignore_in(string):
    for x in ignore:
        if x in string:
            return True
    return False

def sort_by_canon():
    global alpha, ALPHA, canon_alpha
    if canon_alpha:
        a = 0
    else:
        a = 1
    holder = []
    length = min(len(alpha), len(ALPHA))
    for i in range(length):
        holder.append([alpha[i], ALPHA[i]])
    holder.sort(key=lambda seq: seq[a])
    alpha = ""
    ALPHA = ""
    for i in range(length):
        alpha += holder[i][0]
        ALPHA += holder[i][1]

def crib_find(crib):
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

def string_freq(length = 1, mincount = 1):
    global TEXT
    done = []
    result = []
    i = 0
    while i <= len(TEXT) - length:
        sub = TEXT[i:i + length]
        if not sub in done and not ignore_in(sub):
            if TEXT.count(sub) >= mincount:
                result.append([sub, TEXT.count(sub)])
            done.append(sub)
        i += 1
    result.sort(key=lambda seq: seq[0])
    result.sort(key=lambda seq: seq[1], reverse=True)
    return result

def find_repeat_factors():
    global TEXT
    diff_accu = []
    minlength = 3
    while string_freq(minlength, 2):
        print(minlength * 1000000)
        for i in string_freq(minlength, 2):
            pos_accu = []
            k = 0
            for j in range(i[1]):
                pos_accu.append(TEXT.find(i[0], k))
                print(TEXT.find(i[0], k))
                k = TEXT.find(i[0], k) + 1
            a = 0
            print(pos_accu)
            while a < len(pos_accu) - 1:
                b = a + 1
                while b < len(pos_accu):
                    diff_accu.append(pos_accu[b] - pos_accu[a])
        minlength += 1
    return diff_accu


#------Cryptographic functions------#

def substitute(text, sourceAlpha, targetAlpha):
    for i in range(len(sourceAlpha)):
        text = text.replace(sourceAlpha[i], targetAlpha[i])
    return text

def generate_caesar(shift, ALPHA = alphabet.upper()):
    SHIFTED = ""
    for i in range(len(ALPHA)):
        SHIFTED += ALPHA[(i + shift) % len(ALPHA)]
    return SHIFTED

def set_caesar(shift):
    global ALPHA
    ALPHA = generate_caesar(shift)

def set_atbash(shift = 0):
    global ALPHA
    HOLDER = generate_caesar(shift)
    ALPHA = ""
    for i in range(len(HOLDER)):
        ALPHA += HOLDER[len(HOLDER) - (i + 1)]

def set_keyword(KEY, ORIG = alphabet.upper()):
    global ALPHA
    KEY = KEY.upper()
    KEY = process_remove(KEY, strict)
    ALPHA = KEY + ORIG
    i = 0
    while i < len(ALPHA):
        if i > ALPHA.find(ALPHA[i]):
            ALPHA = ALPHA[:i] + ALPHA[(i + 1):]
        else:
            i += 1

def set_mono_ALPHA():
    global alpha, ALPHA
    print(alpha)
    ALPHA = input()

def do_mono_mono_sub():
    global encrypt, text, alphabet, TEXT, ALPHABET
    if encrypt:
        TEXT = substitute(text, alpha, ALPHA)
    else:
        text = substitute(TEXT, ALPHA, alpha)

def keyw_mono_poly_sub(a, keyword, direction):
    KEY = []
    keyword = process_remove(keyword, strict)
    for c in keyword:
        KEY.append(generate_caesar(alphabet.find(c.lower())))
    b = ""
    j = 0
    for i in range(len(a)):
        if not a[i] in ignore:
            if direction:
                b += KEY[j % len(KEY)][alphabet.find(a[i])]
            else:
                b += alphabet[KEY[j % len(KEY)].find(a[i])]
            j += 1
        else:
            b += a[i]
    return b

def do_vignere(keyword):
    global text, TEXT
    KEY = []
    keyword = process_remove(keyword, strict)
    for c in keyword:
        KEY.append(generate_caesar(alphabet.find(c.lower())))
    if encrypt:
        TEXT = keyw_mono_poly_sub(text, keyword, True)
    else:
        text = keyw_mono_poly_sub(TEXT, keyword, False)

def do_beaufort(keyword):
    global text, TEXT
    KEY = []
    keyword = process_remove(keyword, strict)
    for c in keyword:
        KEY.append(generate_caesar(alphabet.find(c.lower())))
    if encrypt:
        TEXT = keyw_mono_poly_sub(text, keyword, False).upper()
    else:
        text = keyw_mono_poly_sub(TEXT, keyword, True).lower()
