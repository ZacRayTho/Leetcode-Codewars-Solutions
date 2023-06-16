# Given a lowercase string that has alphabetic characters only and no spaces, return the highest value of consonant substrings. Consonants are any letters of the alphabet except "aeiou".

# We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.

import re
def solve(s):
    alpha = { "a": 1, "b":2, "c":3, "d":4, "e":5, "f": 6,
             "g": 7, "h":8, "i":9, "j":10, "k":11, "l": 12, 
             "m": 13, "n":14, "o":15, "p":16, "q":17, "r": 18, 
             "s": 19, "t":20, "u":21, "v":22, "w":23, "x": 24, "y":25, "z":26
            }
    high = 0
    current = 0
    for x in s:
        if re.search('[^aeiou]', x):
            current += alpha[x]
            if high < current:
                high = current
        else:
            current = 0
    return high
        