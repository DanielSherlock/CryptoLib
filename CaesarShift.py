
from SimpleSub import (SimpleSub,
                       simplesub,
                       SIMPLESUB,
                       
                       default_alphabet,
                       default_ignore,
                       default_remove)



class Caesar(SimpleSub):
    '''Generic, Caesar-shift-cipher-related, piece of text
    '''
    
    def shift_alphabet(self, alphabet, shift):
        '''Return Type: Data
        Shifts an alphabet by a certain amount.
        Negative Shifts work too.
        '''
        result = ""
        for i in range(len(alphabet)):
            result += alphabet[(i + shift) % len(alphabet)]
        return result



class caesarshift(simplesub, Caesar):
    '''A piece of text that will become a caesar shift cipher.
    '''
    def __init__(self, plaintext = '', key = 0,
                 alphabet = default_alphabet.lower(),
                 ignore = default_ignore,
                 remove = default_remove):
        super(caesarshift, self).__init__(plaintext, key,
                                          alphabet, alphabet,
                                          ignore, remove)

    def update_alphabets(self):
        '''Return Type: MUTATES/None
        Updates the alphabets, according to the key.
        Also ensures that crypto-convention is followed.
        '''
        self.alphabet = self.do_remove(self.alphabet.lower())
        self.cipher_alphabet = self.shift_alphabet(self.alphabet, self.key).upper()


        
class CAESARSHIFT(SIMPLESUB, Caesar):
    '''A piece of text that is an encrypted caesar shift cipher.
    '''
    def __init__(self, ciphertext = '', key = 0,
                 alphabet = default_alphabet.upper(),
                 ignore = default_ignore,
                 remove = default_remove):
        super(CAESARSHIFT, self).__init__(ciphertext, key,
                                          alphabet, alphabet,
                                          ignore, remove)

    def update_alphabets(self):
        '''Return Type: MUTATES/None
        Updates the alphabets, according to the key.
        Also ensures that crypto-convention is followed.
        '''
        self.plain_alphabet = self.do_remove(self.plain_alphabet.lower())
        self.alphabet = self.shift_alphabet(self.plain_alphabet, self.key).upper()

