# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha_lower = alpha.lower()


def sub_encode(text, codebet):
    """
    The text is encoded with a substitution alphabet
    :param text: The message being encoded
    :param codebet: the alphabet it is encoded with
    :return: encoded text
    """
    temp = ""
    if len(codebet) < len(alpha):
        return text
    for i in range(len(text)):
        letter = text[i]
        if letter in alpha:
            for x in range(len(alpha)):
                if text[i] == alpha[x]:
                    temp += codebet[x]
        elif letter in alpha_lower:
            for x in range(len(alpha_lower)):
                if text[i] == alpha_lower[x]:
                    temp += codebet.lower()[x]
        else:
            temp += text[i]
    return temp


def sub_decode(text, codebet):
    """
    The text is decoded with a substitution alphabet
    :param text: The encoded message that has to be decoded
    :param codebet: The alphabet that was used to encode text
    :return: The decoded text
    """
    temp = ""
    if len(codebet) < len(alpha):
        return text
    for i in range(len(text)):
        letter = text[i]
        if letter in codebet:
            for x in range(len(codebet)):
                if text[i] == codebet[x]:
                    temp += alpha[x]
        elif letter in codebet.lower():
            for x in range(len(codebet.lower())):
                if text[i] == codebet.lower()[x]:
                    temp += alpha_lower[x]
        else:
            temp += text[i]

    return temp


test = "HELLOWORLD"
cipher_alphabet = "WJKUXVBMIYDTPLHZGONCRSAEFQ"
enc = sub_encode(test, cipher_alphabet)
dec = sub_decode(enc, cipher_alphabet)
print(enc)
print(dec)
# If this worked, dec should be the same as test!
