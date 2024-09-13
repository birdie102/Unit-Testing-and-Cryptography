# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha_lower = alpha.lower()


def caesar_encode(text, n):
    """
    Encodes text to be encrypted using Caesar Cipher.
    :param text: phrase that needs to be encoded
    :param n: Number the phrase shifts in the alphabet
    :return: encoded text phrase
    """
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
    """
    Decodes text to be decrypted using Caesar Cipher.
    :param text: encoded phrase
    :param n: 
    :return:
    """
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
