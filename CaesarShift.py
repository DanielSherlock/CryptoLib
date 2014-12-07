
from SimpleSub import (simplesub,
                       SIMPLESUB,
                       default_alphabet,
                       default_ignore,
                       default_remove,
                       default_strict)

def shift_alphabet(alphabet, shift):
    '''Return Type: Data
    Shifts an alpahbet by a certain amount.
    Negative Shifts work too.
    '''
    result = ""
    for i in range(len(alphabet)):
        result += alphabet[(i + shift) % len(alphabet)]
    return result



class caesarshift(simplesub):
    '''A piece of text that will become a caesar shift cipher.
    '''
    def __init__(self, text = '', key = 0,
                 alphabet = default_alphabet.lower(),
                 ignore = default_ignore,
                 remove = default_remove,
                 strict = default_strict):
        super(caesarshift, self).__init__(text, key, alphabet,
                                          shift_alphabet(alphabet, key),
                                          ignore, remove, strict)


        
class CAESARSHIFT(SIMPLESUB):
    '''A piece of text that is an encrypted caesar shift cipher.
    '''
    def __init__(self, text = '', key = 0,
                 alphabet = default_alphabet.upper(),
                 ignore = default_ignore,
                 remove = default_remove,
                 strict = default_strict):
        super(CAESARSHIFT, self).__init__(text, key, alphabet,
                                          shift_alphabet(alphabet, -key),
                                          ignore, remove, strict)

