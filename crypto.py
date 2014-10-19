#!/usr/local/bin/python3.4

#------Variables------#

alphabet = "abcdefghijklmnopqrstuvwxyz"

text = "anyone can see... this"
alpha = alphabet.lower()
Key = "keyword"
TEXT = "Vvr Fstkh Pqbq cbq llg Jug eseg rvktwkigo kukqu oeu khx aheqbtwv, yyeg i hecjrdit tafm oyqbt ovcgpxl wa c knjq ecots.Hugm nyvgvd mpog vvr grg nhh nweuh fmgevewmr vp ancmpx tam hecjrdit kadm vvu qygem ffy avbwzq ti efnlqrrtsq kxtfnzmf gjoa llg ftamf.Gjsa llg Eokbv Jkbq tpgn al poef of zi efuel, phv huw qqie am pygk gzi ofrx kzbusyq hku tam hecjrdit woel vvu qygem rrhcbq jwz;srf rt eigg vvr Fstkh Pqbq ioiw yr khx ihggacl. Xjvn mps Fwb fzmpvd hch jcfzdc, ced buarfwnlinp tam hecjrdit kohs csh vvk gnfad.Ibq uc gzi Pfrmp Kvpr jsw qslbosq vc pgrhvsl bvnv huw Wwe wta hug ggjspxek wt gjs gos.vyil qg n xwtfitv".upper()#"CIPHERTEXT IS AN EXAMPLE OF A CIPHER"
ALPHA = alphabet.upper()

encrypt = True
canon_alpha = True

ignore = " ,.!-_'?/><~][;:="
remove = ""
strict = " ,.!-_'?/><~][;:="
key_empty_c = " "


#------Setting functions------#

def _set_crypt_dir(direction):
    global encrypt
    if direction.lower() == "decrypt" or not direction:
        encrypt = False
    else:
        encrypt = True

def _set_canon_alpha(canon):
    global canon_alpha
    if canon == "ALPHA" or canon.lower() == "decrypt" or not canon:
        canon_alpha = False
    else:
        canon_alpha = True

def _process_remove(string, taboo = remove, key = False):
    for c in taboo:
        if not key or not c == key_empty_c:
            string = string.replace(c, "")
    return string

def _set_text(new):
    global text
    text = new.lower()
    text = _process_remove(text)

def _set_TEXT(NEW):
    global TEXT
    TEXT = NEW.upper()
    TEXT = _process_remove(TEXT)


#------Analytic functions------#

def _ignore_in(string):
    for x in ignore:
        if x in string:
            return True
    return False

def _sort_by_canon():
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

def _crib_find(crib):
    global TEXT
    crib = crib.lower()
    crib = _process_remove(crib, strict)
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

def _string_freq(length = 1, mincount = 1):
    global TEXT
    done = []
    result = []
    i = 0
    while i <= len(TEXT) - length:
        sub = TEXT[i:i + length]
        if not sub in done and not _ignore_in(sub):
            if TEXT.count(sub) >= mincount:
                result.append([sub, TEXT.count(sub)])
            done.append(sub)
        i += 1
    result.sort(key=lambda seq: seq[0])
    result.sort(key=lambda seq: seq[1], reverse=True)
    return result

def _find_repeat_factors():
    global TEXT
    HOLDER = _process_remove(TEXT, strict)
    diff_accu = []
    minlength = 3
    while _string_freq(minlength, 2):
        for i in _string_freq(minlength, 2):
            pos_accu = []
            k = 0
            for j in range(i[1]):
                pos_accu.append(HOLDER.find(i[0], k))
                k = HOLDER.find(i[0], k) + 1
            a = 0
            while a < len(pos_accu) - 1:
                b = a + 1
                while b < len(pos_accu):
                    diff_accu.append(pos_accu[b] - pos_accu[a])
                    b += 1
                a += 1
        minlength += 1
    fact_accu = []
    for i in diff_accu:
        j = 2
        while j <= i:
            if i % j == 0:
                fact_accu.append(j)
            j += 1
    done = []
    result = []
    for i in fact_accu:
        if not i in done:
            result.append([i, fact_accu.count(i)])
            done.append(i)
    result.sort(key=lambda seq: seq[0])
    return result


#------Cryptographic functions------#

def _get_v_columns(string, columns):
    result = []
    for number in range(columns):
        count = number
        column = ""
        while count < len(string):
            column += string[count]
            count += columns
        result.append(column)
    return result

