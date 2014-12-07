
from Substitution import (Substitution,
                          default_alphabet,
                          default_ignore,
                          default_remove,
                          default_strict)



class simplesub(Substitution):
    '''A piece of text that will become a simple
    (monoalphabetic, monographic) substitution cipher.
    '''
    def __init__(self, text = '', key = '',
                 plain_alphabet = default_alphabet.lower(),
                 cipher_alphabet = default_alphabet.upper(),
                 ignore = default_ignore,
                 remove = default_remove,
                 strict = default_strict):
        super(simplesub, self).__init__(text.lower(), key,
                                        plain_alphabet.lower(),
                                        ignore, remove, strict)
        self.cipher_alphabet = cipher_alphabet.upper()

    def encrypt(self):
        '''Return Type: Text
        Encrypts this cipher.
        '''
        return SIMPLESUB(self.substitute(self.cipher_alphabet).text,
                         self.key,
                         self.alphabet,
                         self.cipher_alphabet,
                         self.ignore,
                         self.remove,
                         self.strict)


        
class SIMPLESUB(Substitution):
    '''A piece of text that is an encrypted simple
    (monoalphabetic, monographic) substitution cipher.
    '''
    def __init__(self, text = '', key = '',
                 plain_alphabet = default_alphabet.lower(),
                 cipher_alphabet = default_alphabet.upper(),
                 ignore = default_ignore,
                 remove = default_remove,
                 strict = default_strict):
        super(SIMPLESUB, self).__init__(text.upper(), key,
                                        cipher_alphabet.upper(),
                                        ignore, remove, strict)
        self.plain_alphabet = plain_alphabet.lower()

    def decrypt(self):
        '''Return Type: Text
        Decrypts this cipher.
        '''
        return simplesub(self.substitute(self.plain_alphabet).text,
                         self.key,
                         self.plain_alphabet,
                         self.alphabet,
                         self.ignore,
                         self.remove,
                         self.strict)
