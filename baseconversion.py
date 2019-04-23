from string import ascii_lowercase
from string import ascii_uppercase
import string
from math import floor

# Converts to base 62
def base62(num, base=62):
    if base <= 0 or base > 62:
        return 0
    allCharacters = string.digits + ascii_lowercase + ascii_uppercase
    r = num % base
    res = allCharacters[r]
    q = floor(num / base)
    while q:
        r = q % base
        q = floor(q / base)
        res = allCharacters[int(r)] + res
    return res

# Converts to base 10
def base10(num, base=62):
    allCharacters = string.digits + ascii_lowercase + ascii_uppercase
    limit = len(num)
    res = 0
    for i in range(limit):
        res = base * res + allCharacters.find(num[i])
    return res