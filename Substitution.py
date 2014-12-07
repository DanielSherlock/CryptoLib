
import copy
from Text import (Text,
                  default_ignore,
                  default_remove)

default_alphabet = 'abcdefghijklmnopqrstuvwxyz'



class Substitution(Text):
    '''A piece of text that is, or will become,
    some kind of substitution cipher.
    '''
    def __init__(self, text = '', key = '',
                 alphabet = default_alphabet,
                 ignore = default_ignore,
                 remove = default_remove):
        super(Substitution, self).__init__(text, key,
                                           ignore, remove)
        self.alphabet = self.do_remove(alphabet)

    def substitute(self, new_alphabet):
        '''Return Type: Text
        Substitutes each letter from the current Text's
        alphabet with the new alphabet, to get a new Text.
        Warning: Errors may occur if alphabets share characters!
        '''
        new = copy.deepcopy(self)
        new.alphabet = self.do_remove(new_alphabet)
        for i in range(min(len(self.alphabet), len(new.alphabet))):
            new.text = new.text.replace(self.alphabet[i], new.alphabet[i])
        return new
