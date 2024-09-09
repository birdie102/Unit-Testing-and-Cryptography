# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha_lower = alpha.lower()


def caesar_encode(text, n):
    temp = ""
    if text.isdigit():
        return text
    for i in range(len(text)):
        letter = text[i]
        if letter in alpha_lower:
            index = alpha_lower.index(letter)
            if index >= len(alpha_lower) - n:
                temp += alpha_lower[n - 26 % index]
            else:
                temp += alpha_lower[index + n]

        elif letter in alpha:
            index = alpha.index(letter)
            if index >= len(alpha) - n:
                temp += alpha[n - 26 % index]
            else:
                temp += alpha[index + n]
        else:
            temp += letter




    return temp


def caesar_decode(text, n):
    temp = ""
    if text.isdigit():
        return text
    for i in range(len(text)):
        letter = text[i]
        if letter in alpha_lower:
            index = alpha_lower.index(letter)
            if index >= len(alpha_lower) + n:
                temp += alpha_lower[n + 26 % index]
            else:
                temp += alpha_lower[index - n]
        elif letter in alpha:
            index = alpha.index(letter)
            if index >= len(alpha) + n:
                temp += alpha[n + 26 % index]
            else:
                temp += alpha[index - n]
        else:
            temp += letter

    return temp


test = "HELLOWORLD"
shift = 5
enc = caesar_encode(test, shift)
dec = caesar_decode(enc, shift)
print(enc)
print(dec)
# If this worked, dec should be the same as test!
