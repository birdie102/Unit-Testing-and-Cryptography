# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def caesar_encode(text, n):
    temp = ""
    for i in range(len(text)):
        for x in range(len(alpha)):
            if text[i] == alpha[x]:
                if x >= len(alpha) - n:
                    temp += alpha[n - 26 % x]
                else:
                    temp += alpha[x + n]

    return temp


def caesar_decode(text, n):
    temp = ""
    for i in range(len(text)):
        for x in range(len(alpha)):
            if text[i] == alpha[x]:
                if x >= len(alpha) + n:
                    temp += alpha[n + 26 % x]
                else:
                    temp += alpha[x - n]
    return temp


test = "HELLOWORLD"
shift = 5
enc = caesar_encode(test, shift)
dec = caesar_decode(enc, shift)
print(enc)
print(dec)
# If this worked, dec should be the same as test!
