
from SimpleSub import (SimpleSub,
                       simplesub,
                       SIMPLESUB,

                       default_alphabet,
                       default_ignore,
                       default_remove)



class Atbash(SimpleSub):
    '''Generic, Atbash-cipher-related, piece of text
    '''

    def reverse_alphabet(self, alphabet):
        '''Return Type: Data
        Returns own alphabet, reversed.
        '''
        result = ""
        for i in range(len(alphabet)):
            result += alphabet[- (i + 1)]
        return result



class atbash(simplesub, Atbash):
    '''A piece of text that will become an atbash cipher.
    '''
    def __init__(self, plaintext = '', key = False,
                 alphabet = default_alphabet.lower(),
                 ignore = default_ignore,
                 remove = default_remove):
        super(atbash, self).__init__(plaintext, key,
                                     alphabet, alphabet,
                                     ignore, remove,)

    def update_alphabets(self):
        '''Return Type: MUTATES/None
        Updates the alphabets, according to the key.
        Also ensures that crypto-convention is followed.
        '''
        self.alphabet = self.do_remove(self.alphabet.lower())
        self.cipher_alphabet = self.reverse_alphabet(self.alphabet).upper()


        
class ATBASH(SIMPLESUB, Atbash):
    '''A piece of text that is an encrypted atbash cipher.
    '''
    def __init__(self, ciphertext = '', key = False,
                 alphabet = default_alphabet.lower(),
                 ignore = default_ignore,
                 remove = default_remove):
        super(ATBASH, self).__init__(ciphertext, key,
                                     alphabet, alphabet,
                                     ignore, remove)

    def update_alphabets(self):
        '''Return Type: MUTATES/None
        Updates the alphabets, according to the key.
        Also ensures that crypto-convention is followed.
        '''
        self.plain_alphabet = self.do_remove(self.plain_alphabet.lower())
        self.alphabet = self.reverse_alphabet(self.plain_alphabet).upper()

