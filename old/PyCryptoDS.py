#!/usr/local/bin/python3.4

    #------Variables------#

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    text = "anyone can see... this"
    alpha = alphabet.lower()
    Key = "keyword"
    TEXT = "CIPHERTEXT IS AN EXAMPLE OF A CIPHER"
    ALPHA = alphabet.upper()

    encrypt = True
    canon_alpha = True

    ignore = " ,.!-_'?/><~][;:="
    remove = ""
    strict = " ,.!-_'?/><~][;:="
    key_empty_c = " "


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

    def process_remove(string, taboo = remove, key = False):
        for c in taboo:
            if not key or not c == key_empty_c:
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
        crib = process_remove(crib, strict)
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

    def string_freq(length = 1, mincount = 1, TEXT = TEXT):
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
        HOLDER = process_remove(TEXT, strict)
        diff_accu = []
        minlength = 3
        while string_freq(minlength, 2):
            for i in string_freq(minlength, 2):
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

    def get_v_columns(string, columns):
        result = []
        for number in range(columns):
            count = number
            column = ""
            while count < len(string):
                column += string[count]
                count += columns
            result.append(column)
        return result

    def get_h_columns(string, columns):
        result = []
        columns = len(string) // columns
        count = 0
        while count < len(string):
            result.append(string[count:count + columns])
            count += columns
        return result

    def do_h_columnar(nKey):
        global text, TEXT
        TXT = process_remove(TEXT, strict)
        keyLen = len(nKey)
        if encrypt:
            print("Sorry, that is not yet coded!")
        else:
            cols = get_h_columns(TXT, keyLen)
            text = ""
            for i in range(len(TXT)):
                text += cols[nKey[i % keyLen]][i // keyLen]

    def x22_x12_mat_mul(x22, x12):
        return [(x22[0][0] * x12[0] + x22[0][1] * x12[1]) % 26,
                (x22[1][0] * x12[0] + x22[1][1] * x12[1]) % 26]

    def do_hill_2x2():
        if encrypt:
            print("Sorry, that is not yet coded!")
        else:
            l = []
            [l.extend(i) for i in
             [x22_x12_mat_mul(Key, p) for p in
              get_h_columns([ALPHA.index(c)
                             for c in TEXT], 2)]]
            return "".join([alpha[x] for x in l])

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

    def set_keyword_cipher(KEY = Key, ORIG = alphabet.upper()):
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

    def keyw_mono_poly_sub(a, direction, keyword = Key):
        KEY = []
        keyword = process_remove(keyword, strict, True)
        for c in keyword:
            if not c == key_empty_c:
                KEY.append(generate_caesar(alphabet.find(c.lower())))
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

    def do_vignere(keyword = Key):
        global text, TEXT
        if encrypt:
            TEXT = keyw_mono_poly_sub(text, True, keyword)
        else:
            text = keyw_mono_poly_sub(TEXT, False, keyword)

    def do_beaufort(keyword = Key):
        global text, TEXT
        if encrypt:
            TEXT = keyw_mono_poly_sub(text, False, keyword).swapcase()
        else:
            text = keyw_mono_poly_sub(TEXT, True, keyword).swapcase()


    #------End-user CLI Functions------#

    def hi():
        print("""
    Hello, this is a useful crypto library,
    written by Daniel Sherlock, in python!""")

    def show_freq_table(header, colw, data):
        maxv = 0
        widv = 0
        track = maxv = max(data, key=lambda seq: seq[1])[1]
        while track >= 1:
            track /= 10
            widv += 1
        formv = ["{0: >" + str(colw) + "}", "{0: >" + str(widv) + "}"]
        out = header.title() + ":\n"
        ratio = (80 - (colw + 3 + widv + 3)) * 2 / maxv
        for row in data:
            for i in range(2):
                out += "| " + formv[i].format(str(row[i])) + " "
            barlength = round(ratio * row[1])
            out += "=" * (barlength // 2)
            out += "-" * (barlength % 2)
            out += "\n"
        print(out)

    def show_num_freq_table(header, data):
        track = max(data, key=lambda seq: seq[0])[0]
        widv = 0
        while track >= 1:
            track /= 10
            widv += 1
        show_freq_table(header, widv, data)

    ##def two_row_num_table(header1, header2, data):
    ##    while len(header1) < len(header2):
    ##        header1 += " "
    ##    while len(header1) > len(header2):
    ##        header2 += " "
    ##    maxi = max(map(max, data))
    ##    width = 1
    ##    track = maxi / 10
    ##    while track >= 1:
    ##        track /= 10
    ##        width += 1
    ##    form = "{0:0>" + str(width) + "}"
    ##    out = header1 + ":"
    ##    for col in data:
    ##        out += " | " + form.format(str(col[0]))
    ##    out += "\n" + header2 + ":"
    ##    for col in data:
    ##        out += " | " + form.format(str(col[1]))
    ##    print(out)

    def show_repeat_factors():
        show_num_freq_table("repeating factor frequencies", find_repeat_factors())

    def show_freq_analysis(TEXT = TEXT):
        analysis = string_freq(TEXT = TEXT)
        analysis.sort(key=lambda seq: seq[0])
        show_freq_table("single-letter frequency analysis", 1, analysis)

    def analyse_vignere_key_letter(key_length):
        global Key, TEXT
        number = (int(input("""
    Which letter of the key would you like to analyse and guess?
    Key letter number:
      => """)) - 1) % key_length
        print("")
        show_freq_analysis(get_v_columns(process_remove(TEXT, ignore), key_length)[number])
        Key = Key[:number] + input("""
    Based on the frequencey analysis of this subsection of the cipher above,
    what letter of the alphabet do you think it is?
    (Hint: Which letter of this ciphertext section would code to 'a'?)
      => """) + Key[number + 1:]

    def guess_vignere_key():
        print("nothing here yet")

    def solve_vignere():
        global encrypt, Key
        encrypt = False
        show_repeat_factors()
        print("""Choose a key length based on a common factor of
    repeated sequence offset, as calculated above.""")
        key_length = int(input("""Suspected key length:
      => """))
        Key = " " * key_length
        done = False
        understood = True
        while not done or not understood:
            print("")
            if understood:
                do_vignere(Key)
                print("Current key: -" + Key + "-\nCurrent message:\n" + text)
            else:
                print("Sorry, did not understand, please try again.")
            option = input("""
    Do you want to:
     [1]: Analyse and guess a single letter of the key?
     [2]: Guess a larger part of the key?
     [3]: Finish?
     [4]: Restart?
      => """)
            if option == "1":
                understood = True
                analyse_vignere_key_letter(key_length)
            elif option == "2":
                understood = True
                guess_vignere_key()
            elif option == "3":
                understood = True
                done = True
            elif option == "4":
                solve_vignere()
                understood = True
                done = True
            else:
                understood = False

    #-------TEMP SET--------#


