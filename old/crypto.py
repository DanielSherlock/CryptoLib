#!/usr/local/bin/python3.4

class _analysis (object):
    def __init__(self, text):
        self.analysis_text = text

    def match_pattern(self, crib):
        'matches the pattern given to it, in the text
        crib = crib.upper()
        #crib = process_remove(crib, strict)
        result = []
        i = 0
        while i <= len(self.text) - len(crib):
            match = True
            j = 0
            while j < len(crib) and match == True:
                k = j + 1
                while k < len(crib) and match == True:
                    if crib[j] == crib[k]:
                        if self.analysis_text[i + j] != self.analysis_text[i + k]:
                            match = False
                    else:
                        if self.analysis_text[i + j] == self.analysis_text[i + k]:
                            match = False
                    k += 1
                j += 1
            if match == True:
                result.append(self.analysis_text[i:i + len(crib)])
            i += 1
        return result

class cipher (cipher_analysis):
    def __init__(self,
                 plaintext = '',
                 ciphertext = '',
                 crypt_dir = ''):
        
        self.key = ''
        self.plaintext = plaintext
        self.ciphertext = ciphertext
        
        if crypt_dir != '':
            self.crypt_dir = crypt_dir
        else:
            if plaintext == '':
                self.crypt_dir = '<decrypt>'
            elif ciphertext == '':
                self.crypt_dir = '<encrypt>'

        if self.crypt_dir == '<encrypt>':
            _analysis.__init__(self.plaintext)
        elif self.crypt_dir == '<decrypt>':
            _analysis.__init__(self.ciphertext)

    

