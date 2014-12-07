
from SimpleSub import (SimpleSub,
                       simplesub,
                       SIMPLESUB,
                       default_alphabet,
                       default_ignore,
                       default_remove)



class KeywordSub(SimpleSub):
    '''Generic, Keyword-substitution-cipher-related, piece of text
    '''
    
    def keyword_alphabet(self, alphabet, keyword):
        '''Return Type: Data
        Adds the keyword given to it to the front of the alphabet.
        '''
        result = keyword.upper() + alphabet.upper()
        i = 0
        while i < len(result):
            if i > result.find(result[i]):
                result = result[:i] + result[(i + 1):]
            else:
                i += 1
        return result



class keywordsub(simplesub, KeywordSub):
    '''A piece of text that will become a keyword substitution cipher.
    '''
    def __init__(self, plaintext = '', key = '',
                 alphabet = default_alphabet.lower(),
                 ignore = default_ignore,
                 remove = default_remove):
        super(keywordsub, self).__init__(plaintext, key,
                                         alphabet, alphabet,
                                         ignore, remove)

    def update_alphabets(self):
        '''Return Type: MUTATES/None
        Updates the alphabets, according to the key.
        Also ensures that crypto-convention is followed.
        '''
        self.alphabet = self.alphabet.lower()
        self.cipher_alphabet = self.keyword_alphabet(self.alphabet, self.key).upper()


        
class KEYWORDSUB(SIMPLESUB, KeywordSub):
    '''A piece of text that is an encrypted keyword substitution cipher.
    '''
    def __init__(self, ciphertext = '', key = '',
                 alphabet = default_alphabet.upper(),
                 ignore = default_ignore,
                 remove = default_remove):
        super(KEYWORDSUB, self).__init__(ciphertext, key,
                                         alphabet, alphabet,
                                         ignore, remove)

    def update_alphabets(self):
        '''Return Type: MUTATES/None
        Updates the alphabets, according to the key.
        Also ensures that crypto-convention is followed.
        '''
        self.plain_alphabet = self.plain_alphabet.lower()
        self.alphabet = self.keyword_alphabet(self.plain_alphabet, self.key).upper()

