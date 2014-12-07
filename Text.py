
import math
from Grid import Grid

default_ignore = " ,.!-_'?/><~][;:="
default_remove = ""
default_strict = " ,.!-_'?/><~][;:="



class Text(object):
    '''Any piece of text you want to analyse, encrypt, or decrypt.
    '''
    def __init__(self, text = '', key = '',
                 ignore = default_ignore,
                 remove = default_remove,
                 strict = default_strict):
        self.text = text
        self.key = key

        self.ignore = ignore
        self.remove = remove
        self.strict = strict

    def copy(self):
        '''Return Type: Text
        Create a new instance of Text,
        with the same data as this instance.
        '''
        return Text(self.text,
                    self.key,
                    self.ignore,
                    self.remove,
                    self.strict)



    ## === Filter Functions === ##
    # These functions use the filters to be helpful to other functions

    def ignore_in(self, string):
        for x in self.ignore:
            if x in string:
                return True
        return False



    ## === Accessor Functions === ##
    # These are a collection of lenses which let you look at the text differently
    # Commonly used as helper functions

    def break_pattern(self, pattern):
        '''Return Type: Data/Text
        Returns a list, which is the text, but
        having been broken up according to the pattern specified
        '''

        result = []

        loc = 0
        n = 0
        while loc < len(self.text):
            step = pattern[n % len(pattern)]
            result.append(self.text[loc:loc + step])
            loc += step
            n += 1

        return result

    def grid(self, x, y = 0, pattern = [1]):
        '''Return Type: Grid
        Makes a grid, x by y, and enters the text into it.
        Can include a pattern, for making the grid complex.
        '''

        initial = self.break_pattern(pattern)
        result = []

        if y == 0:
            y = math.ceil(len(initial) / x)

        while len(initial) < x * y:
            initial.append('')

        for j in range(y):
            row = []
            for i in range(x):
                row.append(initial[j * x + i])
            result.append(row)

        return Grid(result)



    ## === CryptAnalytic Functions === ##
    # Common to all texts, use these to analyse what you have

    def match_pattern(self, pattern):
        '''Return Type: Data/Text
        Matches the pattern given to it,
        to see where in the text it could be.
        '''

        pattern = pattern.upper()

        result = []

        i = 0
        while i <= len(self.text) - len(pattern):
            match = True
            j = 0
            while j < len(pattern) and match == True:
                k = j + 1
                while k < len(pattern) and match == True:
                    if pattern[j] == pattern[k]:
                        if self.text[i + j] != self.text[i + k]:
                            match = False
                    else:
                        if self.text[i + j] == self.text[i + k]:
                            match = False
                    k += 1
                j += 1
            if match == True:
                result.append(self.text[i:i + len(pattern)])
            i += 1

        return result


    def string_freq(self, length = 1, mincount = 1):
        '''Return Type: Data
        Finds the number of repeated sequences of a certain length, 
        each with a minimum number of occurences, in the text.
        Calling without length or mincount arguments gives frequency analysis.
        '''

        done = []
        result = []

        i = 0
        while i <= len(self.text) - length:
            sub = self.text[i:i + length]

            if not sub in done and not self.ignore_in(sub):
                if self.text.count(sub) >= mincount:
                    result.append([sub, self.text.count(sub)])
                done.append(sub)

            i += 1

        result.sort(key=lambda seq: seq[0])
        result.sort(key=lambda seq: seq[1], reverse=True)

        return result


    def find_repeat_factors(self):
        '''Return Type: Data
        Searches the text for repeated sequences,
        then finds all the factors of the widths between them.
        '''
        
        diff_accu = []
        length = 3

        while self.string_freq(length, 2):
            for i in self.string_freq(length, 2, self.text):
                pos_accu = []

                k = 0
                for j in range(i[1]):
                    pos_accu.append(self.text.find(i[0], k))
                    k = self.text.find(i[0], k) + 1

                a = 0
                while a < len(pos_accu) - 1:
                    b = a + 1
                    while b < len(pos_accu):
                        diff_accu.append(pos_accu[b] - pos_accu[a])
                        b += 1
                    a += 1

            length += 1

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



    ## === Display Functions === ##
    # So that they can be understood in when programming

    def __repr__(self):
        return "'" + self.text + "'"

    def __str__(self):
        return self.text
