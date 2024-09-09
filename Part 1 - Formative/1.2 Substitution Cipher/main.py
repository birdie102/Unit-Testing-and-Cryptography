# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def sub_encode(text, codebet):
    temp = ""
    if len(codebet) < len(alpha):
        return text
    for i in range(len(text)):
        for x in range(len(alpha)):
            if text[i] == alpha[x]:
                temp += codebet[x]
    return temp


def sub_decode(text, codebet):
    temp = ""
    for i in range(len(text)):
        for x in range(len(codebet)):
            if text[i] == codebet[x]:
                temp += alpha[x]
    return temp


test = "HELLOWORLD"
cipher_alphabet = "WJKUXVBMIYDTPLHZGONCRSAEFQ"
enc = sub_encode(test, cipher_alphabet)
dec = sub_decode(enc, cipher_alphabet)
print(enc)
print(dec)
# If this worked, dec should be the same as test!
