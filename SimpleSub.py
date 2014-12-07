
from Substitution import (Substitution,
                          default_alphabet,
                          default_ignore,
                          default_remove)



class SimpleSub(Substitution):
    '''A piece of text that either is, or will become, a
    simple (monoalphabetic, monographic) substitution cipher.
    '''

    def sort_alphabets(self, alphabet1, alphabet2):
        '''Return Type: Data
        Sorts both alphabets together,
        such that alphabet1 is put into order.
        Used to reveal hard-to-spot patterns.
        '''
        holder = []
        length = min(len(alphabet1), len(alphabet2))
        for i in range(length):
            holder.append([alphabet1[i], alphabet2[i]])
        holder.sort(key=lambda seq: seq[0])
        alphabet1 = ""
        alphabet2 = ""
        for i in range(length):
            alphabet1 += holder[i][0]
            alphabet2 += holder[i][1]
        return [alphabet1, alphabet2]



class simplesub(SimpleSub):
    '''A piece of text that will become a simple
    (monoalphabetic, monographic) substitution cipher.
    '''
    def __init__(self, plaintext = '', key = '',
                 plain_alphabet = default_alphabet.lower(),
                 cipher_alphabet = default_alphabet.upper(),
                 ignore = default_ignore,
                 remove = default_remove):
        super(simplesub, self).__init__(plaintext.lower(), key,
                                        plain_alphabet.lower(),
                                        ignore, remove)
        self.cipher_alphabet = self.do_remove(cipher_alphabet.upper())
        self.update_alphabets()

    def update_alphabets(self):
        '''Return Type: MUTATES/None
        Updates the alphabets, according to the key.
        Also ensures that crypto-convention is followed.
        '''
        self.alphabet = self.do_remove(self.alphabet.lower())
        self.cipher_alphabet = self.do_remove(self.cipher_alphabet.upper())

    def encrypt(self):
        '''Return Type: Text
        Encrypts this cipher.
        '''
        self.update_alphabets()
        return SIMPLESUB(self.substitute(self.cipher_alphabet).text,
                         self.key,
                         self.alphabet,
                         self.cipher_alphabet,
                         self.ignore,
                         self.remove)


        
class SIMPLESUB(SimpleSub):
    '''A piece of text that is an encrypted simple
    (monoalphabetic, monographic) substitution cipher.
    '''
    def __init__(self, ciphertext = '', key = '',
                 plain_alphabet = default_alphabet.lower(),
                 cipher_alphabet = default_alphabet.upper(),
                 ignore = default_ignore,
                 remove = default_remove):
        super(SIMPLESUB, self).__init__(ciphertext.upper(), key,
                                        cipher_alphabet.upper(),
                                        ignore, remove)
        self.plain_alphabet = self.do_remove(plain_alphabet.lower())
        self.update_alphabets()

    def update_alphabets(self):
        '''Return Type: MUTATES/None
        Updates the alphabets, according to the key.
        Also ensures that crypto-convention is followed.
        '''
        self.plain_alphabet = self.do_remove(self.plain_alphabet.lower())
        self.alphabet = self.do_remove(self.alphabet.upper())

    def decrypt(self):
        '''Return Type: Text
        Decrypts this cipher.
        '''
        self.update_alphabets()
        return simplesub(self.substitute(self.plain_alphabet).text,
                         self.key,
                         self.plain_alphabet,
                         self.alphabet,
                         self.ignore,
                         self.remove)
