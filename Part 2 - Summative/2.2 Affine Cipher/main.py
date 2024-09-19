import math

# Read the instructions to see what to do!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# PART 1
# These functions are provided for you!
def mod_inverse_helper(a, b):
    q, r = a//b, a%b
    if r == 1:
        return (1, -1 * q)
    u, v = mod_inverse_helper(b, r)
    return (v, -1 * q * v + u)

def mod_inverse(a, m):
    assert math.gcd(a, m) == 1, "You're trying to invert " + str(a) + " in mod " + str(m) + " and that doesn't work!"
    return mod_inverse_helper(m, a)[1] % m


# These are the functions you'll need to write:
def affine_encode(text, a, b):
    temp = ""
    for i in range(len(text)):
        letter = text[i]
        if letter in alpha:
            index = (a * alpha.index(letter) + b) % 26
            temp += alpha[index]
    return temp

def affine_decode(text, a, b):
    temp = ""
    for i in range(len(text)):
        letter = text[i]
        if letter in alpha:
            index = ((alpha.index(letter) - b) * mod_inverse(a, 26)) % 26
            temp += alpha[index]
    return temp

test = "HELLOWORLD"
a = 3
b = 9
enc = affine_encode(test, a, b)
dec = affine_decode(enc, a, b)
print(enc)
print(dec)
# If this worked, dec should be the same as test!



# PART 2
# These  are the functions you'll need to write:
def convert_to_num(ngram):
    temp = 0
    for i in range(len(ngram)):
        letter = ngram[i]
        if letter in alpha:
            index = 26 ** i * alpha.index(letter)
            temp += index
    return temp


def convert_to_text(num, n):
    temp = ""
    for i in range(n):
        number = int(num % 26)
        temp += alpha[number]
        num = num // 26
    return temp



test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
l = len(test)
num = convert_to_num(test)
answer = convert_to_text(num, l)
print(num)
print(answer)
# If this worked, answer should be the same as test!



# PART 3

# These are the functions you'll need to write:
def affine_n_encode(text, n, a, b):
    temp = ""
    num = 0
    if (len(text) % n > 0):
        for i in range(len(text) % n + 1):
            text += "X"
    while num < len(text):
        letters = text[num: num + n]
        nums = convert_to_num(letters)
        nums = (a * nums + b) % (26 ** n)
        temp += convert_to_text(nums, n)
        num += n
    return temp

def affine_n_decode(text, n, a, b):
    temp = ""
    num = 0
    while num < len(text):
        letters = text[num: num + n]
        nums = convert_to_num(letters)
        nums = (nums - b) * mod_inverse(a, (26 ** n)) % (26 ** n)
        temp += convert_to_text(nums, n)
        num += n
    return temp


test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
n = 5
a = 347
b = 1721
enc = affine_n_encode(test, n, a, b)
dec = affine_n_decode(enc, n, a, b)
print(enc, dec)
# If this worked, dec should be the same as test!