def _get_h_columns(string, columns):
    result = []
    count = 0
    while count < len(string):
        result.append(string[count:count + columns])
        count += columns
    return result

def _substitute(text, sourceAlpha, targetAlpha):
    for i in range(len(sourceAlpha)):
        text = text.replace(sourceAlpha[i], targetAlpha[i])
    return text

def _generate_caesar(shift, ALPHA = alphabet.upper()):
    SHIFTED = ""
    for i in range(len(ALPHA)):
        SHIFTED += ALPHA[(i + shift) % len(ALPHA)]
    return SHIFTED

def _set_caesar(shift):
    global ALPHA
    ALPHA = _generate_caesar(shift)

def _set_atbash(shift = 0):
    global ALPHA
    HOLDER = _generate_caesar(shift)
    ALPHA = ""
    for i in range(len(HOLDER)):
        ALPHA += HOLDER[len(HOLDER) - (i + 1)]

def _set_keyword_cipher(KEY = Key, ORIG = alphabet.upper()):
    global ALPHA
    KEY = KEY.upper()
    KEY = _process_remove(KEY, strict)
    ALPHA = KEY + ORIG
    i = 0
    while i < len(ALPHA):
        if i > ALPHA.find(ALPHA[i]):
            ALPHA = ALPHA[:i] + ALPHA[(i + 1):]
        else:
            i += 1

def _set_mono_ALPHA():
    global alpha, ALPHA
    print(alpha)
    ALPHA = input()

def _do_mono_mono_sub():
    global encrypt, text, alphabet, TEXT, ALPHABET
    if encrypt:
        TEXT = _substitute(text, alpha, ALPHA)
    else:
        text = _substitute(TEXT, ALPHA, alpha)

def _keyw_mono_poly_sub(a, direction, keyword = Key):
    KEY = []
    keyword = _process_remove(keyword, strict, True)
    for c in keyword:
        if not c == key_empty_c:
            KEY.append(_generate_caesar(alphabet.find(c.lower())))
        else:
            KEY.append(alphabet)
    b = ""
    j = 0
    for i in range(len(a)):
        if not a[i] in ignore:
            if direction:
                b += KEY[j % len(KEY)][alphabet.find(a[i])]
            elif KEY[j % len(KEY)][0].islower():
                b += a[i]
            else:
                b += alphabet[KEY[j % len(KEY)].find(a[i])]
            j += 1
        else:
            b += a[i]
    return b

def _do_vignere(keyword = Key):
    global text, TEXT
    if encrypt:
        TEXT = _keyw_mono_poly_sub(text, True, keyword)
    else:
        text = _keyw_mono_poly_sub(TEXT, False, keyword)

def _do_beaufort(keyword = Key):
    global text, TEXT
    if encrypt:
        TEXT = _keyw_mono_poly_sub(text, False, keyword).swapcase()
    else:
        text = _keyw_mono_poly_sub(TEXT, True, keyword).swapcase()


#------End-user CLI Functions------#

def hi():
    print("""
Hello, this is a useful crypto library,
written by Daniel Sherlock, in python!""")

def two_row_num_table(header1, header2, data):
    while len(header1) < len(header2):
        header1 += " "
    while len(header1) > len(header2):
        header2 += " "
    maxi = max(map(max, data))
    width = 1
    track = maxi / 10
    while track >= 1:
        track /= 10
        width += 1
    form = "{0:0>" + str(width) + "}"
    out = header1 + ":"
    for col in data:
        out += " | " + form.format(str(col[0]))
    out += "\n" + header2 + ":"
    for col in data:
        out += " | " + form.format(str(col[1]))
    print(out)

def show_repeat_factors():
    two_row_num_table("FACTORS", "REPEATS", _find_repeat_factors())

def solve_vignere():
    global encrypt, Key
    encrypt = False
    print("""
Choose a key length based on a common
factor of repeated sequence offset,
as calculated below:""")
    show_repeat_factors()
    key_length = int(input("Suspected key length: "))
    Key = " " * key_length
    done = False
    _do_vignere(Key)
    print(text)
    while not done:
        number = (int(input("Which letter of the key would you like to try? ")) - 1) % key_length
        Key = Key[:number] + input("What do you think it is? ") + Key[number + 1:]
        _do_vignere(Key)
        print(text)
        if input("Are you done? [Y/N]: ").lower() == "y":
            done = True
            
