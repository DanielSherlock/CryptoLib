
from Substitution import (Substitution,
                          default_alphabet,
                          default_ignore,
                          default_remove,
                          default_strict)



class SimpleSub(Substitution):
    '''A piece of text that either is, or will become, a
    simple (monoalphabetic, monographic) substitution cipher.
    '''

    def sort_alphabet(self):
        pass



class simplesub(SimpleSub):
    '''A piece of text that will become a simple
    (monoalphabetic, monographic) substitution cipher.
    '''
    def __init__(self, plaintext = '', key = '',
                 plain_alphabet = default_alphabet.lower(),
                 cipher_alphabet = default_alphabet.upper(),
                 ignore = default_ignore,
                 remove = default_remove,
                 strict = default_strict):
        super(simplesub, self).__init__(plaintext.lower(), key,
                                        plain_alphabet.lower(),
                                        ignore, remove, strict)
        self.cipher_alphabet = cipher_alphabet.upper()
        self.update_alphabets()

    def update_alphabets(self):
        '''Return Type: MUTATES/None
        Updates the alphabets, according to the key.
        Also ensures that crypto-convention is followed.
        '''
        self.alphabet = self.alphabet.lower()
        self.cipher_alphabet = self.cipher_alphabet.upper()

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
                         self.remove,
                         self.strict)


        
class SIMPLESUB(SimpleSub):
    '''A piece of text that is an encrypted simple
    (monoalphabetic, monographic) substitution cipher.
    '''
    def __init__(self, ciphertext = '', key = '',
                 plain_alphabet = default_alphabet.lower(),
                 cipher_alphabet = default_alphabet.upper(),
                 ignore = default_ignore,
                 remove = default_remove,
                 strict = default_strict):
        super(SIMPLESUB, self).__init__(ciphertext.upper(), key,
                                        cipher_alphabet.upper(),
                                        ignore, remove, strict)
        self.plain_alphabet = plain_alphabet.lower()
        self.update_alphabets()

    def update_alphabets(self):
        '''Return Type: MUTATES/None
        Updates the alphabets, according to the key.
        Also ensures that crypto-convention is followed.
        '''
        self.plain_alphabet = self.plain_alphabet.lower()
        self.alphabet = self.alphabet.upper()

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
                         self.remove,
                         self.strict)