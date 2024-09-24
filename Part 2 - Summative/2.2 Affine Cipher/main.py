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
    """
    Encodes a string using Affine Cipher.
    :param text: is the code that you want to encode
    :param a: mutiplyed by index letter is at in alphabetical order
    :param b: added to the mutplied index and a value
    :return: encoded text using affine cipher
    """
    text = text.upper()
    temp = ""
    for i in range(len(text)):
        letter = text[i]
        if letter in alpha:
            index = (a * alpha.index(letter) + b) % 26
            temp += alpha[index]
    return temp

def affine_decode(text, a, b):
    """
    Decodes a string using Affine Cipher.
    :param text: The encoded text that you want to decode
    :param a: What the text index has to be mod inversed by
    :param b: what is subtracted from the index vaule of the encoded letter
    :return: the decoded text using affine cipher
    """
    text = text.upper()
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
    """
    Converts a message into a number.
    :param ngram: the message being encoded
    :return: the numbers that are an encode version of ngram
    """
    temp = 0
    for i in range(len(ngram)):
        letter = ngram[i]
        if letter in alpha:
            index = 26 ** i * alpha.index(letter)
            temp += index
    return temp


def convert_to_text(num, n):
    """
    Converts a number to a string.
    :param num: The number being converted to a string
    :param n: The length of the orginal string that num is being converted to
    :return: Num converted to a string
    """
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
    """
    Encodes a string using Affine Cipher and numbers.
    :param text: The text being encoded
    :param n: ngrams
    :param a: what the text index is multiplyied by
    :param b: What the text index is getting added by
    :return: The encoded message as a string
    """
    temp = ""
    num = 0
    text = text.upper()
    while (len(text) % n != 0):
        text += "X"
    while num < len(text):
        if text[num] in alpha:
            letters = text[num: num + n]
            nums = convert_to_num(letters)
            nums = (a * nums + b) % (26 ** n)
            temp += convert_to_text(nums, n)
            num += n
    return temp

def affine_n_decode(text, n, a, b):
    """
    Decodes a string using Affine Cipher and numbers.
    :param text: the encoded message as a string
    :param n: ngrams
    :param a: The number the index of text[i] is mod inversed by
    :param b: the number the index of text[i] is getting subtracted by
    :return: The decoded message as a string
    """
    temp = ""
    num = 0
    while num < len(text):
        letters = text[num: num + n]
        nums = convert_to_num(letters)
        nums = (nums - b) * mod_inverse(a, (26 ** n)) % (26 ** n)
        temp += convert_to_text(nums, n)
        num += n
    return temp


test = "COOL"
n = 3
a = 3
b = 121
enc = affine_n_encode(test, n, a, b)
dec = affine_n_decode(enc, n, a, b)
print(enc, dec)
# If this worked, dec should be the same as test!